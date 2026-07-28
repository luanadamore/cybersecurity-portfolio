# Luana D'Amore — Cybersecurity Portfolio

CS student at UZH (year 2), learning cybersecurity hands-on.

**Currently working through:** Linux CLI, networking, web security, and AppSec labs.

---

## Certifications

| Status | Course | Notes |
|--------|--------|-------|
| **In progress** | [Cisco Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity?courseLang=en-US) (NetAcad) | Free · ~6 hours |
| **In progress** | [Grundwissen Cybersecurity](https://www.linkedin.com/learning/paths/grundwissen-cybersecurity-bereitgestellt-von-microsoft-und-linkedin) (LinkedIn Learning) | Free path · ~6 hours · completion badge |
| **In progress** | [Microsoft Cybersicherheit Grundwissen](https://www.linkedin.com/learning/paths/microsoft-cybersicherheit-grundwissen-mit-fachzertifikat-bereitgestellt-von-microsoft-und-linkedin) (LinkedIn Learning) | Free path · ~3 hours · completion badge |


---

## Skills

| Area | Topics |
|------|--------|
| **Linux** | Command line, file permissions, bash scripting, SSH |
| **Networking** | TCP/IP, DNS, HTTP, Wireshark, Nmap |
| **Web Security** | Burp Suite, OWASP Top 10, SQLi, XSS, SSRF |
| **Blue Team** | Log analysis, SIEM, incident response, MITRE ATT&CK |
| **Scripting** | Python, Bash |

---

## Practice platforms

These are the sites I use to practice — profiles and labs linked where available:

| Platform | Link |
|----------|------|
| **TryHackMe** | https://tryhackme.com/p/luanadamore |
| **PortSwigger Web Security Academy** | https://portswigger.net/web-security |
| **OverTheWire (Bandit)** | https://overthewire.org/wargames/ |
| **CyberDefenders** | https://cyberdefenders.org |

---

## Flashcard collection

Importable Anki flashcards for cybersecurity learners — Linux, networking, AppSec, git, and more. I add new cards whenever I learn something worth remembering.

**Files:**
- [`flashcards.txt`](flashcards.txt) — import into [Anki] Flashcard Software
- [`flashcards-viewer.html`](flashcards-viewer.html) — open in any browser for a quick preview (no Anki needed)

### How to use (Anki)

1. Download or clone this repo (or copy `flashcards.txt`)
2. Open **Anki** → **File** → **Import**
3. Select `flashcards.txt` — settings auto-detect from the file header
4. For re-imports after new cards are added: choose **Preserve** existing notes (so your edits stay)
5. Study — filter by tags: `linux`, `networking`, `appsec`, `git`, `concepts`, etc.

### How to preview (browser)

Open `flashcards-viewer.html` in Chrome/Firefox. Click a card to flip. Use tag filters at the top.

---

## Tools

### Port Checker

A bash script that checks whether ports 22, 80, and 443 are open or closed on a given target.

**Location:** `port-checker.sh`

**Usage**
```bash
./port-checker.sh <target>
```

**Example**
```bash
./port-checker.sh google.com
```

**Output**
```
Target: google.com
-------------------
[OPEN]   Port 22 (SSH)
[CLOSED] Port 80 (HTTP)
[OPEN]   Port 443 (HTTPS)
```

**How it works**

Uses `/dev/tcp` — a Linux built-in that attempts a TCP connection to a host and port without any external tools. Exit code 0 = open, anything else = closed.

**Ports checked**

| Port | Service | Meaning |
|------|---------|---------|
| 22 | SSH | Remote shell access |
| 80 | HTTP | Web traffic (unencrypted) |
| 443 | HTTPS | Web traffic (encrypted) |

**What I learned**

- Bash can open TCP connections without Nmap — useful when you only have a shell
- Port state is inferred from whether the connection succeeds or fails
- SSH (22) is often filtered on public hosts; 443 is almost always open on web servers
- Good first portfolio script: small scope, clear output, easy to demo in an interview

---

## Reports

Work in progress — added as completed.

| Report | Description |
|--------|-------------|
| `reports/incident-report-01.md` | Blue team incident report with MITRE ATT&CK mapping |
| `reports/wireshark-analysis-01.md` | PCAP traffic analysis |
| `reports/web-vuln-sqli.md` | SQL injection vulnerability report |
| `reports/web-vuln-xss.md` | XSS vulnerability report |
| `reports/dvwa-pentest-report.md` | Full pentest report on DVWA (flagship) |

---

*Updated July 2026*
