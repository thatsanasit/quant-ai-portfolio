# Time-Series Evaluation & Diagnostics

**Educational demonstration:** Uses synthetic values only, not broker or market data.

## Principles

- Respect time ordering in training, validation and holdout data.
- Avoid look-ahead bias and accidental reuse of future observations.
- Document assumptions, experiment versions and reproducibility settings.
- Compare against simple baselines and account for costs where appropriate.
- Report limitations and unsuccessful outcomes as well as improvements.

## Synthetic example

See [synthetic_volatility.py](../demo/synthetic_volatility.py). It creates made-up OHLC-style observations and calculates standard true range and simple rolling ATR.

The sample performs **no trading, prediction, signal selection, optimization or broker communication**. It is not evidence of performance in real financial markets.
