#!/usr/bin/env python3
"""
Retrieval benchmark for the BOBA corpus index.

Evaluates top-1 accuracy, top-3 accuracy, and mean reciprocal rank (MRR)
against a set of paraphrase queries with known expected chunks.

Usage:
  python3 scripts/eval_boba_retrieval.py
  python3 scripts/eval_boba_retrieval.py --out data/eval/retrieval_eval_results.txt
  python3 scripts/eval_boba_retrieval.py --top-k 5
"""

import argparse
import json
import os
import sys

import numpy as np
import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_DIR = os.path.join(REPO_ROOT, "data", "index")
MANIFEST_PATH = os.path.join(INDEX_DIR, "chunk_manifest.jsonl")
EMBEDDINGS_PATH = os.path.join(INDEX_DIR, "embeddings.npy")
EVAL_PATH = os.path.join(REPO_ROOT, "data", "eval", "retrieval_eval.jsonl")
DEFAULT_OUT = os.path.join(REPO_ROOT, "data", "eval", "retrieval_eval_results.txt")
OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text"


def embed(text):
    resp = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": text}, timeout=60)
    resp.raise_for_status()
    return np.array(resp.json()["embedding"], dtype=np.float32)


def cosine_similarity(a, b_matrix):
    a = a / (np.linalg.norm(a) + 1e-9)
    norms = np.linalg.norm(b_matrix, axis=1, keepdims=True) + 1e-9
    b_norm = b_matrix / norms
    return b_norm @ a


def chunk_matches(chunk, expected_path, expected_heading):
    path_ok = chunk["source_path"].endswith(expected_path) or expected_path in chunk["source_path"]
    heading_ok = expected_heading.lower() in chunk["heading"].lower()
    return path_ok and heading_ok


def load_index():
    chunks = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    embeddings = np.load(EMBEDDINGS_PATH)
    return chunks, embeddings


def load_eval():
    cases = []
    with open(EVAL_PATH, encoding="utf-8") as f:
        for line in f:
            cases.append(json.loads(line))
    return cases


def run_eval(cases, chunks, embeddings, top_k):
    results = []
    for case in cases:
        q_vec = embed(case["query"])
        scores = cosine_similarity(q_vec, embeddings)
        ranked = np.argsort(scores)[::-1][:top_k]

        hit_rank = None
        for rank, idx in enumerate(ranked, 1):
            if chunk_matches(chunks[idx], case["expected_path"], case["expected_heading"]):
                hit_rank = rank
                break

        results.append({
            "id": case["id"],
            "query": case["query"],
            "expected_path": case["expected_path"],
            "expected_heading": case["expected_heading"],
            "hit_rank": hit_rank,
            "top_hits": [
                {
                    "rank": r + 1,
                    "score": float(scores[idx]),
                    "source_path": chunks[idx]["source_path"],
                    "heading": chunks[idx]["heading"],
                }
                for r, idx in enumerate(ranked)
            ],
        })
    return results


def summarize(results, top_k):
    n = len(results)
    top1 = sum(1 for r in results if r["hit_rank"] == 1)
    top3 = sum(1 for r in results if r["hit_rank"] is not None and r["hit_rank"] <= 3)
    topk = sum(1 for r in results if r["hit_rank"] is not None)
    mrr = sum(1.0 / r["hit_rank"] for r in results if r["hit_rank"] is not None) / n

    lines = [
        f"Eval: {n} queries  |  model: {MODEL}  |  top_k={top_k}",
        f"Top-1 accuracy : {top1}/{n} = {top1/n:.1%}",
        f"Top-3 accuracy : {top3}/{n} = {top3/n:.1%}",
        f"Top-{top_k} accuracy: {topk}/{n} = {topk/n:.1%}",
        f"MRR            : {mrr:.3f}",
        "",
    ]

    failures = [r for r in results if r["hit_rank"] is None or r["hit_rank"] > 3]
    if failures:
        lines.append(f"--- Failures / misses (not in top-3) ---")
        for r in failures:
            lines.append(f"\n[{r['id']}] {r['query']!r}")
            lines.append(f"  expected: {r['expected_path']}  §{r['expected_heading']}")
            lines.append(f"  actual top {min(3, len(r['top_hits']))}:")
            for h in r["top_hits"][:3]:
                lines.append(f"    [{h['rank']}] score={h['score']:.3f}  {h['source_path']}  §{h['heading'][:60]}")
    else:
        lines.append("All queries hit in top-3.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--out", default=DEFAULT_OUT)
    args = parser.parse_args()

    for path, label in [(MANIFEST_PATH, "manifest"), (EMBEDDINGS_PATH, "embeddings"), (EVAL_PATH, "eval")]:
        if not os.path.exists(path):
            print(f"Missing {label}: {path}")
            sys.exit(1)

    chunks, embeddings = load_index()
    cases = load_eval()
    print(f"Loaded {len(chunks)} chunks, {len(cases)} eval cases.")

    results = run_eval(cases, chunks, embeddings, args.top_k)
    report = summarize(results, args.top_k)

    print("\n" + report)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    print(f"\nResults written to {args.out}")


if __name__ == "__main__":
    main()
