# Project Instructions

This folder contains an economics paper or research workflow targeting Econometrica-level development.

Default entry point: first read `ECONOMETRICA_ORCHESTRATOR.md` when it exists. Use it to route broad user requests to the correct workflow module and stage, so the user does not need to remember stage numbers or file names.

For pre-manuscript topic discovery, model generation, early derivation, and idea kill tests, first read `ECONOMETRICA_DISCOVERY_WORKFLOW.md` when it exists in this project.

For long-horizon human-AI manuscript development, first read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md` when it exists in this project. Treat it as the stage-gated collaboration protocol for idea testing, contribution locking, manuscript revision, simulated review, and human decision checkpoints.

For mathematical derivations, theorem checks, comparative statics, equilibrium calculations, counterexample searches, numerical examples, symbolic algebra, or formal proof attempts, first read `ECONOMETRICA_VERIFICATION_WORKFLOW.md` when it exists in this project.

For version control, checkpoints, git diffs, branches, worktrees, commits, tags, rollback, and protection of human edits, first read `ECONOMETRICA_VERSION_CONTROL.md` when it exists in this project.

## Local Verification Toolchain

- Use `.venv\Scripts\python.exe` for Python-based symbolic algebra, numerical checks, counterexample searches, plots, and SMT checks.
- Use `.tools\elan\bin\lean.exe` and `.tools\elan\bin\lake.exe` for Lean 4 verification. Set `ELAN_HOME` to `.tools\elan` before invoking them.
- Mathematica 13.0 is installed at `C:\Program Files\Wolfram Research\Mathematica\13.0`. Use `wolframscript.exe` for symbolic checks. The default sandbox may not be able to read WolframScript's user configuration directory, so Mathematica commands may require approval to run outside the sandbox. Do not claim Mathematica verification unless the command succeeds and its output is recorded.
- Run `.\verify_toolchain.ps1` to test the local toolchain.

## Core Rules

- Preserve mathematical correctness, citation integrity, and author intent.
- Do not invent citations, proofs, data results, robustness checks, theorem statements, numerical results, or claims.
- If a citation, proof, result, robustness check, or interpretation requires author verification, write it as a precise TODO in `risk_register.md` instead of fabricating it.
- Prefer direct edits to LaTeX source files when the source can be improved safely.
- Keep `revision_log.md` updated throughout the task.
- Compile the paper after meaningful edits when possible.
- Treat simulated referee acceptance as a diagnostic benchmark only, never as a real publication guarantee.

## Human Gates

- Stop for human approval before changing the central question, main theorem, model primitives, assumption set, claimed novelty, empirical interpretation, or target-journal positioning.
- Do not continue polishing if the main objection is contribution, identification, or economic relevance. Return to idea testing or contribution locking.
- Use `ECONOMETRICA_AI_HUMAN_WORKFLOW.md` to decide which stage should be run next.
- Use `ECONOMETRICA_ORCHESTRATOR.md` as the default router for broad or ambiguous research instructions.
- Use `ECONOMETRICA_DISCOVERY_WORKFLOW.md` before a full manuscript exists or when the task is to discover topics, generate tractable models, test derivations, or run early-stage kill tests.
- Use `ECONOMETRICA_VERIFICATION_WORKFLOW.md` whenever a mathematical claim needs derivation, symbolic checking, numerical testing, counterexample search, proof audit, or formal verification.
- Use `ECONOMETRICA_VERSION_CONTROL.md` before and after meaningful edits, long-running review sessions, and rollback requests.
- Run version control automatically in the background for meaningful edits: status check, safe AI branch when the git tree is clean, checkpoint logging, and post-edit diff summary. Ask only for commits, tags, worktrees, rollback, destructive actions, or dirty pre-existing human changes.
