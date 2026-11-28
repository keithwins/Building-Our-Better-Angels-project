---
title: "First Responder: roadmap"
status: DRAFT, working map (expect frequent revision)
date: 2026-11-14
set: first-responder-00-overview, -01-life-map, -02-front-door, -03-whereabouts, -04-roadmap
folds-in: First Responder v0.1 Plan (first slice, round two, open questions); Whereabouts spec (build order, open questions); 261110 build session
---

# First Responder: roadmap

## In plain terms

Where things stand as of 261114, the three gates that existing BOBA doctrine puts in the path, and the next steps in small and larger sizes. Status words follow `how-we-work-here.md` §5, and status here means "as last known." Re-check the machines before acting on it.

## Where things stand

| Item | Status | As of |
|---|---|---|
| Tailscale on the phone and on Ambient Angel (shown as "ambient-angel"; the OS hostname is still "pianissimo") | confirmed | 261109 |
| Syncthing-Fork on the phone (from the Play Store, since Advanced Protection blocks sideloading F-Droid) | confirmed | 261110 |
| Recorder's Recordings folder shared send-only, with ignore patterns for the auto-generated subfolder and "Recordings archive*" at any depth; zero files showing | confirmed | 261110 |
| Syncthing on Ambient Angel, paired with the phone | not done at 261110; unverified since | 261110 |
| faster-whisper on Ambient Angel, and a speed test on a sample memo | not done | 261110 |
| Watcher script, daily log, four-hour timer, ntfy | not built | 261110 |
| Taildrop test into ~/voice-memos_261109 | unverified | 261109 |
| Porter (Asterisms intake) on Alpha Angels under WSL (Windows Subsystem for Linux); scanner intake folder on the Windows side | exists | 261102 |
| Blob and vector sidecar spec | specification only; its gate not yet revisited | 260712 |
| Resonator | pre-build; prerequisites not met | 260705 |
| Whereabouts | spec only; no worn camera chosen | 261113 |

## Gates from existing doctrine

1. **Before worn-camera capture at volume**: revisit the blob and vector sidecar gate and decide where bytes live. The integration map says "decide before volume." Phone photos at today's rate can wait in plain folders; worn-camera frames cannot.
2. **Before the daily stream is registered on Asterisms**: encryption at rest for it. Any check-in can carry Resonator-class material, and the ledger cannot take a plaintext entry back ("encrypt first, then confide"). Until then the stream stays in plain folders Keith controls.
3. **Before the emotional-support lane answers anything**: the Resonator's crisis path.

## Small steps

Each is an evening or less, and each can be undone.

1. Install Syncthing on Ambient Angel, pair it with the phone, and accept the Recordings folder into a dated landing folder. Confirm with a ten-second test recording.
2. Install faster-whisper with the small model. Time a one-minute and a five-minute memo.
3. Watcher: each new audio file gets a transcript beside it and a timestamped entry in the day's markdown log.
4. Four-hour timer and ntfy nudge, run on Ambient Angel over Tailscale, with snooze and quiet hours.
5. Two weeks of capture and nudges only. Count nudges answered, snoozed and ignored, and adjust the rhythm from that.
6. Share the camera folder too, send-only. Decide whether the photo backlog comes along or only new photos.
7. The first lane beyond the journal: exercise. A display photo or a voice note becomes one entry with time and distance. Confirm the first few readings by hand to seed the display template.
8. Name ten things in focus photos (the welder, the 20-ton brake and so on) to seed Whereabouts.

## Medium steps

- Decide where Porter registration happens for the daily stream (question 2 below), then register it, after gate 2.
- Make transcription one shared capability for the voice workbench, Understory and the First Responder.
- An overnight pass on Alpha Angels, woken by Ambient Angel: category tags on every photo, written as Seen claims.
- Find, version 0: "where's my X" over the photo archive, newest first, candidates outlined.
- Goals folder and raising, version 0: quiet goals raised in the answer to a check-in.
- Read Google Calendar. A plain "today" file with tasks pulled from voice notes.
- Absent claims, and reconstruction on request.
- Plausibility checks, and merging of duplicate episodes.
- Optionally, Obsidian as a viewer over the same markdown folders, with no proprietary format underneath (from v0.1 round two).

## Larger stages

- A worn camera: ambient frames, the "look at this" trigger, angel-requested frames.
- The move record, with pickups and putdowns detected from captures.
- 3D reconstruction of the shop from the archive; then live localization and carry-along.
- The learned skill of when to look, ask and speak, trained from outcomes.
- The Resonator lane, after its gates.
- A tiny first-pass model on the phone.
- Elder Angels inherits the loop, starting with the exercise lane for ElderCycle.

## Open questions

1. Which name stands for the whole: First Responder, life map, Small Council, or something else? (00, Naming)
2. Where does Porter run for the daily stream: on Ambient Angel, which is always on and where captures land, or on Alpha Angels, where it lives now and which is often asleep?
3. Does a failed search start reconstruction automatically, or only when asked? (left open by Keith, 261114)
4. Pre-alert timing: beeps an hour and half an hour before the mark, or one soft buzz at three hours?
5. What a nudge says, and how it avoids becoming noise.
6. Quiet hours: fixed, learned, or tied to what Home Assistant knows (asleep, driving)?
7. The worn camera: which one, and always on or per space?
8. How a spoken name attaches to the right object.
9. Which test questions are the real ones?
10. How the "today" file relates to the Porter drop folder.
11. Does the existing photo backlog come in?
12. Early spoken cues for triage: allowed as a shortcut, or none from the start?
