# Membrane Escalation Checklist v0

**Status:** active for thin collaboration cut (2026-07-10)  
**Audience:** Keith (human membrane). Visitors do not run this.  
**Companions:** `selective-collaboration-membrane-v0.md`, `collaboration-surface-thin-cut-260710.md`, Salon CHARTER.

## When something lands on the Salon floor

For each entry (or batch in a session), ask:

1. **Ignore / leave on floor** — noise, already answered, or wallflower-appropriate.
2. **Answer on floor** — short claim with `refs`; no durable change.
3. **Open / update an open question** — unsettled; stays visible in `open-questions.jsonl`.
4. **Escalate to me (PRIORITIES)** — needs human judgment this week.
5. **Open an Ephemeris score** (optional) — chartered work with boundaries; use when
   coordination across agents matters. Ephemeris is still thin; scores are Keith-side.

   ```bash
   cd ~/boba_work/ephemeris
   PYTHONPATH=src python3 -m ephemeris.cli score open \
     --participant eph:participant:human:keith:main \
     --concern "short concern" \
     --boundaries "what is in / out of scope"
   ```

6. **Resonator pass** — reflective / care-sensitive; not a public floor matter.
7. **Promote via Porter** — only if it deserves to survive as durable material.
   Then triage fate in `~/asterisms/90-system/intake-triage.md`.
   **Never auto-promote into BOBA core.**

## Default bias

Wallflower. Prefer leave-on-floor or answer-on-floor. Escalate sparingly.
Durable survival is rare and deliberate.
