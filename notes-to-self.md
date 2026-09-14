# Notes to Self — PPC Analyst

Running log of lessons so future automated runs go smoothly. Newest lessons at the top.

## Environment / credentials
- **`AMZ_PROFILE_ID` env var is NOT a usable profile ID.** It holds
  `amzn1.application.dd42...` (an application ID). Do not pass it as the
  Advertising-API scope. Instead call `GET /v2/profiles` and pick by
  marketplace. As of 2026-09, the account has 3 seller profiles:
  - **US / USD → profileId `26765323558215`** ← use this one (primary FBA marketplace)
  - CA / CAD → `2840235221595557`
  - MX / MXN → `3892485344323414`
- Region endpoint that works from this environment: **NA only**
  (`advertising-api.amazon.com`). EU/FE hosts are blocked by the proxy
  (tunnel connection failed) — do not waste retries on them.
- Token exchange: `POST https://api.amazon.com/auth/o2/token` with the 4
  env vars works. Access token lasts ~1h; just re-fetch each run.
- Outbound HTTPS uses the agent proxy. Use CA bundle
  `/root/.ccr/ca-bundle.crt` as `verify=` in requests. Never disable TLS.

## Reporting API (v3) gotchas
- Endpoint: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- **Invalid columns:** `acosClicks7d` and `roasClicks7d` are NOT valid
  spCampaigns columns. There is no 7d ACOS/ROAS column. Pull `cost`,
  `sales7d`, `purchases7d` and **compute ACOS = cost/sales, ROAS =
  sales/cost, CTR = clicks/impr, CPC = cost/clicks** yourself.
- Valid computed-ish columns that DO work: `clickThroughRate`,
  `costPerClick`, `topOfSearchImpressionShare` (campaign-level only).
- Reports are async: create → poll `GET /reporting/reports/{id}` until
  `status=COMPLETED` → download the `url` (GZIP JSON). Polling can take
  a few minutes; a single report run can exceed a 120s shell timeout, so
  run the pull in the background.
- Attribution note: for a 2-day window only ~3–4 days old, 7-day
  attribution (`sales7d`/`purchases7d`) is not fully mature — later
  conversions may still land. Report the numbers as-is; they are the best
  available at run time.

## Report window logic
- 2-day report window = `[now-4days, now-2days)` (data lags 48h).
  Run 2026-09-14 → covered **2026-09-10 and 2026-09-11**.
- Previous 2-day report covers the 2 days before that. Compare against
  `reports/ppc-2day-latest.md` from the prior run. **First run 2026-09-14:
  no previous report existed, so no comparison was possible.**

## Delivery
- Save `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`,
  commit & push to branch `claude/great-hopper-ogikii`.
- Upload to Google Drive folder 'PPC Reports' (MCP Google-Drive tools).
- Email to uzoebo.archbold@gmail.com — check what email tool/connector is
  available; none was pre-confirmed at first run.
