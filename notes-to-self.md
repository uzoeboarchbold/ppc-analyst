# Notes to Self — PPC Analyst (automated)

Running log of lessons so each run goes smoother. Read this first every run.

## Environment / API access

- **Amazon Ads API works via NA endpoint only.** Use `https://advertising-api.amazon.com`.
  EU (`-eu`) and FE (`-fe`) hosts return `403 CONNECT tunnel failed` through the agent
  proxy — but the account is US, so NA is all we need.
- **Auth:** POST to `https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token`
  and the four `AMZ_*` env vars. Returns a 1-hour `access_token`. Works fine.
- **`AMZ_PROFILE_ID` env var is WRONG.** It holds an application ID
  (`amzn1.application....`), not a numeric advertising profile ID. Do NOT use it as the
  `Amazon-Advertising-API-Scope` header. Instead call `GET /v2/profiles` and pick the
  **US / USD** profile. As of Aug 2026 that is **`26765323558215`** (US seller,
  Uzoebo Archbold E-Commerce). Other profiles: CA `2840235221595557`, MX `3892485344323414`.

## Reporting API v3 (async)

- Flow: `POST /reporting/reports` → poll `GET /reporting/reports/{id}` until
  `status=COMPLETED` → download the `url` (GZIP_JSON) → gunzip → parse.
- Reports usually complete in ~30–90s. Poll every ~20s.
- Content-Type header must be `application/vnd.createasyncreportrequest.v3+json`.
- **Do NOT include `date` in `columns` when `timeUnit=SUMMARY`** — returns HTTP 400
  ("date is not a supported column for this time unit"). Use start/endDate only.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`. Good columns:
  campaignId, campaignName, impressions, clicks, cost, purchases30d, sales30d,
  clickThroughRate, costPerClick, topOfSearchImpressionShare.
- Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`. Columns:
  keyword, matchType, searchTerm, targeting, impressions, clicks, cost, purchases30d,
  sales30d, clickThroughRate, costPerClick.
- `topOfSearchImpressionShare` comes as a fraction (0.14 = 14%). CTR/CPC come as-is.

## Delivery

- **Google Drive works.** Folder "PPC Reports" = id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload the report there each run.
- **Gmail is installed but `enabledInChat: false`** for this automated session, so email
  CANNOT be sent. Note it in the report each run. To fix, the user must enable the Gmail
  connector for this session in connector settings. (Same issue every run so far.)

## Date window

- 2-day report covers the 2 full days ending 48h before the run.
  Run 2026-08-21 → covered 2026-08-17 & 2026-08-18.

## Comparison targets (previous 2-day reports)

- Reports live in the Drive "PPC Reports" folder. Naming has been inconsistent
  (some titled "PPC 2-Day Report — DD-DD Mon YYYY", some `ppc-2day-YYYY-MM-DD.md`).
  Pick the most recent **2-day** one by covered dates / modified time to compare against.
- 2026-08-21 run compared against "13–14 Aug 2026" report
  (Impr 72, Clicks 0, Spend $0, Sales $0).

## Account context / observations

- Account is barely active. 13–14 Aug: 72 impr, 0 clicks, $0 spend. 17–18 Aug: 74 impr,
  2 clicks, $0.50 spend, still 0 sales. Many campaigns serve 0 impressions (low bids /
  low search volume). No converting search terms yet, so no exact-match promotions and
  no negatives to suggest — keep watching once clicks/sales pick up.
