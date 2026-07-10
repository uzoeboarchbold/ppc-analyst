# Notes to Self — PPC Analyst

Lessons learned from past runs. Read this first every time.

## Credentials & API access (learned 2026-07-10)
- Token exchange works at `https://api.amazon.com/auth/o2/token` with the four
  `AMZ_*` env vars. Access token lasts 3600s.
- **IMPORTANT:** `AMZ_PROFILE_ID` env var holds `amzn1.application.dd42b...` —
  that is an APPLICATION/client id, NOT a usable numeric profile id. Do not pass
  it as the Advertising-API-Scope. Instead list profiles and pick the numeric one.
- Region is **NA** → `advertising-api.amazon.com`. EU/FE hosts are blocked by the
  proxy (CONNECT 403), so don't bother trying them.
- Profiles on this account (seller "Uzoebo Archbold E-Commerce"):
  - **US = 26765323558215** (USD, $40/day budget) ← PRIMARY, use this one
  - CA = 2840235221595557 (has 0 campaigns)
  - MX = 3892485344323414 (polling is slow/times out; not the primary market)

## Reporting API v3 flow (works)
- POST `/reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json` and
  `Amazon-Advertising-API-Scope: <numeric profile>`.
- Report types used: `spCampaigns` (groupBy `campaign`) and `spSearchTerm`
  (groupBy `searchTerm`). Poll GET `/reporting/reports/{id}` until COMPLETED,
  then download the gzip-JSON from `url`.
- `topOfSearchImpressionShare` comes back `null` when impressions are 0.
- Sales/purchases columns: `sales7d`, `purchases7d`.

## Account status observations
- 2026-07-06/07: US account has 2 ENABLED campaigns ("SP KT | ST w/ Sales",
  "SP PT | ST w/ Sales") but BOTH delivered ZERO impressions — verified this is
  real by pulling a 14-day window (Jun24–Jul7), still all zeros. Campaigns are
  live but not serving. Flag this each run until delivery starts.

## Report bookkeeping
- 2-day report files: `reports/ppc-2day-latest.md` + `reports/ppc-2day-YYYY-MM-DD.md`.
- Compare each new 2-day report against the previous `ppc-2day-*` dated file.
