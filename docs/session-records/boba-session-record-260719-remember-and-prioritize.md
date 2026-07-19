# BOBA Session Record: 2026-07-19 — Remember & Prioritize (design + threads)

*A continuity-design session. Recorded as a folded score.* (Working name — rename freely.)

## Session context
- Date: 2026-07-18 afternoon → 2026-07-19 ~00:28 (EDT)
- Environment: WSL2 (Ubuntu), Cursor
- Workspace: `/home/keith260601/boba_work`
- Collaborators: Keith + agent (Opus)
- Repos touched: meta-repo `boba_work` (`private/PRIORITIES.md`); this record in BOBA repo.

## The score
- **Concern:** clear the list (reader, Restic, board, essay) and design *the way we
  remember and prioritize* — with the agent helping keep Keith on track.
- **Boundaries:** low attention by end; capture, don't start new work; preserve history.
- **Stop condition:** state folded so tomorrow's orient surfaces everything.

## Decisions of record
- **Reader ABANDONED (2026-07-18).** `reader-v0` lane + trusted-reader edition — Keith
  does not expect to return. Preserved as dormant history (Never Forget); do NOT apply
  the invitation-v1 ladder there (those reader edits are moot). **The invitation-v1
  FRAME (corpus §0/§0b/§0c + decisions) is unaffected** — it lives in the book/corpus
  layer, not the reader. Optional follow-up: dormant banner on `reader-v0/README.md`.
- **Restic:** understood against `BACKUP.md`. Two layers today (Git/GitHub for source;
  Restic on `/mnt/d/BOBA-backups/restic` for living Asterisms/Ephemeris/Salon/priorities).
  Gap = `D:` is same-machine, not disaster-independent. **Deferred with a TRIGGER** in
  PRIORITIES. Cheapest single win: confirm the restic password is in the password
  manager (`BACKUP.md` line 60). Sharpen options later: rotating USB vs cloud bucket.
- **Project status board — refined requirement.** Modeful / multi-level:
  **moment** (one doc/task) ↔ **project** (a named body of work) ↔ **month/sweep**
  (temporal). **Composable:** reuse `corpus_bibliography.py` overlap embeddings as a
  "composes-with" signal. Builds on the existing tool; missing pieces = (1) project/work
  layer, (2) temporal rollup by last_touched, (3) mode switch. Queued.
- **New essay (topic TBD)** — active. May compose with / draw on existing writing;
  first use-case for the board's composability view.

## Remember-&-prioritize design (the meta-thread)
- **Honest constraint:** the agent does NOT persist across sessions. So "keep me on
  track" = **the substrate remembers + the agent orients from it at session start.**
  Reliability lives in files + ritual, not in the agent's memory.
- **Primitives:** capture (fold/notes/items) ✅ · item (PRIORITIES row) ✅ ·
  **trigger** (`TRIGGER:` field = when an item resurfaces) ⚠️ ad hoc ·
  **orient** (read substrate + surface what's due at session start) ❌ not yet a habit ·
  prioritize (query-not-rank) ✅ declared · levels (the board) 🔜.
- **The gap = the retrieval half:** a trigger only fires if *something reads it* — either
  the agent at session start, or a hook/script. That is the missing piece that makes
  "remind me" real.
- **Proposal (pending Keith's yes):**
  1. Agent adopts **orient-on-start** as default — reads `PRIORITIES.md` + latest
     session-record, gives a short "active / due / stale" readout each session.
  2. **Standardize the `TRIGGER:` field** (condition- or date-based; greppable).
  3. Later: **automate the read** via a Cursor hook so it doesn't depend on the agent.

## OPEN DECISIONS for tomorrow (unanswered — surface these on orient)
1. **Adopt "orient-on-start" as the agent's default behavior?**
2. **Essay:** what's the seed idea / topic? (unlocks the composable-material pass)
3. **Board:** build a v0 now, or shape the design more first?
4. **Restic:** sharpen into concrete options + verify password-in-manager.
5. **Standardize the `TRIGGER:` field format?**

## Open threads / uncommitted
- **Uncommitted (meta-repo `main`):** all `corpus/` notes still untracked (voice,
  chat-export, invitation-v1 decisions/ladder, audits, bibliographies, print/, scripts/).
- **This record + prior fold:** `260718` fold was committed (`a97b286`); **this `260719`
  record is untracked** in the BOBA repo until committed.
- Porter the folds into `~/asterisms/` — deliberate daytime immutable-receipt move.

## How to orient tomorrow (do this first)
1. Read `private/PRIORITIES.md` — Active + Queued + any **TRIGGER** lines (Restic is due).
2. Read this record's **OPEN DECISIONS** list.
3. Then pick by today's energy/pull — it's a query, not a ranked queue.

**Status:** ⚠️ on disk; **not committed.** Fold written so tomorrow's orient is cold-start-safe.
