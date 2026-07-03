#!/usr/bin/env python3
"""
Build a local embedding index over the BOBA repo Markdown corpus.

Outputs:
  data/index/chunk_manifest.jsonl  — text chunks + metadata (committed)
  data/index/embeddings.npy        — embedding vectors (not committed)

Usage:
  python3 scripts/build_boba_index.py
"""

import json
import os
import re
import sys

import numpy as np
import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_DIR = os.path.join(REPO_ROOT, "data", "index")
MANIFEST_PATH = os.path.join(INDEX_DIR, "chunk_manifest.jsonl")
EMBEDDINGS_PATH = os.path.join(INDEX_DIR, "embeddings.npy")
OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text"
EXCLUDED_PATH_PARTS = {
    ".git",
    "__pycache__",
    "docs/probe-set/archive",
}


def find_md_files(root):
    for dirpath, _, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, REPO_ROOT)
        rel_dir_posix = "." if rel_dir == "." else rel_dir.replace(os.sep, "/")
        if any(
            rel_dir_posix == excluded or rel_dir_posix.startswith(f"{excluded}/")
            for excluded in EXCLUDED_PATH_PARTS
        ):
            continue
        for fname in sorted(filenames):
            if fname.endswith(".md"):
                yield os.path.join(dirpath, fname)


def chunk_markdown(text, source_path):
    """Split on headings; yield (heading, body) pairs."""
    rel_path = os.path.relpath(source_path, REPO_ROOT)
    lines = text.splitlines(keepends=True)
    current_heading = ""
    current_lines = []

    def flush(heading, lines):
        body = "".join(lines).strip()
        if body:
            return {"source_path": rel_path, "heading": heading, "text": body}
        return None

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            chunk = flush(current_heading, current_lines)
            if chunk:
                yield chunk
            current_heading = m.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    chunk = flush(current_heading, current_lines)
    if chunk:
        yield chunk


def embed(text):
    resp = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": text}, timeout=60)
    resp.raise_for_status()
    return resp.json()["embedding"]


def main():
    os.makedirs(INDEX_DIR, exist_ok=True)

    chunks = []
    for md_path in find_md_files(REPO_ROOT):
        with open(md_path, encoding="utf-8") as f:
            text = f.read()
        for chunk in chunk_markdown(text, md_path):
            chunks.append(chunk)

    print(f"Found {len(chunks)} chunks across {REPO_ROOT}")

    embeddings = []
    for i, chunk in enumerate(chunks):
        print(f"  [{i+1}/{len(chunks)}] {chunk['source_path']} — {chunk['heading'][:50]}")
        vec = embed(chunk["text"])
        embeddings.append(vec)

    # Write manifest (no vectors — kept small and committed)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk) + "\n")

    # Write embeddings array (not committed)
    np.save(EMBEDDINGS_PATH, np.array(embeddings, dtype=np.float32))

    print(f"\nWrote {len(chunks)} chunks to {MANIFEST_PATH}")
    print(f"Wrote embeddings ({len(embeddings)}×{len(embeddings[0])}) to {EMBEDDINGS_PATH}")


if __name__ == "__main__":
    main()
