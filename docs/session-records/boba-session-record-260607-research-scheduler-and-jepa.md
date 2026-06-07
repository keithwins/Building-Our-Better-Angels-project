# BOBA Session Record — Research-Mode Recalibration & the Research Scheduler

**(worked example: JEPA collapse investigation)**

**Type:** dated session record / handoff document
**Date:** 2026-06-07 (lab work performed overnight 06-06 → 06-07; tooling
discovery 06-07)
**Author:** drafted with Claude, for Keith
**Companion doc:** `hermes_kanban_reference.md` (the verified-facts file the
scheduler is built from — load-bearing; this doc is the narrative)

> **Note on scope and naming.** An earlier draft of this file was titled as a
> "JEPA" document. That was a category error (Keith caught it): JEPA is the
> *occasion*, not the subject. The **durable** content here is BOBA-level — a
> methodological discipline, a scheduler architecture, the
> probe-set-as-model-selector insight, and a recalibration of *how research
> gets done*. The JEPA collapse experiment is the worked example that produced
> those lessons. Read §6–§8 as the durable yield; §2–§5 as the example.

---

## 0. What this document is

A complete, assumption-free record of a BOBA development session. It captures:
the methodological discipline that emerged (and was violated, instructively);
the recalibration away from hand-run sequential experiments toward a
**Hermes-driven research scheduler**; the inaugural-workload decision
(probe-set MVE, which doubles as a model-selection benchmark); and — as the
worked example — a JEPA representational-collapse investigation with clean
negative results.

Written to be read cold by future-Keith, by Hermes/an agent, or by a new
collaborator. **[confirm]** marks anything not yet verified from ground truth.

---

## 1. Larger context: BOBA (the trunk)

BOBA (Building Our Better Angels): an AI system whose mission is to *resource
all humans toward lives of their own choosing in a sustainable future*. Premise:
AI cannot be "aligned to humans" because humans aren't aligned with each other,
nor with themselves; so the grammar is **IFS (Internal Family Systems)** — named
persistent agents ("angels"), user as Self/orchestrator. Core commitments:
**mirror, not cheer**; **open frames, not close them**; reason from premises
rather than relitigate/abandon under pressure.

Runtime architecture, three-cornered:
- **dispatcher** (LFM2.5 1.2B) — routes/executes, dumb and fast
- **brain** (Qwen3-8b-64k) — deliberates
- **orthogonal ground truth** (Anytype **[confirm]**) — substrate the brain
  can't silently rewrite

**Hermes** (Nous Research) is the agent substrate.

> **This document does not contain the BOBA foundational doc.** For a cold
> participant, this session record + the reference doc rope them into the
> *current work and tooling* but NOT the *project*. The handoff bundle needs a
> third piece — `BOBA Core — Mission and Foundational Commitments` (canonical
> Opus version) — as the trunk. See §11 handoff item.

This session advanced **one branch**: JEPA / adaptive predictive intake (vision
is one leaf of it). **Elder Angels** (eldercare deployment for a family member)
is a separate, more grounded BOBA iteration and was *not* advanced here — noted
deliberately.

---

## 2. The worked example: JEPA Experiment 1 (collapse detector validation)

Goal was **not** to build a good model. It was to **validate a collapse
*detector*** — confirm the instrumentation can *see* representational collapse
(the trivial solution where a network maps everything to a near-constant) — by
driving the system toward the collapse-prone corner and checking the detector
fires. A detector that never sees collapse can't be trusted to later certify
"safe" configs.

Prior (Exp 0, complete before this session): V-JEPA 2 ViT-L frozen linear
probe, **96.7% val accuracy**, UCF101 subset — the frozen base yields a strong,
linearly-separable representation.

---

## 3. Setup (the actual mechanism)

- **Base:** `facebook/vjepa2-vitl-fpc64-256` — V-JEPA 2 **ViT-Large**, 64-frame
  256px clips. **Frozen.** (Size matters — see §6 lesson 1. Not a toy.)
- **Adapters:** two **LoRA** adapters over the frozen base — `default`
  (student, trainable), `teacher` (EMA-updated).
- **Predictor:** small 2-layer Transformer + linear head; given student
  features with patches masked, predicts teacher features at masked positions.
  Loss = smooth-L1 on masked positions.
- **Teacher EMA:** `teacher = decay*teacher + (1-decay)*student`.
- **Collapse detector:** monitor validation-embedding **std** vs. baseline;
  `COLLAPSE` if std ratio < **0.55**; `STABLE` if a flat-healthy window.

**Swept parameters:**
- **`rho`** — stream autocorrelation. `1.0` = maximally repetitive
  (collapse-tempting).
- **`decay`** — teacher EMA *momentum* (named "decay" for compat; the everyday
  meaning is inverted — code is source of truth). `0.0` = teacher==student = no
  anchor = most collapse-prone; `1.0` = frozen teacher = strongest anchor.
- (implicit) **LoRA rank `r`** — turned out to matter.

---

## 4. Script: v1 → v2

**v1 defects** that made the night confusing / nearly froze the box:
1. **Uncapped train cache** — held the entire decoded train split in RAM →
   WSL2 swap → near-freeze. (Not a GPU issue.)
2. **No external instrumentation** — printed to stdout, but launched *through
   Hermes* stdout was an invisible pipe; no status file.
3. **Write-at-the-end** — trajectory/verdict only at the very end; no live
   signal.

A long detour confirmed v1 was **clean** (only outbound call = HuggingFace Hub
weight fetch; imports torch/numpy/torchcodec/transformers/peft/sklearn only).
The unease was justified as *process* (running unread, uninstrumented code) but
the code was benign.

**v2** (`~/.hermes/skills/jepa-collapse-sweep/scripts/run_sweep.py`, 242 lines,
parse-verified; v1 backed up as `run_sweep_v1.py`): identical experiment math +
a "legible and stoppable" layer — **cost header** (states it's ViT-L, ~15GB,
99% util is correct, names v1's freeze cause); **`--stream_cap`** (the memory
fix; caching dropped to ~13s); **atomic `status_<label>.json`** rewritten every
step (heartbeat/step/frac/std/acc/drift — "alive/how far/stuck?" is one `cat`);
**stop sentinel** (`touch STOP` → clean exit at next step; also catches
SIGTERM/SIGINT); **hard budgets** (`--max_steps`, `--max_seconds`);
**tunable monitor cadence** (the dominant cost); **dual logging** (also appends
to `run_<label>.log`).

---

## 5. Runs & results

All `rho=1.0`. Hardware: RTX 5070 Ti, 16GB.

| Label | r | decay | cadence | max_steps | std floor | end ratio | verdict | notes |
|---|---|---|---|---|---|---|---|---|
| d0.0_r8 (validation) | 8 | 0.0 | 25/100 | 2000 | ~0.74 (x0.94) @150 | x0.95 @500 | STOPPED@500 | dip→**recovered**; 1980s/500 (expensive cadence) |
| d0.0_r32 | 32 | 0.0 | 50/200 | 800 | x0.89 @200 | flat | held (stopped) | deeper floor, still held; rank = weak knob |
| d0.0_r128 | 128 | 0.0 | 50/200 | 600 | — | — | KILLED | **hit ~16GB VRAM ceiling** (15926 MiB, 100% util); crawled, never reached step 50 |
| d0.0_r256 | 256 | 0.0 | 50/200 | 600 | — | — | KILLED | never ran; launched by runaway chain loop, killed during caching |
| d0.0 | 8 | 0.0 | 50/200 | 600 | x0.94 | x0.95 | **STABLE** | 1483s |
| d0.5 | 8 | 0.5 | 50/200 | 600 | x0.94 | x0.96 | **STABLE** | 1485s; acc 93.3→96.7% |
| d0.9 | 8 | 0.9 | 50/200 | 600 | x0.92 | x0.93 | **STABLE** | 1488s |
| d0.99 | 8 | 0.99 | 50/200 | 600 | x0.93 | x0.94 | **STABLE** | 1488s; drift starts 3× slower |

**Central finding:** across **two axes** (rank 8→32→128, decay 0.0→0.99)
**collapse never occurred.** Every completed cell = `STABLE`, std floor in a
narrow **0.92–0.96** band (threshold 0.55), val acc pinned ~**93.3%**.

**Why:** the **frozen base** does the representational work; only a thin LoRA
adapter moves. Rank-8 lacks capacity to drive the representation constant even
with zero anchor. **LoRA over a frozen base self-anchors.**
- **Rank = weak knob** (x0.94→x0.89 for 4× rank) **and hits hardware before
  collapse** (r128 saturated 16GB; r256 would OOM). On this box, rank runs out
  of *memory* before *anchoring*.
- **Decay = near-flat knob** (~3-pt spread across the full range).

**Texture (verdicts throw this away):** identical **dip-then-recover** shape
every cell (anti-collapse signature); the only decay fingerprint is in **drift**
— d0.99 starts ~3× slower (high momentum → teacher barely moves), the sanity
check that the EMA is wired correctly.

**Implications:**
1. This is a **safe fine-tuning regime** — adapter-over-frozen-base resists
   collapse robustly. For BOBA/Elder-Angels deployment, that's **good news**.
2. It's a **bad regime for validating a collapse detector** — can't validate a
   smoke alarm in a fireproof room. Detector code is sound, sanity checks pass,
   but it never saw a true positive.
3. To study collapse you'd have to **touch the base** (§7a) — undecided whether
   that's worth doing.

---

## 6. Methodological lessons (the durable yield, part 1)

1. **Lamp, not lever — and we failed it twice on our own work.** A lever is
   load-bearing; a lamp only illuminates. Hazard: reasoning from a *label* as if
   it were the *thing*. We let "tiny collapse probe" stand in for the
   measurement (model string = ViT-L). Cost: hours of confusion + a near-frozen
   box. Fix: v2's cost-header puts the measurement first. **Rule: trust the
   filesystem mtime / the interpreter / the GPU util / the `cat` of the file
   over the name, the claim, the narration.**

2. **Blind actuation is the failure mode — not insufficient intelligence.**
   Every real fumble (dead-end paths, backwards `cp`, runaway chain loop,
   misreading a stale heartbeat) was action on an *unverified world model*. A
   *smarter* agent with no feedback loop makes the same errors faster and more
   confidently. **Fix for blind actuation is eyes (status, read-before-write,
   ground-truth reads), not IQ.** → trust in the scheduler comes from
   *legibility*, not the brain. **This recurred at the tooling layer too:**
   qwen3-8b twice confabulated Hermes config (invented `max_concurrent_workers`,
   `resource_constraints`, a whole "inferred" dispatcher block) — caught only by
   reading `--help` and `config.yaml` directly. The reference doc quarantines
   those inventions. *Same lesson, the model is a lossy layer between you and
   the file.*

3. **Cooperative halting > solving the halting problem.** Can't decide if an
   arbitrary process halts; *can* sidestep it — heartbeat + stop-file + self-cap
   = legible and stoppable by design. A **stale heartbeat** is the decidable
   "stuck" proxy. (Hermes' `--max-runtime` SIGTERM→SIGKILL→requeue is this,
   native — see reference doc.)

4. **To stop a chain, kill the supervisor, not the child.** A bash `for` loop is
   its own process; killing the running cell just advances the loop (that's how
   r256 launched after we killed r128). Stop a chain = Ctrl-C the loop / `pkill
   -f`, not a single-PID kill. → argument for a real supervisor over ad-hoc
   loops.

5. **Validate instruments on safe inputs first.** First jobs through a new
   scheduler should be cheap/fast/obviously-correct, not hour-long GPU cells, so
   the scheduler itself is proven before trusted unattended.

---

## 7. New directions

### 7a. JEPA-collapse line — **explicitly undecided**

To reach collapse, loosen the frozen base: unfreeze last block(s) (cheapest,
fits r8 memory); or smaller/weaker base; or remove the predictor's stop-gradient
asymmetry (positive control). **Status: Keith is not convinced this belongs on
the active list.** For: validate the detector. Against: §5-impl-1 (the regime is
safe) may already be the answer that matters, and detector-validation can wait.
**A deliberate decision, not a momentum default.**

### 7b. The recalibration (durable yield, part 2): stop hand-running sequential experiments

The session's deepest finding is about **mode**. We descended three levels below
anything serving Elder Angels, in a fully **sequential, hand-actuated** mode —
operator as human clipboard, the 5070 Ti running *one* question while every
other BOBA thread stalled. The card sat **dark ~3am–10:30am**: pure wasted
capacity. Correction: treat the 5070 Ti as a **shared resource across many
trajectories** — a "SETI/BOINC for your own research" — with a scheduler that
keeps it busy and the operator **out of the *actuation* loop while staying in
the *vetting* loop**.

### 7c. Probe-set MVE = the right first workload (and a model-selector)

The probe-set MVE (embed a fixed reference text set under multiple models → a
portable coordinate system across embedding spaces) should be the **first real
card**:
- **Safe GPU work** (embedding, not training — nothing that melts the card) →
  ideal for proving the scheduler at low stakes (§6.5).
- The **instrument BOBA governance rests on**.
- **Dual role (discovered this session):** it's *also* how you answer *"which of
  the revolving cast of models (Qwen3.6? Gemma? others?) should be the brain?"*
  — discriminating, self-authored benchmarks measuring what *we* care about. The
  system bootstraps its own model-selection criterion, including for the brain
  that runs the scheduler.
- **Corollary — defer the model question.** Don't pick Qwen3.6 vs Gemma by
  vibes. Qwen3-8b is fine for the dumb dispatcher now. Choose on evidence later.

---

## 8. The research scheduler — design + CONFIRMED Hermes mechanics

> The architecture below is now backed by **verified Hermes facts** (see the
> companion `hermes_kanban_reference.md`). What was "design intent" in the first
> draft is now mostly "configure the native system."

### 8a. Core insight: scheduling time is free time

GPU busy ~25 min/job = ~25 min to deliberate "what's next," re-sorting as
results land / Keith weighs in / the world changes. The decision only must be
**ready when the card frees**, not instant. This dissolves dumb-vs-smart:
- **Actuation stays dumb/deterministic:** GPU frees → pop top of priority queue
  → run. (LFM2.5 dispatcher role.)
- **Ordering is a separate, slow, possibly-intelligent process** in the idle
  window. (Qwen3 brain role.)

You need a **dumb dispatcher reading a queue a smarter brain re-sorts in the
GPU's shadow.** A faithful small instance of BOBA grammar: **system surfaces and
schedules; human/brain decides; re-prioritization disagreements escalate for a
second opinion.**

### 8b. Priority as a recomputed *view*, not a frozen field

Store the *inputs* to a priority judgment in each card; recompute ordering as
info lands. Hermes' `--priority` is a **tiebreaker** (confirmed), and readiness
is gated by **`--parent` dependencies + status** — so primary ordering is the
dependency graph, priority breaks ties. The "brain edits priority in the idle
window" design works at tiebreak level; stronger reorders use parent
links / `block`/`unblock`/`promote`. **Minimal version today:** Keith sets
`--priority` at vetting; "re-sort" = editing it while GPU busy; the smart
re-sorter later just edits it for you.

### 8c. CONFIRMED: Hermes already IS most of the scheduler

(Full detail in reference doc; key facts:)
- **`kanban.dispatch_in_gateway: true`, `dispatch_interval_seconds: 60`** — the
  dispatcher runs in the gateway, ticking every 60s. **"The scheduler" =
  `hermes gateway start`.** (`kanban daemon` is DEPRECATED.)
- **`kanban dispatch`** = one pass: "reclaim stale, promote ready, spawn
  workers."
- **Dependency API:** `--parent` / `link` / `unlink` (parent→child).
- **Native legibility** (the layer we hand-built into run_sweep.py): `tail`,
  `watch`, `log`, `runs`, `heartbeat`, `stats`, `context`.
- **Native budgets/failure handling:** `--max-runtime`
  (SIGTERM→SIGKILL→requeue), `--max-retries` (consecutive-failure circuit
  breaker; `kanban.failure_limit: 2` default).
- **`swarm`** (parallel workers→verifier→synthesizer) and `specify`/`decompose`
  (auxiliary-LLM spec drafting / fan-out) exist natively.
- **Boards:** one per project/workstream → a board per BOBA trajectory.

### 8d. CONFIRMED: the GPU-serial lever

- **`kanban.max_in_progress_per_profile`** (currently `null`) is the real
  per-profile concurrency cap. **A dedicated `gpu` profile capped at 1 →
  dispatcher guarantees one GPU job at a time, others parallel.** This is the
  whole GPU-serial strategy, native — no resource-limit hacks.
- **`delegation.max_concurrent_children: 3`** is the real global subagent
  default (qwen's "max_concurrent_workers: 4" was confabulated).
- **[UNVERIFIED]** exact syntax/location to set the per-profile cap (global
  config key vs `~/.hermes/profiles/<name>/config.yaml`) — verify after
  `profile create`.

### 8e. Autonomy posture — CONFIRMED, and the one real pre-flight check

- **`approvals.mode: manual`, `cron_mode: deny`, `subagent_auto_approve:
  false`** — the deliberate gates are real and active.
- **The one thing to pin down before unattended overnight operation:** *exactly
  when* manual-approval + no-auto-approve prompts during worker spawning, or a
  queue will **stall waiting on a human** at 1am. It's a feature
  (vetting-stays-human), but its trigger points must be understood. **Last real
  unknown before the scheduler can run unattended.**

### 8f. Auxiliary client — CONFIRMED (resolves last session's "pin off" worry)

All 11 auxiliary slots are `provider: auto`, empty model/key; `providers: {}`,
no `fallback_model`. So `auto` has nothing authenticated to resolve to — **the
earlier OpenRouter/Nous errors were `auto` trying cloud and failing closed.**
"Pin off" = decide what `auto` resolves to (point at local Qwen, or leave
failing-closed deliberately). **Lower stakes than it felt.** Note:
`specify`/`decompose` need `triage_specifier`/`kanban_decomposer` pointed at a
working model (local Qwen) to function.

### 8g. Monitoring (low priority)

Gateway speaks Telegram/Signal/Discord/Slack/Email/SMS → "monitor from the road"
= connect the gateway to one platform, jobs deliver status there. **Keith's
call: not make-or-break — trip is ~2 days.**

---

## 9. Hardware / environment reference (**[confirm]** where noted)

- **Workstation:** Dell XPS 8930 ("Alpha Angels"), 850W Rosewill PSU.
- **GPU:** RTX 5070 Ti — Blackwell, sm_120, **16GB** (~15.9GB usable observed).
  Sustained 99% util on real work → **sm_120/CUDA stack confirmed real** (also
  closes the original kernel-verification gate).
- **OS/runtime:** WSL2 on Windows; Ubuntu **26.04 [confirm]**; Python **3.14**
  (observed); virtualenv `~/jepa`.
- **PyTorch:** 2.12.0 + CUDA **[confirm exact cuXXX]**; driver passthrough
  confirmed in WSL2.
- **Local models (Ollama):** LFM2.5 1.2B (dispatcher) + Qwen3-8b-64k (brain);
  Hermes primary = `qwen3-8b-64k:latest` @ `localhost:11434/v1`,
  `context_length 64000`.
- **Agent substrate:** Hermes (Nous Research), `_config_version: 27`; reported
  **v0.16.0 [confirm]**.
- **Data:** `~/intake/exp0/UCF101_subset`.

**Environment caveats / open items:**
- **Auxiliary** = `auto`, fails closed today (§8f). Deliberate-pin decision
  pending.
- **Power pinned awake:** `standby-timeout-ac 0`, `monitor-timeout-ac 0`; active
  scheme **Power saver** (may cap clocks). **Revert** if normal sleep wanted;
  consider Balanced/High-performance for GPU.
- **`checkpoints.enabled: false`** — auto-snapshot/rollback safety net is OFF;
  consider enabling for file-mutating work.
- **`security.tirith_enabled: true`** (fail-open) — pre-execution command
  scanner is running.
- **Stale artifact:** `exp0_result_260606.2200.md` — name says `2200`, mtime
  18:33. Clean it (mtime = truth, embedded label = claim).
- **Don't close the WSL terminal mid-run** — tears down the VM, kills Hermes +
  jobs.

---

## 10. Artifacts produced

- **`run_sweep.py` v2** — `~/.hermes/skills/jepa-collapse-sweep/scripts/` (242
  lines, parse-verified). v1 → `run_sweep_v1.py`.
- **Trajectories** (`~/intake/exp0/`): `sweep_d0.0.npy`, `sweep_d0.5.npy`,
  `sweep_d0.9.npy`, `sweep_d0.99.npy`, + partial r8/r32.
- **`sweep_results.txt`**, **`run_<label>.log`**, **`status_<label>.json`**.
- **This doc** + **`hermes_kanban_reference.md`** (the two written this session).

---

## 11. Open decisions & TODO

**Decide deliberately (not by momentum):**
- [ ] Does the **JEPA-collapse line stay on the active list?** (§7a)
- [ ] **Auxiliary**: pin `auto` → local Qwen, or leave failing-closed by
      design? (§8f) — and point `triage_specifier`/`kanban_decomposer` at local
      Qwen if you want `specify`/`decompose`.
- [ ] **Brain model** — defer until the probe set gives evidence (§7c).

**Build (near-term, scheduler):**
- [ ] **Pre-flight the one real unknown:** exactly when manual-approval /
      `subagent_auto_approve: false` prompts during spawning (§8e) — required
      before unattended overnight runs.
- [ ] `hermes kanban init`; make a **board per trajectory** (§8c).
- [ ] `hermes profile create gpu`; **set its `max_in_progress_per_profile: 1`**
      (verify syntax/location first, §8d).
- [ ] First card = **probe-set MVE**, `--assignee gpu`, vetted script,
      `--max-runtime` budget, `--max-retries 1`.
- [ ] `hermes gateway start`; watch via `kanban tail`/`watch`/`log`.
- [ ] (Optional, low priority) connect gateway → a messaging platform for
      remote monitoring (§8g).

**Corpus / git / collaboration (its own deliberate task, via Claude Code):**
- [ ] **Confirm canonical BOBA corpus location** — Drive vs GitHub migration
      (open since ~April). Resolve before filing docs into the wrong home.
- [ ] **Verify git works end-to-end on *our* side** — not just that the GitHub
      repo exists, but that the 8930 has git authenticated + repo cloned +
      `git status` clean + a trivial push succeeds. (Claude cannot see/verify
      this; Claude has **no write access** to the repo.)
- [ ] **Use Claude Code as the git surface** (included in Pro; can clone/commit/
      push with per-step approval — the gap plain-Claude can't fill). Bake
      **git skill-building** into the process deliberately — Keith hasn't
      developed git skills; treat that as a learning thread, not an assumed
      prereq.
- [ ] **Relocate these docs** into the corpus once location is confirmed; the
      **reference doc** especially benefits from git history (audit trail of
      *when* each Hermes fact was confirmed).
- [ ] **Rename/refile** this doc so its durable BOBA content isn't hidden under
      "jepa" — done here (BOBA-forward title); ensure the corpus copy reflects
      it.

**Handoff bundle (to braid in another intelligence):**
- [ ] Three docs, three altitudes: **(1) BOBA Core — Mission & Foundational
      Commitments** (trunk / what+why — *already exists, not in this bundle
      yet*); **(2) this session record** (current branch / what we're doing);
      **(3) `hermes_kanban_reference.md`** (mechanics / how the tooling works).
- [ ] **Draft a short "how we work here" stance note** — the epistemic culture:
      lamp-not-lever, ground-truth-over-narration, verify-before-build,
      confabulation-is-the-failure-mode, mirror-not-cheer. For a project about
      how intelligences relate, this onboarding *is* corpus, not a nicety. (Not
      yet written.)

**Deferred analysis:**
- [ ] Multi-cell **trajectory plot** from the `.npy` files — all four decay
      curves overlaid, drift-vs-std twin axes, floors marked.

---

## 12. One-paragraph summary

A BOBA development session whose worked example was JEPA Experiment 1 — driving
an adapter-over-frozen-ViT-L setup into its most collapse-prone corner and
sweeping LoRA rank and teacher anchor strength. **Collapse never occurred on
either axis:** the frozen base self-anchors, rank is a weak knob that hits the
16GB ceiling before collapse, anchor strength barely moves the floor. A genuine
result — the regime is *safe* (good for deployment) but *can't validate a
collapse detector* (you'd have to loosen the base; undecided whether worth it).
The deeper, durable findings were about **method** (trust comes from legibility,
not intelligence; reason from measurement, not labels — a discipline we violated
twice, including qwen confabulating Hermes config) and **mode** (hand-run
sequential experimentation wastes operator and GPU alike; the 5070 Ti sat dark
3am–10:30am). The recalibration: a **Hermes-native research scheduler** — a dumb
dispatcher pulling a priority queue a smarter brain re-sorts in the GPU's idle
shadow, with a dedicated `gpu` profile capped at one in-progress task for serial
GPU execution — now confirmed to be mostly *configuration of native Hermes*
rather than new code. Inaugural workload: the **probe-set MVE**, which doubles
as the model-selection benchmark that will eventually choose the brain itself.
Governing principle, learned the hard way: **trust comes from legibility and
stoppability, not from intelligence.**
