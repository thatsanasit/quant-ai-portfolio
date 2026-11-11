# ตรวจสอบก่อนเปิด GitHub Portfolio เป็น Public

**Repository:** `thatsanasit/quant-ai-portfolio`  
**สถานะล่าสุดที่ตรวจ:** Private (11 พฤศจิกายน 2026)

## พร้อมแล้ว

- [x] README ภาษาไทยและอังกฤษ
- [x] Project Showcase แยกงานวิจัยกับเดโมที่รันได้
- [x] มี Python ตัวอย่างฝึก Random Forest / LightGBM กับข้อมูลสังเคราะห์ พร้อม Unit Tests
- [x] มีรายงานผล ML เดิมที่ระบุว่าเป็นการประเมินแบบประมาณ และผลยังไม่ได้ดีกว่า Baseline
- [x] ไฟล์ Markdown หลักที่ตรวจไม่พบลิงก์ภายในขาด
- [x] ไม่พบรูปแบบ Credential/Token ทั่วไปในไฟล์ข้อความที่ตรวจ (ไม่ใช่การรับรองว่าปลอดภัยทั้งหมด)

## ข้อมูลที่การเปิด Public จะเผยแพร่

- [x] **เจ้าของเลือกคงภาพ MT5 Demo สองภาพเดิมโดยไม่ปิดบัง** — ภาพมี Ticket ID, เวลา, BUY/SELL, ราคา, Lot, SL/TP, ผลรายไม้
- [ ] ตรวจสอบและยอมรับ **อีเมลผู้เขียนในประวัติ Commit**: Git commit เก่าใช้ที่อยู่อีเมลปกติ ไม่ใช่ GitHub noreply
- [ ] ตรวจประวัติ Commit ทุกครั้งก่อนเผยแพร่: แม้ลบไฟล์ปัจจุบัน ข้อมูลใน Git History อาจยังเข้าถึงได้
- [ ] ตรวจ Issues / Pull Requests / Releases / Actions / Tags หากเคยใช้งาน (ยังไม่ได้ตรวจครบทุกช่องทาง)
- [ ] ทบทวนภาพและเอกสารทั้งหมดจากมุมมองบุคคลภายนอก

## เปิด Public ด้วยตัวเอง

1. เปิด [Settings ของ Repository](https://github.com/thatsanasit/quant-ai-portfolio/settings)
2. เลื่อนลงส่วน **Danger Zone** บนหน้า **General**
3. เลือก **Change repository visibility** แล้วเลือก **Change to public**
4. อ่านคำเตือน ตรวจสอบชื่อ Repository และยืนยันตามขั้นตอนของ GitHub
5. เปิดหน้า [Repository](https://github.com/thatsanasit/quant-ai-portfolio) ในหน้าต่างไม่เข้าสู่ระบบ เพื่อตรวจว่าคนทั่วไปเห็นและลิงก์เปิดได้

**คำเตือน:** เมื่อเปิด Public รูป MT5 และอีเมลในประวัติ Commit อาจถูกเผยแพร่ แม้ภายหลังเปลี่ยนกลับเป็น Private ก็ไม่รับประกันว่าลบสำเนาที่คนอื่นบันทึกไปได้

## สิ่งที่ยังไม่ควรเปิดเผย

- Source Code EA จริง, สูตร/กฎเข้า BUY/SELL และพารามิเตอร์เฉพาะ
- รหัสผ่าน, Token, API Key และข้อมูลบัญชีที่ไม่ได้ตั้งใจเผยแพร่
- Dataset/Trading Log จริงเพิ่มเติมโดยไม่ได้ตรวจสิทธิ์และความลับ

อ่านก่อนเปลี่ยน Public: [คู่มือ GitHub เรื่อง Repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

_ไฟล์นี้เป็นเช็กลิสต์ ไม่ใช่การเปลี่ยน Visibility อัตโนมัติ_
