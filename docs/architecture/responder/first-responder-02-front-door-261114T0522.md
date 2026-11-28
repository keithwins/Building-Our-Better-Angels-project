---
title: "First Responder: the front door"
status: DRAFT, architecture candidate (not yet committed)
date: 2026-11-14
set: first-responder-00-overview, -01-life-map, -02-front-door, -03-whereabouts, -04-roadmap
folds-in: First Responder v0.1 Plan (261110, whole); Small Council notes (261108); Whereabouts addendum (Raising); 261113 discussion of angel-driven capture and learning; 261114 session
---

# First Responder: the front door

## In plain terms

The First Responder receives every capture Keith makes, keeps it, takes a quick first look, and hands it to whatever it concerns. It acts only when there is something concrete to do. It keeps the four-hour rhythm, so that silence brings a gentle nudge. Later, slower passes let every lane look at every capture. That is how the welder in the background of an exercise photo gets noticed without anyone asking.

## In BOBA terms

- **Porter**, the intake stoma, does the mechanical admission: hash, dedupe, register provenance, apply governance.
- **The First Responder** is the angel beside it. It reads, routes, decides whether to speak, and keeps the rhythm. This is the "triage layer next to Porter" already chosen for health records, generalized to the whole day and to scanned documents. (proposed)
- **Timing** (rhythm, raising, nudges) is coordinated through the Ephemeris, by shared reference rather than command.

## Capture

| Channel | When | Notes |
|---|---|---|
| Voice note (Pixel Recorder) | now | The audio file is the truth. Recorder's on-device transcript works offline and is a bonus. Keyboard dictation needs a connection and fails without one. |
| Photo | next | Phone camera; any photo, no tagging. |
| Short clip | later | Same rules as photos. |
| Scan or document photo | exists separately | The Brother scanner and the health-records photo station already feed Porter; they join the same triage. |
| Device report | later | Where a machine can report directly (a bike computer over Bluetooth), that replaces a photo of its display. |
| Worn camera | later | Ambient frames while moving; focus bursts on a spoken "look at this." See 03. |
| Angel-requested | later | The angel takes a frame on scene change, on a schedule, or asks Keith for one. (direction decided 261113) |
| Typed | any time | A line in a chat or a note. |

Transport now: Syncthing from the phone's Recordings folder (send-only) to a landing folder on Ambient Angel, over Tailscale so it works away from home.

## Triage by content

- **No declaring** in the long run. The capture's content says what it concerns. (decided 261114) Early on, a spoken cue ("exercise note," "look at this") may help where the first pass is unsure, but it is never required. (proposed)
- **One capture, many lanes.** The first pass routes to the obvious lane, and background passes give every other lane a look. The photo of the bike display is an exercise reading, a Whereabouts sighting of whatever is in the background, and coverage of that corner of the room. (proposed and agreed 261114)
- **Act only when concrete**: add a task, set a timer, answer a find, flag something time-sensitive. Otherwise log quietly. (decided 261110)

## Lanes

| Lane | Reads | Writes | Ties |
|---|---|---|---|
| Watchdog | check-ins, calendar, today file | notes on plan versus day; nudges | continuity loop |
| Journal and biography | everything | episodes; biographical material | Biographer angel |
| Emotional support | check-ins | reflection, held privately | Resonator charter (local-first, crisis path, encrypt first) |
| Whereabouts | photos, frames, told locations | Seen, Labeled, Moved and Absent claims | 03 |
| Exercise and health | display photos, voice notes, device reports | Measured episodes | health-records stream layer; ElderCycle |
| Goals | everything | raisings, soft credit, externalizations | 01, Goals |
| Documents | scans, document photos | document records and extracted values | health records; document intake |
| Tasks | voice notes | items in a plain "today" file the watchdog reads back | v0.1 round two |

The set is open. A new lane is a new reader of the same captures.

### The exercise lane, as the worked example

Keith finishes on the exercise bike and either photographs the display or says "bicycled for twenty minutes and went five kilometers." Either way it lands as one Measured episode: activity, duration, distance, source.

- **One photo usually beats two.** Most displays show time and distance together.
- **Displays are a known weak spot.** Seven-segment digits, glare and angle trip up general vision models. A small template per display, learned from the first few readings Keith confirms (which field sits where), makes later reads reliable. It is the same "grow templates from real documents" approach as health records.
- **Plausibility checks.** The example as first spoken, four minutes and five kilometers, works out to 75 km/h. A reading like that is a misread or a slip of the tongue, and it gets one quick question rather than a silent log entry.
- **Merge, don't double count.** A photo and a voice note about the same ride make one episode with two sources.

## Background noticing

The slow pass that does what a person does walking past the welder on the porch: notices without noticing that it noticed.

- **Late is preferred** until compute is plentiful. (decided 261114) Overnight on Alpha Angels is the natural home.
- **Noticing writes claims; it does not interrupt.** The welder in the background of the bike photo becomes a Seen claim and, in the happy path, the welder's most recent sighting.
- **Always looking.** Because every capture eventually gets every lane's look, most things need no watch list: whenever the welder shows up anywhere, that is its latest sighting. (Keith, 261114)
- **Noticing absence.** Eventually a pass can notice that a capture covered the welder's recorded spot and the welder wasn't there. That becomes an Absent claim and a gap in the move record. Whether to say anything depends on how much the welder matters right now; usually the angel stays quiet and lets the next sighting settle it. (direction from Keith 261114; not decided)
- **Absence noticing needs coverage.** The spot must be in frame, in focus and unblocked, or every half-glimpse becomes a false alarm.

## Rhythm

A first pass, understood as a first pass (Keith, 261113):

- Any capture resets a four-hour window.
- Gentle pre-alerts before the mark, mellow enough to slide past when in flow. (261108 had beeps an hour and half an hour before; 261113 had one soft buzz at three hours. Open.)
- At the mark, a nudge such as "what have you been up to?" Tapping the nudge should open straight into a voice note, with no hunting for an app. (proposed 261108)
- Snooze and sleep (decided), plus quiet hours for night and driving (proposed).
- Nudge text stays generic. Anything personal stays at home, under the Resonator's egress rules.

Why four-hourly captures instead of an evening summary: summarizing a whole day at its end proved painful and faded after a day or two (261108). Small captures while the day is fresh replace it, and restarting after a lapse has to be cheap and free of shame.

## Raising

From the addendum. An angel raises a goal when it has gone quiet past its review rhythm, or when something on the timeline touches it: a free afternoon, a related event, a sighting of something the goal needs.

Three answers, each cheap and each updating the record:

- **Still on**: resets the clock, optionally with a next step.
- **Not now**: pushes the next raising back and lengthens the rhythm a little.
- **Changed or done**: revise or retire.

Action without mention counts. Time at the wheel raises the pottery goal by itself, so the angel doesn't nag about something already happening. Raising favors natural openings over fixed intervals, and the answer to a check-in nudge is the obvious opening.

## Learning when to look, ask and speak

One learned skill sits under everything here (261113): when to take a frame, when to ask, when to speak up. Capturing on scene change, the check-in nudge, raising and carry-along are the same decision at different moments.

- **Learn from outcomes, mostly by watching.** If the next frames show Keith welding, the find worked, and he never had to report it. (Keith, 261113)
- **That credit is soft.** Seeing him weld shows he found a welder, not that the angel's answer led him there. Over many searches the blur averages out, so the angel asks outright only when a search plainly fails.
- **Silence needs a cost too.** If being waved off is the only penalty, the angel learns to go quiet. A missed appointment, or a tool it should have seen, counts against silence.

## Compute tiers and machines

| Tier | Where | Does |
|---|---|---|
| 1 | Phone (Pixel 11 Pro) | capture; on-device transcript; later a tiny first-pass model |
| 2 | Ambient Angel (always on; i7-8550U, 23 GB; Linux Mint; Home Assistant) | landing folder, Syncthing, faster-whisper "small" for short memos, the timer, ntfy notifications, first pass |
| 3 | Alpha Angels (RTX 5070 Ti, 16 GB; woken by Wake-on-LAN from Ambient Angel) | long recordings with the largest Whisper model, vision passes, deep reading, overnight work |
| 4 | Frontier models | brought in as needed, cycling toward local over time; never for Resonator material |

Journaling and simple appointments need nothing beyond tier 2. The middle band is whatever can wait for the four-hour pass. The top is live work together, with Alpha Angels woken on demand. (decided 261108)

Local transcription now happens in three places: the voice workbench, Understory and this. The integration map already asked whether transcription should be one shared capability; this is the moment to make it one. (proposed)

## Failure modes

- **Interrupting flow.** The first interruption of a good stretch of work breeds resentment, and resentment is how these systems die. Soft pre-alerts, one-tap snooze, quiet hours.
- **Learning that silence is safe.** See above.
- **Misrouting.** The bike display read as a document, a receipt read as a sighting. Every lane reading every capture limits the damage, and Keith's correction is a new claim.
- **Misread numbers.** Templates per display, plausibility checks.
- **The first pass as a bottleneck.** While Alpha Angels sleeps, deep work queues. The queue must be visible, and it must never drop a capture.
- **Two landing places.** Captures land on Ambient Angel; Porter runs on Alpha Angels under WSL (Windows Subsystem for Linux) today. Where registration happens for the daily stream is open (04, question 2).
- **Everything speaking at once.** Too many lanes or goals talking turns into noise. The strict bar applies to every lane, not just the watchdog.
