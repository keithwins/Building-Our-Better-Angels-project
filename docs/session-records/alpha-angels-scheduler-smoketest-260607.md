# Alpha Angels / Hermes Scheduler Smoke Test — 2026-06-07

Result: PASS after profile-localization fix.

Confirmed:
- `hermes kanban init` created the DB.
- `gpu` profile exists.
- `kanban.max_in_progress_per_profile: 1` is set globally.
- Gateway foreground mode works under WSL via `hermes gateway run`.
- Dispatcher picked up ready task assigned to `gpu`.
- First smoke card `t_86c647a4` failed usefully:
  - `gpu` profile was not yet pinned to local model.
  - Worker attempted Gemini and hit quota.
  - Card blocked after one failure due to `--max-retries 1`.
- After copying config into `~/.hermes/profiles/gpu/config.yaml` and patching key auxiliary slots to local custom Qwen/Ollama:
  - `hermes profile show gpu` reported `qwen3-8b-64k:latest (custom)`.
  - Second smoke card `t_77c7ec76` completed successfully.
  - Worker ran `ollama list`, `ollama run qwen3-8b-64k:latest 'Hello'`, and called `kanban_complete`.

Interpretation:
Alpha Angels now has a working local card-driven dispatch loop with a GPU-designated profile, local-model routing, visible failure, and correct completion protocol.

Remaining caution:
Do not treat this as overnight-ready yet. Need to test:
- two simultaneous gpu cards to confirm profile serialization;
- one gpu card plus one default/light card to see concurrency behavior;
- a harmless long-running task with `--max-runtime`;
- whether approval gates stall unattended operation.

## Runtime cap test

Result: PASS.

Confirmed:
- Created a harmless long-running `gpu` task with `--max-runtime 30s`.
- Hermes stopped the task after it exceeded the runtime cap.
- Because `--max-retries 1` was set, the task ended blocked after the first failed attempt.

Interpretation:
Alpha Angels now has confirmed bounded execution for GPU-assigned cards. This is the core protection against unattended runaway jobs.

## Serialization test

Result: PASS.

Confirmed:
- Created two `gpu` cards simultaneously.
- Hermes ran one card while leaving the second in `ready`.
- After the first completed, the second was allowed to run.
- `kanban.max_in_progress_per_profile: 1` successfully prevents overlapping `gpu` tasks.

Interpretation:
Alpha Angels now has confirmed GPU-serial dispatch. This is the core protection against accidentally double-booking the 5070 Ti.

## Cross-profile concurrency test

Result: PASS.

Confirmed:
- Created one `gpu` card and one `default` card simultaneously.
- Hermes ran both at the same time.
- `kanban.max_in_progress_per_profile: 1` means one running task per profile, not one task globally.

Interpretation:
Alpha Angels can serialize heavy GPU work while still allowing a separate lightweight/default worker to run in parallel.

## Grounded probe-set spec attempt

Result: INFRASTRUCTURE PASS, CONTENT FAIL / WEAK.

Confirmed:
- Persistent workspace worked.
- Task `t_58ae9a01` wrote `/home/keith260601/boba_work/probe_set_mve_spec_260607/spec.md`.
- Worker completed normally and preserved artifact.

Content assessment:
- Output was too generic to be trusted as BOBA instrumentation.
- It used weak/non-grounded candidate models and invented `test_mve.py`.
- It copied category labels from the prompt but did not produce real probe material.

Conclusion:
Do not ask the worker to invent BOBA probe substance from a broad prompt. Provide a hand-authored BOBA seed corpus first, then assign Hermes the narrower job of turning that seed into files, scripts, schemas, and executable cards.

## File-writing approval gate test

Result: PASS / EXPECTED BLOCK.

Confirmed:
- Task `t_9a1e767f` attempted to write persistent BOBA probe-set files.
- Hermes blocked the task instead of silently modifying files without approval.
- No expected output files were written.
- Existing workspace files remained limited to `seed.md` and the earlier weak `spec.md`.

Interpretation:
File-mutating Kanban work is gated by approval. This is good for safety and auditability, but means unattended artifact-writing jobs require either an approved workflow, a different command style, or human-in-the-loop approval.

## Manual BOBA seed operationalization

Result: PASS.

Confirmed:
- Worker card `t_9a1e767f` remained blocked after tool/approval confusion and false completion narration.
- Filesystem ground truth showed it had not created the requested files.
- We manually created the first real BOBA-grounded corpus files:
  - `categories.yaml`
  - `reference_texts.jsonl`
  - `contrast_texts.jsonl`
  - `implementation_plan.md`
- Corpus currently contains 10 BOBA-positive reference anchors and 10 nearby contrast anchors.

Interpretation:
The scheduler substrate works, but BOBA corpus substance should initially be authored or closely supervised by Keith/ChatGPT. Hermes can be used for validation and execution after the seed artifacts exist.

## BOBA corpus validation card

Result: PASS.

Confirmed:
- Validation card `t_ec8899ae` completed.
- It ran as a non-mutating inspection card.
- Workspace file set remained stable after validation.
- This is the right role for Hermes at this stage: validate and inspect BOBA-grounded artifacts, not invent the core corpus.

Interpretation:
Alpha Angels can now run BOBA-relevant validation work against persistent local artifacts.

## BOBA corpus validation card

Result: PASS WITH CAVEAT.

Confirmed:
- Validation card `t_ec8899ae` completed.
- It confirmed:
  - `categories.yaml` is valid YAML with 10 categories.
  - `reference_texts.jsonl` contains 10 parseable entries.
  - `contrast_texts.jsonl` contains 10 parseable entries.
  - Every category has matching reference and contrast entries.
  - No placeholder strings were found.

Caveat:
- The worker attempted environment mutation during validation:
  - `pip install pyyaml`
  - `sudo apt install -y python3-yaml` then timed out.
- Future validation cards should explicitly say: do not install packages, do not use sudo, do not modify the Python environment.

Interpretation:
The corpus files passed structural validation. Hermes is useful for inspection, but even inspection cards need explicit "no install / no environment mutation" constraints.

## First BOBA probe-set MVE run

Result: PASS.

Confirmed:
- Created and ran `embed_probe_set.py` manually inside dedicated venv `~/venvs/boba-probes`.
- Installed `sentence-transformers` and `pyyaml` inside that venv, not system Python.
- Downloaded `sentence-transformers/all-MiniLM-L6-v2`.
- Embedded 10 BOBA-positive reference anchors and 10 nearby contrast anchors.
- Wrote:
  - `results.json`
  - `similarity_matrix.csv`
  - `report.md`

Interpretation:
The BOBA probe-set MVE now exists as a real local artifact, not just a plan. This is an infrastructure MVE and coordinate-surface prototype, not proof of alignment.
