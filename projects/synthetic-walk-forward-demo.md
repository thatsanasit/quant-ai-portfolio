# Synthetic Walk-Forward Evaluation Demo

**Status:** Educational, self-contained code demonstration (not a market model).  
**Technology:** Python standard library, unit testing, time-series evaluation.

## What this demonstrates

- Creation of deterministic **artificial** numerical observations
- Expanding-window training, with each prediction using only earlier observations
- Comparison between a persistence baseline and a small AR(1) linear-regression model
- Reporting mean absolute error (MAE) and root mean squared error (RMSE)
- Tests that appended future observations cannot alter earlier predictions
- Reproducible experiments with a fixed random seed

## Run locally

Requires Python 3.10+.

```bash
python examples/walk_forward_synthetic.py
python -m unittest discover -s tests -v
python tools/review_before_publish.py
```

## Evaluation design

For each prediction at index `t`, fit the model using `values[:t]` only. The model and naive baseline forecast `values[t]`. Actual values at `t` are accessed only when scoring predictions.

The synthetic generator is deliberately arbitrary. Its results cannot be interpreted as evidence about gold, trading or any real asset. This repository does **not** contain trading signal logic, order execution, tuned parameters, live data, account details, private EA code, real backtests or learned model weights.

## Boundaries

The code is intentionally small so reviewers can inspect each assumption. It is **not** a production-grade model, financial forecast or investment system.
