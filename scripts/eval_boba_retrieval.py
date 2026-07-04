#!/usr/bin/env python3
"""
Retrieval benchmark for the BOBA corpus index.

Evaluates top-1 accuracy, top-3 accuracy, and mean reciprocal rank (MRR)
against a set of paraphrase queries with known expected chunks.

Usage:
  python3 scripts/eval_boba_retrieval.py
  python3 scripts/eval_boba_retrieval.py --eval data/eval/retrieval_eval_expanded.jsonl
  python3 scripts/eval_boba_retrieval.py --out data/eval/retrieval_eval_results.txt
  python3 scripts/eval_boba_retrieval.py --top-k 5
  python3 scripts/eval_boba_retrieval.py --report docs/architecture/boba-retrieval-eval-report-260607.md
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


def chunk_matches_target(chunk, target):
    path_ok = chunk["source_path"].endswith(target["path"]) or target["path"] in chunk["source_path"]
    heading_ok = target["heading"].lower() in chunk["heading"].lower()
    return path_ok and heading_ok


def chunk_matches(chunk, case):
    return any(chunk_matches_target(chunk, t) for t in case["acceptable_targets"])


def load_index():
    chunks = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    embeddings = np.load(EMBEDDINGS_PATH)
    return chunks, embeddings


def load_eval(path=None):
    cases = []
    with open(path or EVAL_PATH, encoding="utf-8") as f:
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
            if chunk_matches(chunks[idx], case):
                hit_rank = rank
                break

        results.append({
            "id": case["id"],
            "type": case.get("type", "unknown"),
            "query": case["query"],
            "acceptable_targets": case["acceptable_targets"],
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
            targets = "  |  ".join(f"{t['path']}  §{t['heading']}" for t in r["acceptable_targets"])
            lines.append(f"  acceptable: {targets}")
            lines.append(f"  actual top {min(3, len(r['top_hits']))}:")
            for h in r["top_hits"][:3]:
                lines.append(f"    [{h['rank']}] score={h['score']:.3f}  {h['source_path']}  §{h['heading'][:60]}")
    else:
        lines.append("All queries hit in top-3.")

    return "\n".join(lines)


def make_report_md(results, chunks, top_k, eval_path):
    n = len(results)
    top1 = sum(1 for r in results if r["hit_rank"] == 1)
    top3 = sum(1 for r in results if r["hit_rank"] is not None and r["hit_rank"] <= 3)
    topk = sum(1 for r in results if r["hit_rank"] is not None)
    mrr  = sum(1.0 / r["hit_rank"] for r in results if r["hit_rank"] is not None) / n

    # per-type breakdown
    types = {}
    for r in results:
        t = r.get("type", "unknown")
        types.setdefault(t, {"n": 0, "top1": 0, "top3": 0, "topk": 0})
        types[t]["n"] += 1
        if r["hit_rank"] == 1:            types[t]["top1"] += 1
        if r["hit_rank"] and r["hit_rank"] <= 3: types[t]["top3"] += 1
        if r["hit_rank"]:                 types[t]["topk"] += 1

    failures = [r for r in results if r["hit_rank"] is None or r["hit_rank"] > 3]

    lines = [
        f"# BOBA Retrieval Eval Report — 2026-06-07",
        f"",
        f"## Setup",
        f"",
        f"| | |",
        f"|---|---|",
        f"| Index chunks | {len(chunks)} |",
        f"| Eval cases | {n} |",
        f"| Eval file | `{os.path.basename(eval_path)}` |",
        f"| Embedding model | {MODEL} (768 dims, via Ollama) |",
        f"| top_k | {top_k} |",
        f"",
        f"## Overall Results",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Top-1 accuracy | {top1}/{n} = {top1/n:.1%} |",
        f"| Top-3 accuracy | {top3}/{n} = {top3/n:.1%} |",
        f"| Top-{top_k} accuracy | {topk}/{n} = {topk/n:.1%} |",
        f"| MRR | {mrr:.3f} |",
        f"",
        f"## Results by Query Type",
        f"",
        f"| Type | n | Top-1 | Top-3 | Top-{top_k} |",
        f"|---|---|---|---|---|",
    ]
    type_labels = {
        "exact_phrase": "Exact phrase",
        "paraphrase": "Paraphrase",
        "doctrine": "Doctrine",
        "tooling_fact": "Tooling fact",
        "frame_diagnosis": "Frame diagnosis",
        "case_memory": "Case memory",
    }
    for tkey in ["exact_phrase", "paraphrase", "doctrine", "tooling_fact", "frame_diagnosis", "case_memory"]:
        if tkey not in types:
            continue
        d = types[tkey]
        tn = d["n"]
        lines.append(
            f"| {type_labels.get(tkey, tkey)} | {tn} "
            f"| {d['top1']}/{tn} = {d['top1']/tn:.0%} "
            f"| {d['top3']}/{tn} = {d['top3']/tn:.0%} "
            f"| {d['topk']}/{tn} = {d['topk']/tn:.0%} |"
        )

    lines += ["", "## Misses and Diagnosis", ""]
    if not failures:
        lines.append("All queries hit in top-3. No misses.")
    else:
        lines.append(f"{len(failures)} queries missed (not in top-3):\n")
        for r in failures:
            lines.append(f"### `{r['id']}` — {r['query']!r}")
            lines.append(f"**Type:** {r.get('type', 'unknown')}")
            targets = ", ".join(f"`{t['path']} §{t['heading']}`" for t in r["acceptable_targets"])
            lines.append(f"**Expected:** {targets}")
            lines.append(f"**Top 3 actual:**")
            for h in r["top_hits"][:3]:
                lines.append(f"- rank {h['rank']} score={h['score']:.3f}  `{h['source_path']} §{h['heading'][:60]}`")

            # diagnose
            top_paths = {h["source_path"] for h in r["top_hits"][:3]}
            expected_paths = {t["path"] for t in r["acceptable_targets"]}
            if not top_paths & expected_paths:
                diag = "**Diagnosis:** wrong document surfaced — possible index gap or chunk boundary issue."
            else:
                diag = "**Diagnosis:** right document, wrong chunk — heading boundary or chunk granularity issue."
            lines.append(diag)
            lines.append("")

    lines += [
        "## Recommended Next Card",
        "",
        "Based on these results:",
    ]
    if len(failures) == 0:
        lines.append("- Index quality is strong across all query types. Recommended next: expand corpus with new streams (Fog, Walk) to test retrieval on less-structured philosophical text.")
    elif len(failures) <= 5:
        lines.append("- Misses are sparse. Recommended: review miss diagnoses above, then either refine chunk boundaries for failing docs or expand acceptable_targets to cover alternate valid chunks.")
    else:
        lines.append("- Significant miss rate. Recommended: audit chunking of failing source files, check whether heading-boundary chunks are too coarse, and consider paragraph-level chunking as an alternative.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--out", default=DEFAULT_OUT)
    parser.add_argument("--eval", default=None, dest="eval_path",
                        help="Path to eval JSONL (default: data/eval/retrieval_eval.jsonl)")
    parser.add_argument("--report", default=None,
                        help="If given, write a markdown report to this path")
    args = parser.parse_args()

    eval_path = args.eval_path or EVAL_PATH
    for path, label in [(MANIFEST_PATH, "manifest"), (EMBEDDINGS_PATH, "embeddings"), (eval_path, "eval")]:
        if not os.path.exists(path):
            print(f"Missing {label}: {path}")
            sys.exit(1)

    chunks, embeddings = load_index()
    cases = load_eval(eval_path)
    print(f"Loaded {len(chunks)} chunks, {len(cases)} eval cases.")

    results = run_eval(cases, chunks, embeddings, args.top_k)
    report = summarize(results, args.top_k)

    print("\n" + report)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    print(f"\nResults written to {args.out}")

    if args.report:
        md = make_report_md(results, chunks, args.top_k, eval_path)
        os.makedirs(os.path.dirname(args.report), exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(md + "\n")
        print(f"Markdown report written to {args.report}")


if __name__ == "__main__":
    main()
