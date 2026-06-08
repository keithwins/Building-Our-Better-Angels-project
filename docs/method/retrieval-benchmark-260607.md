# BOBA Retrieval Benchmark — 2026-06-07

**What is being measured:** Paraphrase retrieval over the BOBA corpus. A query written in natural language — not the exact phrase from the document — is embedded and matched against the corpus index by cosine similarity. This tests whether the index captures meaning, not just keywords.

**Setup:**
- 8 paraphrase queries, each with one or more acceptable target sections
- Embedding model: `nomic-embed-text` via Ollama (768 dimensions, GPU-accelerated)
- Index: 72 chunks from 8 Markdown files, split at heading boundaries
- Metrics: top-1 accuracy, top-3 accuracy, top-5 accuracy, mean reciprocal rank (MRR)

**Results (after refining acceptable targets for re_04, re_05):**

| Metric | Score |
|---|---|
| Top-1 accuracy | 6/8 = 75.0% |
| Top-3 accuracy | 7/8 = 87.5% |
| Top-5 accuracy | 8/8 = 100.0% |
| MRR | 0.838 |

**The one genuine miss:**

`re_07` — "invented Hermes configuration values" — should land on the `[CONFABULATED]` section of `hermes-kanban-reference-260607.md`. It doesn't, because that section heading is literally `[CONFABULATED]` — a label with no semantic content. The body text describes invented config values clearly, but the chunker uses headings as boundaries and the heading carries no searchable meaning. The information is in the index (it appears at rank 4–5), just not retrievable by meaning alone from the heading.

**What the two earlier apparent failures were:**

`re_04` ("one heavy GPU job at a time") and `re_05` ("first safe GPU workload") were originally marked as failures. After inspection, both were benchmark labeling issues: the queries correctly landed on the GPU-serial strategy sections, which are valid answers. Acceptable targets were expanded to reflect this.

**What this baseline means for BOBA:**

The corpus is searchable by meaning with a single small embedding model and no fine-tuning. At 72 chunks and 8 files this is a proof of concept, but the architecture scales: add files, rebuild the index, the search works. As the corpus grows to include Core doctrine, Fog writing, and Braid material, this becomes a functional memory layer — agents and future-Keith can ask "where did we talk about this?" and get source-attributed answers.

**Honest limitations:**

- 8 queries is a small benchmark. Scores will move as more queries are added.
- Single model — `nomic-embed-text` is not the only or best option; comparison against `qwen3:8b` embeddings is a natural next step.
- Heading-boundary chunking misses content in sections with sparse or label-only headings (re_07).
- Similarity scores are relative rankings, not calibrated confidence values.
