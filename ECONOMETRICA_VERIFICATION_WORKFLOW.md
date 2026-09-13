# Verification for Economic Theory Research

Workflow revision: 2026-09

Modified: 2026-09-13.

Use this protocol to derive, check, or repair mathematical claims. [AGENTS.md](AGENTS.md) defines global priority, authorization, and scientific integrity. Verification can occur during [discovery](ECONOMETRICA_DISCOVERY_WORKFLOW.md) or [writing](ECONOMETRICA_AI_HUMAN_WORKFLOW.md); it does not require passing a separate model-approval sequence.

Use independent checking when a central result or a disputed proof warrants it, following [the panel protocol](ECONOMETRICA_PANEL_PROTOCOL.md). The purpose is to test the mathematics, not to turn agreement among agents into proof or to infer economic importance from correctness.

## Bind claims to their evidence

Keep the current claim records in `model_note.md`. Link long proofs, scripts, and outputs under `verification/` only when needed. Record material checks and changes in `research_log.md`; do not create a separate ledger for every checking technique.

For each consequential claim, record:

```text
Claim ID and model version:
Exact statement, including domain and quantifiers:
Assumptions, definitions, and equilibrium/selection concept:
Dependencies on other claims or external results:
Proof status: conjecture / proof sketch / proved / refuted / unresolved
Proof or disproof location and scope:
Independent check: not run / pass / gap, with checker and evidence location
Computational or formal evidence: type, scope, result, and location
Economic interpretation and its limits:
```

`Proved` means a complete proof is available for the stated claim; it is not shorthand for plausibility, a successful simulation, or reviewer consensus. A proof sketch or a partially formalized lemma must not acquire the status of the full theorem. Record limitations of an independent check explicitly.

Keep truth-critical conditions in the statement or an explicitly referenced assumption block. Explanation and intuition can follow it. A shorter statement is not an improvement if it changes the theorem's meaning.

When primitives, assumptions, definitions, quantifiers, or dependent claims change, mark affected checks as needing revalidation and retain the prior version. A proof may remain valid for its old statement; do not silently transfer its status to a new one. Imported records labeled “verified” need their exact statement and supporting evidence checked before reuse.

A prior independent `pass` belongs to its original claim and model version. For a changed statement, keep that result as history and record the current check as `not run` until checked again, or `gap` if a defect is known. Its proof status is `unresolved` until the evidence has been assessed for that statement. Unchanged claims and their evidence keep their status.

## Select checks that address the actual risk

Inspect the relevant model, claims, and existing evidence first. For research development, understand the mechanism or analytical purpose and an appropriate minimal example, application, or boundary case. For an explicitly mechanical request, verify the given model directly without manufacturing a research-value assessment.

Choose checks based on the claim and failure modes. This is not a mandatory ladder through every tool. Check the availability of tools needed for the selected task; do not inventory or install an entire stack on each run. Use project-configured runtimes when available and record a missing tool as a limitation.

| Check | Suitable use | What it does not establish |
|---|---|---|
| Re-derivation | Rebuild reasoning from primitives and expose missing assumptions. | An unchecked derivation is not independent verification. |
| Symbolic algebra | Derivatives, identities, simplifications, closed-form candidates. | Simplification alone does not prove domain, sign, or equilibrium claims. |
| Numerical or optimization checks | Feasibility, deviations, parameter regions, suspicious boundaries. | Search success or failure does not prove a universal statement. |
| Proof audit | Sufficiency, quantifiers, dependence, limits, selection, and global arguments. | Reviewer agreement does not fill an unresolved gap. |
| Formal proof assistant | Precisely encoded claims within a checked formal environment. | A checked lemma does not establish the full economic theorem or interpretation. |

Use tools already available, such as SymPy for exact algebra, NumPy/SciPy or equivalent numerical tools, an appropriate optimizer, or Lean/another proof assistant for suitable claims. Manual checking remains useful when a tool adds little. Record what was actually run.

## Re-derive and audit the logic

Restate the primitives and solution concept relevant to the claim. Derive behavior from objectives and constraints, rather than assuming a candidate solution is an equilibrium. Check, as applicable:

- whether first-order conditions are necessary, sufficient, or neither at boundaries;
- feasibility, global versus local optimality, and profitable deviations;
- existence versus uniqueness, multiplicity, and equilibrium selection;
- continuity, compactness, convexity, differentiability, and integrability where invoked;
- interchange of limits, derivatives, maximization, and expectations;
- the domain and quantifiers of comparative statics or welfare comparisons;
- the applicability of imported theorems and each proof dependency.

State where assumptions enter. Distinguish a condition used by the current proof from a condition known to be necessary for the claim. A proof gap does not itself refute a theorem; a valid counterexample does. If a purported complete proof has an unresolved gap, remove its `proved` status while preserving the statement as unresolved.

An independent checker should reconstruct the decisive argument from the statement and primitives before relying on the original proof when feasible. If the same derivation or model context was shared, describe that limit to independence. Audit results are evidence about the proof, not a vote on truth.

## Use computation reproducibly

For a material computational check, preserve the minimal script or command, relevant tool/version information, input domain, tolerances, seed when random, output or failure, and interpretation. Link it to the claim ID and model version. Avoid rerunning unchanged checks unless a new concern justifies it.

For symbolic work, supply domain assumptions, track excluded denominators and branches, and check signs or roots under the actual restrictions. A symbolic expression with unspecified assumptions cannot resolve an economic sign claim.

For numerical work, justify the tested parameter region, inspect boundaries and limiting cases where relevant, and report coverage. Check feasibility, solver convergence, residuals, and sensitivity to tolerances or starting values before interpreting a result. Local solver convergence is not evidence of uniqueness or global optimality.

Search for counterexamples deliberately when feasible. A candidate numerical violation should be checked for admissibility and numerical error, preferably by exact calculation or a reliable independent argument. If that validation is incomplete, label it a suspected counterexample and downgrade confidence without asserting a disproof.

No counterexample found means no counterexample was found in the stated search. It does not justify narrowing the domain silently or upgrading a conjecture to a theorem.

## Respond to errors and counterexamples

A valid counterexample refutes the stated claim. Immediately mark it `refuted`, flag dependent claims and affected draft assertions, and notify the user of the mathematical correction and its scope. Do not wait for approval to acknowledge a false claim, and do not silently replace it with a narrower statement.

Classify the next problem precisely:

| Finding | Response |
|---|---|
| Algebra or logical error | Correct the step and recheck its dependencies. |
| Missing proof step | Mark the gap; investigate whether it is repairable without changing the claim. |
| Hidden assumption or selection | State it explicitly; determine whether it changes the model, claim, or interpretation. |
| Valid boundary reversal | Withdraw the universal claim; investigate a conditional result and the mechanism behind the boundary. |
| Conclusion embedded in an assumption | Separate mathematical validity from limited research content and return that issue to discovery. |
| Solver or tool failure | Record the failure and use another justified check; do not infer mathematical falsity. |

Within authorized exploration, investigate alternative assumptions or formulations as provisional branches, preserving the failed version. Changes to an author-selected main line follow AGENTS.md and the recorded authorization. Evidence that a result is false remains visible regardless of the decision about its replacement.

Do not add assumptions merely to restore a desired sign. A restriction can be justified by economic scope, a precise mathematical domain, or a meaningful boundary; explain which. The discovery protocol handles whether the revised result teaches enough to pursue.

## Formalize when the benefit warrants it

Select compact or consequential claims for which formalization is useful and feasible. Specify the mathematical statement, definitions, dependencies, and the correspondence to the informal claim before interpreting an accepted file.

Preserve the proof source, checker command, environment/dependencies, and accepted output. Inspect unresolved placeholders and admitted results; an admission of the target or its dependencies does not establish it. Disclose nonstandard added axioms and distinguish conditional verification from a proof under the stated model assumptions. State exactly which encoded claim was accepted and which parts of the economics remain informal.

A failed formalization attempt can expose ambiguity or missing assumptions, but it may also reflect library or engineering limitations. Record the blocker without calling it a counterexample. Do not make whole-paper formalization a routine prerequisite.

## Report the result and update dependents

Update the affected claim records and link the checks, rather than producing a generic “verified” verdict. Briefly report:

- the exact claims checked, their versions, and the resulting proof and check statuses;
- decisive evidence, unresolved gaps, counterexamples, and coverage limits;
- changed assumptions or interpretations under consideration;
- affected dependent claims or draft passages and what needs revalidation;
- the next justified action within the current authorization.

Review manuscript claims, including prose comparative statics and welfare statements, against these records before they are presented as established. A numerical illustration, plausible intuition, or accepted sublemma must remain labeled at its actual evidentiary level.

## Compact task prompts

**Verify a claim:** Read AGENTS.md, this protocol, and the relevant model version. Extract the exact claim and dependencies, re-derive the decisive argument, select appropriate checks, and update its evidence and status. Report errors immediately and investigate replacements within the existing authorization.

**Search for counterexamples:** For the stated claim and admissible domain, design a targeted search that addresses its likely failure modes. Preserve reproducible evidence, validate suspected violations, and explain the coverage and limitations of a negative search result.

**Assess formalization:** Identify a useful claim, state its relation to the economic result, and assess the required definitions and tools. If an attempt is warranted, run the actual checker and report only what the accepted artifact establishes.
