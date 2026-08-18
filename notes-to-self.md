# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest at top.

## 2026-08-18 (first run, 2-day report)
- **Repo started empty** (only README). Created `reports/` folder and this file.
- **AMZ_PROFILE_ID env is NOT a usable scope.** It is set to an
  `amzn1.application.â€¦` string, which the Ads API rejects as a profile scope.
  The real numeric profile IDs come from `GET /v2/profiles`. This account has 3:
  - CA `2840235221595557` (CAD, default max budget)
  - MX `3892485344323414` (MXN, default max budget)
  - **US `26765323558215` (USD, daily budget $40) â† ACTIVE. Use this one.**
  The US profile is the only one with a real configured budget and is the live
  FBA marketplace. Hard-coded US for now. If numbers ever look wrong, re-check
  `/v2/profiles` and confirm which profile is active.
- **Region = NA** (`https://advertising-api.amazon.com`). EU/FE endpoints are
  blocked by the proxy (403) and are not needed.
- **Auth flow that works:** POST `https://api.amazon.com/auth/o2/token` with
  refresh_token grant â†’ access_token (1h). All requests go through the agent
  proxy: `proxies={"https": os.environ["HTTPS_PROXY"]}`, `verify=/root/.ccr/ca-bundle.crt`.
- **Reporting API = v3 async.** POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), poll
  `GET /reporting/reports/{id}` until `COMPLETED`, download the gzipped-JSON url.
  Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm). 14-day attribution
  columns (`purchases14d`, `sales14d`, `acosClicks14d`, `roasClicks14d`).
  `topOfSearchImpressionShare` is available on the campaign report.
  Reports completed in well under a minute.
- **Date window (2-day):** run day minus 4 and minus 3 (matches the brief's
  "run Sunday â†’ cover Wed & Thu"). Run 2026-08-18 (Tue) â†’ covered Fri 08-14 & Sat 08-15.
- **Traffic is currently tiny.** The whole 2-day window: 77 impressions, 1 click,
  $2.16 spend, 0 sales. Don't over-interpret single clicks; there is not enough
  volume yet to recommend negatives or new exact-match keywords with confidence.
- **Google Drive folder** for uploads: "PPC Reports". Email goes to
  uzoebo.archbold@gmail.com.
- **No previous 2-day report existed** for comparison this run. Next run compares
  against `reports/ppc-2day-latest.md`.
