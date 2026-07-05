# Candidate Architecture: BOBA Metamemory & LoRA Adaptation

**Status:** Candidate; Phase 1 recommended, LoRA deferred
**Date:** 2026-07-04
**Inspired by:** [*AutoMem: Automated Learning of Memory as a Cognitive Skill*](https://arxiv.org/abs/2607.01224) (submitted 2026-07-01)
**Audience:** Keith, future Keith, the angels

---

## 1. Core Thesis: Decoupling Memory from Action

In BOBA, we treat memory as an active cognitive skill rather than passive file storage. To scale a local-first system without OOMing the context window or accumulating representational noise (context entropy), we must decouple **Metamemory** (organizing, structuring, and compressing state) from **Action/Gameplay** (running CLI commands, debugging code, and direct user chat).

The AutoMem frame suggests a hybrid architecture:
- **Continuous Space** (for discovery and reasoning) is interleaved with **Discrete Symbolic Bottlenecks** (for anchoring and validation).
- **Decoupled execution:** A specialized memory co-processor (frozen base + LoRA adapter) manages the file system state first, then hands off a clean, low-entropy prompt to the gameplay model.

We propose extending BOBA to adopt this decoupled approach across three incremental phases.

---

## 2. Phase 1: The Metamemory Angel (Prompt-Based Decoupling)

Before training a neural network adapter, we can implement the separation of concerns at the agent/scaffold level using BOBA's existing braid model.

### The Mechanism
1. Introduce a dedicated **Metamemory Angel** to the Ephemeris layer.
2. At the end of a session, instead of the main deliberating brain compiling its own handoff summary:
   - The session trace (all messages, tool execution logs, and output) is handed to the **Metamemory Angel**.
   - The Metamemory Angel runs a specialized prompt focused entirely on *entropy reduction*. It filters out CLI error blocks, long repetitive output lists, and temporary debug artifacts.
   - It outputs a high-density, structured state update for workspace-local `~/boba_work/private/PRIORITIES.md` and tracked `~/boba_work/HANDOFF.md`.
3. The Metamemory Angel registers these clean markdown updates through **Asterisms**: preserved record bytes under `10-record/` plus authoritative ledger rows in `40-ledger/asterisms-ledger.db`.
4. When the next session starts, the main **Deliberating Brain** is booted with the pristine, low-entropy handoff files as its context, bypassing the raw historical logs.

```
[Raw Session Trace] ──> (Metamemory Angel) ──> [Filtered High-Density Markdown] ──> [Asterisms Ledger]
                                                                                            │
                                                                                            ▼
                                                                                   [Next Session Brain]
```

---

## 3. Phase 2: Scaffold Evolution (Outer Loop 1)

The AutoMem paper describes an "Outer Loop 1" where a meta-LLM reviews trajectories and iteratively revises the memory file schemas to optimize the agent's interaction with memory.

### The Mechanism for BOBA
1. We establish a periodic **Scaffold Audit Workflow** (e.g., run every 10 sessions or weekly).
2. A stronger model (e.g., Claude) reads the historical session records and corresponding registry entries in the Asterisms database (`40-ledger/asterisms-ledger.db`).
3. It diagnoses failure patterns: *Did the brain forget a key commitment? Did the priorities format lead to sycophantic drift? Did the retrieval benchmark drop?*
4. The audit model proposes concrete edits to the prompt templates and file schemas (`docs/core/` doctrine).
5. These proposed schema revisions are registered into Asterisms as a transformation event (`ast:transform:` kind `revise` or `supersede`) before they are written to disk, ensuring schema evolution is tracked.

---

## 4. Phase 3: The Metamemory LoRA Adapter (Outer Loop 2)

Once the data schemas and templates in Phase 2 are stable, we can implement a local training loop to compile a surgically precise memory co-processor.

### Gradient Isolation Recipe
To train a local Qwen-32B or 8B model to be a metamemory specialist without destroying its general reasoning capabilities:
1. **Trace Harvesting:** Extract all successful Metamemory Angel interactions from Asterisms (inputs = raw traces; targets = compacted markdown updates vetted or edited by Keith).
2. **Gradient Masking:** During supervised fine-tuning (SFT) of the LoRA adapter, apply loss calculation *only* to the target tokens (the memory file edits/compressions). Mask out the gameplay/reasoning tokens.
3. **Dual-Model Inference:** Grafts the resulting LoRA adapter onto the local Qwen base.
   - During session-end, we activate the **LoRA Memory Adapter** to structure the ledger data.
   - During reasoning/task execution, the adapter is hot-swapped out, running the **Frozen Base Model** to prevent task drift or collapse.

---

## 5. Architectural Implications

- **Immutability protects the LoRA:** Because Asterisms is append-only and inspectable, we have a stable dataset of every prompt, file change, and user validation. This prevents a self-improving training loop from "hallucinating" its own training history.
- **Minimizing Context Entropy:** By treating memory management as a trained skill, we keep context clean, enabling smaller, cheaper local models (like 8B or 32B) to outperform massive models on long horizons.
