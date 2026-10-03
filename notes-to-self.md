# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future runs are faster and more reliable.

## Account facts (confirmed 2026-10-03)
- The Amazon Ads account has **3 seller profiles** under "Uzoebo Archbold E-Commerce":
  - **US / USD — profileId `26765323558215`** → the ONLY active one (54 SP campaigns, 15 enabled). **Use this profile.**
  - CA / CAD — profileId `2840235221595557` → 0 campaigns (empty).
  - MX / MXN — profileId `3892485344323414` → 0 campaigns (empty).
- All profiles live in the **NA** region endpoint: `https://advertising-api.amazon.com`.
- Primary product advertised: ASIN **B0FXW3GW5F** (pet odor eliminator / cat deterrent spray) + a "Cat Tunnel Bed" product.

## CRITICAL config issue — AMZ_PROFILE_ID is wrong
- `AMZ_PROFILE_ID` env var contains an **application id** (`amzn1.application.…`), NOT a numeric profile id.
- It cannot be used as the API scope. Until it is fixed, hard-use US profile `26765323558215`.
- **Action for owner:** set `AMZ_PROFILE_ID=26765323558215` (US) in the environment.

## How to pull data (works)
- Token: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token + client id/secret. Works.
- Reporting API v3 async flow: POST `/reporting/reports` (Content-Type `application/vnd.createasyncreportrequest.v3+json`),
  poll GET `/reporting/reports/{id}` until `COMPLETED`, download the presigned `url` (gzip JSON, no auth header on the S3 url).
- Headers: `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope` (= numeric profileId), `Authorization: Bearer`.
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
- Attribution columns: `purchases7d`, `sales7d` (7-day window, standard for SP).
- `topOfSearchImpressionShare` is available on spCampaigns.
- GOTCHA: report date range **must be ≤ 31 days** (400 error otherwise).
- GOTCHA: `timeUnit=SUMMARY` **omits zero-activity rows** (returns `[]` when nothing served). Use `timeUnit=DAILY`
  if you need to confirm zero rows exist per campaign; management API `/sp/campaigns/list` confirms enabled campaigns.
- Proxy blocks the EU/FE ad endpoints (403 tunnel); NA endpoint works fine. Don't bother probing EU/FE.

## Date window logic (2-day report)
- Data lags ~48h. Window = the 2 full, finalized days ending 48h before the run.
- Practically: run day minus 4 and minus 3. (Run Sat 2026-10-03 → cover Sep 29 + Sep 30.)

## Observations / history
- 2026-10-03 run (window Sep 29–30): **ZERO delivery** — all 15 enabled campaigns had 0 impressions, 0 spend,
  0 sales, for the whole window AND all of September. Ads enabled but not serving. Likely cause: listing not in
  Buy Box / out of stock / suppressed, bids too low to win auctions, or a billing issue. Flagged to owner.
  This was the FIRST report of this type (no previous 2-day report to compare against).
