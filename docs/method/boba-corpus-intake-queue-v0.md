# BOBA Corpus Intake Queue v0

**Purpose:** Turn loose generated documents into durable BOBA corpus material
without confusing private preservation, public GitHub corpus, and canonical
doctrine.

## Current Reading

The existing BOBA corpus already answers much of what "a life I love" means in
operational terms, but mostly at the governance level:

- resource humans toward lives of their own choosing;
- protect autonomy from coercive steering;
- keep Keith as orchestrator/Self, not a passive target;
- reduce administrative actuation burden without removing judgment;
- preserve local custody, inspectability, and privacy-first operation;
- require legibility, stoppability, handoffs, and recoverable steps before
  autonomy expands;
- judge BOBA by whether it makes Keith more capable of living a life he respects.

What the corpus does not yet contain is a full personal portfolio map of Keith's
projects, resources, body/house/tool realities, accounts, and desired cadence.
That map should be derived from stronger source documents where possible, not
invented from an offhand summary.

## Intake Rule

Use three stages. **Preserve is not promote.** `asterisms-only` is a valid
finished state.

1. **Preserve first in Asterisms.** Anything plausibly relevant but not yet
   curated should be registered through Porter/Asterisms. This keeps original
   bytes and provenance without claiming the document belongs in the public
   corpus.
2. **Triage mandatorily** (same day or next triage pass). Every new material
   gets an explicit **fate** in `~/asterisms/90-system/intake-triage.md`:

   | Fate | Meaning |
   |---|---|
   | `untriaged` | Illegal to leave past weekly review |
   | `asterisms-only` | Provenance / private / weak / disputed — done |
   | `promote-candidate` | Needs Keith before BOBA install |
   | `promoted` | Editable home in BOBA + `ast:` of installed version |
   | `defer-eclosion` | Real; not needed for invitation/launch week |
   | `surface-only` | Web/Salon/reader receipt; not core doctrine |

3. **Promote deliberately into BOBA** only from `promote-candidate` after
   review. Only documents that are public-safe, non-duplicative, and
   corpus-useful should be copied into this GitHub repo, indexed, committed,
   and pushed. **No auto-promote** from Salon/web collaboration into core.

The GitHub BOBA corpus is a durable public/shared rail, not a dumping ground.
The live Asterisms Home is the local continuity substrate.

## Current Loose-Document Decisions

| Source | Decision | Target |
|---|---|---|
| `/home/keith260601/alpha_angels_scheduler_smoketest_260607.md` | Promote. It is a useful BOBA scheduler/session record. | `docs/session-records/alpha-angels-scheduler-smoketest-260607.md` |
| `/home/keith260601/intake/exp0/exp0_result_260606.2200.md` | Promote. It is the compact result record behind the JEPA worked example. | `docs/session-records/vjepa-exp0-static-encoder-baseline-260606.md` |
| `/home/keith260601/docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md` | Preserve only. The BOBA repo already has a better version of this session record. | Asterisms record only |
| `/home/keith260601/REBOOT_RESUME_BOBA_260607.txt` | Preserve only. It is a useful historical breadcrumb but not corpus doctrine. | Asterisms record only |
| `docs/probe-set/archive/spec-superseded-draft.md` | Keep archived in the repo, but exclude from retrieval indexing. | `docs/probe-set/archive/` |

## Asterisms Registration IDs

These files were registered through Porter/Asterisms during the 2026-07-03
intake pass. The queue note itself may have a later installed-version
registration after this table was added.

| File | Material ID | Status |
|---|---|---|
| `docs/method/boba-corpus-intake-queue-v0.md` | `ast:material:20260703T213900Z-OYONHA` | promoted |
| `docs/session-records/alpha-angels-scheduler-smoketest-260607.md` | `ast:material:20260703T213900Z-RC4BBU` | promoted |
| `docs/session-records/vjepa-exp0-static-encoder-baseline-260606.md` | `ast:material:20260703T213900Z-HWB0T5` | promoted |
| `docs/probe-set/archive/spec-superseded-draft.md` | `ast:material:20260703T213900Z-ZZSXEY` | archived, excluded from retrieval index |
| `/home/keith260601/REBOOT_RESUME_BOBA_260607.txt` | `ast:material:20260703T213900Z-SJLFF4` | Asterisms-only |
| `/home/keith260601/docs/session-records/boba-session-record-260607-pipeline-and-retrieval.md` | `ast:material:20260703T213900Z-QQIWAE` | Asterisms-only duplicate/superseded |

## Intake Procedure

For any newly found generated document:

1. Register it through Porter:

   ```bash
   cd ~/asterisms-porter/porter
   python3 - <<'PY'
   from pathlib import Path
   import porter

   path = Path("/absolute/path/to/document.md")
   result = porter.register_file(
       path,
       source_kind="boba_candidate",
       source_label=path.name,
       origin_note="candidate BOBA corpus document",
   )
   print(result.as_dict())
   PY
   ```

2. **Set a fate** in `~/asterisms/90-system/intake-triage.md` (required).
   If the fate is `promote-candidate`, also note a tentative BOBA folder class:
   - `core` / `method` / `architecture` / `tooling` / `session-records` /
     `essays` / `manuscript`.

3. Before public promotion (`promote-candidate` → `promoted`), check:
   - Does it duplicate a stronger existing document?
   - Does it contain private/family/account/location details?
   - Is it source material or an AI summary of source material?
   - Is it needed for eclosion, or should it be `defer-eclosion`?

4. If promoted:
   - copy it into the correct BOBA folder;
   - rebuild/evaluate the retrieval index when appropriate;
   - commit and push the BOBA repo;
   - register the promoted BOBA file into Asterisms as the canonical installed
     version;
   - update the triage row to `promoted` with the BOBA path.

## Near-Term Corpus Gaps

- Fog writing: expected to enrich uncertainty/fog/wobbly-edge doctrine, but
  requires privacy review.
- Walk/manuscript material: likely important source stream, but public/private
  boundary is unresolved.
- Personal operating map: should be derived from existing careful source docs
  and Keith's explicit review, not synthesized prematurely.
- BOBA-to-Asterisms cross-reference: promoted BOBA docs should record their
  Asterisms material IDs in a later metadata layer.
