# Notes to self — PPC Analyst

Running log of lessons so each run goes smoother. Newest at top.

## 2026-10-22 (first run, 2-day report)
- **Repo started empty** (only README). Created `reports/` folder and this file.
- **Date window logic:** run time minus 48h, then take the 2 full *finalised* days.
  Run was 2026-10-22 23:10 UTC → window = **2026-10-18 to 2026-10-19**.
  (Oct 20 was not yet finalised at run time, so it was excluded.)
- **Auth works.** Token endpoint `https://api.amazon.com/auth/o2/token` with the
  4 env vars returns an access token (valid 3600s). Region endpoint for this
  account is **NA**: `https://advertising-api.amazon.com`. EU/FE hosts are blocked
  by the sandbox proxy (CONNECT 403) — don't bother trying them.
- **IMPORTANT — `AMZ_PROFILE_ID` is malformed.** The env var is an `amzn1...`
  opaque string (50 chars), NOT a numeric Ads profile id, and the API rejects it.
  Resolve the real profile from `GET /v2/profiles`. This account exposes 3:
    - US (USD): `26765323558215`  <-- the active FBA account (pet-odour products)
    - CA (CAD): `2840235221595557` (no SP campaigns)
    - MX (MXN): `3892485344323414` (no SP campaigns)
  Use **US `26765323558215`** until the env var is fixed. Flag this to the owner.
- **v2 SP endpoints are sunset** (`/v2/sp/campaigns` → 404 "Method Not Found").
  Use the **v3 async reporting API**: `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, poll
  `GET /reporting/reports/{id}` until COMPLETED, then download the gzipped JSON `url`.
- **Report column gotcha:** `acosClicks7d` / `roasClicks7d` are NOT valid columns
  for spCampaigns SUMMARY. Only `acosClicks14d`/`roasClicks14d` exist. Simplest:
  request `cost`, `sales7d`, `purchases7d` and compute ACOS (cost/sales) and
  ROAS (sales/cost) yourself. 7-day attribution is the SP standard.
- **Data finding:** All 15 US SP campaigns had ZERO impressions/clicks/spend/sales
  for the window AND for the trailing 30 days. The account is live but nothing is
  serving (campaigns paused, zero/exhausted budgets, or not yet launched). This is
  the real story to surface, not an error.
- **No prior 2-day report existed** → no comparison possible on this run. Next run
  compares against `reports/ppc-2day-latest.md`.
- Report delivery:
  - Repo `reports/` save + commit: WORKS.
  - Google Drive: WORKS. Folder 'PPC Reports' id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
    Upload with `create_file` (textContent, contentMimeType text/markdown,
    disableConversionToGoogleType true) and parentId set to that folder.
  - **EMAIL: NOT POSSIBLE in this environment.** There is no Gmail/email/SMTP tool
    connected — only Google-Drive and github MCP servers. The STEP 4 email to
    uzoebo.archbold@gmail.com could not be sent. To enable it, connect a Gmail (or
    other email) connector to the session. Until then, delivery is via the repo +
    Drive copy + the phone/email notification the run sends. Flagged to owner.
