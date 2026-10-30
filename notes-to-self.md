# Notes to self — PPC Analyst (automated runs)

Lessons learned, so future runs are faster and more accurate. Append new lessons; don't delete old ones unless proven wrong.

## Accounts / credentials
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** As of 2026-10-30 it is a 50-character string; real Amazon Ads profile IDs are 14–16 digits and it matched none of the account's profiles. Until it's fixed, use the **US seller profile** directly: **`26765323558215`** (countryCode US, USD).
- The login has 3 profiles, all "Uzoebo Archbold E-Co": US `26765323558215` (USD, **active — 54 SP campaigns**), CA `2840235221595557` (CAD, 0 campaigns), MX `3892485344323414` (MXN, 0 campaigns). Only US matters right now.
- Token exchange works fine: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token + client_id + client_secret + refresh_token. Access token lasts 3600s. Refresh each run.

## Network / endpoints
- **Only North America endpoint is reachable:** `https://advertising-api.amazon.com`. The EU (`-eu`) and FE (`-fe`) endpoints are **blocked by the environment network policy** (403 on CONNECT via the proxy). Don't waste time retrying them. Fine for now since all activity is US.

## Reporting API v3 (what works)
- Flow: POST `/reporting/reports` (Content-Type `application/vnd.createasyncreportrequest.v3+json`) → poll GET `/reporting/reports/{id}` until status COMPLETED → download `url` (GZIP_JSON, gzip-decompress → JSON array). Reports finish in ~15–30s.
- Headers: `Authorization: Bearer <tok>`, `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope: <profileId>`.
- **Campaign report** = reportTypeId `spCampaigns`, groupBy `["campaign"]`, timeUnit `SUMMARY`.
  - **Valid columns include:** campaignId, campaignName, impressions, clicks, cost, purchases7d, sales7d, topOfSearchImpressionShare, clickThroughRate, costPerClick.
  - **INVALID for spCampaigns:** `acosClicks7d`, `roasClicks7d` (API rejects with 400). **Compute ACOS = cost/sales7d, ROAS = sales7d/cost yourself.** (These cols ARE valid on spTargeting though.)
- **Keyword/target report** = reportTypeId `spTargeting`, groupBy `["targeting"]`. Useful columns: campaignName, keyword, keywordType, targeting, matchType, impressions, clicks, cost, purchases7d, sales7d, clickThroughRate, costPerClick, acosClicks7d, roasClicks7d.
- Campaign list (to get names/budgets/states): POST `/sp/campaigns/list` with header `Content-Type: application/vnd.spCampaign.v3+json`; body `{"maxResults":100,"stateFilter":{"include":["ENABLED"]}}`.

## Date window (2-day report)
- Data lags ~48h. Cover the 2 full days ending 48h before run time (UTC). Run 2026-10-30 23:11 → covered **Mon 26 + Tue 27 Oct 2026**. State exact dates at top of report.

## Delivery / email
- **No email tool is available in this environment** (only Google-Drive and github MCP servers; no Gmail/SMTP). I cannot send the email to uzoebo.archbold@gmail.com myself. For now: save to repo + upload to Google Drive 'PPC Reports' folder, and note in the report that email delivery needs a mail connector to be added. If an email/Gmail connector appears later, wire it in.
- Google Drive: use `mcp__Google-Drive__create_file` with `parentId` = the 'PPC Reports' folder id (find/create via `search_files`). Upload as text/markdown.

## Standing finding to watch
- **2026-10-30:** 15 enabled US SP campaigns (Cat Deterrent Spray / Pet Odor Eliminator, ASIN **B0FXW3GW5F**, + a Cat Tunnel Bed) but **ZERO impressions/spend all of October**. Budgets mostly $1.50/day. Likely bids too low and/or listing not eligible. If this is still zero next run, keep flagging it — it's the #1 issue.

## File outputs
- `reports/ppc-2day-latest.md` (overwrite each run) + `reports/ppc-2day-YYYY-MM-DD.md` (dated copy). Commit both. Find previous report of this type in `reports/` to compare against.
