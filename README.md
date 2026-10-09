# vuln-sast-repo

Intentionally vulnerable code for testing SAST and secret scanners. **Do not deploy.**
Every secret here is fake and non-functional; every vulnerability is deliberate.

## What is planted

| File | Vulnerability classes |
|------|----------------------|
| `app.py` | SQL injection, OS command injection, insecure deserialization (pickle), weak hash (MD5), hardcoded secrets |
| `server.js` | SQL injection, `eval` code injection, hardcoded API key, weak randomness |
| `upload.php` | Path traversal, unrestricted file include, reflected XSS |
| `config/.env` | Exposed AWS / Stripe / GitHub / Slack keys (all fake) |
| `config/settings.yaml` | Hardcoded DB password, private key blob (fake) |

All credentials use documented example formats so secret scanners match the pattern without any real key being exposed.
