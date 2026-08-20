# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each automated run gets smarter. Newest at top.

## Environment / API
- **`AMZ_PROFILE_ID` is misconfigured.** It contains an *application ID*
  (`amzn1.application....`), NOT a numeric advertising profile ID. Do not pass
  it as the `Amazon-Advertising-API-Scope`. Instead use the correct profile:
  - **Use profile `26765323558215` (US, USD, $40/day budget)** — the only
    actively funded profile.
  - Other profiles on this account: `2840235221595557` (CA), `3892485344323414`
    (MX) — both have placeholder budgets (999999999) and no real activity.
  - Owner should fix the env var to `26765323558215`. Until then, hardcode US.
- **Region = North America.** Host `advertising-api.amazon.com` works. The proxy
  BLOCKS the EU (`-eu`) and FE (`-fe`) hosts with a 403 tunnel error — don't
  waste retries on them; this account is NA anyway.
- **Token refresh** works via `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id/secret. Access token lasts 3600s.
- **Reporting API v3 (async):** POST `/reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`. Poll
  `GET /reporting/reports/{id}` until status COMPLETED, then download the
  presigned `url` (GZIP JSON, no auth headers on the S3 download). Reports
  completed within ~15–30s in testing.
  - Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
  - Keyword/target report: reportTypeId `spTargeting`, groupBy `["targeting"]`.
  - Columns used: campaignName, impressions, clicks, cost, purchases7d, sales7d,
    topOfSearchImpressionShare (campaign-level only). Compute CTR/CPC/ACOS/ROAS
    locally. `topOfSearchImpressionShare` is a 0–1 fraction; ×100 for %.

## Reporting conventions
- Date window: data lags 48h. 2-day report = the 2 full days ending 48h before
  the run. (Run 20 Aug → covered 16–17 Aug.)
- Comparison: use the previous SAVED 2-day report. On the first run none existed,
  so I pulled the prior window (14–15 Aug) live from the API for a baseline.
  Future runs should diff against `ppc-2day-latest.md` before overwriting it.
- Purchases/sales use 7-day attribution.

## Business state observations
- As of 16–17 Aug the US account is effectively **dormant**: ~81 impressions,
  0 clicks, $0 spend, 0 sales. Prior window (14–15 Aug) similar (1 click,
  $2.16). Root cause is almost certainly **bids too low to win clicks**. Watch
  whether bids get raised; if spend stays at $0 across runs, keep flagging it.
