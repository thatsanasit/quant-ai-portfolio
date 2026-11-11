# Project Showcase

A selection of software, data, and AI/ML projects. **Research work, preliminary results, and runnable examples are clearly distinguished.**

## Featured work

| Project | Status | Evidence |
|---|---|---|
| [Algorithmic Trading Systems Research](algorithmic-trading-research.md) | Independent systems research and demo testing | [Original MT5 test screenshots](mt5-forward-testing-evidence.md) |
| [Machine Learning Model Evaluation](ml-chronological-evaluation.md) | Historical approximate ML study + independent runnable synthetic classifier | [Random Forest / LightGBM code](../examples/synthetic_ml_training.py) · [Tests](../tests/test_synthetic_ml_training.py) |
| [Gold News Analyzer](gold-news-analyzer.md) | Research in progress | Research objectives and proposed evaluation approach |

## Additional runnable demonstrations

| Project | What it demonstrates |
|---|---|
| [Walk-Forward Evaluation](synthetic-walk-forward-demo.md) | Python time-series evaluation and leakage tests |
| [Sales Analytics Pipeline](synthetic-sales-analytics.md) | Python data quality, aggregation and unit tests |
| [Volatility Analysis](../demo/synthetic_volatility.py) | True range and simple ATR on artificial OHLC data |

## Reproduce the code examples

```bash
python -m pip install -r requirements-ml.txt
python examples/synthetic_ml_training.py
python examples/walk_forward_synthetic.py
python examples/synthetic_sales_pipeline.py
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
```

All executable examples use synthetic observations; the separate MT5 page includes the author's original demo-account testing screenshots. No proprietary EA source code is published.

[ภาษาไทย](README_TH.md) · [Portfolio home](../README.md)
