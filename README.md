# HTTP Packet Sniffer (Educational Project)

## 📌 Loyihaning tavsifi
Ushbu loyiha **Python (Scapy)** yordamida yozilgan **HTTP packet sniffer** bo‘lib, tarmoq orqali o‘tayotgan **faqat HTTP (port 80)** so‘rovlarini aniqlash va log qilish uchun mo‘ljallangan.

Loyiha **o‘quv va test (lab) muhitlari** uchun yaratilgan bo‘lib, real tarmoqlarda ruxsatsiz foydalanish **taqiqlanadi**.

---

## ⚙️ Qanday ishlaydi?
Sniffer quyidagi prinsip asosida ishlaydi:

- Belgilangan **Target IP** manzildan chiqayotgan trafik kuzatiladi
- Faqat **HTTP so‘rovlari (GET/POST)** aniqlanadi
- URL (Host + Path) log faylga yoziladi
- Agar HTTP payload ichida login/parolga o‘xshash ma’lumotlar aniqlansa, alohida qayd etiladi

📌 **Muhim:**  
Ushbu dastur **HTTPS (443)** trafikni tahlil qilmaydi.

---

## 🧪 Test muhiti va foydalanish shartlari
Sniffer to‘g‘ridan-to‘g‘ri boshqa qurilma trafikini ko‘ra olmaydi. Shu sababli test muhitida:

- Qurilmalar bir xil **Local Area Network (LAN)** ichida bo‘lishi kerak
- Avval **MITM (Man-in-the-Middle)** holati yaratiladi
- Test maqsadida **ARP Spoofing** usuli qo‘llaniladi
- Shundan so‘ng sniffer orqali HTTP trafik kuzatiladi

⚠️ **Eslatma:**  
ARP spoofing va packet sniffing **faqat ruxsat berilgan test muhitida** amalga oshirilishi lozim.

---

## 🚫 Cheklovlar
- ❌ HTTPS trafik tahlil qilinmaydi
- ❌ Shifrlangan ma’lumotlar ko‘rinmaydi
- ❌ Real tarmoqlarda ruxsatsiz ishlatish mumkin emas

---

## 📝 Loglash
- Barcha aniqlangan HTTP so‘rovlar log faylga yoziladi
- Terminaldagi rangli chiqish log faylda toza matn ko‘rinishida saqlanadi

---

## 📚 Texnologiyalar
- Python 3
- Scapy
- argparse
- Linux (Kali Linux test muhitida sinovdan o‘tkazilgan)

---

## ⚖️ Mas’uliyat
Ushbu loyiha **faqat ta’limiy maqsadlar** uchun mo‘ljallangan.  
Muallif loyiha noto‘g‘ri yoki noqonuniy maqsadlarda ishlatilishi uchun javobgar emas.

---


