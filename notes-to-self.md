# Notes to Self — PPC Analyst (automated runs)

Running log of lessons so future runs are faster and more reliable. Newest at top.

## Account / environment facts (verified 2026-08-06)
- **Seller:** Uzoebo Archbold E-Commerce (advertiser id `A1C2I8MOP52E35`).
- **Region:** North America → API base `https://advertising-api.amazon.com`.
  (EU/FE hosts are blocked by the outbound proxy — don't bother probing them.)
- **Profiles available (all `seller` type, same advertiser):**
  - `26765323558215` → **US** (amazon.com, USD, $40/day budget) ← **USE THIS**. It's the only actively-managed marketplace.
  - `2840235221595557` → CA (CAD, placeholder max budget, effectively inactive).
  - `3892485344323414` → MX (MXN, placeholder max budget, effectively inactive).

## ⚠️ Known issue: AMZ_PROFILE_ID is misconfigured
- The `AMZ_PROFILE_ID` env var contains an LWA **application** id
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric Ads
  profile id. Passing it as the API scope will fail.
- **Workaround that works:** ignore that env var's value; call `GET /v2/profiles`
  and select profile `26765323558215` (US). Flag the misconfig at the top of the
  report each run until the owner fixes the env var to `26765323558215`.
- The other three creds (`AMZ_CLIENT_ID` = `amzn1.application-oa2-…`,
  `AMZ_CLIENT_SECRET` = `amzn1.oa2-cs.v1…`, `AMZ_REFRESH_TOKEN` = `Atzr|…`) are
  all correctly formatted and authenticate fine.

## How to pull the data (working recipe)
1. **Token:** POST `https://api.amazon.com/auth/o2/token`,
   `grant_type=refresh_token` + client_id/secret/refresh_token → `access_token`
   (valid ~1h). Works first try.
2. **Reports (Ads API v3 async):** POST `/reporting/reports` with headers
   `Authorization: Bearer`, `Amazon-Advertising-API-ClientId`,
   `Amazon-Advertising-API-Scope=26765323558215`, and
   `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
   - Campaigns: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`, columns incl.
     `impressions,clicks,cost,costPerClick,clickThroughRate,purchases7d,sales7d,topOfSearchImpressionShare,campaignName,campaignId`.
   - Targets: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
   - Search terms: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`.
   - `timeUnit=SUMMARY`, `format=GZIP_JSON`.
3. **Poll** `GET /reporting/reports/{id}` every ~15s until `status=COMPLETED`
   (took ~30–60s), then download the presigned `url` (S3, **no auth headers**),
   gunzip, parse JSON. All three completed cleanly on 2026-08-06.
- Derive CTR=clicks/impr, CPC=cost/clicks, ACOS=cost/sales, ROAS=sales/cost
  yourself (show "—" for ACOS when sales=0).
- `topOfSearchImpressionShare` is `null` when a campaign served 0 impressions.

## Date window (2-day report)
- Data lags ~48h. Cover the 2 full finalised days ending ≥48h before run.
- 2026-08-06 23:07 UTC run → window **Aug 2–3, 2026**. (Aug 4 not yet finalised.)

## ⚠️ Known issue: email step can't run in automated sessions
- The **Gmail** connector is installed at org level but shows `enabledInChat:false`
  in these scheduled runs, so no Gmail send/draft tool loads — the "email it to
  uzoebo.archbold@gmail.com" step **cannot be completed automatically**.
- **Google Drive** connector IS enabled in-chat and works (upload confirmed).
- Workaround for now: save to repo + upload to the "PPC Reports" Drive folder
  (both done), and flag in the report + notify the owner that email was skipped.
  To fix permanently: enable the Gmail connector for the scheduled session, or
  provide SMTP creds as env vars so the report can be emailed via a script.

## Report bookkeeping
- Save `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`.
- **Previous 2-day report to compare against next time:** `ppc-2day-2026-08-06.md`
  (baseline: 70 impr, 1 click, $2.84 spend, 0 sales, ROAS 0).
- Google Drive folder: **"PPC Reports"**. Email to uzoebo.archbold@gmail.com,
  subject `PPC 2-Day Report — [dates]`.

## Observations / watch-items
- 2026-08-06: Account badly **under-delivering** — $2.84 spent over 2 days vs a
  $40/day budget, only 70 impressions, 1 click, no sales. Likely low bids / paused
  campaigns rather than an efficiency problem. If this persists, the headline of
  each report should be the delivery gap, not ACOS/ROAS. Nothing to add as
  negatives or harvest as exact-match yet (no conversions).
