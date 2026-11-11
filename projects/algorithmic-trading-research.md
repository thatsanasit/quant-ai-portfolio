# Algorithmic Trading Systems Research

**Type:** Independent student software engineering and research  
**Stack:** MQL5, MetaTrader 5, Python, testing and experiment analysis  
**Environment:** MT5 demo-account experiments

## Why I built this project

I wanted to understand how an automated trading system can make decisions, send orders, and be **tested and debugged as software**, rather than judging it by a few profitable trades. Short timeframes are noisy; price can reverse or continue rapidly, and an entry that looks reasonable can still reach its stop-loss first.

The engineering goal is to improve the **quality of experiments and error analysis**. It is not a claim that the system is reliably profitable.

## What I worked on

- **MQL5 implementation and debugging:** Developed and iterated automated order-execution experiments in MetaTrader 5.
- **Order-history inspection:** Reviewed timestamps, directions, exits and loss cases to understand system behavior.
- **Variant comparison:** Compared different versions and kept records of what changed rather than assuming a newer version is better.
- **Reproducible testing:** Investigated conditions that can make repeated backtests produce different orders and worked with controlled testing procedures.
- **Python-based analysis:** Used scripts and summarized results to examine experiments while separating exploratory observations from stronger evidence.
- **AI-assisted development:** Used AI tools to support code review, troubleshooting and research documentation, followed by verification and testing.

## Why these steps matter

| Problem | Engineering reasoning |
|---|---|
| The system sometimes enters on the wrong side or at the wrong moment | Review prior market context and execution history, then test hypotheses rather than modifying rules based on one trade |
| A few trades win consecutively | A short sequence is not enough to prove an advantage; evaluate longer windows and different market conditions |
| Backtests differ between repeated runs | Check reproducibility, data assumptions and potential dependence on machine/runtime state |
| Many trades have small profit targets | Spread, slippage and trading costs can materially change the result |
| A new version appears better | Compare on held-out periods, account for sample size and avoid tuning directly to the test set |
| A machine-learning model produces predictions | Compare it with a baseline and verify whether decisions actually improve, not just whether a metric is above chance |

## Evidence and observations

[Original MT5 demo-testing screenshots](mt5-forward-testing-evidence.md) · [คำอธิบายภาษาไทย](algorithmic-trading-research_TH.md)

The screenshots from two periods show both successful and losing exits. **Some market phases appeared more favorable for certain entries, but performance was not consistently good.** The screenshots cannot establish that a particular trend regime was the cause of the winning trades or that the EA is profitable overall.

## Limitations and what I learned

- Signal selection, testing assumptions and market conditions can interact in ways that are difficult to infer from one trade.
- Reproducibility matters: an apparent improvement is less meaningful if the test cannot be repeated reliably.
- Strong evaluation requires multiple time periods, appropriate baselines and explicit treatment of uncertainty and trading costs.
- Even unsuccessful experiments can reveal software defects, flawed assumptions, or useful next research questions.

## Scope of publication

This page intentionally omits **proprietary EA source code, detailed BUY/SELL decision logic, optimized strategy parameters, account credentials and complete private datasets**. Screenshots are from the author's demo-testing workflow.

**This is a software engineering case study, not proof of investment returns or financial advice.**

[Project Showcase](README.md) · [Thai version](algorithmic-trading-research_TH.md)
