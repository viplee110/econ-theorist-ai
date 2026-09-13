# Old tools, duplicate results, and open mechanisms

Use an exact comparison before deciding that a candidate merely renames an
existing result. The presence of Cournot competition, mechanism design, or
another familiar tool does not establish duplication.

## A duplication claim that can be checked

Consider a candidate called "capacity competition between compute providers":

```text
Provider i chooses service units x_i >= 0.
Inverse service price: r(X) = A - X, where X = sum_i x_i.
Unit resource cost: k >= 0, with A > k.
Setup resource cost: K >= 0, sunk before service quantity is chosen.
Net profit: [A - X - k] x_i - K.
Welfare: integral from 0 to X of (A - z) dz - k X - n K.
```

It claims that a second provider may enter profitably while reducing total
surplus. Compare it with [the Cournot example](cournot_entry.md):

| Candidate object | Cournot object | What must match |
| --- | --- | --- |
| Provider, service units `x_i` | Firm, output `q_i` | Same agents and feasible actions |
| `A`, `k`, `K` | `a`, `c`, `F` | Same parameter restrictions |
| Service price `r(X)` | Price `P(Q)` | Same inverse demand |
| Simultaneous service choice | Simultaneous quantity choice | Same timing and information |
| Setup cost followed by quantity choice | Setup cost followed by quantity choice | Same sunk-cost treatment |
| Consumer benefit minus resource costs | Total surplus | Same welfare objective |
| One incumbent and one potential entrant | One incumbent and one potential entrant | Same comparison and quantifiers |

The identity substitution preserves actions, payoffs, best responses, and
welfare. It therefore reproduces the same production equilibrium and the same
interval `5(A-k)^2/72 < K < (A-k)^2/9`. For this fully specified candidate,
the proposition is a relabeling of the worked baseline. An industry name and
new symbols do not establish a new theoretical contribution. The application
could still be useful as teaching or as a justified component of other work.

This is a comparison with an explicit baseline, not an unsupported claim that
every compute-market result is already in the literature.

## A change that deserves a test, without a novelty promise

Suppose a proposed alternative lets an entrant create an interoperability benefit
for the incumbent's customers. Its sales might then expand the incumbent's
demand. This is a candidate economic mechanism, still **unresolved**: no payoff
specification, equilibrium, or welfare result has been established here.

The identity mapping above no longer suffices if the proposed benefit genuinely
changes cross-firm demand or payoffs. A useful next test is to specify the benefit
in a small model and ask whether removing it changes the predicted behavior or
welfare boundary. Keep the behavioral effect distinct from simply assuming an
extra positive term in social welfare.

Passing that test would distinguish the proposal from this baseline. It would
not establish originality. Mankiw and Whinston already discuss circumstances
with business augmentation and product variety; see p.52, footnote 7, and
Section 4 of their [full text](https://mankiw.scholars.harvard.edu/sites/g/files/omnuum5931/files/mankiw/files/free_entry.pdf).
A literature comparison must check exact assumptions, results, and scope in
these and other close papers. The source was opened on 2026-09-13.

Record the comparison precisely:

- **Established:** the first candidate is identical to the supplied baseline
  under the displayed mapping.
- **Unresolved:** the alternative's behavioral mechanism and economic lesson.
- **Literature evidence:** an opened antecedent identifies relevant nearby
  forces; no exhaustive closest-paper audit has been completed.
- **Next action:** work out the smallest discriminating example and inspect
  close results. Continue the reversible analysis within the user's scope.

Neither a familiar mathematical tool nor a more conditional conclusion is an
automatic reason to abandon a direction. Equally, a changed primitive or a
fashionable application is not evidence of a new contribution.
