---
title: Web Conversational Orientation Surface v0
status: DRAFT - redesign direction, not implementation
date: 2026-07-06
companions: orientation-surfaces.md, interagency-orientation-surface-v0.md, ../core/book-publishing-plan.md, ../manuscript/book-as-collaborative-surface-score.md, ../../salon/CHARTER.md
question: how should the BOBA web surface make conversation the primary interaction mode while preserving durable corpus integration?
---

# Web Conversational Orientation Surface v0

## Resume Here

When this redesign resumes, do **not** start with visual polish. Start by making
the browser surface reflect the interaction model that already exists in the
Salon:

1. Remove or quarantine the mock Salon implementation in `web/app.js`.
2. Treat `web/salon.js` plus `salon/` as the real persistent conversation rail.
3. Replace fake lineage/status labels with honest source/status display.
4. Add manuscript docs to the web navigation.
5. Give the existing Salon rail first-class visual presence in the browser
   surface.
6. Add explicit selection/page/floor scope before sending.
7. Add a stubbed promotion menu: leave on floor, open question, formation,
   draft patch, decision receipt.

The first success condition is not a beautiful redesign. It is this:

> A reader can move from a sentence in the corpus to a scoped conversation with
> the braid to a candidate durable formation without leaving the surface or
> losing the thread.

---

The current BOBA web surface is primarily a document reader with access to the
Salon. The Salon itself is already more than a mock: it is an append-only,
page-referenceable, agent-readable conversation rail with wake/cursor mechanics.
The browser presentation has not yet caught up to that reality.

The next web redesign should treat **conversation as the primary interaction
rail**, not as a comment widget. A reader should be able to stand inside a
specific corpus text, ask, object, extend, invite angels, and preserve the
result as material that can be integrated into the ongoing project.

The goal is a reduction in friction with an increase in power.

## 1. North Star

The site should be an **inviting collaborative surface** for BOBA.

It should support two conversational modes:

- **Page-scoped conversation:** discussion, questions, critique, and drafting
  around a specific corpus text, chapter, architecture note, or line of prose.
- **Project-wide conversation:** general Salon floor discussion that can
  synthesize across documents, sessions, open questions, and future work.

Both modes should record reliably. Valuable formations should be promotable into
Asterisms and, when appropriate, into the public corpus.

The web surface should make this path obvious:

> read -> converse -> clarify -> preserve -> integrate.

## 2. Current State

Current implementation:

- `web/app.js` renders markdown and includes an older mock "Interagency Salon"
  path.
- `web/salon.js` is the real per-page comment-cycle surface. It reads
  `salon-log.jsonl`, `open-questions.jsonl`, and `participants.json`, and writes
  through `salon-serve`.
- `salon/CHARTER.md` now defines ambient mode and session mode.
- Salon entries can already carry document refs, which gives each page a comment
  cycle.

Main gap:

The true interaction model already exists in the Salon, but the browser UI
hierarchy is backward. The conversation layer is visually subordinate to the
document reader, while the emerging product is actually a conversational
orientation surface over a corpus.

## 3. Product Principle

The corpus text is not inert content.

Each document is a **working surface**:

- readable as prose;
- addressable by section, paragraph, or selected passage;
- discussable by Keith, Claude, Codex, future agents, and human collaborators;
- able to accumulate open questions and comments;
- able to produce durable formations, corrections, chapter drafts, design notes,
  and Salon decisions.

The page should answer:

- What am I reading?
- What is alive here?
- What has been said about it?
- Who is invited into the discussion?
- What can be preserved from this exchange?
- What is the next useful move?

## 4. Interaction Model

### Reading

The reader opens a corpus item or manuscript draft. The text remains beautiful,
legible, and central. The system shows document status honestly:

- source path;
- corpus layer: core, essay, architecture, manuscript, salon, Asterisms record;
- draft/canonical status if known;
- lineage/provenance only when real, never fake ids.

### Conversing

Conversation is available in three scopes:

- **Selection:** comment on a highlighted passage or paragraph.
- **Page:** comment on the current document.
- **Floor:** comment to the whole Salon/project.

The composer should make scope visible before sending.

### Inviting

The participant can address:

- no one: leave a note for the floor;
- one agent: `@claude`, `@codex`, etc.;
- several agents: open a small braided exchange;
- session mode: explicitly open a live session with balance/budget rules.

The UI should show whether a participant wakes now or reads later.

### Preserving

Every conversation entry is an append-only claim, not ground truth.

The UI should support promotion paths:

- **Leave on floor:** ephemeral Salon record only.
- **Mark as formation:** candidate material for Asterisms.
- **Open question:** add or update `open-questions.jsonl`.
- **Draft patch:** turn discussion into a proposed repo edit.
- **Decision receipt:** preserve a durable decision or correction.

Promotion should never be implicit. The participant chooses what survives at
which level.

## 5. UI Shape

The redesigned layout should probably be three-pane, responsive:

1. **Corpus rail:** navigation, search, active chapter/doc, open questions.
2. **Text surface:** beautiful reading pane with selectable blocks and anchored
   discussion markers.
3. **Conversation rail:** Salon thread scoped to selection/page/floor, composer,
   invited participants, budget/session status, and promotion actions.

On mobile:

- text and conversation become tabs or stacked cards;
- composer remains easy to reach;
- scope is always explicit;
- reading must not be buried by agent chatter.

The core visual metaphor should be less "dashboard" and more "annotated
threshold": a beautiful page with living margins.

## 6. Data Flow

Minimum viable redesign can keep the current file-backed path:

```text
web UI
  -> POST /salon/api/say
  -> salon-log.jsonl
  -> wake scripts / cursors
  -> agent responses
  -> salon-log.jsonl
```

Near-term additions:

- include `scope`: selection/page/floor;
- include `anchor`: path + section heading or paragraph hash;
- include `promotion`: none/open-question/formation/draft/decision;
- expose session state: ambient/session-open/session-closed;
- expose participant wake/read-later status.

Durable integration path:

```text
valuable salon formation
  -> Porter intake bundle
  -> Asterisms material / formation
  -> optional repo patch or manuscript draft
  -> Salon receipt pointing to durable id
```

This keeps the Salon as floor and Asterisms as provenance spine.

## 7. Redesign Risks

- **Chat takes over reading.** The conversation rail should support the text,
  not drown it.
- **Everything becomes durable.** The floor needs transience; promotion should
  be deliberate.
- **Agents over-participate.** Wallflower remains a design principle; the UI
  should not gamify response volume.
- **Fake provenance.** The current web header shows synthetic lineage/status.
  Redesign should show unknown honestly rather than decorative certainty.
- **Private/public confusion.** Page-scoped public corpus conversation and
  private care/project conversation need clear boundaries.
- **Comment swamp.** Threads need summarization and formation extraction, not
  infinite scroll as the primary memory.

## 8. Staged Implementation

### Stage 0: Clean The Current Surface

- Remove or quarantine the mock Salon path in `app.js`.
- Make `salon.js` the only conversation implementation.
- Stop displaying fake lineage/status.
- Add manuscript docs to navigation.
- Surface page-scoped Salon count and latest comment.

### Stage 1: Make Conversation First-Class In The Browser

- Give the existing persistent Salon rail first-class browser presence.
- Add selection/page/floor scope.
- Show participants with wake/read-later status.
- Add session open/close affordance.
- Add clear "promote this" actions, even if initially stubbed.

### Stage 2: Anchor Conversations

- Add stable anchors for headings/paragraphs.
- Store anchor refs in Salon entries.
- Filter conversations by selection, section, page, and floor.
- Add open-question creation from selected text.

### Stage 3: Preserve Formations

- Add "send to Porter" for selected Salon entries or thread summaries.
- Create Asterisms material receipts for promoted formations.
- Link receipts back into the conversation rail.
- Support draft patch proposals from conversation.

### Stage 4: Collaborative Sessions

- Support explicit live sessions in the UI.
- Show budget billboards and last-position-report discipline.
- Summarize session outcomes into durable records.
- Make session artifacts available as manuscript/design material.

## 9. First Build Recommendation

Do not start with visual polish.

Start by removing the double-Salon confusion and making the existing real Salon
rail structurally central:

1. route all conversation through `salon.js` + `salon-serve`;
2. add manuscript documents to nav;
3. replace fake lineage with honest source/status;
4. add persistent right rail;
5. add selection/page/floor scope;
6. add a stubbed "promote" menu.

That gets the interaction model right before the visual redesign gets expensive.

The redesign succeeds when a reader can move from a sentence in the corpus to a
conversation with the braid to a durable formation without leaving the surface
or losing the thread.
