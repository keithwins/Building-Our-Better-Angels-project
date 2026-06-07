# BOBA Probe-Set MVE Implementation Plan

## Purpose
Create a minimal, local, non-training probe-set instrument for comparing candidate embedding/model representations against BOBA-positive anchors and nearby failure-mode contrasts.

## Inputs
- `seed.md`: human-authored BOBA seed.
- `categories.yaml`: category definitions.
- `reference_texts.jsonl`: BOBA-positive anchor passages.
- `contrast_texts.jsonl`: nearby failure-mode contrast passages.

## First executable script
Create `embed_probe_set.py`.

The script should:
1. Load `reference_texts.jsonl` and `contrast_texts.jsonl`.
2. Embed all passages using one local embedding path.
3. Compute cosine similarity matrix.
4. Save:
   - `results.json`
   - `similarity_matrix.csv`
   - `report.md`

## Candidate embedding paths
Prefer locally available, inspectable options:
1. Python `sentence-transformers` if installed.
2. A small installable SentenceTransformer such as `all-MiniLM-L6-v2`, if acceptable.
3. Ollama embedding models only after confirming `ollama list` includes an embedding-capable model.

Do not use arbitrary model names without checking availability.

## Success criteria
- No placeholder passages.
- All files are present and parseable.
- Every category has at least one reference and one contrast.
- The embedding script runs without training.
- The report distinguishes infrastructure success from instrument validity.
- The result is treated as a first coordinate surface, not as proof of alignment.

## Next card
Create a Kanban card to validate the corpus files and draft `embed_probe_set.py`, without running training and without modifying files outside this workspace.
