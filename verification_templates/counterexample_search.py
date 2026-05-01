"""Template for adversarial numerical checks of theory claims.

Copy this file into a paper-specific `verification/` folder and replace
`claim_holds` with the proposition or comparative static being tested.
Numerical success is not a proof; one valid failure is evidence that the
claim needs narrower assumptions or a corrected statement.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

import numpy as np
import sympy as sp


@dataclass(frozen=True)
class Params:
    alpha: float
    beta: float


def claim_holds(p: Params) -> bool:
    """Replace with the target claim.

    Example placeholder claim: alpha * beta <= alpha when beta <= 1.
    """
    lhs = p.alpha * p.beta
    rhs = p.alpha
    return lhs <= rhs + 1e-10


def sample_params(n: int, seed: int = 0) -> list[Params]:
    rng = random.Random(seed)
    draws: list[Params] = []
    for _ in range(n):
        draws.append(
            Params(
                alpha=rng.uniform(0.0, 10.0),
                beta=rng.uniform(0.0, 1.0),
            )
        )
    return draws


def symbolic_sanity_check() -> None:
    alpha, beta = sp.symbols("alpha beta", nonnegative=True)
    expr = sp.diff(alpha * beta, beta)
    print("symbolic derivative d(alpha*beta)/d beta =", expr)


def main() -> None:
    symbolic_sanity_check()

    failures: list[Params] = []
    for p in sample_params(10_000):
        if not claim_holds(p):
            failures.append(p)
            if len(failures) >= 10:
                break

    if failures:
        print("COUNTEREXAMPLES FOUND")
        for failure in failures:
            print(failure)
    else:
        print("No counterexample found in this numerical search.")

    grid = np.linspace(0.0, 1.0, 11)
    print("boundary grid for beta:", grid)


if __name__ == "__main__":
    main()

