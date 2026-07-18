# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest notes at top.

## Environment / credentials
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It contains an LWA *application* id
  (`amzn1.application....`), NOT a numeric Amazon Ads profile id. Do not use it
  as the `Amazon-Advertising-API-Scope`. Instead resolve the real profile by
  calling `GET https://advertising-api.amazon.com/v2/profiles`.
- Account = "Uzoebo Archbold E-Commerce" (seller id A1C2I8MOP52E35). Three
  profiles exist: US `26765323558215` (USD), CA `2840235221595557` (CAD),
  MX `3892485344323414` (MXN). **Use the US profile `26765323558215`** — it is
  the live one (real $40 daily account budget; CA/MX show placeholder budgets).
- Region = North America. Endpoint `https://advertising-api.amazon.com`.
  EU/FE endpoints are blocked by the proxy (403) and not needed.
- OAuth token refresh works: POST `https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token. Token lasts 3600s.

## Amazon Ads reporting API (v3, async)
- Flow: POST `/reporting/reports` -> poll GET `/reporting/reports/{id}` until
  status COMPLETED -> download the `url` (GZIP_JSON). Reports take ~30-60s.
- **spCampaigns report does NOT accept `acosClicks7d` / `roasClicks7d` columns.**
  Valid: campaignId, campaignName, impressions, topOfSearchImpressionShare,
  clicks, clickThroughRate, cost, costPerClick, purchases7d, sales7d.
  **Compute ACOS = cost/sales and ROAS = sales/cost yourself.**
- spTargeting (groupBy targeting) and spSearchTerm (groupBy searchTerm) accept
  acosClicks7d/roasClicks7d. When there is no delivery they return 0 rows.
- `topOfSearchImpressionShare` is null when impressions = 0.

## Account state (as of 2026-07-18 run)
- ~57 SP campaigns total but **only TWO are ENABLED**:
  `SP KT | ST w/ Sales` (51177386692133, $8/day) and
  `SP PT | ST w/ Sales` (258847863221155, $8/day).
  Everything else is PAUSED or ARCHIVED.
- **Both enabled campaigns delivered ZERO (impressions/clicks/spend/sales) for
  the whole trailing 30 days (Jun 16–Jul 15).** The SP account is effectively
  dark. If future runs still show all-zeros, this is a real account issue
  (bids too low to win impressions, ad groups paused, or out of stock), NOT an
  API bug. Keep flagging it until it changes.

## Reporting mechanics
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
  Cross-check with the previous run: 07-16 run covered 12–13 Jul, 07-18 run
  covers 14–15 Jul.
- Save reports/ppc-2day-latest.md + reports/ppc-2day-YYYY-MM-DD.md, commit,
  push to branch, upload to Google Drive folder "PPC Reports".
- **The repo's reports/ folder starts EMPTY on a fresh branch** — the real
  report history lives in the Google Drive "PPC Reports" folder
  (id 1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo). For the previous-report comparison,
  search that Drive folder and read the most recent ppc-2day-* doc. Prior
  2-day reports: 06-15, 06-18, 06-23, 06-24, 06-27, 07-10, 07-16 (12–13 Jul).
- **NO email tool is connected.** The task asks to email the report but there
  is no Gmail/SMTP tool available. Deliver the headline via PushNotification
  instead (reaches phone + inbox) and note in the report that email needs a
  connector added. Do NOT claim the email was sent.
- Dark-account context: the two enabled campaigns have been live since 9 June
  and have delivered zero every day since — an unbroken run of all-zeros 2-day
  reports. Keep flagging until impressions start.
