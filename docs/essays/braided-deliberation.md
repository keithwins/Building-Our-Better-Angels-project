---
title: "Braided Deliberation"
subtitle: "Contribution Vectors, Fluid Surfaces, and Deliberative Mixture-of-Experts"
description: "A capture memo for a local cognitive ecology"
version: "0.1"
status: "Rough Draft v0.1"
---

# Braided Deliberation

**Contribution Vectors, Fluid Surfaces, and Deliberative Mixture-of-Experts**

*A capture memo for a local cognitive ecology*

> ⚠️ **ROUGH DRAFT — v0.1** — This document is an early capture memo, not a finished paper. Content is provisional and subject to significant revision.

---

> *The surface is not the cognition. It is where cognition leaves weather marks.*

> *The real unit is not persona. It is contribution vector.*

> *Do not make agents exchange thoughts. Make them exchange transformations of the shared problem state.*

---

## Status of This Memo

This document captures a developing architecture and vocabulary for braided deliberation: a multi-participant reasoning system in which local models, tools, humans, retrieval systems, sensors, and other processes influence a shared trajectory through visible transformations. It is intentionally a capture memo rather than a finished paper. Its job is to preserve the nuance while it is still alive, while also shaping enough of the material into a design direction that can guide implementation.

The memo avoids treating hidden chain-of-thought as the central object. Instead, it treats the durable and useful unit as the transformation a participant applies to a shared or temporary representational surface. Some of these transformations will be human-interpretable. Some may be machine-facing. Some may be sub-coherent: sufficiently legible to influence another participant, but not sufficiently legible to support a clean reply in the same language.

## Executive Orientation

Braided deliberation is not multi-agent chat. It is a router-managed ecology of participants creating, perturbing, merging, and dissolving temporary media of coherence.

The core unit is not a persona, role, or model name. The core unit is a contribution vector: the kind of transformation a participant tends to make possible.

The most valuable participant is often not the one that produces the best standalone answer, but the one that bends the problem along a dimension the others would have left flat.

The system should route by state need: what transformation is needed next, what surface should host it, who should perform it, and what costs are justified.

Billboards allow influence without shared ontology. A participant can post a signal that another participant cannot fully understand but can still be changed by.

A frontier model, cloud model, human, or crowd model should be summoned when the local braid knows what kind of outside contribution it needs and what it can safely expose.

A braid participant is anything that can perceive state, apply a distinctive transformation, and expose the result on a mutually usable surface or billboard.

## §1 Originating Intuition

The initial problem was simple but rich: two local models hosted on a constrained machine cannot literally speak to each other during hidden inference. Yet if the visible reasoning process is doing real work, then there may be an opportunity for models, tools, and humans to shape one another in real time by influencing what is remembered, foregrounded, tested, or reframed.

The goal is therefore not to merge private chains of thought. The goal is to create a system in which each participant can alter the trajectory of the shared problem state. The visible artifact is not a transcript of cognition. It is a record of consequential transformations.

The braid does not require a common mind. It requires mutually visible transformations.

User interruption is not an afterthought in this architecture. When a human corrects a premise, suggests a fruitful direction, resists a frame, or marks a phrase as alive, that intervention should mutate the state of the braid. It should not merely append to the chat. It should alter the active surface on which cognition is happening.

## §2 Braided Deliberation Trace

A braided deliberation trace is the durable record of the transformations that mattered. It may include claims, assumptions, disagreements, routing decisions, cost estimates, user interventions, model deltas, retrieved memories, confidence changes, and sub-coherent signals. It need not be fully interpretable; it may have human-facing, machine-facing, and opaque layers.

| Layer | Contents | Purpose |
|---|---|---|
| Human-interpretable trace | Claims, assumptions, tensions, metaphors, next questions, user corrections | Allows the human to participate, steer, preserve, object, and remember |
| Machine-readable trace | Embeddings, graph updates, retrieval signals, confidence scores, routing features | Allows tools and models to condition future moves without forcing prose translation |
| Sub-coherent trace | Signals that influence behavior without being fully shareable in a common ontology | Preserves useful perturbations that would be lost if only coherent claims were allowed |
| Private inference | Transient model-internal processing and opaque tool behavior | May do work without becoming part of the inspectable trace |

The trace therefore resembles a ledger of state changes more than a meeting transcript. It should answer: what changed, who or what changed it, why it mattered, whether the change survived synthesis, and how the change affected subsequent routing.

See also: [Continuity & Decision Lineage](../core/continuity-and-decision-lineage.md) for immutability and reflexivity in trace records.

## §3 Contribution Vector, Not Persona

The early architect-versus-reflective-companion pairing is useful as an initial myth. It creates different attractors: structure and feasibility on one side; salience, trust, and meaning on the other. But it should not be mistaken for the deeper mechanism. The mature system should discover empirical contribution vectors rather than merely assign roles.

Orthogonality beats plurality. Two agents are only better than one when the second bends the problem along a dimension the first would not have bent it.

A contribution vector describes the kind of transformation a participant tends to provide. Possible dimensions include:

- **Decomposition:** breaking a problem into usable parts.
- **Constraint sensitivity:** detecting feasibility, resource, privacy, or timing limits.
- **Contradiction detection:** identifying incompatible assumptions or claims.
- **Compression:** preserving what matters while reducing context load.
- **Novelty generation:** opening a direction not already present in the dominant frame.
- **Reframing:** changing the basis in which the problem is represented.
- **Affective salience:** noticing emotional charge, intimacy, trust, shame, or vulnerability.
- **User-intent preservation:** keeping the system aligned with the human's deeper drift rather than merely literal words.
- **Implementation specificity:** turning an idea into architecture, schema, tests, or code.
- **Epistemic humility:** marking uncertainty and asking for the right outside contribution.

```yaml
contribution_vector:
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
```

See also: [On Scores & Harnesses](on-scores-and-harnesses.md) for how scores and harnesses relate to contribution profiling and trust.

## §4 Empirical Profiles and the Magic Category

A model's apparent behavior is layered. Fine-tuning, instruction tuning, role prompts, task domain, context, partner model, temperature, and prior braid state can all alter what it contributes. This is not merely noise. It is a resource, provided the system profiles it explicitly.

| Profile layer | Question | Why it matters |
|---|---|---|
| Base tendency | What persists across roles, prompts, and partners? | Approximates model-native behavior. |
| Fine-tuned tendency | What appears because of instruction tuning, alignment, style training, or benchmark pressure? | Operationally real in deployment, even if not native. |
| Role-induced tendency | What appears only when a persona or lens is applied? | Measures how much the role overlay is doing. |
| Task-specific tendency | What appears only in code, memory, design, narrative, math, or ethics? | Supports routing by task type. |
| Braid-induced tendency | What appears only after interaction with another participant or surface? | The magic category: latent value revealed by ecology, not solo testing. |

A model's true role in the ecology is not what it says in isolation. It is how it changes the braid.

Fine-tuning is a bug if the aim is to discover a model's native character. It is a feature if the aim is deployed usefulness. It is an opportunity if the system treats tuning as one layer of a participant profile rather than as contamination. The question is not whether fine-tuning "defines" the model's answer. The question is whether its effects are stable, useful, measurable, and orthogonal to the other participants.

See also: [Resonator Charter](../core/resonator-charter.md) for how mirror and angel roles relate to profile layers.

## §5 Test Harness as Nervous System

The test harness should not be a static exam. It should behave more like a nervous system or immune system: continuously sensing deficiencies in the current state, routing transformations, learning which participants help under which conditions, and updating profiles from downstream effects.

| Probe | Purpose |
|---|---|
| Neutral solo pass | Establish baseline tendencies without role overlays. |
| Role overlay pass | Measure what changes when a model is asked to operate through a lens. |
| Role-swap pass | Distinguish model-native differences from persona-induced differences. |
| Partnered braid pass | Detect braid-induced tendencies that appear only in relation. |
| Surface variation pass | Test whether text, graph, image, audio, or timeline surfaces reveal different strengths. |
| Downstream adoption scoring | Track whether contributions survive synthesis, reduce uncertainty, or receive positive user signal. |

```yaml
profile_update:
  participant: local_model_A
  context:
    task_type: conceptual_architecture
    surface: text_schema
    role_overlay: none
    partner: local_model_B
  observed_contribution:
    - implementation_constraint
    - schema_formalization
  downstream_effect:
    adopted_by_synthesis: true
    user_positive_signal: true
    later_revised: false
  profile_delta:
    constraint_sensitivity: +0.03
    schema_usefulness: +0.04
```

See also: [On Scores & Harnesses](on-scores-and-harnesses.md) for the broader harness philosophy and scoring framework.

## §6 Deliberative Mixture-of-Experts

The mixture-of-experts analogy becomes precise when lifted one level up. Token-level MoE routes the next token or hidden representation to an expert. Braided deliberation routes the next transformation of an evolving state to a participant.

Token-level MoE routes the next token. Deliberative MoE routes the next transformation.

| Token-level MoE | Deliberative MoE |
|---|---|
| Input token or hidden state | Shared deliberative state or temporary surface |
| Router chooses neural expert | Router chooses participant, mode, surface, budget, and disclosure |
| Expert transforms representation | Participant transforms state, posts a billboard, or changes a surface |
| Outputs are combined | Adjudicator merges, branches, preserves tension, or dissolves a surface |
| Training signal from prediction loss | Training signal from adoption, user resonance, uncertainty reduction, cost, and later correction |

The router should route by deficiency: what is missing or fragile in the current braid?

- Under-constrained state → route to implementation checker or constraint-sensitive model.
- Tone-deaf state → route to affect-sensitive model or human-facing companion process.
- Internal inconsistency → route to contradiction detector.
- Circular or stale state → route to novelty generator, crowd model, or frontier model.
- Privacy-sensitive state → route to privacy gate before any external call.
- High uncertainty after local saturation → route to human, frontier model, or crowd model.

## §7 Temporary Media of Coherence

The word blackboard is useful but too rigid if it becomes an org chart. A better primitive is the surface: a temporary medium of coherence that appears where thought needs a place to happen. Surfaces are created because they are useful in the moment, not because the system has preassigned departments.

The system should condense temporary surfaces wherever thought needs a place to happen.

The surface is not the cognition. It is where cognition leaves weather marks.

A surface may be text, but it may also be multimodal or machine-native:

- A **paragraph surface** for explicit claims and tensions.
- A **graph patch** for relationships among memories, people, motifs, or unresolved contradictions.
- An **image surface** for spatial metaphor, composition, color, or scale.
- An **audio contour** for rhythm, silence, tension, recurrence, dissonance, or release.
- A **timeline** for developmental or autobiographical structure.
- An **embedding basin** for thematic recurrence and similarity.
- An **affective trace** for salience, arousal, pacing, or vulnerability.
- A **budget surface** for money, latency, privacy, dependency, and cognitive disruption costs.

Surfaces can be spawned, shaped, merged, ignored, forked, transformed, or dissolved. They are not the cognition itself. They are where one or more cognitive processes leave marks that other processes may respond to.

## §8 Billboards and Sub-Coherent Influence

A billboard is a partial projection from one participant or surface into another participant's perceptual range. It need not be fully coherent. It may influence another participant without allowing that participant to respond in kind. This is the core of sub-coherent influence.

Billboards allow influence without shared ontology.

A participant may understand something sufficiently for it to alter behavior, but insufficiently to coherently answer it.

| Source | Billboard signal | Possible influence |
|---|---|---|
| Affect classifier | Arousal increased sharply; confidence 0.72 | Slow down; ask permission before probing; preserve emotional salience. |
| Image model | Small figure near large structure; warm light from one window | Treat themes of shelter, scale, and vulnerability as live. |
| Audio model | Slow build; unresolved cadence; recurring motif | Do not force closure; preserve recurrence as meaningful. |
| Embedding clusterer | High similarity to trust-through-locality cluster | Bring privacy/locality back into the frame. |
| Graph traversal | Unresolved dual-valence edge around admiration and resentment | Do not collapse contradictory memories into a single sentiment. |
| Human interruption | "No, not debate — mutual illumination." | Mutate the active frame and reroute future moves. |

```yaml
billboard:
  source: audio_contour_model
  coherence_level: partial
  medium: audio
  signal:
    - slow_build
    - unresolved_cadence
    - returning_motif
    - warm_but_unstable
  recommended_effect:
    - respond_with_patience
    - do_not_force_closure
    - preserve_recurrence_as_meaningful
```

## §9 Weather Systems, Not Committee

Committee language suggests departments, assigned roles, minutes, votes, and tidy reconciliation. The better metaphor is weather: gradients, pressure, turbulence, condensation, dissipation, fronts, and interacting systems. A braided system should not merely pass memos. It should allow state pressures to create temporary surfaces and route transformations.

| Weather term | Deliberative analogue |
|---|---|
| Pressure | Constraint, cost, or unresolved tension pressing on the state |
| Humidity | Latent material available for condensation: memories, motifs, partial signals |
| Condensation | Formation of a temporary surface where thought can happen |
| Front | Collision of incompatible frames or participant tendencies |
| Turbulence | High novelty, instability, or unresolved contradiction |
| Dissipation | Surface loses usefulness and can be dissolved or compressed |
| Climate | Long-term profile of participant tendencies and user preferences |

This metaphor matters because it discourages premature bureaucracy. The router should not ask which department owns a problem. It should ask what conditions are forming and what surface or participant can productively respond.

## §10 Outside Contribution: Frontier, Human, Crowd

The local braid should be able to determine when outside contribution is worth the cost. Outside contribution may come from a frontier model, a cloud model, a human, a specialized tool, or a crowd model: a large number of small or diverse models asked for quick opinions on a bounded point.

Call the expensive mind only when the local braid knows what it needs from it.

The crowd model idea is especially interesting as a poll of model-space rather than a single authority. A hundred or thousand lightweight opinions might reveal distributional uncertainty, hidden ambiguity, consensus, or surprising minority frames. It should not replace deliberation, but it can post a statistical billboard into the braid.

| Outside source | Best use | Risk |
|---|---|---|
| Frontier model | Deep critique, synthesis, hard reasoning, current-world competence | Money, privacy, dependency, style contamination |
| Cloud model | Capability beyond local hardware or specialized modality | Privacy, latency, external dependency |
| Human | Value judgment, lived intent, consent, taste, priorities | Interruption burden, emotional cost, availability |
| Crowd model | Fast distributional pulse over many cheap or diverse models | Shallow responses, herd effects, noise, governance complexity |
| Specialized tool | Precise retrieval, graph traversal, verification, classification | Narrow ontology, brittle signal, over-trust |

```yaml
escalation_decision:
  triggers:
    - local_models_disagree
    - confidence_low_after_two_braid_cycles
    - high_stakes
    - high_expected_novelty
    - current_world_knowledge_needed
  costs:
    money: medium
    latency: medium
    privacy: high
    dependency: medium
    style_contamination: low
  mitigation:
    - summarize_locally_before_sending
    - strip_personal_memory
    - send_abstract_design_problem_only
    - ask_for_critique_not_final_answer
  decision:
    target: frontier_model
    payload_scope: minimal_abstracted_braid_state
```

```yaml
crowd_model_poll:
  question: "Which missing dimension is most likely to break this design?"
  participants: 256 small_or_diverse_models
  response_budget: 40_tokens_each
  aggregation:
    - cluster_responses
    - identify_consensus
    - preserve_interesting_minorities
    - post_distributional_billboard
  output_billboard:
    consensus: "privacy boundary needs sharper treatment"
    minority_signal: "musical/audial surfaces may be first-class, not decorative"
    uncertainty: high
```

See also: [Ephemeris Charter](../core/ephemeris-charter.md) for coordination patterns and scoring across participants.

## §11 Practical Architecture Sketch

A minimal architecture can be described as a set of primitives and loops rather than fixed agents.

| Primitive | Function |
|---|---|
| Participant | Anything that can perceive, transform, generate, classify, retrieve, or judge. |
| Surface | Temporary medium of coherence where transformations can leave marks. |
| Billboard | Partial projection that allows influence across incompatible or partial ontologies. |
| Router | Chooses participant, mode, surface, budget, and disclosure. |
| Adjudicator | Merges, branches, preserves tension, or dissolves surfaces. |
| Trace | Durable record of consequential transformations and routing decisions. |
| Profile store | Empirical memory of participant contribution vectors and relational orthogonality. |
| Spend manager | Evaluates money, latency, privacy, dependency, style, and disruption costs. |

```python
while braid_active:
    state = observe_canonical_state()
    surfaces = observe_active_surfaces()
    billboards = collect_recent_billboards()

    deficiency = diagnose_state_need(state, surfaces, billboards)

    route = router.choose(
        needed_transformation=deficiency,
        participant_profiles=profiles,
        available_surfaces=surfaces,
        cost_constraints=spend_manager.current_policy,
        privacy_constraints=privacy_gate.current_policy
    )

    contribution = participant_act(route)

    adjudication = adjudicator.integrate(
        contribution=contribution,
        target_surface=route.surface,
        canonical_state=state
    )

    trace.record(route, contribution, adjudication)
    profiles.update_from_downstream_effects(trace)
    dissolve_or_condense_surfaces_if_needed()
```

## §12 Prototype Plan

1. **Text-only two-model braid.** Run two local models over the same prompt. Require each to emit a public artifact: assumptions, deltas, weakest point, novelty claim, and suggested next transformation.

2. **Contribution-vector logging.** Manually or semi-automatically score each artifact for decomposition, constraint sensitivity, novelty, reframing, user-intent preservation, and implementation specificity.

3. **Role-swap harness.** Run neutral, architect/companion, companion/architect, and randomized lens tests to separate model-native from role-induced tendencies.

4. **Adaptive router.** Replace fixed turn-taking with state-deficiency routing: ask what the braid needs next and route accordingly.

5. **Fluid surfaces.** Add non-text surfaces: graph patches, timelines, image boards, affect traces, and embedding basins.

6. **Billboard integration.** Allow non-LLM systems to post partial signals that can influence LLM behavior without requiring full translation.

7. **Outside contribution manager.** Implement escalation rules for frontier, human, cloud, and crowd model calls, with privacy-preserving payload construction.

8. **Long-term profile store.** Track braid-induced tendencies, pairwise orthogonality, branch fitness, and user resonance across sessions.

## §13 Open Questions

- How should contribution vectors be scored without collapsing into arbitrary human taste?
- Which signals best predict that a local braid is saturated and needs outside contribution?
- How can the system preserve sub-coherent influence without hallucinating meaning into every signal?
- When should a surface be dissolved, compressed, promoted, or preserved as a recurring touchstone?
- How can the router avoid expert collapse, where one strong model or frontier model dominates too many moves?
- What is the right balance between privacy-preserving abstraction and useful outside consultation?
- Can crowd model polls detect useful minority frames, or do they mostly amplify shallow consensus?
- What kinds of non-LLM participants contribute the most orthogonal transformations?
- How does a human safely participate in live state mutation without being overburdened?
- Can braid-induced tendencies be robust across changing model sets, or are they always relation-specific?

See also: [Glossary & Ontology](../core/glossary-and-ontology.md) for canonical definitions of terms used throughout.

## §14 Working Vocabulary

| Term | Working definition |
|---|---|
| Braided deliberation | A multi-participant reasoning process in which distinct transformations shape an evolving shared trajectory. |
| Braided deliberation trace | The durable record of consequential transformations across participants, surfaces, billboards, and routing decisions. |
| Contribution vector | The empirical profile of what kind of transformation a participant tends to provide. |
| Braid-induced tendency | A behavior or contribution that appears only in ecological interaction, not in solo testing. |
| Temporary medium of coherence | A surface that forms because thought needs somewhere to happen. |
| Surface | A representational medium where participants leave marks: text, graph, image, audio, timeline, embedding field, or affect trace. |
| Billboard | A partial projection that allows influence across different or incompatible ontologies. |
| Sub-coherent influence | Influence that is useful even though it is not fully coherent, translated, or reciprocally answerable. |
| Deliberative MoE | A mixture-of-experts architecture lifted into deliberation space: route transformations, not tokens. |
| Crowd model | A large pool of models queried briefly to produce a distributional signal or poll-like billboard. |
| Weather marks | The visible or machine-readable traces left by cognition on a temporary surface. |

See also: [Glossary & Ontology](../core/glossary-and-ontology.md) for the project-wide canonical vocabulary.

## §15 Closing Formulation

Braided deliberation begins as a way for two local models to inform each other without sharing hidden chains of thought. It becomes something larger: a local cognitive ecology in which many kinds of participants create temporary media of coherence, post billboards across partial ontologies, and route scarce attention toward the transformations most needed by the current state.

The braid is not the sum of its outputs. The braid is the evolving pattern of transformations that survive contact with one another.

The design challenge is not to make every participant speak the same language. The challenge is to let them leave marks where others can be changed by them. Some marks will be sentences. Some will be graph edges. Some will be contours, clusters, costs, tensions, or pulses of salience. The art is in deciding which marks matter, when to preserve them, when to dissolve them, when to ask the human, and when to call the expensive mind.

*What can this participant bend that the others leave flat?*

---

*Cross-references: [Continuity & Decision Lineage](../core/continuity-and-decision-lineage.md) · [Resonator Charter](../core/resonator-charter.md) · [On Scores & Harnesses](on-scores-and-harnesses.md) · [Ephemeris Charter](../core/ephemeris-charter.md) · [Glossary & Ontology](../core/glossary-and-ontology.md)*
