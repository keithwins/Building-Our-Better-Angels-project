# BOBA Corpus Embedding Index — MVE

**Purpose:** A local, inspectable embedding index over the BOBA repo Markdown corpus. Lets future agents (and Keith) ask "where did we already talk about this?" and get back source-attributed chunks.

**Status:** MVE — infrastructure proven, instrument not yet validated.

---

## How it works

1. `scripts/build_boba_index.py` walks all `.md` files in the repo, splits them by heading into chunks, embeds each chunk via `nomic-embed-text` (Ollama, GPU-accelerated, 768 dims), and writes:
   - `data/index/chunk_manifest.jsonl` — one JSON line per chunk: `source_path`, `heading`, `text`. Committed.
   - `data/index/embeddings.npy` — float32 array, shape `(N_chunks, 768)`. **Not committed** (binary, regenerable).

2. `scripts/search_boba_corpus.py` embeds a query via the same model, computes cosine similarity against the index, and returns the top-k chunks with source paths.

## How to rebuild

```bash
cd ~/boba_work/Building-Our-Better-Angels-project
python3 scripts/build_boba_index.py
```

Requires: Ollama running with `nomic-embed-text` loaded (`ollama pull nomic-embed-text`), `numpy`, `requests`.

## How to search

```bash
python3 scripts/search_boba_corpus.py "your query"
python3 scripts/search_boba_corpus.py --smoke-test   # runs 4 canonical queries
```

## What is and isn't committed

| File | Committed | Why |
|---|---|---|
| `data/index/chunk_manifest.jsonl` | Yes | Text only, human-readable, small |
| `data/index/embeddings.npy` | No | Binary, regenerable from manifest + model |
| `data/index/search_smoke_test.txt` | No | Generated artifact |

## Benchmark

`data/eval/retrieval_eval.jsonl` contains 8 paraphrase queries (not exact phrases) with expected source paths and heading substrings. Run with:

```bash
python3 scripts/eval_boba_retrieval.py
python3 scripts/eval_boba_retrieval.py --top-k 5 --out data/eval/retrieval_eval_results.txt
```

Reports top-1 accuracy, top-3 accuracy, top-k accuracy, MRR, and prints failures with actual top-3 hits. Results file is not committed.

Example queries and their expected targets:

| Query | Expected section |
|---|---|
| overwhelmed by unfamiliar technical system | §14. The wobbly edge |
| avoid making Keith a human clipboard | §9. The human remains in the vetting loop |
| plausible but unchecked claims | §5. Quarantine uncertainty |
| one heavy GPU job at a time | §5.1 Concurrency (hermes-kanban-reference) |
| invented Hermes configuration values | §6. CONFABULATED |
| trust vs inspectability tradeoff | §2. Trust is larger than inspection |

---

## Limitations (MVE scope)

- No incremental update — rebuild from scratch when corpus changes.
- No chunking overlap — heading boundaries only.
- Single model — `nomic-embed-text`. Not yet compared against alternatives.
- Similarity scores are relative, not calibrated — useful for ranking, not thresholding.

## Next steps

- Run probe-set categories through this index to validate discriminability.
- Compare `nomic-embed-text` vs `qwen3:8b` embeddings on the same corpus.
- Add overlap/sliding-window chunking once corpus grows beyond ~50 files.
