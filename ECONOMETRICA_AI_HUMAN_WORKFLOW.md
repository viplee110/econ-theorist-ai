# Developing and Writing Economic Theory

Workflow revision: 2026-09

Modified: 2026-09-13.

Use this module when developing an economic explanation, drafting a paper, or revising an existing manuscript. Read `AGENTS.md` for the shared rules on evidence, authorization, and preservation of author work; this module does not add another approval system. Use `ECONOMETRICA_ORCHESTRATOR.md` to resume work and load only the relevant methods.

The research objective is a useful, defensible change in economic understanding. A frontier paper may contribute a mechanism, an important boundary, an impossibility result, a unifying explanation, or a method that enables previously inaccessible economic analysis. Technical difficulty, generality, a dramatic result, and simulated acceptance are not substitutes for that contribution.

## Work from the Actual Research Problem

Exploration, checking, and writing are activities that can alternate or run alongside one another. They are not a sequence of stages that every paper must complete. Writing a short explanation can expose a missing mechanism; a counterexample can open a new question; a clear result can justify deeper verification.

At the start of a development task:

- Identify the author's current question, intended reader, selected direction, and requested scope from the available materials.
- Separate constraints the author actually imposed from assumptions introduced by the AI.
- Read the current economic explanation and relevant model, claims, and literature evidence. Do not require a project to reconstruct a discovery tournament before working on an existing paper.
- Choose a concrete output that will advance understanding: a mechanism explanation, a discriminating example, a revised result, a section draft, or a targeted check.

Within the scope defined in `AGENTS.md`, investigate alternatives and make reversible improvements. Preserve an author-selected main line when exploring a different one; show a candidate branch and its consequences rather than silently replacing the author's choice. Existing authorization remains effective across related work.

## Small Set of Working Records

Use the [shared record definitions](ECONOMETRICA_ORCHESTRATOR.md#current-state-and-evidence). Develop the economic explanation in `idea_dossier.md`, read the relevant claims from `model_note.md`, and record material revisions in `research_log.md`. Do not create an empty set of files.

Keep manuscript sources in the project's existing location. Preserve proof and computational evidence under `verification/` or link to existing evidence in place. Keep longer calculations and parallel exploratory drafts outside the compact current-state notes.

## Write the Economic Explanation Early

As soon as a mechanism has enough shape to discuss, prepare a short explanation in `idea_dossier.md`. A two-page note or five-minute seminar explanation is a useful format, not a mandatory length or an entry ticket to further research.

The explanation should let the intended reader answer:

1. What is the economic question or theoretical difficulty?
2. What does a natural existing explanation lead one to expect?
3. Who changes behavior, in response to what incentive or information, and with what consequences for others?
4. What does the analysis teach that the reader did not already know?
5. Which condition or institutional feature changes the answer, and why?

For a methodological contribution, explain the economic question that becomes tractable and demonstrate a minimal application. Do not invent a policy story, empirical claim, or behavioral narrative for a result whose contribution is methodological.

Use the smallest example that reveals the force when useful. A finite example is not compulsory if it removes the mechanism; a restricted subproblem, limiting case, diagram, or minimal application may explain it better. Formal analysis may help discover the intuition rather than waiting for a complete intuition in advance.

When alternatives remain plausible, state their different predictions and the next observation, calculation, or literature comparison that could distinguish them. Do not fill explanatory gaps with additional terminology.

## Reader Checks Before Expensive Polish

Use `ECONOMETRICA_PANEL_PROTOCOL.md` for a fresh reader check when the explanation needs an outside test. Give the reader the note and its intended audience, without the author's self-assessment or earlier review verdicts. Ask the reader to restate the question, behavioral mechanism, result, significance, and boundary.

A failure to restate the argument can indicate different problems:

- The economic discovery is present but obscured by exposition: rewrite the reader path.
- The result is clear but the claimed contribution is unsupported: examine the literature comparison or significance.
- The mechanism is missing or inconsistent: return to the relevant modeling question.
- The result is conditional in an economically meaningful way: make the boundary part of the explanation.

An AI reader supplies a diagnostic, not evidence that economists will value the paper. Prepare materials for real expert or seminar feedback when useful, and incorporate feedback the user provides. Follow `AGENTS.md` for any external contact; never invent a human reaction.

## Maintain a Revisable Contribution

Record the current contribution together with its supporting claims and uncertainty. Useful elements are the economic question, the best current answer, the closest published comparison, the reader's resulting understanding, and what could change that answer.

Do not freeze a desired theorem or contribution sentence as a scientific constraint. A prior author choice records research intent, not mathematical truth. Evidence may require withdrawing a claim immediately while the author considers a different direction.

When a result changes, record in `research_log.md`:

- The old and new claim, including changed assumptions or quantifiers.
- The evidence that required or motivated the change.
- Whether the change corrects an error, identifies an economic boundary, or introduces a modeling cost needing justification.
- The implications for the current economic explanation and affected manuscript passages.

A longer or more conditional sentence is not grounds for rejection. A meaningful boundary can strengthen a paper. A shorter sentence obtained by omitting a truth-critical condition is unacceptable. Judge complexity by the economic work it performs, not by counting assumptions or clauses.

Do not dismiss a contribution merely because it uses a known mathematical framework. Use the literature comparison method in `ECONOMETRICA_DISCOVERY_WORKFLOW.md` to establish whether the economic result is already present, or whether familiar tools reveal something new.

## Carry Claim Status into Every Draft

`ECONOMETRICA_VERIFICATION_WORKFLOW.md` owns the verification procedure. Writing must preserve its distinctions:

- Claim status: `conjecture`, `proof sketch`, `proved`, `refuted`, or `unresolved`.
- Independent check: `not run`, `pass`, or `gap`, with the scope of the check.
- Computational and formal evidence: record what was actually checked, under which model version and assumptions.

Each substantive formal claim must link to its claim ID, model version, assumptions, quantifiers, dependencies, and evidence in `model_note.md` or the existing claim records. `proved` requires a complete proof of the stated claim; numerical success or failure to find a counterexample does not supply one. Independent review is recorded separately from the proof's existence.

If a premise changes, identify the claims and passages depending on it and mark their relevant checks and wording for re-examination. Do not invalidate unrelated work or restart the whole project. A prose-only edit does not require repeating a mathematical audit unless its meaning changes.

Provisional drafts may contain conjectures and proof sketches if they are clearly identified where relevant. A reading draft need not wait for every uncertainty to disappear. It must not present a conjecture as a theorem or an incomplete search as established novelty.

## Build the Manuscript around the Argument

Choose section order from the reader's needs and the contribution. A usual progression introduces the question and tension, explains the model, develops the principal findings, and discusses their implications and boundaries. Change that progression when the paper's argument warrants it.

Before a large draft or restructuring, sketch what each section teaches and which claims it uses. Put this outline in the current working note or manuscript plan; it does not require an additional architecture artifact or approval gate.

Ask of each section:

- What understanding does the reader gain here?
- Why is that understanding needed at this point?
- Which assumptions and results carry it?
- What belongs in the main argument, and what can move to a proof appendix or be removed?

Use published papers as exposition references when a specific difficulty warrants it. Select relevant examples and record the source and limits of the comparison in the literature ledger. There is no required number of anchors and no requirement to match another paper's section count. Full-text evidence is needed for claims about its detailed exposition; an abstract supports only limited conclusions.

Extract useful explanatory choices, not prose to imitate. Reuse prior reading when it is relevant. Ordinary editing does not wait for a style contract, a journal profile, or a separate architecture confirmation.

## Draft Clear, Precise Prose

Lead substantive sections with their economic purpose. Introduce notation when it becomes useful. Explain assumptions through the behavior or institutional feature they represent, including where they limit applicability.

Formal theorem and proposition statements must retain every truth-critical assumption, domain, quantifier, and equilibrium qualification, either stated directly or through an unambiguous reference to maintained assumptions. Keep interpretation and proof intuition in surrounding prose when that improves clarity. Concision must not change a mathematical assertion.

After an important result, explain its causal or strategic logic, its relationship to the relevant benchmark, and its economic boundary. An abstract or introduction should communicate the question and contribution in language the intended reader can follow without reconstructing the proof.

Avoid decorative motivation, inflated importance claims, needless terminology, and repeated defensive caveats. State limitations where they bear on an argument. Do not suppress economically central limitations for a stronger narrative, and do not repeat the entire risk register throughout the paper.

Preserve the author's voice. A targeted edit is enough when it solves the problem; a broader rewrite is appropriate when the reader path requires it and the task authorizes it. User-requested writing improvements do not need repeated style approvals.

## Revise According to Evidence

Treat comments as hypotheses to investigate. Identify the exact affected claim or passage, the evidence offered, and whether the comment concerns correctness, contribution, economic interpretation, exposition, or presentation. A reviewer's confidence or repeated objection is not itself proof.

Correct demonstrably false statements promptly. For unresolved substantive objections, compare the plausible responses: a corrected claim, a meaningful boundary, a simpler explanation, a different model, or a change in research question. Do not require a fixed three-branch ritual for every revision.

When the choice is genuinely open, produce enough of the leading alternatives to make the tradeoff reviewable. Reversible branch prototypes may be developed within the authorized scope. Preserve the author's selected manuscript while an alternative direction remains only a proposal.

Judge a proposed assumption by whether it has an economic interpretation, how it affects the result, and what it costs in applicability. Endogenize an object when holding it fixed distorts the question or when its determination is itself the question. More primitive depth is not an automatic improvement.

Repeated criticism calls for diagnosis: is there new evidence, a valid unresolved objection, shared reviewer framing, or a misunderstanding of the paper? Use a targeted check to resolve it. Do not automatically kill, pivot, or retarget after a fixed count of negative reviews.

Record meaningful changes and their reasons in `research_log.md`, preserve recoverable versions following `ECONOMETRICA_VERSION_CONTROL.md`, and compile after meaningful LaTeX edits when the toolchain is available. Report verification limits accurately when a tool is unavailable.

## Assess the Result, Not Workflow Completion

Before describing a draft as ready for outside evaluation, inspect the actual manuscript and its supporting evidence:

- The question, mechanism or methodological contribution, and economic importance are understandable.
- Central results have the status and evidence claimed for them.
- Literature comparisons are accurate and appropriately qualified.
- Assumptions and applicability boundaries are visible to the reader.
- Unresolved concerns and author choices are clearly identified.

Target-journal discussion should draw on relevant published work and the intended audience. No self-score, panel majority, number of revisions, or completion of these methods establishes top-journal quality or a probability of acceptance. Real submission and external commitments follow the authorization rules in `AGENTS.md`.

## Existing Projects

Read old `contribution_lock.md`, field/target profiles, style plans, stage records, and referee reports as historical evidence when relevant. Do not enforce their retired gates or create them for compatibility. A recorded approval is not proof validity, and an old AI recommendation is not a human decision. Use the repository's migration guidance when consolidating old state; preserve the original records and their provenance.
