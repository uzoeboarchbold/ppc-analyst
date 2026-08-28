# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future automated runs go smoothly. Newest at top.

## 2026-08-28 — First run (2-day report)
- **Repo was empty** (only README). Created `reports/` folder and this file. No
  previous report existed, so the 2-day report had no baseline to compare
  against — Part C noted "first report, no prior baseline". Next 2-day run
  should compare against `reports/ppc-2day-latest.md`.
- **Amazon Ads API region:** credentials work against the **North America**
  endpoint `https://advertising-api.amazon.com`. The EU
  (`advertising-api-eu`) and FE (`advertising-api-fe`) hosts are **blocked by
  the egress proxy (403 CONNECT)** — do NOT retry those, they are policy
  denials. Stay on the NA host.
- **Transient 502 "policy unavailable":** the NA `/v2/profiles` call returned a
  502 on the first try, then 200 on retry. Treat 502 as transient — retry a
  few times with a short backoff before giving up.
- **AMZ_PROFILE_ID env var is WRONG.** It contains an *application* id
  (`amzn1.application.dd42...`), not a numeric Ads profile id. The
  `Amazon-Advertising-API-Scope` header needs a numeric profileId. Get the
  real ones from `/v2/profiles`. This account has 3 seller profiles:
    - **US = 26765323558215** (USD)  ← primary market, use this by default
    - CA = 2840235221595557 (CAD)
    - MX = 3892485344323414 (MXN)
  I defaulted to **US**. If the owner wants CA/MX or all three, update this note.
- **Auth:** refresh-token exchange at `https://api.amazon.com/auth/o2/token`
  works fine; access token lasts 3600s.
- **Reporting API:** use v3 async reports (`POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`).
  - Campaigns: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`,
    metric `topOfSearchImpressionShare` is available here.
  - Targeting/keywords: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
  - Sales/purchases columns are windowed: used `sales7d` / `purchases7d`.
  - Poll `GET /reporting/reports/{id}` until COMPLETED, then download the
    `url` (GZIP JSON).
- **Data reality:** account is nearly dormant. Aug 24–25 US totals were 180
  impressions, 3 clicks, $0.75 spend, 0 orders, $0 sales. Campaign names
  contain literal `|` characters — **escape them as `\|` in markdown tables**.
- **Delivery:** save to `reports/`, commit+push to branch
  `claude/great-hopper-g4ug7g`; upload to Google Drive folder "PPC Reports";
  email to uzoebo.archbold@gmail.com.
