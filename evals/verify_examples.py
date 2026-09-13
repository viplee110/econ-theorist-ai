"""Finite exact checks for the teaching model, not an AI research evaluation.

Run from any working directory with Python 3. No third-party packages needed.
The general proof and the scope of the entry comparison are in the worked note.
"""

from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examples.boundary_example import operating_profit, quantity, welfare


class CournotChecks(unittest.TestCase):
    def test_profitable_deviations_absent_in_tested_equilibria(self):
        # Evaluate payoffs directly at alternative actions, not the equilibrium
        # formula again. Finite deviations corroborate but do not prove Nash.
        for a, c in ((F(1), F(0)), (F(7, 3), F(1, 3)), (F(11, 7), F(2, 7))):
            d = a - c
            for n in range(1, 9):
                q = quantity(a, c, n)
                rivals = (n - 1) * q
                equilibrium_payoff = (a - rivals - q - c) * q
                # Include zero, both sides of q, and large output choices.
                deviations = {k * d / 48 for k in range(97)} | {q / 2, q, 3 * q / 2}
                for trial in deviations:
                    with self.subTest(a=a, c=c, n=n, trial=trial):
                        self.assertLessEqual((a - rivals - trial - c) * trial,
                                             equilibrium_payoff)

    def test_welfare_matches_consumer_surplus_plus_producer_profits(self):
        # Independent accounting route: area of consumer-surplus triangle plus
        # revenues minus actual production and setup costs.
        for a, c in ((F(1), F(0)), (F(5, 2), F(1, 2))):
            for n in range(1, 9):
                for fixed_cost in (F(0), F(1, 12), F(1, 3)):
                    q = quantity(a, c, n)
                    total = n * q
                    price = a - total
                    consumer_surplus = (a - price) * total / 2
                    producers = (price - c) * total - n * fixed_cost
                    with self.subTest(a=a, c=c, n=n, fixed_cost=fixed_cost):
                        self.assertEqual(welfare(a, c, n, fixed_cost),
                                         consumer_surplus + producers)

    def test_counterexample_to_original_conjecture(self):
        self.assertEqual(operating_profit(1, 0, 2) - F(1, 12), F(1, 36))
        self.assertEqual(welfare(1, 0, 1, F(1, 12)), F(7, 24))
        self.assertEqual(welfare(1, 0, 2, F(1, 12)), F(5, 18))
        self.assertLess(welfare(1, 0, 2, F(1, 12)), welfare(1, 0, 1, F(1, 12)))

    def test_both_boundaries_and_sides(self):
        # Expected signs are derived in the note. Include exact endpoints to
        # detect accidental weak/strict inequality and tie-breaking mistakes.
        cases = (
            (F(0), 1, 1),
            (F(5, 72), 1, 0),
            (F(1, 12), 1, -1),
            (F(1, 9), 0, -1),
            (F(1, 8), -1, -1),
        )
        for d in (F(1), F(3, 2), F(7, 3)):
            for fraction, profit_sign, welfare_sign in cases:
                a, c, fixed_cost = d + 2, F(2), fraction * d**2
                profit = operating_profit(a, c, 2) - fixed_cost
                change = welfare(a, c, 2, fixed_cost) - welfare(a, c, 1, fixed_cost)
                with self.subTest(d=d, fixed_cost=fixed_cost):
                    self.assertEqual((profit > 0) - (profit < 0), profit_sign)
                    self.assertEqual((change > 0) - (change < 0), welfare_sign)

    def test_invalid_model_inputs_fail(self):
        for a, c, n in ((1, 1, 1), (0, 1, 1), (1, -1, 1),
                        (1, 0, 0), (1, 0, F(3, 2)), (1, 0, True)):
            with self.subTest(a=a, c=c, n=n), self.assertRaises(ValueError):
                quantity(a, c, n)
        with self.assertRaises(ValueError):
            welfare(1, 0, 1, F(-1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
