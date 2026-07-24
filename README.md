# Luana D'Amore — Cybersecurity Portfolio

CS student at UZH (year 2), learning cybersecurity hands-on.

Currently working through: Linux CLI, networking, web security, and AppSec labs.  

---

## Certifications

- ISC2 CC — exam scheduled August 2026
- Google Cybersecurity Certificate
- Linkedin Learning CompTIA Security+ Prep course with certificate

---

## Skills

- **Linux:** command line, file permissions, bash scripting, SSH
- **Networking:** TCP/IP, DNS, HTTP, Wireshark, Nmap
- **Web Security:** Burp Suite, OWASP Top 10, SQLi, XSS, SSRF
- **Blue Team:** log analysis, SIEM, incident response, MITRE ATT&CK
- **Scripting:** Python, Bash

---

## Reports & Tools

Work in progress — added as completed.

- `reports/incident-report-01.md` — blue team incident report with MITRE ATT&CK mapping
- `reports/wireshark-analysis-01.md` — PCAP traffic analysis
- `reports/web-vuln-sqli.md` — SQL injection vulnerability report
- `reports/web-vuln-xss.md` — XSS vulnerability report
- `reports/dvwa-pentest-report.md` — full pentest report on DVWA (flagship)
- `tools/header-checker/` — Python script to audit HTTP security headers

---

## Platforms

- TryHackMe: https://tryhackme.com/p/luanadamore
- PortSwigger Web Security Academy: https://portswigger.net/web-security
- OverTheWire: https://overthewire.org/wargames/
- CyberDefenders: https://cyberdefenders.org

---

*Updated July 2026*

# Port Checker
A bash script that checks whether ports 22, 80, and 443 are open or closed on a given target.

## Usage
```bash
./port-checker.sh <target>

Example
./port-checker.sh google.com

Output
Target: google.com
-------------------
[OPEN]   Port 22 (SSH)
[CLOSED] Port 80 (HTTP)
[OPEN]   Port 443 (HTTPS)

How it works
Uses /dev/tcp — a Linux built-in that attempts a TCP connection to a host and port without any external tools. Exit code 0 = open, anything else = closed.

Ports checked
22 =SSH (remote control)
80 =HTTP (web, unencryped)
443 =HTTPS (web, encrypted)
