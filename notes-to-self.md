# Notes to Self — PPC Analyst (read before every run)

Purpose: carry forward hard-won lessons so future automated runs are smoother.

## Environment / API access
- **Token exchange works.** POST `https://api.amazon.com/auth/o2/token` with
  `grant_type=refresh_token` + AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN. Access token
  lasts 3600s. Refresh at the start of every run.
- **AMZ_PROFILE_ID is WRONG / misconfigured.** The env var contains an
  *application* id (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a
  numeric advertising profile id. Do NOT pass it as the API scope — it will fail.
  Resolve real profiles from `GET /v2/profiles` instead. Known profiles for this
  account (Uzoebo Archbold E-Commerce, seller):
    - **US = 26765323558215  ← the only active one; use this**
    - CA = 2840235221595557 (no SP campaigns as of 2026-09)
    - MX = 3892485344323414 (no SP campaigns as of 2026-09)
  ACTION for a human: set AMZ_PROFILE_ID to `26765323558215`.
- **Only the NA endpoint is reachable** (`https://advertising-api.amazon.com`).
  EU/FE endpoints return `403 Forbidden` through the network proxy. That's fine —
  this account is North America only.

## Reporting API (v3, async)
- Create: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`, header
  `Amazon-Advertising-API-Scope: <numeric profileId>`.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy:["campaign"]`,
  `timeUnit:"SUMMARY"`, `format:"GZIP_JSON"`. Columns that work:
  campaignId, campaignName, impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases14d, sales14d, acosClicks14d,
  roasClicks14d.
- Poll `GET /reporting/reports/{id}` until status COMPLETED, then download the
  gzip-json from `url`. Reports complete in well under a minute for this account.

## Date window (data lags ~48h)
- Use days that are FULLY finalised (≥48h old), i.e. the most recent complete
  calendar day D where D+1 00:00 ≤ now−48h, and for the 2-day report cover D−1..D.
  For a run on 2026-09-02 23:04 UTC this gives **2026-08-29 to 2026-08-30**.

## Account state (as of 2026-09-02 run)
- Account is **near-dormant**: ~329 impressions, **1 click, $0.02 spend, $0 sales**
  over 2 days across 15 US campaigns for two products (B0FXW3GW5F pet-odor/cat-
  deterrent spray; a Cat Tunnel Bed). Most campaigns get 0 impressions.
- Because spend/clicks are ~0 there is nothing to add as exact-match and nothing
  to add as negatives. Don't fabricate optimisation actions — the real issue is
  lack of traffic (bids likely below first-page/placement floor, or newly launched).
- No search-term pull needed while clicks ≈ 0 (nothing actionable). Reinstate it
  once daily clicks are consistently > ~10.

## Delivery
- **Google Drive** connector is enabled in-session — upload works. Folder name
  target: `PPC Reports`.
- **Gmail is connected but toggled OFF for this chat** (enabledInChat=false), so
  this session CANNOT send the email. Report is saved + committed + uploaded to
  Drive instead. ACTION for a human: enable the Gmail connector for the scheduled
  session so the email step can run, OR set up an email-capable tool.

## Comparison
- Store each report so the next run of the same type can diff headline metrics.
  Previous-of-type is found in `reports/` (e.g. `ppc-2day-latest.md`).
