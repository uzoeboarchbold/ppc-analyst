# PPC Analyst — Notes to Self

Running log of lessons so each run gets smoother. Newest at top.

## Key environment facts (confirmed 2026-09-15)
- **Amazon Ads API region:** Only the North America host is reachable through
  the sandbox proxy: `https://advertising-api.amazon.com`. The EU and FE hosts
  return `403 Forbidden` from the proxy — do not bother trying them.
- **LWA token endpoint that works:** `https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token). Returns a fresh access token; refresh it before
  polling long-running reports.
- **AMZ_PROFILE_ID is NOT a usable scope value.** The env var holds an
  `amzn1.…` account/entity identifier (ends `…ada5c5`), but the Ads API
  `Amazon-Advertising-API-Scope` header needs a *numeric* profile ID. Passing
  the amzn1 value gives `400 "profile ID required"`.
  - Fix: call `GET /v2/profiles` (ClientId + Bearer only, NO scope header) to
    list profiles, then pick the one with real campaigns.
  - This seller (A1C2I8MOP52E35, "Uzoebo Archbold E-Commerce") has 3 profiles:
    - CA 2840235221595557 — 0 campaigns
    - MX 3892485344323414 — 0 campaigns
    - **US 26765323558215 — the live advertising market (use this one).**
- Script filenames: never name a scratch script `token.py` — it shadows the
  stdlib `token` module and breaks `import requests`.

## Reporting API (v3) recipe that works
- `POST /reporting/reports` with Content-Type
  `application/vnd.createasyncreportrequest.v3+json`.
- Body: adProduct SPONSORED_PRODUCTS, timeUnit SUMMARY, format GZIP_JSON.
- reportTypeIds used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
- Poll `GET /reporting/reports/{id}` until status COMPLETED, then GET the `url`
  and gzip-decompress the JSON.
- Metric column names: impressions, clicks, clickThroughRate, cost,
  costPerClick, purchases30d, sales30d, acosClicks14d, roasClicks14d,
  topOfSearchImpressionShare, campaignName, campaignId, keyword, matchType,
  targeting, searchTerm, date.

## Standing business issue to watch (opened 2026-09-15)
- **US ad delivery is DARK.** Zero impressions every day from 2026-09-03
  onward (checked through 09-12). The US Seller profile shows
  `validPaymentMethod: false` — almost certainly why Amazon paused delivery.
- Even *before* the blackout (Aug 14–Sep 2) the account generated **£0 / $0
  in Sponsored Products sales all month** despite small daily spend — targeting
  needs a rethink once billing is fixed.
- Until impressions resume, every 2-day/weekly report will legitimately be all
  zeros. That is a real state, NOT an API failure — report it plainly and keep
  flagging the payment method.

## Report bookkeeping
- Previous report of each type: look in `reports/` for `ppc-2day-latest.md`,
  `ppc-weekly-latest.md`, etc. First 2-day report was 2026-09-15 (no prior to
  compare against).
