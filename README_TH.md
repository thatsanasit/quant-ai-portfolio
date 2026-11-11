# ทัศนสิทธิ์ เจริญธรรมรักษ์

**นักศึกษาเทคโนโลยีสารสนเทศอัจฉริยะ | Quantitative Software · Python · Applied AI**

สำนักวิชาสารสนเทศศาสตร์ มหาวิทยาลัยวลัยลักษณ์

สนใจการพัฒนาซอฟต์แวร์ด้วย Python และ MQL5 การวิเคราะห์ข้อมูล AI/Machine Learning และการออกแบบการทดลองที่ตรวจสอบผลซ้ำได้

## ผลงานหลัก

| โปรเจกต์ | สิ่งที่ทำ | ดูผลงาน |
|---|---|---|
| **Algorithmic Trading Systems Research** | พัฒนาระบบด้วย MQL5/MT5, ติดตามผลการทดลอง, Debugging และประเมินการทำงานบนบัญชี Demo | [โครงงานและเหตุผลการพัฒนา](projects/algorithmic-trading-research_TH.md) · [ภาพ MT5 จริง](projects/mt5-forward-testing-evidence_TH.md) |
| **Machine Learning Model Evaluation** | ทดลอง Random Forest และ LightGBM แบ่งข้อมูลตามเวลา ประเมิน ROC AUC/Brier และสร้างโค้ดฝึกโมเดลตัวอย่าง | [กรณีศึกษา](projects/ml-chronological-evaluation_TH.md) · [Python](examples/synthetic_ml_training.py) |
| **Gold News Analyzer** *(กำลังพัฒนา)* | ศึกษาการวิเคราะห์ข่าวการเงิน ความเชื่อมั่น ทิศทางราคาและความผันผวนของทองคำ | [รายละเอียด](projects/gold-news-analyzer.md) |

## ตัวอย่างโค้ด Python เพิ่มเติม

| โปรเจกต์ | ทักษะที่แสดง | โค้ด |
|---|---|---|
| **Walk-Forward Evaluation** | Time Series, AR(1), MAE/RMSE, ป้องกัน Data Leakage | [Python](examples/walk_forward_synthetic.py) · [รายละเอียด](projects/synthetic-walk-forward-demo.md) |
| **Sales Analytics Pipeline** | Data Validation, Deduplication, Aggregation, Unit Tests | [Python](examples/synthetic_sales_pipeline.py) · [รายละเอียด](projects/synthetic-sales-analytics.md) |
| **Volatility Analysis** | ข้อมูล OHLC สังเคราะห์และการคำนวณ True Range/ATR | [Python](demo/synthetic_volatility.py) |

ตัวอย่างโค้ดที่รันได้ใช้ **ข้อมูลสังเคราะห์** ส่วนกรณีศึกษา ML อธิบายการทดลองเดิมที่ผลยังมีข้อจำกัด และหน้า MT5 แสดง **ภาพการทดลองบนบัญชี Demo จริง** ไม่ใช่คำกล่าวอ้างว่าระบบทำกำไรอย่างสม่ำเสมอ

## ทักษะและเครื่องมือ

- **Programming:** Python, MQL5, SQL; ศึกษา Java และ JavaScript/TypeScript ในรายวิชา
- **ML / Data:** scikit-learn, LightGBM, Random Forest, การแบ่งข้อมูลตามเวลาและตัวชี้วัดเชิงสถิติ
- **Development / Testing:** Git/GitHub, Unit Testing, VS Code, Jupyter, Google Colab, MetaEditor และ MT5 Strategy Tester
- **AI-assisted Development:** ใช้ ChatGPT และ Claude ช่วยพัฒนา Debug และทบทวนโค้ด พร้อมตรวจสอบผลจากการทดลอง

## วิธีรันโค้ด

แนะนำ Python 3.10+ และติดตั้งไลบรารีสำหรับตัวอย่าง ML ก่อนรัน Test Suite ทั้งหมด

```bash
python -m pip install -r requirements-ml.txt
python examples/synthetic_ml_training.py
python examples/walk_forward_synthetic.py
python examples/synthetic_sales_pipeline.py
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
```

**[ดูรายละเอียดทุกโปรเจกต์](projects/README_TH.md)** · **[English version](README.md)**

*นำเสนอภาพรวมโครงงานและโค้ดสาธิตที่ตรวจสอบได้ โดยไม่เผยแพร่ Source Code หรือสูตรเลือกฝั่งออเดอร์ของ EA จริง*
