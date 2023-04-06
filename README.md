![tsuta_tenki](https://user-images.githubusercontent.com/104154862/230295402-33b5df59-c3e5-4f28-b104-5d47b6cbb565.jpg)

# Tsuita_tenki
นี่เป็นสคริปต์ Python ที่โพสต์รายงานสภาพอากาศและข้อมูล PM 2.5 บน Twitter โดยใช้ OpenAI API 
เพื่อสร้างข้อความรายงานสภาพอากาศและเว็บไซต์ AQICN เพื่อรับข้อมูล PM 2.5

## เริ่มต้น
* clone repository นี้
* ติดตั้งแพ็กเกจที่จำเป็นโดยรัน pip install -r requirements.txt
* ตั้งค่า API keys ของ Twitter และแทนที่ตัวแปร consumer_key consumer_secret access_token และ access_token_secret ในโค้ดด้วย keys ของคุณ
* รันสคริปต์โดยรัน python main.py

## วิธีใช้
สคริปต์จะทำงานครั้งเดียวต่อวันเวลา 7:40 นาฬิกาตามเวลากรุงเทพฯ 
และโพสต์ทวีตพร้อมรายงานสภาพอากาศและข้อมูล PM 2.5

## การมีส่วนร่วม
หากคุณพบปัญหาใดๆกับสคริปต์หรือมีคำแนะนำสำหรับการปรับปรุงโปรเจ็กต์ 
โปรดส่ง pull request หรือเปิด issue
