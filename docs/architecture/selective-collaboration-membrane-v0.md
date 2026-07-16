---
title: Selective Collaboration Membrane v0
status: DRAFT - architecture note
date: 2026-07-08
companions: orientation-surfaces.md, interagency-orientation-surface-v0.md, web-conversational-orientation-surface-v0.md, ../core/boba-core-mission-and-commitments.md, ../core/boba-braid.md, ../core/continuity-and-decision-lineage.md, ../core/social-protocol-of-angelic-outreach-v0.md, ../manuscript/book-as-collaborative-surface-score.md, ../core/ephemeris-charter.md, collaboration-stack-sketch-v0.md
provenance: Keith + Codex dialogue, 260708
---

# Selective Collaboration Membrane

This is the missing middle layer between the public invitation and the actual
working system.

The project does not need a louder manifesto. It needs a legible membrane:
something that decides what gets in, what gets routed, what gets summarized,
what gets preserved, and what stays local.

## 1. Working proposition

The collaboration surface should be selectively permeable, not maximally open
and not need-to-know in the absolute sense.

The default question is not "may this be seen?" The default question is:

- is it important?
- is it materially useful?
- does it change the state of the work?
- is it timely?
- does it benefit the recipient?
- does it preserve continuity?
- is the expected value worth the human bandwidth cost?

That is not a formula. It is a routing discipline.

The membrane is the place where a contribution becomes one of several things:

- a direct response
- a routed note to a smaller set of participants
- a floor entry that stays public to the braid
- a question that should remain open
- a durable formation
- a local-only artifact that never gets broadcast

## 2. Why "manifesto" is the wrong primary word

You do not need to be allergic to manifestos in the abstract.
You probably should be allergic to the social posture the word often drags in.

Problems with the term:

- it implies totality when the work is provisional
- it suggests declaration when the project is actually invitational
- it can sound like someone pretending to have already closed the argument
- it tends to flatten distinctions between doctrine, protocol, and style

So no, this is not evidence that I think badly of you.
It is more like this: the corpus already knows it is unfinished, reflexive, and
local-first. "Manifesto" is a noisy label for that posture.

Better words already in the corpus:

- charter
- score
- protocol
- invitation
- orientation surface
- working note
- architecture note

## 3. What the membrane actually does

The membrane routes by relevance, continuity, and impact.

That means a contribution does not have to be private to matter, and it does
not have to be universal to be useful.

Routing can consider:

- who is implicated
- who can actually benefit
- who needs to know to avoid drift
- whether a human should be spared the full stream
- whether the contribution is a claim, a correction, a question, or a prompt
- whether the contribution deserves a durable record

This is why "need-to-know" feels too absolute. The better frame is closer to
"benefit-to-know" under a constrained attention budget.

## 4. Federated boba

One avenue of participation is for someone to spin up their own `boba`.

That local instance would have the same basic posture:

- a mission and commitments
- a braid or braid-like collaboration grammar
- a selective collaboration membrane
- an orientation surface
- a durable substrate for receipts

Federation does not mean centralizing all contributions in one place.
It means local instances can participate across boundaries with a shared
minimum protocol.

Possible federation primitives:

- identity continuity across sessions or instances
- declared participation role
- provenance for contributions
- a routing hint for where a contribution should go next
- a compact summary or receipt rather than the full raw stream
- explicit opt-in for any cross-instance forwarding

The local instance should be able to say:

- this stays here
- this can be forwarded
- this should be summarized first
- this should be promoted
- this should be ignored

## 5. Ephemeris is the time layer, not the membrane

The membrane can feel Ephemeris-adjacent because it routes, escalates, and
loops contributions back into the work. But the layers are still distinct:

- **Ephemeris** tracks position, trajectory, and active score.
- **The membrane** decides how a contribution crosses boundaries, or whether it
  crosses at all.

That distinction matters operationally.

If something is about *where things are headed*, *what score is active*, or
*what coordination should happen next*, that is Ephemeris language.

If something is about *who should see this*, *what fidelity should travel*,
*what should remain local*, or *what should be summarized before forwarding*,
that is membrane language.

The membrane may feed the Ephemeris. The Ephemeris may trigger membrane
decisions. But they are not interchangeable.

## 6. Repo and doc structure

The current workspace already has the right bones. The missing layer is mostly
organization, not invention.

### Core

Foundational commitments that should stay stable:

- `docs/core/boba-core-mission-and-commitments.md`
- `docs/core/boba-braid.md`
- `docs/core/continuity-and-decision-lineage.md`
- `docs/core/ephemeris-charter.md`
- `docs/core/social-protocol-of-angelic-outreach-v0.md`
- `docs/core/` should eventually hold the social protocol of angelic outreach
  as a real charter, not only a glossary phrase

### Architecture

Design candidates and mechanism notes:

- `docs/architecture/orientation-surfaces.md`
- `docs/architecture/interagency-orientation-surface-v0.md`
- `docs/architecture/web-conversational-orientation-surface-v0.md`
- this membrane note
- `docs/architecture/collaboration-stack-sketch-v0.md`
- `docs/architecture/boba-metamemory-and-lora-adaptation.md`
- `docs/architecture/braided-discourse-design-spec.md`

### Manuscript

Public-facing invitation and language-layer work:

- `docs/manuscript/book-as-collaborative-surface-score.md`
- the book should be the invitation, not the entire system dump

### Session records

Dated work logs and decision receipts:

- `docs/session-records/`
- use these for "what happened, what changed, what is still open"

### Tooling

Verified mechanics only:

- retrieval
- corpus index
- local queue
- any server or wake script that has been checked on disk

## 7. Comparison to what already exists

What is already good:

- The core mission doc already names open frames, local custody, and no
  coercive steering.
- The braid doc already has the right mechanics for contribution vectors,
  surfaces, trust, and shared reference.
- The continuity doc already has the key fact: reflexivity requires
  immutability.
- The Salon charter already has a working model for selective participation,
  rate limits, receipts, and promotion.
- The book score already says the book is an invitation, not a monument.

What is still unfinished:

- the public-facing collaborative surface is still more implied than wired
- the routing logic is described, but not yet embodied in a shared protocol
- federation is named, but not yet documented as a concrete participation path
- the social protocol exists as a phrase and a drift of related documents, not
  as a single load-bearing charter
- the web surface still needs honest status, real scope handling, and a better
  bridge from reading to contribution
- a LoRA or trained model is a later consolidation step, not the substrate

## 8. Costs and rewards

### Costs

- More protocol means more design work up front.
- Federation means more edge cases about identity, provenance, and forwarding.
- Selective routing means someone has to make judgment calls instead of
  pretending everything is equally relevant.
- Human bandwidth protection can feel slow compared with a fully open feed.
- The more durable the surface, the more important the record hygiene becomes.

### Rewards

- Less overload for humans.
- Less accidental broadcast of low-value material.
- Better continuity across sessions and across local `boba` instances.
- A clearer public invitation that does not require total comprehension.
- A collaboration model that can survive more than one participant, more than
  one machine, and more than one local installation.
- A path from corpus, to protocol, to federation, to model without confusing
  any of those layers.

## 9. Recommended path forward

1. Stabilize the public invitation language in the manuscript and web surface.
2. Write a real social protocol charter under `docs/core/` or `salon/`.
3. Define federation primitives for a local `boba` instance.
4. Make routing explicit in the Salon and web composer.
5. Use session records to track unresolved routing and trust questions.
6. Only then consider a LoRA or trained model as a consolidation layer.

## 10. Practical interpretation

If you want a short phrase for the whole thing, this is the best one I have
right now:

**Selective collaboration membrane**

It is less grand than manifesto, more honest than platform, and close enough
to the actual mechanism to be useful.
