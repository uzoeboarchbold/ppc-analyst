# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Environment / API setup
- **Auth:** POST `https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token`,
  `refresh_token=$AMZ_REFRESH_TOKEN`, `client_id=$AMZ_CLIENT_ID`, `client_secret=$AMZ_CLIENT_SECRET`.
  Access token lasts 3600s. Refresh each run.
- **Region:** Account lives on the **NA** endpoint `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the proxy (403) anyway.
- **IMPORTANT — Profile ID:** The env var `AMZ_PROFILE_ID` contains an *application* id
  (`amzn1.application.…`), which is NOT a valid `Amazon-Advertising-API-Scope` value.
  The Scope header needs a **numeric profileId**. Get profiles via
  `GET /v2/profiles`. This account has 3:
    - CA `2840235221595557` (default max budget — inactive)
    - MX `3892485344323414` (default max budget — inactive)
    - **US `26765323558215` (daily budget $40 — the ACTIVE advertising marketplace) ← use this**
  Currency: USD.

## Reporting API v3 (async)
- Create: POST `/reporting/reports`, header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Poll: GET `/reporting/reports/{reportId}` until `status=COMPLETED`, then download `url` (GZIP JSON).
- **Valid ACOS/ROAS columns are only 14d** (`acosClicks14d`, `roasClicks14d`) — there is no 7d version.
  To keep ACOS/ROAS consistent with 7-day sales/purchases, **compute them ourselves**:
  ACOS = cost / sales7d; ROAS = sales7d / cost.
- Campaign report (`spCampaigns`, groupBy `["campaign"]`, SUMMARY) supports
  `topOfSearchImpressionShare`. Good columns:
  campaignName, campaignId, campaignStatus, impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare, clickThroughRate, costPerClick.
- Search-term report: `spSearchTerm`, groupBy `["searchTerm"]`.

## Date window logic
- Data lags ~48h. 2-day report covers the **2 full days ending 48h before run**.
- Run 2026-07-15 → covered **2026-07-11 and 2026-07-12**.

## Comparison
- Compare each report against the previous report of the SAME type in `reports/`.
- 2-day-latest file: `reports/ppc-2day-latest.md`; dated copies `reports/ppc-2day-YYYY-MM-DD.md`.

## Where previous reports live
- The git repo starts FRESH each session (only "Initial commit"), so `reports/` is
  usually empty at start. **Prior reports are in Google Drive** folder 'PPC Reports'
  (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Search that folder for the latest
  `ppc-2day-*` doc to get the previous 2-day report for comparison.

## Delivery
- **No email tool is connected** in this environment (only Google-Drive + github MCP).
  So the "email to uzoebo.archbold@gmail.com" step cannot run. Deliver via: save to
  repo, upload to Drive 'PPC Reports', and send a PushNotification with the headline.
  Every prior run hit this same wall — don't waste time re-searching for an email tool.

## Account status (standing issue)
- Account has been effectively DARK since ~10 June 2026. Only 2 campaigns enabled
  ("SP KT | ST w/ Sales" #51177386692133, "SP PT | ST w/ Sales" #258847863221155,
  $8/day each, live since 9 June); both serve 0 impressions. ~52 others paused/archived.
  Likely bids too low / internal paused state / Buy Box / stock. Human action needed.
  If still zero next run, this is expected — report it flat, don't re-diagnose from scratch.

## Reporting API timing
- Async reports can take 10–20+ min to move PENDING→COMPLETED when the queue is slow.
  Run the poller in the background so the session isn't blocked.

## History
- 2026-07-15: Ran 2-day report for 11–12 Jul. All zeros again (account still dark ~5 wks).
  Compared vs previous 2-day report (10–11 Jul, from Drive) — flat at zero, no change.
  Established the repo reports folder + this notes file (both were missing at start).
