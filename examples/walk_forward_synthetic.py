"""Educational, synthetic-only demonstration of chronological model evaluation.

Generates artificial numbers; contains no trading, real prices, market feeds,
account data, broker connections, entry decisions, or proprietary strategies.
Requires only the Python standard library.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from random import Random
from typing import Sequence


@dataclass(frozen=True)
class EvaluationRow:
    index: int
    actual: float
    baseline: float
    model: float
    train_size: int


def synthetic_series(length: int = 240, seed: int = 42) -> list[float]:
    """Return deterministic artificial values with an arbitrary AR(1) pattern."""
    if length < 4:
        raise ValueError("length must be at least 4")
    rng = Random(seed)
    current = 0.0
    result: list[float] = []
    for _ in range(length):
        current = 0.7 * current + rng.gauss(0.0, 1.0)
        result.append(current)
    return result


def fit_ar1(history: Sequence[float]) -> tuple[float, float]:
    """Fit y[t] = intercept + slope * y[t-1] using PAST data only."""
    if len(history) < 3 or not all(isfinite(v) for v in history):
        raise ValueError("history needs >=3 finite observations")
    x = history[:-1]
    y = history[1:]
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    sxx = sum((v - x_mean) ** 2 for v in x)
    if sxx < 1e-12:
        return y_mean, 0.0
    sxy = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    slope = sxy / sxx
    return y_mean - slope * x_mean, slope


def walk_forward(values: Sequence[float], min_train: int = 60) -> list[EvaluationRow]:
    """Expanding-window one-step evaluation; never observes target/future values."""
    if min_train < 3 or min_train >= len(values):
        raise ValueError("min_train must be >=3 and smaller than series length")
    if not all(isfinite(v) for v in values):
        raise ValueError("series contains nonfinite values")
    rows: list[EvaluationRow] = []
    for target_index in range(min_train, len(values)):
        history = values[:target_index]
        intercept, slope = fit_ar1(history)
        rows.append(
            EvaluationRow(
                index=target_index,
                actual=values[target_index],
                baseline=history[-1],
                model=intercept + slope * history[-1],
                train_size=len(history),
            )
        )
    return rows


def summary(rows: Sequence[EvaluationRow]) -> dict[str, float]:
    """Return standard error statistics for synthetic forecasts (not trading P&L)."""
    if not rows:
        raise ValueError("rows cannot be empty")
    count = len(rows)
    baseline_errors = [r.actual - r.baseline for r in rows]
    model_errors = [r.actual - r.model for r in rows]
    return {
        "n": float(count),
        "baseline_mae": sum(abs(e) for e in baseline_errors) / count,
        "model_mae": sum(abs(e) for e in model_errors) / count,
        "baseline_rmse": sqrt(sum(e * e for e in baseline_errors) / count),
        "model_rmse": sqrt(sum(e * e for e in model_errors) / count),
    }


def main() -> None:
    values = synthetic_series()
    rows = walk_forward(values)
    results = summary(rows)
    print("SYNTHETIC EDUCATIONAL DATA — NOT MARKET PRICES")
    print(f"Observations: {len(values)}; walk-forward predictions: {int(results['n'])}")
    print(f"Persistence baseline MAE: {results['baseline_mae']:.4f}")
    print(f"Toy AR(1) model MAE:       {results['model_mae']:.4f}")
    print(f"Persistence baseline RMSE: {results['baseline_rmse']:.4f}")
    print(f"Toy AR(1) model RMSE:       {results['model_rmse']:.4f}")
    print("No real data, market signals, strategy, orders or performance claims.")


if __name__ == "__main__":
    main()
