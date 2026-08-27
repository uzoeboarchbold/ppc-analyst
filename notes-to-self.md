# Notes to Self — PPC Analyst

Running log of lessons so future runs work hands-off. Newest at top.

## 2026-08-27 — First run (2-day report)

**Credentials / profile**
- `AMZ_PROFILE_ID` env var is WRONG: it holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an application/client id, NOT a numeric advertising profile id. Do not pass it as scope.
- The real profiles under this account (seller "Uzoebo Archbold E-Commerce", seller id A1C2I8MOP52E35):
  - **US = 26765323558215 (USD)** ← the ACTIVE ad account (daily budget $40). USE THIS as the scope.
  - CA = 2840235221595557 (CAD), MX = 3892485344323414 (MXN) — no real budget, ignore unless told otherwise.
- Get access token from https://api.amazon.com/auth/o2/token with grant_type=refresh_token +
  AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN. Token good ~3600s. The refresh token env var keeps working.

**Endpoints / region**
- Only NA host `advertising-api.amazon.com` is reachable. EU/FE hosts return proxy 403 (CONNECT
  tunnel failed) — not a real error, just not needed (account is US).

**Reporting API v3 (async) gotchas**
- POST /reporting/reports with Content-Type `application/vnd.createasyncreportrequest.v3+json`,
  header `Amazon-Advertising-API-Scope: 26765323558215`.
- Column names: use `keyword` NOT `keywordText`. `topOfSearchImpressionShare` is valid on
  spCampaigns and spTargeting but NOT on spSearchTerm.
- Sales/purchases columns used: `purchases7d`, `sales7d` (7-day attribution). CTR, CPC, ACOS, ROAS
  are computed locally (not returned).
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). timeUnit SUMMARY, format GZIP_JSON.
- **425 "duplicate" error**: an identical report request within a short window is rejected with the
  existing reportId embedded in the detail string. Parse that UUID and poll it instead of failing.

**Account state note**
- Account is nearly dormant. 2-day window Aug 23–24 had only 115 impressions, 3 clicks, $0.75 spend,
  0 sales across 15 campaigns. If future numbers stay near zero, that's real, not a data bug.

**Delivery**
- Google Drive folder for uploads: "PPC Reports" (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Upload as
  `text/markdown` with `disableConversionToGoogleType=true`. NOTE: `update_file` only changes
  metadata (title/parent), not content — to fix content, trash the file and create a new one with
  the full `textContent` in ONE call (don't create a placeholder first).
- **EMAIL: not possible in this environment.** Only the Google-Drive and github MCP servers are
  connected — there is NO Gmail/email/SMTP tool. The requested email to uzoebo.archbold@gmail.com
  could not be sent. Report is delivered via the repo + Google Drive instead. To enable email,
  connect a Gmail (or email) connector to this session. Until then, skip the email step and say so.
