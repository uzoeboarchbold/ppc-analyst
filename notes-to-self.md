# Notes to Self — PPC Analyst

Running log of lessons so each run goes smoother. Newest lessons at top.

## Environment / API access
- **Region:** Account is North America. Use `https://advertising-api.amazon.com`
  (NA host). EU/FE hosts are blocked by the outbound proxy (403 CONNECT tunnel),
  and this account's profiles are all NA anyway.
- **Token:** Refresh via `https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token, client_id, client_secret, refresh_token). Works.
- **PROFILE ID GOTCHA (important):** The env var `AMZ_PROFILE_ID` does NOT contain
  a numeric profile ID — it contains an application id like
  `amzn1.application.xxxxxxxx`. The Ads API rejects it with
  "profile ID required". Fix: call `GET /v2/profiles` (only needs ClientId +
  Bearer, no Scope) and pick the numeric profile. This account has 3 profiles:
  - US  `26765323558215`  (USD, dailyBudget $40 — the ACTIVE / managed one) ← use this
  - CA  `2840235221595557` (CAD)
  - MX  `3892485344323414` (MXN)
  Use the **US** profile (`26765323558215`) as `Amazon-Advertising-API-Scope`.
- **curl vs urllib:** Python `urllib` mangles custom header case; use `curl`
  (subprocess) or `requests` so `Amazon-Advertising-API-*` headers pass verbatim.

## Reporting API v3 (Sponsored Products)
- Async flow: POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`) → poll GET
  `/reporting/reports/{id}` until status COMPLETED → download `url` (GZIP JSON).
- **Invalid columns:** `acosClicks7d` and `roasClicks7d` are NOT valid summary
  columns for `spCampaigns` and cause a 400. Do NOT request them. Compute ACOS
  (cost/sales) and ROAS (sales/cost) yourself from `cost`, `sales7d`.
- Working campaign columns: campaignId, campaignName, impressions, clicks, cost,
  purchases7d, sales7d, clickThroughRate, costPerClick, topOfSearchImpressionShare.
- Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`,
  columns incl. keyword, searchTerm, matchType, impressions, clicks, cost,
  purchases7d, sales7d, costPerClick.
- `topOfSearchImpressionShare` is a percentage value (e.g. 0.11 = 0.11%).
  `clickThroughRate` is also a percent (e.g. 6.67 = 6.67%).

## Date window (2-day report)
- Data lags ~48h. End window 48h before run, then take the 2 most recent FULL days.
- Run 2026-08-03 23:07 UTC → 48h back = 2026-08-01 23:07 → last 2 full days =
  **2026-07-30 and 2026-07-31**.

## Report bookkeeping
- Save to `reports/ppc-2day-latest.md` (overwrite) + dated `ppc-2day-[YYYY-MM-DD].md`.
- Compare against the previous `ppc-2day-*` report. First run (2026-08-03) had no
  prior report, so Part C established the baseline.

## Account context (as of first run)
- Very low activity: 2 days = 50 impressions, 1 click, $0.98 spend, 0 sales.
  Top-of-search share ~0% almost everywhere → ads barely serving. Likely low bids
  / paused campaigns / stock. Flagged in report "what to do next".

## Delivery
- Google Drive: upload the report file to the folder named **"PPC Reports"**.
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
