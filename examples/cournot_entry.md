# When profitable entry lowers welfare

This is a teaching reconstruction of a classic entry problem, not a new paper.
The purpose is to show how a failed conjecture can produce a useful economic
boundary without adding an elaborate model.

## Question and initial conjecture

An additional producer lowers prices in a concentrated market. Does that make
its entry socially beneficial? Begin with the conjecture, "Profitable entry
always raises total welfare." The missing distinction is between sales a new
firm creates and sales it takes from existing firms. Establishing a plant uses
resources even when part of its revenue comes from displaced sales.

## Smallest model that answers the question

Consumers have quasilinear surplus and inverse demand `P(Q) = a - Q`, with
`a > c >= 0`. Each active firm has constant marginal cost `c`. Entry costs
`F >= 0` units of real resources. After entry, firms simultaneously choose
nonnegative quantities. The setup cost is sunk at that production stage: it
does not enter a firm's quantity first-order condition.

For the entry comparison, one incumbent exists and one potential entrant can
pay `F`. We compare the ensuing monopoly and duopoly outcomes. This is not a
claim about every equilibrium of an unrestricted entry game. For convenience,
first solve production conditional on any integer `n >= 1` active firms.

Let `d = a - c > 0`. If the other firms together produce `Q_-i`, firm `i`'s
operating profit is `(d - Q_-i - q_i) q_i`. Its best response is

```text
q_i = max{0, (d - Q_-i)/2}.
```

Strict concavity makes this the global optimum. All firms must be active in
equilibrium: with `m` positive-output firms, their first-order conditions imply
`Q = m d/(m+1) < d`, so any inactive firm would gain from producing a small
positive quantity. The active firms' conditions imply `q_i = d - Q`, so all
quantities are equal. Hence the unique production equilibrium has

```text
q_n = d/(n+1),     Q_n = n d/(n+1),     P_n = c + d/(n+1),
operating profit per firm = d^2/(n+1)^2.
```

Define welfare before entry as consumer gross benefit minus production and
setup resource costs, keeping Cournot behavior after entry:

```text
W_n = integral from 0 to Q_n of (a - x) dx - c Q_n - n F
    = d^2 n(n+2) / [2(n+1)^2] - n F.
```

Equivalently, this is consumer surplus plus all firms' profits net of setup
costs. The incumbent's already-paid setup cost is common to the two outcomes
and cancels in `W_2 - W_1`. We still count the entrant's not-yet-incurred cost.
If all setup costs had already been irreversibly paid in both alternatives,
this entry-cost comparison would answer a different question. A licensing fee
that is merely a transfer would also require a different welfare treatment.

## Boundary, proof, and counterexample

**Proposition.** In the model above, the entrant earns strictly positive net
profit and entry strictly lowers total welfare if and only if

```text
5 d^2/72 < F < d^2/9.
```

**Proof.** With entry the entrant's net profit is `d^2/9 - F`. Monopoly welfare
is `3 d^2/8 - F`, and duopoly welfare is `4 d^2/9 - 2F`. Therefore
`W_2 - W_1 = 5 d^2/72 - F`. Both desired strict inequalities hold exactly on
the stated interval. The interval is nonempty because `5/72 < 1/9`. At the
lower endpoint the welfare difference is zero. At the upper endpoint the
entrant is indifferent; entry there requires a specified tie-breaking rule.

Take `a = 1`, `c = 0`, and `F = 1/12`:

| Outcome | Each firm's output | Price | Total welfare |
| --- | ---: | ---: | ---: |
| Monopoly | `1/2` | `1/2` | `7/24` |
| Duopoly | `1/3` | `1/3` | `5/18` |

The entrant gains `1/36`, but total welfare falls by `1/72`. Consumers gain
`7/72`; the incumbent loses `10/72` of operating profit; and the entrant earns
`2/72` net of its setup cost. Their sum is `-1/72`. The false initial
conjecture is now **refuted**. The conditional proposition is **proved** by
the hand argument above, rather than being demoted for having a boundary.

## Write the economic result before expanding the model

An entrant can profit even when its entry reduces total surplus. Competition
lowers the price and expands industry output, but some of the entrant's sales
replace the incumbent's sales. Revenue transferred from the incumbent is not
itself a social gain. In this example the output expansion is worth less than
the additional setup resources when `F > 5(a-c)^2/72`, although entry remains
privately profitable up to `F < (a-c)^2/9`. This separates the private incentive
to enter from the social value of the entry decision.

The example does not establish that entry is usually harmful, that a particular
industry meets these assumptions, or that intervention has no other costs.
If investigating an actual market, the next useful question is whether entry
mainly expands consumption, replaces incumbents' sales, or introduces valuable
variety. That question determines whether this baseline is sufficient.

## Evidence and continuation

| Item | Claim status | Verification evidence |
| --- | --- | --- |
| Profitable entry always raises welfare in this model | `refuted` | Exact counterexample above |
| Strict profit and welfare-loss interval | `proved` | Hand proof above; executable rational checks |
| Same conclusion in a differentiated-product extension | `unresolved` | No model or proof supplied here |
| This is an original contribution | No originality claim | Classic related model and mechanism located |

**Literature entry.** N. Gregory Mankiw and Michael D. Whinston (1986),
"Free Entry and Social Inefficiency," *RAND Journal of Economics* 17(1):48–58.
The [author's publication page](https://mankiw.scholars.harvard.edu/publications/free-entry-and-social-inefficiency)
and [full text](https://mankiw.scholars.harvard.edu/sites/g/files/omnuum5931/files/mankiw/files/free_entry.pdf)
were opened on 2026-09-13. Pages 48–50 explain business stealing and the
second-best entry comparison; p.52, Example 1 uses linear-demand Cournot
competition. Our one-to-two-firm thresholds are calculated here. They are not
presented as a quotation or a new result from that paper. This source establishes
a classic antecedent, not an exhaustive review of entry theory.

In a live project, keep the proof in `model_note.md` and the source evidence in
`literature_evidence_ledger.md`. Record the failed conjecture and resulting
boundary in `research_log.md`; update `project_state.md` with the next relevant
question. Use `idea_dossier.md` only if comparing research directions. Record
actual user decisions in `human_decisions.md` when they occur. These are small
records supporting the work, not six forms to complete before doing it.

Run `python examples/boundary_example.py` for the numerical reconstruction and
`python evals/verify_examples.py` for tests. The tests check production incentives,
welfare accounting, endpoints, and counterexamples using exact fractions.
They do not prove generalizations, verify publication novelty, or constitute
independent expert review.
