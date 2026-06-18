# Notes to self — PPC Analyst (read before every run)

## Account / API facts (confirmed 2026-06-18)
- Amazon Ads API works with the env credentials. Token endpoint: `https://api.amazon.com/auth/o2/token` (refresh_token grant). Token lasts 3600s.
- Region endpoint: **`https://advertising-api.amazon.com`** (North America). The EU/FE hosts are NOT in the network allowlist — do not bother trying them.
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It contains `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` (an application ID), NOT a numeric profile ID. Do not pass it as the Scope header — the API needs a numeric profile.
  - Real profiles on this account (from `GET /v2/profiles`):
    - **US (USD): `26765323558215`** ← use this one (US FBA business).
    - CA (CAD): 2840235221595557
    - MX (MXN): 3892485344323414
  - Until the env var is fixed, hardcode/scope to `26765323558215`.

## Reporting API gotchas (v3 `/reporting/reports`)
- Content-Type for create: `application/vnd.createasyncreportrequest.v3+json`.
- spCampaigns report: **`acosClicks7d` and `roasClicks7d` are NOT valid columns** — only 14d variants exist (`acosClicks14d`, `roasClicks14d`). Easiest: pull `cost`, `sales7d`, `purchases7d` and compute ACOS (=cost/sales) and ROAS (=sales/cost) yourself.
- `topOfSearchImpressionShare` IS valid for spCampaigns and requires `timeUnit: SUMMARY` (no `date` column with it).
- spSearchTerm report only returns rows when there were clicks/conversions. Empty result = no clicks, not an error.
- Poll the report (status COMPLETED/SUCCESS) then download the gzipped JSON from the returned `url`.

## Standing situation (as of 2026-06-18)
- Account is effectively **dormant**: only 2 campaigns ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", both $8/day, started 2026-06-09), and they win ~0 impressions. ~53 other campaigns PAUSED/ARCHIVED.
- Expect **$0 spend / $0 sales** reports until the owner re-enables campaigns or raises bids. If a future report suddenly shows activity, that's a real change worth highlighting.

## Date window logic (data lags 48h)
- 2-day report: cover the 2 full days ending 48h before run. Practically: run day minus 4 and run day minus 3. (Run 2026-06-18 → covered 2026-06-14 and 2026-06-15.)

## Previous report locations
- `reports/ppc-2day-latest.md` = newest; dated copies `reports/ppc-2day-YYYY-MM-DD.md`. Compare new run against the most recent prior dated copy.
