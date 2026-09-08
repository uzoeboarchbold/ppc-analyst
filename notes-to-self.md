# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest lessons at the top.

## Account / credentials
- **AMZ_PROFILE_ID is WRONG.** The env var holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an *application* ID, not an advertising profile scope. It cannot be used as
  `Amazon-Advertising-API-Scope`. Ignore it and use the real profile below.
- **Real profiles** (from `GET /v2/profiles`, account "Uzoebo Archbold E-Commerce", seller A1C2I8MOP52E35):
  - **US → 26765323558215** ← this is the active account. Use this one.
  - CA → 2840235221595557 (no delivery), MX → 3892485344323414 (no delivery)
- US profile shows `validPaymentMethod: false` and dailyBudget $40. The invalid payment method is the
  most likely reason ads barely deliver — worth flagging to the owner every run until fixed.
- OAuth token refresh works: POST https://api.amazon.com/auth/o2/token (grant_type=refresh_token).
  Access token lasts 3600s.

## API / networking
- Only the **NA** endpoint (advertising-api.amazon.com) is reachable. EU and FE hosts are blocked by
  the egress proxy (CONNECT 403). Don't waste retries on them.
- Reporting API v3 async flow works: POST /reporting/reports (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), poll GET /reporting/reports/{id}, download the
  gzip-json `url`. Use `format: GZIP_JSON`, `timeUnit: SUMMARY`.
- **Campaign report gotcha:** `acosClicks7d` and `roasClicks7d` are INVALID columns at campaign
  grouping (reportTypeId `spCampaigns`). They ARE valid at targeting/search-term grouping. For the
  campaign report, request `cost`, `sales7d`, `purchases7d` and compute ACOS = cost/sales,
  ROAS = sales/cost yourself. `topOfSearchImpressionShare` is valid at campaign grouping.
- Report type IDs used: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm).
- Duplicate report requests within a short window return HTTP 425 pointing at the original reportId —
  reuse that id rather than treating it as an error.
- Coding note: don't `import pull` (the pull script) to reuse its functions — its module-level code
  re-fires all three report creations on import. Keep helper funcs in a module with no top-level calls.

## Data reality
- This account is **nearly dormant**. Full 30-day check (Aug 7–Sep 5 2026): only ~2,099 impressions,
  18 clicks, $8.58 spend, $13.99 sales across the whole month. So a 2-day window showing zeros is
  REAL, not a pull error. Always sanity-check a zero window against a wider range before calling it a
  failure, but don't invent numbers.
- When the window has zero delivery, the targeting and search-term reports return 0 rows (expected).

## Report housekeeping
- Reports live in `reports/`. 2-day report: overwrite `ppc-2day-latest.md` + dated copy
  `ppc-2day-YYYY-MM-DD.md`. Compare against the previous `ppc-2day-*` file (by date in filename).
- Google Drive: upload to folder named "PPC Reports". Email to uzoebo.archbold@gmail.com.
- Date window (2-day, 48h lag): cover the 2 full days ending 48h before run. Run Tue Sep 8 → Sep 4 & 5.
