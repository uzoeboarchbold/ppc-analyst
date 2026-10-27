# Notes to Self — PPC Analyst

Running log of lessons so each run goes smoother. Newest notes at top.

## Account / environment facts (confirmed 2026-10-27)
- **Credentials work.** `AMZ_CLIENT_ID / SECRET / REFRESH_TOKEN` are valid. Token
  refresh endpoint: `POST https://api.amazon.com/auth/o2/token` (grant_type=refresh_token).
  Access tokens last 3600s — refresh at the start of every run.
- **`AMZ_PROFILE_ID` env var is NOT usable.** It is set to an *application* ID
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not the numeric profile ID
  the Ads API needs in the `Amazon-Advertising-API-Scope` header. **Ignore it.**
- **Correct region = NA**: `https://advertising-api.amazon.com`. The proxy BLOCKS
  EU and FE hosts (403 CONNECT tunnel) — do not try them.
- **Three profiles exist** under seller "Uzoebo Archbold E-Commerce" (seller A1C2I8MOP52E35):
  - US `26765323558215` (USD)  ← **THE ACTIVE ONE: 54 SP campaigns**
  - CA `2840235221595557` (CAD) — 0 campaigns
  - MX `3892485344323414` (MXN) — 0 campaigns
  - **Always report on the US profile `26765323558215`.**
- Product line so far: pet odor eliminator / cat deterrent spray, ASIN B0FXW3GW5F.

## Reporting API notes
- Use v3 reporting: `POST /reporting/reports`, poll `GET /reporting/reports/{id}`,
  download the gzip `url`, gunzip, parse JSON.
- `topOfSearchImpressionShare` is a campaign-level column (works with groupBy=campaign, SUMMARY).
- Report type IDs: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm). Purchases/sales columns: `purchases30d`, `sales30d`,
  `acosClicks30d`, `roasClicks30d`.
- Reports can take 30s–several minutes. Create all needed reports first, then poll.

## Date window logic (data lags 48h)
- boundary = now − 48h. Covered days = (boundary_date − 2) and (boundary_date − 1).
- Verified with example: run Sun 00:00 → covers Wed + Thu.

## BIG FINDING — account is NOT delivering (as of 2026-10-27)
- The US account returned **0 impressions / 0 clicks / 0 cost / 0 sales** for the
  2-day window AND for the entire last 30 days. Data pulled fine — the zeros are real.
- Campaign states: 15 ENABLED (tiny budgets $1.50–$2.50/day), 32 PAUSED, 7 ARCHIVED.
- Root cause is almost certainly `validPaymentMethod = false` on the US profile —
  Amazon won't serve ads without a valid payment method. Flag this at the TOP of
  every report until it's fixed and impressions appear. Check `validPaymentMethod`
  each run via `GET /v2/profiles/26765323558215`.
- Reporting columns `acosClicks30d` / `roasClicks30d` are INVALID for spCampaigns.
  Valid: impressions, clicks, cost, costPerClick, purchases30d, sales30d,
  topOfSearchImpressionShare, clickThroughRate. **Compute ACOS = cost/sales and
  ROAS = sales/cost yourself.** (acosClicks14d / roasClicks14d do exist if needed.)
- Report create header content-type: `application/vnd.createasyncreportrequest.v3+json`.

## EMAIL step — blocked in automated runs (2026-10-27)
- Gmail connector IS installed & connected at org level, but `enabledInChat = false`
  in this session, so NO Gmail tools load and the report cannot be emailed from here.
  Google Drive connector IS enabled in chat and works (upload confirmed).
- Workaround until fixed: deliver findings via PushNotification (phone + email inbox),
  and rely on the Drive upload + committed repo file. To enable true emailing, the
  user needs to allow the Gmail connector's tools in this Claude Code session's
  connector settings. Re-check each run with ListConnectors.
- Drive 'PPC Reports' folder id: `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.

## Report history
- 2026-10-27: first ever run. No prior 2-day report existed, so compared current
  window (10-23/10-24) against previous window (10-21/10-22) pulled live from API.
  Result: zero delivery everywhere (billing/payment issue). Report saved + committed.
