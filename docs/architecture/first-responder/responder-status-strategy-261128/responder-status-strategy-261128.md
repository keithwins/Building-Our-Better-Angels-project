---
title: "First Responder: status and strategy report"
status: SNAPSHOT, signed off 261128; canon candidate (three items provisional, listed in the sidecar)
date: 2026-11-28
follows: first-responder-00 to -04 (261114)
folds-in: Inkling and longitudinal-trust handoff (261127); design decisions worked through item by item, 261127 to 261128
provenance: Keith + Claude dialogue, 261127 to 261128; exported from the claude.ai working draft
---

# First Responder — Status and Strategy Report

Nov 27, 2026 · @Keith

## Summary

The Responder is well designed and lightly built. One piece is in daily use: the phone event log you've used since 261123 for the extraction recovery. The always-on loop (voice memos landing on Ambient Angel, transcription, the four-hour pulse) has waited on a single setup step since 261110.

The trust framework from the Inkling conversation doesn't need a new subsystem. The event log already has what a trust ledger needs: entries can't be quietly changed, each carries a time and a fingerprint, and corrections are new entries. Claims, commitments and decisions not to act become three more kinds of entry. The quick pass versus deep pass cross-check you already designed produces trust evidence automatically, at no cost to your attention.

The full handoff, read after this report was drafted, led to a set of design decisions, worked through one at a time on 261127 and 261128 and folded into the sections below. Claims about future you are saved but never scored. Replay is a rough screen and the live ledger gives the verdict. Angels check one another instead of asking your sign-off, except on restraint rules.

On the Inkling question: Inkling 2 Mini is real (released 261120), and a 3-bit build fits the 5070 Ti with room for context. It joins Qwen on the local candidate list; see Local model selection.

Recommended moves, in order:

1. Get the daily loop running. Claude Code on Alpha Angel can now do the Ambient Angel side over SSH; you'd only approve the pairing on the phone.
2. Have every Responder decision write a record, including the quiet ones.
3. Run one small historical replay pilot that mainly compares what context the Responder hands a model, rather than which model it hands it to.

Status here comes from notes and past chats. I couldn't attach the Better Angels repo from this session, so re-check machine status before acting on it.

## Where the Responder stands

The phone event log works; the home-machine loop is designed but not running.

| Piece | Status | As of |
| --- | --- | --- |
| Phone event log ("Dentistry extractions implants 261123") | Built and in use. Templates as data, hash chaining, corrections as new entries, Google Drive backup, dated sharing | 261123 |
| Shared-log integrity | Gap found: anyone allowed to add entries could also rewrite past ones. One stream per contributor was proposed; no record it was built | 261123 |
| Tailscale, phone and Ambient Angel | Working | 261109 |
| Syncthing, phone side | Done: send-only, ignore patterns set | 261110 |
| Syncthing, Ambient Angel side and pairing | No record it was done; calendar reminder set | 261121 |
| SSH, Alpha Angel to Ambient Angel | Working with key login, and Claude Code ran work there. Handoff folder convention not yet written | 261123 |
| Porter | Runs on Alpha Angel; move to Ambient Angel with the 5 TB drive in progress | 261124 |
| Transcription, watcher, four-hour pulse, ntfy nudges | Not built | 261121 |
| Decision records, deep pass, cross-check | Not built (steps 4 and 6 of the 261121 plan) | 261121 |
| Local models on Alpha Angel | Qwen3-8B with 64k context, plus the LFM2.5 1.2B dispatcher. Hermes installed, routing not wired | 261124 |
| 7900 XTX box | Being built: X870E board, 64 GB RAM, 2 TB PCIe 5 drive. Wakes on demand, woken by Ambient Angel | 261128 |
| Design docs | v0.1 plan (261110); front-door consolidation in the repo (261114); Grok's three instantiation docs (261117, on your phone, unread by me); alpha plan (261117); shareable summary (261121) | 261121 |
| Name | "Responder" or "First Response" under consideration | 261123 |

One pattern is worth designing around. The working piece lives entirely on the phone and needed no machine setup. The stalled piece needs you at a particular machine, and you've said you keep forgetting it when you're home. Anything Claude Code can now do over SSH removes most of that friction.

## How the trust work maps onto the Responder

Most of the handoff's mechanisms already exist in Better Angels under other names; what's missing is mostly entry types and a habit of writing them.

| Handoff idea | Already in place | Missing |
| --- | --- | --- |
| Prospective trust ledger | The event log: append-only, hash-chained, every entry timed and fingerprinted, corrections as new entries | Entry types for claims, commitments and quiet decisions, plus resolution entries that point back to them |
| Predictions as checkable promises | Disagreement as escalation: a quick pass and a deep pass read the same capture independently | Writing the quick pass's conclusion down in a form the deep pass can score |
| Evaluating restraint | "Act only when concrete, otherwise log quietly"; counting nudges answered, snoozed and ignored (261114) | A record of each quiet decision with its reason, and a one-tap "that should have been mine" |
| Epistemic humility and staleness | The corpus rule that later interpretations stand beside earlier ones rather than replacing them | An expiry date on every claim about you, so unconfirmed ones lapse visibly |
| Which intelligence gets which job | The Manifesto's confidence/reach estimate, learned from audit data, and act-and-refer routing | The audit data itself, which the ledger supplies |
| Aggregating blind judgments | Your HodgeRank exploration of truth as a field of pairwise claims | A rating template. HodgeRank takes pairwise "which helped more" taps directly, inconsistencies included |

### Three kinds of entry, scored differently

1. **Claims:** what the intelligence believes or expects, with a confidence. Scored as forecasts, against a lazy baseline that assumes next week looks like this week.
2. **Commitments:** what it will do, watch or remember, and the condition that makes it due. Scored on follow-through, and on raising it at the right moment.
3. **Quiet decisions:** what it noticed and chose not to raise. Scored by your rare "should have been mine" and by what happens later.

I'd adjust one piece of the framing. Treating every prediction as a promise invites the cheapest way to keep promises: make vague or safe ones. The promise frame fits commitments exactly. Claims are better scored as forecasts, which rewards being both right and informative. The handoff notes the distinction; I'd make it structural, since the three kinds need different scoring.

Claims split three ways by subject. Claims about the world (events, deadlines, obligations) are scored as forecasts. Claims about present you ("currently working on the mug mold") are checked for staleness: did the system notice when they stopped being true?

Claims about future you are saved and never scored. Each carries the date it was made and a tentative date for when it might come true. They sit in an archive outside what models see by default, so a prediction can't quietly make itself come true, and come out only on purpose, in reflection.

Standing commitments live in each angel's charter, not in the log: rules about behaving a certain way under certain conditions, and about respecting your authority. Trigger rules are checked mechanically; restraint rules take judgment and a look at what you were shown. A breach of a restraint rule weighs far more than ordinary misses.

Charters change without your sign-off, through orthogonal checkers: at least one on a different model family reading different context, and one chartered to argue for less. Narrowing changes go through when the checkers agree; widening changes also appear in a skimmable digest with one-tap reversal. Disagreements come to you, changes to restraint rules stay yours alone, and every change is versioned.

Repair is scored by behavior, not words: no repeat of the same error after a miss, and no retreat into silence in that area. A lapse the model owns up to first costs much less than one the resolution pass finds. Repair is scored to both the angel and the model, and the angel's record carries over when models are swapped.

Checker verdicts are weighted by track record, TrustRank-style: trust traces back to a seed of your taps and hard facts, per area, and can't be created by angels vouching for one another. For now the system only records who checked what, the verdict and how it resolved. Propagation gets computed once the graph is big enough to matter.

### Keeping the auditing burden near zero

Evidence comes from three channels, cheapest first: the automatic quick/deep cross-check, later captures resolving earlier claims, and occasional one-tap judgments from you. There is no review queue. If evaluation ever asks you to read a backlog, the design has failed its own restraint test.

The handoff's six dimensions are a lens, not six ratings. An orthogonal model tags each record by dimension. The tags explain results and guide job allocation but never feed scores, and you don't see them while rating.

Your input stays one "which helped more" tap, with an optional one-word why. Self-authorship isn't tagged per record; it's assessed in periodic reflection, using the future-you archive and idea provenance.

### Check-ins on the four-hour pulse

Check-ins nest by timescale, and each shrinks to fit the time you have, most important item first.

- **Four-hour pulse:** the micro layer. If you don't volunteer a catch-up, it nudges gently, backs off when ignored, and reads silence as possible flow.
- **Daily:** morning looks ahead, evening resolves. Which works better is the first experiment.
- **Weekly:** were commitments kept?
- **Monthly:** patterns, trust shifts, which angel is earning what.
- **Annual:** self-authorship, the future-you archive, idea provenance.

Rounds are threaded: a question planted for next month is a commitment, scored like any other. System-proposed threads are marked as such, and you can veto any. Missed rounds roll up into the next level, so nothing piles up, and "nothing to ask today" is a valid, logged outcome.

## Strategy: the recommended build sequence

Make the daily loop run and write records first, then test the replay method once, small, before investing in it.

1. **Unstick the daily loop.** Have Claude Code on Alpha Angel set up the Ambient Angel side over SSH: Syncthing, a dated landing folder, faster-whisper. You approve the pairing on the phone and record a ten-second test memo. Then the watcher and the four-hour pulse.
2. **A decision record for every capture, silence included.** Fields: what came in (by fingerprint), what was concluded, confidence, action taken or not and why, and any claim or commitment made with its due condition, each claim marked as about the world, present you or future you. This is step 4 of the 261121 plan, widened. Reconcile the fields with Grok's TriagePolicy\_Sketch and MinimalManifold\_Schema first; if those three files go into Drive or the repo, I can read them.
3. **Its own stream for every writer.** Give each model and angel its own stream in the log before any of them writes claims. This is the one-stream-per-contributor fix from 261123. An intelligence able to revise its own past claims makes the ledger worthless.
4. **A resolution pass on the four-hour pulse.** A different model from the claimant checks due items against what has been captured since, and writes a resolution entry pointing back. Items it can't resolve expire visibly.
5. **One replay pilot, by hand.** Pick a dense, well-timestamped date. 261110 is a good candidate, since what followed is well recorded: the pairing stall, the Whereabouts merge, Grok's docs, the extraction. Keep this one date, but ask each model about each area separately (projects, health, paperwork, people), so Better Angels knowledge alone can't win. Draw the other areas from sources with outside dates: chat histories (claude.ai, ChatGPT, Grok, Gemini), Facebook, Substack, email headers, calendars. A good question about a gap in the record counts as a contribution. Run 2 models across the four context packages below, rewrite all eight answers into one plain style, and rate them blind with 15 to 20 pairwise taps.
6. **Decide from the pilot.** If the conditions separate clearly, extend replay. If your ratings can't tell them apart, fix the method before running more.

### The bet: compare context packages more than models

In the 260814 Hutchins conversation you said frontier models already reconstruct the big picture well, and what's missing is longitudinal continuity and control. Continuity is a property of what the Responder hands the model, which it controls, not of the model's weights, which it doesn't. So the experiment most likely to change what you build holds the model fixed and varies the package:

- **A:** the last two weeks of raw captures.
- **B:** A plus the relevant area notes.
- **C:** B plus a Biographer-style running summary.
- **D:** an oracle package of the documents you'd pick by hand.

If D beats C by a wide margin, retrieval is the bottleneck. If D fails too, the model is. That answers the handoff's model-versus-architecture question directly.

Hold off on a separate ledger app, dashboards, or a many-model leaderboard until the pilot shows the method produces signal.

## Local model selection

Inkling 2 Mini is the strongest local candidate at full fidelity on the 7900 XTX, with Qwen on the other machine as the second opinion; the right benchmark for both is the Responder's own quick pass.

### Inkling: what actually exists

| Model | Total / active parameters | Fits 16 GB? | Source |
| --- | --- | --- | --- |
| Inkling 2 Mini (Nov 20, 2026) | 26.4B / 3.4B, about 5.4B effective with looping | Yes at 3-bit (12.6 to 13.3 GB); tight at 4-bit (15 to 17.5 GB) | [Model card](https://huggingface.co/thinkingmachines/Inkling-2-Mini), [AtomicChat GGUFs](https://huggingface.co/AtomicChat/Inkling-2-Mini-GGUF) |
| Inkling 2 Small | 594B / 17B | No: 171.7 GB at 1-bit | [Unsloth](https://unsloth.ai/docs/models/inkling-2) |
| Inkling-Small | 276B / 12B | No: 89 GB at 2-bit | [Unsloth](https://unsloth.ai/docs/models/inkling) |
| Inkling (Jul 2026) | 975B / 41B | No: about 290 GB at 1-bit | [Unsloth](https://unsloth.ai/docs/models/inkling) |

Caveats on the Mini. Its expert weights were trained at 4-bit, so the 20 GB release is the model at full fidelity, and a bigger download (BF16, Q8) adds no information to those layers. Thinking Machines recommends 32 GB or more of video memory for non-Apple GPUs, says local support for looped models is new, and lists Ollama only for Apple Silicon, so on your card the route is llama.cpp. The small active count is why it's fast. The 3-bit builds cost some fidelity: in AtomicChat's measurements the top token matches the original about 93 to 94% of the time at 3-bit, against about 96% at 4-bit. Images add a 0.64 GB vision module.

On the 7900 XTX, the 20 GB release fits whole with a few GB left for context, so there's no 3-bit loss. The XTX is AMD (ROCm or Vulkan, not CUDA), and support for new designs like looping sometimes reaches NVIDIA first. Confirm Inkling runs well there before planning around it; if not, Inkling stays on the 5070 Ti and Qwen goes on the XTX.

One trust-relevant property: looping lets the model reason longer without writing its reasoning down. That favors judging it by explicit records rather than by reading its chain of thought, which is how the ledger already works.

Hosted, Inkling 2 Small is cheap ([MindStudio listing](https://www.mindstudio.ai/models/inkling-2-small): $0.30 per million input tokens, $1.00 per million output), so it's a reasonable replay contestant.

### Qwen: the local landscape

- **Running now:** Qwen3-8B with 64k context, about 11 GB with the cache compressed.
- **Best that fits one consumer GPU:** Qwen3.8-27B ([Aug 2026, Apache 2.0](https://rits.shanghai.nyu.edu/ai/qwen3-8-27b-one-gpu/)). On 16 GB it needs 3-bit compression, about 15 GB total with 16K to 32K of context (approximate; my 261124 estimate).
- **Coming:** Qwen4-27B was [announced Sept 22 with no specs or date](https://www.yottalabs.ai/post/qwen-4-27b-release-date-specs-hardware-what-is-known-2026); no weights as of this report.
- **Your 24 GB 7900 XTX**, now being built out, runs a 27B at 4- or 5-bit. Its 64 GB of RAM lets llama.cpp keep a large mixture-of-experts model's idle experts in system memory, for slower batch work like replay.

### What to measure

The local tier's job in the Responder is the quick pass, so test candidates as the quick pass: Inkling 2 Mini (full release on the XTX, 3-bit on the 5070 Ti) against the Qwen sizes that fit. Run each in shadow mode on real captures beside the deep pass, and score:

- how often its routing matches the deep pass
- when they disagree, how often the disagreement was worth raising
- latency, and tool-call reliability
- whether it ran on Ambient Angel without waking Alpha Angel

That folds the handoff's speed and reliability benchmarks into data the system produces anyway. Allocation then follows the jobs: Ambient Angel, always on, runs the pulse, check-in delivery and recording, transcription, the LFM2.5 dispatcher and the logging gateway. It also sends the wake signal, since wake packets don't travel over Tailscale. The XTX box wakes for quick-pass batches, checking, resolution and replay; Alpha Angel's 5070 Ti runs the second model family when awake; frontier models take the deep pass and spot-checks. Check-ins that need thought are prepared ahead in a batch, so a sleeping machine never makes you wait.

### One model or two, and tooling

Two models on everything is the starting point, not a rule. A model that earns an area runs alone there, with random spot-tests that never drop to zero. Testing rises again after a model version change, a new area, a "should have been mine" tap or a missed commitment.

Restraint rules, charter widening, and actions touching medical, legal or money matters stay double-checked regardless. Records are keyed by model and version; the machine matters only for speed and cost.

No agent framework yet (working lean). The pulse is a scheduled script calling models through llama.cpp's server, the same OpenAI-style interface on every machine, with records going straight to the event log. Tools sit on MCP (Model Context Protocol) servers, and every tool call passes through a gateway that writes a decision record.

That gateway is the fixed point. Any framework, Hermes or something newer, can be swapped in later once a specific pain calls for one, most likely when several angels start acting rather than reading.

## Design failure modes worth fixing early

The most damaging one is replay leaking the future; most of the rest are cheap to prevent now and expensive to retrofit.

| Failure | What goes wrong | Fix |
| --- | --- | --- |
| Replay leaks the future | Essays revised in place, notes updated, file dates rewritten by copies: the "past" slice quietly contains later knowledge | Build slices only from material with intake times and fingerprints (Porter's ledger, git history, chat timestamps, the event log). Another reason the corpus/canon manifest matters. Imported exports keep two times: when it happened, per the platform, and when it was received |
| Hindsight grades the rater | Blind rating hides which model answered, not what happened next, so you'll favor answers that matched the outcome | A second model, run locally with frontier spot-checks, marks whether each claim was grounded in the slice. Replay is a rough screen; the live ledger gives the verdict (provisional) |
| Useful warnings score as misses | A warning you act on prevents what it predicted, so the forecast resolves false | Warnings state their condition ("unless you act by Friday"). If you acted, only "worth raising?" is scored (provisional) |
| Borrowed insight | The slice holds other AIs' past suggestions; a model repeats one and gets credit for it | Tag AI-originated material in the slice. Grounding counts your words and records, not another model's guesses |
| Easy predictions inflate scores | "Keith will keep working on Better Angels" is always right | Credit only what beats a lazy forecaster that assumes next week looks like this week |
| Hedging to protect the record | An intelligence learns to promise little and claim vaguely | Forecast scoring that rewards informativeness; count each commitment's cost in your attention |
| Blind ratings aren't blind | Models have recognizable voices | A separate model rewrites every answer into one plain house style before you see it |
| Self-grading | The claimant judges its own claim | The resolver is never the claimant |
| Silence is invisible | A missed item and a correct quiet look identical | Quiet decisions get records, with reasons |
| Engagement rewards nagging | Nudge response rate rises with nudge count | Pair it with a "worth it?" tap, and credit restraint when nothing needed doing |
| Guesses harden into facts | Already flagged 261121: "Keith seems to be working on pottery" becomes a fact | Every claim about you carries an expiry date and lapses unless reconfirmed. Lapse rates become the staleness measure |

One subtler risk, sketched lightly: anticipation can disguise steering. A system that predicts your next interest and then helps it happen looks well calibrated. Logging who first raised each idea, you in a capture or a model in a suggestion, keeps that visible without slowing anything down.

## Decisions for you and next steps

Three calls are yours; the rest is sequenced above.

- **Name:** Responder, First Response, or keep First Responder.
- **Where the ledger lives first:** the phone event log works today and already has the integrity properties. Its live copy sits in claude.ai storage, though, with Drive as backup, not on your machines. My lean: start there, and mirror to Ambient Angel with the nightly rclone pull already proposed on 261123.
- **The pilot:** one date, 261110 for now, with questions by area. Still open: whether the four context packages are the right ones.

### Next steps

- [ ] Ambient Angel: Syncthing installed and paired, landing folder, test memo (via Claude Code over SSH)
- [ ] A fixed handoff folder convention for Claude Code across machines
- [ ] Grok's three 261117 docs into Drive or the repo
- [ ] One-page decision-record schema with the three entry kinds
- [ ] Per-contributor streams in the event log
- [ ] Replay pilot
- [ ] First charter drafts, with your restraint rules
- [ ] Exports from ChatGPT, Grok, Gemini and Facebook through Porter, keeping platform timestamps
- [ ] 7900 XTX box: build, wake-on-LAN from Ambient Angel, confirm Inkling 2 Mini runs under ROCm or Vulkan

## Sources

- [Unsloth: Inkling 2 Small, run locally](https://unsloth.ai/docs/models/inkling-2)
- [Unsloth: Inkling and Inkling-Small](https://unsloth.ai/docs/models/inkling)
- [MindStudio: Inkling 2 Small pricing](https://www.mindstudio.ai/models/inkling-2-small)
- [RITS: Qwen3.8-27B on a single consumer GPU](https://rits.shanghai.nyu.edu/ai/qwen3-8-27b-one-gpu/)
- [Yotta Labs: what's known about Qwen 4 27B](https://www.yottalabs.ai/post/qwen-4-27b-release-date-specs-hardware-what-is-known-2026)
- Internal: the 261121 First Responder summary doc, the 261123 event log session, memory notes on First Responder, Better Angels, Porter and hardware
- Internal: the 261127 handoff, "Better Angels — Evaluating Intelligence Through Longitudinal Trust"
