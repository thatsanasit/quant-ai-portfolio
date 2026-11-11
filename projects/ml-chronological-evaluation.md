# Machine Learning Experiment: Chronological Evaluation (Case Study)

**Status:** Documented historical research result + independently runnable educational ML example  
**Technologies:** Python, Random Forest, LightGBM, chronological holdout, ROC AUC, Brier score  
**Disclosure:** No proprietary trading strategy, raw MT5 datasets, EA execution rules or trained private weights are published.

## Research question

Could a supervised model improve automated decision-making over an existing baseline? This historical experiment tested classification approaches in an offline, approximate evaluation setup. The purpose of this portfolio page is to demonstrate how experiments are designed, measured, and critically interpreted—not to claim profitable AI trading.

## Historical experiment: what was actually observed

The following values come from a locally saved `ML_Chronological_Test_Metrics_APPROX.csv` report, checked on **11 November 2026**. The experiment used a chronological validation/test split and **approximate labels derived from M1 bars**, *not* verified execution-level or live performance.

| Model | Chronological test events | Test ROC AUC | Test Brier score |
|---|---:|---:|---:|
| Random Forest | 449 | 0.5365 | 0.2362 |
| LightGBM | 449 | 0.5279 | 0.2379 |

**Interpretation:** ROC AUC values only slightly above 0.5 indicate weak ranking ability. More importantly, the model-based side changes **performed worse than the original baseline** in the offline approximate outcome report. These results **do not demonstrate useful or profitable model improvement**. There was also no confirmed robust out-of-sample benefit from this experiment.

**Limitations:** Small test sample, trading costs and slippage not independently reproduced in the approximation, market nonstationarity, dependence between sequential observations, and uncertainty about matching intrabar execution. The raw private data are intentionally not included in this public-facing write-up. Do not compare the approximate outcome figures with live trading statements.

## Reproducible, independent learning demonstration

To show actual model fitting without disclosing any research data, this repository includes a separate **synthetic factory-sensor classification** example. It is **not trained on market data** and is **not a reproduction of the private experiment**.

[Source code](../examples/synthetic_ml_training.py) · [Unit tests](../tests/test_synthetic_ml_training.py) · [Dependencies](../requirements-ml.txt)

The demonstration:
1. Creates 2,400 artificial observations deterministically.
2. Splits them chronologically: 60% train, 20% validation, 20% untouched test.
3. Fits Random Forest and LightGBM classifiers and compares them with a constant-probability baseline.
4. Reports ROC AUC and Brier score, showing both discrimination and probability calibration error.
5. Uses unit tests to verify reproducible data, chronological separation, valid metric ranges, and invalid-input handling.

### Example run (synthetic data only)

```bash
python -m pip install -r requirements-ml.txt
python examples/synthetic_ml_training.py
python -m unittest discover -s tests -v
```

The locally executed default synthetic demonstration produced:

| Synthetic model | Validation AUC | Test AUC | Test Brier |
|---|---:|---:|---:|
| Constant baseline | 0.5000 | 0.5000 | 0.2502 |
| Random Forest | 0.7531 | 0.7720 | 0.1971 |
| LightGBM | 0.7547 | 0.7777 | 0.1948 |

These synthetic metrics **must not** be presented as actual trading model results, financial predictions, or customer outcomes. Unit tests of this new demonstration passed **5/5 locally**, not in a GitHub Actions CI run.

## AI-assisted workflow and responsibilities

AI tools supported drafting code and documentation. The actual code executes `model.fit`, makes probability predictions, evaluates held-out observations, and is accompanied by test assertions. The author should be able to explain the choice of baseline, temporal split, metrics, limitations, and what would change in a deployment-grade evaluation.

**Main lesson:** An ML experiment is valuable even when it fails to outperform a baseline, provided it is evaluated honestly, does not leak future information, and produces learnings for subsequent experiments.

[Project index](README.md) · [Thai version](ml-chronological-evaluation_TH.md)
