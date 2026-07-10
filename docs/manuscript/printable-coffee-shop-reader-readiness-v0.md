# Printable Coffee-Shop Reader Readiness v0

**Status:** working assessment  
**Date:** 2026-07-06  
**Role:** answer to "how close are we to a book I can print out and read in a coffee shop?"  
**Companions:** `book-as-collaborative-surface-score.md`, `invitation-surface-table-of-contents-v0.md`, `00-prologue-the-door-in-the-fog.md`

---

## Short Answer

We are not yet close to a finished book.

We are close to a **printable invitation reader**: a coherent coffee-shop packet
that Keith can print, read end to end, mark up, and use to decide whether the
book's voice and spine are alive.

That reader should not pretend to be final. Its job is to make the book real
enough to sit with.

There are two different readiness thresholds:

- **Keith-copy:** no gate beyond enough coherence to print, read, and mark.
  This can be assembled now.
- **Trusted-reader copy:** gated by doctrine and source lineage questions. This
  should not be handed out as "the book" until the gates below are resolved or
  explicitly marked local-only or omitted.

## What Is Already Strong

- **The governing posture is clear:** the book is an invitation to a
  collaboration that does not quite exist yet, not a monument.
- **The chapter grammar works:** story, pattern, BOBA response, invitation.
- **The prologue has a plausible voice:** beautiful, direct, funny where the
  pressure makes humor honest, and faithful to the ecosystem without explaining
  every pipe.
- **The source corpus is rich:** Fog, Wobbly Edge, Braid, Scores/Harnesses,
  Asterisms, VCL, Elderhood, Asterism Aflutter, Resonator, Salon, and the
  Asterisms records already provide real material.
- **The book has a reason to exist now:** it can function as the first public
  collaborative surface while the software remains incomplete.

## What Is Not Ready

- Most chapters are still **architecture or essay source**, not manuscript
  prose.
- The reader journey needs smoother transitions between metaphors: weather,
  braid, music, astronomy, botany, rope, ledger.
- The Social Protocol / Interbraid chapter is still underdeveloped.
- Chapter 10 needs the rope/countertwist mechanism integrated with Asterism
  Aflutter or moved to a different structural chapter.
- The book needs a deliberate voice policy for polyphony: when Keith, Codex,
  Claude, Opus, and records appear directly; when they are absorbed into the
  narrator; how attribution works.
- The humor needs to be harvested from actual pressure, not manufactured.

## Redline Incorporated

Claude's Salon redline sharpens the practical rule:

- The first reader is a **Keith-copy**, not a trusted-reader copy.
- `reader-v0` should be assembled mechanically enough that each printing is
  dated, reproducible, and source-aware.
- Version labels should stay simple in the repo (`reader-v0`, `reader-v1`) while
  print/build labels carry dates (`260707`) for timeline orientation. Git should
  do the fine-grained change tracking.
- Appendix G, the manuscript lineage ledger, begins with this packet. It does
  not need to be ornate; it needs to make source debts visible.

Trusted-reader release has three current gates:

- **`oq-001`: public/private seam.** The book needs a ruling on what can move
  from the Walk, Fog stream, Drive, corpus, Salon, Asterisms, and GitHub into a
  public artifact.
- ~~**`oq-009`: forgetting doctrine.**~~ **CLOSED 2026-07-10** —
  [`no-forgetting.md`](../core/no-forgetting.md). No forgetting; no crypto-shred;
  shrouding-as-forget retired. Trusted-reader may state this as settled.
- **Multitude source hazard.** The current mission/commitments material may be
  a flattened regeneration. The richer April Drive seed should be located and
  reconciled before Chapter 3 becomes trusted-reader prose.

## Recommended Printable v0

Make the first coffee-shop artifact a **reader**, not a manuscript.

Suggested title:

> *Building Our Better Angels: An Invitation Reader*

Suggested contents:

1. **Prologue: The Door In The Fog**
2. **Book Score: The Book As Collaborative Surface** short excerpt, not full note
3. **Chapter Spine:** one-page TOC with each chapter's question
4. **The Fog:** adapted prose from `the_fog_260629.md` plus AI-fog/fine-tuning note
5. **The Wobbly Edge:** adapted prose from `the-wobbly-edge.md`
6. **The Multitude:** adapted from core mission/glossary, with wounds/gifts handled carefully
7. **No Loyalty Oaths / These Are Angels You Verify:** Braid plus angel-as-genus, ledger-as-epistemology
8. **Trust Further Than You Can Throw:** limits of verification as its own chapter seed
9. **Memory That Cannot Quietly Lie:** Asterisms as living field and receipt spine
10. **A Life Can Narrow; A Life Can Open:** VCL / elderhood continuity
11. **Asterism Aflutter:** Mara sketch, mostly as-is
12. **Eclosion / Invitation:** a short closing that opens the door rather than closing the argument

This can be assembled before every chapter is fully written. It should feel like
a beautiful dossier from the future book.

## Print-Readiness Standard

A coffee-shop reader is ready when:

- it can be read linearly without needing the repo open;
- each section has a human scene, not just a concept;
- every major metaphor has a job;
- the reader can explain the project to someone else after finishing it;
- the packet invites margin notes and objections;
- it includes enough roughness to invite collaboration, but not so much that it
  reads as unfinished debris.

## How Close

For a finished book: early.

For a useful printable reader: close.

One focused drafting pass could produce a rough packet. Two to three passes
could produce something Keith can plausibly print, read in a coffee shop, mark
up, and hand to a trusted reader without apology.

## Best Next Move

Create `docs/manuscript/reader-v0/` and assemble the first printable reader from
existing material:

- copy the prologue;
- convert the TOC into a one-page chapter invitation;
- adapt the strongest existing prose into book voice;
- preserve rough source refs in footnotes or endnotes;
- leave visible "open score" questions at the end of each section.

The aim is not "publishable" yet.

The aim is **readable enough to think with**.

Recommended output:

- `docs/manuscript/reader-v0/README.md` for status, build instructions, and
  gates;
- `docs/manuscript/reader-v0/build-reader-v0.sh` as the reproducible assembly
  step;
- `docs/manuscript/reader-v0/build/building-our-better-angels-invitation-reader-v0-260707.md`
  as the dated Keith-copy.
