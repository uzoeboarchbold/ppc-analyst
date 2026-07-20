# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest first.

## 2026-07-20 (first run — 2-day report)

**Environment / auth**
- Refresh token, client id/secret all work. Token endpoint:
  `https://api.amazon.com/auth/o2/token`.
- Region is **NA**: `https://advertising-api.amazon.com`. EU and FE
  endpoints are BLOCKED by the network proxy (403 on CONNECT) — do not
  waste time trying them.

**IMPORTANT — AMZ_PROFILE_ID is misconfigured**
- The env var `AMZ_PROFILE_ID` holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an LWA *application* id, NOT a numeric advertising *profile* id.
  Passing it as the Ads API scope will fail.
- The account (`get /v2/profiles`) actually has THREE numeric seller
  profiles: CA `2840235221595557`, MX `3892485344323414`, US `26765323558215`.
- The **US** profile `26765323558215` is the active one (real daily budget
  $40, USD; CA/MX have placeholder 999999999 budgets). All PPC runs there.
- **Action for future runs:** ignore the bad env var, scope reports to
  `26765323558215`. Flag the misconfig at the top of every report until the
  owner fixes the env var. (Fix would be: set AMZ_PROFILE_ID=26765323558215.)

**Account state (2026-07-20)**
- ~50 campaigns exist; almost all PAUSED or ARCHIVED.
- Only TWO are ENABLED: `SP KT | ST w/ Sales` and `SP PT | ST w/ Sales`
  ($8/day each) — but both delivered ZERO impressions/clicks/spend for the
  whole of the last 4 weeks. So PPC is effectively OFF.
- Verified zero is REAL (pulled a 4-week window too — all zero), not an API
  error. Do not invent numbers; report zero honestly.

**Reporting API notes**
- Async reporting v3: POST `/reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`,
  body `configuration.adProduct=SPONSORED_PRODUCTS`, `timeUnit=SUMMARY`,
  `format=GZIP_JSON`, groupBy `["campaign"]` etc. Poll GET
  `/reporting/reports/{id}` until COMPLETED, then GET the `url` (gzip JSON).
- Campaign column for TOS share: `topOfSearchImpressionShare` (null when no
  impressions). Sales/purchases: `sales7d` / `purchases7d`.
- Reports complete fast (~30–60s) even for this account.

**Date window logic (2-day report)**
- Data lags ~48h. End window 48h before run, then take the 2 full calendar
  days before that cutoff. Run Mon 2026-07-20 23:03 UTC → cutoff Sat 07-18
  23:03 → covered **Jul 16 & Jul 17**.

**Delivery**
- Google Drive folder for uploads: "PPC Reports" (via Google-Drive MCP).
- Email report to uzoebo.archbold@gmail.com. (Check what email tool is
  available; note the result here next run.)
- Reports saved to repo `reports/`: `ppc-2day-latest.md` + dated copy.
- Previous 2-day report to compare against: NONE yet (this is the first).
