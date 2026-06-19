# Notes to Self — PPC Analyst

Running notes so future runs are faster and avoid repeating mistakes.

## Credentials & environment
- LWA token refresh works: `POST https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token, client_id, client_secret, refresh_token.
  Access token lasts 3600s.
- **IMPORTANT: `AMZ_PROFILE_ID` env var is WRONG.** It contains an
  *application* ID (`amzn1.application....`), not a profile ID. Do NOT pass it
  as the API scope. Instead use the numeric profile IDs below.
- Profiles on this account (from `GET /v2/profiles`, NA host):
  - **US = 26765323558215** (USD) ← primary, the only one with campaigns. USE THIS.
  - CA = 2840235221595557 (CAD) — no campaigns.
  - MX = 3892485344323414 (MXN) — no campaigns.
- Network allowlist: `advertising-api.amazon.com` (NA) and `api.amazon.com`
  WORK. `advertising-api-eu.amazon.com` and `-fe` are BLOCKED (403 host not in
  allowlist). Only NA is needed for this account.

## Reporting API (v3 async)
- Flow: `POST /reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`) → poll
  `GET /reporting/reports/{id}` until status COMPLETED → download `url`
  (GZIP_JSON). Headers need ClientId + Scope(=numeric profileId) + Bearer.
- Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
  Useful cols: impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases14d, sales14d,
  acosClicks14d, roasClicks14d, campaignName, campaignId, date.
- Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
- A SUMMARY report with **0 rows** = no impressions in the window.
  DAILY reports omit days that haven't been processed yet.

## Account state (as of 2026-06-19 run)
- Account is effectively DARK. 54 campaigns total; ~all PAUSED/ARCHIVED.
- Only 2 ENABLED campaigns, both started 2026-06-09:
  "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales".
- These two served impressions ONLY on 2026-06-09 (~78 + others, 0 clicks,
  $0 cost), then ZERO impressions every day 2026-06-10 .. 2026-06-14.
- No data rows at all for 2026-06-15/16 (our window) → no activity (and/or
  not-yet-finalised very-recent data). Last day with any data = 2026-06-14.
- Net: $0 spend, $0 sales for the window. Nothing to optimise; the real
  issue to flag is that enabled campaigns aren't serving.

## Data lag note
- 48h lag may not be enough for the very latest 1-2 days; some recent days
  return no rows until finalised. If window is empty, sanity-check with a
  wider window (DAILY) to see the last day that actually has data.

## Reports / comparison
- Save to `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`.
- Compare each new 2-day report against the previous `ppc-2day-latest.md`.
- 2026-06-19 was the FIRST run → no prior report to compare against.
</content>
</invoke>
