# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work better. Newest notes at top.

## Account / environment facts (verified 2026-11-12)
- **`AMZ_PROFILE_ID` env var is MISCONFIGURED.** It contains an *application ID*
  (`amzn1.application....`), NOT a numeric profile ID. Do **not** pass it as the
  `Amazon-Advertising-API-Scope` header — it will not work.
- Correct numeric profile IDs (seller account "Uzoebo Archbold E-Commerce",
  seller id A1C2I8MOP52E35), fetched from `GET /v2/profiles`:
  - **US** = `26765323558215` (USD, marketplace ATVPDKIKX0DER) ← **the active PPC account**
  - CA = `2840235221595557` (CAD) — 0 campaigns
  - MX = `3892485344323414` (MXN) — 0 campaigns
- **Always target the US profile `26765323558215`** until told otherwise. It holds all
  54 Sponsored Products campaigns (15 enabled). CA/MX have none.
- Only the **NA** API host works from this environment: `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the proxy (403). US is NA, so this is fine.

## How to pull data (works)
- Token refresh: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token,
  refresh_token, client_id, client_secret. Access token lasts 3600s.
- Reports: v3 async API. POST `/reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, adProduct
  SPONSORED_PRODUCTS, reportTypeId `spCampaigns` / `spTargeting` / `spSearchTerm`,
  timeUnit SUMMARY (or DAILY for trend), format GZIP_JSON. Poll `/reporting/reports/{id}`
  until status COMPLETED, then GET the presigned `url` (no auth header) and gunzip JSON.
- Valid v3 campaign columns used: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare. (topOfSearchImpressionShare is null
  when impressions = 0.)
- Compute CTR, CPC, ACOS, ROAS yourself from cost/clicks/sales to avoid field-name issues.

## Open issues / watch items
- **ADS NOT SERVING (2026-11-12 run):** zero impressions/clicks/spend/sales for the whole
  period Oct 27 – Nov 9, 2026, across all enabled campaigns. API is healthy — this is a real
  account state, not a query bug. Most likely cause: US profile shows
  `accountInfo.validPaymentMethod = false` → Amazon halts all delivery when billing fails.
  Owner must fix the payment method in Seller Central → Advertising/Billing. Until fixed,
  every report will show zeros. Re-check `validPaymentMethod` each run and flag if still false.

## Date window logic (2-day report)
- Data lags ~48h. Window = the 2 full calendar days ending 48h before run time.
  Run Thu 2026-11-12 23:10 UTC → 48h back = Tue 2026-11-10 → last full day = Nov 9 →
  cover **Nov 8 and Nov 9**. (Matches the example: run Sun 00:00 → cover Wed+Thu.)

## Reports / comparison
- Reports saved in `reports/`: `ppc-2day-latest.md` (overwrite) + `ppc-2day-YYYY-MM-DD.md` (dated).
- Compare each new 2-day report against the previous 2-day report. 2026-11-12 was the FIRST
  run → no prior report to compare against.
