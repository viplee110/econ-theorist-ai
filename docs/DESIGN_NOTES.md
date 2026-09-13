# Why the original workflow is changing

Design notes, 2026-09-13. Read when maintaining the workflow, not on every
research turn. These are design hypotheses, not measured improvements in an
AI's research quality or a recipe for journal acceptance.

The earlier workflow contained useful scientific checks, but also overlapping
stage gates, candidate quotas, early score cutoffs, contribution locks and a
fixed editorial hierarchy. This update retains evidence integrity while making
discovery, checking and writing activities that can inform one another.

| Design choice | Relevant experience | Limit of the inference |
|---|---|---|
| Explain the economic argument early; place qualifications where they matter | Virginia Gewin, [How to write a first-class paper](https://www.nature.com/articles/d41586-018-02404-4), Nature, 2018. Expert interviews discuss defensive, obscure scientific writing. | Better prose cannot repair a false or unimportant result. |
| Revisit questions after unexpected findings | Dom Byrne with Itai Yanai and Martin Lercher, [Some night science thinking could move it forward](https://www.nature.com/articles/d41586-026-01294-1), Nature Careers Podcast, 2026. The public transcript distinguishes creative inquiry and execution. | Exploratory conjectures still need evidence before becoming conclusions. |
| Move between the simplest useful model and justified generalization | Hal Varian, [How to Build an Economic Model in Your Spare Time](https://people.ischool.berkeley.edu/~hal/Papers/how.pdf), author version. | A finite toy model is not suitable for every methodological contribution. |
| Examine what a result's failure conditions teach | Daron Acemoglu, Do's and Don'ts of the Publication Process, [CSWEP News 2015 II](https://www.aeaweb.org/content/file?id=521), pp.8–9. | A meaningful boundary must be distinguished from a patch that assumes the desired conclusion. |

These sources were inspected for the redesign. They inform the choices above;
none evaluates this software. The earlier workflow's additional research and
agent-system references remain available in the
[historical research-basis section](https://github.com/viplee110/econ-theorist-ai/blob/cc5f61254bb79e7436892e32ec88730ae14dd7f8/ECONOMETRICA_AI_HUMAN_WORKFLOW.md#L1139-L1157).
That record is preserved as provenance, not a claim that every historical citation
was revalidated or that those sources demonstrated the earlier system's efficacy.

The seven protocol filenames remain for installation compatibility. AGENTS owns
shared rules, the orchestrator owns routing and current-state responsibilities,
and activity files supply methods on demand. Long historical logs, examples,
these notes and maintainer tests are outside the default prompt path.

Evaluate changes using the [behavior cases](../evals/behavior_cases.md), then
matched open research questions with documented resources and blinded human
judgment where feasible. Compare workflow and model changes separately. Count
context, interruptions and files, but judge economic contribution, correctness,
source integrity and reader understanding separately. No such comparative AI
research evaluation is reported by this revision.
