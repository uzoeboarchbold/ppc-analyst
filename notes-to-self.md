# Notes to Self — PPC Analyst

Running log of lessons so future runs work first time. Newest at top.

## Environment / API access (learned 2026-11-22, first run)
- **AMZ_PROFILE_ID env var is NOT a usable profile scope.** It holds an
  *application* ID (`amzn1.application.…`). Passing it as
  `Amazon-Advertising-API-Scope` returns `400 Invalid scope`.
  → To get real profiles, GET `https://advertising-api.amazon.com/v2/profiles`
    with NO scope header. Then use the numeric `profileId`.
- **Active account = US profile `26765323558215`** (USD, seller
  "Uzoebo Archbold E-Commerce", marketplace ATVPDKIKX0DER).
  CA (`2840235221595557`) and MX (`3892485344323414`) exist but have 0 campaigns.
- **Proxy only allows the NA host** `advertising-api.amazon.com` and the token
  host `api.amazon.com`. EU (`-eu`) and FE (`-fe`) hosts return
  `403 agent proxy: no rule allows this host`. Don't bother trying them.
- **Token refresh**: POST `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id/secret. Works fine.

## Reporting API (v3) column gotchas
- Campaign groupBy (`spCampaigns`): `acosClicks7d` / `roasClicks7d` are
  **NOT valid columns** → 400. Compute ACOS = cost/sales7d,
  ROAS = sales7d/cost yourself. Valid cols used: campaignName, campaignId,
  campaignStatus, impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare, costPerClick, clickThroughRate.
- Report flow: POST /reporting/reports (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), poll
  GET /reporting/reports/{id} every ~15s until COMPLETED, download `url`
  (gzip JSON). Reports usually finish in 1–3 polls.
- Search-term report (`spSearchTerm`, groupBy searchTerm) returns an **empty
  list when there is no spend in the window** — expected, not an error.

## State of the account (2026-11-22 run)
- **US profile `validPaymentMethod: false`.** All 15 campaigns returned by the
  report are ENABLED but show **ZERO** impressions/clicks/cost/sales — not just
  in the 2-day window but across Nov 5–19. Ads are effectively dark, almost
  certainly because there is no valid payment method on the US Ads account.
  If future runs still show zero delivery, lead the report with this and check
  whether the payment method has been fixed. Don't invent numbers.

## Report mechanics
- Reports folder: `reports/`. 2-day files: `ppc-2day-latest.md` (overwrite) +
  `ppc-2day-[YYYY-MM-DD].md` (dated, by run date). Compare to previous
  `ppc-2day-*` dated file.
- Google Drive folder name: "PPC Reports". Email to uzoebo.archbold@gmail.com.
