# Network Systems Project

โปรเจคระบบเครือข่าย 2 ระบบ: Chat Room และ SNMP Monitoring

## 💬 Chat Room System

**Files:** `chatServer.py`, `chatClient.py`, `test_chatDB2.py`

### การทำงาน
- Server รอรับ connection ที่ port 5000
- Client เชื่อมต่อ → กรอกชื่อ → สนทนาได้
- รองรับหลายคนพร้อมกัน (max 10 คน)
- บันทึกข้อความพร้อมเวลา

### วิธีใช้
```bash
# เริ่ม server
python chatServer.py

# เริ่ม client (เปิดได้หลาย terminal)
python chatClient.py
```

## 📊 SNMP Monitoring System

**Files:** `snmpServer.py`, `snmpClient.py`

### การทำงาน
- Server รอรับ connection ที่ port 8080
- Client ส่งคำสั่งเพื่อตรวจสอบระบบ
- ใช้รหัสผ่าน: `12345`

### Commands
- `01` = Login (ใส่รหัส 12345)
- `02` = ดู CPU usage
- `03` = ดู Memory usage  
- `99` = ออกจากระบบ

### วิธีใช้
```bash
# เริ่ม server
python snmpServer.py

# เริ่ม client
python snmpClient.py
```

## Requirements
```bash
pip install psutil
```
