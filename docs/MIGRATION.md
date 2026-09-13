# Upgrade the original research workflow

This guide is needed once when upgrading a paper. It is not an extra research
stage. The seven protocol filenames remain stable, and all must belong to the
same revision. The new workflow uses questions and evidence to route work rather
than old D0-D7 or manuscript-stage gates.

This is an update to the original `viplee110/econ-theorist-ai` repository.
`Workflow revision: 2026-09` identifies a matching set of instructions; it is
not a release number or a designation for a separate research system.

## What stays familiar, and what changes

| Existing use | This update |
|---|---|
| Download/clone, copy files into a paper folder, root `AGENTS.md` | Same entry; install all seven matching protocols and the help files in [INSTALL](../INSTALL.md) |
| Initialize, continue, screen an idea, audit literature, review a paper, export a preview | Still understood as natural-language research requests |
| An explicitly delegated long run | Still supported within the stated scope and budget; no fixed sequence of old stages or required `final_ratification_report.md` |
| D0-D7, numbered stages, approval gates, candidate counts | Retired internal machinery; old stage-specific commands need interpretation by their intended research task |
| Old project records | Preserve and reuse evidence; new work need not recreate the old files |
| `-ToolRoot`, `-ConfigPath`, `-WriteStatus` | Parameters remain; saved status now defaults beside the script, not the user-level configuration folder |

The tool check requires seven matching protocols marked
`Workflow revision: 2026-09`. Bad or explicitly missing
configuration files fail clearly; an invalid configured tool path does not fall
back silently. Tools outside PATH may need explicit paths. Status text changed,
so external scripts parsing the old output need updating. Lean/Lake/LaTeX/Wolfram
are located without being launched by default; `-RunSmokeTests` explicitly adds
only the Wolfram arithmetic check. See [tool configuration](../TOOLCHAIN_README.md).

If using a submodule or symlinks, preserve a complete, resolvable set of protocol
paths. The old shortcut of exposing only `AGENTS.md` at the paper root is not
assumed compatible with every host. Use the documented complete installation.

## Preserve first

1. Identify the exact paper directory and current workflow version. Inspect
   pre-existing edits and retain a restorable snapshot of files being changed.
2. Compare the seven protocol files with the new versions. Preserve customized
   author instructions, merge the relevant changes, and record genuine conflicts.
3. Replace the distributed instructions as one coherent set. Also update the
   copied help files and this guide. Do not leave conflicting legacy instructions
   in another automatically loaded `AGENTS.md` or active prompt include.
4. Keep historical research artifacts and human decisions. Do not recursively
   delete or reorganize a paper's records as part of a workflow upgrade.

## Reuse evidence without inheriting old certification

| Existing artifact | Treatment |
|---|---|
| `project_state.md`, `active_context.md`, `discovery_state.md` | Build a compact `project_state.md` index, retaining old records as history |
| `idea_dossier.md`, `economic_logic_map.md`, topic lists | Use relevant material in `idea_dossier.md`; link large candidate history |
| `model_base_design.md`, `micro_example_note.md`, `heuristic_derivation.md`, `theorem_candidates.md` | Link or assemble the current `model_note.md`, retaining original evidence |
| `contribution_lock.md` | Treat as historical research intent and a pointer to actual author choices, not truth or a no-correction rule |
| `generality_ledger.md`, `assumption_ledger.md` | Retain meaningful assumptions, dependencies and boundaries in the model note or linked records |
| `literature_evidence_ledger.md`, literature notes | Reuse sources; check that the recorded source actually supports each active comparison |
| `human_decisions.md` | Preserve actual choices and scope; append corrections rather than overwriting history |
| `auto_decisions.md`, `final_ratification_report.md` | Keep AI-made choices distinct from human choices; summarize unresolved ones in current state/log |
| Field/target/style/architecture profiles | Reuse relevant preferences and evidence on demand; do not reopen automatic approval gates |
| Proofs, verification output, review and revision logs | Retain and reference needed evidence; do not load the entire archive routinely |

Legacy cross-project memory, including `researcher_profile.md` and method or
negative-knowledge libraries, is not loaded or copied automatically. Reuse
relevant entries within the authorized scope as pointers or provisional search
priors, never as evidence overriding current sources or proofs. Consider
explanations outside the researcher's usual preferences when breadth matters.
Preserve actual author constraints separately from inferred preferences.

For each active claim identify its source, model version, assumptions,
quantifiers, proof and independent-check evidence. A legacy `verified` label,
human approval or successful toolchain check cannot supply missing proof.
Preserve evidence-backed status; mark unsupported or incompatible certification
unresolved and say why. A model change makes dependent checks stale. It does not
erase the old proof under its original assumptions.

Separate historical goals, currently selected claims, and corrected alternatives.
Do not silently replace an author-selected contribution during migration. Within
already delegated scope, record AI choices as such. If a critical preference is
missing, prepare the concrete alternatives and request that choice; continue
unaffected work. Never synthesize a human approval from an old AI report.

## Resume check

- The current-state record identifies the selected model/version, or the live
  branches if none is selected yet, and the immediate economic uncertainty.
  Unresolved conflicts are visible.
- All active protocol files say `Workflow revision: 2026-09`; old rules occur only in
  historical material, not in automatic instructions or current examples.
- Existing citations, proofs and author edits are recoverable. No research
  data, logs or private files were removed or published.
- The next action uses the relevant activity document and evidence, with no
  demand to recreate obsolete gate/profile files.

## Rollback and experimental releases

The exact baseline before this redesign is
[`cc5f61254bb79e7436892e32ec88730ae14dd7f8`](https://github.com/viplee110/econ-theorist-ai/tree/cc5f61254bb79e7436892e32ec88730ae14dd7f8).
It is two commits after the published
[`v0.2.0` release](https://github.com/viplee110/econ-theorist-ai/releases/tag/v0.2.0).
The recovery tag `original-workflow-before-refresh-2026-09` identifies this exact
baseline, not a new release. Keep a source archive as an additional backup.
Publish the experiment on its own branch first if the main branch should stay
on the old workflow. A local tag or branch becomes available on GitHub only
after it is pushed.

Committing or pushing the workflow does not publish a GitHub release. Publish
the next release only after the maintainer explicitly authorizes that release
after evaluation.

If an experimental change is later merged into a shared branch, a
[Git revert](https://git-scm.com/docs/git-revert) can record a new commit that
reverses that change while retaining history. Identify the actual release
commit(s), preserve unrelated work and resolve any subsequent conflicts; a merge
commit needs the appropriate mainline parent. Avoid rewriting shared history.

For a paper, restore the captured instruction set as a whole. The workflow
repository cannot restore manuscript edits, untracked files or external settings
that were never saved there: preserve the paper's own snapshot before upgrading.
Keep new scientific findings and corrections; rolling back the workflow does
not make a refuted theorem valid again.
