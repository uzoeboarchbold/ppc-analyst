# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / API facts (verified 2026-06-17)
- **AMZ_PROFILE_ID env var is NOT usable** — it holds an *application id*
  (`amzn1.application...`), not a numeric advertising profile id.
  The real profiles for this seller (Uzoebo Archbold E-Commerce, seller
  A1C2I8MOP52E35) are: **US = 26765323558215** (USD, $40 daily budget — the
  active one), CA = 2840235221595557, MX = 3892485344323414.
  **Use US profile 26765323558215** as the Amazon-Advertising-API-Scope.
- Region endpoint: NA = `advertising-api.amazon.com` works. EU
  (`advertising-api-eu`) and FE (`advertising-api-fe`) are **blocked by the
  network egress allowlist** — do not bother trying them.
- Token: POST `https://api.amazon.com/auth/o2/token` with grant_type=
  refresh_token + client id/secret. Access token lasts 3600s.

## Reporting API v3 (Sponsored Products)
- Endpoint: POST `/reporting/reports` with Content-Type
  `application/vnd.createasyncreportrequest.v3+json`. Async: poll GET
  `/reporting/reports/{id}` until status COMPLETED, then download the gzip URL.
- **acosClicks30d / roasClicks30d are NOT valid columns.** Only 7d/14d
  attribution variants exist for acos/roas. **Compute ACOS and ROAS myself:**
  ACOS = cost / sales30d, ROAS = sales30d / cost. Use `sales30d` and
  `purchases30d` for 30-day attribution.
- Report type ids used: `spCampaigns` (groupBy ["campaign"]),
  `spTargeting` (groupBy ["targeting"]), `spSearchTerm` (groupBy ["searchTerm"]).
- Pull script lives at repo root: `pull_ppc.py` (edit dates START/END at top).

## Account status snapshot (2026-06-17)
- Almost the entire account is **PAUSED/ARCHIVED**. Only TWO campaigns were
  ENABLED: "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales" ($8/day each,
  started 2026-06-09). Both delivered **zero impressions** on 2026-06-13/14.
- When the window shows all zeros, that is REAL (account dormant), not a bug —
  the campaign report still returns the campaign names, confirming the pipeline.
  spTargeting/spSearchTerm return [] when there is no click activity.

## Date window logic
- Data lags ~48h. 2-day report = the 2 full days ending 48h before run.
  Run 2026-06-17 → cutoff 2026-06-15 → cover 2026-06-13 (Sat) & 2026-06-14 (Sun).

## Reports of this type
- File pattern: `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`.
- Previous 2-day report to compare against = most recent dated `ppc-2day-*.md`
  before today. 2026-06-17 was the FIRST run (no baseline).
