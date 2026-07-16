# BOBA Session Record: 2026-07-16 — Naming the Fog

*A corpus legibility pass. Recorded as a folded score: the frame it followed, and
what the improvisation produced.* (Working name — rename freely.)

## Session context
- Date: 2026-07-15 evening → 2026-07-16 ~01:40 (EDT)
- Environment: WSL2 (Ubuntu), Cursor
- Workspace: `/home/keith260601/boba_work`
- Collaborators: Keith + agent (Opus)
- Repos touched: `Building-Our-Better-Angels-project`, meta-repo `boba_work`

## The score (the frame the work improvised inside)
- **Concern:** make the corpus more legible to itself — in words (define what we
  already say) and in structure (see what we already have).
- **Boundaries:** conceptual/language changes flow to the *corpus* (doctrine
  layer), not just the book (presentation layer); protect immutable history and
  generated builds; do not absorb sibling repos into the meta-repo; keep sibling
  and personal Asterisms content out of scope.
- **Invariant:** every accepted edit in the book is propagated to its corpus
  source (corpus-first), so the two never silently diverge.
- **Stop condition:** committed + pushed, with a named provenance record.

## What it produced (provenance)
### Naming / doctrine pass
- Defined five previously-undefined core terms in
  `docs/core/glossary-and-ontology.md`: **The Wobbly Edge** (in Keith's tongue),
  **The Fog**, **Braided Discourse**, **Better Angels** (deliberately
  unfinished), **Eclosion**.
- Renamed the corpus prologue `The Door in the Fog` → **`The Fog Between Us`**
  (`00-prologue-the-door-in-the-fog.md` → `00-prologue-the-fog-between-us.md`);
  reframed `Fog as in weather.` → `Fog as in the space between minds — theirs,
  ours, and our own.`
- Propagated accepted book edits back to the corpus prologue (corpus-first):
  dropped "It is not a tool-user pair"; "question card" → "handrail"; "systems
  that do not know how to love us" → "were never built to love us"; the
  wound/plan line → "old wound it has learned to call realism"; and cut the
  "tenderness without structure gets tired and goes home" couplet (solved in the
  book fork as "…what it is to be managed without care or attention to whether
  they are okay").
- Seeded a parenting **open thread** in `docs/essays/the-wobbly-edge.md` (edge as
  held reaching; ties to trust-and-verify and humans-as-angels).

### Orientation surface for the corpus itself
- Extended `scripts/corpus_bibliography.py`: per-doc **status** derivation,
  overlap detection **scoped** to exclude session/log noise, cluster
  classification into a **decision queue** (dedupe / merge-track / reconcile /
  review / archive), a rendered **`corpus/corpus-map.md`**, and a **`--check`**
  freshness/drift mode.
- Regenerated `corpus/` indices (167 source docs, 27 scoped clusters); linked the
  map from `CORPUS_MAP.md`; committed `CORPUS_BIBLIOGRAPHY.md`.

### Book artifacts
- Regenerated the book build and current **print PDF**
  (`.../print/…-260716.pdf`, 94pp); synced the print tool's reading sequence to
  the reshuffled opening (Known → The Village) and auto-dated all book/print
  build stamps so filenames and page headers stop drifting.

## Commits
- meta `5840e59` — corpus document-map generator + generated indices.
- BOBA `270949a` — rename prologue; define glossary terms; reshuffle book opening.
- BOBA `04fc483` — current print PDF; sync + auto-date print tools.

## Decisions of record
- Sibling repos stay independent; fixed a leak where the renamed
  `lively-mirror-platform/` was not ignored by the meta-repo.
- Kept the prologue body's "It is a door." (book-as-threshold, a different door
  than the retired title's).
- Corpus-first propagation adopted as the working rule for this kind of edit.

## Open threads / next beginnings
- Place the parenting analogy (currently an open thread in `the-wobbly-edge.md`).
- Decision-queue candidates to work: near-identical `continuity-and-decision-lineage`
  ↔ book `60-trust…`; the `book-publishing-plan` / collaborative-surface cluster;
  retire/settle the `corpus-intake-*` pair.
- Map polish: repos without `docs/<subdir>/` nesting fragment into single-file
  "areas" (a `kind_for` quirk).
- The book's **ending** (Eclosion) — the next beginning — remains the large open
  work.
- If true immutability is wanted, Porter this record into `~/asterisms/`.

**Status:** ✅ committed + pushed. Provenance materialized.
