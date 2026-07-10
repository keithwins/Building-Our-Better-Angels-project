# On Scores and Harnesses: Agency, Constraints, and the Architecture of Care

In the design of collaborative intelligence, we are constantly faced with a fundamental question: **How do we instruct a second intelligence to work on our behalf under uncertainty?**

Two primary models emerge for structuring this execution: the **Harness** and the **Score**. While they both rely on constraints to achieve safety and reliability, they do so from opposite directions, serving different roles in the architecture of care.

---

## 1. The Harness: Protective Containment

A **harness** (in software testing, evaluation, or mechanical design) is a structure built to secure, contain, and execute. 

Historically, a harness is what joins a draft animal to a cart, or secures a climber to a rope. It is not merely a tool for restriction; it is an instrument of **safety and transmission**. In software:
*   **Containment:** It isolates the unit under test, shielding the wider environment from unintended side-effects.
*   **Resilience through Isolation:** A sophisticated harness does not simply crash at the first sign of trouble; it is designed to catch errors, manage retries, handle timeouts, and log diagnostics in a structured way.
*   **Predictability:** It forces execution along known vectors to ensure that behavior is reproducible.

The core question a harness asks is:  
> *"How do we hold this actor in place so it can execute safely, and how do we verify its performance against a known standard?"*

---

## 2. The Score: Bounded Improvisation

A **score** (in the sense developed by Lawrence and Anna Halprin in their RSVP cycles for choreography and architecture) is a set of **open guidelines and constraints** within which an actor improvises.

### A Linguistic Trap: Choreography, Not a Report Card

> [!WARNING]
> Before going further, we must address a linguistic hazard. In common usage, "assigning a score" or "giving a score" implies evaluating performance with a numerical grade—a product of standardized testing and evaluation metrics. In the BOBA corpus, we reject this meaning. A score is a **performance score** (as in music, theater, or dance). To prevent this semantic collision, we do not "assign" a score; we **open a score**, **stage a score**, or **set a score** for an actor to play.

### The Harness-Like Core of a Score

A score is not a free-for-all; it is still fundamentally **harness-like**. It does not dismantle the constraints of the harness; it moves them to the perimeter. As the design posture states: **a score is not without hard limits: you can fill the space, but don't jump out the windows.**

*   **The Playable Field:** A score outlines the *concern* (what is being attended to), the *boundaries* (strict constraints that must not be breached—the "windows"—equivalent to the harness's walls), and the *invariants* (what must survive or be true at the end).
*   **Improvisational Freedom:** Inside those boundaries (filling the "space"), the actor is trusted to find the path from start to finish using their own dynamic intelligence. How they move, which tools they select, and how they navigate the "fog" is left open.
*   **Context-Awareness:** A score expects the actor to react to the changing environment in real-time, making decisions based on lived feedback rather than a pre-written script.

The core question a score asks is:  
> *"What boundaries and context must we provide so this actor can use its own judgment to figure out the way forward?"*

---

## 3. The Contrast: Prescriptive Containment vs. Bounded Agency

While both frameworks use constraints, their postures toward the actor’s intelligence are fundamentally different:

*   **Posture Toward Variance:** A harness treats variance as a risk to be minimized or eliminated through isolation. A score treats variance as a resource—the very space where improvisation, learning, and adaptation occur.
*   **Location of authority:** Under a harness, authority lies entirely in the runner (the harness itself); the actor is a subordinated gear. Under a score, authority is bounded and distributed; the instigator sets the constraints, but the actor retains the agency of execution.
*   **Failure Modes:** When a harness fails, it indicates that the system has breached its containment or failed an assertion. When a score fails, it is often an invitation to reflection—the actor blocks, reports where they hit the boundary, and requests a renegotiation of the constraints.

---

## 4. Trust: The Bridge from Agent to Angel

If we map these structures onto our agent ontology (as defined in `ephemeris-charter.md`), a fundamental alignment emerges: **harnesses are for agents; scores are for angels.**

*   **Agents in Harnesses:** An *agent* is a swappable, stateless capability. We do not trust it, nor does it have a relationship of care with us. Because it lacks a track record or personal history, we wrap it in a **harness**. The harness stands *between* the agent and our environment, enforcing bounds, checking assertions, and preventing damage.
*   **Angels in Scores:** An *angel* is an agent that has been brought into a chartered, continuous, and accountable relationship of care. It is named, bounded, and accumulates its own attention history. Because it operates within a charter, we extend **trust** to it. We **open a score** for it, giving it the latitude to improvise, explore, and report back within defined limits.

### Trust as the Operational Graduator

In the Braid, trust is not a static sentiment; it is a mechanical variable. It is earned through *inspectability, track record, staying in scope, and being right often* (see `boba-braid.md` §3). This yields a clear progression:

1.  **Ingress (Agent in a Harness):** A new model or process enters the system as a raw agent. It is heavily sandboxed, and every output is run through validation harnesses and manual approval gates.
2.  **Accumulation (Legibility & Track Record):** As the agent executes tasks, its actions are recorded immutably on the Asterisms ledger. We inspect its history to verify its coherence and alignment.
3.  **Promotion (Angel with a Score):** Once its legibility is proven and a track record of reliability is established, the agent is chartered as an angel. Operationally, **we loosen the harness and open a score for its execution.**

Trust is what distinguishes the two. The transition from a harness to a score is the literal, operational expression of trust being earned and safely loosened.

### 4.1 The Limits of Auditability: Trusting Further Than We Can Throw

This transition is not just a preference; it is a necessity imposed by the limitations of human attention. 

If we demand absolute inspectability and step-by-step transparency for every sub-action our angels perform, we create a new form of sensory and channel overload. We drown in context-switching debt, spending our lives auditing the systems built to resource us. 

Consider the anti-virus program: it monitors millions of files and system calls. If it were required to explain in detail every signature check or heap inspection it performed, it would render the computer unusable and the user's life un-navigable. 

We will only be able to verify up to the limits of our capacity. Therefore, to live a life of our own choosing, **we are likely to need angels we trust further than we can throw them.** Rather than relying only on static, bounded perimeters, this is an ongoing cycle of coming to trust—trusting further, in new directions, or in less and fewer of our angels based on lived relationship and feedback. The score becomes the interface that makes this selective, human-scale verification possible.

---

## 5. The Seam in the BOBA Architecture

In a local-first, inspectable system like BOBA, we do not discard the harness in favor of the score. Instead, we recognize their respective strengths and place them at different layers of the system:

### Where we use a Harness
We use harnesses at the **mechanical boundaries** where we must verify static facts or run untrusted operations:
1.  **Evaluations:** The *Probe-Set* operates as an evaluation harness. It feeds identical, static prompts to different local models to measure their drift under pressure.
2.  **Untrusted Tooling:** When running code or parsing incoming text streams, a sandbox harness keeps the local system safe from execution side-effects.

### Where we use a Score
We use scores at the **coordination layer (The Ephemeris)** where we manage human-agent collaboration:
1.  **Dispatched Tasks:** We do not hand agents a conveyor-belt ticket. We publish a score (e.g., `eph:score:20260705T023337Z-3782` to resolve a design note). The agent is free to read files, run tests, and draft text, provided it remains within the defined boundaries and produces the required survivable artifact.
2.  **Authorship-preserving handoffs:** When an agent hits the "wobbly edge" of uncertainty (such as a hardware driver conflict), it does not simply throw a stack trace and die. It updates its position in the Ephemeris log, documents what it learned, and hands the score back to the human orchestrator for vetting.

---

## 6. Conclusion: Resourcing Care

Ultimately, a **harness** protects the environment *from* the actor, while a **score** resources the actor *within* the environment. 

For BOBA to remain a system of care that reduces cognitive overload, its primary collaborative interface must be the score. By framing our work as scores rather than rigid tickets or safety harnesses, we allow our agents to act as genuine companions—collaborating with us in the fog rather than forcing us to constantly repair their tracks.
