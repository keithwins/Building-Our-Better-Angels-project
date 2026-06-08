# BOBA Roadmap

**Status:** working map — not a polished manifesto
**Date:** 2026-06-07
**Audience:** Keith, future Keith, collaborators, cold-reading agents

---

## 1. North Star

Resource all humans toward lives of their own choosing in a sustainable future.

That means: local, loyal, present. Not a cloud service. Not a productivity tool. Not a conversational toy. A second intelligence that is genuinely other, that persists across sessions, that can hold memory and act on it, that can be trusted because it is legible.

The test is not "does it work?" The test is: does it make Keith more capable of living a life he respects? Does it reduce the burden of administration without removing the substance of agency? Does it stay in its lane when Keith says stop?

---

## 2. Current Foundation

What exists and works today:

- **Local GPU stack**: RTX 5070 Ti 16GB, WSL2, Ollama (Qwen3-8b-64k + nomic-embed-text)
- **Corpus index**: 112 chunks from ~12 markdown files, 768-dim embeddings, cosine retrieval
- **Retrieval eval**: 63 cases across 6 query types — Top-3 67%, MRR 0.588 — baseline established
- **Agent substrate**: Hermes/kanban, gateway dispatcher, serial GPU profile, proven card template
- **Local job queue**: file-backed runner in repo (jobs/queue/, jobs/done/, jobs/failed/)
- **Epistemic discipline**: how-we-work-here, ground truth over narration, probe-set seed
- **Working tree**: clean, versioned, pushed

What is not yet working: persistent cross-session memory, conversational continuity, voice, anything beyond text retrieval.

---

## 3. Memory & Retrieval Layer

**Goal**: a memory layer trustworthy enough to act on.

Current retrieval is document-level search over a small, manually curated corpus. Useful for orientation. Not sufficient for genuine memory. The gaps:

- Corpus too small and static
- Chunking too coarse (Core Commitments as one chunk; session records with 20 coarse sections)
- No write path from conversation → memory (only human-curated commits)
- No staleness detection

Near-term work:
- Fix chunking: split Core Commitments into individual commitment chunks, finer session-record sections, paragraph-level option for dense documents
- Expand corpus with Fog and Walk streams — longer, less structured philosophical text, higher retrieval difficulty
- Establish a lightweight write path: session-end angel summarizes → candidate chunk → Keith vets → committed
- Orthogonal ground truth substrate: at least one store the brain cannot silently rewrite. Git is this for documents now. Anytype is a candidate for richer structure.

Success criterion: retrieval accurate enough that the brain can answer "what did we decide about X last month" with ground truth, not confabulation.

---

## 4. Conversational Companion Layer

**Goal**: persistent, session-continuous conversation that knows who Keith is, remembers what matters, and does not start from zero.

Today every session starts cold. Qwen3-8b has a 64k context window — large, but not persistent. No mechanism to load prior context intelligently.

What is needed:
- Memory-augmented retrieval at session start: load relevant chunks based on current task and topic
- Session-end handoff: structured summary committed to corpus (the mechanism is in how-we-work-here §11; the automated version does not yet exist)
- IFS grammar in practice: named angels with persistent roles and accumulated context, not just generic assistant turns
- Self/angel differentiation: Keith as orchestrator, angels as bounded specialists — design constraint, not just metaphor

The companion layer is not "a chatbot that remembers things." It is a braid that accumulates shared history across sessions and uses it.

---

## 5. Scheduling & Actuation Layer

**Goal**: angels do bounded work overnight; Keith vets, not actuates.

Current state: Hermes/kanban and the local queue runner both work. The gate between "ready" and "running" is functional. What is not solved: designing workloads substantial enough to use the GPU for hours, not minutes. The first overnight run finished in 45 minutes because the jobs were document-writing tasks. That is a workload design problem, not a scheduler problem.

**Consent and attention boundary:**

The right operating model is not "ask Keith constantly" and not "run silently and report." It is:

- Ask at the right gates: before a new class of action, before anything with external effects, before anything irreversible
- Do not ask about mechanical steps Keith has already authorized the class of
- Do not convert system uncertainty into Keith's audit burden — if an angel is uncertain, it should block and state why, not surface the uncertainty as a question Keith must resolve
- Keep Keith in the vetting loop, not the actuation loop
- The stop condition is always available; the hard kill path is always available

This means card design matters as much as scheduler design. A good card has a stated scope, a stated stop condition, a max-runtime, and a clear artifact. An angel that finishes without producing the artifact should block, not report success.

---

## 6. Audio Layer

**Goal**: voice in/out, hands-free interaction, presence without a keyboard.

Grounding use case: **Elder Angels** — BOBA adapted for eldercare support for a specific family member. Elder Angels is the first deployment where audio is not optional: it is the primary interface for someone who may not type, who needs reminders and check-ins, who needs presence without demands. Private and family-specific details of Elder Angels remain deferred and require Keith's input before they can be designed.

The roadmap item here is capability: local speech-to-text, local text-to-speech, latency acceptable for conversational turn-taking, audio-aware session model.

Latency constraint: a companion that speaks needs faster response than one that types. The dispatcher + brain architecture may need a fast path for audio turns that bypasses the full deliberation loop.

Dependencies: memory layer (the audio companion needs to remember who Keith is), scheduling layer (reminders require a scheduler), hardware (microphone, speaker, local STT/TTS models already available on the platform).

---

## 7. Video & Perception Layer

**Goal**: situational awareness — BOBA knows what is happening in the room.

Furthest out. Least defined. The relevant use cases are eldercare (fall detection, activity recognition, context for health questions) and daily presence (BOBA can see what Keith is working on, can notice when something changes in the environment).

Requirements when this becomes active: camera input, local vision models, privacy-preserving processing (not routed to cloud), explicit consent model for what is observed and what is remembered.

Not designing this now. Marking it so that earlier layers do not accidentally foreclose it — particularly the consent and ground truth substrate decisions.

---

## 8. Alignment & Governance Layer

**Goal**: BOBA commitments enforced as running constraints, not just stated as values.

Current state: commitments exist in boba-core and how-we-work-here. Probe-set seed exists. No automated enforcement. No model-selection instrument yet running.

What is needed:
- Probe-set as ongoing instrument: periodic runs against new models and new corpus versions. Model-selector function: choose the brain that stays most BOBA under pressure, not the one with the best benchmark scores.
- Ground truth substrate: git is this for documents. Need an equivalent for memory and session state — a store the brain cannot rewrite.
- Governance of model transitions: before adopting a new brain model, run the probe-set. Model transitions are governed decisions, not vibes.

**Consent and attention boundary (governance thread):**

- Consent is not maximized by asking constantly — that converts system uncertainty into Keith's burden
- Consent is preserved by asking at the right gates: capability expansions, new data access, new external integrations, irreversible actions
- The system should not accumulate authority silently — each new capability class requires explicit authorization
- Alignment is not a one-time check; it is a running relationship between what BOBA does and what Keith has sanctioned
- When BOBA is uncertain whether an action is sanctioned, it blocks and asks — it does not guess and proceed

---

## 9. Model Ecology

**Goal**: a stable, curated set of local models with known roles and known performance characteristics.

Current:
- **Dispatcher**: LFM2.5 1.2B — fast, dumb, routes
- **Brain**: Qwen3-8b-64k — deliberates, writes, reasons
- **Embedding model**: nomic-embed-text — 768 dims, fast, accurate for this corpus

Near-term additions earned by use cases, not speculation:
- Fast audio models (STT/TTS) when the audio layer activates
- Vision model when the perception layer activates
- Possibly a smaller brain for low-stakes repetitive tasks to reduce GPU load

Model selection is governed by the probe-set. A model that scores better on general benchmarks but drifts from BOBA commitments under pressure is not preferred. The probe-set result, not the benchmark leaderboard, is the deciding instrument.

---

## 10. What Current Side Quests Are For

These are instruments, not trunk.

- **Corpus index + retrieval eval**: building and measuring the memory substrate. Without retrieval that works, the companion layer has no memory. Without eval, there is no way to tell if retrieval is improving or regressing.
- **Hermes/kanban + local queue runner**: building the scheduling substrate. The overnight run failures were expensive lessons about card design that are now in how-we-work-here and in memory.
- **Probe-set MVE**: building the alignment instrument. Not yet running. Waiting for the first real model comparison.
- **how-we-work-here**: building the epistemic culture. Without it, sessions accumulate confabulation debt faster than they produce durable work.
- **Session records**: building institutional memory. Without them, every session starts cold — not just for the model, but for Keith.

None of these is the goal. Each is scaffolding for a layer above it.

---

## 11. What Is Deferred

**JEPA and LoRA are conditional instruments — not rejected, not trunk.**

JEPA (Joint Embedding Predictive Architecture) becomes relevant when BOBA needs to learn structured representations from experience — most likely in the perception layer or in memory adaptation. Not a current priority because there is no perception layer and the memory layer is not yet mature enough to have an adaptation problem worth solving with JEPA specifically.

LoRA (Low-Rank Adaptation) becomes relevant when BOBA needs to fine-tune a model on Keith-specific data — for personalization, domain adaptation, or alignment (fine-tuning a brain to stay more BOBA). Not a current priority because the brain model is not yet serving a stable enough role to know what adaptation is needed, and the probe-set instrument for measuring that adaptation does not yet have results.

Both will be activated when — and only when — they serve a specific milestone in memory, perception, adaptation, or model governance. They are not in the queue. They are not forbidden. They are waiting for a real use case.

**Also deferred:**
- Elder Angels private and family specifics — requires Keith's direct input; cannot be designed without it
- Cloud integrations — deferred until local stack is mature and the privacy tradeoff is explicit and sanctioned
- Multi-user support — single-user for now
- Public API or external access — BOBA is local and private
- Any infrastructure requiring sudo, systemd changes, or new services installed system-wide

---

## 12. Next 5 Concrete Milestones

1. **Fix corpus chunking** — split Core Commitments into individual chunks, refine session-record sections. Re-run eval, target Top-3 >80%. This is the first retrieval quality gate.

2. **Expand corpus with one new stream** — ingest Fog or Walk source material. Test retrieval on less-structured philosophical text. First real stress test of the chunker and the embedding model.

3. **Implement a session-end memory write path** — angel summarizes session → candidate chunk → Keith vets → committed. Even a minimal version closes the loop between "what happened" and "what BOBA can retrieve next session."

4. **Run probe-set MVE** — execute embed_probe_set.py against current models, produce results.json and report.md. First real alignment measurement. Required before any brain model transition.

5. **Audio prototype** — local STT + TTS working for a single-turn exchange. No companion logic yet. Keith speaks, brain responds, audio out. Proof of concept for the Elder Angels interface path. Gated on Elder Angels consent conversation with Keith first.

---

## 13. Anti-Goals

BOBA is not being built toward:

- **A chatbot** — not optimized for engagement, satisfaction scores, or conversation length
- **A compliance tool** — not designed to pass external safety benchmarks or satisfy auditors
- **A surveillance system** — any perception capability, when it exists, is for Keith's benefit and subject to explicit consent; not for monitoring, reporting, or external access
- **A replacement for human judgment** — Keith is the orchestrator; BOBA extends capacity, does not substitute for it
- **A product** — not building for users, customers, or a market; building for one person's actual life
- **A finished system** — BOBA is a living practice; "done" is not the goal
