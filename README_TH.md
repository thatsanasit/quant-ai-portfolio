# Quantitative Development และ Applied AI — แฟ้มผลงาน

ผู้จัดทำ: นักศึกษาสาขา **เทคโนโลยีสารสนเทศอัจฉริยะ (Intelligent Information Technology)** สำนักวิชาสารสนเทศศาสตร์ มหาวิทยาลัยวลัยลักษณ์

Repository นี้ใช้รวบรวมผลงานเชิงเทคนิคสำหรับการสมัครฝึกงานสาย Quantitative Developer, AI และ Machine Learning โดยเริ่มจากสถานะ **Private**

## โปรเจกต์ที่แนะนำ

1. [Algorithmic Trading Systems Research](projects/algorithmic-trading-research.md) — แนวคิดด้านการพัฒนาและทดสอบซอฟต์แวร์ระบบเทรดอัตโนมัติ (เผยแพร่เฉพาะภาพรวม)
2. [Gold News Analyzer](projects/gold-news-analyzer.md) — ศึกษาข่าวเศรษฐกิจและการเคลื่อนไหวของราคาทองคำด้วย NLP และ ML (อยู่ระหว่างพัฒนา)
3. [Time-Series Evaluation](projects/time-series-evaluation.md) — วิธีตรวจสอบการทดลองข้อมูลตามลำดับเวลาและป้องกันข้อมูลรั่วจากอนาคต

## ตัวอย่างโค้ด Python

`demo/synthetic_volatility.py` ใช้ **ข้อมูลสังเคราะห์** เท่านั้น เพื่อสาธิตการคำนวณค่าความผันผวนทางสถิติ ไม่มีการเชื่อมต่อ MT5 ไม่มีระบบเปิดคำสั่ง BUY/SELL และไม่มีสูตรเทรดจริง

```bash
python demo/synthetic_volatility.py
python -m unittest discover -s tests -v
python tools/review_before_publish.py
```

## ขอบเขตข้อมูลที่เก็บเป็นความลับ

ไม่รวมโค้ด EA จริง, สูตรตัดสินใจซื้อขาย, พารามิเตอร์เฉพาะ, รหัสผ่าน, Token, ข้อมูลบัญชี, ไฟล์ Tester/Log, ข้อมูลราคาและข่าวที่มีข้อจำกัด หรือผลวิจัยที่ยังไม่ต้องการเผยแพร่

**คำอธิบายโปรเจกต์ไม่ได้หมายถึงการรับรองว่ากลยุทธ์มีกำไรหรือโมเดลทำนายถูกต้องแล้ว** อ่าน [เช็กลิสต์ความปลอดภัย](SECURITY_CHECKLIST_TH.md) ก่อนเผยแพร่ทุกครั้ง
