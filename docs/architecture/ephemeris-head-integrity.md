# Candidate Design: Ephemeris Head Integrity & Tail-Truncation Detection

**Status:** Accepted v0 baseline; v1 automation deferred
**Date:** 2026-07-04
**Updated:** 2026-07-05
**Score:** `eph:score:20260705T023337Z-3782` (closed)
**Concern:** Find the smallest trustworthy treatment of Ephemeris head integrity
**Asterisms record:** design note `ast:material:20260705T024146Z-A310C6`; first literal head anchor `ast:material:20260705T025112Z-154K6Q`

---

## 1. The Tail-Truncation Vulnerability

Because `ephemeris-log.jsonl` is a sequential append-only file secured by a parent-hash chain:
*   Any modification in the middle of the log breaks the hash chain.
*   Any deletion in the middle of the log breaks the hash chain.
*   **Vulnerability:** If an agent or attacker deletes the last $N$ lines (tail truncation), the remaining log has a perfectly valid hash chain. A reader scanning the file from genesis will see a valid log but will be unaware that recent events were erased.

To detect tail truncation, the system must reference an **external anchor** containing the expected log head hash.

---

## 2. Candidate Solutions

| Solution | Mechanism | Complexity | Dependencies | Trust Grade |
|:---|:---|:---|:---|:---|
| **A. Defer & De-prioritize** | Defer the problem, accept the risk, keep it documented. | Zero | None | **Low** (Truncation goes undetected) |
| **B. Git-Commit Anchoring** (Recommended v0) | Every session handoff and git commit records the current head hash in tracked prose (`HANDOFF.md` or git commit message). | Very Low | Git history | **High** (Git commit hashes are cryptographically secure and pushed to remote origin) |
| **C. `ephemeris anchor` command** (Planned v1) | Implement a command that registers the current log head hash directly as an immutable material inside Asterisms. | Medium | Asterisms system API | **Very High** (Sovereign local database authority) |

---

## 3. The Smallest Trustworthy Move (v0 Baseline)

We select **manual external anchoring** as the immediate v0 baseline: record the
current Ephemeris head hash in an inspectable outside witness. In practice, the
first v0 witness is an Asterisms material, supplemented by prose/git references
where useful. Solution C (`ephemeris anchor`) remains the planned transition for
v1 automation.

First literal head anchor:

- Asterisms material: `ast:material:20260705T025112Z-154K6Q`
- Event count: `11`
- Latest event: `eph:event:20260705T024208Z-16FC`
- Head hash: `be448b30598235c81b0f90789555813aa171e071936cb4289ff5828d54d98bfd`

### The Protocol (Manual External Anchoring)
1.  **Handoffs:** At the end of every workspace session, the active agent (or user) running the handoff must output the current Ephemeris log head hash:
    ```bash
    tail -n 1 ~/.ephemeris/ephemeris-log.jsonl | python3 -c 'import json,sys; print(json.load(sys.stdin)["hash"])'
    ```
2.  **External Witness:** The agent records this head hash in a durable outside
    witness: preferably an Asterisms head-anchor record; otherwise tracked prose
    or a commit message for the current session.
3.  **Sanity Check:** When a new session starts, the next agent:
    *   Reads the latest Asterisms head-anchor record, tracked prose, or commit
        message to get the expected head hash.
    *   Runs the local CLI `ephemeris now` (which validates the log's internal hash chain).
    *   Compares the latest event hash against the expected anchor.
    *   If the local log cannot reach the expected anchor, the log has been
        truncated or replaced relative to that checkpoint and the session should
        stop for human review.

### Why this is the right v0 move:
*   It requires **zero new code** or dependencies in the v0 CLI.
*   It is **transparent and inspectable** with ordinary file reads, git history,
    and Asterisms records.
*   It keeps Ephemeris time anchored outside itself without turning the v0 CLI
    into an Asterisms client before the workflow has stabilized.

---

## 4. Path Forward for v1 (`ephemeris anchor`)

Once the basic workflow stabilizes, v1 will automate this by adding an `ephemeris anchor` command:
1.  **Command:** `ephemeris anchor --ast-id <ast:id>` or `ephemeris anchor`
2.  **Seam:** The CLI calls the Asterisms Registry API to preserve a lightweight anchor record containing the head hash, returning an `ast:material:` ID.
3.  **Log Entry:** The Ephemeris log appends an `anchor` event referencing that `ast:` ID:
    ```json
    {"type": "anchor", "payload": {"ast_id": "ast:material:..."}}
    ```
    This completes the loop: Ephemeris time is anchored into Asterisms space.
