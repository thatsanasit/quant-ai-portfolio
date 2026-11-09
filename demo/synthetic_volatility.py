"""Educational example using synthetic OHLC-like values only.

No live or historical market data, no signals, no trading and no network I/O.
"""
from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass(frozen=True)
class Bar:
    open: float
    high: float
    low: float
    close: float


def make_synthetic_bars(count: int = 240, seed: int = 42) -> list[Bar]:
    """Return deterministic artificial OHLC bars, never actual market prices."""
    if count < 1:
        raise ValueError("count must be positive")
    random = Random(seed)
    prev_close = 100.0
    result: list[Bar] = []
    for _ in range(count):
        open_price = prev_close
        close_price = max(0.01, open_price + random.gauss(0, 0.30))
        high_price = max(open_price, close_price) + abs(random.gauss(0, 0.12))
        low_price = max(0.001, min(open_price, close_price) - abs(random.gauss(0, 0.12)))
        result.append(Bar(open_price, high_price, low_price, close_price))
        prev_close = close_price
    return result


def true_ranges(bars: list[Bar]) -> list[float]:
    """Compute the standard true range from valid bars."""
    values: list[float] = []
    previous_close: float | None = None
    for bar in bars:
        if bar.high < bar.low or not (bar.low <= bar.open <= bar.high):
            raise ValueError("invalid OHLC bar")
        if not (bar.low <= bar.close <= bar.high):
            raise ValueError("invalid OHLC bar")
        candidates = [bar.high - bar.low]
        if previous_close is not None:
            candidates.extend([
                abs(bar.high - previous_close),
                abs(bar.low - previous_close),
            ])
        values.append(max(candidates))
        previous_close = bar.close
    return values


def rolling_atr(bars: list[Bar], period: int = 14) -> list[float | None]:
    """Calculate a trailing simple mean of true range without future data."""
    if period < 1:
        raise ValueError("period must be positive")
    ranges = true_ranges(bars)
    result: list[float | None] = []
    window_sum = 0.0
    for index, value in enumerate(ranges):
        window_sum += value
        if index >= period:
            window_sum -= ranges[index - period]
        result.append(window_sum / period if index + 1 >= period else None)
    return result


def main() -> None:
    bars = make_synthetic_bars()
    values = rolling_atr(bars, 14)
    print("SYNTHETIC DATA ONLY — EDUCATIONAL DEMO")
    print(f"Generated bars: {len(bars)}")
    print(f"Final synthetic close: {bars[-1].close:.4f}")
    print(f"Final simple ATR: {values[-1]:.4f}")
    print("No market feed, signals, broker account or trading operations.")


if __name__ == "__main__":
    main()
