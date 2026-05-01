# Human-AI Discovery Workflow for Econometrica-Level Theory Projects

Version: 2026-05-01

This file is a pre-manuscript discovery protocol. Use it before `ECONOMETRICA_AI_HUMAN_WORKFLOW.md` when the project is still at the topic, idea, model, or early theorem stage.

The goal is to help the human and AI search broadly without fooling themselves. The agent should generate many candidates, impose tractability and novelty constraints, attempt simple derivations, run hostile kill tests, and stop at human decision gates.

This workflow supports three starting modes:

- `Field mode`: the human knows the broad field but not the exact question.
- `Idea mode`: the human has a rough idea or mechanism.
- `Open mode`: the human wants AI to explore candidate topics from scratch.

## Core Principle

AI can expand the search frontier, but it cannot certify that a topic is unstudied, important, or Econometrica-level. Treat all generated topics as hypotheses. A candidate survives only if it passes novelty, tractability, economic importance, and execution tests.

## Required Artifacts

Maintain these files during discovery:

- `discovery_state.md`: current mode, constraints, active candidates, last human decision.
- `topic_longlist.md`: broad list of candidate topics and mechanisms.
- `topic_shortlist.md`: surviving candidates after screening.
- `model_candidates.md`: structured model sketches for each surviving candidate.
- `derivation_notes.md`: first-pass derivations, algebra, proof attempts, and failure points.
- `literature_probe.md`: closest literatures, nearest substitutes, novelty risks, and citation TODOs.
- `idea_kill_tests.md`: hostile referee/editor tests for each candidate.
- `human_decisions.md`: human choices, taste judgments, pivots, and reasons.

If a candidate becomes a real paper project, create or update:

- `idea_dossier.md`
- `contribution_lock.md`
- `project_state.md`

Then continue with `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`.

## Human-AI Division of Labor

AI should own:

- broad candidate generation
- combinatorial mechanism exploration
- structured model sketching
- first-pass derivation attempts
- closest-literature search plans
- hostile novelty objections
- tractability diagnosis
- artifact maintenance

The human should own:

- taste and importance
- whether a question is worth caring about
- whether assumptions are economically acceptable
- whether a mechanism feels deep or merely clever
- whether to pivot, abandon, or invest
- final novelty interpretation after real literature checks

## Stage D0 - Intake and Mode Selection

Autonomy: Gate

Purpose:

Determine what kind of discovery problem this is.

The human should provide as much as available:

- broad field
- known literatures
- rough mechanism
- target journal
- mathematical comfort zone
- preferred model style
- forbidden directions
- empirical, theoretical, or mixed orientation
- whether the project should be single-author tractable
- time budget

AI tasks:

- Create `discovery_state.md`.
- Identify the mode: `Field`, `Idea`, or `Open`.
- Ask only essential clarifying questions.
- If enough information exists, proceed with stated assumptions.

Human gate:

Approve the mode and constraints.

## Stage D1 - Search Space Expansion

Autonomy: Auto

Purpose:

Generate a wide but structured set of possible research directions.

AI tasks:

- Create `topic_longlist.md`.
- Generate 30-80 candidate topic-mechanism combinations, depending on scope.
- Use multiple axes:
  - field
  - friction
  - agents
  - information structure
  - strategic variable
  - market design or institutional environment
  - welfare object
  - identification object if relevant
  - closest literature family
  - possible surprising result

Candidate template:

```text
Candidate ID:
Working title:
Field:
Core economic question:
Agents:
Friction:
Mechanism:
Strategic choice:
Information/timing:
Potential main result:
Why it might matter:
Closest literature families:
Tractability guess:
Novelty risk:
Execution risk:
One-sentence pitch:
```

Rules:

- Do not repeat minor variants as separate candidates.
- Prefer mechanisms that could change a specialist's belief.
- Include some high-risk/high-upside candidates.
- Include some clean and tractable candidates.
- Flag candidates that sound clever but not important.

## Stage D2 - Coarse Screening

Autonomy: Auto, then Gate

Purpose:

Reduce the longlist to a serious shortlist.

AI tasks:

- Score every candidate 1-5 on:
  - economic importance
  - novelty potential
  - non-substitutability
  - tractability
  - likelihood of a sharp theorem
  - literature risk
  - assumption plausibility
  - fit for Econometrica
- Penalize candidates that rely on vague "AI/platform/algorithm" language without a real mechanism.
- Penalize candidates where the result seems obvious before modeling.
- Penalize candidates where all novelty comes from adding one extra feature to a known model.
- Create `topic_shortlist.md` with 5-10 surviving candidates.

Human gate:

The human selects 1-3 candidates for model sketching.

## Stage D3 - Literature Probe

Autonomy: Checkpoint

Purpose:

Avoid rediscovering known papers.

AI tasks:

- Create `literature_probe.md`.
- For each shortlisted candidate:
  - identify closest literature families
  - list likely nearest substitute papers
  - generate search queries for Google Scholar, Semantic Scholar, RePEc, NBER, CEPR, SSRN, arXiv, and author pages
  - describe what would kill the novelty claim
  - describe what would preserve the contribution
- Separate verified facts from AI inferences.
- Mark all unverified references as TODO.

Human gate:

The human should inspect the top substitute papers or ask the AI to help locate them. Do not trust novelty until this gate is passed.

## Stage D4 - Model Candidate Generation

Autonomy: Auto

Purpose:

Generate tractable model skeletons for each surviving idea.

AI tasks:

- Create `model_candidates.md`.
- For each selected candidate, generate 3-5 model variants:
  - minimalist baseline
  - richer but still tractable version
  - alternative timing
  - alternative information structure
  - alternative equilibrium concept if relevant

Model template:

```text
Model ID:
Candidate topic:
Core question:
Agents:
Primitives:
Timing:
Information:
Actions:
Payoffs/objectives:
Equilibrium concept:
Key assumptions:
Main endogenous objects:
Predicted main proposition:
Comparative statics:
Welfare or policy object:
Why tractable:
Likely proof technique:
What could go wrong:
Closest existing model:
```

Tractability constraints:

- Prefer two or three agent types before many-type models.
- Prefer one central friction before multiple interacting frictions.
- Prefer closed-form or monotone comparative statics where possible.
- Avoid unnecessary dynamic state variables.
- Avoid assumptions that exist only to force the desired result.
- Make every assumption economically interpretable.

## Stage D5 - First-Pass Derivation

Autonomy: Auto, but must be rigorous

Purpose:

Test whether the model has a real result.

AI tasks:

- Create or update `derivation_notes.md`.
- For each model variant, attempt a first-pass derivation.
- Write:
  - agent problem
  - objective functions
  - constraints
  - equilibrium conditions
  - candidate solution
  - main comparative static
  - proof sketch
  - exact algebra where possible
  - conditions required
  - counterexample attempt
  - failure points

Required derivation discipline:

- Every proposition must state its assumptions.
- Every comparative static must identify the derivative, monotone order, or argument used.
- Every proof sketch must state where each assumption enters.
- If a result follows almost immediately from an assumption, flag it as low contribution.
- If the result needs an unstated regularity condition, add it explicitly to `derivation_notes.md` and mark it as a risk.
- If algebra becomes messy, try a simpler model before adding assumptions.
- Try to construct at least one counterexample to the predicted proposition.
- If the proposition fails, record the failure rather than repairing silently.

Output categories:

- `Promising`: clean result, plausible assumptions, nontrivial insight.
- `Technically possible but weak`: solvable but low economic bite.
- `Too tailored`: result depends on artificial assumptions.
- `Too messy`: solution exists but not paper-tractable.
- `Fails`: proposition false or no clear result.

## Stage D6 - Contribution and Kill Test

Autonomy: Gate

Purpose:

Decide whether the candidate deserves further investment.

AI tasks:

- Create `idea_kill_tests.md`.
- For each promising model, simulate:
  - hostile closest-literature referee
  - theory referee
  - economic relevance referee
  - editor deciding whether to desk reject
- Ask:
  - Is the insight new or just a relabeling?
  - Is the mechanism economically important?
  - Does the model reveal something not visible without formal analysis?
  - Are assumptions credible?
  - Is the result surprising after reading the closest literature?
  - Would a top-field seminar audience care?
  - What is the strongest reason to kill this idea today?

Decision labels:

- `Invest`: begin full paper development.
- `Refine`: keep the idea but modify the model.
- `Pivot`: change the mechanism/question.
- `Park`: save for later but do not invest now.
- `Kill`: abandon for current purposes.

Human gate:

The human must choose a decision label. AI may recommend, but not decide.

## Stage D7 - Pre-Paper Package

Autonomy: Auto

Purpose:

Convert a surviving candidate into a paper-ready starting package.

AI tasks:

- Create `idea_dossier.md`.
- Create `contribution_lock.md`.
- Create `project_state.md`.
- Write a 1-2 page concept note:
  - question
  - mechanism
  - model
  - main predicted proposition
  - proof status
  - closest literature
  - contribution claim
  - biggest risks
  - next work plan

Proceed condition:

- The human approves the concept note.
- Then continue with `ECONOMETRICA_AI_HUMAN_WORKFLOW.md`, starting at Stage 1 or Stage 2 depending on maturity.

## Common Failure Modes

Stop or pivot if:

- The generated topic is just a fashionable noun plus a standard model.
- The model's result is obvious without the model.
- The model becomes complex before producing a clean insight.
- The assumptions are doing all the work.
- The nearest substitute paper already has the same mechanism.
- The AI cannot explain why the question matters to economists.
- The result only says "more friction leads to worse outcomes" without a sharp twist.
- The contribution is a parameter extension, not a conceptual insight.
- The human cannot pitch the idea in one minute with conviction.

## Prompt Templates

### Start Discovery in Field Mode

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D0 and D1 in Field mode. My broad field is: [FIELD]. Generate a structured longlist of candidate Econometrica-level theory topics. Do not write a manuscript. Create discovery_state.md and topic_longlist.md, then stop.
```

### Start Discovery in Idea Mode

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D0 through D2 in Idea mode. My rough idea is: [IDEA]. Expand nearby mechanisms and model variants, then screen them. Create discovery_state.md, topic_longlist.md, and topic_shortlist.md. Stop at the human gate.
```

### Start Discovery in Open Mode

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D0 and D1 in Open mode. Generate a broad but disciplined set of candidate theory topics that could plausibly lead to Econometrica-level contributions. Favor tractable models, sharp mechanisms, and non-obvious comparative statics. Create discovery_state.md and topic_longlist.md, then stop.
```

### Generate Models for Shortlisted Ideas

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Use topic_shortlist.md and run Stage D4. Generate 3-5 tractable model variants for each selected candidate. Create model_candidates.md. Do not write the paper yet.
```

### Attempt First-Pass Derivations

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D5 for the selected model candidates. Attempt clean first-pass derivations, state assumptions, show algebra where possible, identify failure points, and attempt counterexamples. Create derivation_notes.md. Do not hide failed models.
```

### Run Discovery Kill Test

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D6. Use model_candidates.md, derivation_notes.md, and literature_probe.md if available. Simulate hostile referees and an editor. Create idea_kill_tests.md and recommend Invest, Refine, Pivot, Park, or Kill for each candidate. Stop for my decision.
```

## How This Connects to the Main Workflow

Use this discovery workflow before writing a full paper. Once a candidate receives `Invest`, create the pre-paper package in Stage D7 and then continue with:

```text
Read ECONOMETRICA_AI_HUMAN_WORKFLOW.md. Run Stage 1 or Stage 2 using the idea_dossier.md and contribution_lock.md created during discovery.
```

