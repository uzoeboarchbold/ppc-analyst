# Notes to Self — PPC Analyst

Living memory for the automated PPC reporting runs. Read this first every run; add lessons at the end.

## Account / API facts (verified 2026-09-13)
- **AMZ_PROFILE_ID env var is WRONG.** It contains an *application* id
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a numeric profile id.
  Do NOT pass it as the Advertising-API-Scope. Instead hit `GET /v2/profiles` and
  pick the profile. The active advertising marketplace is **US**:
  - Profile ID: **26765323558215** (US, USD, seller "Uzoebo Archbold E-Commerce", daily budget $40).
  - Other profiles exist but are unused defaults: CA (2840235221595557) and MX (3892485344323414),
    both at the placeholder $9.99e8 budget.
- **Region = NA.** Use host `advertising-api.amazon.com`. The proxy blocks the EU
  (`-eu`) and FE (`-fe`) hosts with 403 — expected, this is a NA account, don't retry those.
- **LWA token refresh** works: POST https://api.amazon.com/auth/o2/token with grant_type=refresh_token.
- **CA bundle**: set `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt` for outbound HTTPS via the proxy.
- Report download URLs (S3) ARE reachable through the proxy — download works.

## Reporting API (v3) gotchas
- Endpoint: `POST /reporting/reports`, header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- **ACOS/ROAS are NOT valid 7d columns.** `acosClicks7d`/`roasClicks7d` -> 400.
  Only 14d variants exist (`roasClicks14d`). Simplest: request `cost`, `sales7d`,
  `purchases7d` and **compute ACOS = cost/sales, ROAS = sales/cost, CTR, CPC yourself.**
- Working campaign columns: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare.
- Working targeting columns (reportTypeId spTargeting, groupBy [targeting]):
  campaignName, keyword, keywordType, matchType, targeting, impressions, clicks, cost, purchases7d, sales7d.
- Working search-term columns (reportTypeId spSearchTerm, groupBy [searchTerm]):
  campaignName, keyword, matchType, searchTerm, targeting, impressions, clicks, cost, purchases7d, sales7d.
- Reports take ~40-90s to move PENDING -> PROCESSING -> COMPLETED. Poll every ~20s.
- If a window has no delivery, targeting/search-term reports come back with **0 rows** (normal, not an error).

## Delivery / connectors
- **Gmail connector is connected but toggled OFF for the chat session**
  (`enabledInChat: false`), so email CANNOT be sent from the run. Until it's enabled
  in this chat's connector settings, the emailing step will be skipped — rely on the
  push notification + the committed report + the Google Drive upload. Flag it in the report.
- **Google Drive connector is available** (enabledInChat: true). Upload the report there.
  Target folder: "PPC Reports" (create if missing).

## Business context / observations
- Single ASIN in play: **B0FXW3GW5F** (cat deterrent / pet odor / cat tunnel bed products).
- 15 SP campaigns exist (Auto, Exact, Phrase, isolated ranking campaigns, etc.).
- **MAJOR ISSUE seen 2026-09-13:** campaigns served **0 impressions every day from 2026-09-03
  onward** (verified through the 28-day window Aug 14 - Sep 10). Before that, impressions were
  tiny (tens-to-hundreds/day) with almost no clicks and **ZERO sales across the entire period**.
  Likely causes to watch: all campaigns paused, out of budget/billing issue, ASIN out of
  stock / buy-box lost / listing suppressed, or bids far below market. Each future run should
  check whether delivery has resumed.

## Report bookkeeping
- 2-day report window = the 2 full days ending 48h before run (48h data lag).
  Run 2026-09-13 -> window 2026-09-09 to 2026-09-10.
- Previous 2-day report: none before 2026-09-13 (this was the first run). Compare future runs
  against `reports/ppc-2day-latest.md`.
