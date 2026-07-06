---
title: Blob & Vector Sidecars v0 (spec)
status: DRAFT — provisional, pre-build
date: 2026-07-04
companions: system-fit-integration-map.md (§4 Seam 2), ../core/ephemeris-charter.md, ../core/continuity-and-decision-lineage.md, boba-corpus-index-mve.md
scope: the two heavy substrates Asterisms must NOT swallow — large-media bytes and embedding vectors
---

# Blob & Vector Sidecars v0

The system-fit map (`system-fit-integration-map.md` §4) names two heavy substrates
that would bloat or slow the immutable provenance spine if the ledger tried to hold
them directly: **large audio/video bytes** and **embedding vectors**. Both are
handled by the same move — a **sidecar**: a companion store that carries the weight
while Asterisms keeps only the lean provenance record, joined by `ast:` id and
content hash.

This is **one spec for two sidecars** because the vector store's *canonical bytes
live in the blob store* — they share a foundation. Two parts: §2 blob store, §3
vector index, on top of §1 the shared contract they both obey.

**Status:** DRAFT for review, pre-build. No code exists. Written against the actual
`asterisms_registry.py` v0 (the `register_file` copy path, streaming `sha256_file`,
the `embed`/`index` transform kinds, `_governance_for_output` inheritance). This is
the review surface before machinery.

## 1. The shared sidecar contract

Every sidecar in the system obeys the same three rules. They generalize the pattern
the Ephemeris already established (a canonical append-only store + a disposable
projection):

1. **Spine holds provenance; sidecar holds weight.** Asterisms holds the material
   row, manifest, governance envelope, and lineage. The sidecar holds the bytes or
   the vectors. Neither duplicates the other's job.
2. **Join by `ast:` id + content hash.** A sidecar entry is addressed by its
   content hash; the Asterisms material points at it; the durable join key is
   *(material id, sha256)*. Given a material you can find its bytes/vector; given a
   sidecar hit you can resolve full provenance.
3. **Canonical stores are append-only; derived stores are rebuildable and
   disposable.** The blob CAS is canonical (append-only, deletion only via audited
   `retire`). The ANN index is derived — it can be dropped and rebuilt from the
   canonical vectors at any time, and is never authoritative. (Same law as the
   Ephemeris JSONL-truth vs. its rebuildable index.)

Nothing here changes existing small-file behavior: `register_file` still copies
small records into `10-record/` verbatim — right for a 6 KB note, legible, cheap.
The sidecars are **additive**, for the heavy cases.

## 2. Blob store (large-media bytes)

### 2.1 Problem
`register_file` copies bytes into `10-record/<record_id>/` and hashes the whole
file. Right for notes; wrong for A/V — it (a) turns the ledger tree into a media
dump, (b) makes a *fresh full copy* every time the same media is registered (no
dedup), and (c) couples big-byte movement to the registration critical path.
(Streaming hashing itself is fine — `sha256_file` already reads in 1 MB chunks.)

### 2.2 Content-addressed store (CAS)
Bytes are stored **once, keyed by hash** — git-style sharding:

```
$ASTERISMS_HOME/60-blobs/<sha256[:2]>/<sha256>
```

(`60-blobs/` extends the existing numeric grammar: `00-incoming … 40-ledger …
90-system, 99-backups`.) Because the filename *is* the content hash, blobs are
**immutable by construction** — changing bytes changes the name — and identical
media registered twice dedups to one blob.

### 2.3 Two storage modes
| mode | what happens | for |
|------|--------------|-----|
| **managed** | stream-hash, copy into CAS once (skip if hash already present) | media we want to own + preserve |
| **referenced** | stream-hash, record location + size, **no copy** | files too large to duplicate, or externally authoritative |

### 2.4 The material it produces
A new registration path, additive to the registry:

```
register_blob(source, mode="managed"|"referenced",
              content_type=..., media=<probe>, governance=...) -> AsterismsMaterial
```

It writes a normal material + manifest + lineage (a `capture`/`register`
transformation), but instead of a `10-record/` byte copy the material carries a
**blob descriptor** in its metadata:

```json
"blob": {
  "sha256": "…", "size_bytes": 734003200,
  "store": "managed",
  "location": "60-blobs/ab/ab34…",        // or "file:///…", "s3://…" when referenced
  "content_type": "video/mp4",
  "media": { "duration_s": 612.4, "container": "mp4",
             "video": {"w":1920,"h":1080,"fps":30},
             "audio": {"sr":48000,"ch":2} }
}
```

`content_sha256` on the material = the blob hash, so the existing provenance and
`register`/`derive`/`anchor` machinery all work unchanged.

### 2.5 Integrity, immutability, deletion
- **Verify lazily**, not on every read; a `blob verify [--all]` sweep re-hashes and
  reports drift.
- **No silent deletion.** Blobs are append-only in spirit. Garbage collection (a
  blob with zero referencing materials) is **out of scope for v0**; when added it
  is an *audited* `retire` transformation with a tombstone, never a quiet unlink —
  per `continuity-and-decision-lineage.md`.

### 2.6 Time-media anchors (closes system-fit Seam 3)
Anchors already store arbitrary JSON in `anchors.selector_json`, so time-based
selection needs only a defined vocabulary:

```json
{"type":"time-range","start_s":12.0,"end_s":18.5}     // audio + video
{"type":"frame","index":900}                          // video still
{"type":"frame-range","start":900,"end":960}
```

v0 defines `time-range` + `frame`. This lets a formation cite *"0:12–0:18 of this
recording"* the way it cites a line-range of a note today.

## 3. Vector index (embeddings)

### 3.1 The split
An embedding is **two artifacts with two homes**:
- the **provenance** (which source, which model, which transform) → an Asterisms
  **derivative material** (`embed` transform);
- the **vector** → canonical bytes in the **blob CAS** (§2), and a queryable copy in
  a **derived ANN index** (disposable).

So embeddings *reuse the blob sidecar* for canonical storage and add only a
rebuildable index on top.

### 3.2 Creating an embedding
```
create_embedding(source_material_id, vector, model, metric="cosine",
                 normalized=True) -> AsterismsMaterial   # kind="embed"
```
- Stores the vector as a **managed blob** (raw float32 / `.npy`), hash-addressed.
- Creates a derivative material via the existing derivative path, with descriptor:
  ```json
  "embedding": {"model":"…","dim":1024,"metric":"cosine","normalized":true,
                "vector_blob_sha256":"…"}
  ```
- Lineage: `source_material → (embed) → embedding_material`, preserved by the
  existing transformation machinery.
- **Governance rides for free.** `_governance_for_output` already merges input
  governance into derivatives — so *an embedding of a restricted recording is itself
  restricted, automatically.* (A real safety property; state it, keep it.)

### 3.3 The ANN index (derived, disposable)
```
70-index/<model>/…            // one index space per embedding model
```
- `vector_query(query_vector, k, model) -> [(material_id, score)]` — returns
  **`ast:` material ids + scores**; the caller resolves provenance via Asterisms.
- `reindex(model)` — rebuild the index from scratch by scanning `embed`-derivative
  materials and reading their canonical vectors from the blob CAS. Because it is
  derived, it may be dropped and rebuilt freely and is never the source of truth.
- **Re-embedding / model change** → a *new* `embed` derivative (new transform); the
  old embedding is retained (immutability). Index spaces are per-model, so a new
  model builds a new space rather than overwriting the old.
- **Staleness**: when a source material is superseded, its embedding entries are
  marked stale, not deleted; `reindex` reconciles.

### 3.4 Relationship to the existing corpus index
This generalizes `boba-corpus-index-mve.md` / the live retrieval index (already the
vector-sidecar pattern) into the standard shape: canonical vectors in CAS with
Asterisms provenance, a rebuildable ANN projection for query.

## 4. Compatibility & routing
- `register_file` (small-file copy) is **unchanged**.
- A convenience `register(path)` may **auto-route by size**: below a threshold →
  today's `10-record/` copy; above → `register_blob(managed)`. Threshold is an open
  question (see §6).
- Everything is additive: no schema migration for existing materials; the blob and
  embedding descriptors live in the already-present `metadata_json`.

## 5. Scope
**v0 does:** the blob CAS (`60-blobs/`) with managed + referenced modes; `register_blob`
with a blob descriptor; lazy `blob verify`; time-range + frame anchors;
`create_embedding` storing canonical vectors as managed blobs with inherited
governance; a per-model ANN index with `vector_query` + `reindex`.

**v0 does *not*:** blob garbage collection / deletion (audited `retire` comes
later); media probing beyond basic container/duration/dims (a `probe` adapter is
its own concern); distributed/remote blob backends (the `location` field leaves room
— `file://`, `s3://` — but v0 is local); automatic re-embedding on supersede;
cross-model query fusion.

## 6. Open questions (quarantined)
- **Auto-route threshold.** What size flips `register()` from `10-record/` copy to
  managed blob? (Leaning a few MB; make it configurable.)
- **Vector encoding on disk.** Raw little-endian float32 vs. `.npy` vs. a packed
  shard per model. (Leaning `.npy` for legibility + tooling.)
- **ANN backend.** Flat/brute-force for v0 (exact, tiny corpus) vs. HNSW/IVF later.
  (Leaning flat for v0 — the retrieval corpus is small; upgrade when it isn't.)
- **Where the ANN index lives.** `70-index/` (proposed) vs. under `90-system/`.
  It's derived/disposable either way.
- **Referenced-mode integrity.** For `file://` referenced blobs we don't own, what
  happens when the external bytes change under us? (Leaning: `verify` flags the
  hash drift; the ledger's recorded hash stays authoritative as *what was seen*.)

---

*Provisional, pre-build. The §1 contract is the durable part; §2–§3 are the first
concrete application of it. Next step if approved: implement `register_blob` +
`60-blobs/` CAS first (unblocks A/V intake through Porter), then `create_embedding`
+ the ANN projection. Coordinate with whoever holds the `asterisms-system` lane —
this touches the registry.*
