---
title: "First Responder and the Life Map: overview"
status: DRAFT, architecture candidate (not yet committed)
date: 2026-11-14
set: first-responder-00-overview, -01-life-map, -02-front-door, -03-whereabouts, -04-roadmap
folds-in: First Responder v0.1 Plan (261110); Whereabouts working spec (261113T1704); Whereabouts addendum, the life map (261113); Small Council notes (261108); central-record notes (261108)
provenance: Keith + Claude dialogue, 261108 to 261114
proposed-home: docs/architecture/first-responder/
---

# First Responder and the Life Map

## In plain terms

Through the day, Keith leaves a trail of small captures: a voice note, a photo of the exercise bike's display, a picture of a shelf, a scanned letter, and later the frames of a worn camera. One front door, the **First Responder**, receives every capture, keeps it permanently, takes a quick first look, and passes it to whatever it concerns. Nothing has to be labeled. A photo of the bike display is read as exercise. Later, a slower pass notices the welder in the background and notes where it was, the way a person notices things in passing without noticing that they noticed.

Everything the angels learn goes into one shared record, the **life map**: the past as captured, the present (where Keith and his things are, what he is doing) and the future (goals, plans, calendar, pending moves). Specialized lanes read and write that record: the watchdog, the journal, emotional support, Whereabouts for physical things, exercise and health, goals, documents.

A rhythm keeps the record alive. Any capture counts as a check-in, and four hours of silence brings a gentle nudge. Over time the angels learn the one skill under all of it: when to look, when to ask, and when to speak up, at the lowest cost to Keith.

## Why this is a central step for Better Angels

This is the first design in which the continuity loop of Building Our Better Angels (BOBA) runs on Keith's actual day with real senses. The adopted doctrine (`continuity-and-decision-lineage.md` §4) names the loop: observe the current state, compare it against commitments, surface the smallest useful next step, check its fit, record what was decided, and preserve it. The First Responder is that loop's daily runner.

It also brings four layers of the June roadmap (`boba-roadmap.md`) into one place: the conversational companion (§4), scheduling (§5), audio (§6) and perception (§7), which the roadmap called "furthest out" and deliberately left undesigned. Each was scaffolded on its own. Here they meet in one loop, with Keith as patient zero. What works here is what Elder Angels inherits, in the same way the Resonator charter builds a confidential-care substrate for both.

## The shape

```
capture            voice note, photo, short clip, scan, typed line, device report;
                   later worn-camera frames and angel-requested captures
   |
landing            Ambient Angel (always on), so nothing is dropped while other machines sleep
   |
Porter             intake stoma: hash, dedupe, register provenance on Asterisms;
                   bytes go to a blob store
   |
First Responder    first pass: transcribe, quick read, route, act only if
                   something concrete needs doing
   |
lanes              each lane reads the capture and writes claims to the life map
   |
background passes  later and deeper: every lane gets a look at every capture;
                   re-run when better models arrive
   |
Ephemeris          rhythm, raising, nudges, carry-along timing; out to the phone
```

## The parts

| Part | What it is | BOBA role | Detail |
|---|---|---|---|
| Capture tools | Pixel Recorder and camera now; scanner; worn camera later; device reports where available | edge tools that emit bundles | 02 |
| Ambient Angel | the always-on laptop (Home Assistant, Syncthing, transcription, timer, notifications) | landing and first-pass host | 02, 04 |
| Porter | the existing intake | Asterisms intake stoma | 01 |
| First Responder | the front door: first pass, routing, rhythm, nudges | an angel paired with the intake stoma | 02 |
| Life map | the shared record: captures, claims, views | Asterisms provenance plus views computed from it | 01 |
| Lanes | watchdog, journal and biography, emotional support, Whereabouts, exercise and health, goals, documents, tasks | angels or spokes on the provenance spine | 02, 03 |
| Rhythm and raising | four-hour window, nudges, goals brought up | Ephemeris (coordination by shared reference) | 02 |
| Compute tiers | phone, Ambient Angel, Alpha Angels on wake, frontier models when needed | runners | 02 |

## Principles

Marked **decided** (Keith has said so), **proposed** (Claude's suggestion, not yet accepted) or **doctrine** (already adopted in the corpus).

1. **Patient zero.** It has to work on Keith first, inside his actual day, and be demonstrably helpful. (decided)
2. **Captures are permanent ground truth.** Every capture is kept, with the metadata that cannot be recovered later. Everything else (transcripts, captions, fingerprints, 3D models) is a reading that can be regenerated, ideally by better models later. (decided; doctrine under No Forgetting)
3. **Nothing is buried.** Storage is not the constraint; attention and compute are. The angels hold everything. What varies is how deeply each capture has been read so far. (decided 261114)
4. **Claims, not facts.** Each reading says what, when, from which capture or statement, and how sure, using the corpus's uncertainty grades. Keith's word is final. (decided; grades are doctrine)
5. **Corrections are new layers.** A change of mind or a corrected reading supersedes and never overwrites. Current views are computed from the layers. (doctrine)
6. **No declaring.** In the long run nothing needs a label: the content of a capture says what it concerns. A spoken cue may help early on but is never required. (long run decided; early cue proposed)
7. **Every capture is read by every lane**, quickly by the obvious lane and later, more slowly, by the rest. (proposed and agreed 261114)
8. **Late is fine.** The first pass is quick and shallow; deep reading happens when compute is free. (decided 261114)
9. **Happy path: Keith is the actor and records what he does.** The record of where things are is complete by intent. Photos audit it rather than reconstruct it. Gaps are expected and repaired. (decided 261114)
10. **Resolution matches the need.** A location, time or measure is held at whatever resolution its source supports and answered at the coarsest resolution that does the job. (decided 261114)
11. **Strict bar for interruptions.** Only what Keith would thank it for. Raising waits for natural openings, and "not now" costs one word. (bar decided 261110; openings proposed)
12. **Ask and offer, don't conclude.** As the biography deepens, the angels keep asking and offering rather than telling Keith who he is. (decided)
13. **Own the record.** Plain files and local storage that Keith controls; devices and models are swappable. (decided)
14. **Show coverage.** A thinly captured place or day must not look like an empty one. (proposed 261113)

## How it fits the corpus

| Corpus idea | How this design uses it |
|---|---|
| Asterisms, the provenance spine | Every capture is registered. Readings are derivative materials with lineage (the `transcribe` and `embed` transforms already exist). "Where is the welder now" and "which goals are active" are views computed over the immutable record. |
| Porter, the intake stoma | The single mouth. Health records (261031) already put recognition and extraction in "the triage layer next to Porter, not Porter's core," and document intake (261102) already feeds Porter from the scanner. The First Responder is that triage layer, generalized to the whole day. |
| Blob and vector sidecars | Photo and audio bytes belong in a content-addressed blob store, fingerprints in a vector index, provenance on the ledger. Worn-camera capture at a few gigabytes a day crosses the "pre-media-volume gate," so that gate is revisited before ambient capture starts. |
| Ephemeris, the time layer | Rhythm, raising, nudges and carry-along timing are coordination: where Keith is and is headed. |
| No Forgetting | Matches Keith's "nothing is buried." Confidentiality is a separate matter from forgetting. |
| Uncertainty grades (`how-we-work-here.md` §5) | Claim status: confirmed, inferred, suspected, disproven, with links to whatever supersedes a claim. |
| Continuity loop (lineage §2, §4) | The First Responder runs it daily. "The job is continuity, not nagging" is the same strict bar. |
| The Resonator | The emotional-support lane. Its charter carries over: local-first processing, a crisis path, "encrypt first, then confide." |
| The Biographer angel | The journal and biography lane. |
| Health records | Exercise and sleep land in its stream layer, beside its document layer. |
| Elder Angels | Inherits the loop. The exercise lane is the same machinery ElderCycle needs, including reading a bike's display when its Bluetooth is not available. |
| Material-world interface (July) | Its "route-optimized physical movement" is Whereabouts' carry-along. |

A naming note: the charter calls Asterisms "space" in the sense of what patterns together, and the Ephemeris "time." Whereabouts deals with physical space. They fit without collision: moves and sightings are records on Asterisms, the current-location view is computed from them, and where Keith is heading is Ephemeris territory.

## Naming

- **First Responder**: the front door, first pass and rhythm. The name says exactly that.
- **Life map**: the shared record of past, present and future.
- **Whereabouts**: the spatial lane. Too narrow as the frame (Keith, 261114), right as a lane.
- **Small Council**: the 261108 working name for the whole ensemble (journal, scheduler, coach, health records).

Open: which name stands for the whole. Claude's view: stretching "First Responder" over everything repeats the Whereabouts problem in reverse, since the front door would then need a new name. "Life map" or "Small Council" could carry the whole while First Responder keeps its literal job. This set uses both names in its title until that is settled.

## The documents in this set

- **01 Life map**: the shared record (captures, claims, views, resolution, the move record, goals, reading depth, coverage).
- **02 First Responder**: the front door (capture, triage, lanes, background noticing, rhythm, raising, learning when to speak, compute tiers).
- **03 Whereabouts**: the spatial lane (identity, location, finding, misses as evidence, a second pair of eyes, carry-along, 3D stages).
- **04 Roadmap**: where things stand, gates, small next steps, larger stages, open questions.

## What this set changes from the earlier documents

- First Responder becomes the front door for all captures, not a voice-only watchdog with three lanes. Lanes are an open set. (261114)
- Whereabouts moves from frame to lane. (261114)
- The Whereabouts spec's "lazy by default, nothing tracked continuously" becomes: keep everything, record every move by intent, and be lazy only about compute (reading depth). (261114)
- Told locations no longer carry a shelf life. A location stands until a later move or sighting supersedes it; its age is shown, not used to discount it. (follows from the 261114 premise)
- The addendum's goals, review rhythm and raising carry over unchanged.
- First Responder v0.1 named Alpha Angels as the landing machine. The same session corrected that to Ambient Angel, which is always on. Short memos are transcribed there; long walk recordings go to Alpha Angels on wake.
- "First responder" first named the tiny first-pass model (261108). It now names the front door as a whole, with the tiny model as its first tier.

## Lineage

| Date | Source | Contribution |
|---|---|---|
| by 2026-07 | material-world interface note | cognition from images, decoupled from route-optimized physical movement |
| 261031 | health-records sessions | photos through Porter as hashed originals; recognition in the triage layer next to Porter; documents and continuous streams as separate layers |
| 261102 | document intake | scanner into Porter; pile splitting as an early Porter step |
| 261108 | Small Council (book chat) | four-hour check; gentle pre-alerts; snooze; tiers from phone to Alpha Angels; micro-journaling in place of a painful end-of-day summary |
| 261108 | central-record chat | one record everything reads; plain dated folders (goals, daily notes, voice memos with transcripts); Google Calendar stays the source of truth |
| 261110 | First Responder v0.1 plan | principles, three lanes, first slice; phone side of Syncthing done |
| 261113 | Whereabouts spec and life-map addendum | records and claims, identity levels, spatial stages, goals as live claims, raising; angel-driven capture; learning when to look, ask and speak |
| 261114 | this session | front door for all captures; triage by content; every lane reads every capture; background noticing; late is fine; nothing buried; variable resolution; the move record; misses as evidence; a second pair of eyes |

## Glossary for cold readers

- **Angel**: an agent in a chartered, accountable, continuous relationship of care.
- **Stoma**: a regulated passage in the membrane. It applies its charter and escalates when the charter does not decide. Porter is the current intake stoma.
- **Asterisms**: the append-only record of memory and lineage.
- **Ephemeris**: the coordination layer, tracking where angels, work and Keith are and are headed.
- **View**: something computed over the record (current location, active goals), never edited directly.
- **Lane**: one concern that reads captures and writes claims (exercise, Whereabouts, journal and so on).
- **Ambient Angel**: the always-on laptop, formerly called Pianissimo. **Alpha Angels**: the GPU desktop, woken on demand.

## Corpus references

`docs/core/continuity-and-decision-lineage.md`, `docs/core/no-forgetting.md`, `docs/core/ephemeris-charter.md`, `docs/core/glossary-and-ontology.md`, `docs/core/resonator-charter.md`, `docs/core/boba-roadmap.md`, `docs/method/how-we-work-here.md`, `docs/architecture/system-fit-integration-map.md`, `docs/architecture/blob-and-vector-sidecars-v0.md` (pointer to the Asterisms System copy).
