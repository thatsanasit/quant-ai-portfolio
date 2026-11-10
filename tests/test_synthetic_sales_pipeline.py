"""Unit tests for the educational sales-data pipeline."""
import sys
from decimal import Decimal
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.synthetic_sales_pipeline import (
    Order, clean_orders, make_synthetic_orders, run_demo, summarize
)
from datetime import date


class SalesPipelineTests(unittest.TestCase):
    def test_deterministic_generator(self):
        self.assertEqual(make_synthetic_orders(12, 9), make_synthetic_orders(12, 9))

    def test_expected_demo_data_quality(self):
        rows = make_synthetic_orders(30)
        clean, stats = clean_orders(rows)
        self.assertEqual(len(clean), 30)
        self.assertEqual(stats, {"input": 32, "accepted": 30, "duplicates": 1, "invalid": 1})

    def test_invalid_date_and_bad_price(self):
        rows = make_synthetic_orders(1)[:1]
        invalid_date = {**rows[0], "order_id": "x", "order_date": "nonsense"}
        invalid_price = {**rows[0], "order_id": "y", "unit_price": "NaN"}
        out, stats = clean_orders([invalid_date, invalid_price])
        self.assertEqual(out, [])
        self.assertEqual(stats["invalid"], 2)

    def test_duplicate_does_not_double_count(self):
        row = make_synthetic_orders(1)[0]
        out, stats = clean_orders([row, row])
        self.assertEqual(len(out), 1)
        self.assertEqual(stats["duplicates"], 1)

    def test_exact_currency_revenue(self):
        orders = [
            Order("A", date(2026, 1, 1), "books", 3, Decimal("2.10")),
            Order("B", date(2026, 1, 2), "books", 2, Decimal("1.05")),
            Order("C", date(2026, 1, 2), "home", 1, Decimal("0.40")),
        ]
        self.assertEqual(summarize(orders), {
            "orders": 3,
            "total_revenue": "8.80",
            "revenue_by_category": {"books": "8.40", "home": "0.40"},
        })

    def test_empty_data(self):
        self.assertEqual(summarize([]), {"orders": 0, "total_revenue": "0.00", "revenue_by_category": {}})

    def test_demo_is_synthetic_and_reconciled(self):
        result = run_demo()
        quality = result["quality"]
        self.assertEqual(result["dataset"], "synthetic only")
        self.assertEqual(quality["input"], quality["accepted"] + quality["invalid"] + quality["duplicates"])
        self.assertEqual(result["summary"]["orders"], quality["accepted"])


if __name__ == "__main__":
    unittest.main()
