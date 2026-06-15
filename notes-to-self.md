# Notes to Self — PPC Analyst

Lessons learned across runs. Read this first every run and apply.

## Account / credentials
- **AMZ_PROFILE_ID is misconfigured.** It holds an LWA *application* ID
  (`amzn1.application.…`), NOT a numeric Ads profile ID. The reporting API needs
  the numeric profile in the `Amazon-Advertising-API-Scope` header.
  - Resolve numeric profiles via `GET /v2/profiles` on the NA host.
  - **Use US profile `26765323558215`** — it is the only one with campaigns.
  - Other profiles (no campaigns): Canada `2840235221595557`, Mexico `3892485344323414`.
  - All three are "Uzoebo Archbold E-Commerce".
- Token exchange: `POST https://api.amazon.com/auth/o2/token` with refresh_token
  grant works fine. Access token lasts ~1h.

## Network / region
- Only the **NA** Ads host is allowed by egress policy:
  `advertising-api.amazon.com`. The EU (`-eu`) and FE (`-fe`) hosts are
  **blocked** ("Host not in allowlist"). US account lives on NA, so this is fine.

## Reporting API (v3) — what works
- Create: `POST /reporting/reports` with Content-Type/Accept
  `application/vnd.createasyncreportrequest.v3+json`.
- Poll: `GET /reporting/reports/{id}` until status COMPLETED, then download the
  `url` (GZIP_JSON). Reports took ~30–90s to finish.
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting` (groupBy
  targeting), `spSearchTerm` (groupBy searchTerm). All accept SUMMARY timeUnit.
- Useful columns: impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases14d, sales14d, acosClicks14d,
  roasClicks14d.

## Known business issue (flag until fixed)
- **No valid payment method** on the account (`validPaymentMethod = none` for all
  profiles). As of the 2026-06-15 run, ads were serving ZERO impressions/spend.
  Almost certainly the cause of zero delivery. Keep flagging until real spend
  appears in the data.

## Email
- **No email/Gmail tool is connected** in this environment, so the "email the
  report" step cannot run automatically. Report is still saved to repo + Google
  Drive, and a push notification is sent. If email becomes required, an email
  integration must be added.

## Date window (2-day report)
- Data lags ~48h. Window = the 2 full days ending 48h before run time.
- Run 2026-06-15 23:03 UTC → covered 11 Jun & 12 Jun 2026.

## Report locations
- `reports/ppc-2day-latest.md` (overwrite each run) + `reports/ppc-2day-[date].md`.
- Google Drive folder: "PPC Reports".
