---
title: "Whereabouts: the spatial lane"
status: DRAFT, architecture candidate (not yet committed)
date: 2026-11-14
set: first-responder-00-overview, -01-life-map, -02-front-door, -03-whereabouts, -04-roadmap
folds-in: Whereabouts working spec (261113T1704, whole); 261113 and 261114 sessions
---

# Whereabouts: the spatial lane

## In plain terms

Whereabouts knows where Keith's things are, in the shop, basement, house, yard and car. It learns what things are when Keith names them, finds them in photos, and keeps a record of every move. "Where's my welder?" gets an answer at whatever resolution finds it, with the photo to prove it. When the answer turns out wrong (he goes to the southwest corner and the welder isn't there), Whereabouts works with him to find where it went. When he is tired and looking straight at a thing without seeing it, a photo lets the angel look for him. Eventually, knowing where he is heading, it can say "you're passing the loft, and the box by the door goes there."

## Premise

Happy path (decided): long-term radical transparency, with Keith's own records working for him. He is the actor and records his moves through the angels. The adversarial note is one line, at the end of Failure modes.

## Identity: three levels

1. **Category** ("any welder"). An image-text model from the CLIP or SigLIP families answers this from photos, with no labeling.
2. **Model** ("Miller Multimatic 215"). Read the nameplate once and the thing links to its manual, parts and settings, and becomes findable by model number. The cheapest way to add depth.
3. **Individual** ("my Miller"). A fingerprint built from naming moments separates Keith's welder from an identical one. Several reference views per thing; every confirmed sighting adds another.

Look-alikes (ten identical clamps) need identity from context ("the one in the tray by the door"), not appearance. Things inside closed containers are never seen directly and need a "went into this box" claim, ideally spoken.

**The fingerprint model is swappable.** The DINOv2 family (image models strong at telling individual objects apart) is the expected default. JEPA (Joint Embedding Predictive Architecture) is one candidate, tested against the others on Keith's own look-alike tools. Every fingerprint records the model that made it, so it can be regenerated.

## How a spoken name reaches the right object

Keith says "this is my 20-ton brake" while looking at it. A segmenter (a model that outlines objects in a picture) cuts out the candidates, and the one at the center of view, or the one being pointed at, gets the name. Open: pointing, gaze, or only "the thing in front of me."

## Capture streams

| Stream | What | Rate | Purpose |
|---|---|---|---|
| Ambient | wide shots from a worn camera | about one every 5 to 10 seconds while walking; slower when still | sightings, coverage, the place map |
| Focus | a high-resolution burst on one thing | on a spoken "look at this"; perhaps gaze dwell later | nameplates, detail, naming, 3D detail |
| Incidental | photos taken for other reasons | whenever | background sightings (the welder behind the bike) |
| Told | spoken or typed, no photo | whenever | "the torque wrench lives in the red drawer" |
| Imported | existing photos, receipts, manuals, emails | once | depth and history |
| Angel-requested | frames on scene change, on a schedule, or by asking | learned | filling gaps in coverage |

## Location and the move record

Location is containment first (shop, southwest corner, bench, red drawer), with coordinates where known. Every claim keeps the resolution its source supports, and answers come at the coarsest resolution that finds the thing. The welder is big, so "in the shop" is a complete answer. The welder pinned ten inches from each wall in March and seen "in the shop" this morning is answered with both.

Under the premise, location is a record of moves rather than a running estimate. Pickups and putdowns are the unit, photos audit them, and the background pass reconciles the two. The detail is in 01, The move record, and 01, Resolution.

## Find

"Where's my welder?"

1. Read the move record: the last putdown and the latest sighting.
2. Answer at the resolution that suffices, with the supporting photo and the welder outlined in it.
3. If the record is thin or stale, search captures newest first, favoring recall over precision. Show a handful of candidates, each checkable at a glance.
4. A confirmed hit becomes another reference view.

## When the thing isn't there: misses as evidence

Keith goes to the southwest corner and the welder is gone. Perhaps a neighbor borrowed it, perhaps it was left where it was last used, perhaps a move went unrecorded.

1. **The miss is a claim.** "Not here, as of now" is an Absent claim. A photo of the empty spot is the best evidence, and it fixes the coverage.
2. **Walk the record back.** The last recorded putdown, the last sighting, the last episode that used it (welding on the porch on Tuesday).
3. **Rank the candidates.** Places of last use first, then places on the path between, then places where things like it tend to be left, and another actor only when nothing else fits.
4. **Search the captures since the last confirmed sighting** at a lower threshold, including the backgrounds of unrelated photos.
5. **Offer the next check** with the frame that suggests it: "Tuesday's porch photo shows something like it by the steps."
6. **Each check is new evidence.** Another Absent claim eliminates a place. A find closes the gap with "moved sometime between March 3 and today" and, once known, who moved it.

A failed search is also the moment to offer to take a frame, since that is exactly when the record most needs a correction.

Open (Keith left this uncertain, 261114): does a failed search start the reconstruction automatically, or only when asked? A related direction: an angel may one day notice, in an unrelated photo, that the welder is missing from where it was thought to be, judge that it doesn't matter right now, and stay quiet, since its next appearance anywhere will update the record anyway.

## A second pair of eyes

Tired, and unsure whether the unit is still in its box or was taken out, Keith may be looking straight at it without seeing it. A photo of what he is looking at lets the angel search the frame with no expectation to fight.

- **Answer with the state, not just yes or no**: "the box is closed and the unit isn't visible anywhere in the frame"; "it's on the left shelf, behind the grey case"; "the box is open and empty."
- **Use the record.** If a "went into this box" claim exists, say so; the camera cannot see through cardboard.
- **Ask for a second angle** when the frame is too narrow or too dark.

## Out of place

For things with a "lives at" home, notice when a sighting disagrees. Eager, but only for a short flagged list.

## Carry-along

Keith is going from A to C and will pass B, and something at A belongs at B. This needs three things: a Destined-for claim (from Keith, or a suggestion he accepts), a guess at where he is heading (calendar, current activity, or his word), and live localization (Stage 3 below). It starts with explicit, flagged items only, because wrong guesses turn into noise fast. This is the "route-optimized physical movement" half of the July material-world interface note.

## Backward naming

When Keith names something today, search older captures for it. This works because captures are permanent and fingerprints can be re-run.

## Spatial stages

"World model" here means an increasingly detailed, inspectable view of Keith's spaces, not a neural network that predicts what happens next. Each stage is useful on its own.

- **Stage 0, view graph.** Captures are nodes, things link to the captures they appear in, and captures link where they overlap.
- **Stage 1, pose-tagged views.** Motion-sensor and signal-strength hints give each frame a rough position and direction.
- **Stage 2, reconstructed 3D.** Many overlapping photos go through photo-to-3D reconstruction, after the fact, one space at a time, starting with the shop. Things found in frames get 3D positions.
- **Stage 3, live localization.** The worn camera matches its current view to the 3D model to know where Keith is. Carry-along needs this.

Stages 2 and 3 wait until 0 and 1 work and the test questions are settled. Deliberate, slow "sweep" passes through a space will do more for reconstruction than any choice of model. SLAM (simultaneous localization and mapping) is the heavier alternative to this staged path.

## Test questions (to confirm or replace)

1. Where is my welder right now? (I didn't point it out when I walked past it.)
2. When did I last service the lift?
3. What's in the garage loft?
4. What's at the shop bench that belongs in the house?
5. Show me every photo with the 20-ton brake in it.
6. Which of my active goals has had nothing scheduled in the last month? (life map)
7. The welder isn't in the southwest corner. Where else could it be? (261114)
8. Is the unit in this box? (261114)

The shop alone exercises nearly every mechanism.

## Failure modes

- **Odd-angle matches are weak.** Named in shop light and seen on the porch from a head camera, the welder will match poorly. Return several candidates and keep several reference views.
- **Absence without coverage** is not evidence.
- **Resolution versus age** (see 01).
- **Gaps in the move record** are expected; the audit exists for them.
- **Look-alikes and closed containers** need context and spoken claims.
- **Carry-along needs a route guess.** Start with explicit items.
- **Uneven coverage.** The shop photographed to death, the car barely. Show coverage.
- **A rich graph that nobody queries.** Build to the test questions.
- **Entity drift.** One-step merge and split.
- **3D from a bouncing head camera** is hard. Sharpness filtering and sweep passes help most.
- **Adversarial note.** This archive would be a very complete record of the household, so local custody and access rules should be settled before it grows large.

## Open questions

- Is the worn camera always on, or started when Keith begins working a space?
- Which camera first: the phone on a chest mount, or a dedicated head or body camera?
- How does a spoken name attach to the right object: pointing, gaze, or "the thing in front of me"?
- Does a failed search start reconstruction automatically, or only on request?
- Which test questions are the real ones?
