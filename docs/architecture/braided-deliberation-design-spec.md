---
title: "Braided Deliberation"
subtitle: "Design Spec Overlay"
version: "0.1"
status: "⚠️ ROUGH DRAFT v0.1"
description: >
  Toward a deliberative mixture-of-experts architecture.
  Implementation-facing companion to the Capture Memo.
---

> **⚠️ ROUGH DRAFT — This document is an early working draft. It has not been reviewed, stabilized, or approved. Expect gaps, inconsistencies, and structural changes.**

# Braided Deliberation — Design Spec Overlay

**Toward a deliberative mixture-of-experts architecture**

*Version 0.1 — Implementation-facing companion to the [Braided Deliberation Capture Memo](../essays/braided-deliberation.md)*

> *The real unit is not persona. It is contribution vector.*

> *A surface is a temporary medium of coherence: a place where thought can leave weather marks.*

> *Deliberative MoE routes the next transformation, not merely the next token.*

---

## 0. Purpose and Scope

This document translates the [Braided Deliberation Capture Memo](../essays/braided-deliberation.md) into an implementation-facing design overlay. It is not a final engineering specification. It is a scaffold for building and testing a local cognitive ecology in which LLMs, non-LLM tools, humans, retrieval systems, sensors, and external models can participate in shared reasoning without requiring a single shared ontology or exposed chain-of-thought.

The design treats cognition as a pattern of consequential transformations across temporary surfaces of coherence. Participants do not need to exchange private reasoning. They need to post useful transformations, signals, or billboards that can alter the trajectory of the braid.

The immediate design target is a local-first prototype that can host two or more local models and a small set of non-LLM processes, while learning when to summon outside contribution from a human, a frontier model, a cloud model, or a crowd model.

## 1. Core Design Commitments

- **Do not center hidden chain-of-thought.** Center durable transformations of shared state.
- **Do not equate agent identity with persona.** Profile contribution vectors empirically. *(See [on-scores-and-harnesses.md](../essays/on-scores-and-harnesses.md) for trust mechanics.)*
- **Do not treat the blackboard as an org chart.** Condense temporary surfaces where thought needs a place to happen.
- **Do not force all signals into full coherence.** Preserve sub-coherent influence when it usefully bends the braid.
- **Do not call expensive or external minds by default.** Summon them when the local braid knows what it needs and what it can safely expose.
- **Do not optimize for agreement alone.** Optimize for useful nonredundant transformations.

## 2. System Primitives

> See also: [glossary-and-ontology.md](../core/glossary-and-ontology.md) for canonical definitions.

| Primitive | Definition | Implementation hint |
|---|---|---|
| **Participant** | Anything that can perceive state, transform state, or post a signal. | LLM, embedding search, graph process, sensor classifier, human, frontier model, crowd model. |
| **Contribution vector** | Empirical profile of the transformations a participant tends to provide. | Tracked over tasks, partners, roles, surfaces, and braid states. |
| **Surface** | Temporary medium of coherence where a transformation can occur. | Text scratchpad, graph patch, image board, audio contour, memory cluster, schema, timeline. |
| **Billboard** | Partially interpretable influence packet visible across surfaces or participants. | Can be prose, tags, vector IDs, affect signals, image descriptors, confidence deltas. |
| **Trace** | Durable record of consequential transformations and routing decisions. | Append-only event log plus summarized durable memory. *(See [continuity-and-decision-lineage.md](../core/continuity-and-decision-lineage.md) on immutability.)* |
| **Router** | Chooses participant, mode, surface, disclosure level, and budget. | Starts rule-based; later learns from downstream effects. |
| **Adjudicator** | Accepts, rejects, merges, branches, or preserves tensions between transformations. | Can be one model, a voting process, a rules engine, or human-controlled. |
| **Spend manager** | Estimates whether outside contribution is worth money, latency, privacy, dependency, and disruption costs. | Attached to router as a cost-aware gate. |

## 3. Reference Architecture

The architecture is a router-managed ecology rather than a committee of agents. A participant acts only when a surface needs a transformation and the router expects that participant to provide useful, nonredundant movement.

```
user_input
  -> state_interpreter
  -> surface_manager
  -> router
  -> participant_call(s)
  -> billboard_ingestion
  -> adjudicator
  -> trace_update
  -> profile_update
  -> synthesis_or_next_cycle
  -> user_visible_response
```

> See also: [ephemeris-charter.md](../core/ephemeris-charter.md) for coordination patterns.

### 3.1 Minimal components

- **State interpreter:** parses the user prompt, current trace, live interventions, and active surfaces.
- **Surface manager:** creates, updates, merges, suspends, or dissolves temporary media of coherence.
- **Router:** decides what transformation is needed and who should attempt it.
- **Participant adapters:** normalize calls to local LLMs, tools, retrieval systems, sensors, or external models.
- **Billboard bus:** accepts partial signals that may be less than fully coherent but still influential.
- **Adjudicator:** determines which transformations enter canonical state, branch state, or trace only.
- **Profile learner:** updates empirical participant and relation profiles from downstream effects.

## 4. Data Model

The following schemas are intentionally lightweight. They should be treated as starting shapes for JSON, YAML, or local database records rather than fixed ontology.

> See also: [glossary-and-ontology.md](../core/glossary-and-ontology.md) for term definitions.

### 4.1 Participant

```yaml
participant:
  id: local_qwen_27b_q4
  kind: llm
  locality: local
  modalities: [text]
  cost_profile:
    money: low
    latency: medium
    privacy: low
    vram_pressure: high
  current_affordances:
    - decomposition
    - implementation_specificity
    - schema_generation
  known_failure_modes:
    - overlong_outputs
    - brittle_confidence_estimates
```

### 4.2 Contribution vector

```yaml
contribution_vector:
  participant_id: local_model_A
  scope:
    task_family: conceptual_architecture
    partner: local_model_B
    surface_type: text_schema
  scores:
    decomposition: 0.72
    constraint_sensitivity: 0.81
    contradiction_detection: 0.64
    compression: 0.58
    novelty_generation: 0.47
    reframing: 0.69
    affective_salience: 0.35
    user_intent_preservation: 0.74
    implementation_specificity: 0.86
    epistemic_humility: 0.61
  confidence: 0.42
  sample_count: 17
  last_updated: 2026-06-02
```

### 4.3 Surface

```yaml
surface:
  id: surface_2026_06_02_001
  form: text_schema
  purpose: hold implementation-facing routing architecture
  status: active
  coherence_level: medium
  contents_ref: local_object_uri_or_json_blob
  associated_trace_events:
    - trace_event_101
    - trace_event_104
  dissolution_policy:
    merge_if_adopted: true
    archive_if_stale_cycles: 3
```

### 4.4 Billboard

```yaml
billboard:
  id: billboard_204
  source_participant: affect_classifier_v1
  target_scope: any_surface
  coherence_level: sub_coherent
  medium: signal_tags
  payload:
    arousal_change: sharp_increase
    confidence: 0.72
    interpretation: possible_salience_not_necessarily_distress
  recommended_effect:
    - slow_down
    - ask_permission_before_probing
  expires_after_cycles: 2
```

### 4.5 Trace event

```yaml
trace_event:
  id: trace_event_144
  cycle: 6
  event_type: transformation_adopted
  actor: local_model_B
  surface_id: surface_2026_06_02_001
  transformation_type: reframing
  summary: shifted from assigned blackboards to fluid temporary surfaces
  downstream_effect:
    adopted_by_synthesis: true
    user_resonance: positive
    changed_routing: true
  durable_memory_candidate: true
```

## 5. Routing Logic

The router is the core of the deliberative MoE. It should route by state deficiency, not by fixed persona. The same participant may act as decomposer, critic, compressor, or novelty source depending on the current surface and observed profile.

### 5.1 Deficiency detection

| Detected deficiency | Likely transformation | Candidate participant |
|---|---|---|
| Under-constrained | Constraint check | Engineer-like local model, rules engine, implementation checker |
| Circular or stale | Novelty injection | Different local model, crowd model, frontier model |
| Emotionally flat | Affective salience | Reflective LLM, affect classifier, human |
| Internally inconsistent | Contradiction detection | Verifier model, symbolic checker, graph consistency routine |
| Too sprawling | Compression | Small local model, summarizer, trace compressor |
| Privacy-sensitive | Disclosure minimization | Privacy gate, local-only summarizer |
| High stakes and low confidence | Escalation decision | Spend manager, human, frontier model |
| Sub-coherent but interesting | Billboard preservation | Surface manager, human-visible trace selector |

### 5.2 Router decision record

```yaml
routing_decision:
  cycle: 8
  current_deficiency: local_saturation
  selected_mode: outside_critique
  selected_participant: frontier_model_minimal_payload
  target_surface: surface_design_spec
  disclosure_level: abstracted_no_personal_memory
  expected_value: high
  costs:
    money: medium
    latency: medium
    privacy: medium
    dependency: low
    style_contamination: low
  rationale:
    - local_models_disagree_after_two_cycles
    - confidence_remains_low
    - decision_affects_architecture
    - payload_can_be_abstracted
```

### 5.3 Pseudocode

```python
while not done:
    state = load_trace_and_active_surfaces()
    deficiencies = detect_state_deficiencies(state)
    candidate_moves = propose_moves(deficiencies, participant_profiles)
    move = select_move(candidate_moves, cost_model, orthogonality_bonus)

    result = call_participant(
        participant=move.participant,
        mode=move.mode,
        surface=move.target_surface,
        disclosure=move.disclosure_level
    )

    billboards = extract_billboards(result)
    adjudication = adjudicate(result, billboards, state)
    update_surfaces(adjudication)
    append_trace(move, result, adjudication)
    update_profiles_from_downstream_effects()

    if ready_for_user_response(state):
        break
```

## 6. Surface Management

Surfaces should not be assigned departments. They should condense, transform, and dissolve as needed. A surface is a temporary medium of coherence: a place where cognition leaves weather marks.

### 6.1 Surface lifecycle

1. **Condense:** the system detects that a particular representation would make the next transformation possible.
2. **Populate:** one or more participants add transformations, billboards, or artifacts.
3. **Protect:** the surface may be allowed to develop without premature reconciliation.
4. **Cross-influence:** other surfaces or participants may read billboards from it without fully translating it.
5. **Merge, archive, or dissolve:** the surface is incorporated into canonical state, preserved as a branch, or discarded.

### 6.2 Surface examples

- **Text schema:** useful for implementation plans, routing rules, and state definitions.
- **Graph patch:** useful for relationship edges, unresolved tensions, autobiographical knowledge graphs.
- **Image board:** useful for spatial metaphors, design language, emotional atmosphere.
- **Audio contour:** useful for pacing, tension, cadence, recurrence, and unresolved affect.
- **Embedding basin:** useful for memory clusters and thematic recurrence.
- **Timeline:** useful for autobiographical sequencing, development, and change over time.
- **Cost ledger:** useful for deciding whether to call frontier, cloud, human, or crowd contribution.

## 7. Billboards and Sub-Coherent Influence

A billboard is a perceptible perturbation, not necessarily a coherent message. It allows one participant to influence another without requiring shared ontology. This is essential for multimodal and non-LLM participants.

Billboards allow influence without shared ontology.

A participant may understand something sufficiently for it to alter its behavior, but insufficiently to coherently respond in the same language. The system should preserve that middle category instead of forcing either full translation or dismissal.

### 7.1 Billboard types

| Type | Example payload | Likely effect |
|---|---|---|
| **Affective** | arousal shift, hesitation, warmth, tension | Slow down, ask permission, preserve phrase, avoid closure |
| **Visual** | small figure, large structure, warm window, surrounding emptiness | Introduce shelter, scale, vulnerability, or spatial framing |
| **Audio** | returning motif, unresolved cadence, dissonance, silence | Preserve recurrence, resist premature synthesis, adjust rhythm |
| **Graph** | unresolved edge, contradictory relation, missing consent link | Do not collapse ambiguity; retrieve related memories |
| **Embedding** | theme cluster similarity, anomalous nearest neighbor | Bring prior theme back into active surface |
| **Crowd** | distribution of quick judgments across many small models | Estimate robustness, ambiguity, majority frame, minority insight |

## 8. Empirical Profiling Harness

The harness should become a living nervous system rather than a static benchmark. It should learn which participants supply which transformations under which conditions and in relation to which other participants.

> See also: [on-scores-and-harnesses.md](../essays/on-scores-and-harnesses.md) for trust mechanics and scoring philosophy.

### 8.1 Probe families

| Probe family | Description |
|---|---|
| **Neutral solo pass** | What does the participant do without role overlay? |
| **Role overlay pass** | What changes under an assigned lens such as architect, companion, critic, compressor? |
| **Role swap pass** | Does the difference follow the model or the role? |
| **Partnered braid pass** | What appears only after another participant bends the state? |
| **Surface variation pass** | Does the participant perform differently on text, schema, graph, image summary, or timeline surfaces? |
| **Downstream adoption pass** | Which contributions survive synthesis, user correction, or later implementation? |

### 8.2 Braid-induced tendency detection

```yaml
braid_induced_tendency_probe:
  prompt_family: architecture_design
  base_condition:
    participant_A: neutral_solo
    participant_B: neutral_solo
  braid_condition:
    sequence:
      - A proposes transformation
      - B reads A delta and posts counter-delta
      - A revises after B billboard
  measured_difference:
    new_capability_visible_only_in_braid: true
    contribution_type: reframing_after_constraint
    adopted_by_synthesis: true
  interpretation: participant_A becomes more useful after participant_B introduces meaning-pressure
```

## 9. Outside Contribution: Human, Frontier, Cloud, Crowd

Outside contribution should be treated as an explicit routing option with costs and payload constraints. The local braid should decide not only whether to call outside help, but what version of itself to expose.

> See also: [resonator-charter.md](../core/resonator-charter.md) for angel identity and ethical constraints on external exposure.

### 9.1 Escalation targets

| Target | Use when | Main costs | Payload strategy |
|---|---|---|---|
| **Human** | Frame ambiguity, values, consent, taste, lived meaning, personal correction | Attention, interruption, emotional burden | Ask the smallest useful question or present a concise choice |
| **Frontier model** | High-stakes reasoning, technical uncertainty, synthesis review, fresh external capability | Money, latency, privacy, dependency | Send abstracted design state; ask for critique or missing dimensions |
| **Cloud model** | Need a specific outside model or hosted capability | Privacy, dependency, latency | Minimize personal detail; separate prompt from memory |
| **Crowd model** | Need quick robustness poll, ambiguity estimate, or distribution of interpretations | Coordination, cost at scale, aggregation noise | Ask many small or cheap models one narrow question; aggregate distributions, not essays |
| **Different local model** | Need orthogonal local bend without privacy cost | VRAM, latency, orchestration | Route to known complementary contribution vector |

### 9.2 Crowd model pattern

A crowd model call asks many small or cheap models for a quick opinion on a narrow point. It is not primarily a way to get one better answer. It is a way to sample a field: disagreement, common readings, surprising minority frames, or ambiguity in the current surface.

```yaml
crowd_model_call:
  question: Which framing is most natural for this design problem?
  options:
    - routing_architecture
    - autobiographical_trust_system
    - multimodal_surface_manager
    - deliberative_moe
  sample_size: 100
  response_budget_per_model: 40_tokens
  collect:
    - selected_option
    - confidence
    - one_surprising_reason
  aggregate:
    majority_distribution: true
    minority_clusters: true
    representative_outliers: 5
  privacy_payload: abstracted_no_user_memory
```

### 9.3 Escalation rule, first version

```python
if local_models_disagree and confidence_low_after_cycles >= 2:
    if stakes_high or novelty_value_high or current_information_needed:
        run_privacy_gate()
        if payload_can_be_abstracted:
            consider_frontier_or_crowd_call()
        else:
            ask_human_or_continue_local()

if user_values_or_consent_are_unclear:
    ask_human_before_external_escalation()

if question_is_narrow_and_pollable:
    prefer_crowd_model_over_single_frontier_model()

if question_requires_deep_synthesis_or expertise:
    prefer_frontier_model_over_crowd_model()
```

## 10. Scoring and Learning

The system should learn from downstream effects rather than relying only on preassigned roles. Each transformation can be scored by adoption, correction, user resonance, implementation usefulness, novelty, and whether it changed the next routing decision.

> See also: [on-scores-and-harnesses.md](../essays/on-scores-and-harnesses.md) for the broader scoring philosophy.

### 10.1 Transformation score

```yaml
transformation_score:
  trace_event_id: trace_event_144
  participant: local_model_B
  transformation_type: reframing
  metrics:
    adopted_by_synthesis: 1.0
    user_resonance: 0.9
    later_revised: 0.1
    changed_next_action: 0.8
    novelty: 0.7
    orthogonality_to_prior_state: 0.85
    cost: 0.2
  composite_value: 0.78
```

### 10.2 Orthogonality matrix

```yaml
orthogonality_matrix:
  local_model_A__local_model_B:
    redundancy: 0.31
    productive_tension: 0.74
    synthesis_gain: 0.68
  local_model_A__embedding_retrieval:
    redundancy: 0.12
    synthesis_gain: 0.81
  local_model_B__affect_classifier:
    redundancy: 0.05
    synthesis_gain: 0.77
  local_model_pair__frontier_model:
    marginal_gain_after_two_cycles: 0.43
    privacy_cost: 0.61
```

## 11. Prototype Roadmap

### Phase 1 — Text-only local braid

- Two local LLMs.
- Manual or rule-based router.
- Text surfaces only.
- Structured artifacts: assumptions, deltas, weak points, next moves.
- Append-only trace in JSONL or SQLite.

### Phase 2 — Contribution-vector logging

- Add transformation labels and downstream adoption scoring.
- Run role-swap and neutral-profile probes.
- Track model-native, role-induced, task-specific, and braid-induced tendencies.
- Begin pairwise orthogonality matrix.

### Phase 3 — Adaptive routing by deficiency

- Detect under-constraint, circularity, inconsistency, privacy sensitivity, and low confidence.
- Route to participants based on expected transformation value.
- Add cost model for latency, VRAM pressure, privacy, and money.
- Introduce surface lifecycle: condense, populate, protect, merge, dissolve.

### Phase 4 — Non-LLM billboards

- Add retrieval or embedding clusters as billboard sources.
- Add graph consistency checks for knowledge graph work.
- Add simple affect or salience tags if sensor or interaction data is available.
- Allow billboards to influence routing without forcing full natural-language interpretation.

### Phase 5 — Outside contribution gates

- Add privacy-preserving payload builder.
- Add frontier/cloud escalation rules.
- Add crowd model polling for narrow ambiguity or robustness questions.
- Log whether outside contributions actually improved the braid.

## 12. First Implementation Slice

The first useful implementation should be deliberately small. It should prove that two local participants can produce useful nonredundant transformations and that the trace can preserve what changed.

> See also: [continuity-and-decision-lineage.md](../core/continuity-and-decision-lineage.md) for trace immutability requirements.

```yaml
minimum_viable_braid:
  participants:
    - local_model_A
    - local_model_B
    - trace_summarizer
  surfaces:
    - canonical_text_surface
    - optional_branch_surface
  cycle:
    1: user_prompt_to_surface
    2: A_posts_delta
    3: B_posts_delta_after_reading_A
    4: adjudicator_merges_or_preserves_tension
    5: trace_records_transformation
    6: synthesis_response_to_user
  logged_metrics:
    - transformation_type
    - adopted_by_synthesis
    - user_correction
    - novelty
    - orthogonality_estimate
    - cost
```

## 13. Open Research Questions

1. How can the router distinguish true orthogonality from superficial stylistic difference?
2. How can braid-induced tendencies be detected without overfitting to a small number of conversations?
3. What is the right representation for sub-coherent influence so that it can bend the braid without becoming noise?
4. When should a surface be protected from premature synthesis, and when should it be dissolved?
5. How should crowd model outputs be aggregated so that minority insights are not erased by majority polling?
6. How can privacy cost be quantified well enough to support routing decisions?
7. How can the system learn from human interruption without becoming overly dependent on explicit feedback?
8. What kinds of multimodal surfaces are most useful for autobiographical AI: timelines, images, audio contours, graph patches, or something else?
9. How can a local-first system remain porous to outside contribution without losing its ethical center?

## 14. Working Glossary

> See also: [glossary-and-ontology.md](../core/glossary-and-ontology.md) for canonical project glossary.

| Term | Working definition |
|---|---|
| **Braided deliberation** | A router-managed ecology in which participants apply distinct transformations to evolving shared or temporary state. |
| **Contribution vector** | The empirical profile of what a participant tends to bend, reveal, preserve, or distort. |
| **Braid-induced tendency** | A behavior or capability that appears only in interaction with other braid participants or surfaces. |
| **Surface** | A temporary medium of coherence where thought can happen in a form useful to one or more participants. |
| **Billboard** | A partial projection or signal that can influence another participant without requiring full shared ontology. |
| **Sub-coherent influence** | Influence that is legible enough to matter but not coherent enough for clean reciprocal dialogue. |
| **Deliberative MoE** | A mixture-of-experts architecture at the level of reasoning transformations rather than tokens. |
| **Crowd model** | A many-model outside contribution pattern used to sample quick judgments, ambiguity, or robustness across a field. |
| **Weather marks** | Traces left on surfaces by cognition: tension, salience, uncertainty, recurrence, confidence, cost pressure. |

## 15. Closing Design Principle

A braid participant is anything that can perceive state, apply a distinctive transformation, and expose the result on a mutually usable surface or billboard.

The system becomes intelligent not because every participant shares a mind, language, or chain of thought, but because the router learns which transformations are needed, which participants can supply them, which surfaces can host them, and which weather marks deserve to survive into the trace.

> *Call the expensive mind only when the local braid knows what it needs from it.*

---

*Cross-references: [Braided Deliberation Capture Memo](../essays/braided-deliberation.md) · [continuity-and-decision-lineage.md](../core/continuity-and-decision-lineage.md) · [resonator-charter.md](../core/resonator-charter.md) · [on-scores-and-harnesses.md](../essays/on-scores-and-harnesses.md) · [ephemeris-charter.md](../core/ephemeris-charter.md) · [glossary-and-ontology.md](../core/glossary-and-ontology.md)*
