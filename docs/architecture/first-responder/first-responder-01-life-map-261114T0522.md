---
title: "Life map: the shared record"
status: DRAFT, architecture candidate (not yet committed)
date: 2026-11-14
set: first-responder-00-overview, -01-life-map, -02-front-door, -03-whereabouts, -04-roadmap
folds-in: Whereabouts working spec (Records, Claim kinds, Source and trust, Time axis); Whereabouts addendum, the life map (whole); central-record notes (261108)
---

# Life map: the shared record

## In plain terms

One record of Keith's life that every lane reads from and writes to. It has three layers. **Captures** are the raw recordings, kept forever. **Claims** are what Keith or the angels say about the captures and about the world: this is the welder, the ride was twenty minutes, the drill went into the red drawer, the book is an active goal. **Views** are computed from the claims: where the welder is now, what today looked like, which goals have gone quiet. A view can always be recomputed, so nothing is ever edited in a view. A correction is a new claim.

The record spans past, present and future. The past is what was captured. The present is where Keith and his things are and what he is doing. The future is what he has committed to: goals, plans, calendar, pending moves.

## Three layers

**Captures (ground truth).** Audio, photo, clip, scan, device report, typed line. Each is saved with the metadata that cannot be recovered later: timestamp, device and camera settings, and for a worn camera the head orientation from a motion sensor (an IMU, inertial measurement unit), a room-level position hint from Wi-Fi or Bluetooth signal strength, and a sharpness score. Blurry frames are kept and marked. Bytes live in a blob store; provenance (hash, time, source, governance) is registered on Asterisms through Porter.

**Claims (readings and statements).** Each claim records subject, relation, object, time, source (a capture or a statement), maker (Keith, or a named model and version), status and kind. Claims never change. A later claim can supersede an earlier one and says so.

**Views (computed).** Current location of each thing, the daily log, active goals and when each was last raised, coverage by place and by time, exercise history. Disposable and recomputable.

## Records

Five record types. People and events are labels on these, not new structures.

- **Capture**: any raw recording with its metadata. (The spec called this Frame; generalized here to every kind of capture.)
- **Place**: any scale, nested by containment: shop, southwest corner, bench, red drawer. A car is a place that moves; a toolbox in the car is a place inside a moving place. Coordinates are optional.
- **Thing**: an object, a person, a pet, a document. Optional "lives at" home place.
- **Claim**: the workhorse, as above.
- **Episode**: something that happened over a span of time (a ride, a welding session, a meeting), linking places, things and captures. Calendar entries, journal moments and exercise sessions are all episodes.

## Claim kinds

| Kind | Meaning | Usual status | From |
|---|---|---|---|
| Seen | a model spotted it in a capture | inferred | spec |
| Labeled | Keith named it in a capture | confirmed | spec |
| Told | Keith said it with no capture ("my toothbrush is in the bathroom") | confirmed as of when said | spec |
| Moved | a pickup or a putdown, the unit of the move record | confirmed if told or plainly captured; otherwise inferred | 261114 |
| Absent | looked for at a place and not there, with how well the spot was covered | confirmed if Keith looked; inferred from a capture | 261114 |
| Lives at | a standing home place | confirmed | spec |
| Destined for | a pending move ("this goes to the garage loft") | confirmed | spec |
| Measured | a number from an activity (time, distance, weight) | inferred until checked | 261114 |
| Goal | a live commitment (below) | confirmed | addendum |

Status words come from `how-we-work-here.md` §5: **confirmed** (Keith said or confirmed it, or inspected output shows it), **inferred** (a model's reading), **suspected** (a soft hunch, such as credit from observation) and **disproven**. A superseded claim keeps its status and gains a pointer to what replaced it.

"Lives at" and "Seen" stay separate on purpose, so a toothbrush seen on the shop bench shows up as out of place rather than one claim overwriting the other.

## The move record (happy path)

Premise (decided 261114): Keith is the actor, and he records what he does through the angels. There are no ghosts by design. So a thing's location is not an estimate that decays. It is wherever the last recorded move put it.

- The unit is the **pickup and the putdown**. Each is a Moved claim, from Keith's word, from a capture sequence (his hands on the welder in one frame, the welder on the porch in the next), or inferred.
- Photos **audit** the move record. They do not reconstruct it. When a sighting disagrees with where the record says a thing is, that is a **gap**.
- A gap gets repaired, not explained away: the record gains "moved sometime between A and B" and, once known, by whom. A neighbor borrowing the welder is simply an unrecorded move by another actor. In the happy path these are rare, and the record names them when learned.
- The background pass is the auditor. It is what notices "the record says porch, the frame says shop."

## Resolution

Location (and time, and measure) is held at whatever resolution its source supports: "in the shop" from a doorway glance, "southwest corner" from a wide frame, "ten inches from each wall of the southwest corner" from a focused shot or a measurement.

- A query is answered at the **coarsest resolution that does the job**. The welder is big, so "in the shop" ends the search. A drill bit needs the drawer. (decided 261114)
- How fine is "enough" can be learned per thing from searches: if "in the shop" reliably ends welder searches, room level is enough for the welder. (proposed)
- **Resolution and age pull against each other.** The newest claim may be coarse and an older one precise. Answer with both: "in the shop as of this morning; last pinned to the southwest corner in March." (proposed 261114)
- When finer resolution is needed and missing, say so plainly ("seen at room level only") rather than implying more.

## Time: past, present, future

Claims have times, episodes have spans, and future-tense claims (goals, planned episodes, Destined-for moves) use the same record types. That gives "what was in the loft in March," "when did I last service the lift," and a forward timeline in one structure.

- Google Calendar stays the source of truth for scheduled events. The life map reads it rather than copying it. (decided 261108)
- The calendar records what was planned, not what Keith has decided this afternoon. A mismatch between plan and present is a question to ask, never a correction to apply.

## Goals as live claims

Carried over from the addendum. A goal stays alive until Keith questions, changes or retires it. Nothing ages it out. If it goes quiet, the angels raise it (see 02, Raising).

Fields beyond an ordinary claim:

- **Status**: active, paused, done or retired. Only Keith changes it.
- **Stated**: when and how, with a pointer to the source, in his own words so they can be quoted back to him when he doubts the goal.
- **Externalizations**: the events, meetings, deadlines and tasks it has been turned into. A goal with none is a wish; worth noticing, not a failure.
- **Last raised**: when it last came up, from Keith or from an angel.
- **Review rhythm**: how often it should come up if Keith doesn't raise it. It starts at a default and adjusts to his answers.
- **Parent and children**: goals nest.

Over weeks and seasons the map shows which ways of externalizing a goal (a meeting, a deadline, a buddy, a calendar block) actually move Keith and which don't. That is the learning loop the life map exists for.

## Reading depth

Every capture has a reading depth, and depth only grows:

1. **Kept**: registered, not yet read.
2. **First pass**: transcribed, routed, a few quick tags.
3. **Swept**: every lane has had a cheap look (category tags, text read off labels and displays).
4. **Deep**: objects outlined and fingerprinted, matched against known things, placed in the spatial map.
5. **Re-read**: read again by a newer model, with both readings kept under their model names.

Deepening happens when a question needs it, when a thing is flagged or tied to a live goal, when compute is idle (overnight on Alpha Angels), or when a better model arrives. A shallowly read capture is not lost, only not yet read. (proposed, following "nothing buried" and "late is fine")

## Coverage

For each place: how recently and how thoroughly it has been captured. For each stretch of time: how much was captured at all. Coverage keeps a thinly captured place from looking empty, and it is what makes an Absent claim mean anything. "Not in this photo" only counts if the photo actually covered the spot.

## Corrections

- Keith's word is final and arrives as a new claim.
- Merging two names for one thing, and splitting two things wrongly merged, must each be a single step, or the record slowly rots.
- Corrections reach views by recomputation, never by editing a view.

## Storage form

- **Now**: plain dated folders Keith controls: goals, daily notes, voice memos with transcripts beside them (decided 261108), plus a daily markdown log (261110).
- **Next**: registration through Porter onto Asterisms; bytes in a blob store; fingerprints in a vector index.
- **Volume**: voice notes are small. Worn-camera frames at about one every ten seconds while moving come to a few gigabytes a day, a few terabytes a year. That is fine on drives, and it is the reason the blob decision comes first (see 04, Gates).

## Failure modes

- **Same event, many captures.** A photo of the bike display and a voice note about the same ride must become one episode with two sources, not two rides. The same goes for a meeting mentioned three times. Merge by time window and content, and let Keith split a wrong merge.
- **A view mistaken for the record.** Editing "where the welder is" by hand would break lineage. Every edit is a claim.
- **Plan treated as present.** See Time.
- **Too many live goals.** A periodic "here is everything active; still true?" pass keeps the list honest.
- **Soft credit hardening.** Seeing Keith at the wheel suggests the pottery goal moved; it does not prove it. Credit from observation stays "suspected" unless Keith confirms.
- **Entity drift.** The same drill under three names, two clamps merged. One-step merge and split.
- **Resolution confusion.** A coarse new claim silently replacing a precise old one in an answer. Answer with both.
