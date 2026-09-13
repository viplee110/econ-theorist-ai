# Independent Checks and Developmental Review

Workflow revision: 2026-09

Modified: 2026-09-13.

Use this module when a research decision benefits from a fresh, question-specific examination. `AGENTS.md` owns the shared evidence and authorization rules. The orchestrator selects useful work; a panel is not a compulsory gate before exploration, modeling, drafting, or revision.

A useful review adds evidence, exposes a missed explanation, or makes a disagreement testable. Simulated editorial authority and repeated judgments from related models do not establish scientific quality.

## Scope the Check

Start with the uncertainty to resolve and the material needed to resolve it. Reuse current project notes and literature evidence; do not require separate field, target, panel-configuration, or style files before beginning.

Record a short task brief with:

- The specific claim, model version, economic explanation, or manuscript passages to examine.
- The question each reviewer should answer and why that perspective is needed.
- Allowed materials, any intentionally withheld judgments, and access to search or verification tools.
- The actual execution arrangement and the location of outputs.

Put the brief and synthesis in `research_log.md` or the relevant working note. Save separate reports only when their substance or independent provenance merits preservation. An ordinary check should not create an editorial hierarchy of documents.

## Select Functions, Not a Fixed Cast

Choose only the functions needed for the current question:

| Function | Useful task |
| --- | --- |
| Economic mechanism reader | Reconstruct who responds to which incentive; identify competing explanations and an informative distinguishing test. |
| Closest-literature reader | Compare exact published claims, assumptions, quantifiers, and economic interpretations with the candidate contribution. |
| Proof or computation checker | Check the specified formal claim and dependencies; seek a counterexample or verify a disputed step. |
| Fresh intended reader | Restate the question, result, importance, and boundary from the explanation or manuscript alone. |

One targeted check may be enough. A consequential choice may justify several complementary checks. Do not add referees merely to fill fixed slots or attach a separate Associate Editor and Co-Editor to each exercise. The coordinating agent synthesizes the evidence once.

A user-requested full manuscript review should cover the paper's material economic, literature, formal, and exposition risks in sufficient depth. Expand independent tasks where the manuscript warrants them, while avoiding duplicate reports and ceremonial editorial layers.

## Independence and Information Access

Use separate workers with explicit input boundaries when available and useful. Reviewers should not read each other's initial reports or the author's desired verdict. Record the model/session provenance actually known; do not invent it or delay the work to obtain an unnecessary label.

Choose material boundaries according to the task:

- A fresh reader receives the explanation or manuscript and intended audience, without contribution self-ratings or prior verdicts.
- A proof checker receives the complete relevant model, statement, assumptions, definitions, and proof dependencies. Blinding must not remove information needed to check the mathematics.
- A literature reader receives the exact candidate claim and may examine sources independently. Claims about papers must have retrievable evidence.
- A revision reviewer may need both the old and proposed claims to understand the change.

Distinct workers can still share model biases. Independent execution means separated work, not statistically independent errors. If the runtime only supports sequential analysis in one conversation, label it a multi-perspective analysis; do not claim independent or blind review. A later reviewer who saw earlier verdicts is a contextual follow-up, not another independent vote.

## Match the Posture to the Work

During exploration, reconstruct the strongest coherent version before judging it. Identify what is promising, what is unknown, and which affordable test could materially change the decision. Difficulty, unfamiliarity, unresolved proof, or a familiar modeling tool is not sufficient evidence to discard an idea.

During development, check whether the model and economic explanation agree. Examine how an assumption changes behavior and whether an apparently fragile result reveals a useful boundary. A small example, minimal application, or restricted subproblem can clarify the issue without imposing a mandatory modeling format.

During verification, follow `ECONOMETRICA_VERIFICATION_WORKFLOW.md`. Check the stated claim rather than a stronger, weaker, or more convenient substitute. A counterexample must satisfy the claim's premises; a proof must establish its full quantifiers and conclusion.

During writing review, test what an intended reader can understand and what the evidence supports. Distinguish an obscured insight from a missing insight. Suggest a targeted exposition repair when that is the problem; suggest a research test when the underlying economics remains unresolved.

These postures may be used on different parts of the same project at the same time. They are not stages with one-way admission rules.

## Require Evidence-bearing Reports

A useful report states:

1. Its answer to the assigned question, with scope and uncertainty.
2. The evidence: exact passage, equation, assumption, proof step, counterexample, calculation, or published comparison.
3. The strongest defensible interpretation of the current work.
4. The consequential unresolved issue and what would change the assessment.
5. The next action, if any, justified by that evidence.

Prioritize concerns that could change the argument. Distinguish a demonstrated error from an untested suspicion, missing information, a taste judgment, or a suggested extension. If evidence is unavailable, identify the limitation rather than manufacture a confident verdict.

For formal claims, use the [claim and evidence definitions](ECONOMETRICA_VERIFICATION_WORKFLOW.md#bind-claims-to-their-evidence). Retain the exact claim, version and evidence pointers; distinguish a complete proof, the scope of an independent check and finite computational evidence.

When a premise changes, flag only the dependent claims, checks, and passages for re-examination. Preserve unrelated evidence. Do not reset the entire project because one assumption changed.

For literature claims, record source evidence in `literature_evidence_ledger.md` or link to an existing entry. Compare the economic claim and its conditions, not merely the presence of a familiar framework. Source access limitations must remain visible in the conclusion.

## Contribution Changes and Complexity

Assess the current manuscript against its actual supporting evidence and the author's stated research intent. Do not impose a hard ratchet against an earlier contribution sentence.

If a claim has changed, explain the old and new propositions, the reason for the change, and its economic consequences. Classify the change as appropriate: correction, useful boundary, alternative mechanism, exposition repair, or added modeling cost. A more conditional result may be more informative and more accurate.

Examine whether an extra object or assumption performs necessary economic work. An object need not be endogenized merely because it is reduced-form. A general theorem is valuable when its scope teaches something; a restricted result is valuable when the restriction defines an important economic setting or boundary.

A known mathematical tool is compatible with a new economic contribution. A genuine duplication objection must show that existing work already delivers the relevant result and interpretation under the relevant conditions. Use `ECONOMETRICA_DISCOVERY_WORKFLOW.md` for the detailed comparison method.

Do not rank `kill`, `park`, `pivot`, `retarget`, and `invest` on a numerical scale. They are different research actions. A review recommendation does not authorize replacing the author's selected direction or abandoning their project; follow the scope rules in `AGENTS.md`.

## Synthesize Once

The coordinating agent examines the evidence, rather than averaging scores or counting votes. The synthesis should answer:

- What did the checks establish, and what remains uncertain?
- Which disagreements are substantive, and which arise from different premises or reader expectations?
- What did the reviewers collectively miss?
- Which next action best resolves a consequential uncertainty or improves the argument?

Resolve disagreements through a specific source check, proof check, counterexample, or reader test when possible. Repeated criticism without additional evidence should not trigger automatic termination or retargeting. Preserve minority observations when they identify a testable possibility.

Save the material findings in the relevant current notes and record the decision rationale in `research_log.md`. Only actual human decisions belong in `human_decisions.md`. Recommendations, including favorable simulated reviews, remain AI analysis.

## Published-paper Calibration

When judging fit for a particular audience or journal, use relevant published work to make the standard concrete. Select papers because their question, contribution type, or intended reader is informative; do not require an arbitrary number of anchors.

Distinguish a source-supported comparison from a general impression. Do not force the new manuscript to match another paper's structure, theorem count, or rhetorical style. Evidence about exposition requires access to the relevant text.

When evaluating the review system itself, use a varied set of appropriately matched published papers and deliberately flawed examples. Inspect whether objections are correct and useful; a single rejection of a published paper does not establish miscalibration, and accepting every published control is not the objective. Model familiarity with public papers can also affect the result.

No simulated verdict, self-score, or agreement rate establishes publication readiness, top-journal quality, or an acceptance probability. Human field feedback and the substantive evidence remain essential inputs to scientific judgment.

## Existing Reports

Old panel configurations, referee reports, contribution locks, and editorial syntheses may contain useful evidence. Read them as historical material when relevant. Do not revive their fixed role counts, hard ratchets, obsolete gates, or unsupported certainty. Preserve their provenance when carrying a finding into the current notes.
