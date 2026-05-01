-- Minimal Lean 4 smoke-test lemma.
-- For substantial real-analysis lemmas, initialize a Mathlib project first.

theorem nat_square_nonneg (n : Nat) : 0 <= n * n := by
  exact Nat.zero_le (n * n)

