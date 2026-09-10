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

## Report history
- Reports live in `reports/`. Latest of this type: `ppc-2day-latest.md`.
  (First run: no previous 2-day report to compare against.)
