# Notes to Self — PPC Analyst (automated runs)

Lessons learned across runs so that future runs are smoother. Read this first.

## Amazon Ads API — environment & auth
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an application ARN
  (`amzn1.application.…`, 50 chars, non-numeric), NOT a numeric Ads profile id.
  Do not pass it as the `Amazon-Advertising-API-Scope` header — it returns
  `400 Invalid scope`.
- The OAuth creds (`AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`)
  ARE valid. Refresh token flow at `https://api.amazon.com/auth/o2/token` works.
- To get real profile ids: `GET /v2/profiles` **without** a scope header.
  Seller "Uzoebo Archbold E-Commerce" (account A1C2I8MOP52E35) has 3 profiles:
  - **US (USD): `26765323558215`  ← THE LIVE ONE. Use this.** 54 SP campaigns.
  - CA (CAD): `2840235221595557` — 0 campaigns (empty).
  - MX (MXN): `3892485344323414` — 0 campaigns (empty).
  All Sponsored Products activity is in the **US** marketplace. Currency = USD.
- Egress proxy only allows the **NA** endpoint
  (`https://advertising-api.amazon.com`). EU/FE endpoints return
  `403 Forbidden` at the tunnel — expected, account is US-only anyway.

## Reporting
- Use Ads API **v3 async reporting**: `POST /reporting/reports`, then poll
  `GET /reporting/reports/{id}` (~15s interval) until `COMPLETED`, download the
  gzip-json `url`. Content-Type header:
  `application/vnd.createasyncreportrequest.v3+json`.
- Report type ids: `spCampaigns` (groupBy `campaign`) and `spTargeting`
  (groupBy `targeting`). `timeUnit: SUMMARY`, `format: GZIP_JSON`.
- Sales/purchases column names use the `30d` attribution suffix
  (`sales30d`, `purchases30d`). `topOfSearchImpressionShare` is the ToS IS.
- CTR, CPC, ACOS, ROAS are not returned directly — compute them:
  CTR=clicks/impr, CPC=cost/clicks, ACOS=cost/sales, ROAS=sales/cost.

## Date window (data lags 48h)
- 2-day report covers the 2 full days ending ~48h before the run.
- Reports live in `reports/`: `ppc-2day-latest.md` (overwrite) +
  `ppc-2day-YYYY-MM-DD.md` (dated, by run date). Compare vs previous 2-day file.

## Delivery
- Save to repo, commit to branch `claude/great-hopper-uf50s6`.
- Upload to Google Drive folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Run history
- 2026-11-07: First run. No previous 2-day report existed, so no comparison
  possible this time (Part C notes baseline). Window: 2026-11-03 to 2026-11-04.
