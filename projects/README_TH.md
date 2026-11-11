# ผลงานด้าน Software, AI/ML และ Data

รวบรวมผลงานวิจัย การทดลอง และตัวอย่างโค้ดที่สามารถตรวจสอบได้ โดยแยก **งานที่กำลังพัฒนา** ออกจาก **ตัวอย่างที่รันได้**

## ผลงานหลัก

| โปรเจกต์ | สถานะ | หลักฐาน |
|---|---|---|
| [Algorithmic Trading Systems Research](algorithmic-trading-research.md) | วิจัยและทดลองระบบด้วย MT5 Demo | [ภาพประวัติ MT5 จริง](mt5-forward-testing-evidence_TH.md) |
| [Machine Learning Model Evaluation](ml-chronological-evaluation_TH.md) | ผลการทดลองเดิมแบบประมาณ + ตัวอย่างฝึก ML ที่รันได้ | [โค้ด Random Forest / LightGBM](../examples/synthetic_ml_training.py) · [Tests](../tests/test_synthetic_ml_training.py) |
| [Gold News Analyzer](gold-news-analyzer.md) | งานวิจัยระหว่างพัฒนา | เป้าหมายและแนวทางการประเมิน |

## ตัวอย่างโค้ดเพิ่มเติม

| โปรเจกต์ | สิ่งที่แสดง |
|---|---|
| [Walk-Forward Evaluation](synthetic-walk-forward-demo.md) | Time Series, Baseline, Data Leakage, Unit Tests |
| [Sales Analytics Pipeline](synthetic-sales-analytics.md) | Data Cleaning, Validation, Deduplication, Reporting |
| [Volatility Analysis](../demo/synthetic_volatility.py) | True Range และ ATR จากข้อมูลจำลอง |

## วิธีรันและทดสอบ

```bash
python -m pip install -r requirements-ml.txt
python examples/synthetic_ml_training.py
python examples/walk_forward_synthetic.py
python examples/synthetic_sales_pipeline.py
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
```

ตัวอย่างโปรแกรมใช้ข้อมูลสังเคราะห์ทั้งหมด ส่วนภาพ MT5 เป็นภาพการทดสอบ Demo ที่เจ้าของโครงการให้เผยแพร่ โดยไม่รวมโค้ด EA หรือสูตรซื้อขายจริง

[English](README.md) · [กลับหน้าแรก](../README_TH.md)
