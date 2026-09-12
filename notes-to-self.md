# Notes to Self — PPC Analyst

Running notes so future automated runs go smoothly. Newest lessons at the top.

## Run log
- **2026-09-12 (2-day, covers Sep 8–9):** Whole US account served NOTHING in
  the window — 0 impressions/clicks/spend/sales across all 15 ENABLED SP
  campaigns. 14-day context (Aug27–Sep9): only ~1,020 impr, 4 clicks, $0.60
  spend, $0 sales. Root cause almost certainly **US profile
  `validPaymentMethod = false`** (billing blocks delivery). CA & MX have no SP
  campaigns. First run of this report type, so no prior 2-day report to compare.
  → Future runs: if totals are all zero again, check whether billing was fixed;
  don't treat zero as an API failure — verify with a wider window first (that's
  how I confirmed it's real, not a bug).

## Environment / credentials
- Credentials live in env vars: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`,
  `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
- **`AMZ_PROFILE_ID` is misconfigured.** It holds an *application* id
  (`amzn1.application.…`), NOT a numeric Amazon Ads profile id. Do not use it
  as the `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` and
  pick the profile you need.
- Real profiles on this account (seller "Uzoebo Archbold E-Commerce"):
  - US (USD): `26765323558215`  ← primary FBA marketplace, main reporting target
  - CA (CAD): `2840235221595557`
  - MX (MXN): `3892485344323414`
- Token refresh: POST `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token. Access token lasts 3600s. Works fine.
- Region endpoint: **NA = `https://advertising-api.amazon.com`** works. EU/FE
  hosts are blocked by the proxy (403) — don't bother, this account is NA.
- Outbound HTTPS goes through `$HTTPS_PROXY`; use CA bundle
  `/root/.ccr/ca-bundle.crt` in Python (`ssl.create_default_context(cafile=...)`).

## Reporting API (v3) gotchas
- Endpoint: POST `/reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`. Async:
  poll `GET /reporting/reports/{id}` until status COMPLETED, then download the
  gzip-JSON from the returned `url`.
- **Invalid columns:** `acosClicks7d` / `roasClicks7d` are NOT allowed for
  `spCampaigns`. Only the 14d variants exist. Simplest fix: request `cost`,
  `sales7d`, `purchases7d` and **compute ACOS = cost/sales7d and
  ROAS = sales7d/cost yourself.** That keeps 7-day attribution consistent.
- Useful spCampaigns columns: impressions, clicks, cost, purchases7d, sales7d,
  campaignName, campaignId, clickThroughRate, costPerClick,
  topOfSearchImpressionShare, campaignStatus.
- `topOfSearchImpressionShare` / `clickThroughRate` come back `null` when there
  are zero impressions.

## Date window
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
- Compute in UTC: cutoff = now-48h; end_day = cutoff.date()-1; start_day = end_day-1.

## Reports / delivery
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated `ppc-2day-YYYY-MM-DD.md`.
- Upload to Google Drive folder "PPC Reports"; email to uzoebo.archbold@gmail.com.
- Compare each 2-day report against the previous 2-day report in `reports/`.
- **Google Drive works.** Folder "PPC Reports" id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with `create_file` (parentId=that, contentMimeType=text/markdown,
  disableConversionToGoogleType=true).
- **EMAIL CANNOT BE SENT in this environment.** The Gmail connector is
  connected at org level but `enabledInChat = false`, so no gmail send/draft
  tool is loaded, and an automated run can't toggle it on. Delivery this run =
  repo commit + Drive upload only. To enable email: in claude.ai, enable the
  Gmail connector's tools for this chat/session (connector settings), or attach
  an email-capable tool. Until then, surface the report via PushNotification.
