# Notes to Self — PPC Analyst (automated reports)

Running log of lessons so each run gets smoother. Newest lessons on top.

## Environment / setup gotchas

- **`AMZ_PROFILE_ID` is NOT usable as-is.** The env var contains an Amazon
  *entity* ID (`amzn1…`, ~50 chars), not the numeric profile ID the Ads API
  scope header needs. Passing it literally to
  `Amazon-Advertising-API-Scope` returns HTTP 400 "profile ID required".
  - The account has 3 profiles under `GET /v2/profiles`: US, CA, MX.
  - **Use the US profile: `26765323558215`** (USD, real daily budget, live
    "Cat Deterrent Spray / Pet Odor" campaigns). CA & MX have placeholder
    budgets (9.99e8) and appear inactive.
  - TODO for owner: set `AMZ_PROFILE_ID` to `26765323558215` (numeric) so
    future runs don't have to resolve it.

- **Email step blocked.** The Gmail connector exists but is
  `enabledInChat: false` in this automated session, so there is NO email
  send tool available. Reports are saved to the repo and uploaded to Google
  Drive, but cannot be auto-emailed until Gmail is enabled for this
  workflow. State this clearly at the top of each report until fixed.

## Amazon Ads API — working recipe (v3)

1. Get token: `POST https://api.amazon.com/auth/o2/token` with
   grant_type=refresh_token + AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN. Token
   lasts 3600s.
2. Base URL: `https://advertising-api.amazon.com` (North America).
3. Headers: `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope`
   (= numeric profile ID), `Authorization: Bearer <token>`.
4. Reports are **async**: `POST /reporting/reports` → poll
   `GET /reporting/reports/{id}` until status COMPLETED → download the `url`
   (GZIP_JSON). Took ~30–60s in practice.
5. **Column gotchas (spCampaigns, SUMMARY timeUnit):**
   - `acosClicks30d` / `roasClicks30d` are **invalid** — only the 14d
     variants exist. Simplest to OMIT ACOS/ROAS columns and compute them
     yourself: ACOS = cost/sales, ROAS = sales/cost.
   - `date` is invalid for SUMMARY timeUnit (use startDate/endDate instead).
   - Valid useful columns: campaignId, campaignName, campaignStatus,
     impressions, topOfSearchImpressionShare, clicks, clickThroughRate,
     cost, costPerClick, purchases30d, sales30d.
   - `topOfSearchImpressionShare` returns as a percentage number (e.g.
     1.33 = 1.33%), and can be null when there are no impressions.
6. Report types used: `spCampaigns` (groupBy campaign),
   `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
   Search-term report is EMPTY when there are no clicks in the window.

## Report conventions

- 2-day window = the 2 full days ending 48h before run time. For a run on
  2026-08-23, that's 2026-08-20 & 2026-08-21.
- Save `reports/ppc-2day-latest.md` (overwrite) + dated copy
  `reports/ppc-2day-[run-date].md`. Commit both.
- Previous-report comparison: find the prior `ppc-2day-*.md` (excluding
  `latest`) to diff headline metrics. First run = baseline, nothing to
  compare.

## Data-state observations

- 2026-08-20/21: account essentially dormant — 74 impressions, 0 clicks,
  $0 spend, $0 sales across 19 campaigns (only 5 served). Root cause looks
  like very low daily budgets ($1.50–$2.50) and/or low bids. No wasted
  spend and no negatives/exact-match adds possible with zero clicks.
