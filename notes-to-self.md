# PPC Analyst — Notes to Self

Lessons learned across runs. Read this first, every run.

## Credentials / account (learned 2026-11-25)
- `AMZ_PROFILE_ID` env var is **invalid** — it is a 50-char non-numeric string,
  not a real Amazon profile ID. Do NOT pass it as the Scope header; the API
  returns `400 profile ID required`.
- Auth itself works (CLIENT_ID / CLIENT_SECRET / REFRESH_TOKEN are valid).
  Token endpoint: `https://api.amazon.com/auth/o2/token`.
- Resolve the real profile via `GET /v2/profiles`. This account has 3 profiles:
  - CA `2840235221595557` (CAD) — 0 campaigns
  - MX `3892485344323414` (MXN) — 0 campaigns
  - **US `26765323558215` (USD) — the active one. 54 campaigns. USE THIS.**
- The US profile shows **`validPaymentMethod: false`**. This matters (see below).

## Amazon Ads API v3 reporting gotchas
- Base: `https://advertising-api.amazon.com`. Endpoint: `POST /reporting/reports`.
- For `spCampaigns` reportType, columns `acosClicks7d` / `roasClicks7d` are
  **NOT allowed** (only the 14d variants exist). Pull `cost`, `sales7d`,
  `purchases7d` and **compute ACOS = cost/sales, ROAS = sales/cost** yourself.
- Valid-and-useful spCampaigns columns: impressions, topOfSearchImpressionShare,
  clicks, clickThroughRate, cost, costPerClick, purchases7d, sales7d,
  campaignName, campaignId, campaignStatus.
- `spTargeting` report returns rows only where there was activity; with zero
  delivery it returns **0 rows** (not zeroed rows).
- v3 reports are async: create -> poll `GET /reporting/reports/{id}` until
  `COMPLETED` -> download the gzipped JSON from the `url`.

## Current business situation (as of 2026-11-25)
- **The account is NOT delivering ads.** All 15 ENABLED campaigns show
  0 impressions / 0 clicks / 0 spend / 0 sales over the last 14 days.
  Most likely cause: `validPaymentMethod: false` on the US Ads profile has
  suspended delivery. Each run, re-check the payment flag and whether delivery
  has resumed; flag it loudly until fixed.
- Product/ASIN in play: B0FXW3GW5F (Cat Deterrent Spray / Pet Odor Eliminator),
  plus a Cat Tunnel Bed campaign.

## Report mechanics
- Reports folder: `reports/`. Save `ppc-2day-latest.md` + `ppc-2day-YYYY-MM-DD.md`.
- Compare each run against the previous report of the SAME type.
- Google Drive folder: "PPC Reports". Email to uzoebo.archbold@gmail.com.
- Date window for 2-day report: the 2 full days ending 48h before run time.
