#!/usr/bin/env python3
"""
Search the BOBA corpus embedding index.

Usage:
  python3 scripts/search_boba_corpus.py "your query here"
  python3 scripts/search_boba_corpus.py --smoke-test
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
SMOKE_TEST_PATH = os.path.join(INDEX_DIR, "search_smoke_test.txt")
OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text"

SMOKE_QUERIES = [
    "wobbly edge",
    "trust beyond audit",
    "Hermes gpu profile",
    "quarantine uncertainty",
]


def embed(text):
    resp = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": text}, timeout=60)
    resp.raise_for_status()
    return np.array(resp.json()["embedding"], dtype=np.float32)


def cosine_similarity(a, b_matrix):
    a = a / (np.linalg.norm(a) + 1e-9)
    norms = np.linalg.norm(b_matrix, axis=1, keepdims=True) + 1e-9
    b_norm = b_matrix / norms
    return b_norm @ a


def load_index():
    chunks = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    embeddings = np.load(EMBEDDINGS_PATH)
    return chunks, embeddings


def search(query, chunks, embeddings, top_k=3):
    q_vec = embed(query)
    scores = cosine_similarity(q_vec, embeddings)
    top_idx = np.argsort(scores)[::-1][:top_k]
    return [(float(scores[i]), chunks[i]) for i in top_idx]


def format_result(rank, score, chunk):
    return (
        f"  [{rank}] score={score:.3f}  {chunk['source_path']}"
        + (f"  §{chunk['heading']}" if chunk["heading"] else "")
        + f"\n      {chunk['text'][:120].replace(chr(10), ' ')}..."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--smoke-test", action="store_true")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    if not os.path.exists(MANIFEST_PATH) or not os.path.exists(EMBEDDINGS_PATH):
        print("Index not found. Run scripts/build_boba_index.py first.")
        sys.exit(1)

    chunks, embeddings = load_index()
    print(f"Loaded {len(chunks)} chunks.")

    queries = SMOKE_QUERIES if args.smoke_test else [args.query]
    if not queries[0]:
        parser.print_help()
        sys.exit(1)

    output_lines = []
    for query in queries:
        print(f"\nQuery: {query!r}")
        results = search(query, chunks, embeddings, top_k=args.top_k)
        for rank, (score, chunk) in enumerate(results, 1):
            line = format_result(rank, score, chunk)
            print(line)
            output_lines.append(f"Query: {query}\n{line}\n")

    if args.smoke_test:
        with open(SMOKE_TEST_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
        print(f"\nSmoke test results written to {SMOKE_TEST_PATH}")


if __name__ == "__main__":
    main()
