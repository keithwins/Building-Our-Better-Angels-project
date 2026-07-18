# BOBA Session Record: 2026-07-18 — Stakes, Scaffold, and the Wisdom-Permeable Membrane

*A frame-and-continuity session. Recorded as a folded score: the frame it followed,
and what the improvisation produced.* (Working name — rename freely.)

## Session context
- Date: 2026-07-17 evening → 2026-07-18 ~01:16 (EDT)
- Environment: WSL2 (Ubuntu), Cursor
- Workspace: `/home/keith260601/boba_work`
- Collaborators: Keith + agent (Opus)
- Repos touched: meta-repo `boba_work` (corpus notes + `private/PRIORITIES.md`).
  BOBA repo **not** committed this session (its de-pathologize work landed earlier
  in `083efd8`).

## The score (the frame the work improvised inside)
- **Concern:** (1) continue de-pathologizing the invitation; (2) explore "capturing
  a person" technology (voice, chat history); (3) sharpen the project's big *why*;
  (4) design orientation/continuity habits (fold-on-close / orient-on-open).
- **Boundaries:** draft-only for the live book/reader (no live reader prose changed);
  preserve immutable history; corpus notes are decision-aids, not doctrine amendments;
  do not commit unrelated files.
- **Invariant:** needing help is legitimate; the *medical-case talk* is the distortion.
  Personalize with situations/roles/instruments, never Keith-as-patient (L2).
- **Stop condition:** frame captured to disk; a sticky queued; this fold written.

## What it produced (provenance)

### Research notes (via background subagents)
- `corpus/voice-self-expression-exploration.md` — voice self-expression / cloning
  survey. Recommendation: **Chatterbox** (Resemble AI, MIT, local on RTX 5070 Ti,
  PerTh watermark by default). Key finding: the voice can be saved as a portable,
  inspectable **`.pt` conditioning artifact** (`Conditionals.save()/load()`) — enroll
  once, regenerate offline forever; not proprietary. ElevenLabs ruled out for the
  corpus (terms collide with Never Forget). Reading-list stance **decided:
  self-authorship passages only** (not Keith-mirror text).
- `corpus/chat-history-export-exploration.md` — exporting ChatGPT / Claude / Gemini /
  Grok history. No dedicated tool/API for web-UI history; each has an official
  self-service export (ChatGPT DAG `mapping`; Claude `chat_messages[]`; Gemini via
  Takeout activity log; Grok `prod-grok-backend.json`). Class 4/5 → local-first,
  Porter intake, never third-party importers. First step: request the ChatGPT export,
  hash it, verify via `chat.html`, copy Custom Instructions + Memory by hand.

### Frame work (invitation-v1)
- `corpus/invitation-v1-decisions.md` extended:
  - **§0 — the civilizational *why*** (confirmed L2 stance): old safety guarantees
    failing; "$500 and a grudge" cheap asymmetric power; unenforceable safety; a
    society that can be torn at; the *search* for collaborative intelligence that
    resources *all of us*. Recovers existing seeds (mission universality, Lincoln
    tear-apart, disalignment premise); adds the previously-unrecorded threat half.
    **A search posture, not a promise that AI saves us.**
  - **§0b — help is not pathology.** The taboo (help looks like a medical case)
    delayed the ask; the delay got misread as private failure. Legitimate: asking for
    a scaffold that holds so the better parts can work. Distorted: patient-0 / managed
    case.
  - **§0c — membrane ≠ stoma; enclosure ≠ eclosion.** Untangled two collapsed jobs.
    Membrane = selective routing posture; **stoma** = named selective *channel through*
    it (ingress: **Porter**; material egress: **Little Flea**; care egress: unnamed;
    invitation/eclosion egress: allowlist+seam). Chrysalis/scaffold = *hold*; eclosion
    = *emerge*; retire the portmanteau "enclosion." Coinage (Keith): **"wisdom-permeable
    membrane"** — permeable not only *against* being torn apart but *for* wisdom,
    health, and cultural breadth to ingress ("the hope half of the fog").
  - **Decision 5** (§0 = load-bearing L2 stakes frame; personal work is method, not
    subject) and **Decision 6** (ladder arc = recognition → orientation →
    accompaniment-with-authorship → scope → invitation).
- `corpus/invitation-v1-ladder-draft.md` revised: added a **stakes** rung (threat +
  hope), rewrote **accompaniment** around chrysalis→eclosion / retained authorship /
  membrane-with-passage, kept the **scope** rung. Per-file edit blocks updated. **Still
  draft — not applied to the live reader.**

### Continuity / workflow design (conceptual, no build)
- **fold-on-close ⇄ orient-on-open** must be a *pair*; a fold nobody reads is a diary,
  not a membrane. Existing homes: `session-records/` + fold discipline (close);
  `HANDOFF.md` + `PRIORITIES.md` + AGENTS pointer (open).
- **Repo-attached metadata:** you already do the standard thing (in-tree convention
  files). Menu: in-tree files (ADR/CHANGELOG/HANDOFF/AGENTS) · git-native (notes, tags,
  trailers) · triggers (git hooks for git events; **Cursor hooks** for the true
  window-close/session event) · platform (issues/wiki, not in-tree). The close-window
  gap is an *agent/editor* event → Cursor hooks, not git hooks.
- **Hooks are not background agents.** A hook fires on an event, runs once, exits. No
  loop, no persistent process, API call only if you want a smart summary. Looping =
  an always-on watcher (you already run one: **Porter**); not needed for folding.
- **Status/todo reframe (Problem B):** four distinct kinds — project *state* (lives
  WITH each project, in front-matter) · session *events* (append-only records) ·
  *priorities* (a query, recomputed — as `PRIORITIES.md` already declares) · the
  *master list* (generated, never hand-woven). The repeatedly hand-built annotated
  biblios are a symptom that the generated index (`scripts/corpus_bibliography.py`)
  isn't yet load-bearing.

### Sticky queued
- `private/PRIORITIES.md` → Queued: **"Generate a project status board from existing
  files"** (inspect what `corpus_bibliography.py` emits; propose minimal per-file
  front-matter; generate one woven board).

## Commits
- **None this session.** BOBA branch `cursor/depathologize-invitation-never-forget`
  was already committed + pushed earlier (`083efd8`). Meta-repo corpus notes remain
  **uncommitted** (see open threads).

## Decisions of record
- Civilizational *why* (§0) is L2 stakes doctrine; personal continuity work is
  method/instrument, not the project's care-subject.
- Help ≠ pathology; enclosure ≠ confinement; scaffold/chrysalis → eclosion.
- **stoma ≠ membrane** (glossary already said so); don't force all egress into one organ.
- Coinage adopted: **wisdom-permeable membrane**.
- Voice: **Chatterbox local-first**; reading-list = **self-authorship only**.
- Chat-history: **local-first, Porter intake, no third-party importers**; start with
  ChatGPT export.

## Open threads / next beginnings
- **Uncommitted (meta-repo `main`):** all `corpus/` notes are untracked — voice +
  chat-export explorations, `invitation-v1-decisions.md`, `invitation-v1-ladder-draft.md`,
  keith audit/genealogy, annotated bibliographies, `corpus/print/`, `corpus/scripts/`.
  Decide: commit on `main` vs a branch; **exclude** `adaptive-pneumatic-wing/` and root
  `scripts/build-corpus-print-packet.py` unless confirmed ours. (Do NOT use the BOBA
  branch Commit button — wrong repo.)
- **Project status board** — queued sticky in `PRIORITIES.md`.
- **Apply the invitation-v1 ladder to the live reader** (`reader-v0/sections/01-how-to-read.md`
  + `sections-trusted/01-a-note-on-this-copy.md`) — still draft; needs approval + build
  regen. Open feel-checks: is the accompaniment rung too dense; "I" vs "we"; stakes-first
  vs stakes-in-prologue.
- **Book-opening "why now" section** carrying §0 in long form — not drafted.
- **fold-on-close / orient-on-open automation** (Cursor hooks) — optional build;
  `create-hook` skill available.
- **Salon** park/retire decision — still open (lean: park as history, keep the
  append-only/open-questions bone; charter reads as governance it never earned).
- **Local Chatterbox setup guide** for the RTX 5070 Ti — optional next.
- If true immutability is wanted, Porter this record into `~/asterisms/`.

**Status:** ⚠️ notes on disk; **not committed, not pushed.** Frame captured; sticky
queued; fold written.
