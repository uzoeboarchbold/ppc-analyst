# Notes to self — PPC Analyst routine

Lessons learned, so future runs are faster and don't repeat mistakes. Append new lessons as they come up.

## Account / credentials
- **`AMZ_PROFILE_ID` env var is WRONG.** It holds an *application* ID
  (`amzn1.application....`), NOT a numeric advertising profile ID. Do not pass it
  as the API scope. Instead call `GET /v2/profiles` and pick the right profile.
- **The active account is US:** profile `26765323558215`, USD. CA
  (`2840235221595557`) and MX (`3892485344323414`) exist but have **no campaigns** —
  ignore them.
- **ROOT CAUSE of zero activity: the US account has `validPaymentMethod: false`.**
  With no valid payment method, the ~15 ENABLED Sponsored Products campaigns cannot
  serve at all — hence 0 impressions / 0 spend / 0 sales every run. Outstanding since
  at least late September 2026. Always check `accountInfo.validPaymentMethod` on the
  US profile and lead the report with it when false.

## API mechanics (Amazon Ads v3 reporting)
- Token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token.
- Endpoint: NA = `https://advertising-api.amazon.com`. EU/FE endpoints are blocked by
  this environment's proxy (403 tunnel) — the account is NA anyway, so ignore.
- Required headers: `Authorization: Bearer`, `Amazon-Advertising-API-ClientId`,
  `Amazon-Advertising-API-Scope: <numeric profileId>`.
- Report flow: `POST /reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`) → poll `GET /reporting/reports/{id}`
  until `COMPLETED` → download the presigned S3 `url` (no auth header) → gunzip → JSON.
- **Column gotcha:** use `keyword` NOT `keywordText` (400 error otherwise). Valid
  columns incl: impressions, clicks, cost, purchases7d, sales7d, topOfSearchImpressionShare,
  campaignName, campaignId, campaignStatus, campaignBudgetAmount, costPerClick, matchType,
  searchTerm, targeting.
- reportTypeIds used: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). timeUnit SUMMARY, format GZIP_JSON.
- Campaign metadata (start date, state, budget): `POST /sp/campaigns/list` with
  Content-Type/Accept `application/vnd.spCampaign.v3+json`. Campaigns started 2026-05-18,
  so they are NOT new — zero impressions is a real problem, not a warm-up.
- CTR/CPC/ACOS/ROAS are not direct metrics — compute them (and they are n/a while spend is 0).

## Date window (2-day report, 48h data lag)
- A day D is safely finalised at (D + 3 days) 00:00 UTC. Pick the two most recent days
  that satisfy that vs. now. Matches the spec example (Sun run → Wed+Thu).

## Delivery
- **Google Drive works.** Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload the report there as a Google Doc, title `PPC 2-Day Report — DD-DD Mon YYYY`
  (matches existing convention).
- **EMAIL DOES NOT WORK from the cloud session.** Gmail connector is connected at the
  org level but `enabledInChat: false`, so its tools aren't loaded and I cannot send
  mail. Report this limitation in the report + notification rather than claiming the
  email was sent. To fix: user must enable the Gmail connector's tools for Claude Code
  sessions (claude.ai connector settings).
- Repo: develop on branch `claude/great-hopper-3yhq19`. Save to `reports/`:
  overwrite `ppc-2day-latest.md` and a dated copy `ppc-2day-<window-end-YYYY-MM-DD>.md`
  (named by the window's end date, matching the Drive title's period).
- Previous reports live in the Drive folder (repo `reports/` started empty on this branch).
  Read the latest Drive doc of this type to compare headline metrics.
