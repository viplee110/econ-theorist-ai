"""Exact arithmetic for cournot_entry.md. Teaching example, not a new result."""

from fractions import Fraction


def quantity(a, c, n):
    """Production equilibrium conditional on n firms having paid setup costs."""
    a, c = Fraction(a), Fraction(c)
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    if not a > c >= 0:
        raise ValueError("require a > c >= 0")
    return (a - c) / (n + 1)


def operating_profit(a, c, n):
    q = quantity(a, c, n)
    return (Fraction(a) - n * q - Fraction(c)) * q


def welfare(a, c, n, fixed_cost):
    """Total surplus before entry, including real setup resource costs."""
    q = quantity(a, c, n)
    fixed_cost = Fraction(fixed_cost)
    if fixed_cost < 0:
        raise ValueError("fixed_cost must be nonnegative")
    total = n * q
    return (Fraction(a) - Fraction(c)) * total - total**2 / 2 - n * fixed_cost


def main():
    a, c, fixed_cost = Fraction(1), Fraction(0), Fraction(1, 12)
    for n in (1, 2):
        q = quantity(a, c, n)
        print(f"n={n}: q={q}, price={a - n*q}, W={welfare(a,c,n,fixed_cost)}")
    print(f"Entrant net profit: {operating_profit(a,c,2) - fixed_cost}")
    print(f"Welfare change: {welfare(a,c,2,fixed_cost) - welfare(a,c,1,fixed_cost)}")
    print("Classic teaching reconstruction; no originality claim.")


if __name__ == "__main__":
    main()
