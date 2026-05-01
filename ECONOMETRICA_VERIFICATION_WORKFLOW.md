# Computational and Formal Verification Workflow for Economic Theory Papers

Version: 2026-05-01

Use this file whenever Codex derives, checks, repairs, or criticizes mathematical claims in an economics paper. This workflow is designed to reduce language-model hallucination by forcing derivations to interact with external tools, explicit assumptions, symbolic algebra, numerical checks, counterexample search, and, where feasible, formal proof assistants such as Lean 4.

This file complements:

- `ECONOMETRICA_DISCOVERY_WORKFLOW.md` for early topic and model discovery.
- `ECONOMETRICA_AI_HUMAN_WORKFLOW.md` for manuscript development and simulated review.
- `AGENTS.md` for project-level standing rules.

## Core Principle

The language model may propose a theorem, proof, or derivation, but it does not certify it. A mathematical claim becomes more credible only after it passes a layered verification process:

1. assumption extraction
2. hand derivation
3. symbolic or algebraic check
4. numerical sanity check
5. counterexample search
6. proof audit
7. optional formalization

Failure in any layer should be recorded, not hidden.

## Verification Artifacts

Maintain these files when doing mathematical work:

- `math_claims.md`: list of propositions, lemmas, comparative statics, and proof-dependent claims.
- `assumption_ledger.md`: assumptions, where they are used, and whether they are economic, technical, or suspiciously tailored.
- `derivation_notes.md`: hand derivations, algebra, FOCs, equilibrium conditions, and proof sketches.
- `verification_log.md`: tool runs, commands, outputs, failures, and interpretation.
- `counterexamples.md`: failed claims, numerical counterexamples, boundary cases, and parameter regions where results break.
- `formalization_notes.md`: Lean 4 or other proof-assistant attempts, formalizable lemmas, blockers, and informal-to-formal gaps.

## Tool Ladder

Use the strongest available tool that fits the claim.

### Layer 1 - Exact Algebra

Preferred tools:

- Python `sympy`
- Matlab Symbolic Math Toolbox
- Mathematica, if available
- manual algebra checked line by line

Use for:

- FOCs
- derivatives
- comparative statics
- algebraic simplification
- determinant/sign checks
- fixed point equations
- boundary cases

### Layer 2 - Numerical Sanity Checks

Preferred tools:

- Python `numpy`, `scipy`
- Matlab
- Julia
- grid search or random search scripts

Use for:

- equilibrium computation
- parameter sweeps
- sign checks
- monotonicity checks
- visualizing comparative statics
- searching for counterexamples
- finding suspicious boundary behavior

### Layer 3 - Optimization and Equilibrium Checks

Preferred tools:

- Python `scipy.optimize`
- Matlab optimization routines
- CVX/CVXPY for convex programs when appropriate
- custom best-response iteration for simple games

Use for:

- verifying equilibrium candidates
- checking uniqueness or multiplicity numerically
- testing deviations
- checking global versus local optima

### Layer 4 - Formal Verification

Preferred tools:

- Lean 4 with Mathlib
- Isabelle/HOL or Coq if already available

Use for:

- small clean lemmas
- order, monotonicity, continuity, convexity, fixed-point, or algebraic claims
- checking whether assumptions are sufficient

Do not expect Lean 4 to formalize an entire economics paper quickly. Use it to verify compact lemmas and expose missing assumptions.

## Stage V0 - Tool Inventory

Autonomy: Auto

Purpose:

Determine what verification tools are available in the local environment.

AI tasks:

- Check whether Python, Matlab, Octave, Julia, Lean 4, Lake, and relevant packages are available.
- Record results in `verification_log.md`.
- If a tool is unavailable, do not pretend it was used.
- If a tool requires setup, record exact setup instructions or blockers.

Output:

- `verification_log.md`

## Stage V1 - Claim and Assumption Extraction

Autonomy: Auto

Purpose:

Create a complete inventory of mathematical claims before checking them.

AI tasks:

- Create `math_claims.md`.
- Extract every theorem, proposition, lemma, corollary, comparative static, equilibrium claim, identification claim, welfare claim, and nontrivial proof-dependent statement.
- Create `assumption_ledger.md`.
- For each claim, list:
  - exact statement
  - location in manuscript
  - assumptions used
  - conclusion
  - proof status
  - tool-check status
  - counterexample status

Rule:

No claim should be treated as verified merely because it appears plausible.

## Stage V2 - Re-Derivation from Primitives

Autonomy: Auto, with Gate if foundational issues appear

Purpose:

Rebuild the result from the model primitives.

AI tasks:

- Restate primitives, timing, information, actions, payoffs, constraints, and equilibrium concept.
- Derive agent problems from primitives.
- Derive FOCs or best responses.
- Identify whether FOCs are sufficient or only necessary.
- Identify boundary cases.
- Identify global versus local optimum issues.
- State every assumption used in each step.

Stop if:

- The claim does not follow from the stated primitives.
- A hidden assumption is required.
- A boundary case reverses the result.
- The result is simply assumed.

## Stage V3 - Symbolic Verification

Autonomy: Auto

Purpose:

Use symbolic tools to check algebraic steps where possible.

AI tasks:

- Write minimal scripts or commands for symbolic checks.
- Check derivatives, simplifications, signs, discriminants, and closed-form solutions.
- Store scripts in a `verification/` folder when useful.
- Paste or summarize results in `verification_log.md`.

Rules:

- Keep symbolic checks minimal and focused.
- Do not overinterpret symbolic output.
- If a sign cannot be determined without assumptions, record the missing conditions.
- If symbolic simplification fails, try a simpler subproblem before adding assumptions.

## Stage V4 - Numerical Counterexample Search

Autonomy: Auto

Purpose:

Actively try to falsify the result.

AI tasks:

- Define admissible parameter ranges.
- Run grid search and random search over parameters.
- Check whether the predicted sign, monotonicity, equilibrium property, or welfare ranking holds.
- Test boundary cases and limiting cases.
- Save failures in `counterexamples.md`.

Rules:

- Counterexample search should be adversarial.
- A numerical pass does not prove the theorem.
- A single valid counterexample kills or narrows the theorem.
- If counterexamples occur only outside economically relevant regions, record the needed domain restrictions.

## Stage V5 - Proof Audit

Autonomy: Checkpoint

Purpose:

Audit the informal proof after symbolic and numerical checks.

AI tasks:

- Match every line of proof to a stated assumption or previous result.
- Identify gaps:
  - existence
  - uniqueness
  - continuity
  - compactness
  - convexity or concavity
  - monotonicity
  - equilibrium selection
  - differentiability
  - interchange of limits, derivatives, or expectations
  - boundary behavior
- Classify each gap as:
  - fixable by exposition
  - fixable by adding a mild assumption
  - serious but maybe repairable
  - fatal to current result

Human gate:

The human must approve any new assumption that affects economics, novelty, or interpretation.

## Stage V6 - Formalization Triage

Autonomy: Checkpoint

Purpose:

Decide whether any part should be formalized in Lean 4 or another proof assistant.

AI tasks:

- Identify compact lemmas suitable for formalization.
- Rewrite them in formal-friendly language.
- Separate mathematical content from economic interpretation.
- Record candidate lemmas in `formalization_notes.md`.

Good Lean candidates:

- algebraic identities
- monotonicity of simple functions
- convexity or concavity of simple functions
- order arguments
- fixed assumptions over real numbers
- finite-game or finite-action lemmas if small

Poor Lean candidates:

- long prose proofs
- large equilibrium existence arguments with many economic definitions
- claims depending on undefined economic intuition
- results requiring extensive custom theory before the main lemma

## Stage V7 - Formal Verification Attempt

Autonomy: Auto if Lean is installed, otherwise record setup blocker

Purpose:

Try to formalize selected compact lemmas.

AI tasks:

- Create a `formal/` or `lean/` folder only if appropriate.
- Create minimal Lean files for selected lemmas.
- Prefer small lemmas over ambitious full-theorem formalization.
- Record what Lean verifies and where it fails.
- Do not claim formal verification unless the proof assistant accepts the file.

Rule:

Partial formalization is useful even when it fails, because failure often exposes hidden assumptions or imprecise statements.

## Stage V8 - Verification Report

Autonomy: Auto

Purpose:

Summarize what is known after checks.

AI tasks:

- Update `verification_log.md`.
- Update `counterexamples.md`.
- Update `assumption_ledger.md`.
- Write a final section with:
  - verified claims
  - partially verified claims
  - claims with counterexamples
  - claims needing human proof work
  - assumptions requiring human approval
  - recommended theorem revisions

## Decision Rules

- If symbolic algebra contradicts the proof, revise the proof or theorem.
- If numerical search finds a valid counterexample, narrow or kill the theorem.
- If a theorem requires a new assumption, the human must decide whether the assumption is economically acceptable.
- If the proof uses a hidden selection, regularity, or boundary condition, state it explicitly.
- If formalization fails because definitions are imprecise, improve the informal theorem statement.

## Prompt Templates

### Start Tool Inventory

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. Run Stage V0. Check what verification tools are available locally: Python, sympy, numpy, scipy, Matlab, Octave, Julia, Lean 4, and Lake. Create verification_log.md and report exact blockers. Do not modify the manuscript.
```

### Extract Claims

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. Run Stage V1. Extract all mathematical claims from the manuscript into math_claims.md and create assumption_ledger.md. Do not attempt to prove or edit yet.
```

### Verify One Proposition

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. Verify Proposition [X]. Run Stages V2 through V5 for this proposition only. Re-derive from primitives, check algebra symbolically if possible, run numerical counterexample search if applicable, audit the proof, and update verification_log.md, derivation_notes.md, counterexamples.md, and assumption_ledger.md. Stop before changing theorem assumptions.
```

### Search for Counterexamples

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. Run Stage V4 for Claim [X]. Treat the claim adversarially. Define admissible parameter ranges, run grid/random search using available tools, test boundary cases, and write all failures or near-failures to counterexamples.md. A numerical pass is not a proof.
```

### Lean Triage

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. Run Stage V6 for the current theorem list. Identify which lemmas are realistic candidates for Lean 4 formalization, rewrite them in formal-friendly language, and create formalization_notes.md. Do not claim formal verification.
```

### Lean Attempt

```text
Read ECONOMETRICA_VERIFICATION_WORKFLOW.md. If Lean 4 and Lake are installed, run Stage V7 on the selected compact lemmas. Create minimal Lean files, run the checker, and record accepted lemmas and blockers in formalization_notes.md. If Lean is not installed, record the setup blocker and do not simulate proof-assistant output.
```

