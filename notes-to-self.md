# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Environment / credentials
- LWA token refresh works: POST `https://api.amazon.com/auth/o2/token`
  with `grant_type=refresh_token` + client id/secret + refresh token.
  Access token lasts 3600s.
- **`AMZ_PROFILE_ID` env var is INVALID.** It holds an *application* id
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a numeric
  Amazon Ads profile id. Do NOT pass it as the `Amazon-Advertising-API-Scope`.
  Instead call `GET /v2/profiles` and pick the right numeric profile.
- Region is **NA** (`https://advertising-api.amazon.com`). EU/FE endpoints are
  blocked by the outbound proxy (403) and are not needed anyway.
- Account has 3 profiles (seller "Uzoebo Archbold E-Commerce"):
  - US `26765323558215` (USD) — `validPaymentMethod:false`, dailyBudget 40.
  - CA `2840235221595557` (CAD).
  - MX `3892485344323414` (MXN).
  Determine the ACTIVE marketplace by pulling a campaign report per profile
  and seeing which has impressions/spend. (US had ZERO rows for 2026-09-06/07.)

## Reporting API (v3 async)
- POST `/reporting/reports` with Content-Type
  `application/vnd.createasyncreportrequest.v3+json`; body has
  `configuration` {adProduct SPONSORED_PRODUCTS, groupBy, columns,
  reportTypeId, timeUnit SUMMARY, format GZIP_JSON}. Poll
  `GET /reporting/reports/{id}` until status COMPLETED, then download the
  presigned `url` (no auth headers) and gunzip.
- **Invalid columns**: `acosClicks7d` and `roasClicks7d` are NOT allowed for
  spCampaigns. Only 14d variants exist (`acosClicks14d`, `roasClicks14d`).
  Simplest: request `cost`, `sales7d`, `purchases7d`, `impressions`, `clicks`
  and compute ACOS = cost/sales, ROAS = sales/cost, CTR = clicks/impr,
  CPC = cost/clicks yourself.
- reportTypeId per groupBy: spCampaigns (["campaign"]), spTargeting
  (["targeting"]), spSearchTerm (["searchTerm"]).
- `topOfSearchImpressionShare` is a valid spCampaigns column.

## Date window
- Data lags ~48h. 2-day report covers the 2 full calendar days ending 48h
  before run time. Run 2026-09-10 23:04 UTC → covered 2026-09-06 & 2026-09-07.

## Report history — IMPORTANT
- The git repo is cloned FRESH each run, so `reports/` starts EMPTY. Do NOT
  conclude "first run / no previous report" from an empty repo folder.
- The real archive of previous reports is the **Google Drive "PPC Reports"
  folder** (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). ALWAYS look there
  for the previous report of this type to compare against. Files are named like
  "PPC 2-Day Report — 30–31 Aug 2026". Read the latest one and pull its
  headline metrics for Part C.
- Previous 2-day report before this run: 30–31 Aug 2026 = 331 impressions,
  1 click, $0.25 spend, $0.00 sales, ROAS 0.00.

## Email delivery — UNRESOLVED (needs human)
- The task's Step 4 says email the report. The **Gmail connector is connected
  but NOT enabled in this chat session** (`enabledInChat:false`), so there is
  no send tool available and the email CANNOT be sent automatically. Every run
  so far has hit this. Save + Drive upload still work. To fix: enable the Gmail
  connector for this automated session's chat. Until then, note the miss at the
  top of each report and in the run summary.

## Delivery status trend
- Account has been barely serving for weeks and has produced $0 ad sales.
  On 2026-09-06/07 it served NOTHING at all (0 impressions across 15 US
  campaigns). US marketplace shows `validPaymentMethod:false` — most likely a
  billing/payment problem is now fully pausing delivery. Flag this loudly.
