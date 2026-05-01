# Independent Panel Protocol for Econometrica-Level Research

Version: 2026-05-02

This protocol generalizes a stronger simulated review methodology into a reusable decision procedure for the entire research lifecycle. Use it whenever the system must make a high-stakes judgment about an idea, model, derivation, manuscript, referee report, or revision plan.

The core pattern is:

```text
independent specialist judgments
-> explicit disagreement
-> Associate Editor synthesis
-> Co-Editor decision
-> parent-agent summary of consensus, disagreement, omissions, and next actions
```

The purpose is not to make the AI "vote." The purpose is to reduce self-confirmation, preserve real disagreement, and force decisions to be tied to specific claims, assumptions, equations, theorems, manuscript locations, or literature comparisons.

## When To Use

Use this protocol for:

- idea kill tests
- broad topic screening
- tractable model selection
- first-pass theorem or equilibrium assessment
- mathematical proof audits
- simulated Econometrica reviews
- referee-guided revision triage
- final readiness decisions

Do not use a full panel for small copyediting, formatting, bibliography cleanup, or mechanical LaTeX fixes.

## Information Modes

Choose one mode before running a panel.

### Blind Mode

Use for independent evaluation:

- idea kill tests
- manuscript review
- final readiness checks
- external-style referee simulations

Rules:

- Panelists read only the allowed manuscript/idea/model materials.
- Panelists must not read prior referee reports, revision logs, risk registers, old drafts, previous AI discussions, or workflow notes unless explicitly permitted.
- Panelists do not read each other's outputs.
- External web search is off unless the panel is explicitly a literature audit.

### Context Mode

Use for constructive work:

- revision planning
- proof repair
- model redesign
- response to referee reports

Rules:

- Panelists may read relevant state files and previous reports.
- The synthesis must distinguish old objections from newly discovered issues.
- The system must avoid overfitting to prior AI reports.

### Literature Mode

Use for novelty and positioning:

- closest-literature search
- novelty audit
- contribution positioning

Rules:

- Web search or external paper lookup may be used when available.
- Every literature claim must be labeled as verified, unverified, or inferred.
- Missing citations should be marked as TODO rather than invented.

## Panel Types

### Idea Panel

Use before committing to a paper.

Roles:

- Referee 1: economic importance and field relevance.
- Referee 2: closest-literature and novelty risk.
- Referee 3: tractability and model feasibility.
- Referee 4: hostile editor focused on fatal objections.
- Associate Editor: synthesizes the four reports and recommends Proceed, Pivot, Narrow, Split, Park, Kill, or Retarget.
- Co-Editor: independently decides whether to accept the AE recommendation or override it.

Outputs:

- `panel_reports/idea_referee_1.md`
- `panel_reports/idea_referee_2.md`
- `panel_reports/idea_referee_3.md`
- `panel_reports/idea_referee_4.md`
- `panel_reports/idea_ae_report.md`
- `panel_reports/idea_co_editor_decision.md`

### Model Panel

Use after candidate models exist.

Roles:

- Referee 1: minimalist tractability and baseline clarity.
- Referee 2: economic mechanism and comparative statics.
- Referee 3: novelty relative to canonical models.
- Referee 4: mathematical existence, uniqueness, fixed point, IFT, contraction, boundary, and assumption packaging.
- Associate Editor: selects Invest, Refine, Pivot, Park, or Kill for each model.
- Co-Editor: decides which model, if any, should enter full paper development.

Outputs:

- `panel_reports/model_referee_1.md`
- `panel_reports/model_referee_2.md`
- `panel_reports/model_referee_3.md`
- `panel_reports/model_referee_4_math_rigor.md`
- `panel_reports/model_ae_report.md`
- `panel_reports/model_co_editor_decision.md`

### Verification Panel

Use for theorem, proposition, equilibrium, identification, or comparative-static checks.

Roles:

- Referee 1: re-derivation from primitives.
- Referee 2: symbolic and numerical counterexample search.
- Referee 3: proof structure and hidden assumptions.
- Referee 4: formalization triage, Lean suitability, and mathematical rigor.
- Associate Editor: classifies each claim as Verified, Partially Verified, Needs Assumption, Counterexample Found, or Fatal Gap.
- Co-Editor: approves theorem restatement, proof repair path, or claim withdrawal.

Outputs:

- `panel_reports/verification_referee_1.md`
- `panel_reports/verification_referee_2.md`
- `panel_reports/verification_referee_3.md`
- `panel_reports/verification_referee_4_formal.md`
- `panel_reports/verification_ae_report.md`
- `panel_reports/verification_co_editor_decision.md`

### Review Panel

Use for simulated Econometrica review.

Roles:

- Referee 1: field/theory specialist.
- Referee 2: adjacent literature specialist.
- Referee 3: IO/applied micro/economic relevance specialist when appropriate.
- Referee 4: mathematical/probabilistic rigor specialist.
- Associate Editor: independent read first, then synthesis of referee reports.
- Co-Editor: independent read first, then decision letter and internal notes.

Outputs:

- `referee_reports/round_N/referee_1.md`
- `referee_reports/round_N/referee_2.md`
- `referee_reports/round_N/referee_3.md`
- `referee_reports/round_N/referee_4_math_rigor.md`
- `referee_reports/round_N/associate_editor_report.md`
- `referee_reports/round_N/co_editor_decision.md`
- `referee_reports/round_N/00_summary.md`

### Revision Panel

Use after reports exist but before major edits.

Roles:

- Referee 1: which objections are fatal.
- Referee 2: which objections are fixable without changing the contribution.
- Referee 3: which edits would dilute the core idea.
- Referee 4: which fixes require new assumptions, proofs, computations, or citations.
- Associate Editor: creates a ranked revision plan.
- Co-Editor: approves Revise, Pivot, Retarget, External Feedback, or Stop.

Outputs:

- `panel_reports/revision_triage.md`
- updated `risk_register.md`
- updated `revision_log.md`

## Generic Panel Phases

### P0 - Scope and Allowed Materials

Before running a panel, define:

- target object: idea, model, theorem, manuscript, review report, or revision plan
- allowed files
- prohibited files
- web/search policy
- output directory
- decision labels

If the panel is blind, explicitly list prohibited materials.

### P1 - Independent Specialist Reports

Each referee must:

- produce an independent report
- state recommendation and confidence
- cite exact locations when judging a manuscript or proof
- identify fatal concerns before minor concerns
- avoid reading other reports

Recommendation must be chosen from an explicit set. Do not use vague language such as "maybe promising" without a label.

### P2 - Associate Editor Synthesis

The AE must:

1. first produce an independent judgment before reading referee reports
2. then read all referee reports
3. identify consensus
4. identify real disagreement
5. identify collective omissions
6. make a signed recommendation

The AE must not mechanically average or majority-vote the reports.

### P3 - Co-Editor Decision

The Co-Editor must:

1. first produce an independent judgment when the target material is available
2. then read AE and referee reports
3. decide whether to agree with or override the AE
4. write a decision and internal notes

The Co-Editor must explain the reason for agreement or override.

### P4 - Parent-Agent Summary

The parent agent must create a summary with:

- recommendation distribution
- consensus objections
- disagreement structure
- collective omissions
- decision path
- next actions
- issues requiring human judgment

## Econometrica Bar

All high-stakes panels should evaluate three dimensions:

1. Conceptual novelty: the paper offers a research object, mechanism, or framing not naturally reproduced by existing theory.
2. Deep result: at least one nontrivial theorem, identification result, equilibrium insight, or proof strategy carries real bite.
3. Economic interpretation: the result changes how economists understand, measure, predict, or regulate something important.

For each dimension, panelists should score 1-5 and explain the score.

## Recommendation Scales

### Idea and Model Decisions

```text
Kill < Park < Retarget < Pivot < Refine < Invest
```

### Verification Decisions

```text
Fatal Gap < Counterexample Found < Needs Assumption < Partially Verified < Verified
```

### Manuscript Review Decisions

```text
Reject < Reject and Resubmit < Major Revision < Minor Revision < Accept
```

Distinguish `Reject and Resubmit` from `Major Revision` carefully:

- `Reject and Resubmit`: structural redesign is required; the resubmission should be treated as a new paper.
- `Major Revision`: the paper is close enough that the core contribution is conditionally acceptable, with fixable problems.

## Location and Evidence Requirements

Every major concern must cite specific evidence:

- line number if available
- section/subsection
- theorem/proposition/lemma/corollary label
- equation label
- assumption name
- model primitive
- table/figure
- closest-paper comparison

If the concern involves a formula, restate the relevant formula or condition so the AE and Co-Editor can verify it.

## Confidence Labels

Each panelist must self-label:

```text
Confidence: High / Medium / Low
```

They must explain uncertainty sources:

- unavailable literature
- missing proof details
- inability to run code
- ambiguity in notation
- unclear model primitives
- limited domain expertise

## Math Rigor Checklist

The math-rigor referee should actively look for:

- fixed point theorem assumptions
- domain invariance
- compactness
- continuity
- convexity or concavity
- contraction constants
- Jacobian invertibility
- implicit/inverse function theorem conditions
- boundary behavior
- spectral radius and Neumann series conditions
- measurable selection
- integrability
- Fubini/Tonelli usage
- dominated convergence
- equilibrium selection
- assumptions that package the main difficulty
- hidden gaps behind "obvious", "standard", "by continuity", "clearly", or "straightforward"

## Tool Integration

When a panel reaches a mathematical or numerical claim:

- use `ECONOMETRICA_VERIFICATION_WORKFLOW.md`
- use Python for quick symbolic/numerical checks
- use Mathematica for assumption-heavy symbolic simplification when available
- use Lean for compact lemmas where formalization is realistic
- record tool outputs in `verification_log.md`
- do not claim verification unless the tool actually ran

## Human Gates

The system must stop for human judgment before:

- committing to a new project
- choosing the model to develop
- adding economically meaningful assumptions
- changing the main theorem
- changing the contribution lock
- deciding to submit, pivot, retarget, split, or kill
- accepting a simulated editorial decision as action-guiding

## Prompt Template

```text
Read ECONOMETRICA_PANEL_PROTOCOL.md. Run a [Idea/Model/Verification/Review/Revision] Panel in [Blind/Context/Literature] Mode for [target object]. Define allowed and prohibited materials, produce independent referee reports, then AE synthesis, then Co-Editor decision, then parent-agent summary. Stop at the human gate.
```

