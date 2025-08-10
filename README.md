# 🛡️ Cybersecurity Internship Projects

This repository contains two completed tasks for the **CodeAlpha Cyber Security Internship**:

1. [**Basic Network Sniffer**](#-task-1-basic-network-sniffer) – A Python tool to capture and analyze network traffic in real-time.  
2. [**Phishing Awareness Module**](#-task-2-phishing-awareness-module) – Educational content on identifying and avoiding phishing attacks.

---

## 🔍 Task 1: Basic Network Sniffer

### 📋 Overview  
A Python script leveraging the powerful [Scapy](https://scapy.net/) library to capture and display detailed network packet information including protocol types, IP addresses, ports, and payload data in real-time.

### ✨ Features  
- 🕵️‍♂️ Real-time capture of **TCP**, **UDP**, **ICMP**, and other IP packets  
- 🌐 Displays source and destination IP addresses and port numbers  
- 📊 Shows protocol-specific details (e.g., TCP flags, ICMP codes)  
- 📦 Payload inspection (if available)  
- 💻 Cross-platform support:  
  - Windows (requires [Npcap](https://nmap.org/npcap/))  
  - Linux/Mac (requires [libpcap](https://www.tcpdump.org/))

### ⚙️ Requirements  
- 🐍 [Python 3.x](https://www.python.org/downloads/)  
- 📦 [Scapy](https://scapy.net/) library  
  ```bash
  pip install scapy
  ```
  
### 🖧 Packet Capture Drivers
- **Windows:** Install [Npcap](https://nmap.org/npcap/)  
- **Linux/Mac:** `libpcap` is usually pre-installed or available via your package manager

---

### 🚀 Usage
Run the sniffer script with administrator/root privileges:
```bash
python network_sniffer.py
```
