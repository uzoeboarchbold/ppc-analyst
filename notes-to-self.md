# Notes to Self — PPC Analyst

Running memory so each run is a bit smarter than the last. Read this first.

## Account / API facts (confirmed 2026-07-17)

- **The `AMZ_PROFILE_ID` env var is WRONG.** It is set to an *application* ID
  (`amzn1.application....`), NOT a numeric Amazon Ads profile ID. Do not pass it
  as `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` and pick the
  right numeric profile.
- Region endpoint: **NA** → `https://advertising-api.amazon.com`. The EU/FE
  endpoints are blocked by the proxy (403) and aren't needed anyway.
- Profiles on this account (seller "Uzoebo Archbold E-Commerce", seller id
  A1C2I8MOP52E35):
  - **US = 26765323558215 (USD)** ← the ACTIVE advertising account. Use this.
  - CA = 2840235221595557 (CAD) — 0 campaigns, ignore.
  - MX = 3892485344323414 (MXN) — 0 campaigns, ignore.
- Main product advertised: Pet Odor Eliminator / Cat Deterrent Spray, ASIN
  B0FXW3GW5F (many campaigns paused; only a few ENABLED).

## Auth

- Token endpoint: `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + AMZ_REFRESH_TOKEN + AMZ_CLIENT_ID + AMZ_CLIENT_SECRET.
  Access token lasts ~60 min. Refresh token in env works.

## Reporting API v3 (async) — gotchas learned

- Endpoint: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`.
- **spCampaigns report does NOT allow `acosClicks7d` / `roasClicks7d` columns.**
  Compute ACOS = cost/sales*100 and ROAS = sales/cost yourself. CTR
  (`clickThroughRate`) and CPC (`costPerClick`) ARE provided. Also has
  `topOfSearchImpressionShare`.
- spTargeting report DOES allow acosClicks7d/roasClicks7d, plus keyword,
  matchType, targeting.
- Use `timeUnit: SUMMARY` (no `date` column allowed with SUMMARY).
- Attribution: use `purchases7d` / `sales7d`. Note: because data ends ~48h ago,
  7-day conversion attribution is still partial — sales may tick up later.
- Poll `GET /reporting/reports/{reportId}` until status=COMPLETED, then download
  the gzip JSON from the returned `url` (S3, no auth headers needed).

## Date window logic

- Data lags ~48h. 2-day report = the 2 full days ending 48h before run time.
  e.g. run Fri 2026-07-17 23:04 UTC → cover 2026-07-13 and 2026-07-14.

## Delivery

- Reports saved to repo `reports/`: overwrite `ppc-2day-latest.md` + dated copy
  `ppc-2day-YYYY-MM-DD.md`. Commit + push to branch claude/great-hopper-0r2lvc.
- Upload to Google Drive folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Open items / TODO for future runs

- (2026-07-17) First run: no previous 2-day report existed, so no comparison was
  possible. Next run should compare against ppc-2day-latest.md from this run.
- (2026-07-17) CONFIRMED: there is NO email-sending tool in this environment.
  Available delivery = Google Drive MCP (create_file) + GitHub repo commit only.
  So the "email to uzoebo.archbold@gmail.com" step cannot be done automatically.
  Deliver via Drive folder "PPC Reports" + repo commit, and state clearly in the
  report + notification that email could not be sent. Future runs: if an email/
  gmail MCP tool appears, use it; otherwise keep flagging this gap.
