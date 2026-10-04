# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / environment facts
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It contains an application ID
  (`amzn1.application...`), NOT a numeric advertising profile ID. Do not use it
  directly as the API scope.
- The working profiles live in the **NA** region endpoint
  (`https://advertising-api.amazon.com`). EU/FE endpoints are blocked by the
  proxy (403) and are not needed.
- Three profiles exist on this account (seller "Uzoebo Archbold E-Commerce"):
  - US `26765323558215` (USD) — **the active account; use this one.**
  - CA `2840235221595557` (CAD) — no campaigns.
  - MX `3892485344323414` (MXN) — no campaigns.
- Product line: cat / pet-odor products (ASIN B0FXW3GW5F and a cat tunnel bed).

## API how-to (Sponsored Products, Ads API v3)
- OAuth: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token
  + client_id/secret. Access token lasts 3600s.
- Reports: async v3 at POST `/reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`. Poll
  GET `/reporting/reports/{id}` until status COMPLETED, then download the
  presigned `url` (GZIP JSON, no auth header on the S3 URL).
- **ACOS and ROAS are NOT valid columns** (`acosClicks7d`/`roasClicks7d` rejected).
  Pull `cost` and `sales7d` and compute: ACOS = cost/sales, ROAS = sales/cost.
- Valid campaign columns used: campaignId, campaignName, impressions, clicks,
  cost, purchases7d, sales7d, clickThroughRate, costPerClick,
  topOfSearchImpressionShare.
- To find the active profile when scope is unknown: list `/sp/campaigns/list`
  per profile; the one with campaigns is the live account.

## Data observations (as of 2026-10-04 run)
- **Account has had ZERO impressions since 2026-09-02.** Every day from Sep 3
  onward (incl. the whole report window Sep 30–Oct 1) returned 0 impressions,
  0 clicks, 0 spend, 0 sales. This is real data, not an API failure.
- 15 campaigns ENABLED with tiny $1.50–$2.50/day budgets (total $23.50/day) yet
  getting zero delivery — points to bids far below market and/or listing
  ineligibility (out of stock / lost Buy Box / suppressed listing).
- If a future window again returns 0 rows, it is almost certainly a genuine
  "no delivery" state, not a bug — confirm by pulling a wider historical window.

## Delivery channels
- **Google Drive: works.** Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with create_file, parentId = that id, contentMimeType text/markdown,
  disableConversionToGoogleType=true (keeps it a .md).
- **Email: BLOCKED in this session.** Gmail connector is connected at the org
  level but `enabledInChat:false` — its tools aren't loaded here, so the report
  can't be emailed automatically. The user must enable the Gmail connector for
  this chat/automation in connector settings. Until then, delivery = repo +
  Drive + the run notification. Re-check each run; send the email once Gmail is
  enabled.

## Report bookkeeping
- Reports saved to `reports/`: `ppc-2day-latest.md` (overwritten each run) +
  dated `ppc-2day-YYYY-MM-DD.md`.
- This 2026-10-04 run is the FIRST 2-day report → no prior report to compare
  against (baseline). Future runs: compare against the previous `ppc-2day-*`.
