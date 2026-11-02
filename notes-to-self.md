# Notes to self — PPC Analyst

Running log of lessons so future runs are smoother. Newest first.

## 2026-11-02 — First run (2-day report)

### Credentials / environment
- LWA token exchange works: `POST https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token + AMZ_CLIENT_ID / AMZ_CLIENT_SECRET /
  AMZ_REFRESH_TOKEN. This succeeded first try.
- **IMPORTANT: the `AMZ_PROFILE_ID` env var is WRONG.** It is set to an
  *application* id (`amzn1.application.…`), not a numeric Amazon Ads
  profile id. Using it as the `Amazon-Advertising-API-Scope` header gives
  HTTP 400 `Invalid scope`. Do NOT trust `AMZ_PROFILE_ID`.
- To get the real profile id: call `GET /v2/profiles` with NO scope header
  (just ClientId + Bearer). It returns the numeric profile ids.
- Discovered profiles (seller account A1C2I8MOP52E35 "Uzoebo Archbold
  E-Commerce"):
  - **US  = 26765323558215** (USD)  ← the active one, use this
  - CA  = 2840235221595557 (CAD) — 0 SP campaigns
  - MX  = 3892485344323414 (MXN) — 0 SP campaigns
- Only the **US** profile has Sponsored Products campaigns (54 total:
  15 enabled, 32 paused, 7 archived). Report on US.

### Network / proxy
- Outbound must go through `$HTTPS_PROXY` with CA bundle
  `/root/.ccr/ca-bundle.crt`.
- Only the **NA** Ads host `advertising-api.amazon.com` is reachable.
  `advertising-api-eu` and `advertising-api-fe` are BLOCKED by egress
  policy (403 on CONNECT). Fine, because the account is NA.
- `requests` is not installed; use urllib with the proxy + CA bundle.

### Reporting API (v3)
- `POST /reporting/reports` with configuration adProduct=SPONSORED_PRODUCTS,
  reportTypeId spCampaigns / spTargeting / spSearchTerm, timeUnit=SUMMARY,
  format=GZIP_JSON, groupBy [campaign|targeting|searchTerm]. Then poll
  `GET /reporting/reports/{id}` until status COMPLETED, download the gzip
  url. Works. Reports usually finish within ~1 min.
- Working campaign columns: campaignName, campaignId, impressions, clicks,
  cost, purchases14d, sales14d, topOfSearchImpressionShare,
  clickThroughRate, costPerClick, acosClicks14d, roasClicks14d.
- targeting / searchTerm reports return 0 rows when there is no click/
  impression activity in the window (they only include active entities).

### KEY BUSINESS FINDING (watch this each run)
- Across Oct 17–30 the US account served **ZERO** impressions/clicks/spend
  on all enabled campaigns. The US profile shows `validPaymentMethod:false`.
  Strong signal that ads are suspended due to no valid payment method.
  If future runs keep showing all-zero with validPaymentMethod=false, the
  headline is "ads not serving — fix payment method", not a data error.
- Always check `validPaymentMethod` on the profile and surface it when
  spend is zero.

### Date window
- 2-day report: cover the 2 full days ending 48h before run. Run
  Mon 2026-11-02 23:09 UTC → window = 2026-10-29 and 2026-10-30.

### Script
- Reusable puller saved in scratchpad (`pull_ppc.py`) — reads env creds,
  auto-detects region, runs the 3 reports. Override profile with
  `AMZ_PROFILE_ID=26765323558215` since the env default is wrong.
