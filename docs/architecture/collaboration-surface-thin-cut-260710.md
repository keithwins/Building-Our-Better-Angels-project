---
title: Collaboration surface for eclosion — thin cut
status: DRAFT sketch
date: 2026-07-10
companions: web-conversational-orientation-surface-v0.md, selective-collaboration-membrane-v0.md, ../core/ephemeris-charter.md, interagency-orientation-surface-v0.md
---

# Collaboration surface — thin cut (given thin Ephemeris)

## Honest dependency

Eclosion’s public face does **not** require a mature Ephemeris. Ephemeris v0 is a
CLI + log: enough to open/close scores and force `ast:` on consequential
handoffs; not enough to be the visitor-facing coordination UI.

So the thin cut **leans on Salon + membrane + curated orientation**, and treats
Ephemeris as **Keith-side** coordination (escalations become scores when useful),
not as something visitors operate.

## What ships in the thin cut

1. **Orientation** — curated public docs (invitation spine), not the whole vault.
2. **Salon floor** — document-tied questions/comments (interagency collaboration
   surface); append-only; page-scoped `refs`.
3. **Membrane (mostly Keith)** — escalate important items to PRIORITIES /
   Ephemeris score / Resonator pass; no auto-promote into core.
4. **Porter** — only path for durable survival of anything that should leave the
   floor.

## What waits

- Visitor-facing Ephemeris UI
- Auto-wake angels for public traffic (rate/cost/trust)
- Spin-up / hardware guides for other people’s full stacks

## Build order

1. ~~Public doc allowlist + web nav that doesn’t deep-link private vault paths~~ **done 2026-07-10** (`web/public-allowlist.json`, rebuilt `web/index.html` / `app.js`)
2. ~~Real Salon path only (retire mock); composer on allowlisted pages~~ **done** — mock nav/paths removed; `salon.js` is the only floor UI
3. ~~Escalation checklist (human membrane)~~ **done** — `docs/method/membrane-escalation-checklist-v0.md`
4. **Thick later:** thicken Ephemeris only if coordination pain demands it (visitor UI, richer multi-participant coordination)

## How to run (local)

```bash
# from boba_work — salon-serve serves web + /salon/ write API
~/boba_work/salon/bin/salon-serve
# open the BOBA web root it exposes (see salon README)
```

If using a plain static server for docs only, Salon writes stay read-only until `salon-serve` is up.
