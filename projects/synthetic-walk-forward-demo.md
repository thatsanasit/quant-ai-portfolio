# Synthetic Walk-Forward Evaluation

**Python educational demonstration — artificial data only**

## What it implements

- Deterministic numerical observations with a fixed random seed
- Expanding-window fitting with predictions based on earlier observations only
- Persistence baseline compared with an AR(1)-style linear regression model
- Evaluation using MAE and RMSE
- Unit tests including a check that future observations do not change past predictions

## Run

Python 3.10+; standard library only.

```bash
python examples/walk_forward_synthetic.py
python -m unittest discover -s tests -p "test_walk_forward_synthetic.py" -v
```

For a forecast at time `t`, the model is trained only on `values[:t]`; the observation at `t` is used to measure the error afterward.

This demonstration is intentionally small and is **not** a real market model or verified investment strategy.

[Source](../examples/walk_forward_synthetic.py) · [Tests](../tests/test_walk_forward_synthetic.py) · [Project index](README.md)
