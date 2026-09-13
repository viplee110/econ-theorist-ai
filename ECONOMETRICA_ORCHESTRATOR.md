# Research routing

Workflow revision: 2026-09

Modified: 2026-09-13.

Use [AGENTS.md](AGENTS.md) for shared rules. This document selects the next
economic task; it does not repeat the scientific or authorization policy.

## Minimal entry

1. Read the current request and `project_state.md` if it exists.
2. Identify the immediate uncertainty or requested deliverable.
3. Read the relevant section of the activity document and the specific evidence
   needed for this task. Follow evidence links rather than loading every artifact.
4. Perform the most informative authorized action. Update only changed state.
5. Explain the economic finding, its status and the next useful action.

If state is absent, infer what can be inferred from the supplied idea or paper
and create a brief state record when work will continue across turns. Do not
initialize a directory of empty templates. Setup checks are optional unless
the requested operation needs a tool whose availability is unknown.

## Activities, with return paths

| Request or immediate need | Read | Work to perform |
|---|---|---|
| New direction, fuzzy idea, weak mechanism, model alternatives | [Discovery](ECONOMETRICA_DISCOVERY_WORKFLOW.md) | Develop the question, compare mechanisms, inspect literature and test small cases |
| A fixed model to solve, a proof to check, a counterexample | [Verification](ECONOMETRICA_VERIFICATION_WORKFLOW.md) | Check the specified claim; respect a request to solve a model mechanically |
| Explain findings, write or revise a paper, improve readability | [Writing](ECONOMETRICA_AI_HUMAN_WORKFLOW.md) | Build the reader's argument from evidence and accurate claims |
| Independent criticism or an explicit review | [Review](ECONOMETRICA_PANEL_PROTOCOL.md) | Select the needed independent functions and produce one actionable synthesis |
| Installation or tool availability | [First run](FIRST_RUN.md) / [Toolchain](TOOLCHAIN_README.md) | Diagnose only the requested capability |
| Changes to files, checkpoints or rollback | [Version control](ECONOMETRICA_VERSION_CONTROL.md) | Preserve existing work and inspect the diff |
| Older paper project | [Migration](docs/MIGRATION.md) | Reuse evidence and decisions without inheriting obsolete gates |

Discovery, verification and writing can alternate within one session. A failed
proof may reveal a useful economic boundary; an unclear explanation may reveal
a weak model; writing a short explanation can help choose what to prove next.
Neither a stage number nor the existence of a file certifies readiness.

For an explicitly fixed-model calculation, solve and assess that model rather
than forcing a discovery tournament. For a full research project, inspect whether
the supplied primitives are restrictions chosen by the author or exploratory
suggestions. If uncertain, preserve them as the starting branch while examining
authorized alternatives; do not silently discard them.

## Current state and evidence

Create each artifact only when it has content the project needs:

| Artifact | Single responsibility |
|---|---|
| `project_state.md` | Current question, activity, scope of authorization, selected branch/model version, uncertainties, next action and evidence pointers |
| `idea_dossier.md` | Economic question, baseline understanding, candidate mechanisms, contribution and readable explanation; links to relevant author choices |
| `model_note.md` | Model and assumptions, small example/application, versioned claims and their proof status, scope, dependencies and evidence locations |
| `literature_evidence_ledger.md` | Inspected sources, precise prior results, project comparisons and unresolved literature gaps |
| `research_log.md` | Brief dated increments: experiments, AI decisions, counterexamples, revisions and reasons |
| `human_decisions.md` | Actual researcher decisions and reversals, including any delegated research scope |

The manuscript, proof files and recorded computations remain the evidence for
their respective claims. A state summary is an index, not a substitute for them.
Read the relevant recent log entry or claim rather than the full historical log.
Large calculations and abandoned ideas belong in `verification/`, `scratch_runs/`
or `agent_runs/`, with links from the current note when needed.

A claim in `model_note.md` has an ID, model version, exact assumptions and
quantifiers, status, dependencies and proof/evidence location. Proof status is
`conjecture`, `proof sketch`, `proved`, `refuted` or `unresolved`; independent
checking is recorded separately as `not run`, `pass` or `gap`, with scope and
evidence. See Verification for meanings. A source or model change makes only
dependent checks and text stale; a style edit does not reset discovery.

Field and target journal can begin as provisional fields in the idea dossier.
Reuse separate existing profiles if they contain useful evidence. Do not create
new profiles, style contracts, architecture audits or a dashboard solely to route
a task. Confirm a journal choice only if the task needs an unprovided author choice.

## Choosing the next action

Identify the uncertainty that most changes the research decision. Examples:
a close prior result, an untested strategic response, a sign reversal, an unclear
equilibrium quantifier, or a reader who cannot reconstruct the economic mechanism.
Choose a specific test and describe what outcomes would change the decision.
Do not require numerical scores or a fixed number of competing models.

Separate an attractive question from its current feasibility. Keep a difficult
but valuable direction available when a further test has information value.
If repeated work produces no new evidence, change the test, park the branch or
report the unresolved blocker. Do not create more reports to simulate progress.

Use independent lanes when their different starting questions or evidence can
add information. Each lane receives its task and necessary sources, works in its
own location, and reports its assumptions, result and uncertainty. Comparison is
an evidence-based decision, not a mandatory extra judge ceremony. Consult Review
for isolation rules when independence matters.

## Long runs and existing commands

Existing commands such as "initialize this paper project", "continue by the
system", "quickly screen this idea", "run a full literature audit", "run a full
simulated review", and "export a working preview" still route by their meaning.
Chinese instructions such as "按系统继续" and "快速看看这个想法" work identically.
Old D0-D7 and numbered manuscript stages are historical labels, not active gates.

For an explicitly delegated end-to-end run, record the objective, researcher
constraints, available budget and delegated choices in current state. Use the
same activities and scientific checks. Mark AI choices in the research log;
collect material unresolved author choices at the end. Honor explicit time, cost
or stop limits: finish the current safe checkpoint and report remaining work
when the limit is reached, without starting another research branch. Do not require a second
set of auto-mode files. Drafting can finish with conjectures clearly excluded
from established conclusions, or stop with an honest research note if the central
result remains unresolved. Report the actual outcome rather than promising that
every run will produce a complete publishable paper.

When a decision requires the researcher, present the specific alternative,
evidence and consequence. Prior authorization governs; ordinary formatting,
exploratory tests and provisional labels do not trigger repeated questions.
