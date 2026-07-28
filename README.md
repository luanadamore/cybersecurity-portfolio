# Luana D'Amore — Cybersecurity Portfolio

CS student at UZH (year 2), learning cybersecurity hands-on.

**Currently working through:** Linux CLI, networking, web security, and AppSec labs.

---

## Certifications


| Status          | Course                                                                                                                                                                                                  | Notes                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **In progress** | [Cisco Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity?courseLang=en-US) (NetAcad)                                                                         | Free · ~6 hours                         |
| **In progress** | [Grundwissen Cybersecurity](https://www.linkedin.com/learning/paths/grundwissen-cybersecurity-bereitgestellt-von-microsoft-und-linkedin) (LinkedIn Learning)                                            | Free path · ~6 hours · completion badge |
| **In progress** | [Microsoft Cybersicherheit Grundwissen](https://www.linkedin.com/learning/paths/microsoft-cybersicherheit-grundwissen-mit-fachzertifikat-bereitgestellt-von-microsoft-und-linkedin) (LinkedIn Learning) | Free path · ~3 hours · completion badge |


---

## Skills


| Area             | Topics                                              |
| ---------------- | --------------------------------------------------- |
| **Linux**        | Command line, file permissions, bash scripting, SSH |
| **Networking**   | TCP/IP, DNS, HTTP, Wireshark, Nmap                  |
| **Web Security** | Burp Suite, OWASP Top 10, SQLi, XSS, SSRF           |
| **Blue Team**    | Log analysis, SIEM, incident response, MITRE ATT&CK |
| **Scripting**    | Python, Bash                                        |


---

## Practice platforms

These are the sites I use to practice — profiles and labs linked where available:


| Platform                             | Link                                                                         |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| **TryHackMe**                        | [https://tryhackme.com/p/luanadamore](https://tryhackme.com/p/luanadamore)   |
| **PortSwigger Web Security Academy** | [https://portswigger.net/web-security](https://portswigger.net/web-security) |
| **OverTheWire (Bandit)**             | [https://overthewire.org/wargames/](https://overthewire.org/wargames/)       |
| **CyberDefenders**                   | [https://cyberdefenders.org](https://cyberdefenders.org)                     |


---

## Flashcard collection

Importable Anki flashcards for cybersecurity learners — Linux, networking, AppSec, git, and more. I add new cards whenever I learn something worth remembering.

**Files:**

- `[flashcards.txt](flashcards.txt)` — import into [Anki] Flashcard Software
- `[flashcards-viewer.html](flashcards-viewer.html)` — open in any browser for a quick preview (no Anki needed)

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


| Port | Service | Meaning                   |
| ---- | ------- | ------------------------- |
| 22   | SSH     | Remote shell access       |
| 80   | HTTP    | Web traffic (unencrypted) |
| 443  | HTTPS   | Web traffic (encrypted)   |


**What I learned**

- Port state is inferred from whether the connection succeeds or fails
- SSH (22) is often filtered on public hosts; 443 is almost always open on web servers

---

### HTTP Security Header Checker

A Python command-line tool that audits any website for five key HTTP security headers and prints a pass/fail result with explanations.

**Location:** `tools/header-checker/header_checker.py`

**Requirements:** Python 3 + `pip install requests`

**Usage**

```bash
python header_checker.py <url>
```

**Example**

```bash
python header_checker.py https://github.com
```

**Output**

```
Checking: https://github.com
==================================================
[PASS] Strict-Transport-Security
       max-age=31536000; includeSubdomains; preload

[PASS] Content-Security-Policy
       default-src 'none'; ...

[PASS] X-Frame-Options
       deny

[PASS] X-Content-Type-Options
       nosniff

[PASS] Referrer-Policy
       strict-origin-when-cross-origin

==================================================
Score: 5/5 headers present
```

**Headers checked**


| Header                      | Attack prevented                |
| --------------------------- | ------------------------------- |
| `Strict-Transport-Security` | HTTPS downgrade / SSL stripping |
| `Content-Security-Policy`   | XSS script injection            |
| `X-Frame-Options`           | Clickjacking                    |
| `X-Content-Type-Options`    | MIME sniffing                   |
| `Referrer-Policy`           | Sensitive URL leakage           |


**What is an HTTP header?**

When a browser visits a website, the server sends back two things: the **body** (HTML, images -> what you see) and **headers** (invisible metadata -> instructions to the browser). Headers are key: value pairs like `X-Frame-Options: DENY`. 

Security headers tell the browser to apply specific safety restrictions: block scripts, force HTTPS, prevent iframe embedding. The user never sees them, but the browser silently obeys. You can inspect them in Chrome/Firefox with **F12 → Network → click any request → Headers**.

**What I learned**

- HTTP response headers are invisible to users but control how browsers behave — a missing header can leave a site open to well-known attacks
- Even major organisations miss headers: Wikipedia scores 1/5, UZH (my own university) scores 2/5, and even PortSwigger (makers of Burp Suite) score 4/5
- Some sites actively block automated requests — UBS and Migros returned errors, which is itself a security control worth noting
- Risk is context-dependent: a 0/5 score on a volleyball club site is very different from a 0/5 on a banking site — the data exposed and the attacker motivation differ significantly
- Python's `requests` library makes it straightforward to inspect HTTP responses.
- Writing a report in a structured way and realistically assess the risks.

---

## Reports


| Report                                                             | Description                                                                                | Status   |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | -------- |
| `[reports/header-audit-report.md](reports/header-audit-report.md)` | HTTP security header audit of 7 real sites — consulting-style findings and risk assessment | **Done** |
| `reports/incident-report-01.md`                                    | Blue team incident report with MITRE ATT&CK mapping                                        | Planned  |
| `reports/wireshark-analysis-01.md`                                 | PCAP traffic analysis                                                                      | Planned  |
| `reports/web-vuln-sqli.md`                                         | SQL injection vulnerability report                                                         | Planned  |
| `reports/dvwa-pentest-report.md`                                   | Full pentest report on DVWA (flagship)                                                     | Planned  |


---

*Updated July 2026*