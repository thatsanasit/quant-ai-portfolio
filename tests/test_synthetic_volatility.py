import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from demo.synthetic_volatility import Bar, make_synthetic_bars, true_ranges, rolling_atr


class SyntheticVolatilityTests(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(make_synthetic_bars(10, seed=7), make_synthetic_bars(10, seed=7))

    def test_valid_ohlc(self):
        for bar in make_synthetic_bars(10):
            self.assertLessEqual(bar.low, min(bar.open, bar.close))
            self.assertGreaterEqual(bar.high, max(bar.open, bar.close))

    def test_true_range(self):
        rows = [Bar(10, 12, 9, 11), Bar(11, 14, 10, 13)]
        self.assertEqual(true_ranges(rows), [3, 4])

    def test_rolling_atr_no_future_leakage(self):
        rows = make_synthetic_bars(30, seed=8)
        full = rolling_atr(rows, 5)
        self.assertEqual(full[:12], rolling_atr(rows[:12], 5))
        self.assertEqual(full[:4], [None] * 4)
        self.assertGreater(full[4], 0)

    def test_invalid_period(self):
        with self.assertRaises(ValueError):
            rolling_atr(make_synthetic_bars(10), 0)


if __name__ == "__main__":
    unittest.main()
