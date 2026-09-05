# Notes to Self — PPC Analyst

Running log of lessons so future automated runs go smoothly. Newest at top.

## Environment / API setup (learned 2026-09-05)
- **AMZ_PROFILE_ID is NOT a numeric profile ID.** It is set to an application
  ARN (`amzn1.application....`). It cannot be used as `Amazon-Advertising-API-Scope`.
  Instead: get an access token, call `GET /v2/profiles`, and pick the numeric
  profile. There are three profiles on this account (all "Uzoebo Archbold
  E-Commerce"): CA `2840235221595557` (CAD), MX `3892485344323414` (MXN),
  US `26765323558215` (USD).
  **Only the US profile has Sponsored Products campaigns** (54 total: 15 enabled,
  32 paused, 7 archived). CA and MX have zero campaigns. → Always report on the
  **US profile 26765323558215, currency USD.**
- **Region = North America.** Base URL `https://advertising-api.amazon.com`.
  The EU and FE hosts are blocked by the outbound proxy (403) — do not try them.
- **Token refresh** at `https://api.amazon.com/auth/o2/token` with client_id,
  client_secret, refresh_token — works, returns a 1-hour access token.
- **Do not name a script `token.py`** — it shadows Python's stdlib `token`
  module and breaks `import requests`.

## Reporting API (v3) — what works
- Create async report: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: `reportTypeId: spCampaigns`, `groupBy: ['campaign']`,
  columns incl. `impressions, clicks, cost, purchases7d, sales7d,
  clickThroughRate, costPerClick, topOfSearchImpressionShare, campaignName,
  campaignStatus`. Returns only rows that had data (≈ enabled/active campaigns).
- Search-term report: `reportTypeId: spSearchTerm`, `groupBy: ['searchTerm']`,
  columns incl. `searchTerm, keyword, matchType, impressions, clicks, cost,
  purchases7d, sales7d`.
- `timeUnit: SUMMARY`, `format: GZIP_JSON`. Poll `GET /reporting/reports/{id}`
  until status COMPLETED, then download the `url` (gzip JSON).
- Compute ACOS = cost/sales, ROAS = sales/cost, CTR = clicks/impressions,
  CPC = cost/clicks yourself. `topOfSearchImpressionShare` is a fraction
  (e.g. 0.03 = 3%); can be null when 0 impressions.

## Business context
- Account is currently **very low activity**. On 2026-09-01→02 the whole US
  account served only 287 impressions, 1 click, $0.08 spend, 0 sales.
  This is real data, not an error — report it honestly, don't invent numbers.
- Report cadence for this file: 2-DAY report. Compare vs the previous 2-day
  report in `reports/`. Latest lives at `reports/ppc-2day-latest.md`, dated
  copies at `reports/ppc-2day-[YYYY-MM-DD].md`.

## Delivery
- Google Drive upload target: folder named "PPC Reports"
  (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Upload with `create_file`,
  `contentMimeType: text/markdown`, `disableConversionToGoogleType: true`,
  and pass content via `base64Content` or `textContent` — NOT the placeholder.
  (`update_file` only changes metadata, not content; to replace content,
  trash the old file and create a new one.)
- **Email: NO email/Gmail connector is available in this session.** The
  requested email to uzoebo.archbold@gmail.com (subject "PPC 2-Day Report —
  [dates]") could NOT be sent. State this in the report's delivery note each
  run until a mail connector is added. Do not fake a send.
- Date window: data lags ~48h. For the 2-day report cover the 2 full days
  ending 48h before the run (e.g. run Sat 2026-09-05 → cover Sep 1 & Sep 2).
