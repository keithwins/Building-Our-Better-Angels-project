# BOBA Corpus Intake Plan

**Purpose:** Decide which document streams belong in the GitHub corpus, in what order, and how to treat them.

---

## Document streams to intake

### 1. Core — BOBA Mission and Foundational Commitments
**What it is:** The canonical Opus-drafted document establishing BOBA's mission, grammar (IFS), and core commitments. The trunk all other work branches from.
**Target folder:** `docs/core/`
**Priority:** Highest. This is the most load-bearing document for the retrieval index and for any future agent onboarding. Every other document references it implicitly.
**Treatment:** Import as-is. Light copy-editing only — do not summarize or restructure. This document should be authoritative.
**Privacy:** [needs-Keith-input] — confirm whether any family-specific or private-deployment details are present before committing publicly.

---

### 2. Method — How We Work Here (already present, expand)
**What it is:** Epistemic culture, process discipline, working rules. `how-we-work-here.md` is already in the repo and indexing well.
**Target folder:** `docs/method/`
**Priority:** High. Already the best-performing section in the retrieval benchmark.
**Treatment:** Continue expanding as new methodological insights emerge from sessions.
**Privacy:** None — this is process, not personal content.

---

### 3. Braid — Intelligence-Braiding Framework
**What it is:** The framework for how human and AI intelligences relate in BOBA — not pledged, not obedient, braided. Distinct from the IFS grammar but closely related.
**Target folder:** `docs/core/` or `docs/method/` depending on whether it reads as foundational or procedural.
**Priority:** High. The retrieval index currently has no content representing this concept explicitly; queries about braiding would miss.
**Treatment:** [needs-Keith-input] — confirm whether the Braid material exists as a standalone document or is embedded in other writing.
**Privacy:** None expected, but confirm.

---

### 4. Fog — Epistemic and Phenomenological Writing
**What it is:** Writing about navigating uncertainty, ecological confusion, the limits of audit. Closely related to the `how-we-work-here.md` sections on quarantine uncertainty and the wobbly edge.
**Target folder:** `docs/essays/` if exploratory; `docs/core/` if it has reached foundational status.
**Priority:** Medium. The retrieval benchmark already handles related queries reasonably from method docs. Fog writing would enrich it.
**Treatment:** May need light chunking decisions — if the writing is longform and continuous rather than headed sections, heading-boundary chunking will underperform. Flag for future chunking strategy work.
**Privacy:** [needs-Keith-input] — Fog writing may draw on personal experience. Review before committing publicly.

---

### 5. Walk — The Walk (longform philosophical source-stream)
**What it is:** Longform philosophical writing. The source material for BOBA's deeper commitments.
**Target folder:** `docs/manuscript/finite-and-infinite-frames/` or `docs/manuscript/` depending on scope.
**Priority:** Lower for retrieval index utility in the near term; higher for corpus completeness and future agent context.
**Treatment:** Do not chunk aggressively. Longform philosophical prose loses coherence when split at headings alone. Consider paragraph-level chunking or overlapping windows when this is indexed.
**Privacy:** [needs-Keith-input] — confirm public/private boundary for manuscript material.

---

## Recommended intake order

1. **Core** — unblocks agent onboarding, most load-bearing for retrieval
2. **Braid** — fills the largest current gap in the retrieval index
3. **Method expansions** — ongoing, as sessions produce new doctrine
4. **Fog** — enriches the index; requires privacy review first
5. **Walk** — after chunking strategy is improved beyond heading-boundary only

---

## Open questions for Keith

- [ ] Does Core contain private deployment details (Elder Angels specifics) that need separation before public commit?
- [ ] Does the Braid material exist as a standalone document?
- [ ] What is the privacy boundary for Fog writing?
- [ ] Is the Walk intended to be public in the repo, or is it manuscript-private?
- [ ] Should `docs/manuscript/` be a public folder, or should it live outside the repo until ready?
