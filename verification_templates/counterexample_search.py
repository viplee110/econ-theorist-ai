"""A small, dependency-free counterexample-search template.

Modified for the original workflow refresh (2026-09-13).

Replace the domain, claim and cases for your paper. The example claim is
alpha * beta <= alpha for alpha >= 0 and 0 <= beta <= 1. Tested cases include
both domain boundaries and a reproducible interior sample. No failures found
does not establish a proof; a floating-point failure still needs validation.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from itertools import chain
from typing import Callable, Iterable


@dataclass(frozen=True)
class Params:
    alpha: float
    beta: float


def claim_holds(p: Params) -> bool:
    return p.alpha * p.beta <= p.alpha + 1e-10


def boundary_cases() -> Iterable[Params]:
    # The finite search window is alpha in [0, 10], not the full theorem domain.
    for alpha in (0.0, 1e-9, 1.0, 10.0):
        for beta in (0.0, 1e-9, 0.5, 1.0 - 1e-9, 1.0):
            yield Params(alpha, beta)


def sample_params(n: int, seed: int = 0) -> Iterable[Params]:
    rng = random.Random(seed)
    for _ in range(n):
        yield Params(rng.uniform(0.0, 10.0), rng.uniform(0.0, 1.0))


def find_counterexamples(
    claim: Callable[[Params], bool], cases: Iterable[Params], limit: int = 10
) -> list[Params]:
    if limit < 1:
        raise ValueError("limit must be positive")
    failures = []
    for case in cases:
        if not claim(case):
            failures.append(case)
            if len(failures) >= limit:
                break
    return failures


def main() -> None:
    failures = find_counterexamples(claim_holds, chain(boundary_cases(), sample_params(10_000)))
    if failures:
        print('Candidate counterexamples (validate arithmetic and assumptions):')
        for failure in failures:
            print(failure)
    else:
        print('No counterexample in the boundary cases and 10,000 seeded interior draws.')
        print('This is a finite search, not a proof.')


if __name__ == '__main__':
    main()
