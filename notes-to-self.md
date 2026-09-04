# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons at top.

## Environment / API
- **Region:** Account lives in **NA** — use `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the outbound proxy (403 CONNECT tunnel) anyway.
- **OAuth:** Refresh token in `AMZ_REFRESH_TOKEN` works against
  `https://api.amazon.com/auth/o2/token`. Access token lasts 3600s.
- **PROFILE ID GOTCHA (important):** `AMZ_PROFILE_ID` env var contains an
  *application* id (`amzn1.application.…`), **not** a numeric Ads profile id.
  It cannot be used as the scope header. The real profiles under this account
  (`/v2/profiles`) are:
    - US: `26765323558215` (USD, dailyBudget $40) ← **active advertising account, use this**
    - CA: `2840235221595557` (CAD, no real budget)
    - MX: `3892485344323414` (MXN, no real budget)
  Use the **US** profile `26765323558215` in the `Amazon-Advertising-API-Scope`
  header. Re-verify each run in case budgets/accounts change.

## Reporting
- Use Sponsored Products v3 async reporting: `POST /reporting/reports`.
  Poll `GET /reporting/reports/{id}` until status COMPLETED, then download the
  gzipped JSON from the returned `url`.
- Report types used: `spCampaigns` (groupBy campaign — has
  topOfSearchImpressionShare), `spSearchTerm` (groupBy searchTerm — for
  negatives + exact-match ideas).
- Account timezone: America/Los_Angeles. Report dates are in account tz.

## Date window
- Data lags ~48h. For the 2-day report cover the 2 full days ending 48h before
  run time. E.g. run Fri Sep 4 23:03 UTC → cutoff Sep 2 23:03 → last fully
  finalised day = Sep 1 → cover **Aug 31 + Sep 1**.

## Report bookkeeping
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `ppc-2day-[YYYY-MM-DD].md`.
- Compare against the previous `ppc-2day-*.md` (this-type) report.
- Upload to Google Drive folder 'PPC Reports'; email to uzoebo.archbold@gmail.com.

## History
- 2026-09-04: First run. No prior 2-day report exists, so no comparison
  baseline yet — next run compares against this one.
