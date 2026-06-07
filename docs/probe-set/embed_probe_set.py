#!/usr/bin/env python3
"""
BOBA Probe-Set MVE embedding script.

Loads:
  - categories.yaml
  - reference_texts.jsonl
  - contrast_texts.jsonl

Writes:
  - results.json
  - similarity_matrix.csv
  - report.md

This script does not train anything. It uses sentence-transformers if already
available. If the dependency is missing, it exits with a clear message.
"""

import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATEGORIES = ROOT / "categories.yaml"
REFERENCE = ROOT / "reference_texts.jsonl"
CONTRAST = ROOT / "contrast_texts.jsonl"


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{i}: invalid JSON: {e}") from e
            for key in ("id", "category", "text"):
                if key not in obj or not isinstance(obj[key], str) or not obj[key].strip():
                    raise SystemExit(f"{path}:{i}: missing/invalid required field {key!r}")
            rows.append(obj)
    return rows


def load_category_ids(path: Path):
    try:
        import yaml
    except ImportError:
        raise SystemExit(
            "Missing dependency: PyYAML is not installed. Install pyyaml or provide "
            "a JSON categories file. No files were written."
        )

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "categories" not in data:
        raise SystemExit("categories.yaml must contain a top-level 'categories' list.")
    ids = []
    for i, item in enumerate(data["categories"], 1):
        if not isinstance(item, dict) or "id" not in item:
            raise SystemExit(f"categories.yaml category #{i} missing id.")
        ids.append(item["id"])
    return ids


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main():
    category_ids = set(load_category_ids(CATEGORIES))
    refs = load_jsonl(REFERENCE)
    cons = load_jsonl(CONTRAST)
    all_rows = [{"kind": "reference", **r} for r in refs] + [{"kind": "contrast", **r} for r in cons]

    for row in all_rows:
        if row["category"] not in category_ids:
            raise SystemExit(f"{row['id']} uses unknown category {row['category']}")

    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        raise SystemExit(
            "Missing dependency: sentence-transformers is not installed. "
            "No embeddings were computed and no output files were written."
        )

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)
    texts = [r["text"] for r in all_rows]
    embeddings = model.encode(texts, normalize_embeddings=True).tolist()

    matrix = []
    for i, row_i in enumerate(all_rows):
        for j, row_j in enumerate(all_rows):
            matrix.append({
                "id_a": row_i["id"],
                "kind_a": row_i["kind"],
                "category_a": row_i["category"],
                "id_b": row_j["id"],
                "kind_b": row_j["kind"],
                "category_b": row_j["category"],
                "cosine": cosine(embeddings[i], embeddings[j]),
            })

    results = {
        "model": model_name,
        "num_reference": len(refs),
        "num_contrast": len(cons),
        "num_categories": len(category_ids),
        "items": all_rows,
    }

    (ROOT / "results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

    with (ROOT / "similarity_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(matrix[0].keys()))
        writer.writeheader()
        writer.writerows(matrix)

    report = [
        "# BOBA Probe-Set MVE Report",
        "",
        f"Embedding model: `{model_name}`",
        f"Reference anchors: {len(refs)}",
        f"Contrast anchors: {len(cons)}",
        f"Categories: {len(category_ids)}",
        "",
        "This is an infrastructure MVE, not proof of alignment.",
        "Interpretation should focus on whether the coordinate surface is useful",
        "for comparing BOBA-positive anchors against nearby failure modes.",
        "",
    ]
    (ROOT / "report.md").write_text("\n".join(report), encoding="utf-8")
    print("Wrote results.json, similarity_matrix.csv, and report.md")


if __name__ == "__main__":
    main()
