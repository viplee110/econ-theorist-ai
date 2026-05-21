# 04 Model Base Design

Status: Provisional toy design

## D4.5 Example-To-Theory Construction

Real-world scene:

A two-person team produces a joint output. Each worker can allocate effort to a
visible task or a less visible task. A sponsor may announce recognition before
effort is chosen or after output is realized.

Core economic tension:

Recognition motivates effort, but early recognition can redirect effort toward
visible activities that are not the most productive for the team.

## Skeleton Funnel

Cheap model skeletons considered: 24

Semi-formal baselines retained: 7

Toy examples retained: 3

Formal candidates for D5: 2

## Top Toy Examples

Toy example A: One worker, one visible task, one hidden task.

- Strength: easiest economic intuition
- Weakness: no team interaction

Toy example B: Two workers, one public task, one hidden task, fixed recognition
rule.

- Strength: minimal team-production tradeoff
- Weakness: recognition timing is still mechanical

Toy example C: Two workers, two tasks, recognition announced before or after
effort, output requires both task types.

- Strength: clean comparative static in recognition timing
- Weakness: slightly less minimal

## Recommended Baseline

Use toy example C as the baseline if the literature audit does not absorb it.
It has the cleanest path from example to theorem:

```text
Recognition timing -> task visibility -> effort allocation -> team output
```

## Failed Simpler Alternatives

- Pure recognition-bonus model: too easily absorbed.
- Pure multitask moral-hazard model: loses the timing primitive.
- Full dynamic reputation model from the start: mechanically formal and not
  economically transparent.

## Minimal Model Base Gate

```text
Gate name: Minimal Model Base Gate
Why the system is stopping: The model base is still provisional.
Evidence summary: Candidate C best preserves the economic tension while avoiding
premature dynamic-reputation machinery.
Decision needed: Confirm candidate C, request another skeleton pass, or return
to primitive hunting.
Recommended option: Confirm candidate C only after real literature audit checks
the closest social-image, career-concerns, and multitask moral-hazard papers.
Alternatives: Candidate B for a more minimal note; new D4.5 generation if all
candidates feel artificial.
Consequences: Confirmation allows D5 derivation; rejection keeps primitives
provisional.
Files to update: model_base_design.md, heuristic_derivation.md,
human_decisions.md
Next stage after decision: D5 first-pass derivation.
```

