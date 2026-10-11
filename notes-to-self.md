# Notes to self — PPC Analyst

Running log of lessons so future automated runs work better. Newest notes at top.

## 2026-10-11 — First run (2-day report)

- **Repo started empty** (just README.md). Created `reports/` folder and this file on first run.
- **Environment / API setup that works:**
  - `python3` is 3.11 at `/usr/local/bin/python3`. `requests` is NOT pre-installed — install with
    `python3 -m pip install requests` (plain `pip` targets a different 3.13 and won't be importable).
  - Set `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt` so HTTPS through the agent proxy verifies.
  - OAuth token refresh works: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token,
    refresh_token, client_id, client_secret. Returns a 1-hour access token. **Confirmed working.**
  - **Only the NA Ads endpoint is reachable:** `https://advertising-api.amazon.com`.
    The EU (`-eu`) and FE (`-fe`) hosts are BLOCKED by org egress policy (proxy 403). Don't retry them.
- **IMPORTANT — `AMZ_PROFILE_ID` is MISCONFIGURED.** It contains an LWA *application* id
  (`amzn1.application.…`), NOT a numeric advertising profile id. So it cannot be used directly as the
  Amazon-Advertising-API-Scope header.
  - The account has 3 NA seller profiles (all "Uzoebo Archbold E-Commerce"):
    - **US / USD: `26765323558215`**  (treating this as the primary marketplace)
    - CA / CAD: `2840235221595557`
    - MX / MXN: `3892485344323414`
  - **Workaround used:** call `GET /v2/profiles`, then select the **US (USD)** seller profile as the
    primary for reporting. Flagged this at the top of the report.
  - **Fix for a human:** correct the `AMZ_PROFILE_ID` env var to the numeric profile id of the intended
    marketplace (likely `26765323558215` for US). Until then, runs auto-select US.
- **Date window logic (2-day):** cover the 2 full days ending 48h before run time. Run Sun 2026-10-11
  → window = 2026-10-07 (Wed) and 2026-10-08 (Thu).
- Reporting: Amazon Ads API v3 async reports — POST `/reporting/reports`, poll `GET /reporting/reports/{id}`,
  download the GZIP_JSON url. Use `SPONSORED_PRODUCTS`, 7-day attribution columns (purchases7d/sales7d).
  Compute CTR/CPC/ACOS/ROAS myself where not returned.
- Previous report of this type: NONE yet (this is the first 2-day report). No comparison possible this run.
