---
title: Ephemeris Mechanism v0 (implementation spec)
status: DRAFT — implemented local v0; provisional interface
date: 2026-07-05
companion: ephemeris-charter.md (concept), continuity-and-decision-lineage.md (why immutability)
naming: provisional
implementation: ../../../ephemeris/ (sibling workspace repo at /home/keith260601/boba_work/ephemeris)
---

# Ephemeris Mechanism v0

The charter (`ephemeris-charter.md`) names *what* the Ephemeris is: the
coordination layer that tracks **where angels, agents, work, and Keith are, and
where they are headed** — coordinating *by shared reference, never by command.*
This spec proposes *how* a first, minimal version of that mechanism works, on the
substrate we already have.

**Status:** DRAFT interface, implemented as a local Python package in
`/home/keith260601/boba_work/ephemeris`. This document is now the alignment
surface between the charter and the working v0 code.

## 1. The load-bearing insight — an ephemeris is append-only

A real astronomical ephemeris is a table of **computed positions over time**.
Asking *"where is Jupiter now?"* is a **read** — you take the latest (or
interpolated) row. You never go back and *edit* where Jupiter was yesterday; you
**append** the next observation.

That is exactly the shape the coordination layer wants, and it resolves the one
apparent tension with Asterisms head-on:

- **Asterisms is immutable / append-only** (space, memory, the durable record).
- **The Ephemeris is the present and its trajectories** (time, motion) — which
  *sounds* mutable ("current position" changes).

The resolution: **the Ephemeris is also append-only. "The present" is not stored;
it is a projection — a fold over the log.** Positions accrete; *now* is a query.
This is the git model (immutable commits; `HEAD` is a computed pointer) and it
keeps reflexivity→immutability (`continuity-and-decision-lineage.md`) intact: no
participant can silently rewrite where it — or anyone — was.

## 2. Two record types

Everything the Ephemeris publishes is one of two append-only kinds.

### 2a. Position report — *where a participant is and is headed*
Lightweight, high-frequency, disposable-in-spirit (the log keeps them; attention
doesn't have to). A participant publishes:

| field         | meaning                                                         |
|---------------|-----------------------------------------------------------------|
| `participant` | stable ID: `eph:participant:<role>:<name>:<session-uuid>`       |
| `at`          | UTC timestamp (assigned by the layer)                           |
| `phase`       | short status: `attending` · `blocked` · `resting` · `handoff` · `departed` … |
| `attending`   | free text — what they are on right now                          |
| `heading`     | free text — where they are headed next (the *trajectory*)       |
| `refs`        | optional list of `ast:` ids and/or `eph:score:` ids in play     |

**Structured Participant IDs:** To prevent collision between concurrent agent runs, developer terminals, and different models (e.g. Claude Code vs. agy vs. Hermes workers), free strings are prohibited. IDs must carry a suffix to isolate sessions (e.g., `eph:participant:agent:claude-code:8f2a` or `eph:participant:human:keith:main`).

**Current position of X** = the latest report for `participant = X`. There is no
`UPDATE`; a new position is a new row.

### 2b. Score — *the unit of chartered work* (charter §3, Halprin)
A score is **bounded constraints within which an agent improvises** — not a task
on a conveyor belt. It has a lifecycle, expressed as append-only **events** (never
in-place edits). We explicitly separate the immutable definition of a score from its active state:

**Score Identity (Immutable Genesis):**
Established at the `open` event:

| field           | meaning                                                       |
|-----------------|---------------------------------------------------------------|
| `concern`       | what this score is about                                       |
| `boundaries`    | the constraints inside which the doing stays open              |
| `stop`          | stop conditions — when to halt (done, or halt-and-report)      |
| `survives`      | what must survive / be true at the end (invariants)           |

**Score Folded State (Mutable Projection):**
Derived dynamically by parsing the subsequent event log:

| field           | meaning                                                       |
|-----------------|---------------------------------------------------------------|
| `assigned`      | current assignee (from latest `claim` or `handoff` event, defaults to `open`) |
| `phase`         | active status (`open` · `claimed` · `updated` · `closed` · `abandoned` · `handedoff`) |
| `refinements`   | accumulated list of boundary adjustments from `update` events |

Lifecycle events (each append-only, each stamped + attributed):
`open` → `claim` → `update`* → (`close` | `abandon` | `handoff`).

- **open** — a score is published (by Keith, or an angel proposing work), establishing the identity.
- **claim** — a participant takes it (`assigned` becomes them).
- **update** — progress / a note / a boundary refinement (append; original boundaries stay legible in the log).
- **close** — done. Carries an `outcome` and, if consequential, a pointer to the durable record promoted into Asterisms (see §4).
- **abandon** — halted without completion; carries `why`. Visible, not erased.
- **handoff** — passed to another participant / left for the next session.

**Open scores** = fold the event log to the scores whose latest event is not
`close`/`abandon`. This is the work-in-flight surface.

## 3. The read side — `ephemeris now`

The whole point is the **shared reference**. The primary verb is a read that folds
the log into a legible board:

```
EPHEMERIS · now (2026-07-04T20:10Z)

POSITIONS
  Keith      resting        — heading: back ~21:00
  Claude     attending      — ephemeris mechanism v0 spec   → build v0 next
  Codex      handoff        — asterisms-system clean         → awaiting next score
  Porter     attending      — watching 00-incoming (cherub)

OPEN SCORES
  eph:score:…A  [Claude]  Build Ephemeris v0
                 stop: `now` renders from a real log; tests pass
  eph:score:…B  [open]    Reconcile Porter dedup policy
```

Positions publish; participants move in relation to one another. Nothing here
*commands* — it is a chart you steer by.

Implemented secondary read: `ephemeris log [--since …]` (the raw append-only
stream). Participant-specific position and score list commands are reserved for
a later interface pass; v0 exposes that state through `ephemeris now`.

Write verbs (thin): `ephemeris report …` (a position), `ephemeris score open|claim|
update|close|abandon|handoff …`.

## 4. Where it lives, and the seam with Asterisms

**The Ephemeris gets its own append-only store** — *not* the Asterisms ledger —
and cross-references Asterisms by id. Reasons:

1. **The pairing is the point.** Asterisms is *space*; Ephemeris is *time*.
   Collapsing time into the space-store erases the distinction the charter draws.
2. **Weight.** An Asterisms material is heavyweight by design — a preserved-bytes
   record, a per-record directory, a manifest, four+ table rows, a transformation.
   Right for durable materials; wrong for a position ping every few minutes.
3. **Cadence.** Positions are frequent and low-stakes; Asterisms materials are
   deliberate and permanent.

But immutability doctrine still governs the parts that *matter*:

> **Promotion & Enforced Seam:** When a score **closes with a consequential outcome** (a decision, a merge, or a handoff that alters the project baseline), the Ephemeris **enforces** that the `close` or `handoff` event contains a valid `ast:` material or formation ID from Asterisms. The CLI will reject a consequential close command if no `ast:` ID is supplied. This prevents consequential decision records from existing solely in the transient Ephemeris log, keeping the "one ledger, not two" commitment (see [continuity-and-decision-lineage.md](./continuity-and-decision-lineage.md) §8) intact from day one.

Concretely for v0:

- **Store:** A single append-only text file `ephemeris-log.jsonl` under the Ephemeris home (default `~/.ephemeris/`, overridable by `EPHEMERIS_HOME`). There is **no SQLite database in v0**. This eliminates dual-write drift structurally. SQLite is deferred to v1 purely as a rebuildable, derived index.
- **Locked local appends:** Writers take an exclusive file lock while reading the current head, validating the candidate event, and appending the next line. This protects local multi-agent writes from parent-hash races.
- **Cryptographic hash chain:** Each JSON line in the log contains a `parent_hash` (the SHA-256 hash of the preceding line) and its own `hash` (SHA-256 of its content including the `parent_hash`). The reader validates this chain on every query. It detects in-place edits, reordered lines, and missing middle lines. It **does not by itself prove that the tail was not truncated**; that requires an external head hash or Asterisms anchor.
- **Projections:** Reads like `now` are computed on the fly by doing an in-memory fold over the JSONL log from beginning to end.
- **Score lifecycle enforcement:** Score mutations are fold-validated inside the append lock before commit. Invalid claims/updates/abandons do not enter the log; duplicate opens are rejected; `closed` and `abandoned` scores are terminal.
- **IDs:** Follow the Asterisms grammar where implemented: `eph:participant:<role>:<name>:<session>`, `eph:score:<UTCstamp>-<suffix>`, `eph:event:<UTCstamp>-<suffix>`. Position reports are events in v0, not separate `eph:position:` objects.
- **Runner-independent (charter §5):** The log file format + a plain Python library/CLI is the Ephemeris. Hermes is simply a participant that appends and reads from the log. v0 does not depend on Hermes.

## 5. Scope — what v0 is and is not

**v0 does:** append position and score events to `ephemeris-log.jsonl`; lock local writes; prevalidate score mutations before commit; compute the active state (`now`) via an in-memory fold over the log; enforce that consequential closes/handoffs carry a valid `ast:` identifier; validate the SHA-256 hash chain on all events; follow the implemented id grammar; be usable by hand from a CLI.

**v0 does *not* (yet):** use SQLite (postponed to v1); prove tail non-truncation without an external head/anchor; automate the creation of Asterisms records (only enforces that an ID is provided for consequential closes); integrate Hermes; do any network/multi-host sync; enforce auth between participants; interpolate trajectories.

## 6. Open questions (quarantined — [how-we-work-here.md](../method/how-we-work-here.md) §5)

- **Home location.** Resolved for v0 as `~/.ephemeris/`, overridable by
  `EPHEMERIS_HOME`.
- **Repo home for the code.** Resolved for v0 as the sibling workspace repo
  `/home/keith260601/boba_work/ephemeris`.
- **Participant registry.** v0 requires structured IDs to avoid collision, but a formal agent registration/vetting handshake is deferred.
- **Promotion trigger.** Automatic on every `close`, or explicit `--promote`?
  Leaning explicit for v0 (Keith decides what's consequential), automatic later.
- **Head anchoring.** The next integrity milestone is anchoring the current log
  head hash into Asterisms periodically or on consequential transitions, so tail
  truncation becomes detectable.

---

*This spec is provisional but implemented. Next step: dogfood real scores and then
add Asterisms head anchoring once the CLI shape has survived ordinary use.*
