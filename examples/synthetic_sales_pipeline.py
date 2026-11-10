"""End-to-end analytics pipeline using artificial retail transactions only.

Demonstrates deterministic data generation, validation, deduplication and
aggregation. It uses no customer records, external services or credentials.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from random import Random
import json
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Order:
    order_id: str
    order_date: date
    category: str
    quantity: int
    unit_price: Decimal


CATEGORIES = ("books", "home", "stationery", "electronics")


def make_synthetic_orders(count: int = 120, seed: int = 2026) -> list[dict[str, str]]:
    """Generate non-real transactions and add controlled quality problems."""
    if count < 1:
        raise ValueError("count must be positive")
    rng = Random(seed)
    first_day = date(2026, 1, 1)  # Arbitrary demonstration date.
    rows = []
    for index in range(count):
        amount = Decimal(rng.randint(100, 4500)) / Decimal("100")
        rows.append({
            "order_id": f"DEMO-{index + 1:04d}",
            "order_date": (first_day + timedelta(days=rng.randrange(30))).isoformat(),
            "category": rng.choice(CATEGORIES),
            "quantity": str(rng.randint(1, 5)),
            "unit_price": str(amount),
        })
    rows.append(dict(rows[0]))
    rows.append({**rows[1], "order_id": "DEMO-BAD", "quantity": "-2"})
    return rows


def clean_orders(records: Sequence[Mapping[str, str]]) -> tuple[list[Order], dict[str, int]]:
    """Remove invalid and duplicate orders; preserve one row per order_id."""
    cleaned: list[Order] = []
    ids: set[str] = set()
    counters = {"input": 0, "accepted": 0, "duplicates": 0, "invalid": 0}
    for raw in records:
        counters["input"] += 1
        try:
            order_id = raw["order_id"].strip()
            category = raw["category"].strip().lower()
            order_date = date.fromisoformat(raw["order_date"].strip())
            quantity = int(raw["quantity"])
            price = Decimal(raw["unit_price"])
            if not order_id or category not in CATEGORIES or quantity <= 0:
                raise ValueError("invalid record")
            if not price.is_finite() or price <= 0:
                raise ValueError("invalid price")
        except (KeyError, TypeError, AttributeError, ValueError, InvalidOperation):
            counters["invalid"] += 1
            continue
        if order_id in ids:
            counters["duplicates"] += 1
            continue
        ids.add(order_id)
        cleaned.append(Order(order_id, order_date, category, quantity, price))
        counters["accepted"] += 1
    return cleaned, counters


def summarize(orders: Sequence[Order]) -> dict[str, object]:
    """Aggregate revenue by category using Decimal for monetary precision."""
    by_category: dict[str, Decimal] = defaultdict(Decimal)
    total_revenue = Decimal("0")
    for order in orders:
        revenue = order.quantity * order.unit_price
        total_revenue += revenue
        by_category[order.category] += revenue
    return {
        "orders": len(orders),
        "total_revenue": str(total_revenue.quantize(Decimal("0.01"))),
        "revenue_by_category": {
            name: str(value.quantize(Decimal("0.01")))
            for name, value in sorted(by_category.items())
        },
    }


def run_demo() -> dict[str, object]:
    raw = make_synthetic_orders()
    cleaned, quality = clean_orders(raw)
    return {"dataset": "synthetic only", "quality": quality, "summary": summarize(cleaned)}


def main() -> None:
    print(json.dumps(run_demo(), indent=2, ensure_ascii=False))
    print("No real people, customers, broker data, or financial market signals.")


if __name__ == "__main__":
    main()
