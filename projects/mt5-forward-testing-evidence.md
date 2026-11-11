# MT5 Forward-Testing Evidence — Privacy-Safe Presentation

**Context:** Algorithmic Trading Systems Research / MQL5 and Python  
**Platform:** MetaTrader 5  
**Evidence source:** Two distinct order-history screenshots provided by the project author, showing entries from October 2026  
**Publication method:** Schematic reconstruction with **all actual trade rows and values omitted**. Original screenshots are not uploaded.

![Privacy-safe visual reconstruction of MT5 forward-testing history](../assets/mt5-forward-testing-redacted.svg)

## What was observed

The supplied screenshots contain multiple closed-order rows from a MetaTrader 5 history view. The display includes order direction, time, prices, stop levels, lot volume, and individual trade outcomes. The first and third supplied screenshots show the same excerpt; only two different excerpts were considered.

## Engineering work this illustrates

- Using MT5 to run and monitor algorithmic order execution
- Reviewing entry/exit records and logging experimental outcomes
- Diagnosing software behavior using testing history
- Comparing experiment variants while considering reproducibility and limitations
- Preparing documentation without publishing proprietary implementation details

## Evidence and limitations

- This page **does not** publish the original screenshots, real trade data, transaction-level statistics or proprietary Expert Advisor logic.
- The graphic above is **an illustrative reconstruction**, not an authentic screenshot or verified performance chart.
- The screenshots alone do **not** establish that the account was a demo account, that the EA was profitable overall, or that a model met out-of-sample performance targets.
- No total profit, win rate, ROI, Sharpe ratio or drawdown is claimed on the basis of the excerpts.
- The underlying source screenshots can be reviewed privately when appropriate, after separate confidentiality review.

## Confidentiality

Original screenshots were deliberately excluded because they contain ticket identifiers, exact times, order sequence, lot sizing, entry/exit prices, SL/TP, and trade-by-trade profit/loss. The owner has chosen not to publish the EA's trading signals, model parameters, broker/account information, datasets or source code.

This is a **software engineering evidence exhibit**, not investment advice or a strategy performance endorsement.

[Back to Algorithmic Trading Research](algorithmic-trading-research.md) · [ภาษาไทย](mt5-forward-testing-evidence_TH.md)
