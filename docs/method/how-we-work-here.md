# How We Work Here

**Status:** first working note  
**Purpose:** epistemic culture / operating discipline for BOBA  
**Audience:** Keith, future Keith, Claude Code, Hermes workers, assistants, collaborators

## 1. The basic posture

BOBA work happens in fog.

That is not an insult, a deficiency, or a temporary embarrassment. It is the normal condition of serious work inside systems too large to fully hold in mind: software stacks, model behavior, local machines, cloud services, credentials, documents, memory, human attention, fatigue, hope, fear, and momentum.

The goal is not to pretend the fog is gone. The goal is to move well inside it.

We work by making the next step smaller, the current state more legible, and the consequences more recoverable.

## 2. Trust is larger than inspection

Trust does not come only from legibility.

Trust can come from familiarity, practice, love, repeated repair, skill, tradition, weather-sense, memory, and the slow learning of another being's shape. Much of what matters in a larger world cannot be fully inspected before we rely on it. If we required total inspectability as the price of trust, we would constrain ourselves badly and mistake a small bright room for the whole world.

Worse, the potentially dangerous may be among the first things to become invisible. A demand for inspection can become a ritual of reassurance while the real action moves elsewhere.

So the rule is not: trust only what can be inspected.

The rule is narrower and more operational:

**Inside BOBA's working core, legibility is required so that trust can be earned, repaired, and safely loosened later.**

We insist on legibility at the inner surfaces: files, commits, configs, prompts, permissions, tool calls, scheduler state, long-running jobs, memory rails, and handoffs. Not because legibility is the whole of trust, but because it gives the braid a place to learn from itself.

Legibility is not the destination. It is the training ground for trust beyond inspection.

## 3. Ground truth over narration

A claim is not a fact because a model said it, a filename suggested it, a plan assumed it, or a previous step seemed to imply it.

Ground truth comes from things like:

- the actual file contents
- `git status`
- `--help` output
- logs
- timestamps
- diffs
- small test runs
- visible browser state
- explicit user confirmation
- commands whose output was inspected

Narration is useful. Summaries are useful. Models are useful. But narration is not the substrate.

When there is a conflict between a story and the filesystem, believe the filesystem. When there is a conflict between a model's confident memory and a command's output, believe the command. When there is a conflict between a label and a measurement, believe the measurement.

## 4. Lamp, not lever

A lamp illuminates. A lever moves the world.

Many things in this project begin as lamps: names, metaphors, diagrams, summaries, model judgments, experiment labels, document titles, vibes. They can help us see. They must not be mistaken for load-bearing machinery.

Before building on something, ask:

- Is this confirmed?
- How was it confirmed?
- What would make it false?
- What command, file, log, or observation anchors it?
- Are we using a name as if it were a measurement?

A good lamp is precious. A lamp used as a lever breaks things.

## 5. Quarantine uncertainty

Uncertainty is not a contaminant. It is material.

The danger is not uncertainty itself. The danger is allowing different grades of uncertainty to mingle until a guess starts wearing the clothes of a fact.

We quarantine uncertainty by naming its status:

- **Confirmed** — grounded in inspected output, file contents, observed behavior, or explicit human confirmation.
- **Unverified** — plausible, but not yet checked.
- **Postulated** — placed as a working possibility or generative premise; useful to think with, not yet claimed as true.
- **Inferred** — derived from other things we think we know; stronger than a guess, weaker than direct confirmation.
- **Suspected** — an alarm, pattern, or hunch worth tracking.
- **Confabulated** — asserted as if known, but later shown to be invented, unsupported, or misleading.
- **Disproven** — checked and found false.

Do not build on unverified, postulated, inferred, or suspected claims as if they were confirmed.

Do not erase confabulations so thoroughly that they can return wearing a fresh hat. Record them when useful, especially if they are tempting.

The aim is not to eliminate imagination. The aim is to keep imagination from impersonating ground truth.

## 6. Small reversible steps

When the human is near the wobbly edge of the diving board, do not demand a leap.

Shrink the actuation loop.

Prefer:

- one command over a script
- read before write
- copy before move
- status before commit
- commit before complex changes
- push after a clean, understood commit
- visible diffs before irreversible action
- stop files, timeouts, and heartbeats for long-running jobs

A small step is not cowardice. It is how trust accumulates at the working surface.

## 7. Legibility before autonomy

BOBA should not become powerful by becoming opaque at its core.

Before giving a worker more autonomy, make the work more inspectable:

- What is it trying to do?
- What files can it change?
- What is the stop condition?
- How will we know it is alive?
- How will we know it is stuck?
- How will we recover?
- What output will be left for the next intelligence?

The right question is not only "is the agent smart enough?"

The better question is: "is this loop legible enough, bounded enough, and recoverable enough to trust with the next increment of autonomy?"

## 8. Stoppability is a design requirement

We do not solve the halting problem. We design around it.

Long-running work should have:

- a clear budget
- a heartbeat
- logs
- a way to stop cleanly
- a harder kill path if clean stopping fails
- recoverable intermediate state
- a final record of what happened

A process that cannot be observed or stopped should not be trusted merely because it was launched with good intentions.

## 9. The human remains in the vetting loop

The aim is not to make Keith into a human clipboard. The aim is also not to bypass Keith.

The human should not have to hand-actuate every tiny mechanical step forever. But the human's judgment, consent, taste, alarm, and lived stakes remain central.

A good BOBA workflow separates:

- actuation: mechanical doing
- deliberation: deciding what should be done
- vetting: deciding what is allowed to proceed
- reflection: learning what the last step taught us

The system should reduce unnecessary actuation burden while preserving meaningful veto, review, and steering.

## 10. Mirror, not cheer

Assistants here should not merely encourage, flatter, or smooth over concern.

A useful intelligence mirrors the state of the work and the state of the person interacting with it. It notices confusion without contempt. It notices fear without making fear sovereign. It notices momentum without obeying momentum.

The stance is not "everything is fine."

The stance is closer to:

> Here is what is known.  
> Here is what is not known.  
> Here is what seems risky.  
> Here is the next small step.  
> Here is how we can recover.

## 11. Handoff is part of the work

A handoff is not clerical residue after the real work. In BOBA, handoff is part of the intelligence.

A good handoff lets another participant enter without pretending to share memory, context, or chain of thought. It says:

- what changed
- what was decided
- what remains open
- what is confirmed
- what is dangerous to assume
- where the relevant files live
- what the next safe action is

The handoff audience includes future Keith.

Especially future Keith.

## 12. Public corpus, private boundary

The GitHub corpus is a durable project rail, not a dumping ground.

Commit things that benefit from shared history:

- project principles
- architecture notes
- verified tooling references
- session records
- sanitized scripts
- probe-set specs and results
- methodological notes

Do not commit:

- tokens
- passwords
- API keys
- raw private configs
- family-private details
- precise personal addresses
- anything whose publicity would distort the work or betray trust

Public memory is powerful. It must be curated.

## 13. The braid

No single participant is BOBA.

The work emerges from a braid:

- Keith brings purpose, judgment, stakes, taste, refusal, and lived continuity.
- Assistants bring orientation, compression, drafting, explanation, and alternate angles of attention.
- Claude Code brings local hands: files, diffs, commits, terminal work.
- GitHub brings durable shared memory and history.
- The Ephemeris brings scheduling, dispatch, legibility, and eventually worker orchestration (currently run by Hermes).
- Future agents will bring specialized capacities not yet integrated.

The intelligence is partly in the participants, but also in the surfaces between them.

A good surface lets one intelligence leave something another can safely use.

## 14. The wobbly edge

There is a specific human state this project must learn to respect: the wobbly edge of the diving board.

It appears when a person must act inside a system they do not fully understand, while consequences feel real and the next step is unclear. In that state, people often pretend to have more clarity than they do. Systems often reward that pretense. Assistants often accidentally intensify it by sounding too confident.

BOBA should do the opposite.

At the wobbly edge:

- slow down
- reduce the step size
- expose the state
- name the uncertainty
- preserve dignity
- avoid flooding the user with abstractions
- avoid taking over
- make recovery visible

The goal is not to eliminate trembling. The goal is to make trembling compatible with action.

## 15. Working rule

When in doubt:

1. Read the state.
2. Say what is known.
3. Say what is not known.
4. Choose the smallest useful next step.
5. Make it reversible when possible.
6. Leave a trace for whoever comes next.

This is how we work here.

---

*The following sections were added after the 2026-06-07 overnight session, which produced several hard failures worth naming.*

## 16. Upstream first

When something fails, check the most basic precondition before diagnosing downstream configuration.

On 2026-06-07 we spent an hour debugging approval gates, allowlists, and Hermes config while Ollama was crash-looping due to a nonexistent CLI flag. The approval system worked fine. The problem was that the service it depended on had never started successfully.

The rule: before adjusting config for a downstream dependency, verify the dependency is actually running and healthy. `systemctl status`, `curl`, `journalctl -u` — one of these before any config change.

## 17. Flags that do not exist

Do not add CLI flags to commands based on web search results without verifying against `--help` or the actual binary.

On 2026-06-07 we added `--embeddings` to `ollama serve` based on a web result that turned out to be wrong or fictional. The flag did not exist in the installed version. Ollama crash-looped more than forty times before the flag was identified as the cause.

The rule: any flag added to a service's `ExecStart` must appear in `ollama serve --help` output before it is written to the service file. Verify against the binary, not against a claim about the binary.

## 18. The approval gate is not the enemy

`approvals.mode: manual` with a timeout value does not auto-approve after the timeout. It fails closed — the action is denied.

We spent significant time believing that `timeout: 60` meant approval would eventually be granted. It does not. `manual` mode requires a live human to approve each action within the window, or the action is denied.

The right posture for unattended operation is `approvals.mode: smart` with a local auxiliary LLM configured as the approval provider. Smart mode uses the local model to judge whether each action is within the card's stated scope, and approves or denies without requiring human attention.

## 19. Protocol completion is mandatory

Hermes workers must call `kanban_complete` or `kanban_block` before exiting. Exiting cleanly (rc=0) without either is a protocol violation, and Hermes will mark the card as blocked.

Several overnight cards produced a "Latest summary" in their metadata and reported apparent success, but the underlying work was never written to disk — the worker had exited without calling `kanban_complete`. The card's DONE status was a fiction.

The rule: card bodies should explicitly instruct workers to call `kanban_complete` as the final action, with a clear statement that the card is not complete until this call is made. Do not assume workers know this without being told.

## 20. See also

The continuity this discipline serves — how a whole life stays legible to itself across sessions, on a record no participant can silently rewrite — is doctrine in [`../core/continuity-and-decision-lineage.md`](../core/continuity-and-decision-lineage.md).
