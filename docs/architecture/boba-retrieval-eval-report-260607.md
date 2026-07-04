# BOBA Retrieval Eval Report — 2026-06-07

## Setup

| | |
|---|---|
| Index chunks | 112 |
| Eval cases | 63 |
| Eval file | `retrieval_eval_expanded.jsonl` |
| Embedding model | nomic-embed-text (768 dims, via Ollama) |
| top_k | 5 |

## Overall Results

| Metric | Value |
|---|---|
| Top-1 accuracy | 31/63 = 49.2% |
| Top-3 accuracy | 42/63 = 66.7% |
| Top-5 accuracy | 45/63 = 71.4% |
| MRR | 0.588 |

## Results by Query Type

| Type | n | Top-1 | Top-3 | Top-5 |
|---|---|---|---|---|
| Exact phrase | 8 | 3/8 = 38% | 6/8 = 75% | 6/8 = 75% |
| Paraphrase | 15 | 6/15 = 40% | 11/15 = 73% | 11/15 = 73% |
| Doctrine | 12 | 3/12 = 25% | 5/12 = 42% | 7/12 = 58% |
| Tooling fact | 12 | 7/12 = 58% | 8/12 = 67% | 9/12 = 75% |
| Frame diagnosis | 8 | 8/8 = 100% | 8/8 = 100% | 8/8 = 100% |
| Case memory | 8 | 4/8 = 50% | 4/8 = 50% | 4/8 = 50% |

## Misses and Diagnosis

21 queries missed (not in top-3):

### `ep_04` — 'CONFABULATED recorded so we never re-adopt these'
**Type:** exact_phrase
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §CONFABULATED`
**Top 3 actual:**
- rank 1 score=0.525  `docs/method/how-we-work-here.md §5. Quarantine uncertainty`
- rank 2 score=0.516  `docs/method/how-we-work-here.md §15. Working rule`
- rank 3 score=0.512  `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §🧹 Clean-Up`
**Diagnosis:** wrong document surfaced — possible index gap or chunk boundary issue.

### `ep_05` — 'max_in_progress_per_profile'
**Type:** exact_phrase
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §Concurrency`
**Top 3 actual:**
- rank 1 score=0.713  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §8d. CONFIRMED: the GPU-serial lever`
- rank 2 score=0.699  `docs/tooling/hermes-kanban-reference-260607.md §5.5 Remaining small unknowns`
- rank 3 score=0.659  `docs/tooling/hermes-kanban-reference-260607.md §7. Build path — now unblocked (the critical gate is cleared)`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `pp_01` — "what is BOBA's core purpose"
**Type:** paraphrase
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Mission`
**Top 3 actual:**
- rank 1 score=0.692  `docs/README.md §BOBA Corpus — Folder Map`
- rank 2 score=0.668  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §1. Larger context: BOBA (the trunk)`
- rank 3 score=0.662  `docs/core/boba-core-mission-and-commitments.md §7. What BOBA Is Not`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `pp_06` — 'preferring actions that can be undone'
**Type:** paraphrase
**Expected:** `docs/method/how-we-work-here.md §Small reversible steps`
**Top 3 actual:**
- rank 1 score=0.625  `docs/method/how-we-work-here.md §9. The human remains in the vetting loop`
- rank 2 score=0.599  `docs/method/how-we-work-here.md §14. The wobbly edge`
- rank 3 score=0.593  `docs/method/how-we-work-here.md §15. Working rule`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `pp_14` — 'how the embedding index is structured internally'
**Type:** paraphrase
**Expected:** `docs/architecture/boba-corpus-index-mve.md §How it works`
**Top 3 actual:**
- rank 1 score=0.659  `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §Corpus Index MVE`
- rank 2 score=0.611  `docs/probe-set/report.md §BOBA Probe-Set MVE Report`
- rank 3 score=0.606  `docs/architecture/boba-corpus-index-mve.md §BOBA Corpus Embedding Index — MVE`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `pp_15` — 'adding new documents to the search index'
**Type:** paraphrase
**Expected:** `docs/architecture/boba-corpus-index-mve.md §How to rebuild`
**Top 3 actual:**
- rank 1 score=0.577  `docs/method/corpus-intake-plan.md §Recommended intake order`
- rank 2 score=0.555  `docs/architecture/boba-corpus-index-mve.md §Next steps`
- rank 3 score=0.545  `docs/method/corpus-intake-plan.md §BOBA Corpus Intake Plan`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_01` — 'an AI that always agrees provides no value as a second intelligence'
**Type:** doctrine
**Expected:** `docs/core/boba-braid.md §No Loyalty Oaths`
**Top 3 actual:**
- rank 1 score=0.697  `docs/core/boba-core-mission-and-commitments.md §2. The Premise`
- rank 2 score=0.600  `docs/core/boba-braid.md §What is the Braid?`
- rank 3 score=0.593  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §1. Larger context: BOBA (the trunk)`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_03` — 'human disorientation as a feature of complex systems not personal failure'
**Type:** doctrine
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Core Commitments`
**Top 3 actual:**
- rank 1 score=0.707  `docs/core/boba-core-mission-and-commitments.md §2. The Premise`
- rank 2 score=0.646  `docs/method/how-we-work-here.md §14. The wobbly edge`
- rank 3 score=0.645  `docs/method/how-we-work-here.md §1. The basic posture`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_04` — 'running AI locally rather than routing data through cloud services'
**Type:** doctrine
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Core Commitments`
**Top 3 actual:**
- rank 1 score=0.595  `docs/core/boba-core-mission-and-commitments.md §2. The Premise`
- rank 2 score=0.586  `docs/core/boba-braid.md §Conclusion`
- rank 3 score=0.576  `docs/core/boba-braid.md §What is the Braid?`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_05` — 'resisting the tendency to tell people what they want to hear'
**Type:** doctrine
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Core Commitments`, `docs/method/how-we-work-here.md §Mirror, not cheer`
**Top 3 actual:**
- rank 1 score=0.522  `docs/method/how-we-work-here.md §14. The wobbly edge`
- rank 2 score=0.515  `docs/core/boba-braid.md §1. No Loyalty Oaths`
- rank 3 score=0.513  `docs/method/how-we-work-here.md §15. Working rule`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_07` — "why an AI should not override the human's direction"
**Type:** doctrine
**Expected:** `docs/method/how-we-work-here.md §human remains in the vetting loop`, `docs/core/boba-braid.md §Vetting vs Actuation`
**Top 3 actual:**
- rank 1 score=0.787  `docs/core/boba-core-mission-and-commitments.md §2. The Premise`
- rank 2 score=0.643  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §1. Larger context: BOBA (the trunk)`
- rank 3 score=0.632  `docs/core/boba-braid.md §What is the Braid?`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `dc_10` — 'avoiding premature closure on open questions'
**Type:** doctrine
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Core Commitments`
**Top 3 actual:**
- rank 1 score=0.597  `docs/method/how-we-work-here.md §15. Working rule`
- rank 2 score=0.589  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §7a. JEPA-collapse line — **explicitly undecided**`
- rank 3 score=0.583  `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §Hermes Approval Gate`
**Diagnosis:** wrong document surfaced — possible index gap or chunk boundary issue.

### `dc_11` — 'presenting choices without steering the outcome'
**Type:** doctrine
**Expected:** `docs/core/boba-core-mission-and-commitments.md §Core Commitments`
**Top 3 actual:**
- rank 1 score=0.614  `docs/method/how-we-work-here.md §9. The human remains in the vetting loop`
- rank 2 score=0.576  `docs/core/boba-braid.md §2. Vetting vs Actuation`
- rank 3 score=0.574  `docs/core/boba-core-mission-and-commitments.md §2. The Premise`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `tf_02` — 'how to start the hermes dispatcher process'
**Type:** tooling_fact
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §Build path`
**Top 3 actual:**
- rank 1 score=0.681  `docs/tooling/hermes-kanban-reference-260607.md §5.2 The dispatcher IS the gateway — Q2 RESOLVED ✅`
- rank 2 score=0.601  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §8c. CONFIRMED: Hermes already IS most of the scheduler`
- rank 3 score=0.581  `docs/method/how-we-work-here.md §19. Protocol completion is mandatory`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `tf_03` — 'how to follow a kanban task log in real time'
**Type:** tooling_fact
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §Build path`, `docs/tooling/hermes-kanban-reference-260607.md §GPU-serial`
**Top 3 actual:**
- rank 1 score=0.610  `docs/tooling/hermes-kanban-reference-260607.md §5.1 Concurrency — Q1 RESOLVED ✅ (the load-bearing answer)`
- rank 2 score=0.600  `docs/probe-set/implementation_plan.md §Next card`
- rank 3 score=0.583  `docs/tooling/hermes-kanban-reference-260607.md §Hermes Kanban / Dispatcher — Verified Reference`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `tf_05` — 'the flags available on hermes kanban create'
**Type:** tooling_fact
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §create`
**Top 3 actual:**
- rank 1 score=0.691  `docs/tooling/hermes-kanban-reference-260607.md §Verify-next (small, direct reads):`
- rank 2 score=0.661  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §8. The research scheduler — design + CONFIRMED Hermes mechan`
- rank 3 score=0.620  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §8c. CONFIRMED: Hermes already IS most of the scheduler`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `tf_09` — 'how to configure the hermes auxiliary approval provider'
**Type:** tooling_fact
**Expected:** `docs/tooling/hermes-kanban-reference-260607.md §Auxiliary`, `docs/tooling/hermes-kanban-reference-260607.md §Approvals`
**Top 3 actual:**
- rank 1 score=0.639  `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §Hermes Approval Gate`
- rank 2 score=0.636  `docs/tooling/hermes-kanban-reference-260607.md §Verify-next (small, direct reads):`
- rank 3 score=0.631  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §8. The research scheduler — design + CONFIRMED Hermes mechan`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `cm_01` — 'what was the first real GPU workload run in BOBA'
**Type:** case_memory
**Expected:** `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §Probe-set MVE`
**Top 3 actual:**
- rank 1 score=0.613  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §0. What this document is`
- rank 2 score=0.604  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §7b. The recalibration (durable yield, part 2): stop hand-run`
- rank 3 score=0.603  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §12. One-paragraph summary`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `cm_02` — 'what was decided about the JEPA line of work'
**Type:** case_memory
**Expected:** `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §JEPA-collapse`
**Top 3 actual:**
- rank 1 score=0.609  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §BOBA Session Record — Research-Mode Recalibration & the Rese`
- rank 2 score=0.574  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §0. What this document is`
- rank 3 score=0.568  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §11. Open decisions & TODO`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `cm_04` — 'what the smart approval smoke test verified'
**Type:** case_memory
**Expected:** `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §Worker Write-Path Bug`
**Top 3 actual:**
- rank 1 score=0.618  `docs/method/how-we-work-here.md §18. The approval gate is not the enemy`
- rank 2 score=0.608  `docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md §Hermes Approval Gate`
- rank 3 score=0.566  `docs/core/boba-braid.md §3. Trust Through Legibility`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

### `cm_08` — 'what was the outcome of the JEPA collapse experiment'
**Type:** case_memory
**Expected:** `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §Runs & results`
**Top 3 actual:**
- rank 1 score=0.709  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §2. The worked example: JEPA Experiment 1 (collapse detector `
- rank 2 score=0.664  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §BOBA Session Record — Research-Mode Recalibration & the Rese`
- rank 3 score=0.633  `docs/session-records/boba-session-record-260607-research-scheduler-and-jepa.md §12. One-paragraph summary`
**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue.

## Recommended Next Card

Based on these results:
- Significant miss rate. Recommended: audit chunking of failing source files, check whether heading-boundary chunks are too coarse, and consider paragraph-level chunking as an alternative.
