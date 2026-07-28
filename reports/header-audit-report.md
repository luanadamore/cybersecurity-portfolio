# HTTP Security Header Audit Report

**Author:** Luana D'Amore  
**Date:** 2026-07-28  
**Tool:** `tools/header-checker/header_checker.py` (Python, custom-built)  
**Method:** Passive HTTP header inspection — read-only GET requests, no exploitation

---

## Executive Summary

Seven public websites were audited for the presence of five HTTP security response headers.

Security headers are server-side controls that instruct browsers how to behave safely. They mitigate common web attacks including XSS, clickjacking, and HTTPS downgrade attacks at zero implementation cost.

**Key finding:** Only one of seven sites (GitHub) achieved a perfect score. The remaining six sites had between one and five headers missing. Notably, both a local volleyball club (volebo.ch) and the national Swiss volleyball federation (volleyball.ch) scored 0/5, confirming this is a systemic issue in managed sports platforms rather than individual oversight. Content-Security-Policy was the most commonly absent header (5/7 sites), followed by Referrer-Policy (4/7 sites).

---

## Headers Checked


| Header                             | Attack Mitigated                                       |
| ---------------------------------- | ------------------------------------------------------ |
| `Strict-Transport-Security` (HSTS) | HTTPS downgrade / SSL stripping attacks                |
| `Content-Security-Policy` (CSP)    | Cross-Site Scripting (XSS), malicious script injection |
| `X-Frame-Options`                  | Clickjacking (loading site in invisible iframe)        |
| `X-Content-Type-Options`           | MIME sniffing attacks                                  |
| `Referrer-Policy`                  | Sensitive URL leakage to third-party sites             |


---

## Findings

### 1. volebo.ch (my own Volleyball Club, created with ClubDesk)

**Score: 0 / 5** — Critical


| Header                    | Status  | Risk                                                         |
| ------------------------- | ------- | ------------------------------------------------------------ |
| Strict-Transport-Security | MISSING | Users can be downgraded to HTTP by network attackers         |
| Content-Security-Policy   | MISSING | No XSS protection — injected scripts would execute freely    |
| X-Frame-Options           | MISSING | Site can be embedded in an iframe for clickjacking           |
| X-Content-Type-Options    | MISSING | Uploaded files could be MIME-sniffed and executed as scripts |
| Referrer-Policy           | MISSING | URLs including any parameters sent in full to third parties  |


**Comment:** This site was built using ClubDesk, a Swiss website builder designed for sports clubs. Like most managed website platforms, ClubDesk gives clubs very limited control over server configuration. There is no built-in option to add custom HTTP response headers. 

I looked into whether this could be changed within ClubDesk and concluded it is not possible without switching to a self-hosted solution. This is a known limitation of managed club site builders and is not unique to volebo.ch. 

---

### 2. volleyball.ch (Swiss Volleyball Federation)

**Score: 0 / 5** — Critical


| Header                    | Status  | Risk                                                 |
| ------------------------- | ------- | ---------------------------------------------------- |
| Strict-Transport-Security | MISSING | Users can be downgraded to HTTP by network attackers |
| Content-Security-Policy   | MISSING | No XSS protection                                    |
| X-Frame-Options           | MISSING | Site can be embedded in an iframe for clickjacking   |
| X-Content-Type-Options    | MISSING | MIME sniffing risk                                   |
| Referrer-Policy           | MISSING | URL leakage to third parties                         |


**Comment:** The national Swiss volleyball federation scores 0/5 — the same result as volebo.ch. This is a useful comparison: even the official governing body for the sport in Switzerland has the same header configuration as a small local club. This confirms that the issue is not specific to volebo.ch but is typical across Swiss sports organisations at all levels. 

---

### 3. github.com

**Score: 5 / 5** — Excellent


| Header                    | Status | Value                                                       |
| ------------------------- | ------ | ----------------------------------------------------------- |
| Strict-Transport-Security | PASS   | `max-age=31536000; includeSubdomains; preload`              |
| Content-Security-Policy   | PASS   | Comprehensive allowlist (all sources explicitly listed)     |
| X-Frame-Options           | PASS   | `deny`                                                      |
| X-Content-Type-Options    | PASS   | `nosniff`                                                   |
| Referrer-Policy           | PASS   | `origin-when-cross-origin, strict-origin-when-cross-origin` |


**Comment:** GitHub achieves a perfect score and serves as the benchmark for this audit. Their CSP policy is extensive, explicitly listing every permitted source for scripts, images, fonts, and media. `X-Frame-Options: deny` is the strictest possible setting. Used as comparison baseline.

---

### 4. uzh.ch (University of Zurich)

**Score: 2 / 5** — Weak


| Header                    | Status  | Value / Risk                                   |
| ------------------------- | ------- | ---------------------------------------------- |
| Strict-Transport-Security | MISSING | HTTPS enforcement missing at HTTP header level |
| Content-Security-Policy   | MISSING | No XSS mitigation via headers                  |
| X-Frame-Options           | PASS    | `SAMEORIGIN`                                   |
| X-Content-Type-Options    | PASS    | `nosniff`                                      |
| Referrer-Policy           | MISSING | URL referrer leakage uncontrolled              |


**Comment:** My own university scores below average, which I found surprising. Two headers are in place, but the most important ones — HSTS and CSP — are missing. HSTS matters especially here because UZH students and staff regularly connect on university WiFi. Without it, the very first HTTP request (before the server redirects to HTTPS) is sent in plain text and could be intercepted by someone on the same network. That is a realistic attack scenario in a university environment with hundreds of users on shared WiFi. The missing CSP is also a concern for a site that handles student and staff login and personal data.

---

### 5. srf.ch

**Score: 4 / 5** — Good


| Header                    | Status  | Value / Risk                                                     |
| ------------------------- | ------- | ---------------------------------------------------------------- |
| Strict-Transport-Security | PASS    | `max-age=2592000; includeSubDomains; preload`                    |
| Content-Security-Policy   | MISSING | XSS risk — likely complex to implement due to third-party embeds |
| X-Frame-Options           | PASS    | `DENY`                                                           |
| X-Content-Type-Options    | PASS    | `nosniff`                                                        |
| Referrer-Policy           | PASS    | `no-referrer-when-downgrade`                                     |


**Comment:** SRF performs well overall. The missing CSP is common on media sites due to the complexity of allowlisting third-party video players, ad networks, and analytics. The `Referrer-Policy` value of `no-referrer-when-downgrade` is acceptable but not the strictest — `strict-origin-when-cross-origin` would be preferred.

---

### 6. wikipedia.org

**Score: 1 / 5** — Weak


| Header                    | Status  | Value / Risk                                    |
| ------------------------- | ------- | ----------------------------------------------- |
| Strict-Transport-Security | PASS    | `max-age=106384710; includeSubDomains; preload` |
| Content-Security-Policy   | MISSING | No XSS header protection                        |
| X-Frame-Options           | MISSING | Embeddable in iframes                           |
| X-Content-Type-Options    | MISSING | MIME sniffing risk                              |
| Referrer-Policy           | MISSING | Referrer leakage                                |


**Comment:** Wikipedia has an exceptionally long HSTS `max-age` (over 3 years) indicating mature HTTPS enforcement, but scores poorly on all other headers. This may reflect a deliberate policy decision — Wikipedia encourages embedding and open content reuse — rather than an oversight.

---

### 7. portswigger.net (PortSwigger / Burp Suite)

**Score: 4 / 5** — Good


| Header                    | Status  | Value / Risk                                 |
| ------------------------- | ------- | -------------------------------------------- |
| Strict-Transport-Security | PASS    | `max-age=31536000; preload`                  |
| Content-Security-Policy   | PASS    | Detailed nonce-based CSP with strict-dynamic |
| X-Frame-Options           | PASS    | `SAMEORIGIN`                                 |
| X-Content-Type-Options    | PASS    | `nosniff`                                    |
| Referrer-Policy           | MISSING | Referrer leakage uncontrolled                |


**Comment:** PortSwigger makes Burp Suite, the industry-standard tool for web security testing — so finding a missing header on their own site is interesting.

They score 4/5 overall, which is strong. Their CSP uses a nonce-based `strict-dynamic` approach: a nonce is a one-time random code generated per page load that only allows scripts with a matching code to run, preventing any injected script from executing. 

`strict-dynamic` extends this trust to scripts those approved scripts load in turn. It is one of the most effective and modern ways to implement CSP. The only missing header is `Referrer-Policy`, which is a minor oversight. Adding one line of server config would bring them to 5/5.

---

## Summary Table


| Site            | HSTS | CSP  | X-Frame | X-Content-Type | Referrer | Score   |
| --------------- | ---- | ---- | ------- | -------------- | -------- | ------- |
| github.com      | PASS | PASS | PASS    | PASS           | PASS     | **5/5** |
| srf.ch          | PASS | FAIL | PASS    | PASS           | PASS     | **4/5** |
| portswigger.net | PASS | PASS | PASS    | PASS           | FAIL     | **4/5** |
| uzh.ch          | FAIL | FAIL | PASS    | PASS           | FAIL     | **2/5** |
| wikipedia.org   | PASS | FAIL | FAIL    | FAIL           | FAIL     | **1/5** |
| volebo.ch       | FAIL | FAIL | FAIL    | FAIL           | FAIL     | **0/5** |


---

## Key Observations

1. **CSP is the hardest header to get right** — only 2/6 sites have it. It requires explicitly listing every permitted resource origin, which is complex for sites with third-party content. This explains why it's absent even on sites with good overall scores.
2. **HSTS is widely adopted** — 4/6 sites have it. It is the simplest header to add and has the most immediate security benefit. Sites still missing it (volebo.ch, uzh.ch) should treat this as a priority.
3. **Referrer-Policy is underused** — only 2/6 sites have it despite being trivial to add. A single line of server configuration eliminates referrer leakage.
4. **Even security vendors are imperfect** — PortSwigger's missing Referrer-Policy shows that 100% compliance is rare in practice. This reinforces the value of regular security header audits.
5. **Some sites actively block automated requests** — UBS and Migros returned 403/connection reset errors, which is itself a security control. This tool is not suitable for sites with bot protection; manual browser inspection or tools like [securityheaders.com](https://securityheaders.com) would be needed.

---

## Recommendations

### For volebo.ch

Since the site is built on ClubDesk, server configuration cannot be changed by the club administrator. The remediation steps below are what *would* be applied if the site were self-hosted, and are provided for reference:

```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
```

CSP would require additional testing before enabling to avoid breaking site content:

```apache
Header always set Content-Security-Policy "default-src 'self'"
```

**Realistic risk assessment for volebo.ch:**

Since the headers cannot be changed, it is worth considering how serious the actual risk is in practice.


| Attack           | Likelihood | Impact | Notes                                                                                                                                     |
| ---------------- | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| HTTPS downgrade  | Low        | Medium | Requires attacker on same network as a visitor; more realistic on public WiFi than at home                                                |
| Clickjacking     | Very low   | Low    | An attacker would need a reason to target a local volleyball club specifically; the site contains no financial or sensitive personal data |
| XSS injection    | Very low   | Low    | Only exploitable if an attacker can inject content into the site, which requires a separate vulnerability first                           |
| MIME sniffing    | Very low   | Low    | Only relevant if users upload files to the site; which is not possible on volebo.ch                                                       |
| Referrer leakage | Low        | Low    | URLs from a volleyball club site are unlikely to contain sensitive parameters                                                             |


**Conclusion:** The missing headers on volebo.ch are a real security gap, but the practical risk is low given the nature of the site — it is a public information site for a local sports club with no login, no payments, and no sensitive user data. The risk is not zero, but it is not the same as the same gaps on a banking or healthcare site. The right action is to flag this to ClubDesk as a platform-level improvement request, or to consider migrating to a self-hosted solution if the club's security posture becomes a priority in the future.

### For [uzh.ch](http://uzh.ch)

Priority: add HSTS and Referrer-Policy — both are low-risk, one-line additions that significantly improve the security posture of an authentication-handling site.

### General recommendation

All sites should aim for at minimum:

- HSTS with `max-age` ≥ 1 year and `includeSubDomains`
- `X-Frame-Options: SAMEORIGIN` or CSP `frame-ancestors`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`

---

## Tool

This audit was performed using a custom Python script built as a portfolio project:

**Repository:** [github.com/luanadamore/cybersecurity-portfolio](https://github.com/luanadamore/cybersecurity-portfolio)  
**Script:** `tools/header-checker/header_checker.py`  
**Usage:** `python header_checker.py <url>`  
**Dependencies:** `requests` (pip install requests)