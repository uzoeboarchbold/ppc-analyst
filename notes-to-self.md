# PPC Analyst — Notes to Self

Lessons learned across runs. Read this first, every run.

## Account / API facts (confirmed 2026-07-22)
- **AMZ_PROFILE_ID env var is MISCONFIGURED**: it holds an application ID
  (`amzn1.application...`), NOT a numeric Ads profile ID. Do NOT use it directly.
- The account (`Uzoebo Archbold E-Commerce`, seller A1C2I8MOP52E35) has 3 profiles,
  all in the **NA region** (`https://advertising-api.amazon.com`):
  - CA (2840235221595557, CAD) — 0 SP campaigns
  - MX (3892485344323414, MXN) — 0 SP campaigns
  - **US (26765323558215, USD) — the ACTIVE one. 54 SP campaigns. USE THIS.**
- EU and FE region endpoints are blocked by the proxy (403). NA works fine.
- Auth: refresh-token grant at `https://api.amazon.com/auth/o2/token` works.
  Access token lasts 3600s.

## How to pull data
- Use v3 async reporting: `POST /reporting/reports` then poll
  `GET /reporting/reports/{id}` until status COMPLETED, download the gzip url.
- Content-Type for create: `application/vnd.createasyncreportrequest.v3+json`.
- Report types used: spCampaigns (groupBy campaign), spTargeting (groupBy targeting),
  spSearchTerm (groupBy searchTerm).
- `topOfSearchImpressionShare` is available on spCampaigns.
- Attribution: using **7-day** (purchases7d / sales7d) as the headline. NOTE: for a
  window ending only ~2 days ago, 7-day attribution is NOT fully mature, so recent
  sales/purchases may tick up in later runs. Keep the same window for consistency.
- CTR, CPC, ACOS, ROAS computed locally from impressions/clicks/cost/sales/purchases.

## Date window logic (data lags 48h)
- Most recent finalized full day D satisfies: D+3 (00:00) <= now. i.e. D <= today-3days.
- 2-day report = that day and the one before it.
- Example: run Wed 2026-07-22 -> cover Sat 2026-07-18 & Sun 2026-07-19.

## Reports / delivery
- Save to `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-YYYY-MM-DD.md`.
- Commit to branch `claude/great-hopper-q6szrp`.
- Google Drive: folder 'PPC Reports' id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload works
  (uploads convert to a Google Doc — fine).
- **EMAIL CANNOT BE SENT AUTOMATICALLY YET.** The Gmail connector is installed but
  `enabledInChat: false` for this scheduled session, so its tools don't load and there is
  no send-email capability. An automated run can't toggle it. FIX: the account owner must
  enable the Gmail connector for this scheduled session in the chat's connector settings.
  Until then, report is delivered via repo + Drive only, and the run sends a push
  notification instead of the email.
- Compare against previous 2-day report (previous `ppc-2day-*.md`). First run = no baseline.

## Root-cause diagnosis toolkit (if account shows zero delivery)
- Check enabled campaigns' keywords (`POST /sp/keywords/list`), targets (`/sp/targets/list`),
  and product ads (`/sp/productAds/list`). If all ENABLED with sensible bids but zero
  impressions -> the ADVERTISED PRODUCT is ineligible (out of stock / lost Buy Box /
  suppressed listing), NOT an ad-settings problem. Don't recommend bid/budget changes.

## Run history
- 2026-07-22: FIRST RUN. Baseline established. Account is DARK: both enabled campaigns
  (51177386692133 "SP KT", 258847863221155 "SP PT") delivered ZERO impressions/clicks/
  spend/sales for the window AND for a 30-day cross-check. Config is healthy (16 keywords,
  3 ASIN targets, $8/day budgets). Sole advertised ASIN = B0FXW3GW5F (cat deterrent / pet
  odour). Likely out of stock / lost Buy Box. Email not sent (Gmail disabled in chat) ->
  used push notification.
