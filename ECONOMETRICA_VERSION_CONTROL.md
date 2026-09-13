# Reversible research edits

Workflow revision: 2026-09

Modified: 2026-09-13.

Use the authorization policy in [AGENTS.md](AGENTS.md). Git is optional; a project
can use file snapshots instead. Checkpoints must preserve file contents, not
merely record that a checkpoint was intended.

## Before and after a coherent edit

- Inspect `git status --short` and the relevant diff, or identify changed files
  in a project without Git. Distinguish existing work from the current task.
- Preserve the pre-edit contents using an existing commit, an isolated branch
  with a real snapshot, or a scoped file backup. A branch alone does not save
  uncommitted contents. Keep backups out of the manuscript and active prompt path.
- Make the authorized edit. Existing uncommitted changes are not automatically
  a blocker: work around them or merge carefully. Ask only when a real conflict
  or unclear author intent prevents safe progress.
- Review the resulting diff. Check claims, assumptions, citations and rendering
  affected by the edit, not every unrelated research stage.
- Record the material change, reason and recovery point in `research_log.md`.
  Reuse an existing revision/version log when appropriate; do not duplicate it.

Use branches or isolated folders when exploring alternatives that could replace
an author's selected model or manuscript. Reuse a suitable existing branch.
Commits, worktrees and tags follow the user's existing authorization and host
policy; do not ask again merely because a checkpoint operation has a stage name.

## Recovery and sharing

Before recovery, show the source version, exact affected files and what work
would be displaced. Prefer restoring a specific file or making a revert that
preserves history. Destructive deletion, history rewrites and overwriting
unpreserved work require explicit authorization for that action.

A local edit or checkpoint does not authorize publishing, submitting or pushing
private research. Follow the requested destination and sharing scope. Copying a
paper project to another computer should include its evidence and decisions;
verify machine-specific tool locations separately when needed.

The workflow repository's `.gitignore` protects paper-specific runtime files.
It is not a recommended blanket ignore policy for a researcher's own paper:
reproducible proofs, computation and selected decision records may belong in that
paper's version history. Preserve its existing ignore choices during upgrades.
