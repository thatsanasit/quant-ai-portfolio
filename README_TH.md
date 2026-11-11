# ทัศนสิทธิ์ เจริญธรรมรักษ์
### นักศึกษาเทคโนโลยีสารสนเทศอัจฉริยะ | Quantitative Development · Applied AI · Data Analysis

**สำนักวิชาสารสนเทศศาสตร์ มหาวิทยาลัยวลัยลักษณ์**

สนใจการพัฒนาซอฟต์แวร์เชิงปริมาณ การวิเคราะห์ข้อมูล AI/Machine Learning และการออกแบบการทดลองที่ตรวจสอบผลได้ โดยมีประสบการณ์ทำโปรเจกต์ด้วย Python และ MQL5

## ผลงานที่น่าสนใจ

**[ดู Project Showcase ทั้งหมด](projects/README_TH.md)** — แยกงานวิจัยที่กำลังทำกับโค้ดตัวอย่างที่รันได้


| โครงงาน | ทักษะที่แสดง | รายละเอียด |
|---|---|---|
| **Gold News Analyzer** *(กำลังวิจัย)* | วิเคราะห์ข่าวการเงิน, NLP, การประเมินโมเดลตามลำดับเวลา | [ภาพรวมโครงงาน](projects/gold-news-analyzer.md) |
| **Algorithmic Trading Systems Research** | การพัฒนา MQL5/Python, Debugging, Backtesting และความสามารถในการทดสอบซ้ำ | [ภาพรวมงานวิจัย](projects/algorithmic-trading-research.md) · [ภาพประวัติ MT5 จริง](projects/mt5-forward-testing-evidence_TH.md) |
| **Synthetic Walk-Forward Evaluation** | Python, Walk-Forward, Baseline, MAE/RMSE และ Unit Tests | [โค้ดตัวอย่าง](examples/walk_forward_synthetic.py) · [คำอธิบาย](projects/synthetic-walk-forward-demo.md) |
| **Synthetic Volatility Demo** | ข้อมูล OHLC จำลองและการคำนวณ True Range/ATR | [โค้ดตัวอย่าง](demo/synthetic_volatility.py) |
| **Synthetic Sales Analytics Pipeline** *(ตัวอย่างสร้างด้วย AI ช่วย)* | Python, Data Cleaning, การจัดการข้อมูลซ้ำ และ Unit Tests | [รายละเอียด](projects/synthetic-sales-analytics.md) |

| **ML Model Training & Chronological Evaluation** *(กรณีศึกษา + เดโมฝึกโมเดล)* | ฝึก Random Forest / LightGBM, ROC AUC, Brier Score, ประเมินตามเวลา | [กรณีศึกษาภาษาไทย](projects/ml-chronological-evaluation_TH.md) · [โค้ดฝึกโมเดล](examples/synthetic_ml_training.py) |

## ทักษะและเครื่องมือ

- **ภาษาโปรแกรม:** Python, MQL5, SQL และวิชาที่ศึกษาเพิ่มเติม Java, JavaScript/TypeScript
- **เครื่องมือพัฒนา:** VS Code, Git/GitHub, MetaEditor, MT5 Strategy Tester, Google Colab, Jupyter
- **ข้อมูลและการวิจัย:** Time-Series Analysis, Backtesting, การจัดทำบันทึกการทดลอง, Unit Testing
- **AI/ML:** ChatGPT, Claude, scikit-learn และกำลังศึกษา FinBERT, PyTorch, Gradient Boosting

## การใช้ AI ช่วยพัฒนาซอฟต์แวร์

ใช้ **ChatGPT และ Claude** ช่วยพัฒนาโปรแกรม วิเคราะห์และแก้ไขข้อผิดพลาด ทบทวนโค้ด วางแผนการทดลอง และจัดทำเอกสารทางเทคนิค พร้อม **ตรวจสอบผลด้วยการทดสอบอย่างเป็นระบบ** ไม่ถือว่าคำตอบจาก AI ถูกต้องโดยอัตโนมัติ

## วิธีทดลองโค้ดตัวอย่าง

ใช้ Python 3.10+ และ Standard Library

```bash
python examples/walk_forward_synthetic.py
python demo/synthetic_volatility.py
python examples/synthetic_sales_pipeline.py
# ตัวอย่าง ML แยก: ติดตั้ง requirements-ml.txt ก่อน
# python examples/synthetic_ml_training.py
python -m unittest discover -s tests -v
python tools/review_before_publish.py
```

โค้ดสาธิตมาตรฐานใช้ Python Standard Library ส่วนเดโม ML เพิ่มเติมต้องติดตั้งไลบรารีจาก requirements-ml.txt

ข้อมูลในโค้ดตัวอย่างเป็น **ข้อมูลสังเคราะห์** เพื่อแสดงวิธีประเมินโปรแกรมและโมเดลเท่านั้น ไม่ใช่ผลกำไรหรือคำแนะนำการลงทุน

[English version](README.md) · [เช็กลิสต์การตรวจความปลอดภัย](SECURITY_CHECKLIST_TH.md) · [เช็กก่อนเปิด Public](PUBLIC_RELEASE_CHECKLIST_TH.md) · [เตรียมสัมภาษณ์](INTERVIEW_PREP_TH.md)

*Repository นี้ประกอบด้วยสรุปโครงงาน โค้ดตัวอย่าง และภาพประวัติ MT5 จริง 2 ภาพที่เจ้าของอนุญาตให้เผยแพร่โดยไม่ปิดบังข้อมูล ไม่มีโค้ด EA หรือสูตรเลือกฝั่งจริง โปรดทบทวนข้อมูลในภาพก่อนเปิด Public*
