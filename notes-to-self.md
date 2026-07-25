# Notes to Self — PPC Analyst routine

Running log of lessons so future runs are faster and more reliable. Newest notes at top.

## Account facts (stable)
- Business: **Uzoebo Archbold E-Commerce**, Amazon **US** Sponsored Products, USD.
- **Correct Ads profile ID = `26765323558215`** (US seller). USE THIS.
- The `AMZ_PROFILE_ID` env var holds an **application ID** (`amzn1.application.…`), NOT a
  numeric ads-profile ID. It is wrong every run. Do not use it — hardcode/derive the
  numeric US profile from `/v2/profiles` instead. (CA profile 2840235221595557 and
  MX profile 3892485344323414 exist but are empty placeholders — ignore.)
- Only NA API host works: `https://advertising-api.amazon.com`. **EU/FE hosts are
  blocked** by the environment proxy (CONNECT tunnel 403) — don't bother; US is NA anyway.
- Account catalogue centres on ASIN **B0FXW3GW5F** (cat-deterrent / pet-odour eliminator).
- Of ~54 campaigns, only 2 are ENABLED: "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"
  (~$8/day each). All others paused/archived.

## The big ongoing situation
- **The account has been DARK since ~9–10 June 2026.** Every 2-day report since mid-June
  reads all zeros (0 impressions / 0 clicks / $0 spend / $0 sales). The 2 enabled campaigns
  serve 0 impressions despite funded budgets. This is a status/delivery problem, not a
  performance one. Likely causes: bids too low to win auctions, something paused one level
  down (ad group / product ad / target), or the product not buyable (stock / Buy Box /
  suppressed listing). Keep flagging until it changes.

## Credentials / auth
- OAuth refresh works: POST `https://api.amazon.com/auth/o2/token` with grant_type=
  refresh_token + client_id + client_secret + refresh_token. Returns 1h access token.
- Env length check gotcha: `${#VAR}` in bash measures the *name* not the value if you pass
  the name as a string — verify by printing the actual value.

## Reporting API (v3)
- Use v3 async reports: POST `/reporting/reports` with content-type
  `application/vnd.createasyncreportrequest.v3+json`. Report types used:
  `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). timeUnit SUMMARY, format GZIP_JSON.
- topOfSearchImpressionShare column is available on spCampaigns.
- **Reports can take a LONG time to move from PENDING → COMPLETED (often >10 min, sometimes
  much more).** Poll patiently (20s interval, allow ~20+ min). When the account is dark the
  reports still complete and just return 0 rows.
- Metric columns: cost, purchases30d, sales30d, clicks, impressions, clickThroughRate,
  costPerClick, acosClicks14d, roasClicks14d.

## Delivery (save / Drive / email)
- Google Drive "PPC Reports" folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload the
  report there each run (prior runs land as Google Docs — fine).
- Repo: save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`,
  commit & push to branch `claude/great-hopper-h1lv6r`.
- **Email: no working Gmail/send-email tool has been available in past automated runs.** If
  still unavailable, deliver the headline via PushNotification and note email couldn't be
  sent. Check each run in case a connector was added.
- Previous 2-day report to compare against lives in the Drive folder (titled
  "PPC 2-Day Report — <dates>"). The repo reports/ folder starts empty each fresh container,
  so pull the prior baseline from Drive if the repo has none.
