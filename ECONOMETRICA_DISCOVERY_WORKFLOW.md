# Human-AI Discovery Workflow for Econometrica-Level Theory Projects

Version: 2026-05-08

This file is a pre-manuscript discovery protocol. Use it before `ECONOMETRICA_AI_HUMAN_WORKFLOW.md` when the project is still at the topic, idea, model, or early theorem stage.

The goal is to help the human and AI search broadly without fooling themselves. The agent should generate many candidates, impose tractability and novelty constraints, attempt simple derivations, run hostile kill tests, and stop at human decision gates.

This workflow supports three starting modes:

- `Field mode`: the human knows the broad field but not the exact question.
- `Idea mode`: the human has a rough idea or mechanism.
- `Open mode`: the human wants AI to explore candidate topics from scratch.

For high-stakes screening, model selection, and investment decisions, also read `ECONOMETRICA_PANEL_PROTOCOL.md`. Use independent panels rather than a single-agent judgment when deciding whether to invest in an idea or model.

## Core Principle

AI can expand the search frontier, but it cannot certify that a topic is unstudied, important, or Econometrica-level. Treat all generated topics as hypotheses. A candidate survives only if it passes novelty, tractability, economic importance, and execution tests.

Nonconvex discovery expands candidate generation; it does not certify quality. Tree search remains the search structure. Nonconvex discovery is an internal branch-generation and false-kill prevention discipline inside D1, D4, Primitive Hunter, and D6.

Specificity is not stage advancement. Stage is determined by artifacts and human gates, not by how formal the user's language sounds. User-supplied agents, timing, information, payoffs, equilibrium concepts, or assumptions are provisional modeling constraints until the model base is confirmed.

Model discovery should move from examples to theory. Exhaust broadly at the model-skeleton level; derive narrowly at the formal level. A model is not ready because it is formal; it is ready when its smallest version explains the economic force.

Main-theorem-first rule: do not move into a full manuscript until the project has a candidate main theorem that can be stated in one sharp sentence:

```text
This paper proves X, and existing theory cannot obtain X because Y.
```

The default discovery output is a 5-8 page model note, not a polished paper. The note should contain only the question, closest substitutes, one model, one main theorem candidate, proof status, and killer intuition. Manuscript development begins only after the theorem survives absorption and model-competition gates.

## Required Artifacts

Maintain these files during discovery:

- `discovery_state.md`: current mode, constraints, active candidates, last human decision.
- `topic_longlist.md`: broad list of candidate topics and mechanisms.
- `topic_shortlist.md`: surviving candidates after screening.
- `model_candidates.md`: structured model sketches for each surviving candidate.
- `primitive_hunter_report.md`: deepest primitive, reduced-form object audit, and non-neighborhood model directions.
- `generality_ledger.md`: running record of generality losses, special-case restrictions, and whether each restriction makes the nugget sharper.
- `model_tournament.md`: side-by-side comparison of model variants and why weaker variants were killed or demoted.
- `model_base_design.md`: example-to-theory model base design, skeleton funnel, failed simpler alternatives, recommended baseline, and human confirmation status.
- `heuristic_derivation.md`: economic derivation path from toy examples to formal objects before proof machinery begins.
- `theorem_candidates.md`: candidate main theorems, theorem sentences, proof status, and failure modes.
- `absorption_tests.md`: tests for whether the idea is absorbed by existing theoretical families.
- `derivation_notes.md`: first-pass derivations, algebra, proof attempts, and failure points.
- `literature_probe.md`: closest literatures, nearest substitutes, novelty risks, and citation TODOs.
- `literature_evidence_ledger.md`: verified source records for closest papers, anchor papers, absorption threats, and style anchors.
- `field_profile.md`: project-level field configuration confirmed by the human when possible.
- `target_journal_profile.md`: target-journal calibration, including primary target, stretch target, fallback target, target audience, fit standard, and quality floor.
- `idea_kill_tests.md`: hostile referee/editor tests for each candidate.
- `pre_paper_model_note.md`: 5-8 page note created only after a candidate passes the main-theorem gate.
- `spike_dossier.md`: optional dossier created only when a possible frontier spike survives D6 and needs focused development.
- `human_decisions.md`: human choices, taste judgments, pivots, and reasons.

## Exploration Quota

D1, D4, and any Primitive Hunter / Theorem Generator Panel must preserve at least 1-2 non-mainstream but internally coherent directions until they have been tested for deep primitive potential, theorem bite, and absorption risk.

For every exploration direction, record:

- deep primitive
- possible theorem sentence
- absorption risk
- why this is not just a local variant of the current model or a nearby paper

Do not kill an exploration-quota variant merely because it does not look like mainstream taste. It can be killed only after the workflow explains why the primitive is shallow, the theorem has low bite, the direction is absorbed by closest literature, or the assumptions become artificial.

## Nonconvex Branch Generation

D1, D4, and Primitive Hunter should classify serious candidates by candidate geometry:

```text
local extension
recombination
possible frontier spike
absorbed benchmark
clever but shallow
hidden gem
```

Possible frontier spike protection is not acceptance. A possible frontier spike cannot be killed merely for weirdness, non-mainstream taste, or weak initial positioning. It can be killed after tests show shallow primitive, weak theorem bite, absorption by existing theory, artificial assumptions, infeasible proof, or unacceptable legibility cost.

Use these mutation operators when the search is trapped in local repair or when discovery breadth matters:

```text
primitive mutation
endogenization mutation
timing mutation
information mutation
objective mutation
equilibrium-concept mutation
boundary mutation
duality mutation
field-transfer mutation
```

Reuse existing artifacts:

- Put the frontier map in `literature_probe.md` and `literature_evidence_ledger.md`.
- Put the mutation queue in `primitive_hunter_report.md`.
- Create `spike_dossier.md` only if a possible frontier spike survives D6.
- Put convexification plans in `model_tournament.md` or `contribution_lock.md`.
- Put negative results in `idea_kill_tests.md`.

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
- confirmation of the project-level field profile before high-stakes panels rely on it

## Human Gate Persistence

Human gate outcomes are persistent project state, not chat memory. Before proceeding past a gate, create `human_decisions.md` if it is missing, write the outcome there, and update the active artifact affected by the gate, such as `discovery_state.md`, `topic_shortlist.md`, `field_profile.md`, `target_journal_profile.md`, `model_tournament.md`, `absorption_tests.md`, `pre_paper_model_note.md`, or `project_state.md`.

Use this entry format in `human_decisions.md` when useful:

```text
Decision record
Date:
Stage or gate:
Decision:
Reason:
Affected artifacts:
Supersedes:
Next checks:
```

Human decisions are append-only by default. If the user reverses or overrides a prior choice, do not delete the old decision. Add a reversal entry and update the current-state files so later workflow stages know which decision controls.

```text
Decision reversal / Override
Date:
Previous decision:
New decision:
Reason:
Affected artifacts:
Required updates or rechecks:
```

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
- If the user supplies agents, timing, information, payoffs, equilibrium concepts, or assumptions, record them as `provisional modeling constraints`, not confirmed primitives.
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
Deep primitive:
Possible theorem sentence:
Absorption risk:
Why not local variant:
Why it might matter:
Closest literature families:
Candidate geometry:
Evidence status: verified / inferred / speculative
Main uncertainty:
Most informative next test:
Kill condition:
Spike protection status:
Tractability guess:
Novelty risk:
Execution risk:
Exploration quota status:
One-sentence pitch:
```

Rules:

- Do not repeat minor variants as separate candidates.
- Prefer mechanisms that could change a specialist's belief.
- Include some high-risk/high-upside candidates.
- Include some clean and tractable candidates.
- Include at least 1-2 non-mainstream but internally coherent exploration-quota candidates when the search space permits.
- Flag candidates that sound clever but not important.
- Classify each serious candidate by candidate geometry: local extension, recombination, possible frontier spike, absorbed benchmark, clever but shallow, or hidden gem.
- Use candidate geometry to diversify branch generation and prevent false kills; it is not evidence that a candidate is high quality.

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
- Create `topic_shortlist.md` with 5-10 surviving directions for broad Field/Open discovery. For a specific fuzzy idea, create 12-24 mechanism routes and screen them to 4-6 promising directions before model-base construction.

Human gate:

The human selects 1-3 candidates for model sketching.

Panel option:

- If the user asks whether a topic is worth pursuing, run an Idea Panel from `ECONOMETRICA_PANEL_PROTOCOL.md` after D2.
- Use Blind Mode when judging the idea itself.
- Use Literature Mode when the main uncertainty is whether the idea is already known.

## Stage D3 - Literature Probe

Autonomy: Checkpoint

Purpose:

Avoid rediscovering known papers.

AI tasks:

- Create `literature_probe.md`.
- Create or update `literature_evidence_ledger.md`.
- Create or update `field_profile.md`.
- Create or update `target_journal_profile.md` when enough evidence exists to recommend a target ladder.
- For each shortlisted candidate:
  - identify provisional closest literature families from the idea and model primitives
  - list likely nearest substitute papers
  - generate search queries for Google Scholar, Semantic Scholar, RePEc, NBER, CEPR, SSRN, arXiv, and author pages
  - when web/search tools are available, run the searches and record the papers actually found
  - update the closest literature families using the search results rather than relying only on memory
  - describe what would kill the novelty claim
  - describe what would preserve the contribution
- In `field_profile.md`, state:
  - primary field and subfield
  - adjacent fields and closest literature themes
  - absorption-risk theory families derived from the papers actually found
  - method, mechanism, application, or institutional lens
  - main technical risk
  - proposed Referee 1-3 field-sensitive roles
  - which role assignments are field-sensitive and which are functional
  - confidence, uncertainty, and evidence that would reopen the classification
- Separate verified facts from AI inferences.
- Mark all unverified references as TODO.
- Every closest-paper, anchor-paper, absorption-threat, or style-anchor claim must have a `literature_evidence_ledger.md` entry before downstream artifacts treat it as confirmed.
- Use this minimum ledger entry:

```text
Paper title:
Authors:
Year:
Publication / working paper status:
Source opened:
DOI / journal / NBER / SSRN / RePEc / publisher link:
Verified claim from source:
AI inference:
Relation to current project:
  nearest substitute / ancestor / method anchor / style anchor / absorption threat / adjacent literature
Novelty threat:
Confidence:
Unverified TODO:
```

- If a relevant paper has not been recorded in the ledger, mark the corresponding `field_profile.md`, `target_journal_profile.md`, `absorption_tests.md`, `panel_config.md`, and `style_calibration.md` judgment provisional.
- Default to search/open/verify/record evidence, not bulk-downloading PDFs.
- Download only open-access papers, user-provided PDFs, or papers explicitly authorized by the user. If downloaded, store them in `literature_cache/` and record source and permission status in the ledger.
- Extract model, proof, and exposition moves from papers; do not copy copyrighted prose or treat an anchor as a prose template.
- Recommend a provisional target ladder using the idea, field profile, closest-literature themes, contribution type, theorem evidence if available, and absorption risk:
  - Econometrica, Theoretical Economics, or JET when the primitive is deep, the theorem is general, theorem bite is high, and absorption risk is low.
  - RAND when the economic mechanism has IO, platform, market design, regulatory, institutional, or applied-theory relevance with clear comparative statics and an applied-theory reader path.
  - GEB when strategic interaction or a game-theoretic mechanism is central.
  - ReStud, AER, or QJE theory-style when the question is broad, the mechanism is clean, and the result travels beyond a narrow field.
  - Field journal or working-paper route when the idea is valuable but theorem bite, novelty, or generality is not yet top-field-ready.
- Treat target-level judgments as provisional until the package contains enough evidence: an idea dossier, a model base or model-base audit, a theorem sentence or theorem candidate, and closest-literature evidence. Do not infer target-journal potential from the idea alone.
- State explicitly that target journal changes calibration, not quality; no target may bypass model tournament, absorption testing, generality ledger, main-theorem gate, or proof verification.

Human gate:

The human should inspect the top substitute papers or ask the AI to help locate them. The human should confirm or correct `field_profile.md` once before high-stakes panels rely on it, and the agent should record that confirmation in both `field_profile.md` and `human_decisions.md`. If `target_journal_profile.md` is created or materially changed, the human should also confirm or correct the target ladder, and the agent should record that confirmation in both `target_journal_profile.md` and `human_decisions.md`. Do not trust novelty until this gate is passed. If web/search tools are unavailable, label the literature probe, field profile, target profile, panel role configuration, and all downstream absorption tests `provisional`.

Once confirmed, later Idea, Model, Verification, Review, Style Calibration, and Revision Panels should inherit `field_profile.md` and `target_journal_profile.md` rather than asking for confirmation again. Reopen the field or target gate only if a closer substitute paper appears, the primitive or theorem direction changes materially, the target audience changes, the user disputes the classification, or a panelist explains why the current profile makes the absorption or fit test unreliable.

## Stage D4 - Primitive Hunting and Model Candidate Generation

Autonomy: Auto

Purpose:

Find the deepest primitive, then generate broad model skeletons before any paper draft or formal derivation exists.

AI tasks:

- Create or update `primitive_hunter_report.md`.
- Create or update `generality_ledger.md`.
- Create `model_candidates.md`.
- Create or update `model_tournament.md`.
- Before generating local variants, identify:
  - the deepest primitive
  - the object currently treated as reduced-form
  - the primitive that must be endogenized for the theorem to be non-substitutable
  - whether to change theorem, change model, or keep the question but change primitive
- For each selected direction, generate a wide set of cheap model skeletons before formal derivation:
  - 20-40 model skeletons total, or 10-20 per selected direction when there are multiple directions
  - local extension, recombination, possible frontier spike, hidden-gem, and absorbed-benchmark candidates where appropriate
  - alternative agents, timing, information, choice objects, state variables, market objects, frictions, equilibrium concepts, and welfare/comparative-static objects
  - primitive, endogenization, timing, information, objective, equilibrium-concept, boundary, duality, and field-transfer mutations when local repair is a risk
- Screen the skeletons with an economic filter before any formal proof attempt:
  - keep 6-10 semi-formal baselines
  - keep 3-5 example-to-theory candidates
  - select only 1-3 formal derivation candidates for D5
- Preserve 1-2 non-mainstream but internally coherent directions from the exploration quota unless D1 or the Primitive Hunter already killed them for documented primitive, theorem, or absorption reasons.
- For each exploration-quota direction, state the deep primitive, possible theorem sentence, absorption risk, and why it is not a local variant.
- When local repair is a risk, use the mutation operators from the Nonconvex Branch Generation section before adding auxiliary features to the current model.
- For each possible frontier spike, identify the primitive-theorem pair, closest absorption threat, proof bottleneck, and legibility cost before any kill decision.

Model template:

```text
Model ID:
Candidate topic:
Core question:
Real-world scene:
Economic tension:
Provisional modeling constraints:
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
Possible theorem sentence:
Candidate geometry:
Belief state:
  evidence status: verified / inferred / speculative
  main uncertainty:
  most informative next test:
  kill condition:
  spike protection status:
Comparative statics:
Welfare or policy object:
Smallest example that makes the force visible:
Why simpler models fail:
Why tractable:
Likely proof technique:
What could go wrong:
Closest existing model:
Generality loss:
Why not local variant:
```

Tournament rule:

- Treat every model variant as competing to produce the main theorem.
- Do not repair a weak variant by adding features until at least one alternative model space has been tried.
- If two variants produce the same theorem, keep the simpler one and demote the other.
- If a variant only creates a theorem package of local sufficient conditions, label it `Local repair trap`.
- If the result follows from a named existing framework, label it `Absorbed benchmark` rather than a main model.
- Update `generality_ledger.md` whenever a variant becomes a special case, adds a distribution assumption, imposes a special graph structure, adds an agent or state, adds a regularity condition, or makes the theorem sentence longer.
- If the current winner is mechanically formal, assumption-heavy, lacks a clear toy example, has an unsharp theorem sentence, or relies on fixed point machinery before economic necessity is explained, expand the skeleton search rather than entering D5.

Absorption pre-test:

For each model variant, infer the closest classical theory families from the
topic, primitive friction, agents, information structure, market design, timing,
and predicted theorem. Ask whether the predicted result is essentially a
renaming or modest extension of one of those nearest theory families.

This inference must be checked against the live literature search in
`literature_probe.md` and `literature_evidence_ledger.md` when web/search tools
are available. If no search was run, or if the closest substitute is not recorded
in the ledger, record the theory-family classification as provisional and do not
use it as a final kill or invest decision.

If yes, the model can still be useful, but it cannot be the main theorem unless the note explains the non-absorbed element.

Tractability constraints:

- Prefer two or three agent types before many-type models.
- Prefer one central friction before multiple interacting frictions.
- Prefer closed-form or monotone comparative statics where possible.
- Avoid unnecessary dynamic state variables.
- Avoid assumptions that exist only to force the desired result.
- Make every assumption economically interpretable.
- Do not introduce fixed point, contraction, IFT, or existence-theorem language before explaining the economic object that requires consistency and why the simplest example points to that object.

Panel option:

- If the current primitive is unclear or appears reduced-form, run a Primitive Hunter / Theorem Generator Panel from `ECONOMETRICA_PANEL_PROTOCOL.md` before the Model Panel.
- If multiple model-base candidates survive, run a Model Panel from `ECONOMETRICA_PANEL_PROTOCOL.md` and include the Model Base Architect / Economic Naturalness Reader function.
- Require the math-rigor panelist to check fixed point, IFT, contraction, boundary behavior, equilibrium selection, and assumption packaging risks before a model is selected for the D7 pre-paper package.

## Stage D4.5 - Example-to-Theory Model Base Construction

Autonomy: Checkpoint

Purpose:

Turn the surviving skeletons into a minimal, economically natural model base before formal derivation. This stage is the bridge between primitive hunting and first-pass derivation.

Inputs:

- `topic_shortlist.md`
- `primitive_hunter_report.md`
- `model_candidates.md`
- `model_tournament.md`
- `literature_evidence_ledger.md`
- user-supplied provisional modeling constraints

AI tasks:

- Create or update `model_base_design.md`.
- Create or update `heuristic_derivation.md`.
- For each of the 3-5 leading example-to-theory candidates, write:
  - real-world micro scene
  - core economic tension
  - minimal agents, timing, information, choice object, state variable, friction, and object of interest
  - which user-supplied constraints are retained, relaxed, or rejected as premature
  - the smallest toy example that makes the mechanism visible
  - why simpler models fail
  - what general primitive the toy example suggests
  - likely theorem path and likely failure point
  - where formal machinery may enter, if it is economically necessary
- Recommend one baseline, one backup baseline, and one parked alternative when evidence supports them.

Required `model_base_design.md` sections:

```text
Model base status: provisional / human-confirmed / stale / reopen requested
Provisional modeling constraints:
Skeleton funnel:
  initial skeleton count:
  semi-formal baselines kept:
  toy examples kept:
Recommended minimal baseline:
Backup baseline:
Parked alternative:
Real-world scene:
Economic tension:
Minimal primitives:
Failed simpler alternatives:
Top toy examples:
Why this baseline is elegant:
Likely theorem path:
Likely failure point:
Human confirmation:
```

Required `heuristic_derivation.md` sections:

```text
Toy example:
Agent tradeoff:
Aggregate consistency or market pressure:
Equilibrium pressure:
Comparative-static intuition:
Where formal machinery enters:
What the heuristic does not prove:
```

Human gate:

Minimal Model Base Gate.

The system must present the minimal real-world scene, economic tension, which user constraints are retained or relaxed, the top 3-5 toy examples, the recommended model base, why simpler models fail, and the next theorem path. The human must confirm, edit, or reject the model base before D5 treats primitives, assumptions, or equilibrium concepts as durable state. Record the decision in `human_decisions.md` and update `model_base_design.md`.

## Stage D5 - First-Pass Derivation

Autonomy: Auto, but must be rigorous

Purpose:

Test whether any model has a real main theorem.

AI tasks:

- Read `model_base_design.md` and `heuristic_derivation.md` first, unless the user explicitly asked only to solve a given model mechanically.
- Do not treat primitives, assumptions, or equilibrium concepts as confirmed unless the Minimal Model Base Gate is passed or the file clearly marks them as provisional.
- Create or update `derivation_notes.md`.
- Create or update `theorem_candidates.md`.
- For each model variant, attempt a first-pass derivation.
- Write:
  - agent problem
  - objective functions
  - constraints
  - equilibrium conditions
  - candidate solution
  - main comparative static
  - proof sketch
  - candidate main theorem sentence
  - exact algebra where possible
  - conditions required
  - counterexample attempt
  - failure points

Required derivation discipline:

- Begin from the heuristic path: agent tradeoff, aggregate consistency or market pressure, equilibrium pressure, and comparative-static intuition.
- Use fixed point, contraction, IFT, or existence-theorem machinery only after stating why the economic object requires that tool.
- Every proposition must state its assumptions.
- Every comparative static must identify the derivative, monotone order, or argument used.
- Every proof sketch must state where each assumption enters.
- If a result follows almost immediately from an assumption, flag it as low contribution.
- If the result needs an unstated regularity condition, add it explicitly to `derivation_notes.md` and mark it as a risk.
- If the derivation adds a distribution assumption, special graph structure, extra agent, extra state, regularity condition, or longer theorem sentence, update `generality_ledger.md`.
- If algebra becomes messy, try a simpler model before adding assumptions.
- Try to construct at least one counterexample to the predicted proposition.
- If the proposition fails, record the failure rather than repairing silently.
- If the result is true but unsurprising under a known framework, demote it to a benchmark.
- If the model requires a reduced-form primitive to carry the whole contribution, record what primitive must be endogenized before manuscript development.

Output categories:

- `Main-theorem candidate`: clean result, plausible assumptions, nontrivial insight, and not absorbed by a known framework.
- `Promising but needs endogenization`: result is interesting, but a key primitive is still reduced-form.
- `Technically possible but weak`: solvable but low economic bite.
- `Absorbed benchmark`: result is useful but naturally reproduced by existing theory.
- `Too tailored`: result depends on artificial assumptions.
- `Too messy`: solution exists but not paper-tractable.
- `Fails`: proposition false or no clear result.

## Stage D6 - Absorption, Main Theorem, and Kill Test

Autonomy: Gate

Purpose:

Decide whether the candidate deserves manuscript investment or must return to model search.

AI tasks:

- Create `idea_kill_tests.md`.
- Create or update `absorption_tests.md`.
- Create or update `model_tournament.md`.
- Use `model_base_design.md` and `heuristic_derivation.md` to check whether the model base is economically natural before treating derivations as investable.
- Create or update `generality_ledger.md`.
- Use the latest `literature_evidence_ledger.md` before treating closest-paper, anchor-paper, or absorption-threat claims as confirmed.
- If a closest substitute or absorption threat is not recorded in `literature_evidence_ledger.md`, mark the corresponding absorption judgment provisional.
- Check whether `field_profile.md` is confirmed, provisional, stale, or marked `Reopen requested`. If it is missing, provisional, stale, or reopened, update it from the latest `literature_probe.md` and stop for field confirmation before treating absorption as final.
- Check whether `target_journal_profile.md` is confirmed, provisional, stale, or marked `Reopen requested`. If theorem quality, absorption risk, target audience, or field evidence materially changes the target ladder, update it and stop for target confirmation before treating journal fit as final.
- Do not skip absorption tests, model tournament, generality ledger, or main theorem gate because the target is RAND, GEB, a field journal, or any non-Econometrica outlet.
- If the decision is high-stakes, run an Idea Panel or Model Panel from `ECONOMETRICA_PANEL_PROTOCOL.md` rather than a single-agent kill test.
- If the candidate's deepest primitive or theorem direction is still unclear, run a Primitive Hunter / Theorem Generator Panel before recommending `Invest`, `Refine`, or `Pivot`.
- For each promising model, simulate:
  - absorption referee who tries to reduce the result to known theory
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
  - What is the cleanest theorem sentence: "This paper proves X, and existing theory cannot obtain X because Y"?
  - Which primitive must be endogenized for the theorem to be more than reduced-form relabeling?
  - What is the strongest reason to kill this idea today?

Absorption test:

- Before judging absorption, confirm the nearest theory families and substitute papers through the latest `literature_probe.md`.
- Confirm that the nearest substitute papers and absorption threats appear in `literature_evidence_ledger.md`.
- If the theorem is equivalent to a nearest classical theory family after renaming variables, it fails as a main theorem.
- If web/search tools were unavailable, the closest literature was not checked, or the relevant papers are missing from the ledger, label the absorption result `provisional` rather than final.
- If only a narrow part is absorbed, demote that part to a benchmark and search for the non-absorbed theorem.
- If the model's key object is assumed rather than generated, require an endogenization plan before `Invest`.
- Do not kill an exploration-quota variant because it lacks mainstream taste; judge it separately on deep primitive potential, theorem bite, absorption risk, and assumption artificiality.
- Do not kill a possible frontier spike merely because it looks weird or initially hard to position. Kill or park it only after spike-specific tests show weak primitive depth, weak theorem bite, absorption escape failure, artificial assumptions, infeasible proof, or unacceptable legibility cost.

Main theorem gate:

The candidate cannot receive `Invest` unless all are true:

- The theorem sentence is sharp enough to be put in the introduction unchanged.
- The theorem changes a specialist's belief after conditioning on closest substitutes.
- The result is not merely a package of local sufficient conditions.
- The model primitive that carries the contribution is economically interpretable or explicitly endogenized.
- The model base has passed the Minimal Model Base Gate or is explicitly marked provisional with a clear reason.
- At least one alternative model variant has been killed for a documented reason.
- Any closest-literature or absorption-threat evidence used for the theorem gate is recorded in `literature_evidence_ledger.md`, or the gate is explicitly provisional.

Hostile kill conditions:

Triggering any one condition should lead to `Kill`, `Park`, or `Demote to benchmark` unless the human explicitly overrides with a documented reason.

- `Conclusion-first triviality`: after removing the mathematical shell, the result is just a trivial statement that a specialist would already believe.
- `Name-swap absorption`: replacing topical nouns such as data, algorithms, platforms, AI, benchmarks, certification, or diagnostics with generic terms such as information, technology, intermediary, signal, or machine makes the result equivalent to an old model.
- `Assumption manipulation`: removing a minor-looking regularity condition, distributional restriction, or boundary assumption changes the sign or existence of the core result.
- `Defensive dilution`: the contribution sentence becomes longer, more conditional, or more legalistic after revision.
- `Complexity shield`: heterogeneity, dynamics, extra states, or special distributions mainly protect the theorem rather than reveal the mechanism.

Decision labels:

- `Invest`: proceed to D7 pre-paper package; begin full manuscript development only after human approval of the model note and theorem sentence.
- `Refine`: keep the idea but modify the model.
- `Pivot`: change the mechanism/question.
- `Demote to benchmark`: keep as background, but do not build the paper around it.
- `Park`: save for later but do not invest now.
- `Kill`: abandon for current purposes.

Human gate:

The human must choose a decision label. AI may recommend, but not decide.

## Stage D7 - Pre-Paper Package

Autonomy: Auto

Purpose:

Convert a surviving theorem into a paper-ready model note.

AI tasks:

- Create `idea_dossier.md`.
- Create or update a draft `contribution_lock.md`.
- Create `project_state.md`.
- Create `pre_paper_model_note.md`.
- Carry forward the confirmed `field_profile.md` if it exists; otherwise mark field-sensitive panel assignments as provisional.
- Carry forward the confirmed `target_journal_profile.md` if it exists; otherwise mark target-sensitive review and style calibration as provisional.
- Carry forward `model_base_design.md` and `heuristic_derivation.md`; if the Minimal Model Base Gate was not passed, mark the model note as provisional and do not treat it as ready for full manuscript development.
- Write a 5-8 page model note:
  - question
  - mechanism
  - smallest example and model-base rationale
  - model
  - main theorem candidate
  - theorem sentence
  - proof status
  - absorption-test result
  - killed model variants
  - closest literature
  - contribution claim
  - biggest risks
  - next work plan

Proceed condition:

- The human approves the model note and theorem sentence.
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
- The project starts accumulating fixes before it has a central theorem.
- Two independent panels say the same thing: no central theorem, too close to old theory, or absorbed by a known framework.
- The manuscript becomes more complete while the theorem sentence becomes less sharp.
- The model's important object remains a reduced-form primitive after several repair attempts.

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

### Run Literature Probe And Field Profile

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D3 for the shortlisted candidate. Search for closest substitute papers when web/search tools are available, record verified and inferred literature claims separately, create literature_probe.md, and create or update literature_evidence_ledger.md with entries for every closest paper, anchor paper, absorption threat, and style anchor used downstream. Create or update field_profile.md with the primary field, adjacent fields, absorption-risk theory families, and field-sensitive Referee 1-3 roles. If evidence is sufficient, create or update target_journal_profile.md with a primary/stretch/fallback target ladder and quality floor. If any closest-literature or absorption claim lacks a ledger entry, mark the affected judgment provisional. Stop for my confirmation of the field profile and target profile before any high-stakes panel relies on them.
```

### Generate Models for Shortlisted Ideas

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Use topic_shortlist.md and run Stage D4. First identify the deepest primitive, the reduced-form object that may need endogenization, and whether we should change theorem, change model, or keep the question but change primitive. Treat any user-supplied agents, timing, information, payoffs, or equilibrium language as provisional modeling constraints until the model-base gate confirms them. Generate broad cheap model skeletons before formal derivation: 20-40 total, or 10-20 per selected direction. Screen them to 6-10 semi-formal baselines, then to 3-5 example-to-theory candidates, and choose only 1-3 formal derivation candidates. For each serious direction, record real-world scene, economic tension, candidate geometry, belief state, deep primitive, possible theorem sentence, absorption risk, most informative next test, kill condition, spike protection status, smallest example, why simpler models fail, and why it is not a local variant. Create primitive_hunter_report.md, generality_ledger.md, model_candidates.md, and model_tournament.md. Do not write the paper yet.
```

### Construct Minimal Model Base

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D4.5 Example-to-Theory Model Base Construction before D5. Use topic_shortlist.md, primitive_hunter_report.md, model_candidates.md, model_tournament.md, literature_evidence_ledger.md, and the user's provisional modeling constraints. Create model_base_design.md and heuristic_derivation.md. Start from real-world micro scenes, economic tensions, smallest toy examples, failed simpler alternatives, and only then identify the minimal formal baseline. Do not introduce fixed point, contraction, IFT, or existence machinery before explaining why the economic object requires consistency. Stop at the Minimal Model Base Gate and ask me to confirm, edit, or reject the recommended model base.
```

### Attempt First-Pass Derivations

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D5 for the model candidates selected after the Minimal Model Base Gate. Read model_base_design.md and heuristic_derivation.md first. Attempt clean first-pass derivations from the heuristic path, state assumptions, show algebra where possible, identify failure points, attempt counterexamples, and write candidate theorem sentences in the form: "This paper proves X, and existing theory cannot obtain X because Y." Create derivation_notes.md and theorem_candidates.md. Do not hide failed models.
```

### Run Discovery Kill Test

```text
Read ECONOMETRICA_DISCOVERY_WORKFLOW.md. Run Stage D6. Use model_candidates.md, model_tournament.md, model_base_design.md, heuristic_derivation.md, theorem_candidates.md, derivation_notes.md, literature_probe.md, literature_evidence_ledger.md, generality_ledger.md, field_profile.md, and target_journal_profile.md if available. Derive the absorption families from the closest-literature search and papers actually found; if a closest substitute or absorption threat lacks a ledger entry, mark the absorption judgment provisional. If field_profile.md is missing, provisional, stale, or marked `Reopen requested`, update it and stop for field confirmation before making a final absorption judgment. If theorem quality, absorption risk, field evidence, or target audience changes the target ladder, update target_journal_profile.md and stop for target confirmation before treating journal fit as final. Simulate hostile referees and an editor. Create absorption_tests.md, generality_ledger.md, and idea_kill_tests.md, then recommend Invest, Refine, Pivot, Demote to benchmark, Park, or Kill for each candidate. Do not kill exploration-quota or possible frontier-spike variants merely because they are non-mainstream or hard to position; use spike-specific tests for primitive depth, theorem bite, absorption escape, assumptions, proof feasibility, legibility, and model-base naturalness. Do not skip absorption or theorem gates because the target is not Econometrica. Stop for my decision.
```

## How This Connects to the Main Workflow

Use this discovery workflow before writing a full paper. Once a candidate receives `Invest`, create the pre-paper package in Stage D7 and then continue with:

```text
Read ECONOMETRICA_AI_HUMAN_WORKFLOW.md. Run Stage 1 or Stage 2 using the idea_dossier.md and contribution_lock.md created during discovery.
```

If a later manuscript review says "no central theorem," "too close to existing theory," "absorbed by known models," or "unnatural model base" in two independent rounds, return here to D4.5 or D4-D6 instead of continuing manuscript polishing.
