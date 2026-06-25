# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## 2026-06-25 (first run — 2-day report)
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It is set to an *application ID*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT an advertising
  profile ID. Do not pass it to the Ads API — it will fail.
- **Resolve the profile at runtime** by calling `GET /v2/profiles` on the NA
  endpoint and picking the right one. Available profiles (seller "Uzoebo
  Archbold E-Commerce"):
    - US: `26765323558215` (USD, dailyBudget 40.0)  ← ACTIVE advertising account
    - CA: `2840235221595557` (CAD, dailyBudget default/unlimited — not active)
    - MX: `3892485344323414` (MXN, dailyBudget default/unlimited — not active)
  Use the **US profile `26765323558215`** — it is the only one with a real
  daily budget, i.e. where ads actually run. Reports are in **USD**.
- **Region = NA** (`advertising-api.amazon.com`). EU and FE endpoints are
  BLOCKED by the network proxy (CONNECT tunnel 403), so only NA is reachable.
- **Token refresh** works against `https://api.amazon.com/auth/o2/token` with
  the env creds. Access token lasts 3600s.
- **Date window logic (2-day):** end 48h before run, cover the 2 full days
  before that cutoff. Run 2026-06-25 23:02 UTC → cutoff 06-23 23:02 → cover
  **06-21 and 06-22**.
- Reports folder + previous report did not exist on first run; created them.
- Reporting API: use v3 async `/reporting/reports` (adProduct
  SPONSORED_PRODUCTS). topOfSearchImpressionShare is available in the campaign
  groupBy report. Compute CTR/CPC/ACOS/ROAS ourselves from raw columns.
