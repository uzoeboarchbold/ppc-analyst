# PPC Analyst — Notes to Self

Running log of lessons so future runs go smoothly. Newest notes at top.

## Environment / API
- **AMZ_PROFILE_ID is MISCONFIGURED.** The env var holds an application-ID
  string (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric
  Amazon Ads profile ID. Do NOT pass it as the Scope header — it will fail.
  Resolve the real profile by calling `GET /v2/profiles` and picking the
  active seller account. As of 2026-08-05 the three profiles under seller
  "Uzoebo Archbold E-Commerce" (account A1C2I8MOP52E35) are:
    - US  26765323558215  (USD, dailyBudget $40  ← ACTIVE, use this one)
    - CA  2840235221595557 (CAD, placeholder max budget)
    - MX  3892485344323414 (MXN, placeholder max budget)
  We report on the **US** profile (only one with a real budget / active ads).
- **Region endpoint:** NA works (`advertising-api.amazon.com`). EU/FE are
  blocked by the proxy (403 CONNECT tunnel) — don't waste time on them.
- **Auth:** LWA token exchange at `https://api.amazon.com/auth/o2/token`
  with the four env creds works. Access token lasts ~60 min.

## Reporting API v3 (Sponsored Products)
- Endpoint: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`. Poll
  `GET /reporting/reports/{id}` until status=COMPLETED, then GET the `url`
  (a presigned S3 link, GZIP JSON). Reports are async (PENDING→COMPLETED).
- **ACOS / ROAS are NOT valid columns** at 7-day attribution. Only
  `acosClicks14d` / `roasClicks14d` exist. To keep a consistent 7-day window
  we pull `sales7d` + `purchases7d` + `cost` and compute ACOS = cost/sales,
  ROAS = sales/cost ourselves.
- `topOfSearchImpressionShare` IS available on spCampaigns (campaign level),
  but NOT on search-term/targeting reports.
- Report types used: `spCampaigns` (groupBy campaign) for Part A table;
  `spSearchTerm` (groupBy searchTerm) for negatives + exact-match candidates.

## Date window
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
  Run 2026-08-05 → covered 2026-08-01 and 2026-08-02.

## Reports / delivery
- Save reports/ppc-2day-latest.md + dated copy; commit to branch
  claude/great-hopper-jk7mbk. WORKS.
- Google Drive folder "PPC Reports" id=1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo.
  Upload via create_file with disableConversionToGoogleType=true. WORKS.
- **EMAIL STEP BLOCKED (2026-08-05).** The Gmail connector is installed for
  this org but shows `enabledInChat: false` — its tools are NOT loaded in the
  automated session, so there is NO way to send the email hands-off. Nothing to
  retry; it's a per-chat toggle a human must flip. ACTION FOR THE OWNER: enable
  the Gmail connector for this scheduled task's chat (connector settings), or
  wire an SMTP/API email path via env vars. Until then, delivery = Drive +
  git commit + the run's push notification. Don't waste cycles hunting for an
  email tool each run — check ListConnectors once; if still off, note & move on.
