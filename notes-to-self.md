# PPC Analyst — Notes to Self

Running log of lessons so future runs go smoothly. Newest at top.

## 2026-06-22 (first run, 2-day report)

**Credentials / environment**
- `AMZ_PROFILE_ID` env var is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`
  — that is an **application/client ID, NOT a numeric profile ID**. It cannot be
  passed as `Amazon-Advertising-API-Scope`. Do not use it directly.
- The real numeric profiles (from `GET /v2/profiles` on the NA endpoint) are:
  - **US — 26765323558215** (USD, seller)  ← primary, used for this report
  - CA — 2840235221595557 (CAD, seller)
  - MX — 3892485344323414 (MXN, seller)
- Only the **NA** endpoint (`advertising-api.amazon.com`) is reachable. EU and FE
  endpoints return `403 Host not in allowlist` — they'd need to be added to the
  environment's network egress allowlist. Not needed unless we start advertising
  in EU/FE marketplaces.

**Auth flow that works**
- POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token,
  client_id, client_secret → access_token. Works fine.

**Reporting API (v3) recipe that works**
- POST `https://advertising-api.amazon.com/reporting/reports`, header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, plus
  Authorization, ClientId, and Scope=<numeric profile id>.
- reportTypeId `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy
  `targeting`), `spSearchTerm` (groupBy `searchTerm`). format GZIP_JSON,
  timeUnit SUMMARY (or DAILY for day-by-day).
- `topOfSearchImpressionShare` is a valid column on spCampaigns.
- Poll `GET /reporting/reports/{id}` until status COMPLETED, then download `url`
  (gzip JSON). Reports take ~30–90s; poll every ~10–15s. Budget >2 min total per
  report — the day-by-day probe over 3 profiles can exceed a 2-min shell timeout,
  so run reports one profile at a time or with a longer timeout.

**Delivery channels available in this environment**
- Google Drive MCP: available (used to upload the report).
- Email: **no email/Gmail tool is available** in this environment. Could not send
  the email to uzoebo.archbold@gmail.com. The report is committed to the repo and
  uploaded to Drive instead. If email is required, an email/Gmail MCP or an SMTP
  setup needs to be added to the environment.
- No PushNotification tool is available either.

**Account state observed (IMPORTANT)**
- US Sponsored Products delivery STOPPED after 2026-06-09. Daily breakdown:
  - 06-08: 1,180 impr, 9 clicks, $46.36 spend, 0 purchases, $0 sales
  - 06-09: 159 impr, 0 clicks, $0 spend
  - 06-10 → 06-19: zero impressions / zero spend (campaigns not serving)
- So the 2-day window (06-18, 06-19) has ZERO activity. This is real, not a data
  lag (06-08/06-09 finalised fine). Likely cause: budgets exhausted, campaigns
  paused, or a billing/account issue. Flag this prominently every run until it
  resolves.
- The one active day (06-08) spent $46.36 for 0 sales → 100% wasted spend.
