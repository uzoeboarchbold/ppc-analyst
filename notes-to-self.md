# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future automated runs are faster and more reliable.
Newest lessons at the top of each section.

## Environment / setup
- Python `requests` is NOT pre-installed. Install with `python3 -m pip install requests`
  (plain `pip install requests` installed to a different interpreter and the import failed).
- Do NOT run my own scripts with `python3 -I` — `-I` ignores site-packages, so `requests`
  won't import. `-I` is only for running scripts that read untrusted downloaded files.
- Outbound HTTPS goes through an agent proxy; `requests` picks up the CA bundle and proxy
  from env vars automatically (REQUESTS_CA_BUNDLE, HTTPS_PROXY are pre-set). No extra config.
- Only the **NA** Amazon Ads endpoint (`https://advertising-api.amazon.com`) is reachable.
  EU (`-eu`) and FE (`-fe`) endpoints are BLOCKED by the proxy (403). Our account is NA, fine.
- Python `print()` to a redirected file is block-buffered — output only appears at process
  exit. Use `python3 -u` (unbuffered) when backgrounding so I can read interim output.

## Amazon Ads API — credentials & account
- Auth works: LWA token endpoint `https://api.amazon.com/auth/o2/token` with
  AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN → access_token (valid ~1h).
- **AMZ_PROFILE_ID is MISCONFIGURED.** It holds an application-id string
  (`amzn1.application.xxxxxxxx`), NOT a numeric Amazon Ads profile id. It does not match
  any real profile. I discovered the real profiles via `GET /v2/profiles`.
- Real profiles on this account (all SELLER):
  - `2840235221595557` — CA — EMPTY (0 campaigns)
  - `3892485344323414` — MX — EMPTY (0 campaigns)
  - `26765323558215`  — **US** — the live account. Use THIS profile id as the
    `Amazon-Advertising-API-Scope` header until AMZ_PROFILE_ID is fixed.
  ACTION FOR OWNER: set AMZ_PROFILE_ID to `26765323558215` (US) so runs don't have to
  auto-detect. Until then, this script hard-selects the US profile by elimination.

## Reporting API (SP v3)
- Create: `POST /reporting/reports`, Content-Type
  `application/vnd.createasyncreportrequest.v3+json`. Poll `GET /reporting/reports/{id}`
  until status COMPLETED, then download the presigned `url` (GZIP JSON).
- `spCampaigns` report does NOT allow `acosClicks7d` / `roasClicks7d` columns (400 error).
  Only 14d versions exist (`acosClicks14d`, `roasClicks14d`). I compute ACOS & ROAS myself
  from `cost` and `sales7d`: ACOS = cost/sales7d, ROAS = sales7d/cost. Use 7d attribution
  for headline sales/purchases (`sales7d`, `purchases7d`).
- Valid-ish column set that works: campaignName, campaignId, campaignStatus,
  campaignBudgetCurrencyCode, impressions, clicks, cost, purchases7d, sales7d,
  clickThroughRate, costPerClick, topOfSearchImpressionShare.
- A SUMMARY report returns NO rows for a window where campaigns served nothing (0 rows ≠
  error). Confirm "no activity" by also pulling a wider window and listing campaigns.

## Date window
- Data lags ~48h. 2-day report covers the 2 fully-finalised days ending at (now-48h),
  rounded to day boundary. A day is finalised when day+1 00:00 ≤ now-48h.

## Account status observations (update each run)
- 2026-11-26 run (covering Nov 22–23): US account has 15 SP campaigns but ZERO delivery —
  0 impressions / clicks / cost / sales for the window AND for the trailing 30 days.
  Campaigns appear to be not serving (likely paused or never launched / tiny $1.50 budgets).
  No spend = nothing to optimise yet; the real issue is ads not running.
