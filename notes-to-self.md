# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work smoothly. Newest at top.

## Environment / setup facts (confirmed 2026-07-13)
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It contains an application ARN
  (`amzn1.application...`), NOT a numeric Amazon Ads profile ID. Do not pass it
  as the `Amazon-Advertising-API-Scope` header — it will not work.
- The real profiles (from `GET /v2/profiles` on the NA endpoint) are:
  - **US = `26765323558215`** ← primary FBA marketplace, use this one
  - CA = `2840235221595557`
  - MX = `3892485344323414`
  - Account name: "Uzoebo Archbold E-Commerce"
- Region endpoint = **NA** (`advertising-api.amazon.com`). The EU and FE
  endpoints are blocked by the egress proxy (403), and we have no profiles there
  anyway, so NA is correct.
- Auth: token endpoint `https://api.amazon.com/auth/o2/token` with the four
  AMZ_* env vars works. Access token lives ~60 min.
- Networking: outbound HTTPS goes through a proxy. Set
  `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt` for python urllib/requests or
  TLS verification fails.

## Reporting API (v3) lessons
- Use POST `/reporting/reports` (async). Reports are PENDING for several
  minutes — poll every ~20s and refresh the access token inside the loop
  (a single shell call times out at 2 min; run the poller in the background).
- Reports used: `spCampaigns` (groupBy campaign, has topOfSearchImpressionShare),
  `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
- Attribution window: using 14-day (purchases14d/sales14d/acosClicks14d/
  roasClicks14d). NOTE: for a 2-day window ending 48h ago, the 14-day
  attribution is still maturing, so purchases/sales may tick up in later runs.

## Date window rule
- Data lags ~48h. 2-day report covers the 2 full days ending at the day BEFORE
  the (now − 48h) boundary. E.g. run 2026-07-13 → window 2026-07-09..07-10.

## Report/output locations
- Save `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-[date].md`.
- Google Drive folder: "PPC Reports" = id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
- **EMAIL NOT POSSIBLE YET:** no email/Gmail connector is available in this
  environment (only Google-Drive and github MCP servers are connected). Cannot
  send the email step automatically. Workaround used: deliver via repo commit +
  Drive upload, and alert the owner with a push notification. To enable real
  email, a Gmail/SMTP connector needs to be added to the session.

## Campaign-state check is worth doing
- The reporting API's spCampaigns SUMMARY only returned the ENABLED campaigns.
  To understand WHY numbers are zero, also call POST `/sp/campaigns/list`
  (headers `Content-Type`/`Accept: application/vnd.spCampaign.v3+json`) to see
  state + budget per campaign. That's how we found 52/54 campaigns paused.

## History
- 2026-07-13: First run of the 2-day report. No previous 2-day report existed,
  so no comparison was possible this time (Part C notes this). Established all
  the facts above.
  KEY FINDING: account is effectively dark on Sponsored Products. Only 2 of 54
  campaigns are ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day
  each, started 2026-06-09), and even those served 0 impressions over 30 days.
  $0 spend, $0 sales, no clicks. Nothing to optimise until ads actually serve —
  likely bids too low, inner ad group/ad/targets paused, or ASIN not buyable.
  Watch for this staying zero in future runs.
