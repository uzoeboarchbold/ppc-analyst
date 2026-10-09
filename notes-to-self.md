# Notes to Self — PPC Analyst

Running notes so future automated runs work better. Read this first, apply the lessons, and append new ones.

## Environment / setup
- **Working repo:** `/home/user/ppc-analyst`. Reports go in `reports/`.
- **Report naming:** `ppc-2day-latest.md` (overwrite) + dated `ppc-2day-YYYY-MM-DD.md`.
- Equivalent patterns expected for other cadences (7day, 30day) when those run.

## Amazon Ads API — what works
- Auth: LWA token endpoint `https://api.amazon.com/auth/o2/token`, grant_type=refresh_token
  with `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`. Works.
- **Region is NA**: `https://advertising-api.amazon.com`. EU/FE endpoints are not reachable
  for these creds (connection fails) — don't waste time probing them.
- Reporting API v3: `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`. Async — poll
  `GET /reporting/reports/{id}` until status `COMPLETED`, then download the presigned
  `url` (GZIP_JSON, no auth headers on the S3 download).
- Useful report types: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). `timeUnit: SUMMARY` for a window total.
- `topOfSearchImpressionShare` is available on the `spCampaigns` report.

## KNOWN ISSUE — AMZ_PROFILE_ID is misconfigured (IMPORTANT)
- `AMZ_PROFILE_ID` env var does **NOT** contain a numeric Advertising profile ID. It holds
  an `amzn.application.*` string (~50 chars). Passing it as `Amazon-Advertising-API-Scope`
  returns HTTP 400 `"profile ID required"`.
- Real profiles come from `GET /v2/profiles` (needs ClientId header + bearer, no Scope).
  Available seller profiles on this account:
  - **US: `26765323558215`**
  - CA: `2840235221595557`
  - MX: `3892485344323414`
- This FBA business reports against the profile with actual Sponsored Products activity in
  the window (determined by probing each). See each report for which profile was used.
- **TODO for a human:** fix the `AMZ_PROFILE_ID` env var to the correct numeric profile ID
  so runs don't have to auto-detect. Until then this script auto-selects.
- Auto-select logic that works: only the **US** profile has campaigns; CA and MX return
  0 campaigns. So default to US (`26765323558215`) unless that changes.

## Lessons from run 2026-10-09 (first 2-day report)
- **Account was fully dark in the window.** 15 ENABLED SP campaigns, but 0 impressions /
  0 clicks / 0 spend / 0 sales on Oct 5–6 AND across the prior 30 days. Confirmed via
  `spCampaigns` SUMMARY report for both windows — it is real, not a data error.
- Campaign states via `POST /sp/campaigns/list` (ct `application/vnd.spCampaign.v3+json`):
  54 total = 15 ENABLED, 32 PAUSED, 7 ARCHIVED. Enabled ones run tiny $1.50 daily budgets.
- **Likely cause of zero delivery on enabled campaigns:** bids/budgets too low to win
  auctions, or product listing ineligible (out of stock / lost Buy Box). Main ASIN is
  B0FXW3GW5F (Cat Deterrent Spray / Pet Odor Eliminator). Check listing health first.
- **Don't fabricate.** When everything is zero, report zero plainly and explain the
  probable cause + next actions. ACOS/ROAS/CTR/CPC/ToS-share are undefined (shown as "—").
- `spTargeting` / `spSearchTerm` reports are pointless when there are 0 clicks — skip them
  to save time while the account is dark; re-enable once impressions return.
- Report files written: `reports/ppc-2day-latest.md` + `reports/ppc-2day-YYYY-MM-DD.md`.
  For comparison next run, load the most recent dated file BEFORE this one.

## Delivery / email status (run 2026-10-09)
- Fill in whether Google Drive upload ('PPC Reports' folder) and the email to
  uzoebo.archbold@gmail.com succeeded, so the next run knows the state of those integrations.
