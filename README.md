# Thatsanasit Charoenthammarak

**Intelligent Information Technology Student | Quantitative Software · Python · Applied AI**

School of Informatics, Walailak University

I build and evaluate Python and MQL5 projects with an interest in quantitative development, machine learning, data analysis, and reproducible software testing.

## Featured projects

| Project | What I worked on | Explore |
|---|---|---|
| **Algorithmic Trading Systems Research** | MT5/MQL5 development, experiment logging, software debugging, and demo-account evaluation | [Project](projects/algorithmic-trading-research.md) · [MT5 evidence](projects/mt5-forward-testing-evidence.md) |
| **Machine Learning Model Evaluation** | Random Forest and LightGBM evaluation, chronological splits, ROC AUC/Brier metrics; separate runnable training example | [Case study](projects/ml-chronological-evaluation.md) · [Python code](examples/synthetic_ml_training.py) |
| **Gold News Analyzer** *(in progress)* | Research on financial news sentiment, market direction, and volatility estimation | [Research overview](projects/gold-news-analyzer.md) |

## Additional Python projects

| Project | Focus | Code |
|---|---|---|
| **Walk-Forward Evaluation** | Time-series baseline, AR(1), MAE/RMSE, leakage checks | [Python](examples/walk_forward_synthetic.py) · [Notes](projects/synthetic-walk-forward-demo.md) |
| **Sales Analytics Pipeline** | Data validation, deduplication, aggregation, unit tests | [Python](examples/synthetic_sales_pipeline.py) · [Notes](projects/synthetic-sales-analytics.md) |
| **Volatility Analysis** | Artificial OHLC observations, true range, simple ATR | [Python](demo/synthetic_volatility.py) |

All runnable portfolio demonstrations use **synthetic data**. The ML case study summarizes a separate historical experiment with limited results, while the MT5 page contains **original demo-testing screenshots**. These are not claims of trading profitability.

## Skills and tools

- **Programming:** Python, MQL5, SQL; Java and JavaScript/TypeScript coursework
- **ML and data analysis:** scikit-learn, LightGBM, Random Forest, chronological validation, statistical metrics
- **Development and testing:** Git/GitHub, unit tests, VS Code, Jupyter, Google Colab, MetaEditor, MT5 Strategy Tester
- **AI-assisted workflow:** ChatGPT and Claude for implementation support, debugging, code review, and documentation, with testing and critical evaluation

## Run the examples

Python 3.10+ is recommended. Install the additional dependencies to run the ML example and the full test suite.

```bash
python -m pip install -r requirements-ml.txt
python examples/synthetic_ml_training.py
python examples/walk_forward_synthetic.py
python examples/synthetic_sales_pipeline.py
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
```

**[Browse all project descriptions](projects/README.md)** · **[ภาษาไทย](README_TH.md)**

*Project descriptions and demonstrations are provided for technical review. Proprietary EA source code and trading decision rules are not included.*
