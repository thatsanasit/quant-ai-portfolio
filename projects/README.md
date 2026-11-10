# Project Showcase

**Intelligent Information Technology — Quantitative Software, AI and Data Engineering**

Explore selected research and educational projects. Work that is still in progress is identified separately from runnable code.

| Project | Status | Key skills | Materials |
|---|---|---|---|
| **Gold News Analyzer** | **Research in progress** | Financial NLP, sentiment, ML evaluation | [Overview](gold-news-analyzer.md) |
| **Algorithmic Trading Systems Research** | **Independent research; overview only** | MQL5, Python, debugging, reproducible testing | [Overview](algorithmic-trading-research.md) |
| **Walk-Forward Evaluation** | **Runnable educational demo** | Time-aware validation, AR(1), error metrics, tests | [Details](synthetic-walk-forward-demo.md) · [Python](../examples/walk_forward_synthetic.py) |
| **Synthetic Volatility Analysis** | **Runnable educational demo** | OHLC-like data, true range, ATR, Python | [Python](../demo/synthetic_volatility.py) |
| **Synthetic Sales Analytics Pipeline** | **Runnable AI-assisted demo** | Data validation, deduplication, aggregation, unit tests | [Details](synthetic-sales-analytics.md) · [Python](../examples/synthetic_sales_pipeline.py) |

## Research vs. demonstrations

**Gold News Analyzer** is a research direction, not a deployed product or proof of predictive accuracy. **Algorithmic Trading Systems Research** summarizes engineering work without exposing internal trading software.

**Walk-Forward, Volatility and Sales Analytics** are small independently runnable samples made using synthetic information. They demonstrate general programming skills rather than a production implementation or a claim of personal authorship of every line. AI assistance was used to prepare the portfolio samples.

## Quick start

```bash
python examples/walk_forward_synthetic.py
python demo/synthetic_volatility.py
python examples/synthetic_sales_pipeline.py
python -m unittest discover -s tests -v
```

All examples use Python 3.10+ and the standard library only.

[Read in Thai](README_TH.md) · [Back to portfolio](../README.md)
