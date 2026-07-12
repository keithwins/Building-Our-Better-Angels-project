---
title: System Fit — Integration Map (v0)
status: DRAFT — provisional; fit test accepted
date: 2026-07-04
companions: ../core/ephemeris-charter.md, ../core/continuity-and-decision-lineage.md, boba-metamemory-and-lora-adaptation.md, boba-corpus-index-mve.md
question: will Asterisms, Porter, voice, Understory, and future audio/video/embedding modalities fit together gracefully?
---

# System Fit — Integration Map (v0)

How the parts of the system fit together as it grows to hold **audio experiences,
video experiences, embeddings, and other modalities** — and the one discipline
that keeps that fit graceful.

This is an architecture note, not a build order. It names the grain of the wood.

## 1. The organizing principle — one spine, many spokes

There is a single architectural move underneath the whole system. The evidence
that it is *real* and not imposed is that it has already been arrived at
independently more than once:

- **Ephemeris ↔ Asterisms** — the time-store references the space-store by
  `ast:` id rather than duplicating it (`ephemeris-charter.md`).
- **The retrieval index** — vectors live in their own index; provenance stays in
  the ledger (`boba-corpus-index-mve.md`).
- **The Metamemory Angel** — compacts session traces, then *commits the clean
  result into the Asterisms ledger* and registers schema changes as
  transformations (`boba-metamemory-and-lora-adaptation.md`).

Generalized:

> **Asterisms is the immutable provenance spine.** Everything else is a **spoke**
> that keeps its own heavy or specialized substrate and **cross-references the
> spine by `ast:` id.** No spoke reimplements provenance; the spine never swallows
> a spoke's heavy runtime.

Asterisms was built for this: its contract declares itself domain-general —
*"papers, chats, code, images, lab results… one continuous field,"* **"do not
build domain silos"** — and its transformation vocabulary already names
`transcribe`, `render`, `embed`, `index`. The foundation runs the right way.

## 2. The fit test

For any new component or modality, one question decides whether it fits gracefully:

> **Does it register its provenance in Asterisms and keep its own weight,
> referencing the spine by `ast:` id?**

- **Fits** — a spoke that lands its lineage/governance record on the spine and
  holds its heavy/specialized substrate (bytes, vectors, playback, model runtime)
  in its own store, pointing back by id.
- **Misfit A — the silo:** a component that keeps a private store with **no ledger
  link.** (This is what voice and Understory are *today* — fine as vertical
  slices, a problem if left unwired.)
- **Misfit B — the swallow:** a component that **dumps heavy bytes or vectors into
  the ledger**, turning the immutable provenance spine into a media dump or a
  vector database.

## 3. Current components, grounded

| Component | Role | Spine link today | Note |
|-----------|------|------------------|------|
| **Asterisms** | provenance spine (space/memory/lineage) | — (it *is* the spine) | immutable; modality-agnostic by design |
| **Porter** | Asterisms **intake stoma** (membrane passage) | writes through to the Registry API | current intake implementation; not the only possible intake stoma |
| **Ephemeris** | coordination (time/motion) | references `ast:` ids | v0 CLI exists; still thin vs charter ambition; live log outside repo |
| **Voice workbench** | audio capture → local ASR → task packet | **none yet (silo)** | output is *already bundle-shaped* (wav + jsonl + md) |
| **Understory** | transcript analysis / validation clips | **none yet (silo)** | overlaps voice on local transcription |
| **Retrieval index** | embedding retrieval | references `ast:` ids | the vector-sidecar pattern, already live |
| **Metamemory Angel** | entropy-reducing memory co-processor | commits into the ledger | candidate; already spine-shaped |

## 4. The three seams where the work is

### Seam 1 — Intake: one mouth, not N silos
Voice-workbench's session directory (`wav + events.jsonl + transcript.md +
task-packet`) is *already* a Porter-ingestible **bundle**, and Asterisms already
has bundle registration for multi-artifact captures. Wiring it is natural; it just
isn't done. Understory is the same shape.

**Decision:** Porter is the **current sole intake stoma** for anything crossing
inward into Asterisms. Dedup, governance, and consent live in one guarded place
(bound judgment under the stoma’s charter; escalate when the charter does not
decide). Point tools stay specialists at the edge and *emit* bundles; Porter
registers them. Other intake stomata may exist later under the same stoma
protocol; they are not free silos.

### Seam 2 — The two heavy substrates the spine must not swallow
Same sidecar pattern, applied twice more:

- **Blobs (large A/V).** `register_file` currently *copies bytes into `10-record/`
  and hashes the whole file.* Right for a 6 KB note; wrong for a video library —
  it turns the ledger into a media dump and re-hashes gigabytes. The ledger should
  hold the **provenance record** (sha256, manifest, governance, lineage); the bytes
  belong in a **content-addressed blob store** (or stay by-reference for very large
  files), with the material pointing at it. **Decide before volume — migrating a
  byte-copying ledger later is the painful path.**
- **Embeddings.** An embedding *is* a derivative material (provenance: which model,
  which source, `embed` transform) → that belongs on the spine. The **vector**
  belongs in an ANN index for retrieval → not the ledger. Cross-reference by id.
  Identical shape to Ephemeris ↔ Asterisms; the retrieval index already does this.

### Seam 3 — Time-based media: time-anchors, and "experience" across the pair
Anchors already accept arbitrary JSON selectors, so `{type:"time-range", start,
end}` / frame selectors just need a defined vocabulary — the model anticipated it.

The deeper distinction: an **"audio/video experience" is two things.**
- The **artifact** — a rendered derivative with lineage to its sources — is an
  **Asterisms** material (`render` transform, lineage preserved).
- The **unfolding** — live, interactive, temporal — is **Ephemeris** territory.

This is exactly where the space/time pairing earns its keep: **Asterisms holds the
experience-as-object; Ephemeris holds the experience-as-it-happens.** Naming it now
prevents cramming live/temporal media into the immutable store.

## 5. Three honest risks

1. **Immutability vs. media churn.** The copy-bytes-preserve doctrine is right for
   provenance and wrong for large binaries. The **blob decision** is the one not to
   defer.
2. **A/V governance is heavier than text.** Voices and faces carry consent and
   sensitivity that text usually does not. The generic governance envelope inherits
   through derivatives (good), but the *policies* must be first-class **at the
   membrane (**Porter intake stoma**) — that is where recordings enter.
3. **Two overlapping audio tools.** Voice-workbench and Understory both transcribe
   locally — duplicated ASR setup and duplicated session storage. Not urgent, but
   *"is transcription one shared capability or two?"* is a graceful-fit smell that
   will want an answer.

## 6. Net

The grain runs the right way; the foundation was built domain-general on purpose.

- **Near-term graceful-fit move (small):** give voice + Understory the **Porter
  intake seam** — their outputs are already bundle-shaped.
- **Design work worth doing before A/V scales:** the canonical
  **[blob + vector sidecar spec](../../../asterisms-system/docs/blob-and-vector-sidecars-v0.md)**
  in Asterisms System — which is just the spine-and-spokes pattern applied twice
  more, not new invention. Its presence does not approve implementation.

---

*Provisional. The test in §2 is the durable part; the component table in §3 is a
snapshot and will drift — re-ground against disk.*
