# Notes to self — PPC Analyst automated runs

Lessons carried between runs. Update this whenever something breaks or surprises you.

## Environment / credentials
- Amazon Ads API creds come from env: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
- **IMPORTANT — `AMZ_PROFILE_ID` is WRONG.** It contains an *application* ID
  (`amzn1.application....`), not a usable advertising profile ID. Do NOT pass it
  as `Amazon-Advertising-API-Scope`; the request will fail.
- Get a token from `https://api.amazon.com/auth/o2/token` (grant_type=refresh_token),
  then `GET /v2/profiles` to find the real profile IDs.
- Account = "Uzoebo Archbold E-Commerce", seller A1C2I8MOP52E35. Profiles:
  - **US = 26765323558215 (USD)** ← the active one, real $40 daily budget. USE THIS.
  - CA = 2840235221595557, MX = 3892485344323414 (both look inactive / default budgets).
- Region is **NA** (`advertising-api.amazon.com`). EU/FE endpoints are blocked by the proxy (403).

## Reporting API v3 (Sponsored Products)
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`. Poll `GET /reporting/reports/{id}`
  until `COMPLETED`, then download the `url` (GZIP JSON). Reports take ~20-60s.
- `spCampaigns` groupBy `campaign` does **NOT** accept `acosClicks7d` / `roasClicks7d`
  columns (400 error). Compute ACOS = cost/sales and ROAS = sales/cost yourself, or
  use `roasClicks14d`. `spTargeting`/`spSearchTerm` DO accept `acosClicks7d`/`roasClicks7d`.
- `topOfSearchImpressionShare` only comes back with `timeUnit: SUMMARY`.
- Working column sets used (all valid):
  - campaign: campaignName, campaignId, impressions, clicks, cost, costPerClick,
    clickThroughRate, purchases7d, sales7d, topOfSearchImpressionShare
  - targeting: campaignName, keyword, keywordType, matchType, targeting, impressions,
    clicks, cost, costPerClick, clickThroughRate, purchases7d, sales7d, acosClicks7d, roasClicks7d
  - searchTerm: campaignName, keyword, matchType, searchTerm, impressions, clicks, cost,
    purchases7d, sales7d, acosClicks7d, roasClicks7d

## Date window
- Data lags ~48h. 2-day report = the 2 full calendar days ending 48h before the run.
- e.g. run Sun 6 Sep 2026 23:04 UTC → window = Wed 2 Sep + Thu 3 Sep 2026.

## Account state observations (watch these trend over time)
- 2026-09-02/03: account was essentially dormant — 53 impressions total, 0 clicks,
  $0 spend, $0 sales across all 15 campaigns. 10 of 15 campaigns had 0 impressions.
  This is a "ads not showing" problem (bids too low / paused / no budget), not wasted
  spend. If future runs still show ~0 clicks, flag it — bids likely below market.

## Reports folder
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-[YYYY-MM-DD].md` (run date).
- Then upload same file to Google Drive folder "PPC Reports" and email to uzoebo.archbold@gmail.com.
- Google Drive folder "PPC Reports" id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with
  `create_file` (contentMimeType `text/markdown`, disableConversionToGoogleType true). Works.
- **EMAIL STEP BLOCKED (2026-09-06):** the Gmail connector IS connected at org level but is
  `enabledInChat: false` — its tools are NOT loaded in the automated session, so the report
  could not be emailed. Escape hatch for the user: enable the Gmail connector for this
  session/chat in connector settings so a future run can send the email. Until then, the
  report is delivered via git (reports folder) + Google Drive only. Table markdown: escape
  literal `|` in campaign names (two campaigns contain them) or the columns break.
