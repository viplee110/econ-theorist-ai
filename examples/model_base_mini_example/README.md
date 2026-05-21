# Model Base Mini Example

This example focuses on D4/D4.5: broad model-skeleton generation before narrow
formal derivation.

The point is not that more skeletons mechanically guarantee a better model. The
point is to make generation cheap, diverse, and economically grounded before the
system spends effort on proof machinery.

Toy user prompt:

```text
Use the system: I have a fuzzy idea about public recognition in team production.
Find the minimal model base before formal derivation.
```

Expected behavior:

- Treat the prompt as Idea Mode with provisional modeling constraints.
- Generate many cheap model skeletons.
- Filter for economic naturalness, smallest example, theorem path, absorption
  risk, and proof tractability.
- Stop at the Minimal Model Base Gate.

