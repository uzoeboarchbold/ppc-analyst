# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest first.

## Environment / API facts learned
- **Region:** The account lives on the **North America** Advertising API host
  `https://advertising-api.amazon.com`. The EU (`-eu`) and FE (`-fe`) hosts are
  **blocked by the environment's egress/network policy** (proxy returns
  `403 Forbidden` on CONNECT). Do not waste retries on EU/FE — use NA only.
- **Token refresh works:** `https://api.amazon.com/auth/o2/token` with
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN` returns a valid
  access token. Credentials themselves are good.
- **Valid profiles on this account** (from `/v2/profiles`, NA host, no scope
  header): US seller `26765323558215` (ATVP…), CA seller `2840235221595557`,
  MX seller `3892485344323414`. The US profile is the most likely intended one
  for an amazon.com FBA business.
- **Credential env vars cannot be echoed** — the harness blocks printing them.
  Have a script read them from the environment directly; never `echo`/`cat` them.
- Run Python that reads env/untrusted dirs with `python3 -I`.

## Open issues to fix
- **[2026-10-06] `AMZ_PROFILE_ID` is misconfigured.** It is set to an
  `amzn1.application.*` identifier (a Login-with-Amazon *application* ID), not a
  numeric Advertising *profile* ID. Every reporting call fails with
  `400 "Invalid scope: amzn1.application…"`. **Fix:** set `AMZ_PROFILE_ID` to a
  numeric profile ID — almost certainly the US seller profile `26765323558215`.
  Until this is corrected no live data can be pulled, so reports are blocked.

## Reporting API notes (for when the profile ID is fixed)
- Use Ads API v3 reporting: POST `/reporting/reports` with
  `adProduct=SPONSORED_PRODUCTS`, `groupBy=["campaign"]` for the campaign table
  and `groupBy=["targeting"]` for keyword/target rows, `timeUnit=SUMMARY`,
  `format=GZIP_JSON`. Poll the report id until `COMPLETED`, then GET the signed
  `url` and gunzip the JSON.
- Metrics columns: impressions, clicks, cost, purchases14d, sales14d,
  topOfSearchImpressionShare. Derive CTR = clicks/impr, CPC = cost/clicks,
  ACOS = cost/sales, ROAS = sales/cost.
- `topOfSearchImpressionShare` is only returned on the campaign groupBy.

## Report cadence / comparison
- 2-day window = the 2 full days ending 48h before the run (data lags ~48h).
  Example: run Tue → covers the preceding Fri & Sat.
- Previous 2-day report lives at `reports/ppc-2day-latest.md`; dated copies at
  `reports/ppc-2day-YYYY-MM-DD.md`. Compare headline metrics against the latest.
