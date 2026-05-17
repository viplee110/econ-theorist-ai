# Independent Panel Protocol for Target-Calibrated Frontier Research

Version: 2026-05-08

This protocol generalizes a stronger simulated review methodology into a reusable decision procedure for the entire research lifecycle. Use it whenever the system must make a high-stakes judgment about an idea, model, derivation, manuscript, referee report, or revision plan.

Target journal changes calibration, not quality. Panels may calibrate reader path, referee mix, exposition style, and fit standard to Econometrica, RAND, JET, Theoretical Economics, GEB, ReStud, AER, or another confirmed target, but they must not lower rigor, theorem discipline, novelty scrutiny, absorption testing, or proof verification.

The core pattern is:

```text
independent specialist judgments
-> explicit disagreement
-> Associate Editor synthesis
-> Co-Editor decision
-> parent-agent summary of consensus, disagreement, omissions, and next actions
```

The purpose is not to make the AI "vote." The purpose is to reduce self-confirmation, preserve real disagreement, and force decisions to be tied to specific claims, assumptions, equations, theorems, manuscript locations, or literature comparisons.

## Dynamic Panel Configuration

Before writing any individual referee prompt or running a panel, create or update a panel configuration file:

- `panel_reports/panel_config.md` for idea, model, verification, and revision panels.
- `referee_reports/round_N/panel_config.md` for simulated manuscript reviews.

Use the project-level `field_profile.md` and `target_journal_profile.md` when they exist and are still current. If they do not exist, create provisional profiles from the target material, closest-literature search, theorem package, target audience, and paper-specific evidence before assigning roles.

Use `literature_evidence_ledger.md` as the evidence ledger for closest-paper, anchor-paper, absorption-threat, and style-anchor claims. If a panel relies on such a paper and the ledger has no entry for it, the relevant field, target, absorption, calibration-anchor, or style judgment must be marked provisional.

The panel configuration must infer the narrowest defensible research field, confirmed target, target audience, and closest literature themes from the target material and the current profiles. Do not hard-code IO, search theory, network theory, contract theory, asset pricing, econometrics, behavioral economics, RAND, JET, GEB, or any other field or journal unless the manuscript, model, target profile, or closest-literature comparison actually warrants it.

The human should confirm the field profile and target journal profile once near the start of a project or before the first high-stakes panel. Later panels inherit those confirmed profiles. Reopen field or target confirmation only when new evidence changes the likely assignment: a closer substitute paper is found, the primitive or theorem direction changes materially, the target journal or target audience changes, the user disputes the classification, or a closest-literature/absorption/fit referee says the current profile makes the absorption or target-fit test unreliable.

The parent agent must finish and save `panel_config.md` before writing any individual referee prompt. Each referee prompt must be generated from that saved configuration. Prior rounds, historical review methodology files, or examples may be used only as evidence about earlier work, not as role templates, unless the current `panel_config.md` independently justifies the same assignments.

Minimum `field_profile.md` schema:

```text
Project or candidate:
Status: Confirmed / Provisional / Stale / Reopen requested
Human confirmation:
Primary field and subfield:
Adjacent fields:
Closest literature themes:
Nearest substitute papers and evidence status:
Absorption-risk theory families:
Method, mechanism, application, or institutional lens:
Main technical risk:
Field-sensitive role mapping:
  Referee 1 primary-field role:
  Referee 2 closest-literature or adjacent-field role:
  Referee 3 method/mechanism/application/institutional role:
Functional role slots retained:
  Referee 4 risk/rigor role:
  Referee 5 Scientific Judge / Idea Critic:
  Referee 6 Advocate / Best-Case Reader:
  Associate Editor and Co-Editor:
Uncertainty and missing evidence:
Reopen triggers:
```

Minimum `target_journal_profile.md` schema:

```text
Project or candidate:
Status: Confirmed / Provisional / Stale / Reopen requested
Human confirmation:
Primary target:
Stretch target:
Fallback target:
Target audience:
Fit standard:
Quality floor:
Theorem rigor expectation:
Reader path:
Referee mix implications:
Style calibration implications:
What must improve to move upward:
What would trigger retargeting:
Evidence used:
Missing evidence:
Reopen triggers:
```

The configuration must include:

- detected primary field and subfield
- evidence used for the field and subfield classification
- field-profile source: confirmed, provisional, or reopened for confirmation
- target-journal-profile source: confirmed, provisional, or reopened for confirmation
- confidence in the classification and main classification uncertainty
- closest literature themes and nearest substitute papers if known
- main contribution type: theory, econometrics, empirical, experimental, computational, institutional, or mixed
- central method or model class
- main technical risk: proof, identification, equilibrium existence, computation, data, measurement, institutional interpretation, or novelty
- selected referee roles and why each role is necessary
- target-calibrated referee mix and fit standard
- allowed materials, prohibited materials, and web/search policy
- execution mode: parallel independent agents if available; serial isolated simulation otherwise

For Review Panels, the default role logic is:

- Referee 1: primary-field specialist selected from the detected narrow field.
- Referee 2: closest-literature or adjacent-field specialist selected from the nearest substitute literature.
- Referee 3: method, mechanism, application, or institutional specialist selected from the manuscript's actual contribution.
- Referee 4: rigor specialist selected from the main risk type, such as mathematical proof, econometric identification, computation, empirical design, experimental design, or institutional interpretation.
- Referee 5: Scientific Judge / Idea Critic who runs the Nugget Test, Occam Test, defensive dilution check, and deep primitive potential check.
- Referee 6: Advocate / Best-Case Reader who argues for acceptance if acceptance were required, and states the strongest defensible "why should we care?" case in the paper's own terms.

If the target spans multiple fields, the panel must explain the tradeoff and choose the referee mix that is most likely to reveal fatal objections, not the mix that is easiest for the AI to simulate.

For Idea, Model, Verification, and Revision Panels, the role descriptions below are functional slots rather than fixed field assignments. The `panel_config.md` must specialize each slot to the detected field, literature, method, and risk before execution. For example, "closest-literature specialist" is not enough; the configuration should state which closest literature family the specialist represents and why.

Minimum `panel_config.md` schema:

```text
Target:
Panel type and information mode:
Field profile source and status:
Target journal profile source and status:
Confirmed primary target:
Stretch and fallback targets:
Target audience and quality floor:
Detected primary field and subfield:
Evidence for classification:
Classification confidence and uncertainty:
Closest literature themes / nearest substitutes:
Literature evidence ledger status:
Candidate geometry if applicable:
Contribution type:
Central method or model class:
Main technical risk:
Target-calibrated calibration anchors (required for Review Panels):
Control-paper calibration plan (optional but recommended):
Allowed materials:
Prohibited materials:
Web/search policy:
Execution mode:
Referee assignments:
AE and Co-Editor instructions:
Field confirmation needed before execution?:
Target confirmation needed before execution?:
Risks of this assignment:
```

## Calibration Anchors and Control-Paper Checks (Review Panels)

Simulated review has a strong reject prior. Without target calibration, a panel can become stricter than the journal it aims to simulate or misread the paper through the wrong audience.

### Calibration anchors (required)

For every Review Panel, `referee_reports/round_N/panel_config.md` must include:

- 2-3 **target-calibrated calibration anchors**: short descriptions of published papers that match the confirmed target, field, method, and contribution type.
- A sentence instructing referees to calibrate their "fit for the confirmed target" judgment **against the anchors**, not an idealized standard.
- If the confirmed primary target is RAND, anchors should prioritize RAND or nearby IO/applied-theory papers when they match the paper's field and method; use Econometrica or TE anchors only as stretch-target calibration.

Rules:

- Do not fabricate citations. If anchors cannot be named with high confidence, list them as TODOs and state what the anchors should be (topic/method).
- Every named calibration anchor must have a `literature_evidence_ledger.md` entry. If it does not, keep the anchor as provisional and do not use it as settled evidence about fit, style, or contribution.
- Anchors are for calibration, not for claiming novelty. Novelty remains a separate audit.
- A non-Econometrica target does not relax the quality floor: weak theorem bite, fake novelty, defensive complexity, or unverified claims remain fatal or near-fatal concerns.

### Control-paper calibration (recommended)

Periodically run the same Review Panel protocol on a **published paper from the confirmed target or stretch target** (author/title removed if possible) and record the decision distribution.

- If the panel rejects a known-accepted paper, treat the panel as miscalibrated and discount "reject" language in subsequent simulations.
- Save results in a local `panel_calibration_log.md` in the paper project (not in this workflow repo).

## Execution Mode

Prefer real parallel independence when the runtime supports agent delegation. On models or IDEs with native agents, such as future GPT-5.5-class or Claude/Opus-class agentic runtimes when available, the referee reports should be run as parallel, isolated workers by default:

- Each referee receives the same allowed materials and its assigned role from `panel_config.md`.
- Referees must not read other referee outputs.
- The Associate Editor starts from an independent judgment before reading referee reports.
- The Co-Editor starts from an independent judgment before reading the AE and referee reports.

When the runtime does not provide true agents, simulate independence serially:

- Run each referee in a separate prompt block.
- Do not show earlier referee outputs to later referees.
- Save each report before starting the next one.
- Only the AE and Co-Editor may read the full report set at their synthesis stages.

Never claim true parallel independence unless the environment actually ran separate agents or isolated workers.

## When To Use

Use this protocol for:

- idea kill tests
- broad topic screening
- primitive hunting and theorem generation
- tractable model selection
- first-pass theorem or equilibrium assessment
- mathematical proof audits
- target-calibrated simulated reviews
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
- absorption-family identification

Rules:

- Web search or external paper lookup should be used when available.
- Closest literature themes and absorption families must be updated from the papers actually found, not fixed from a prewritten field list.
- If web/search tools are unavailable, mark the literature classification and any absorption conclusion as provisional.
- Every literature claim must be labeled as verified, unverified, or inferred.
- Every closest-paper, anchor-paper, absorption-threat, or style-anchor claim must be backed by `literature_evidence_ledger.md`, or the downstream conclusion remains provisional.
- Missing citations should be marked as TODO rather than invented.

## Panel Types

### Idea Panel

Use before committing to a paper.

Roles:

- Referee 1: economic importance and field relevance.
- Referee 2: closest-literature, novelty risk, and absorption by existing theory.
- Referee 3: tractability and model feasibility.
- Referee 4: hostile editor focused on fatal objections.
- Associate Editor: synthesizes the four reports and recommends Proceed, Pivot, Narrow, Split, Park, Kill, or Retarget.
- Co-Editor: independently decides whether to accept the AE recommendation or override it.

Outputs:

- `panel_reports/panel_config.md`
- `panel_reports/idea_referee_1.md`
- `panel_reports/idea_referee_2.md`
- `panel_reports/idea_referee_3.md`
- `panel_reports/idea_referee_4.md`
- `panel_reports/idea_ae_report.md`
- `panel_reports/idea_co_editor_decision.md`

### Model Panel

Use after candidate models exist.

Roles:

- Referee 1: minimalist tractability and baseline clarity, specialized to the model class in `panel_config.md`.
- Referee 2: economic mechanism and comparative statics, specialized to the detected field.
- Referee 3: novelty and absorption risk relative to the closest canonical or substitute models.
- Referee 4: rigor specialist selected from the candidate model's main risk, such as existence, uniqueness, fixed point, IFT, contraction, boundary behavior, computation, or assumption packaging.
- Model Base Architect / Economic Naturalness Reader: checks whether the model base is built from a smallest economically interpretable example, whether user-supplied model elements are still provisional or confirmed, whether simpler models fail for economic reasons, and whether proof machinery is entering before economic necessity has been explained.
- Associate Editor: selects Invest, Refine, Pivot, Demote to Benchmark, Park, or Kill for each model.
- Co-Editor: decides which model, if any, should enter the pre-paper model-note stage.

Outputs:

- `panel_reports/panel_config.md`
- `panel_reports/model_referee_1.md`
- `panel_reports/model_referee_2.md`
- `panel_reports/model_referee_3.md`
- `panel_reports/model_referee_4_rigor.md`
- `panel_reports/model_base_architect.md`
- `panel_reports/model_ae_report.md`
- `panel_reports/model_co_editor_decision.md`

### Primitive Hunter / Theorem Generator Panel

Use before model selection when the current project risks local repair, weak theorem search, or reduced-form primitives. This panel does not review or revise a manuscript. It searches for deeper primitives and non-neighborhood theorem directions.

Core questions:

- What is the deepest economic primitive in the current idea or paper?
- Is the valuable object being treated as reduced-form rather than generated by the model?
- If the main theorem is weak, should the project change theorem, change model, or keep the question but change primitive?
- Can the panel generate three non-neighborhood models rather than small variants of the current model?
- Is each candidate a local extension, recombination, possible frontier spike, absorbed benchmark, clever but shallow, or hidden gem?
- What is the most informative next test for each serious candidate?

Roles:

- Hunter 1: primitive archaeologist who strips away labels and identifies the irreducible economic object.
- Hunter 2: endogenization designer who asks which reduced-form object must be generated inside the model.
- Hunter 3: non-neighborhood model generator who proposes three models outside the current local basin.
- Hunter 4: theorem generator who states candidate theorem sentences for each primitive/model direction.
- Scientific Judge: runs the Nugget, Occam, absorption, and deep primitive potential tests on the generated directions; it cannot kill a non-mainstream exploration or possible frontier spike merely for being non-mainstream, weird, or initially hard to position.
- Associate Editor: recommends Keep Question / Change Primitive / Change Theorem / Change Model / Park / Kill.
- Co-Editor: decides which primitive-theorem direction, if any, should enter D4 model tournament.

Outputs:

- `panel_reports/panel_config.md`
- `panel_reports/primitive_hunter_report.md`
- updated `model_candidates.md`
- updated `theorem_candidates.md`
- updated `absorption_tests.md`

Each serious direction in the output must include:

```text
Candidate geometry:
Belief state:
  evidence status: verified / inferred / speculative
  main uncertainty:
  most informative next test:
  kill condition:
  spike protection status:
```

### Verification Panel

Use for theorem, proposition, equilibrium, identification, or comparative-static checks.

Roles:

- Referee 1: re-derivation from primitives.
- Referee 2: symbolic and numerical counterexample search.
- Referee 3: proof structure and hidden assumptions.
- Referee 4: formalization triage, Lean suitability, and rigor focus selected from the claim's main risk in `panel_config.md`.
- Associate Editor: classifies each claim as Verified, Partially Verified, Needs Assumption, Counterexample Found, or Fatal Gap.
- Co-Editor: approves theorem restatement, proof repair path, or claim withdrawal.

Outputs:

- `panel_reports/panel_config.md`
- `panel_reports/verification_referee_1.md`
- `panel_reports/verification_referee_2.md`
- `panel_reports/verification_referee_3.md`
- `panel_reports/verification_referee_4_formal.md`
- `panel_reports/verification_ae_report.md`
- `panel_reports/verification_co_editor_decision.md`

### Review Panel

Use for target-calibrated simulated review.

Before assigning roles, create `referee_reports/round_N/panel_config.md` using the Dynamic Panel Configuration rules above.

Roles:

- Referee 1: primary-field specialist selected from the manuscript's narrowest defensible field.
- Referee 2: closest-literature or adjacent-field specialist selected from the nearest substitute literature.
- Referee 3: method, mechanism, application, or institutional specialist selected from the paper's actual contribution.
- Referee 4: rigor specialist selected from the main risk type: mathematical proof, econometric identification, computational reproducibility, empirical design, experimental design, or institutional interpretation.
- Referee 5: Scientific Judge / Idea Critic. This referee does not audit algebra. It judges taste, strategy, simplicity, deep primitive potential, whether the paper's nugget survives the revision process, and whether the target profile is being used to calibrate fit rather than lower quality. It may strongly oppose defensive dilution, fake novelty, weak theorem bite, and complexity shields, but it must not kill a non-mainstream exploration or possible frontier spike solely for being non-mainstream, weird, or initially hard to position. It must separately ask whether a primitive-theorem pair has enough depth, theorem bite, absorption escape, and follow-up fertility to warrant further discovery before rejection.
- Referee 6: Advocate / Best-Case Reader who argues for acceptance if acceptance were required, and states the strongest defensible "why should we care?" case in the paper's own terms.
- Associate Editor: independent read first, then synthesis of referee reports.
- Co-Editor: independent read first, then decision letter and internal notes.

Outputs:

- `referee_reports/round_N/referee_1.md`
- `referee_reports/round_N/referee_2.md`
- `referee_reports/round_N/referee_3.md`
- `referee_reports/round_N/referee_4_rigor.md`
- `referee_reports/round_N/referee_5_scientific_judge.md`
- `referee_reports/round_N/referee_6_advocate.md`
- `referee_reports/round_N/dilution_check.md`
- `referee_reports/round_N/associate_editor_report.md`
- `referee_reports/round_N/co_editor_decision.md`
- `referee_reports/round_N/00_summary.md`

The Referee 6 Advocate / Best-Case Reader role must write `referee_reports/round_N/referee_6_advocate.md`; do not rename the role without renaming the output consistently.

### Revision Panel

Use after reports exist but before major edits.

Roles:

- Referee 1: which objections are fatal.
- Referee 2: which objections are fixable without changing the contribution.
- Referee 3: which edits would dilute the core idea.
- Referee 4: which fixes require new assumptions, proofs, computations, citations, or a return to model discovery.
- Associate Editor: creates a ranked revision plan.
- Co-Editor: approves Revise, Pivot, Retarget, External Feedback, or Stop.

Outputs:

- `panel_reports/panel_config.md`
- `panel_reports/revision_triage.md`
- updated `risk_register.md`
- updated `revision_log.md`

### Exposition Editor / Elegant Reader

Use during Stage 6.5 Deep Style Anchor Pass or when the manuscript reads like a mechanical solution note even though the theorem and contribution may be sound. This is a light functional role, not a referee vote.

The Exposition Editor / Elegant Reader evaluates whether:

- the paper has a humane reader path
- the theorem appears as the answer to a real economic question
- assumptions are interpreted before being used
- proof roadmaps explain why the proof moves as it does
- prose avoids AI-list style and decorative rhetoric
- elegance is improving clarity rather than hiding weakness

Rules:

- This role cannot approve conceptual changes.
- It must not change theorem statements, assumptions, novelty claims, target-journal positioning, or unverified literature claims.
- It reads `style_anchor_notes/`, `style_anchor_matrix.md`, and `style_calibration.md` when they exist.
- It may use published papers as style anchors only to extract exposition architecture and exposition moves, not sentences, paragraph structures, or framing.
- It should check whether the anchor evidence is full-text, partial, or provisional, and whether any style claim lacks a `literature_evidence_ledger.md` entry.
- If it finds a structural issue, it routes to the Scientific Judge, Discovery D4-D6, or Stage 8 tree search rather than polishing.
- Its findings should be written into `style_calibration.md` or, if run inside a panel, summarized in the panel output.

## Generic Panel Phases

### P0 - Scope and Allowed Materials

Before running a panel, define:

- target object: idea, model, theorem, manuscript, review report, or revision plan
- field profile status: confirmed, provisional, stale, or reopened for human confirmation
- target journal profile status: confirmed, provisional, stale, or reopened for human confirmation
- dynamic referee configuration and execution mode
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

## Frontier-Level Quality Bar

All high-stakes panels should evaluate three dimensions. The confirmed target journal may change how these are explained to readers, but not whether they matter.

1. Conceptual novelty: the paper offers a research object, mechanism, or framing not naturally reproduced by existing theory.
2. Deep result: at least one nontrivial theorem, identification result, equilibrium insight, or proof strategy carries real bite.
3. Economic interpretation: the result changes how economists understand, measure, predict, or regulate something important.

For each dimension, panelists should score 1-5 and explain the score.

## Absorption and Main-Theorem Test

Idea and Model Panels must explicitly ask whether the candidate theorem is absorbed by existing frameworks. The required theorem sentence is:

```text
This paper proves X, and existing theory cannot obtain X because Y.
```

Absorption families to test must be derived from the closest-literature search and the papers actually found. Do not use a fixed field list as a substitute for identifying the nearest theory families for the user's topic.

The closest substitute papers and absorption threats used in this test must appear in `literature_evidence_ledger.md`. If they do not, the panel may still explain a provisional risk, but it must not present the absorption conclusion as final.

If the panel can reproduce the result by renaming variables inside a known framework, it should recommend `Demote to benchmark`, `Pivot`, `Park`, or `Kill`, not `Invest`. If the issue is that a key primitive is reduced-form, the panel should identify what must be endogenized before manuscript development.

## Model-Base Naturalness Test

Before a Model Panel recommends a candidate for D5 derivation or D7 pre-paper packaging, it must check:

- Is the candidate grounded in a smallest real-world scene or toy example?
- Are the agent set, timing, information, choices, state variables, frictions, and equilibrium concept necessary for the economic force?
- Which user-supplied model elements remain provisional modeling constraints rather than confirmed primitives?
- Why do simpler models fail?
- Does the model rely on fixed point, contraction, IFT, or existence machinery before explaining the economic object requiring consistency?
- If the model is mechanically formal, assumption-heavy, or lacks a clear toy example, route back to D4.5 rather than recommending formal derivation.

## Nugget and Occam Test

Every Review Panel and high-stakes Revision Panel must include a scientific-taste judgment. The judge should answer:

- What is the paper's nugget in one sentence without mathematical notation?
- Did the latest revision make the nugget shorter, sharper, and more surprising, or longer and more defensive?
- Is each additional variable, agent type, state, distributional assumption, or regularity condition necessary for the mechanism?
- Could the same insight be obtained from a simpler primitive or cleaner model?
- Does the paper contain a theorem package without one central theorem?
- Does a non-mainstream direction have deep primitive potential, theorem bite, or a non-absorbed mechanism that warrants further discovery before rejection?

If the contribution sentence requires many clauses such as "under the specific condition that..." or "provided that..." to sound true, label the issue `Defensive Dilution`. If complexity is essential, the judge must say exactly what economic work it performs. If complexity mainly protects a fragile result, the judge should recommend `Pivot`, `Demote to Benchmark`, or `Reject and Resubmit` rather than local repair.

Scientific taste is a filter, not the sole objective. The judge can reject defensive dilution, fake novelty, or a complexity shield, but must separately evaluate deep primitive potential before recommending Kill/Pivot for a non-mainstream exploration.

Target-journal calibration is not a quality discount. If the primary target is RAND, GEB, a field journal, or another non-Econometrica outlet, the Scientific Judge must still flag weak theorem bite, old-theory absorption, fake novelty, unverified claims, and defensive complexity. The appropriate recommendation may be `Retarget`, but only after explaining whether the issue is fit, reader path, or genuine quality.

## Contribution-Lock Dilution Check (Hard Ratchet)

When a paper project uses `contribution_lock.md`, every Review Panel must include a **separate dilution check artifact** produced by the parent agent:

- Output file: `referee_reports/round_N/dilution_check.md`
- Inputs allowed: the current manuscript + `contribution_lock.md` (and nothing else).
- Output: for each locked statement (Central question / Main theorem sentence / Non-substitutable insight / Reader belief update), score 1-5 how strongly the current manuscript delivers it, and explicitly flag any **weakening relative to the lock** as `Defensive Dilution`.

Rules:

- This is not a rewrite step. It is a diagnostic guardrail.
- Referees do **not** read `contribution_lock.md` and do **not** read `dilution_check.md`.
- The Associate Editor and Co-Editor may read `dilution_check.md` during synthesis as a constraint: if the manuscript no longer delivers the locked contribution, the correct action is usually `Reject and Resubmit`, `Pivot`, or `Return to Discovery`, not additive local repair.

## Recommendation Scales

### Idea and Model Decisions

```text
Kill < Park < Retarget < Demote to Benchmark < Pivot < Refine < Invest
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

If the concern relies on a named closest paper, calibration anchor, absorption threat, or style anchor, cite the corresponding `literature_evidence_ledger.md` entry or mark the concern provisional.

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
- confirming a new or materially changed project-level field profile
- choosing the model to develop
- adding economically meaningful assumptions
- changing the main theorem
- changing the contribution lock
- deciding to submit, pivot, retarget, split, or kill
- accepting a simulated editorial decision as action-guiding

Every panel-facing human gate must be recorded before the next panel or revision step relies on it. Create `human_decisions.md` if it is missing, append the decision there, and update the panel-specific artifact that the decision controls, such as `field_profile.md`, `target_journal_profile.md`, `style_calibration.md`, `panel_reports/panel_config.md`, `referee_reports/round_N/panel_config.md`, `contribution_lock.md`, `revision_tree.md`, or `risk_register.md`.

If the user reverses a prior panel decision, preserve the earlier decision and add a reversal entry:

```text
Decision reversal / Override
Date:
Previous decision:
New decision:
Reason:
Affected panel artifacts:
Required reruns or rechecks:
```

## Prompt Template

```text
Read ECONOMETRICA_PANEL_PROTOCOL.md. Run a [Idea/Model/Verification/Review/Revision] Panel in [Blind/Context/Literature] Mode for [target object]. Reuse confirmed field_profile.md and target_journal_profile.md when current; if either is missing, provisional, stale, or marked `Reopen requested`, create or update it from closest-literature, theorem, target-audience, and manuscript evidence and stop for confirmation before running field- or target-sensitive roles. Then create panel_config.md by detecting the narrowest field, confirmed target, target audience, closest literature themes, main method, contribution type, and main risk. Assign specialist roles dynamically from panel_config.md. Use parallel isolated agents if available; otherwise use serial isolated referee prompts. Define allowed and prohibited materials, produce independent referee reports, then AE synthesis, then Co-Editor decision, then parent-agent summary. Stop at the human gate.
```
