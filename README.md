# Quantitative Development & Applied AI Portfolio

**Tup | Intelligent Information Technology Student**  
School of Informatics, Walailak University

Welcome to my student portfolio focused on quantitative software development, machine learning, financial data analysis, and reproducible software experiments.

> **Privacy-first portfolio:** This repository is currently private. The examples here are educational and do not contain my trading system, proprietary signals, actual trading data, credentials, or private research results.

## Featured projects

| Project | Focus | What is shared here |
|---|---|---|
| [Algorithmic Trading Systems Research](projects/algorithmic-trading-research.md) | MQL5, Python, systematic testing, reproducibility | High-level project overview only |
| [Gold News Analyzer](projects/gold-news-analyzer.md) | Financial NLP, news analysis, volatility research | Research concept; work in progress |
| [Time-Series Evaluation](projects/time-series-evaluation.md) | Time-aware evaluation, diagnostics, data leakage prevention | Educational methodology and synthetic-data code |

## New: privacy-safe walk-forward evaluation

[Read the synthetic walk-forward demo](projects/synthetic-walk-forward-demo.md) · [View Python source](examples/walk_forward_synthetic.py)

This standalone Python exercise demonstrates chronological train/test separation, a simple AR(1) linear model, baseline comparisons, MAE/RMSE evaluation and reproducibility tests. It uses only artificially generated numbers—**no proprietary EA logic, trade data, live market information or order placement**.

```bash
python examples/walk_forward_synthetic.py
python -m unittest discover -s tests -v
```

## Educational Python demonstration

[demo/synthetic_volatility.py](demo/synthetic_volatility.py) generates **artificial OHLC-like data** and computes true range and a simple rolling ATR. It has no market connection, buy/sell logic, broker API, account data, or live trading functionality.

With Python 3.10+:

```bash
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
python tools/review_before_publish.py
```

## Engineering toolkit & responsible AI use

- **Programming:** Python, MQL5, SQL; additional coursework in Java and JavaScript/TypeScript
- **Development:** VS Code, Git/GitHub, MetaEditor, MetaTrader 5 Strategy Tester, Google Colab and Jupyter notebooks
- **Research:** reproducible backtesting, data analysis, unit tests and chronological model evaluation
- **AI-assisted development:** ChatGPT and Claude used to explore approaches, debug, review code and organize experiments. AI-generated suggestions are independently checked rather than treated as verified results
- **ML under study:** scikit-learn, financial NLP/FinBERT, PyTorch and boosting methods

This skills overview does **not** share any proprietary Expert Advisor source, market-entry rules, tuned settings, account data, or private trading results.

## Technologies and interests

Python · MQL5 · SQL · Machine Learning · NLP · Time-Series Analysis · Backtesting Research

These describe technologies I have used or studied; not all projects are production-ready. No profitability or predictive-accuracy claims are made.

## Languages and safety

- [ภาษาไทย / Thai README](README_TH.md)
- [Disclosure & security checklist (Thai)](SECURITY_CHECKLIST_TH.md)
- Private EA code, trading rules, account information, logs, and datasets are **not** published here.

This portfolio is for education and software engineering demonstration only; not trading or investment advice.
