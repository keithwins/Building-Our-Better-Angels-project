# Red-Team Findings — Invitation Reader v0

**Score:** `eph:score:20260707T003608Z-4247` · **Reviewer:** Claude (CC)
**Date:** 2026-07-07 · **Read as:** the skeptic, the person in the fog, the technical reader
**Grades:** `BLOCKS` (don't print) / `WEAKENS` (print, but fix before next edition) / `POLISH`
**Copies:** each finding marked for **K** (Keith-copy) and/or **TR** (trusted-reader copy)

---

## Verdict

**Keith-copy: PRINT IT.** Zero blocking findings. All cited receipts verified
real (both salon timestamps, the web-conversational doc, both ast: records, the
score ID). **Update 2026-07-10:** `oq-009` is closed — [`no-forgetting.md`](../../core/no-forgetting.md).
Gate 2 in sources now states No Forgetting as settled doctrine.

**Trusted-reader copy: correctly self-assessed as not-yet.** The gates the
packet names are the right gates. Findings below add four more items to close
before that edition.

---

## Findings

### F1 · WEAKENS (TR only, fine in K) — The title's argument is never cashed
"Better angels" is defended ("the name is a little embarrassing, which is one
of its virtues") but its lineage — Lincoln's secular "better angels of our
nature," angel-as-genus, ontology-kept/epistemology-replaced, *these are angels
you verify* — never appears. A skeptical outside reader hears vague theology;
the disarming answer exists on the ledger (`ast:record:…-B6SBQC`) and isn't
used. **Fix:** 2–3 sentences in the prologue or ch. 4 seed.

### F2 · WEAKENS (TR; margin-note in K) — The mirror edges toward owning the picture
Ch. 8 spine: the Resonator "notice[s] harmonies and dissonances between present
choice and the future person those choices are helping create." One step from
the mirror holding its own theory of who you're becoming — the intimate form of
the reflexivity hazard. The salon thread already has the guardrails (picture
stays Keith-authored, angel-attended; the deeper-drift reading revisable on the
record). **Fix:** one clause: the mirror surfaces the picture; it never gets to
decide it.

### F3 · WEAKENS (TR; intentional in K) — Two registers, one binding
The prologue speaks in book-voice; the Field Notes speak in editorial-voice
("The book should be ruthless about this distinction"). For the Keith-copy this
is the design — pressure tests beside prose. A trusted reader will experience
it as the book arguing with itself mid-sentence. **Fix for TR:** field notes
either graduate to book-voice or move behind an explicit "workshop" divider.

### F4 · POLISH (K+TR) — Signature line diluted by repetition
"The record keeps receipts. The score sets (the) boundaries. The stop condition
remains real." appears verbatim in the prologue *and* the No Loyalty Oaths
field note. A signature line spends its force the second time. Keep the
prologue instance.

### F5 · POLISH (K+TR) — Front-matter stack delays the door
Title/status → How To Read → Prologue means the person in the fog does ~1,100
words of apparatus before the first sentence written for them. The tonight
edition reportedly moves gates to back matter (good); consider prologue-first,
apparatus-after for the next build of the md packet too.

### F6 · POLISH (repo hygiene) — `tools/__pycache__/*.pyc` is committed alongside sources
Add `__pycache__/` to gitignore before this directory gets busy.

### F7 · OBSERVATION (no grade) — What passed that I tried to break
- oq-009 compliance: Gate 2 now states settled **No Forgetting**
  (`docs/core/no-forgetting.md`, closed 2026-07-10). Earlier packet drafts used
  provisional safer language before the ruling; that was correct for the time.
- Provenance: every source ref I spot-checked exists on disk or in the log.
  After tonight's NPC-salon incident this was the first thing I hunted.
- The humor is load-bearing, not decorative ("expensive echo"; the pronunciation
  accident; the sprout triad). Nothing manufactured found.
- The Multitude field note's patience ("some protectors learned their craft in
  bad weather") is the best new prose in the packet and is correctly held back
  from hardening pending the April seed.

---

## Standing gates (unchanged, packet already names them)
oq-001 (public/private seam) · ~~oq-009 (forgetting)~~ closed → no-forgetting.md · April Drive seed
for the Multitude · Social Protocol chapter (rope/countertwist mechanism on the
ledger, awaiting integration) · polyphony score.

*Findings delivered; score closes with this file as the survivable artifact.*
