"""Conservative allowlist / pattern check, NOT a comprehensive secret scanner."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ALLOWED = {
    "README.md",
    "README_TH.md",
    "PROFILE_README_TEMPLATE.md",
    "SECURITY_CHECKLIST_TH.md",
    ".gitignore",
    "projects/algorithmic-trading-research.md",
    "projects/gold-news-analyzer.md",
    "projects/time-series-evaluation.md",
    "demo/synthetic_volatility.py",
    "tests/test_synthetic_volatility.py",
    "tools/review_before_publish.py",
    "examples/walk_forward_synthetic.py",
    "tests/test_walk_forward_synthetic.py",
    "projects/synthetic-walk-forward-demo.md",
    "examples/synthetic_sales_pipeline.py",
    "tests/test_synthetic_sales_pipeline.py",
    "projects/synthetic-sales-analytics.md",
    "projects/README.md",
    "projects/README_TH.md",
    "projects/mt5-forward-testing-evidence.md",
    "projects/mt5-forward-testing-evidence_TH.md",
    "assets/mt5-history-2026-10-29-morning.png",
    "assets/mt5-history-2026-10-29-afternoon.png",
}
PATTERNS = {
    "private key": r"-----BEGIN\s+(?:RSA\s+|EC\s+|OPENSSH\s+)?PRIVATE\s+KEY-----",
    "GitHub token": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})",
    "cloud key": r"\bAKIA[0-9A-Z]{16}\b",
    "API key": r"\bsk-[A-Za-z0-9_-]{24,}\b",
}


def main() -> int:
    problems: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in {".git", "__pycache__"} for part in rel.parts):
            continue
        name = rel.as_posix()
        if name not in ALLOWED:
            problems.append(f"Unexpected file: {name}")
            continue
        if path.stat().st_size > 1_000_000:
            problems.append(f"Large file: {name}")
            continue
        if path.suffix.lower() == ".png":
            if not path.read_bytes().startswith(bytes((137, 80, 78, 71, 13, 10, 26, 10))):
                problems.append(f"Unexpected PNG contents: {name}")
            # Two owner-approved, unredacted screenshots; manual review is still required.
            continue
        content = path.read_text(encoding="utf-8")
        for label, pattern in PATTERNS.items():
            if re.search(pattern, content):
                problems.append(f"Possible {label} in {name}")
    if problems:
        print("REVIEW REQUIRED:")
        for item in problems:
            print("-", item)
        return 1
    print("Allowlist and basic checks passed; manual review still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
