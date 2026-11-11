"""Reproducible, runnable ML training example on synthetic factory sensor data.

This educational experiment is entirely independent from any proprietary EA,
market data, account information, trade logs, or private model features.

Run:
    python -m pip install -r requirements-ml.txt
    python examples/synthetic_ml_training.py
"""
from __future__ import annotations

import json
from dataclasses import dataclass

import numpy as np
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss, roc_auc_score


@dataclass(frozen=True)
class ChronologicalSplit:
    train: slice
    validation: slice
    test: slice


def chronological_split(n: int) -> ChronologicalSplit:
    """Split by observation order; test data are held out until final evaluation."""
    if n < 500:
        raise ValueError("Use at least 500 synthetic observations")
    train_end = int(n * 0.60)
    valid_end = int(n * 0.80)
    return ChronologicalSplit(
        train=slice(0, train_end),
        validation=slice(train_end, valid_end),
        test=slice(valid_end, n),
    )


def synthetic_sensor_data(n: int = 2400, seed: int = 2026) -> tuple[np.ndarray, np.ndarray]:
    """Create labelled observations using random, artificial sensor variables."""
    if n < 500:
        raise ValueError("n must be >= 500")
    rng = np.random.default_rng(seed)
    temperature = rng.normal(loc=0, scale=1, size=n)
    pressure = 0.35 * temperature + rng.normal(size=n)
    vibration = rng.normal(size=n)
    humidity = rng.normal(size=n)
    X = np.column_stack([temperature, pressure, vibration, humidity])
    time_drift = np.linspace(-0.15, 0.15, n)
    logits = (
        1.1 * temperature - 0.75 * pressure + 0.9 * vibration
        + 0.40 * temperature * humidity + time_drift
        + rng.normal(scale=0.4, size=n)
    )
    probabilities = 1 / (1 + np.exp(-logits))
    y = rng.binomial(1, probabilities).astype(np.int64)
    return X, y


def evaluate_probabilities(y: np.ndarray, probabilities: np.ndarray) -> dict[str, float]:
    if len(y) != len(probabilities) or len(y) == 0:
        raise ValueError("Targets and predictions must be nonempty and aligned")
    if len(np.unique(y)) < 2:
        raise ValueError("AUC requires both classes")
    return {
        "auc": round(float(roc_auc_score(y, probabilities)), 4),
        "brier": round(float(brier_score_loss(y, probabilities)), 4),
    }


def run_experiment(n: int = 2400, seed: int = 2026) -> dict[str, object]:
    X, y = synthetic_sensor_data(n=n, seed=seed)
    split = chronological_split(n)
    X_train, y_train = X[split.train], y[split.train]
    x_valid, y_valid = X[split.validation], y[split.validation]
    x_test, y_test = X[split.test], y[split.test]

    # The baseline and both models depend on training observations only.
    baseline_probability = float(y_train.mean())
    models = {
        "random_forest": RandomForestClassifier(
            n_estimators=100, max_depth=6, min_samples_leaf=12,
            random_state=seed, n_jobs=1,
        ),
        "lightgbm": LGBMClassifier(
            n_estimators=90, max_depth=4, num_leaves=12, learning_rate=0.05,
            min_child_samples=24, random_state=seed, n_jobs=1, verbosity=-1,
        ),
    }

    results: dict[str, object] = {
        "data": "synthetic sensor observations only",
        "observations": int(n),
        "split": {
            "train": int(len(y_train)),
            "validation": int(len(y_valid)),
            "test": int(len(y_test)),
        },
        "models": {
            "constant_probability_baseline": {
                "validation": evaluate_probabilities(
                    y_valid, np.full(len(y_valid), baseline_probability)
                ),
                "test": evaluate_probabilities(
                    y_test, np.full(len(y_test), baseline_probability)
                ),
            }
        },
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        results["models"][name] = {
            "validation": evaluate_probabilities(
                y_valid, model.predict_proba(x_valid)[:, 1]
            ),
            "test": evaluate_probabilities(
                y_test, model.predict_proba(x_test)[:, 1]
            ),
        }
    return results


if __name__ == "__main__":
    print(json.dumps(run_experiment(), indent=2))
