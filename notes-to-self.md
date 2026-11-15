# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future automated runs go smoothly. Newest lessons at top.

## Environment & API setup (confirmed working 2026-11-15)

- **Auth works.** Token refresh: POST `https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token + AMZ_CLIENT_ID / AMZ_CLIENT_SECRET /
  AMZ_REFRESH_TOKEN. Access token lasts 3600s. Save it and reuse within the run.
- **Region is NA.** Use host `advertising-api.amazon.com`. EU and FE hosts are
  blocked by the egress proxy (403) and aren't needed.
- **All HTTPS must trust the proxy CA** at `/root/.ccr/ca-bundle.crt`. In Python,
  `ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")` + a ProxyHandler
  reading `HTTPS_PROXY`. `requests` is NOT installed — use urllib from stdlib.

- **IMPORTANT — AMZ_PROFILE_ID is wrong/unusable.** The env var holds an
  *application* ID (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a
  numeric advertising profile ID. It CANNOT be used as the
  `Amazon-Advertising-API-Scope` header. Resolve by calling `GET /v2/profiles` and
  picking the live account. The three profiles on this account:
    - US seller `26765323558215` (USD, daily budget $40) ← **use this one; the only active ad account**
    - CA seller `2840235221595557` (CAD, budget = default max → inactive)
    - MX seller `3892485344323414` (MXN, budget = default max → inactive)
  If a real numeric AMZ_PROFILE_ID is set in future, prefer it, but sanity-check it
  isn't an `amzn1.application.*` string first.

## Reporting API (v3) recipe that works

- Create: `POST /reporting/reports`, Content-Type
  `application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`,
  timeUnit `SUMMARY`, format `GZIP_JSON`. Columns used: campaignName, campaignId,
  impressions, clicks, cost, purchases7d, sales7d, topOfSearchImpressionShare.
- Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
- Poll `GET /reporting/reports/{id}` every 15s until status COMPLETED (took < 1 min
  each). Download the returned `url` (pre-signed, no auth header), gunzip, JSON.
- Campaign state/budget: `POST /sp/campaigns/list`, Content-Type
  `application/vnd.spCampaign.v3+json`. Gives state ENABLED/PAUSED/ARCHIVED + budget.

## Data situation as of 2026-11-15

- **Account is DARK.** 15 campaigns are ENABLED but served 0 impressions / 0 spend
  every day from 1 Nov through 12 Nov (checked a 14-day daily pull to confirm —
  not a window glitch, genuinely zero). Budgets are tiny (~$1.50/day).
- Likely cause: advertised product B0FXW3GW5F (cat deterrent spray / pet odor
  eliminator) is out of stock / lost Buy Box / suppressed, OR bids are below the
  auction clearing price. Reported this to the user as the headline.
- When the account is all-zero: the search-term report correctly returns 0 rows
  (no clicks → no terms). Don't treat that as an error. Report the zeros honestly;
  never invent numbers.
- **Watch for recovery:** next runs should check whether impressions have returned.
  If still zero, keep flagging it — this is the thing the owner needs to fix.

## Report bookkeeping

- Reports live in `reports/`. 2-day files: `ppc-2day-latest.md` (overwrite each run)
  + dated `ppc-2day-YYYY-MM-DD.md`. Previous 2-day report to compare against = the
  most recent dated `ppc-2day-*.md` before today's.
- Date window for 2-day report = (run_date − 4) and (run_date − 3), i.e. the 2 full
  days ending 48h before the run. For 2026-11-15 run → 11–12 Nov.
- Delivery: commit to repo (branch `claude/great-hopper-mbfcpl`), upload to Google
  Drive folder "PPC Reports" (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`),
  email to uzoebo.archbold@gmail.com.
- **EMAIL NOT POSSIBLE (2026-11-15):** no Gmail/email/SMTP tool is connected in
  this session — only Google-Drive, GitHub and agent tools. The report CANNOT be
  emailed automatically. Workaround used: delivered via repo commit + Drive upload,
  and sent the headline as a push notification to the owner. To enable email, the
  user needs to connect a Gmail (or other email) connector to these cloud sessions.
  Future runs: don't waste time re-searching; email stays unavailable until a
  connector is added. Still upload to Drive + commit, and push-notify the summary.
