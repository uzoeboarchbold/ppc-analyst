# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each run gets smoother. Newest lessons at top.

## Account / API facts (confirmed 2026-08-04)
- **AMZ_PROFILE_ID env var is WRONG.** It holds an *application* ID
  (`amzn1.application.dd42...`), NOT a numeric Ads profile ID. Do not use it
  as the `Amazon-Advertising-API-Scope` header — it will fail.
- **Real profiles** (from `GET /v2/profiles` on the NA endpoint):
  - **US = `26765323558215`** (USD, $40/day budget) → the ACTIVE account. Use this.
  - CA = `2840235221595557`, MX = `3892485344323414` → exist but no spend/activity.
    Still worth a quick check each run in case they switch on.
  - All under seller "Uzoebo Archbold E-Commerce" (seller id A1C2I8MOP52E35).
- **Endpoints:** only NA (`advertising-api.amazon.com`) is reachable. EU/FE
  hosts return proxy 403 (blocked) — fine, account is North America only.
- **Auth:** refresh-token flow at `https://api.amazon.com/auth/o2/token` works.
  Access token lasts 1h. Refresh + all 4 AMZ_* secrets are present and valid
  (client id `amzn1.ap...`, refresh `Atzr|...`).

## Reporting API (v3) recipe that works
- POST `/reporting/reports` (async). Content-Type & Accept:
  `application/vnd.createasyncreportrequest.v3+json`.
- Body: `configuration.adProduct=SPONSORED_PRODUCTS`, `timeUnit=SUMMARY`,
  `format=GZIP_JSON`, plus `reportTypeId`, `groupBy`, `columns`, `startDate`,
  `endDate`.
- **Campaign table:** `reportTypeId=spCampaigns`, `groupBy=["campaign"]`,
  columns incl. `campaignName, impressions, clicks, cost, purchases7d,
  sales7d, topOfSearchImpressionShare`.
- **Search terms:** `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`,
  columns incl. `searchTerm, keyword, matchType, impressions, clicks, cost,
  purchases7d, sales7d`.
- Poll `GET /reporting/reports/{id}` until `status=COMPLETED`, then GET the
  signed `url` and gunzip the JSON. Report gen takes ~1-4 min; poll every 8s.
- Conversions are 7-day attribution (`purchases7d`/`sales7d`).
- Working helper script kept in scratchpad as `pull.py` — reuse its shape.

## Date window (data lags 48h)
- 2-day report = the 2 full, finalised days ending 48h before run time.
  Verified: run Tue 2026-08-04 23:04 UTC → covered Fri 07-31 + Sat 08-01.

## Delivery
- Google Drive connector: connected + enabled in chat. Upload report to the
  **"PPC Reports"** folder (create it if missing).
- **Gmail connector exists but is NOT enabled in this chat** (`enabledInChat:false`).
  Emailing may fail until it's toggled on for the session. If email can't be
  sent, still save + commit + Drive-upload, and note the email gap in the report.
- Reports live in `reports/`: overwrite `ppc-2day-latest.md` + dated copy
  `ppc-2day-[YYYY-MM-DD].md` (date = run date). Commit both.
- Previous-report comparison: read `ppc-2day-latest.md` BEFORE overwriting it.

## Account observations
- 2026-08-04: account is barely active. Whole 2-day window = $0.98 spend,
  1 click, 0 sales across 11 SP campaigns. Most campaigns get near-zero
  impressions. Looks newly launched / just ramping. Don't over-optimise on
  1-click samples.
