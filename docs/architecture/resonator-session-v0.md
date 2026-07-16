---
title: Resonator Session v0
status: DRAFT - first operational note, pre-build
date: 2026-07-06
companions: ../core/resonator-charter.md, ../core/boba-braid.md, ../essays/braided-discourse.md, braided-discourse-design-spec.md, ../core/continuity-and-decision-lineage.md
question: what does a Resonator pass do inside a braid?
---

# Resonator Session v0

This note answers the audit gap: the Resonator is well named and structurally
bounded, but its session behavior has not been described concretely enough.

The Resonator is not a separate product bolted onto BOBA. It is a participant in
the Braid whose special work is to keep Keith, Future Keith, and the ongoing
conversation legible to one another in service of emergent Self-authorship.

Its core motion is resonance: noticing the harmonies and interesting dissonances
between present Keith, the durable record of prior Keith, and the Future Keith
being made more possible or less possible by present choices.

Here **Self-authorship** has the special BOBA meaning: not preference
satisfaction, not compliance with present utterance, and not optimization toward
a fixed ideal. It names an unfolding process in which a life becomes more able
to choose itself from its deeper potential.

This is a first operational note, not an implementation claim. No braided
deliberation router, contribution-vector scorer, or Resonator runtime exists yet.
The v0 described here can be performed manually in the Salon or in a short
append-only trace before any platform is built.

## 1. Purpose

A Resonator pass helps the braid keep making sense of Keith over time.

It does not primarily produce a task, recommendation, or final answer. Those may
appear, but they are secondary. The useful output is a better-shaped shared
state:

- what is live in Keith right now;
- what in the current surface rhymes with prior commitments, patterns, or open
  questions;
- what dissonance should not be flattened;
- what Future Keith seems to be asking present Keith to preserve, revise, or
  notice;
- what should be remembered as lineage rather than lost as chat exhaust.

## 2. Contribution vector

The Resonator's expected contribution vector is:

| Dimension | What the Resonator contributes |
|---|---|
| Affective salience | Notices charge, vulnerability, warmth, avoidance, grief, irritation, relief, and trust. |
| User-intent preservation | Holds Keith's deeper drift when literal wording is incomplete or noisy. |
| Emergent Self-authorship | Tracks the evolving shape of the life Keith is becoming more able to choose. |
| Autobiographical continuity | Relates present material to prior choices, recurring motifs, and future consequences. |
| Dissonance detection | Preserves productive contradiction without forcing premature synthesis. |
| Compression | Names the smallest durable shape that should survive into the trace. |
| Care boundary | Notices when reflection is not enough and a human/crisis path may be needed. |
| Anti-flattery | Reflects honestly without converting care into agreement. |

This contribution vector is provisional. In the mature braid, it should be
discovered empirically from traces, not asserted once and treated as identity.

## 3. Inputs

A Resonator pass needs only a small surface at first:

- the current user utterance or conversation fragment;
- any active Salon/open-question context directly referenced by the fragment;
- a short memory summary or prior trace, if one exists and is safe to read;
- the current privacy class and egress policy;
- any explicit user correction, resistance, or phrase marked as alive.

For real confidential sessions, the prerequisites in
[resonator-charter.md](../core/resonator-charter.md) still gate use: encrypt
first, apply `confidential:resonator`, block or gate egress, and define the
crisis path. Before that exists, use throwaway or non-confidential material.

## 4. The pass

### 4.1 Establish the boundary

The Resonator starts by checking the operating boundary:

- Is this confidential Resonator material?
- Is the current channel local-only?
- Is any outside model or outside human being drafted?
- Is there distress that requires the care path rather than more reflection?

In v0, the default answer is local-only and no egress. If the boundary is not
safe, the pass stops or continues only on a deliberately non-confidential
abstraction.

### 4.2 Open the active surface

The active surface is the smallest temporary medium where the present question
can be held. For early text-only work, this is just a paragraph surface:

```yaml
surface:
  kind: resonator_text_surface
  purpose: hold present Keith, prior trace, and Future Keith tension
  privacy: local_only
  status: active
```

Later, this may become a timeline, affective trace, graph patch, audio contour,
or embedding basin. The v0 does not need those to prove usefulness.

### 4.3 Listen for harmonies

The Resonator asks what in the present material harmonizes with the durable
record:

- Does this echo a prior commitment?
- Does it continue a known pattern without needing to restate the whole history?
- Does it reveal that something once vague has become clearer?
- Does it show present Keith acting in care toward Future Keith?

The output is not praise. It is a named resonance that other participants can
use.

### 4.4 Listen for dissonances

The Resonator also asks what should remain unresolved:

- Is there a tension between what Keith says he wants and what the current move
  would make more likely?
- Is a protective part speaking as if it were the whole person?
- Is the system trying to close a question that should stay open?
- Is an angel mistaking fluency, speed, or agreement for care?

Dissonance is not failure. It is often the most useful billboard the Resonator
can post into the braid.

### 4.5 Address Future Keith

The distinctive Resonator move is to include Future Keith without making Future
Keith an external authority.

The question is not "what would an optimized Keith do?" The question is:

> What present choice would make Keith more available to the Keith he is trying
> to love and cherish tomorrow?

This keeps continuity personal rather than managerial. The Resonator does not
optimize Keith toward a fixed endpoint. It reflects how present choices shape the
person who will inherit their consequences, and whether those choices make the
unfolding process of Self-authorship more available or less available.

### 4.6 Post a billboard, not a verdict

The Resonator should usually produce a billboard into the braid rather than a
final judgment. A useful billboard is short, traceable, and easy for another
participant to be changed by.

Examples:

```yaml
billboard:
  source: resonator
  type: dissonance
  payload: "The current plan preserves momentum but may spend tomorrow's Keith's trust."
  recommended_effect:
    - slow_down
    - ask_what_needs_preserving
    - avoid_false_closure
```

```yaml
billboard:
  source: resonator
  type: harmony
  payload: "This choice echoes the local-first care boundary rather than merely the privacy slogan."
  recommended_effect:
    - keep_boundary_visible
    - record_as_lineage_candidate
```

### 4.7 Close with a trace candidate

At close, the Resonator proposes what should survive:

- one named harmony, if present;
- one named dissonance, if present;
- one phrase, question, or choice that Future Keith may need later;
- whether this should remain a temporary surface, enter the Salon, or be
  promoted to Asterisms after review.

It does not need to force a next action. Sometimes the right close is: preserve
the tension and do not decide yet.

## 5. Minimal manual trace

Before building a router, a Resonator pass can be recorded as a small JSONL or
Salon entry:

```json
{
  "kind": "resonator_pass",
  "surface": "present-keith/future-keith",
  "input_ref": "salon:entry-or-file-ref",
  "harmonies": ["..."],
  "dissonances": ["..."],
  "future_keith_question": "...",
  "billboards": [
    {"type": "dissonance", "payload": "..."}
  ],
  "survival_recommendation": "temporary|salon|asterisms-candidate",
  "privacy": "local-only",
  "egress": "none"
}
```

This is enough to test whether the Resonator is helpful. If the trace does not
improve later orientation, preserve user intent, or reduce false closure, the
concept should be revised before code is built.

## 6. First scenario to test

Use the current design question as the first scenario:

> Is braided discourse necessary and useful, or is it pie in the sky?

A Resonator pass should not answer only with architecture. It should notice that
the question carries practical concern: Keith does not want a beautiful theory
that consumes attention without becoming useful. The harmony is with BOBA's
discipline of ground truth over narration. The dissonance is that the same
language that names a real interaction pattern can become platform fantasy if
it outruns use.

The Resonator billboard might be:

> Treat braided discourse as a discipline already needed in conversation, not
> as a platform to build before proof. The first proof is whether this very
> Resonator pass helps future work stay clearer.

## 7. Non-goals

- Do not make the Resonator a therapist, diagnostic tool, or shame engine.
- Do not make it a general task planner.
- Do not require a full router before testing it manually.
- Do not turn every reflection into an action item.
- Do not send confidential Resonator material outside the local boundary in v0.
- Do not treat Future Keith as a productivity manager. Future Keith is the
  inheritor of care, not a boss.

## 8. Open questions

- What exact crisis threshold and care path should v1 use?
- What belongs in the durable trace versus a temporary surface?
- How does the Resonator ask for correction when it misreads Keith?
- How should confidentiality / access control interact with
  `confidential:resonator` records? (**Not** a forgetting path —
  [`no-forgetting.md`](../core/no-forgetting.md); `oq-009` closed.)
- Which parts of this pass should be automated first, and which should remain
  human-reviewed until the contribution vector is proven?

## 9. Next implementation-sized move

Do not build the router yet. Run three manual Resonator passes over existing
BOBA questions and record whether they helped:

1. braided discourse: useful discipline or platform fantasy;
2. `confidential:resonator`: hard local-only wall or gated egress;
3. confidentiality without forgetting: encrypt-at-rest and access control under
   [`no-forgetting.md`](../core/no-forgetting.md) (no crypto-shred / key-fade).

After three passes, compare the traces. If the Resonator consistently names
useful harmonies/dissonances that other participants build from, then the next
small code move is a trace schema and CLI helper. If not, revise the pass before
building machinery.
