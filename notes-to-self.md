# Notes to Self — PPC Analyst

Lessons learned across runs. Read this before every run and keep it updated.

## Credentials & account (IMPORTANT)
- `AMZ_PROFILE_ID` env var holds an **application id** (`amzn1.application....`), NOT a
  numeric Amazon Ads profile id. Do **not** pass it as the `Amazon-Advertising-API-Scope`.
- Get the real profile from `GET /v2/profiles` on the **NA** endpoint
  (`https://advertising-api.amazon.com`). The account (seller "Uzoebo Archbold E-Commerce",
  seller id A1C2I8MOP52E35) has 3 profiles: CA `2840235221595557`, MX `3892485344323414`,
  US `26765323558215`.
- **Use the US profile `26765323558215`** (USD, marketplace ATVPDKIKX0DER). It is the active
  advertising account (daily budget $40); CA/MX have no real budget set.
- EU/FE Ads endpoints are blocked by the outbound proxy (403). That's fine — this account is NA.
- Token exchange: `POST https://api.amazon.com/auth/o2/token` with refresh_token grant. Works.
  Access token lasts 3600s.

## Reporting API (v3) — what works
- Async flow: `POST /reporting/reports` (Content-Type & Accept
  `application/vnd.createasyncreportrequest.v3+json`) → poll `GET /reporting/reports/{id}`
  until status COMPLETED → download presigned `url` (GZIP JSON, no auth headers on the S3 GET).
- Config that works: `adProduct=SPONSORED_PRODUCTS`, `timeUnit=SUMMARY`, `format=GZIP_JSON`.
- Report types used: `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy `targeting`),
  `spSearchTerm` (groupBy `searchTerm`).
- Valid columns confirmed: campaignName, campaignId, campaignStatus, impressions,
  topOfSearchImpressionShare, clicks, clickThroughRate, cost, costPerClick,
  purchases14d, sales14d, acosClicks14d, roasClicks14d (and keyword/matchType/searchTerm/targeting).
- `topOfSearchImpressionShare` is only populated when there are impressions; it comes back
  `null` when impressions are 0.

## Account behaviour — expect near-zero volume
- This account is **barely serving**. Over the 14 days Aug 26 – Sep 8 2026 the WHOLE account
  produced only ~1,120 impressions, 5 clicks, $0.85 spend, 0 purchases, 0 sales.
- So an all-zero 2-day window is a **real result, not an error**. Do NOT treat zeros as a
  pull failure. When metrics are all zero, sanity-check with a wider (e.g. 14-day) pull to
  confirm the API is returning data, then report the zeros honestly.
- Likely cause of low delivery: campaigns are new / bids likely below the auction clearing
  price / very tight budgets. Worth flagging to the owner as "not delivering" rather than
  "wasted spend".

## Date window logic (2-day report)
- Data lags ~48h. End the window 48h before run time, then take the 2 full days ending at
  that boundary. Run Fri 2026-09-11 23:03 UTC → window = Mon 2026-09-07 and Tue 2026-09-08.

## Delivery
- Reports saved to `reports/` (ppc-2day-latest.md + dated copy), committed to branch.
- Also upload to Google Drive folder "PPC Reports" and email uzoebo.archbold@gmail.com.
