"""Tests for the independent synthetic ML training demo."""
import sys
from pathlib import Path
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examples.synthetic_ml_training import (
    chronological_split,
    synthetic_sensor_data,
    run_experiment,
    evaluate_probabilities,
)


class SyntheticMLTrainingTests(unittest.TestCase):
    def test_generation_repeatable(self):
        x1, y1 = synthetic_sensor_data(500, seed=22)
        x2, y2 = synthetic_sensor_data(500, seed=22)
        np.testing.assert_array_equal(x1, x2)
        np.testing.assert_array_equal(y1, y2)

    def test_chronological_disjoint(self):
        split = chronological_split(2400)
        self.assertEqual((split.train.start, split.train.stop), (0, 1440))
        self.assertEqual((split.validation.start, split.validation.stop), (1440, 1920))
        self.assertEqual((split.test.start, split.test.stop), (1920, 2400))

    def test_train_results_are_complete(self):
        report = run_experiment(n=600, seed=12)
        self.assertEqual(report["split"], {"train": 360, "validation": 120, "test": 120})
        self.assertEqual(set(report["models"]), {
            "random_forest", "lightgbm", "constant_probability_baseline"
        })
        for model in report["models"].values():
            for row in model.values():
                self.assertTrue(0 <= row["auc"] <= 1)
                self.assertTrue(0 <= row["brier"] <= 1)

    def test_invalid_short_data_rejected(self):
        with self.assertRaises(ValueError):
            chronological_split(100)
        with self.assertRaises(ValueError):
            synthetic_sensor_data(10)

    def test_invalid_predictions_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_probabilities(np.array([0, 1]), np.array([0.5]))
        with self.assertRaises(ValueError):
            evaluate_probabilities(np.array([1, 1]), np.array([0.5, 0.5]))


if __name__ == "__main__":
    unittest.main()
