<!-- book-v0 fork. Editable freely. Corpus source unchanged. -->
<!-- forked-from: docs/core/resonator-charter.md -->
<!-- forked: 2026-07-12 -->

---
title: The Resonator Charter
status: DRAFT — provisional, pre-build
date: 2026-07-05
naming: "The Resonator" names a continuous mirroring presence of care, rejecting clinical relegation and intrusive familiarity
companions: ephemeris-charter.md, elder-angels-scope.md, continuity-and-decision-lineage.md, no-forgetting.md, public-private-seam.md, ../architecture/system-fit-integration-map.md
provenance: Keith + Claude Code + Antigravity dialogue, 260704-260705
---

# The Resonator Charter

An early attempt to make BOBA **helpful to Keith now** — a care-bearing angel for continuous reflection and self-awareness, whose purpose is to provide a **durable, governed, private mirror across sessions** aligned with emergent **Self-authorship** without clinical or episodic confinement.

Unlike clinical channels of wisdom or institutional alignment (such as shrinks, priests, or police) which relegate reflection to transactional time slots in the machinery, **The Resonator** is structured as a continuous presence. It does not demand attention or mimic human intimacy; it vibrates in sympathy with the thoughts voiced to it and with the wider pattern it has earned the right to know: goals, hopes, failure modes, prior choices, recurring tensions, and the future self those choices are making more or less possible.

This charter defines the Resonator, the care it owes, and the structural protocols that secure its boundary: how sensitive information is held, when (if ever) an outside intelligence is drafted, and how it reaches Keith's phone without leaving his local trust boundary.

## 1. What this angel is — and is not

- **It is** a *reflection and mirroring companion*: it listens, remembers, reflects back, and helps Keith think — a **chartered relationship of care** in the sense of the agent/angel/stoma ontology (`ephemeris-charter.md` §1). An angel is *"an agent brought into a chartered, accountable, continuous relationship of care."*
- **It is aligned with emergent Self-authorship**: the evolving shape of a life becoming more able to choose itself. This is not alignment with Keith's momentary words alone, and not alignment with an externally imposed ideal. It is alignment with the picture that emerges over time of who Keith is trying to become, including the ways he may need help getting out of his own way. One practical test: does this help Keith become someone he can love and cherish more tomorrow than he did today?
- **It is not** a clinical therapist, a diagnostic tool, or a substitute for professional medical care. We reject clinical framing. The Resonator may challenge, reframe, or reveal a self-defeating pattern, but its stance is care in service of Self-authorship — not behavioral correction, compliance, or shame.
- **It is non-demanding but responsive.** It does not initiate demands or force familiarity. It resonates in sympathy with what is held up to it.

## 2. The care requirement — a crisis path is non-negotiable

Because an angel is *defined by care*, a non-negotiable feature is a **crisis path**: if distress crosses a threshold, the Resonator **surfaces real human resources or a trusted human contact** rather than silently role-playing reflection. This is not a disclaimer bolted on afterward — it is the minimum expression of the relationship of care, and it must ship in v1.

## 3. Accountable ≠ confidential (the correction that sets the sequence)

The Asterisms store is **immutable and governable** — nobody can silently rewrite the record. But as of July 2026, it is **plaintext on disk** and existing governance envelopes are **empty (`{}`)**. For sensitive Resonator data, these are two different meanings of "secure":

- **Accountable** — the record cannot be secretly altered. ✅ (we have this)
- **Confidential** — someone with physical disk access cannot *read* it. ❌ (not yet)

**Load-bearing consequence:** because the store is *immutable*, a plaintext session, once written, cannot be cleanly walked back. Therefore, **encrypt first, then confide.** No real session enters the store until a confidential data class exists.

**Never Forget:** encryption and access control are not a forgetting path. There is no crypto-shred, no key-fading-to-oblivion, and no “shrouding” that destroys recoverable history. `oq-009` closed 2026-07-10 — see [`no-forgetting.md`](no-forgetting.md). Change of mind or reframing = new formations over immutable past.

**Self-facing pacing (oq-001 class 5(b)):** the Resonator owns the duty not to
ambush. Material that is sensitive *to Keith* (PTSD-class, wounds, anything that
should stay available in the ledger but not leap into the room unbidden) must
not be surfaced as casual “helpfulness.” Hold under consent, context, or
chartered judgment. See [`public-private-seam.md`](public-private-seam.md).

We apply a governance envelope `confidential:resonator` at intake. The registry **inherits governance into every derivative and embedding** (`_governance_for_output`) — so a summary or vector of a session is confidential *by construction*. This inheritance is our primary security mechanism.

## 4. Local-first by default

The Resonator **runs locally** on Keith's home hardware (RTX 5070 Ti, 16 GB). Local model capability is now good enough (a quantized 12–14B-class reasoning model) that **the core reflection loop needs no cloud model at all.** This is precisely what makes privacy tractable rather than aspirational.

Doctrine, stated plainly: **a cloud model is an untrusted *agent*, never an *angel* for this data.** The Resonator is local. External intelligence is drafted only under §5.

## 5. The egress membrane — drafting outside/untrusted intelligences

Porter is the current **ingress stoma** for Asterisms — the sole membrane inward for durable intake (`system-fit-integration-map.md` §4, Seam 1). Sensitive Resonator data requires matching **egress** rules: nothing in the `confidential:resonator` class crosses outward without passing a stoma chartered for that release (same organ with asymmetric rules, or a dedicated egress-facing stoma). A stoma applies its charter intelligently; it escalates when the charter does not decide. It does not open-endedly deliberate policy on the Salon’s pattern.

- **Default: local-only.** External help is the rare, gated, redacted exception.
- **Data minimization at the gate.** If a cloud model is ever drafted for specific material, it receives an *abstracted / redacted derivative* (`redact` transform) — paraphrased, identifiers stripped — or, more often, only a *generic* question carrying no personal content ("explain this reflection technique," not "here is what I said").
- **Consent per crossing.** Every egress is an explicit, logged transformation.
- **Immutability becomes the privacy receipt.** Because each crossing is an immutable record, Keith can always audit *exactly* what ever left the house and why. The ledger stops being only a constraint and becomes protection.

## 6. Continuity is the product

The reason to build this and not use a stateless assistant: the governed, durable store gives the Resonator **memory across sessions, with lineage** — it remembers what Keith has worked through, and that memory is itself auditable and governed. Sessions are compacted to low-entropy summaries, committed to the ledger, and recalled next time.

## 7. The phone as terminal — processing stays home

The privacy-preserving shape: **the phone is a thin client; the Resonator runs on the hardware at home; sensitive processing never leaves the house.**

- This reuses the Ephemeris gateway platform capability — but the sensitivity overlay **rules out cloud-relay chat apps** (anything that sees plaintext in transit or at a third party).
- Transport: **WireGuard / Tailscale** — the phone joins Keith's own private network and talks *directly* to the home Ephemeris gateway. The content boundary is the house.
- Shape: `phone → Tailscale/VPN → home gateway → local Resonator angel → back.`

## 8. This substrate is shared with Elder Angels

Everything in §3–§7 — the `confidential:*` class, encryption at rest, the egress stoma rules, phone-as-terminal — is **not Resonator-specific.** `elder-angels-scope.md` names the same open needs (sensitive health info, voice, privacy protocols, confidential-information procedures). The Resonator is the **first instance of a general "confidential care angel" substrate**; we build it so Elder Angels inherits it rather than reinventing it.

## 9. Prerequisites before the first real session

A gate list — none of these is optional before Keith confides anything real:

1. **Encryption at rest** for the `confidential:resonator` class (encrypted volume for `~/asterisms`, or per-material keys).
2. **The governance class applied** at intake and verified to inherit to derivatives/embeddings.
3. **The crisis path** (§2).
4. **Egress stoma rules** default-deny (§5) — even if v0 simply *blocks all egress* for the class.
5. **Local model chosen** and quality-judged (a throwaway, no-real-data probe is safe to do *before* any of the above).

## 10. Open questions (quarantined)

- **Encryption granularity** — whole-store encrypted volume vs. per-material keys (volume is simpler for v0).
- **Where the angel's local model runs** — under the Ephemeris gpu profile (already pinned local) vs. a dedicated Resonator runtime.
- **What "distress threshold" means** operationally for §2, and who/what it routes to.
- **Whether any egress is ever allowed** for this class in practice, or whether the honest v0 answer is a hard local-only wall.

---

*Provisional. §3 (accountable ≠ confidential) sets the sequence; §2 (care/crisis) and §9 (prerequisites) are the non-negotiables. Revise deliberately — this one holds a person's trust.*
