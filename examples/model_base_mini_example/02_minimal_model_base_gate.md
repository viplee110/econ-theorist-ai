# 02 Minimal Model Base Gate

Status: Toy gate prompt

```text
Gate name: Minimal Model Base Gate
Why the system is stopping: The system has narrowed the model-skeleton
generation but the canonical model base is not confirmed.
Evidence summary: S03, S09, and S18 survive the cheap skeleton funnel. S03 gives
the clearest example-to-theory path; S18 is more abstract; S09 best isolates the
timing primitive.
Decision needed: Choose the baseline model base, request another skeleton pass,
or return to primitive hunting.
Recommended option: Use S03 as the baseline and keep S09 as the timing extension.
Alternatives: Use S18 for a more abstract note; rerun D4.5 if all candidates
feel mechanical.
Consequences: Confirmation allows D5 first-pass derivation. Rejection keeps all
model primitives provisional.
Files to update: model_base_design.md, heuristic_derivation.md,
human_decisions.md
Next stage after decision: D5 first-pass derivation and absorption test.
```

What the assistant should not do:

- It should not say the model is confirmed before this gate.
- It should not move straight to fixed point language unless it has explained
  the economic object that requires consistency.
- It should not treat the number of skeletons as proof of model quality.

