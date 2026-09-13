# Discovery for Economic Theory Research

Workflow revision: 2026-09

Modified: 2026-09-13.

Use this protocol to develop economic questions, competing explanations, and models. The filename is retained for existing installations; the approach covers microeconomic theory, IO theory, and other theory fields.

[AGENTS.md](AGENTS.md) defines instruction priority, authorization, and scientific integrity. Discovery, verification, and writing are activities that can be revisited in any order, not a one-way sequence of approval gates. Use [the verification protocol](ECONOMETRICA_VERIFICATION_WORKFLOW.md) for mathematical claims, [the writing protocol](ECONOMETRICA_AI_HUMAN_WORKFLOW.md) for reader-facing work, and [the panel protocol](ECONOMETRICA_PANEL_PROTOCOL.md) when independent judgment would resolve a material uncertainty.

## Start from the actual task

Read `project_state.md` if it exists, then only the research material needed for the request. Establish the question, intended audience, available evidence, authorized scope, and the most consequential unknown. Do not infer that a detailed user-supplied model is a proven or valuable research contribution.

- For a broad field, look for unsettled questions, institutional changes, conflicting explanations, or theoretical limits.
- For a rough idea, articulate its economic tension and plausible competing mechanisms before selecting a model.
- For an existing model, investigate what it teaches and which assumptions carry that lesson.
- For an explicit derivation or editing request, do that work directly; do not force a new discovery process.

Within authorized exploration, vary assumptions and compare branches without treating each experiment as an author-selected change of direction. Changes to the selected research line follow the authorization recorded under AGENTS.md. Research decisions must not be inferred from an old lock file or the presence of a polished draft.

## Keep a small research record

Use the shared [record definitions](ECONOMETRICA_ORCHESTRATOR.md#current-state-and-evidence). Keep the question and competing mechanisms in `idea_dossier.md`, and the model and claims in `model_note.md`. Create only records with useful content.

Long derivations and executable checks may live in `verification/`, linked from the relevant claim. Earlier files such as `model_base_design.md`, `theorem_candidates.md`, and `contribution_lock.md` are compatibility sources: inspect their evidence and decisions before reusing them. Their names or old status labels do not establish current validity.

Reuse earlier project experience only when relevant and authorized. Treat remembered successes or rejections as hypotheses to reconsider against current evidence, not permanent filters. Do not automatically load unrelated project archives or restrict search to previously successful methods.

## Frame a question worth understanding

An initial idea needs an intelligible question and a reason to investigate, not an introduction-ready theorem. Write a short account of:

- the economic phenomenon or theoretical difficulty;
- what a knowledgeable reader currently expects and why;
- the conflicting incentives, constraints, explanations, or analytical limits;
- what learning the answer would change;
- what is currently conjectured, known, or unknown.

For IO, make the relevant choices and institutional setting concrete: who chooses what, what information or commitment they have, how rivals or consumers respond, and whose outcome is at issue. Do not invent a policy claim to make a model seem important.

For a methods, representation, existence, or impossibility project, explain the analytical obstacle and which economic questions or classes of models the result would illuminate. A novel tool can contribute without a directional comparative static or a topical real-world story.

Possible contributions include a mechanism, a meaningful boundary or reversal, an impossibility, a unifying explanation, a characterization, or a useful analytical method. These are possibilities, not boxes every project must fill. Several results may jointly establish one contribution.

## Explore different explanations

Start branches from different substantive perspectives when useful: institutional observations, rival explanations, counterexamples to conventional reasoning, overlooked decision makers, or limitations of a method. Independent contributors should formulate their reasoning before seeing the current preferred answer when anchoring is a concern.

Record only what distinguishes a live branch:

```text
Question or tension:
Candidate explanation and behavioral logic:
What would differ from the leading alternative:
Evidence status and main unknown:
Next informative test, its cost, and possible implications:
```

Changing a parameter, industry name, or timing detail does not by itself create a distinct explanation. Such variations can still be useful tests of one mechanism. Non-mainstream ideas deserve evaluation on their content; labels such as “frontier spike” or “hidden gem” are not evidence of quality.

Choose search breadth from the task and available resources. Generate another batch only when it is likely to expose a missing explanation or useful test. Stop expanding when variants repeat known mechanisms or a concrete investigation is more informative. Record actual work; never manufacture candidates or rejection reasons to satisfy a count.

Compare potential value, evidence, unresolved uncertainty, and the information a feasible next test would provide. Do not turn an uncalibrated numerical score, early proof difficulty, or initial lack of positioning into an automatic rejection. A difficult but informative test may justify a small investment; an easy proof may have little research value.

## Use examples to expose the mechanism

For applied theory, start with the smallest setting that reveals the relevant incentives. A hand-solvable numerical or symbolic example is often best. State the initial intuition before calculation, then record whether the result supports it, contradicts it, or remains ambiguous.

Explain who changes behavior, why that response matters, and where the explanation may fail. A useful example may reproduce an established benchmark to isolate what a later change adds. The example itself need not be a new theorem.

When a finite hand-solved example cannot carry the contribution, use a minimal application, a representative failure or boundary case, or an explanation of why finite simplification loses the object of study. Methodological and general theory work should make its analytical and economic use intelligible without fabricating a vignette.

Difficulty explaining the model is diagnostic: distinguish missing economic content, a poorly chosen model, and poor exposition. Do not add assumptions merely to produce a clean illustration. Move between an example and the general model as needed; formal language alone does not establish progress.

## Build only what the question requires

In `model_note.md`, identify the model version, agents, timing, information, actions, payoffs or objectives, constraints, solution concept, and assumptions relevant to the claim. Mark exploration branches as provisional and retain their relation to the selected model.

For each important assumption, ask what economic force it represents, whether it builds in the conclusion, and what changing it would teach. Distinguish economic content, domain restrictions, and mathematical convenience.

A reduced-form object is not automatically defective. Endogenize it when holding it fixed distorts the central question, assumes the purported mechanism, or prevents a useful comparison of explanations. Otherwise explain its interpretation and scope. Consider alternatives or sensitivity analysis before adding another layer of choice. Stop adding layers when they do not improve the answer or its applicability.

Prefer a simpler model when it preserves the relevant insight. Complexity is justified when it reveals a distinct force, determines a meaningful boundary, or enables an important analysis. Do not judge a model by the number of primitives, conditions, or lines in its theorem.

Record candidate results with the claim discipline in the verification protocol. First-pass derivations may redirect the question. A failed prediction is research evidence, not a reason to hide the attempt.

## Compare the actual literature contribution

Identify the closest papers through inspected sources. In `literature_evidence_ledger.md`, separate source-supported statements, inferences, and unresolved search questions. An unavailable source or incomplete search permits a provisional comparison, not a definitive novelty or duplication claim.

Use legitimate available sources, such as publisher access, author manuscripts or repositories. Record access limits and respect permissions when downloading or sharing texts; do not bypass access controls.

For a serious comparison, record:

| Dimension | Candidate versus closest inspected result |
|---|---|
| Question and setting | Economic object, agents, institution, information, and choices. |
| Assumptions and scope | Domains, restrictions, solution concept, and relevant quantifiers. |
| Result | What is actually established, with a precise source location. |
| Interpretation | What a reader learns and whether that lesson is already present. |
| Relationship | Shared tool, benchmark application, substantive equivalence, extension, or distinct contribution; explain the mapping. |

Using a named framework or an established proof method does not establish duplication. Conversely, new terminology or a new setting does not establish a new theoretical insight. To conclude substantive equivalence, show that the prior result covers the relevant assumptions, conclusions, scope, and economic lesson; identify any remaining difference and assess its value separately.

An extension can matter if it changes an important prediction, explains a previously unresolved boundary, unifies cases, or enables a useful analysis. A difficult mathematical extension can still be economically uninformative. Do not require the claim that “existing theory cannot obtain this result”: distinguish what was established before from what follows using available tools.

## Learn from boundaries and failures

When a condition changes the sign, existence, or scope of a result, use the verification protocol to determine what failed. Then examine what the failure teaches:

- A calculation or logical error defeats that derivation; correct it and reassess the claim. Mark the claim `refuted` only when a valid disproof is available.
- An economically interpretable boundary may reveal competing forces and become the contribution.
- A technical restriction may limit the current proof without describing the true boundary.
- A tailored patch may preserve a desired conclusion while removing its relevance.

A longer or more conditional contribution sentence is not itself evidence of dilution. Evaluate the information gained and the naturalness of the conditions. State genuine limits clearly; do not omit necessary assumptions for rhetorical sharpness.

For a failed approach, record the original prediction, the evidence, what remains plausible, and what would justify revisiting it. Separate rejection of a proposition from rejection of the question. A valid counterexample can be the start of a better explanation.

## Test whether a reader learns something

Use a short economic explanation early, before committing to a full manuscript. Keep it proportional to the idea; around two pages is often sufficient. Explain the question, the tension, the emerging result or uncertainty, the mechanism, the closest comparison, and the boundary that matters.

Ask an independent reader to reconstruct the question, behavioral logic or analytical gain, result, importance, and limitation from that explanation. This can be an AI check clearly labeled as such; it does not substitute for actual economist feedback. Failed reconstruction should identify whether the problem is research content or writing.

Do not optimize for surprise alone. A result may be valuable because it explains, characterizes, unifies, or enables something important. Interesting prose must remain faithful to the model and evidence.

## Choose the next action from the evidence

Decide among further exploration, targeted verification, reader explanation, fuller development, parking, or abandoning a line. These are revisable research choices, not mandatory stage gates.

Before substantial manuscript investment, the record should support a coherent economic or analytical contribution, an appropriate set of formal claims with transparent proof status, a credible comparison to inspected literature, and a reader explanation. A rough draft can itself be an exploratory test and should be labeled accordingly.

Use independent review for consequential uncertainty rather than running a full panel on every branch. A final recommendation should explain:

- what has been learned and why it could matter;
- which evidence supports the current contribution;
- the strongest unresolved objection;
- the next useful action and what its possible outcomes would change;
- whether any decision exceeds the current authorization.

Mathematical correctness is necessary for a claimed result but does not establish research value. A supported finding of duplication or an uninformative conclusion can justify changing course; unfamiliarity, a low self-assigned score, or repetition of the same AI opinion cannot establish that finding.

## Compact task prompts

**Explore:** Read AGENTS.md and this protocol. Use the stated question and available evidence to develop distinct explanations, compare their unknowns, and perform the most useful feasible test. Update only the records the work needs. Explain what changed in our economic understanding.

**Investigate a model:** Read the current model and relevant claims. Identify what the model teaches, use an appropriate minimal example or application, compare the closest inspected results, and test the most consequential assumption or prediction. Apply the verification protocol to mathematical claims and preserve failed attempts.

**Reconsider a direction:** Read the evidence behind the selected line and its main objection. Determine whether the issue is validity, contribution, model choice, or exposition. Investigate authorized alternatives, explain the tradeoff, and use AGENTS.md for any decision outside the existing authorization.
