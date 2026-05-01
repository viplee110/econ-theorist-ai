# Econometrica Research Orchestrator

Version: 2026-05-01

This is the single entry point for the Econometrica research system. When the user gives a broad instruction, do not require them to remember workflow file names or stage numbers. Read this file, infer the task type, inspect available state files, choose the next appropriate module, and proceed until a human gate is reached.

The system is made of four modules:

- `ECONOMETRICA_DISCOVERY_WORKFLOW.md`: topic discovery, model generation, first-pass derivation, early kill tests.
- `ECONOMETRICA_VERIFICATION_WORKFLOW.md`: symbolic checks, numerical counterexample search, proof audit, Lean/Mathematica/Python verification.
- `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`: manuscript development, contribution lock, simulated review, referee-guided revision, submission readiness.
- `ECONOMETRICA_VERSION_CONTROL.md`: git status, checkpoints, branches/worktrees, diffs, commits, tags, rollback, and protection of human edits.
- `TOOLCHAIN_README.md`: local Python, Lean, Mathematica, and verification tool usage.

`AGENTS.md` contains standing project rules and should already point here.

## Default Behavior

When the user asks for research help, follow this sequence:

1. Inspect the local folder and current state files.
2. Infer whether the task is discovery, verification, manuscript revision, simulated review, or toolchain work.
3. For meaningful edits or long-running sessions, read `ECONOMETRICA_VERSION_CONTROL.md` and run automatic version-control setup in the background.
4. State the selected module and stage in one short sentence.
5. Execute the stage directly if it is safe.
6. Stop at human gates.
7. Update the relevant state/log files before stopping.
8. For meaningful edits, summarize the git diff or version-control state before finishing.

Do not ask the user to choose a stage unless the routing is genuinely ambiguous or the next step changes the core contribution, theorem, model, assumptions, novelty claim, or target journal.

## Universal User Commands

The user should be able to use short commands like these:

```text
I want to discuss a new topic. Start the system.
```

```text
I have a rough idea. Help me evaluate it.
```

```text
Continue from the current state.
```

```text
Check the math carefully.
```

```text
Run a simulated Econometrica review.
```

```text
Revise according to the latest referee report.
```

```text
Prepare a final readiness report.
```

The assistant should translate these commands into the correct workflow and stage.

## State Files to Inspect First

Before routing, inspect whichever of these files exist:

- `project_state.md`
- `discovery_state.md`
- `idea_dossier.md`
- `contribution_lock.md`
- `manuscript_map.md`
- `model_candidates.md`
- `derivation_notes.md`
- `math_claims.md`
- `verification_log.md`
- `counterexamples.md`
- `risk_register.md`
- `revision_log.md`
- latest `referee_reports/round_N.md`
- `final_report.md`
- `version_log.md`

If no state file exists, begin with intake:

- no manuscript or no clear paper files: Discovery D0.
- manuscript exists: Manuscript Stage 0.

## Routing Table

Use this table to choose the module.

### New Topic or Unknown Direction

Triggers:

- "new topic"
- "find a topic"
- "what should I work on"
- "explore a field"
- "I only know the broad area"
- "AI helps me enumerate research directions"

Route:

- Read `ECONOMETRICA_DISCOVERY_WORKFLOW.md`.
- Run D0 and D1.
- If the user gave a broad field, use Field mode.
- If the user gave no field, use Open mode.
- Create or update `discovery_state.md` and `topic_longlist.md`.
- Stop at the first human gate unless the user explicitly asks for screening too.

### Rough Idea

Triggers:

- "I have an idea"
- "rough idea"
- "possible mechanism"
- "can this become a paper"
- "evaluate this idea"

Route:

- Read `ECONOMETRICA_DISCOVERY_WORKFLOW.md`.
- Run D0 through D2 in Idea mode.
- Create or update `discovery_state.md`, `topic_longlist.md`, and `topic_shortlist.md`.
- Stop for human choice among candidates.

### Model Generation

Triggers:

- "generate a model"
- "tractable model"
- "model variants"
- "turn this idea into a model"

Route:

- Read `ECONOMETRICA_DISCOVERY_WORKFLOW.md`.
- Run D4.
- Create or update `model_candidates.md`.
- If candidate models already exist, ask only if the user wants new variants or derivation.

### First-Pass Derivation

Triggers:

- "derive"
- "solve the model"
- "main proposition"
- "comparative static"
- "equilibrium conditions"

Route:

- Read `ECONOMETRICA_DISCOVERY_WORKFLOW.md` and `ECONOMETRICA_VERIFICATION_WORKFLOW.md`.
- Run Discovery D5 plus Verification V1-V4 as needed.
- Create or update `derivation_notes.md`, `math_claims.md`, `assumption_ledger.md`, `verification_log.md`, and `counterexamples.md`.
- Use Python first for quick symbolic/numerical checks; use Mathematica if symbolic assumptions or inequalities benefit from it; use Lean only for compact lemmas.

### Mathematical Verification

Triggers:

- "check the proof"
- "verify the theorem"
- "find counterexamples"
- "use Python"
- "use Mathematica"
- "use Lean"
- "formal verification"

Route:

- Read `ECONOMETRICA_VERIFICATION_WORKFLOW.md`.
- Run V0 if tool availability is unknown.
- Run V1 if claims are not extracted.
- For a named theorem/proposition, run V2-V5 for that claim.
- Use V6-V7 only if a compact lemma is suitable for formalization.
- Stop before changing theorem assumptions or economic interpretation.

### Manuscript Intake

Triggers:

- "here is my paper"
- "open this paper folder"
- "start revising"
- "analyze this draft"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 0.
- Create or update `project_state.md` and `manuscript_map.md`.
- Stop for confirmation before judging or editing if this is the first pass.

### Idea Kill Test for a Paper

Triggers:

- "kill test"
- "is this Econometrica-level"
- "does this deserve Econometrica"
- "judge the contribution"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 1.
- Do not edit the manuscript.
- Create or update `idea_dossier.md`.
- Stop at the human gate.

### Contribution Lock

Triggers:

- "lock the contribution"
- "central question"
- "non-substitutable insight"
- "reader belief update"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 2.
- Create or update `contribution_lock.md`.
- Stop for approval.

### Deep Manuscript Revision

Triggers:

- "revise the paper"
- "improve the draft"
- "write the introduction"
- "make it Econometrica-ready"
- "section-by-section revision"

Route:

- If `contribution_lock.md` does not exist, recommend Stage 1 or 2 first.
- If contribution is locked, read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stages 3, 4, and 6 as appropriate.
- Use `ECONOMETRICA_VERIFICATION_WORKFLOW.md` for mathematical claims.
- Compile when possible.
- Update `revision_log.md` and `risk_register.md`.
- Stop if a foundational issue appears.

### Simulated Review

Triggers:

- "simulate referees"
- "review like Econometrica"
- "run editorial board"
- "give referee reports"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 7.
- Do not edit the manuscript in this pass unless explicitly asked.
- Write `referee_reports/round_N.md`.
- Update `risk_register.md`.
- Stop for human decision.

### Referee-Guided Revision

Triggers:

- "revise according to referee"
- "respond to review"
- "fix round_N"
- "use the latest referee report"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 8 using the latest referee report.
- Create a revision plan tied to objections.
- Edit only where safe.
- Stop before conceptual changes that require human approval.

### Final Readiness

Triggers:

- "final check"
- "ready to submit"
- "submission readiness"
- "final report"

Route:

- Read `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.
- Run Stage 10.
- Do not make major conceptual edits.
- Write or update `final_report.md`.

### Version Control and Rollback

Triggers:

- "checkpoint"
- "commit"
- "diff"
- "version"
- "rollback"
- "回退"
- "compare rounds"
- "branch"
- "worktree"

Route:

- Read `ECONOMETRICA_VERSION_CONTROL.md`.
- For status/checkpoint, run G0-G1.
- For ordinary editing sessions, use the default automation policy: status check, safe AI branch if clean, checkpoint logging, and post-edit diff summary.
- For post-edit review, run G3.
- For commits/tags, run G4-G5 and ask approval.
- For rollback, run G6 and ask before executing destructive commands.

## Auto-Continue Rules

The assistant may automatically proceed from:

- D0 to D1 when the user asks for new-topic exploration.
- D1 to D2 when the user explicitly asks for screening.
- D4 to D5 when the user explicitly asks to solve or derive.
- V1 to V4 for a named mathematical claim.
- Stage 3 to Stage 6 after contribution lock is approved.
- Stage 7 to Stage 8 only if the user explicitly asks to revise according to the report.

The assistant must stop at gates involving:

- target journal choice
- central research question
- main theorem
- model primitives
- assumption set
- novelty claim
- economic interpretation
- decision to submit, pivot, retarget, split, or abandon

## Current-State Continuation

When the user says "continue" or "按系统继续":

1. Inspect the state files.
2. Identify the most recent completed stage.
3. Identify whether a human gate is awaiting a decision.
4. If a gate is awaiting a decision, summarize the decision needed and stop.
5. If no gate is pending, recommend and run the next safe stage.

Priority order for continuation:

1. Resolve pending human gate.
2. Verify unresolved mathematical claims.
3. Address fatal risks in `risk_register.md`.
4. Continue the current module's next stage.
5. If unclear, run an intake/status reconstruction pass.

## Minimal Prompt the User Can Use

For most work, the user can simply say:

```text
Read ECONOMETRICA_ORCHESTRATOR.md and proceed according to the system. My task is: [brief description].
```

If this file is referenced by `AGENTS.md`, the user can usually shorten this to:

```text
按系统处理：[brief description]
```

## Response Style

At the beginning of a routed task, the assistant should say only:

```text
I will route this to [module] [stage] because [short reason].
```

Then execute. Avoid dumping the whole workflow back to the user unless asked.
