# Hermes Kanban / Dispatcher — Verified Reference

**Purpose:** the load-bearing facts the research scheduler is built from.
**Discipline:** every entry is tagged. Build only on **[CONFIRMED]**.

- **[CONFIRMED]** — pasted verbatim from `--help`, `cat` of a real file, or
  observed behavior. Ground truth.
- **[UNVERIFIED]** — plausible but not yet checked. Do not build on it.
- **[CONFABULATED]** — a model asserted it; checking disproved it OR it was
  flagged "inferred." Recorded so we don't re-adopt it by accident.

**Last updated:** 2026-06-07 (config.yaml + `kanban --help` folded in)

---

## 1. `hermes kanban create` flags — [CONFIRMED] (verbatim `--help`)

```
usage: hermes kanban create [-h] [--body BODY] [--assignee ASSIGNEE]
                            [--parent PARENT] [--workspace WORKSPACE]
                            [--branch BRANCH] [--tenant TENANT]
                            [--priority PRIORITY] [--triage]
                            [--idempotency-key IDEMPOTENCY_KEY]
                            [--max-runtime MAX_RUNTIME]
                            [--created-by CREATED_BY] [--skill SKILLS]
                            [--max-retries N] [--goal] [--goal-max-turns N]
                            [--initial-status {blocked,running}] [--json]
                            title
```

Key fields for the scheduler:

- **`title`** (positional) — task title.
- **`--body`** — opening post / instructions.
- **`--assignee`** — profile name to assign. **(This is the routing lever — see
  §4 GPU-serial strategy.)**
- **`--parent`** (repeatable) — parent task id. **Native dependency gating** =
  the "what does this unblock" mechanism. Use to enforce order.
- **`--workspace`** — `scratch | worktree | worktree:<path> | dir:<path>`
  (default `scratch`).
- **`--priority`** — described verbatim as **"Priority tiebreaker."** **NOTE the
  wording: "tiebreaker," not "primary sort key."** This matters for the
  re-sorter design — see §5 open question Q3.
- **`--max-runtime`** — per-task runtime cap. Accepts `300` (s) or `90s/30m/2h/1d`.
  **"When exceeded, the dispatcher SIGTERMs (then SIGKILLs) the worker and
  re-queues the task."** → native graceful-then-forced kill + requeue. This is
  the cooperative-halting budget, built into the dispatcher.
- **`--max-retries N`** — per-task override for the **consecutive-failure
  circuit breaker.** `--max-retries 1` = block on first failure (no retries).
  Omit → uses dispatcher's `kanban.failure_limit` config (**default 2** per help
  text).
- **`--skill`** (repeatable) — force-load a skill into the worker; appended to
  the built-in `kanban-worker` skill.
- **`--triage`** — park in triage; a specifier fleshes out the spec and promotes
  to todo.
- **`--goal`** + **`--goal-max-turns N`** (default 20) — goal loop: a judge
  checks each turn against title/body; worker continues until judge agrees or
  turn budget exhausts (then blocks for review). Best for open-ended cards.
- **`--initial-status {blocked,running}`** — `blocked` for cards needing
  immediate human ops (an "R3 gate").
- **`--idempotency-key`** — dedup; returns existing task id instead of
  duplicating.
- **`--json`** — JSON output.

---

## 2. `hermes profile` verbs — [CONFIRMED] (verbatim `--help`)

```
{list, use, create, delete, describe, show, alias, rename,
 export, import, install, update, info}
```

- **`describe`** — "Read or set a profile's description **(used by the kanban
  orchestrator)**." → the orchestrator reads profile descriptions; this is how
  a profile's *role* is communicated to routing. Likely relevant to GPU-serial
  routing.
- **`use`** — set sticky default profile.
- `create / delete / show / rename / alias / export / import / install /
  update / info` — as named.

**NOTE:** there is **NO** `profile config set ... max_concurrent` subcommand in
this verb list. See §6 [CONFABULATED].

---

## 3. Card schema (core fields) — [CONFIRMED via create flags] + [UNVERIFIED extras]

**[CONFIRMED]** (because they're real `create` flags): `title`, `body`,
`assignee`, `parent`(s), `workspace`, `branch`, `tenant`, `priority`,
`max-runtime`, `max-retries`, `skill`(s), `goal`/`goal-max-turns`,
`initial-status`, `idempotency-key`.

**[UNVERIFIED]** (claimed in an earlier qwen summary, not seen in `--help`):
`goal_mode` (vs the real `--goal`), a generic `metadata={...}` dict, and a
`metadata.priority` nested field. The real surface uses **flags**, not a
metadata dict — until proven otherwise, assume **no arbitrary `metadata`
field exists.**

---

## 4. GPU-serial strategy — current best plan (mix of [CONFIRMED] + [OPEN])

**Goal:** the 16GB 5070 Ti runs **at most one heavy GPU job at a time**, while
light CPU jobs run in parallel.

**Plan (pending the §5 concurrency check):**
- Route all GPU-heavy cards to a **dedicated profile** (e.g. `gpu`) via
  `--assignee gpu`. [mechanism CONFIRMED: `--assignee` is real]
- **IF** the dispatcher serializes within a profile (one worker per profile at
  a time), a dedicated gpu profile gives serial GPU execution **for free**,
  with no resource-limit field needed. [**behavior UNVERIFIED — this is the
  load-bearing open question, see §5 Q1**]
- Light/CPU cards → a *different* profile → run in parallel.
- Use `--parent` to gate any card that must wait on a GPU result.
- Use `--max-runtime` as the per-card hard budget (native SIGTERM→SIGKILL→
  requeue). Belt-and-suspenders with the `run_sweep.py` stop-sentinel.

---

## 5. RESOLVED — dispatcher, concurrency, verbs (all [CONFIRMED] from config.yaml + `kanban --help`)

### 5.1 Concurrency — Q1 RESOLVED ✅ (the load-bearing answer)

Real `kanban:` config block (verbatim from `~/.hermes/config.yaml`):

```yaml
kanban:
  dispatch_in_gateway: true
  dispatch_interval_seconds: 60
  failure_limit: 2
  worker_log_rotate_bytes: 2097152
  worker_log_backup_count: 1
  orchestrator_profile: ''
  default_assignee: ''
  max_in_progress_per_profile: null      # ← THE GPU-SERIAL LEVER
  auto_decompose: true
  auto_decompose_per_tick: 3
  dispatch_stale_timeout_seconds: 14400
```

- **`max_in_progress_per_profile`** is the real per-profile concurrency cap.
  Currently `null` (unlimited). **Set a dedicated `gpu` profile's cap to 1 →
  the dispatcher guarantees ONE GPU job at a time, while other profiles run in
  parallel.** This confirms the "dedicated gpu profile = serial GPU for free"
  strategy (§4). **[CONFIRMED — field exists; exact set-syntax still to verify,
  see §5.4]**
- **`delegation.max_concurrent_children: 3`** (from the `delegation:` block) is
  the real source of "3 concurrent subagents." Global default = 3; per-profile
  caps layer on top.

### 5.2 The dispatcher IS the gateway — Q2 RESOLVED ✅

- `dispatch_in_gateway: true`, `dispatch_interval_seconds: 60` → **the
  dispatcher runs inside the gateway and ticks every 60s.** "The scheduler" is
  not something to build — it's `hermes gateway start`.
- `kanban dispatch` verb = one manual pass: *"reclaim stale, promote ready,
  spawn workers."*
- `kanban daemon` verb = **DEPRECATED** ("dispatcher now runs in the gateway").
- `dispatch_stale_timeout_seconds: 14400` (4h) — stale-claim reclaim window.

### 5.3 Selection order — Q3 partial

`--priority` is a **"tiebreaker"** (confirmed §1). The full selection order
isn't spelled out in config, but the dispatch pass is "promote ready → spawn
workers," and `claim` is *atomic on ready tasks*. Ready-ness is gated by
`--parent` dependencies and status. **Working model:** dependencies + status
gate readiness; among ready cards, priority breaks ties. The "brain re-sorts by
editing priority" design still works for **tiebreak-level** ordering; if a
stronger primary reorder is needed, use parent links / block/unblock /
promote. **[CONFIRMED mechanism; exact multi-key sort still [UNVERIFIED]]**

### 5.4 Full verb list — Q4 RESOLVED ✅ (verbatim `kanban --help`)

```
init, boards, create, swarm, list/ls, show, assign, reclaim, reassign,
diagnostics/diag, link, unlink, claim, comment, complete, edit, block,
schedule, unblock, promote, archive, tail, dispatch, daemon(DEPRECATED),
watch, stats, notify-subscribe, notify-list, notify-unsubscribe, log, runs,
heartbeat, assignees, context, specify, decompose, gc
```

Highlights relevant to the scheduler:

- **`init`** — "Create kanban.db if missing (idempotent)." First command to run.
- **`boards`** — one board per project/workstream. Board slug via
  `boards switch` or `HERMES_KANBAN_BOARD` env var. → **separate boards per
  BOBA trajectory** (JEPA, probe-set, Elder-Angels, corpus).
- **`swarm`** — native **"parallel workers → verifier → synthesizer"** graph.
  Relevant for probe-set work fanned across multiple models.
- **`link`/`unlink`** — add/remove parent→child dependency (the real dependency
  API).
- **`claim`** — "atomically claim a ready task (prints resolved workspace
  path)." The serialization enforcement point.
- **`specify`** — flesh out a triage card into a concrete spec via
  `auxiliary.triage_specifier`. (The "brain drafts the spec" layer.)
- **`decompose`** — fan a triage card into child tasks routed to specialist
  profiles by description, via `auxiliary.kanban_decomposer`.
- **Legibility verbs:** `tail` (follow event stream), `watch` (live all events),
  `log` (worker log from `<kanban-root>/kanban/logs/`), `runs` (attempt history),
  `heartbeat` (worker liveness), `stats` (per-status/assignee + oldest-ready
  age), `context` (full context a worker sees). **The legibility layer we
  hand-built into run_sweep.py is native here.**
- **`gc`** — garbage-collect archived workspaces/events/logs.

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
and `docs/hermes-kanban-v1-spec.pdf`.

### 5.5 Remaining small unknowns

- **[UNVERIFIED]** exact syntax to set `max_in_progress_per_profile` for one
  profile (is it a global config key, or per-profile via
  `~/.hermes/profiles/<name>/config.yaml`?). Check: `cat
  ~/.hermes/profiles/<name>/config.yaml` after `profile create`, or
  `hermes kanban create --help` had no such flag, so it's a **config**, not a
  per-card setting.
- **[UNVERIFIED]** precise multi-key ready-task sort order (§5.3).

---

## 5A. Approvals & autonomy posture — [CONFIRMED]

From config.yaml:

```yaml
approvals:
  mode: manual
  timeout: 60
  cron_mode: deny
delegation:
  subagent_auto_approve: false
  max_concurrent_children: 3
  orchestrator_enabled: true
cron:
  max_parallel_jobs: null
```

- **`approvals.mode: manual`** and **`cron_mode: deny`** — the deliberate gates
  are real and active. Good.
- **`subagent_auto_approve: false`** — **IMPORTANT for unattended runs:** the
  dispatcher spawning workers may require per-spawn approval. **Pin down exactly
  when it prompts before trusting an overnight queue**, or the queue stalls
  waiting on approval. This is the next thing to verify before unattended
  operation (it's a feature, not a bug — it's the vetting-stays-human property —
  but it must be understood).

---

## 5B. Auxiliary client — [CONFIRMED] (resolves last session's "pin off" worry)

Every auxiliary slot (`vision`, `web_extract`, `compression`, `skills_hub`,
`approval`, `mcp`, `title_generation`, `triage_specifier`, `kanban_decomposer`,
`profile_describer`, `curator`) is set to:

```yaml
provider: auto
model: ''
base_url: ''
api_key: ''
```

- They are **`auto`** — not configured to reach any specific cloud provider.
  With `providers: {}`, `fallback_providers: []`, and no `fallback_model` set,
  `auto` has nothing authenticated to resolve to. **The earlier OpenRouter/Nous
  errors were the `auto` resolver attempting cloud and failing closed.**
- So "pin auxiliary off" = decide what `auto` resolves to for these 11
  functions (likely point them at the local Qwen, or leave failing-closed
  deliberately). **Lower stakes than it felt** — nothing is authenticated to
  phone out. Still worth a deliberate pass.
- **Note:** `triage_specifier` and `kanban_decomposer` are auxiliary functions —
  if you want `specify`/`decompose` to work, those slots need a working model
  (point them at local Qwen).

---

## 5C. Other confirmed facts worth keeping

- **Primary model:** `qwen3-8b-64k:latest` via local Ollama
  (`http://localhost:11434/v1`, chat_completions). `custom_providers` defines it
  with `context_length: 64000`.
- **Terminal backend:** `local`, `container_memory: 5120` (5GB), `container_cpu:
  1` — note the **default container is CPU-1/5GB**; GPU work runs on the host
  `local` backend, not in these containers.
- **`checkpoints.enabled: false`** — the auto-snapshot/rollback safety net is
  currently OFF. Consider enabling for file-mutating work.
- **`cron.max_parallel_jobs: null`** and **`cron_mode: deny`** — cron exists but
  is gated off by approvals.
- **`security.tirith_enabled: true`** (`tirith_fail_open: true`) — there's a
  pre-execution command scanner ("tirith") running, fail-open.
- Config schema version: `_config_version: 27`.

---

## 6. [CONFABULATED] — recorded so we never re-adopt these

These were asserted by qwen3-8b and are **disproven or self-flagged as
inferred.** Do **NOT** build on them:

- `hermes profile config set <profile> max_concurrent 1` — **no such
  subcommand** in the real `profile` verb list (§2).
- `metadata={"resource_constraints": {"gpu": "max:1", "memory": "limit:4GB"}}`
  on `kanban_create` — **no `metadata`/`resource_constraints` field** in the
  real `create` flags (§1).
- The entire "Dispatcher Configuration" block from the *second* qwen reply —
  qwen **explicitly labeled it "Inferred from Context"** and did not paste
  `hermes config show`. Its values were inventions: `max_concurrent_workers: 4`
  (the real field is `delegation.max_concurrent_children: 3` + the per-profile
  `kanban.max_in_progress_per_profile`), `task_timeout: 180s`, `heartbeats:
  300s`, `retry_backoff: 2s` — **none of these key names exist** in the real
  config. Only `failure_limit: 2` was real (and `kanban.failure_limit: 2` is
  confirmed in config). **The "global only, not per-profile" claim was
  precisely backwards** — per-profile control is the real mechanism (§5.1).

**Process note:** twice now, qwen has (a) run a command but not pasted its
output, and (b) filled the gap with plausible-looking invented values. For
ground-truth reads, prefer `cat <file>` or piping `--help` directly over asking
the model to summarize — the model is a lossy, sometimes-confabulating layer
between you and the file.

---

## 7. Build path — now unblocked (the critical gate is cleared)

The load-bearing question (per-profile serialization) is **answered**:
`max_in_progress_per_profile` makes a dedicated `gpu` profile run serially. The
dispatcher is the gateway. The legibility verbs are native. So the build is:

1. `hermes kanban init` — create the board db.
2. `hermes kanban boards` — make a board per trajectory (or one to start).
3. `hermes profile create gpu` (+ set its `max_in_progress_per_profile: 1` —
   **verify the set-syntax first, §5.5**).
4. Point `auxiliary.triage_specifier` + `auxiliary.kanban_decomposer` at local
   Qwen if you want `specify`/`decompose` to work (§5B).
5. Create the **first card = probe-set MVE**, `--assignee gpu`, with the vetted
   job script, a `--max-runtime` budget, `--max-retries 1` (block on first
   failure while we're still learning).
6. `hermes gateway start` — the dispatcher ticks every 60s and runs it.
7. Watch via `hermes kanban tail <id>` / `watch` / `log`.

**Before unattended overnight operation:** confirm exactly when
`subagent_auto_approve: false` + `approvals.mode: manual` prompts for approval
(§5A), or the queue stalls waiting on a human.

### Verify-next (small, direct reads):

```bash
hermes profile create --help          # exact profile-create flags
cat ~/.hermes/profiles/gpu/config.yaml # after creating gpu profile: confirm where the per-profile cap lives
hermes kanban create --help            # re-confirm (already captured §1)
```

