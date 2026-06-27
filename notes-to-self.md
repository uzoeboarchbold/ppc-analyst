# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons at top.

## Account / credentials
- **`AMZ_PROFILE_ID` env var is NOT usable.** It contains an application-ID string
  (`amzn1.application....`), not a numeric Advertising profile ID. The API's
  `Amazon-Advertising-API-Scope` header needs a **numeric** profile ID.
- Real profiles on this account (from `GET /v2/profiles`, NA endpoint):
  - **US (active): `26765323558215`** — USD, daily budget $40. This is the one to report on.
  - CA: `2840235221595557` — CAD, no SP campaigns (0 rows).
  - MX: `3892485344323414` — MXN, no SP campaigns (0 rows).
  - Seller name: "Uzoebo Archbold E-Commerce".
- Only the **NA endpoint** `advertising-api.amazon.com` is reachable. EU/FE hosts
  return proxy 403 (CONNECT tunnel failed) — fine, the account is NA anyway.

## Auth
- Token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token,
  refresh_token, client_id, client_secret. Returns access_token (1h). Works.

## Reporting API v3 (Sponsored Products)
- Submit: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Async: poll `GET /reporting/reports/{id}` until status=COMPLETED, then download
  the presigned `url` (S3, **no auth headers**, gzip JSON).
- **spCampaigns** valid ACOS/ROAS columns are `acosClicks14d` / `roasClicks14d`
  (NOT the `...7d` variants — those 400). Targeting/SearchTerm reports DO accept
  `acosClicks7d`/`roasClicks7d`. To keep windows consistent across reports, just
  pull `cost`, `sales7d`, `purchases7d` and compute ACOS=cost/sales, ROAS=sales/cost.
- `topOfSearchImpressionShare` is a valid spCampaigns column (returns null when no
  impressions).
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm).

## Date window (data lags ~48h)
- Data is final up to (now − 48h). For the 2-day report, cover the 2 full calendar
  days ending at the last midnight ≤ (now − 48h).
- e.g. run Sat 2026-06-27 23:02 UTC → cover 2026-06-23 and 2026-06-24.

## Account state (as of 2026-06-27 run)
- **Almost all US campaigns are PAUSED.** Over the last 30 days the previously-active
  "SP Isolated ... B0FXW3GW5F" Cat Deterrent / Pet Odor Eliminator campaigns drove
  ~$329 spend but are now paused. The only ENABLED campaigns —
  "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales" — serve ~zero impressions.
- Consequence: **zero-activity 2-day windows are expected** until the owner re-enables
  campaigns. Report the zeros honestly; do NOT invent numbers. Flag it to the owner —
  their ads are effectively off.
- Main advertised product: ASIN B0FXW3GW5F (cat deterrent / pet odor eliminator).

## Reports of this type
- Save to `reports/ppc-2day-latest.md` and `reports/ppc-2day-[YYYY-MM-DD].md`.
- Compare each run against the previous `ppc-2day-*.md`. (2026-06-27 was the FIRST
  2-day report — no prior to compare against.)
