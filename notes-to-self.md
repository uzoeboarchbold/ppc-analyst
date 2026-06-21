# Notes to Self — PPC Analyst

Lessons learned across runs. Read this first, every run.

## Environment / API
- **AMZ_PROFILE_ID env var is NOT a usable profile ID.** It contains an
  *application* ID (`amzn1.application.…`). The real numeric profile IDs must
  be fetched from `GET /v2/profiles`. Do not pass the env var as the
  `Amazon-Advertising-API-Scope` header.
- Account has 3 seller profiles under "Uzoebo Archbold E-Commerce":
  - US `26765323558215` (USD) ← **primary, use this for reports**
  - CA `2840235221595557` (CAD)
  - MX `3892485344323414` (MXN)
- API region: **NA only** — `https://advertising-api.amazon.com`. The EU and
  FE hosts are NOT in the network egress allowlist (403). Don't bother trying.
- Auth: standard LWA refresh-token exchange at
  `https://api.amazon.com/auth/o2/token`. Access token lasts 1h.

## Reporting
- Use Reporting API v3 (`POST /reporting/reports`, async: create → poll → download GZIP_JSON).
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (keyword/target), `spSearchTerm` (search terms for negatives + exacts).
- Sales/purchases use the 7-day attribution columns (`sales7d`, `purchases7d`).
- TOS impression share column = `topOfSearchImpressionShare` (spCampaigns).

## Date window logic (2-day report)
- Data lags ~48h. Window = the 2 full days ending 48h before run time.
- e.g. run 2026-06-21 23:02 UTC → window 2026-06-17 to 2026-06-18.

## Reports / comparison
- Save to `reports/`: `ppc-2day-latest.md` + dated `ppc-2day-YYYY-MM-DD.md`.
- Compare against the previous `ppc-2day-*` dated file (not latest, which is
  overwritten). 2026-06-21 was the FIRST run — no prior 2-day report existed,
  so no comparison was possible.

## Delivery
- Google Drive folder name: "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Run history
- 2026-06-21: first run. Window 2026-06-17–18. **Result: ZERO SP activity in
  window** (0 impressions/clicks/spend/sales) — genuine, not an API error
  (confirmed via 30-day cross-check). Account spent ~$50/day through 2 June,
  then went dark; tiny blip 8–9 June; nothing from 10 June on. Only 2 of 50
  campaigns "enabled" and serving nothing. Likely out-of-stock/paused/budget.
  Notified user. No prior report → no Part C comparison. Lead ASIN in catalogue:
  B0FXW3GW5F (cat-deterrent / pet-odour). NEXT RUN: if still zero, re-flag; if
  spend resumed, compare 2-day metrics normally.
- TODO next run: campaign list /sp/campaigns/list only pulled first 50 (use
  pagination / nextToken if confirming enabled-campaign count matters).
