# Relational Spatiotemporal Acoustic Odometry (RSAO)
*Project Specification, v0.1 — June 29, 2026*
*Parent project: Understory Steward*

---

## 1. Project identity

*   **Working name:** Relational Spatiotemporal Acoustic Odometry
*   **Abbreviation:** RSAO
*   **Parent project:** Understory Steward
*   **Primary artifact:** An **Acoustic Scene Record**: a confidence-bearing account of persistent sound-producing entities and their changing relations across time.

RSAO is a research and engineering effort to infer an evolving acoustic field from several microphones carried by people moving through the world together.

It is not fundamentally a diarization project, a source-separation project, a localization project, or a recording project, though it contains all of those as partial capabilities.

Its central aim is to answer a larger question:
> *What persistent sound-producing entities are present in this field; where are they relative to the moving listeners; how do their trajectories, directivity, acoustics, and identities cohere through time?*

A “speaker diarization” answer such as “Keith spoke from 14:23:11 to 14:23:18” should emerge as one small projection of the larger field model.

---

## 2. Central proposition

A small distributed microphone constellation may support a qualitatively richer form of acoustic understanding than conventional diarization.

The proposed capture arrangement is initially:
*   two microphones associated with person A, separated across a reasonably stable local body frame;
*   two microphones associated with person B, similarly separated;
*   optionally, one additional microphone or stereo node placed on a fixed local surface during a walk, conversation, work session, or repeated place-based activity.

The microphones do not merely capture “individual channels.” They sample substantially the same acoustic world from different moving points. This creates overlapping evidence about:
*   source identity;
*   source activity;
*   source direction;
*   relative distance;
*   body orientation;
*   movement;
*   conversational relation;
*   environmental sound;
*   recurrence;
*   clock relationship;
*   acoustic transfer through the setting.

The intended system treats these relationships as a joint inference problem. It does not first “synchronize the files,” then separately “do diarization,” then separately “localize sources.”

Instead, it infers a changing relational model in which:
*   microphones move;
*   bodies move;
*   sources move or remain fixed;
*   local clocks have unknown relationships;
*   direct sound competes with reflections and noise;
*   sound-producing entities persist, disappear, reappear, overlap, and change character;
*   later evidence may revise earlier interpretation.

---

## 3. Why this is not merely diarization

Conventional diarization generally asks:
> *Who spoke when?*

It commonly relies on speech detection, speaker embeddings, segmentation, and clustering. This is useful, but narrow. It often struggles when voices overlap, change orientation, move through wind or reverberation, become partially obscured, or lack long clean segments.

RSAO begins from a different premise:
> *A voice is one persistent acoustic entity among many, whose identity is supported by spatial, temporal, spectral, embodied, and relational continuity.*

For a vocal entity, the system may use:
*   vocal timbre and learned speaker identity;
*   near-field capture on the speaker’s own body-associated microphones;
*   remote arrival at the other person’s microphones;
*   inter-channel delay;
*   cross-channel coherence;
*   spectral filtering caused by orientation and body position;
*   changing level ratios;
*   source continuity across time;
*   compatibility with inferred body trajectories;
*   compatibility with other sources in the field.

This creates a broader and more redundant basis for source continuity than ordinary diarization.

Diarization is therefore an output query:
> *Which persistent vocal entities were active at which times?*

Other output queries may include:
*   What non-vocal sound entities were present?
*   Which sounds were attached to which bodies?
*   Which sounds remained fixed in the environment?
*   Which sounds moved through the field?
*   When did the two people move from side-by-side to face-to-face?
*   When did an external event interrupt or redirect the social field?
*   Which acoustic entities recur across walks or sessions?
*   What evidence supports a particular attribution, and what remains uncertain?

---

## 4. Conceptual model

### 4.1 The acoustic field
The system models a session as an evolving acoustic field containing:
*   microphones;
*   bodies;
*   clocks;
*   sources;
*   paths;
*   direct sound;
*   reflections;
*   diffuse sound;
*   environmental acoustics;
*   uncertainty.

The system should not assume that the world is known in advance. It should infer only what the evidence supports.

The core object is not an absolute map. The core object is a network of changing relations.

### 4.2 Gauge freedom
The system will necessarily choose convenient coordinate conventions for display and computation, such as:
*   one microphone as the initial origin;
*   one body frame as a temporary reference;
*   one recording timeline as a display axis;
*   an arbitrary initial heading.

These conventions are not discoveries about the world. They are chosen gauges.

The important claims are relational invariants:
*   the two walkers moved closer or farther apart;
*   one person was likely ahead-left of the other;
*   both bodies reoriented toward a particular sound;
*   a source remained stationary relative to the local environment;
*   a source remained attached to a person;
*   a sound was likely external rather than body-associated.

The system must distinguish clearly among:
1.  **directly observed evidence:** Four waveforms, onset timing, channel coherence, signal energy, spectral content.
2.  **inferred relations:** Relative bearing, likely distance range, body relation, source persistence, source trajectory.
3.  **chosen display conventions:** Coordinate origins, headings, reference timelines.
4.  **unresolved ambiguity:** Alternative geometries, uncertain source identity, reflection-versus-direct-path confusion, insufficient evidence.

This distinction is essential to Understory’s broader commitment to trustworthy memory and sensemaking.

---

## 5. Core research question

Can a moving, distributed microphone constellation infer a persistent, uncertainty-bearing inventory of acoustic entities—voices, bodies, objects, animals, environmental sources—and their changing relations, such that diarization, source separation, localization, transcription, and contextual interpretation become different surfaces of one underlying Acoustic Scene Record?

A successful answer need not produce perfect 3D coordinates. It needs to demonstrate that the joint model can recover useful relational structure more reliably, more rapidly, and more intelligibly than conventional diarization alone.

---

## 6. Primary goals

### 6.1 Entity persistence
Maintain candidate acoustic entities through time. An entity may be:
*   Keith’s voice;
*   another participant’s voice;
*   a dog;
*   a bird;
*   a vehicle;
*   a creek;
*   footsteps;
*   a tool;
*   a generator;
*   wind in trees;
*   a distant conversation;
*   a recurring room or site sound;
*   a diffuse acoustic field.

The system should permit uncertainty, splitting, merging, disappearance, and reappearance. It should not prematurely force every sound into a fixed label.

### 6.2 Relational source tracking
Estimate, where evidence allows:
*   whether a source is body-associated, environmental, or external;
*   source bearing relative to each body;
*   approximate change in distance;
*   source motion or stationarity;
*   relation to the two moving body frames;
*   source continuity across overlap and interruption.

### 6.3 Joint temporal inference
Treat clock relationship as part of the inferred state of the system.

The system should estimate a smooth, revisable relation among recorder timelines while preserving physical timing effects that may represent actual changing range or motion.

It should not blindly warp recordings into maximum correlation, because doing so could erase evidence of approach, separation, orientation change, or relative pace.

### 6.4 Better-than-diarization source understanding
The system should aim to outperform ordinary diarization in situations that are difficult for it:
*   overlapping speech;
*   shifting physical orientation;
*   walking or movement;
*   changing distance;
*   noisy outdoor environments;
*   interrupted speech;
*   partial vocal occlusion;
*   multi-person interaction;
*   environmental sounds that matter to interpretation.

### 6.5 Evidence-preserving sensemaking
The system should preserve raw audio and retain provenance for all inferences.

A later user or agent should be able to ask:
*   What did the model infer?
*   What evidence supported this inference?
*   What competing interpretations existed?
*   How confident was the system?
*   What changed after later evidence was incorporated?

---

## 7. Explicit non-goals for the first project phase

The first phase does **not** require:
*   a full virtual-reality acoustic playback system;
*   Gaussian-splat or visual scene reconstruction;
*   video capture;
*   photogrammetry;
*   perfect absolute 3D localization;
*   real-time operation;
*   laboratory-grade survey accuracy;
*   universal sound-event recognition;
*   complete environmental reconstruction;
*   a polished consumer product.

Playback, visual reconstruction, and generalized novel-view audio may become useful later surfaces. They are not central to the first research target.

The first target is a durable, evidence-rich Acoustic Scene Record.

---

## 8. Capture architecture

### 8.1 Minimum viable constellation
The first serious configuration should contain four independent microphone channels:
*   person A, left-side microphone;
*   person A, right-side microphone;
*   person B, left-side microphone;
*   person B, right-side microphone.

The two microphones associated with each person should be separated by a meaningful baseline, preferably approximately shoulder-width or otherwise fixed across a body-associated frame.

Potential mounting locations include:
*   shoulder straps;
*   backpack straps;
*   collar yokes;
*   a light chest harness;
*   a structured garment with stable left/right mounting;
*   a hat, though shoulder/body placement may create more useful body-relative geometry for the initial experiments.

The important requirement is not perfection. It is repeatable geometry and limited fabric-induced wandering.

### 8.2 Optional local reference node
For a local walk, porch conversation, workshop session, garden activity, trail segment, or repeated place-based encounter, add one fixed microphone or stereo node.

The fixed node may be placed on:
*   a porch rail;
*   a table;
*   a trailhead marker;
*   a garden gate;
*   a workshop bench;
*   a kiln area;
*   a tree or stake;
*   another stable local surface.

This node is valuable because it introduces a partial bridge from the moving social relation into the surrounding place. It may help distinguish:
*   change in relation between the two people;
*   change in relation between the pair and the setting;
*   stationary environmental sources;
*   returning trajectories;
*   repeated events at the same site.

### 8.3 Recording rules
Recordings should preserve the original evidence.

Initial requirements:
*   raw PCM or WAV;
*   no Bluetooth audio path if avoidable;
*   no destructive mixing;
*   no automatic gain control where it can be disabled;
*   no voice enhancement;
*   no noise suppression;
*   no beamforming;
*   no channel mixing;
*   no mono conversion;
*   no lossy compression for primary archive;
*   continuous recording without pause/restart;
*   all channels retained independently.

A 48 kHz sample rate is a sufficient initial target. It preserves useful sub-millisecond timing information while remaining practical for long captures and GPU processing.

Higher sample rates may be explored later, but should not delay the first prototype.

### 8.4 Synchronization events
A sharp shared event at the beginning and end of a session remains useful:
*   a handclap;
*   a pair of hard taps;
*   an audible chirp;
*   another broadband transient.

These are not “the synchronization solution.” They are strong observations in a larger acoustic inference problem.

The system should also make use of naturally occurring shared evidence:
*   speech;
*   laughter;
*   coughs;
*   footsteps;
*   taps;
*   sticks breaking;
*   door latches;
*   bird calls;
*   vehicle transients;
*   dog barks;
*   tools;
*   moving environmental sounds;
*   sustained environmental sources.

---

## 9. Mathematical framing

Let the physical world evolve in hidden time $t$.

Each recording device maintains its own local sample-time coordinate:
$$a = C_A(t)$$
$$b = C_B(t)$$

The functions $C_A$ and $C_B$ represent local clock behavior. Their relationship is not assumed to be fixed or perfectly known.

Each microphone has a body-relative placement, and each body has a changing pose through time.

For microphone $m$, source $k$, and source signal $s_k$, the observed microphone waveform can be modeled approximately as:
$$y_m(t) = \sum_k [h_{m,k}(t) * s_k(t)] + n_m(t)$$

where:
*   $y_m(t)$ is the observed signal at microphone $m$;
*   $s_k(t)$ is a latent source stream for entity $k$;
*   $h_{m,k}(t)$ is a time-varying transfer function from source $k$ to microphone $m$;
*   $n_m(t)$ represents noise, residual reflections, wind, clothing noise, and model mismatch.

The transfer function $h_{m,k}(t)$ is not merely nuisance. It contains evidence about:
*   delay;
*   relative range;
*   bearing;
*   orientation;
*   directivity;
*   body shadowing;
*   local reflection;
*   source motion;
*   microphone motion.

The project seeks a joint posterior or optimization over:
$$P(\text{clock relations, body trajectories, microphone geometry, source streams, entity identities, source trajectories, acoustics})$$

The system should operate as a retrospective smoother whenever possible: later evidence may revise earlier estimates.

---

## 10. The Acoustic Scene Record

The primary output of a session should be an Acoustic Scene Record, not merely a transcript and not merely a set of separated WAV files.

An Acoustic Scene Record should contain:

### 10.1 Evidence layer
*   original multichannel audio;
*   device and channel metadata;
*   timestamps;
*   known capture topology;
*   microphone placement notes;
*   optional IMU or motion metadata;
*   detected acoustic primitives;
*   onset and coherence measurements;
*   raw correlation and likelihood traces where useful.

### 10.2 Entity layer
For every candidate acoustic entity:
*   unique identifier;
*   provisional type or class;
*   source activity intervals;
*   source stream estimate where available;
*   identity hypothesis;
*   confidence;
*   persistence history;
*   merge/split history;
*   evidence links;
*   relation to one or more body frames;
*   estimated trajectory or spatial support.

### 10.3 Relational layer
*   inferred local clock relation;
*   body-relative bearing estimates;
*   source-to-body relation;
*   side-by-side, facing, trailing, converging, separating, or stationary hypotheses;
*   estimated distance bands;
*   transition points;
*   confidence traces;
*   environmental source relations.

### 10.4 Semantic layer
Only after the acoustic field is established:
*   transcripts;
*   diarization labels;
*   named participants;
*   sound-event labels;
*   conversational turns;
*   interruptions;
*   thematic segments;
*   possible attention shifts;
*   later human or agent annotations.

### 10.5 Provenance and uncertainty layer
Every meaningful output should retain:
*   source evidence;
*   model version;
*   confidence;
*   alternatives considered;
*   whether a claim is observed, inferred, or user-annotated;
*   whether later evidence altered the estimate.

---

## 11. Inference architecture

The project should begin as a hybrid system rather than a single end-to-end neural model.

### 11.1 Acoustic primitive extraction
Detect and represent:
*   transients;
*   voiced intervals;
*   tonal sounds;
*   sustained noise sources;
*   broad diffuse noise;
*   likely direct-path arrivals;
*   reflections;
*   local handling and clothing noise;
*   silence and low-evidence intervals.

The system should preserve likelihood surfaces rather than reducing everything immediately to hard labels.

### 11.2 Local pair modeling
For each person’s local stereo pair:
*   estimate stable channel relationship;
*   detect body-associated near-field sources;
*   distinguish near voice from remote voice where possible;
*   estimate local left/right relations;
*   track microphone-specific artifacts;
*   identify body-associated sounds such as breathing, contact, clothing, and footsteps.

### 11.3 Cross-array association
For all channels, estimate whether acoustic fragments may arise from the same underlying source. Use evidence including:
*   time delay;
*   local time stretch;
*   cross-correlation;
*   phase coherence;
*   spectral similarity;
*   level relation;
*   transfer-function similarity;
*   temporal continuity;
*   source-motion compatibility;
*   body-association compatibility.

### 11.4 Entity management
Create, maintain, split, merge, and retire candidate entities.

The system must support ambiguity. It should allow:
*   “possibly the same bird as earlier”;
*   “two overlapping voice hypotheses remain unresolved”;
*   “this source may be a reflection of entity E3 rather than a new source”;
*   “this sound is likely body-associated but not confidently assigned.”

### 11.5 Joint relational odometry
Infer jointly:
*   relative device-clock behavior;
*   microphone-channel delays;
*   source arrivals;
*   body-relative geometry;
*   source trajectories;
*   source/body associations;
*   uncertainty.

This stage must not force a master timeline. It should infer a relation among local time coordinates.

### 11.6 Separation and enhancement
Use the inferred scene to improve source separation.

Do not treat separation as a front-end cleanup step that destroys evidence. Instead:
1.  infer an initial field;
2.  derive source hypotheses;
3.  use them to improve separation;
4.  feed cleaner source estimates back into entity tracking and relational inference;
5.  iterate.

### 11.7 Semantic interpretation
Only after the acoustic field has reached a useful degree of coherence should the system apply:
*   speech recognition;
*   speaker naming;
*   sound-event classification;
*   conversation analysis;
*   summary;
*   reflective commentary;
*   later BOBA sensemaking processes.

---

## 12. Minimum Viable Experiment

### 12.1 Purpose
The first experiment should not attempt to reconstruct an entire world. It should test whether four body-associated microphone channels, plus optionally one fixed local node, produce a meaningfully stronger entity and relation model than ordinary diarization.

### 12.2 Proposed session
A 20–40 minute local walk or site-based conversation involving two people.

Capture conditions:
*   person A wears a stable stereo microphone pair;
*   person B wears a stable stereo microphone pair;
*   all four channels record continuously;
*   one sharp shared event occurs at the beginning;
*   one sharp shared event occurs at the end;
*   optional fixed microphone is placed at a meaningful site;
*   participants naturally walk, pause, turn, stand beside one another, face one another, and encounter ordinary environmental sound.

A short intentional prelude may be useful:
*   each person speaks while standing in several relative positions;
*   the pair briefly walk side-by-side;
*   the pair briefly face one another;
*   one person moves ahead and returns;
*   one external sound or deliberate sound is made from a known local position.

This is not a calibration ritual intended to replace natural capture. It is a small supply of known constraints against which the system can be checked.

### 12.3 First success criteria
The first prototype succeeds if it can demonstrate several of the following with evidence:
*   identify which participant is speaking, including some overlapping or degraded moments;
*   retain voice identity through orientation and distance changes;
*   identify major non-vocal entities;
*   distinguish near-body and remote-source sound;
*   infer broad relative relation classes such as side-by-side, facing, trailing, or converging;
*   infer a coherent, smooth inter-recorder time relation;
*   identify some recurring environmental sound sources;
*   outperform a baseline diarizer on the session’s difficult segments;
*   produce a human-inspectable Acoustic Scene Record with confidence and provenance.

The first experiment does not need precise meter-scale position estimates.

---

## 13. Evaluation strategy

Evaluation should compare the system against both ordinary diarization and direct human observation.

### 13.1 Diarization comparison
Measure:
*   speaker attribution accuracy;
*   overlap handling;
*   missed speech;
*   false speaker splits;
*   false merges;
*   recovery after movement or orientation change;
*   robustness to environmental interference.

### 13.2 Entity persistence comparison
Measure whether the system can correctly maintain entities through:
*   temporary silence;
*   movement;
*   overlap;
*   changing orientation;
*   partial occlusion;
*   environmental masking;
*   re-entry.

### 13.3 Relational classification
Use manually annotated intervals to test:
*   side-by-side;
*   face-to-face;
*   one person ahead;
*   one person behind;
*   stationary conversation;
*   movement together;
*   convergence;
*   separation;
*   shared orientation toward an external event.

### 13.4 Clock-relation evaluation
Use beginning/end events and deliberately inserted intermediate events to measure:
*   inferred relative timeline stability;
*   local drift estimate;
*   residual alignment error;
*   uncertainty calibration;
*   performance during low-evidence intervals.

### 13.5 Human usefulness
The most important question is not only numerical accuracy. A useful evaluation asks whether the record enables a person to recover meaningful context that conventional transcript-plus-diarization misses.

Examples:
*   Can a human identify when a conversation shifted from casual walking to shared observation?
*   Can an external sound be distinguished as a recurring environmental source rather than a speech artifact?
*   Can a difficult overlap be resolved more convincingly?
*   Can a later reviewer understand why the system made a source attribution?
*   Can the record preserve the relation between people and their setting more faithfully?

---

## 14. Hardware and compute assumptions

### 14.1 Capture hardware
Initial capture should prioritize:
*   raw multichannel recording;
*   stable channel identity;
*   low noise;
*   continuous recording;
*   known channel ordering;
*   repeatable microphone placement;
*   wind protection;
*   minimal clothing rub;
*   local storage sufficient for lossless audio.

A single shared multichannel recorder would simplify some timing questions, but two stereo recorders or phones remain useful research configurations because the project explicitly studies distributed local time systems.

### 14.2 GPU compute
The RTX 5070 Ti with 16 GB VRAM should be adequate for substantial offline prototype work, including:
*   multichannel STFT analysis;
*   dense cross-correlation;
*   generalized cross-correlation with phase transform;
*   batched source-embedding extraction;
*   sound-event classification;
*   multichannel source separation;
*   iterative optimization;
*   factor-graph or differentiable scene estimation;
*   multiple repeated inference passes across a session.

The first system should favor offline batch smoothing over real-time response. The eventual real-time question is important, but should not constrain the initial scientific architecture.

---

## 15. Initial software architecture

A first codebase should separate raw evidence, inference modules, and user-facing products.

Suggested logical modules:
*   `capture/`: channel metadata, session manifests, microphone-placement notes, raw-audio integrity checks.
*   `audio/`: resampling, STFT, cross-correlation, phase coherence, onset detection, source embeddings, event features.
*   `clock/`: local timestamp extraction, relative clock-map hypotheses, smooth clock-relation estimation, uncertainty traces.
*   `geometry/`: local body-pair geometry, source bearing estimation, relational motion hypotheses, trajectory priors, factor graph.
*   `entities/`: entity birth, association, split/merge, persistence, body association, source identity.
*   `separation/`: scene-informed filtering, source extraction, iterative refinement.
*   `semantic/`: ASR, diarization surface, sound-event labels, session interpretation.
*   `scene_record/`: entity graph, relational trace, provenance, confidence, export formats.
*   `evaluation/`: annotations, baselines, metrics, experiment reports.

The architecture should preserve the ability to replace models without destroying the original evidence or prior inference history.

---

## 16. Data and storage principles

The raw multichannel recording is the archival truth. Derived products are useful but replaceable.

The system should preserve:
*   original WAV files;
*   checksums;
*   session manifests;
*   microphone geometry notes;
*   software versions;
*   model versions;
*   intermediate inference products;
*   human annotations;
*   final Acoustic Scene Record;
*   uncertainty and provenance data.

No downstream process should silently overwrite or discard the original capture.

---

## 17. Privacy, consent, and trust envelope

This project touches intimate human context. Its legitimacy depends on clear consent and strong local control.

The system should be designed around:
*   informed consent of recorded participants;
*   visible, understandable capture practices;
*   local-first storage where possible;
*   ability to restrict or revoke access;
*   differentiated access to raw audio, transcripts, entity records, and semantic summaries;
*   preservation of provenance;
*   explicit uncertainty;
*   no covert surveillance posture;
*   careful treatment of third-party voices and sensitive places.

The purpose is not to make people more legible to institutions. The purpose is to help people preserve and make sense of their own situated lives, relationships, projects, and environments.

---

## 18. Open research questions

1.  How much useful relational geometry can be inferred from two moving stereo body frames without video?
2.  How much does a single fixed local microphone improve observability and entity persistence?
3.  Which microphone placements preserve enough stable geometry while remaining comfortable for real walks and conversations?
4.  Can body-associated near-field microphones provide robust source-ownership anchors for voices?
5.  How reliably can the system separate clock-rate variation from changing propagation delay?
6.  What forms of natural movement produce enough constraint to resolve otherwise ambiguous geometry?
7.  Which environmental sounds become useful acoustic landmarks, and under what conditions?
8.  How should the system represent diffuse sounds such as wind, rain, creek noise, or crowd murmur?
9.  Can source separation and source tracking improve each other iteratively without creating self-reinforcing hallucinations?
10. What is the smallest useful Acoustic Scene Record that materially improves on transcript plus ordinary diarization?
11. Which inferences are stable enough to present directly, and which should remain as alternatives or confidence distributions?
12. How can semantic interpretation remain grounded in the underlying acoustic evidence rather than floating free of it?

---

## 19. Near-term development sequence

*   **Phase 0 — Capture integrity:** Establish reliable four-channel recording with raw separate channels, stable channel ordering, repeatable mounting, clear session manifests, beginning/end sharp events, and no destructive processing.
*   **Phase 1 — Four-channel evidence explorer:** Build tools that visualize waveform alignment, cross-correlation, coherence, inter-channel delay, local time-stretch, source activity, and candidate shared events. The immediate goal is to learn what the recordings actually contain.
*   **Phase 2 — Baseline comparison:** Run standard diarization and source-separation tools against the same sessions. Document where they fail (overlap, movement, orientation change, environmental noise, source continuity, non-speech entities).
*   **Phase 3 — Persistent acoustic entity prototype:** Build an entity graph that can maintain candidate source identities across time using acoustic embeddings, cross-channel timing, coherence, body association, and continuity priors.
*   **Phase 4 — Joint clock-and-relation inference:** Implement a first relational odometry model that estimates smooth inter-recorder timing relations, broad relative body relations, source association, and confidence.
*   **Phase 5 — Scene-informed separation and semantic surfaces:** Use the inferred field to improve source separation, diarization, transcription, sound-event inventory, and session review. At this point, the project can begin to test whether an Acoustic Scene Record is genuinely more valuable than conventional audio processing outputs.

---

## 20. Definition of success

The project succeeds when an Understory session can preserve a richer, more grounded account of an encounter than transcript plus diarization alone.

A successful record should make statements such as these possible, with evidence and uncertainty:
*   *“These were two persistent voices, not four fragmented diarization identities.”*
*   *“The speakers moved from side-by-side walking into a face-to-face pause.”*
*   *“A recurring external sound source became salient at this point.”*
*   *“This interruption was likely a bird to the right of both walkers.”*
*   *“This phrase was spoken while the speakers were separating rather than standing together.”*
*   **“This sound was body-associated with one participant.”*
*   *“This source remained fixed in the setting while both participants moved.”*
*   *“The system cannot decide whether these two fragments were one source or two; both interpretations remain plausible.”*

The central achievement is not numerical precision for its own sake. It is a more faithful preservation of **situated acoustic life**: voices, bodies, atmosphere, interruption, relation, place, and time held together in a form that can later support responsible human sensemaking.

Understory Steward should not reduce an encounter to a transcript. It should preserve an acoustic field from which speech, source identity, relation, situation, and meaning can be recovered.
