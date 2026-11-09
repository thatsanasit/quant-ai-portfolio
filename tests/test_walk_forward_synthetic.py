"""Safety and correctness checks for a synthetic educational demonstration."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.walk_forward_synthetic import (
    fit_ar1,
    summary,
    synthetic_series,
    walk_forward,
)


class WalkForwardSyntheticTests(unittest.TestCase):
    def test_generated_data_is_repeatable(self):
        self.assertEqual(synthetic_series(25, seed=9), synthetic_series(25, seed=9))

    def test_training_uses_only_history(self):
        values = synthetic_series(80, seed=8)
        all_rows = walk_forward(values, min_train=15)
        short_rows = walk_forward(values[:40], min_train=15)
        self.assertEqual(all_rows[: len(short_rows)], short_rows)

    def test_training_window_is_strictly_earlier(self):
        rows = walk_forward(synthetic_series(70), min_train=20)
        self.assertEqual(len(rows), 50)
        self.assertTrue(all(r.train_size == r.index for r in rows))

    def test_ar1_estimator_matches_simple_linear_example(self):
        intercept, slope = fit_ar1([1.0, 3.0, 5.0, 7.0])
        self.assertAlmostEqual(intercept, 2.0)
        self.assertAlmostEqual(slope, 1.0)

    def test_handles_constant_history(self):
        intercept, slope = fit_ar1([2.0] * 10)
        self.assertEqual(intercept, 2.0)
        self.assertEqual(slope, 0.0)

    def test_invalid_input_is_rejected(self):
        with self.assertRaises(ValueError):
            synthetic_series(3)
        with self.assertRaises(ValueError):
            walk_forward([1.0, 2.0, 3.0], min_train=3)
        with self.assertRaises(ValueError):
            walk_forward([1.0, float('nan'), 2.0, 3.0], min_train=3)
        with self.assertRaises(ValueError):
            summary([])

    def test_summary_is_nonnegative(self):
        results = summary(walk_forward(synthetic_series(80), min_train=20))
        self.assertEqual(results['n'], 60.0)
        self.assertTrue(all(value >= 0.0 for value in results.values()))


if __name__ == "__main__":
    unittest.main()
