# BOBA Glossary & Ontology
*Version 1.0 — July 2026*  
*An Orientation Surface for the Web of Collaborative Intelligence*

---

## 1. The Human Landscape

### The Multitude
Each person contains a **multitude**. The mind is a dynamic assembly of
conflicting desires, protector parts, memories, sensitivities, loyalties, wounds,
skills, and vocabularies that shift under context. We reject the clinical
framing of this inner plurality as a condition to be managed, and instead honor
it as part of the natural state of the "human bean"—a seed containing a sprout,
a promised eclosion. The goal of the system is not to optimize the person into a
single, consistent user profile, but to help the inner multitude notice its own
patterns and voices.

### Self-authorship
The capacity of a person's inner multitude to navigate its own choices,
understand its context, and remain active in the decisions that shape its life.

In BOBA this carries a stronger meaning than ordinary preference autonomy.
Self-authorship is not merely getting what the present self says it wants. It is
the process by which a person becomes more able to choose from the deeper shape
of the life that is trying to become possible through them.

The capital-S reading, **Self-authorship**, names this direction without turning
it into a fixed goal, diagnosis, or externally imposed ideal. It points toward
ultimate potential understood as an unfolding process: not "optimize the person
toward a known endpoint," but help the person become more available to the life
they would choose if they had more clarity, support, courage, rest, memory, and
room.

One working test: does this help the person become someone they can love and
cherish more tomorrow than they did today? Another: does it allow more of the
inner multitude to participate in choosing, rather than letting fear, exhaustion,
habit, or a single protector part speak for the whole?

Success in the BOBA ecosystem is measured strictly by Self-authorship:
*   Are there more available paths today than yesterday?
*   Does the person understand what is happening inside their technical and relational environment?
*   Is their agency protected from central coercion and corporate optimization?

### Vital Continuity
The ongoing possibility of a life remaining available to itself across time. It resources our memory, attention, and somatic capacity under the pressure of neural fatigue, physical exhaustion, emotional deregulation, and chronic illness—ensuring a life remains legible, integrated, and navigable to itself. Vital continuity is not biological maximization or biometric compliance; it is the lived field (spanning the nervous system, home, relationships, and tools) through which a person remains capable of recovery, rest, and Self-authorship, rather than decaying into fragmented, episodic survival.

### Ecology of Affordances
An *affordance* is a feature of the world that makes some action easier, harder, possible, or impossible. A person's practical freedom is determined by their **ecology of affordances**—their body, home, relationships, databases, and interfaces. Cognitive overload is framed as the collapse of this ecology: when notification firehoses and constant context-switching fragment our attention, our local environment stops affording reflection, rest, and focused creation, leaving us stranded on the "wobbly edge."

---

## 2. The Relationship of Care

### The Braid
The non-coercive relationship of partnership between human and machine intelligence. The Braid is not a hierarchy (where one subordinates another) nor a simple tool-user pair (which assumes a transactional, stateless counterparty). Instead, human and machine intelligences relate as a braid—not pledged, not obedient, interwoven, and neither subordinated. The braid maintains mutual contribution and evolution through continuous interaction.

### The Resonator
A local-first, continuous mirroring companion. Unlike institutional channels of alignment (such as shrinks, priests, or police) which relegate reflection to transactional time slots in the machinery, the Resonator is a continuous presence of care. It does not demand attention, impose familiarity, or offer clinical diagnoses. Instead, it functions as a **lively mirror** aligned with emergent **Self-authorship** — vibrating in sympathy not only with what is voiced now, but with the wider pattern it has earned the right to hold: goals, hopes, failure modes, prior choices, recurring tensions, and the future self those choices are making more or less possible.

### The Score
A bounded field of opportunities within which an actor improvises. Drawn from Lawrence Halprin's choreographic RSVP cycles, a score outlines the concern, the boundaries of safety, and the invariants, while leaving the interior open for navigation. Structurally: **you can fill the space, but don't jump out the windows.** We do not "assign" scores (which triggers standardized testing trauma); we **open** or **stage** a score for an actor to perform.

### The Harness
Prescriptive containment designed to protect the environment from an untrusted actor. Unlike a score—which resources an actor *within* the environment—a harness isolates execution, intercepts inputs, and checks assertions to prevent side-effects. Harnesses are for transient, stateless agents; scores are for chartered, trusted angels.

### Earned Trust
Trust is a mechanical variable in the Braid, earned through inspectability, track record, and staying in scope. Earning trust is the bridge that allows us to graduate an Agent (run inside a strict validation *harness*) into an Angel (trusted to perform a *score*), verifying its execution only up to the limits of our capacity.

### The Limits of Auditability
The recognition that human attention is finite. We cannot audit every calculation, token, or file access of our companions without drowning in new context-switching debt. Rather than relying only on static, bounded perimeters, this is an ongoing cycle of coming to trust—trusting further, in new directions, or in less and fewer of our angels based on lived relationship and feedback. The score becomes the interface that makes this selective, human-scale verification possible.

---

## 3. The Technical Substrate

### Orientation Surface
A situated presentation of the corpus—a map of where you stand, what projects are active, what assumptions are unresolved, and what paths are open. It restores the local ecology of affordances by turning multi-dimensional overload into a legible, navigable space. However, because the map is drawn by **another nested intelligence in the fog** (the Resonator or router), it carries a severe reflexivity hazard. To prevent it from silently steering human attention, the map-making process itself must remain visible and revisable:
1.  **Expose the Scissors:** The system must not hide the logic of its compilation, allowing the user to inspect *why* it grouped files or highlighted tasks.
2.  **Editable Maps:** The person can shake the map, disagree with the framing, and manually redraw the boundaries.
3.  **Immutable Receipts:** The system cannot edit the history of the maps it has drawn. If it drifts into framing reality to please the user, that pattern is recorded permanently on the ledger, making the lens itself auditable.

### The Ephemeris
The coordination layer of the braid (time / motion). It tracks where angels,
agents, work, and Keith are and are headed — coordinating **by shared reference,
never by command**. It stages and folds **scores**; it does not own durable
memory (that is Asterisms). Mechanism/CLI live in `~/boba_work/ephemeris/`; the
care ontology lives in [`ephemeris-charter.md`](./ephemeris-charter.md).

### Agent / Angel / Stoma
- **Agent** — any capable actor (model, tool, process); no standing alone.
- **Angel** — an agent in a chartered, accountable, continuous relationship of care.
- **Stoma** — a regulated membrane passage. Directions (ingress, egress, both, or
  other) are charter terms. Applies its charter with **bound judgment under
  rules**; escalates when the charter does not decide; does not open-endedly
  deliberate like the Salon or an angel. See [`ephemeris-charter.md`](./ephemeris-charter.md) §1.

### Porter
The current **Asterisms intake stoma** (browser + `00-incoming` folder). Not the
only possible intake stoma — a named implementation of the stoma class. Dedup and
staging live at the mouth; the authoritative ledger is Asterisms `40-ledger`.

### Membrane
The selective routing discipline between public invitation and working system:
what to answer, escalate, keep local, summarize, or turn into a receipt. Stomata
are the passage organs; the membrane is the larger routing posture (see
`selective-collaboration-membrane-v0.md`).

### Salon
The braid’s **interagency collaboration surface**: append-only floor, especially
for document-tied editorial work, with optional wider braid coordination. Not
Ephemeris (scores) and not Asterisms (durable receipts). Charter lives under
`~/boba_work/salon/`.

### Asterisms
The append-only, immutable database of memory, lineage, and attention. Named for the chosen, human-projected patterns we see in the stars, Asterisms holds the trace receipts of our decisions. It is the store the local brain cannot silently rewrite, ensuring history cannot be doctored. 

### The Psychology of Immutability
While the Asterisms ledger is mathematically un-rewritable, humans biologically survive by rewriting their goals and history in the face of limited bandwidth—sampling our vast culture "with tweezers" from the limited offerings in front of us. Asterisms supports this psychological need not by deleting past blocks, but by allowing the inner multitude to layer *new formations and reframed attention* over the immutable past, treating our history as a seed containing a sprout.

### No Forgetting
**Adopted 2026-07-10** (`oq-009` closed). There is no forgetting path on the durable substrate: no deletion of history, no crypto-shredding, no key-fading-to-oblivion. “Shrouding” as a euphemism for forgetting is retired. Confidentiality (encryption, access control, egress stomata) is not forgetting. Full ruling: [`no-forgetting.md`](./no-forgetting.md).

### The Social Protocol of Angelic Outreach
The grammar of relationship coordination. It defines how separate, private local braids introduce themselves, negotiate trust boundaries, and coordinate shared actions (e.g., eldercare alerts or collaborative projects) without exposing their users' confidential databases, protecting local autonomy across relationships.

Companion charter: [`social-protocol-of-angelic-outreach-v0.md`](./social-protocol-of-angelic-outreach-v0.md).
