# Notes to Self — PPC Analyst

Running memory of lessons learned so future runs are faster and more accurate.

## Environment / API
- **Region is NA.** Endpoint: `https://advertising-api.amazon.com`. The proxy blocks
  the EU/FE ads endpoints (403), so don't bother probing them.
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an *application* id
  (`amzn1.application....`), NOT a numeric Ads profile id. Do not pass it as the
  `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` and pick the profile.
  Three seller profiles exist under "Uzoebo Archbold E-Commerce":
  - US  = `26765323558215`  (this is the one we use — primary FBA market)
  - CA  = `2840235221595557`
  - MX  = `3892485344323414`
  If the owner ever wants CA/MX too, pull those profiles separately.
  *(Flagged in every report until the env var is fixed to the numeric US profile id.)*
- Token refresh: `POST https://api.amazon.com/auth/o2/token` with the 4 creds. Works fine.
- Reporting API v3: `POST /reporting/reports` (header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`), poll
  `GET /reporting/reports/{id}` until `COMPLETED`, download the presigned `url`
  (gzip-json). Reports usually finish in ~60s. Presigned S3 download works through
  the proxy.
- Useful columns (spCampaigns): campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare. CTR/CPC/ACOS/ROAS are NOT columns —
  compute them. Using 7-day attribution (purchases7d/sales7d) as the standard.
- Campaign state/budget: `POST /sp/campaigns/list`
  (header `application/vnd.spCampaign.v3+json`).

## Account observations
- **2026-09-17 run (2-day report, window Sep 13–14):** Account is DARK. Zero
  impressions/clicks/spend/sales on ALL campaigns since **2026-09-03**. Before that,
  Aug traffic was tiny (tens–hundreds of impressions/day, 0–2 clicks, sub-$1 spend,
  ZERO purchases the whole month). 15 campaigns are ENABLED with $1.50–$2.50 daily
  budgets but serving nothing. Enabled-but-zero-impressions across the whole account
  starting on one date = almost certainly an account-level cause: billing/payment
  failure, the advertised ASIN going out of stock / listing suppressed, or bids below
  the auction floor. Owner needs to check Seller Central billing + inventory + listing
  health. Watch whether serving resumes.
- Search-term report returns 0 rows (no clicks/impressions to attribute in the window),
  so no exact-match candidates or negatives can be suggested until traffic resumes.

## Reports
- First 2-day report was 2026-09-17 (this is the baseline; no prior 2-day report to
  compare against). Next run: compare against `ppc-2day-latest.md`.
