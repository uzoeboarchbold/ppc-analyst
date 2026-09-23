# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons at top.

## Account facts (verified 2026-09-23)
- Business: Amazon FBA, seller "Uzoebo Archbold E-Commerce" (seller id A1C2I8MOP52E35).
- **Active ad account = US marketplace.** Use Ads profile ID `26765323558215`
  (currencyCode USD, marketplace ATVPDKIKX0DER). CA (`2840235221595557`) and
  MX (`3892485344323414`) profiles exist but have **0 campaigns** — ignore them.
- Main product being advertised: ASIN **B0FXW3GW5F** (cat deterrent spray / pet
  odor eliminator). Campaign naming uses SKU 6K-PZMX-MTDZ.
- Campaign counts (2026-09-23): 15 ENABLED, 32 PAUSED, 7 ARCHIVED.

## IMPORTANT: env var gotcha
- `AMZ_PROFILE_ID` is **misconfigured** — it holds an *application* id
  (`amzn1.application....`), NOT a numeric Ads profile id. Do NOT pass it as
  `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` and pick the
  US profile (`26765323558215`). If profiles change, re-derive by choosing the
  profile that actually has campaigns.

## API how-to (Amazon Ads API v3, works)
- Token: POST https://api.amazon.com/auth/o2/token (grant_type=refresh_token
  with AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN). Access token ~1h.
- Region host: **advertising-api.amazon.com** (NA). EU/FE hosts are blocked by
  the proxy (403) and not needed.
- Always pass CA bundle: /root/.ccr/ca-bundle.crt for TLS via the agent proxy.
- Reports: POST /reporting/reports (async). Poll GET /reporting/reports/{id}
  until status COMPLETED, then download the S3 `url` (GZIP_JSON -> gunzip).
- Column gotchas for reportTypeId=spCampaigns: `acosClicks7d`/`roasClicks7d`
  are INVALID. Only 14d variants exist. Simplest: pull `cost`, `sales7d`,
  `purchases7d` and compute ACOS = cost/sales, ROAS = sales/cost yourself.
  `topOfSearchImpressionShare` is valid on spCampaigns (campaign groupBy).
- v3 SUMMARY reports **omit all-zero rows**, so an empty report ([]) means
  "no delivery in window", not an error. Confirm with a wider DAILY report.

## Delivery status observations
- 2026-09-23 run: US account had only trivial delivery Sep 1–2 (287 impr, 1 clk,
  $0.08) then **ZERO impressions Sep 3 onward** despite 15 enabled campaigns.
  Report windows since then show no spend/sales. Likely causes to flag to owner:
  bids below floor, new-account ramp, or listing/buy-box ineligibility. Keep
  reporting this as the key finding until delivery resumes.

## Email delivery gotcha (2026-09-23)
- The **Gmail connector is installed but toggled OFF for the session chat**
  (`enabledInChat: false`), so no `mcp__Gmail__*` send tool loads and the report
  email CANNOT be sent automatically. Google Drive upload works fine. To fix:
  the account owner must enable the Gmail connector for this chat/automation in
  connector settings. Until then, delivery is: repo commit + Drive upload +
  push notification. Re-check `ListConnectors` each run; send the email once the
  connector is enabled.

## Report mechanics
- 2-day window = the 2 full days ending 48h before run time. Data lags ~48h.
- Save reports/ppc-2day-latest.md + reports/ppc-2day-YYYY-MM-DD.md, commit,
  upload to Google Drive folder "PPC Reports", email uzoebo.archbold@gmail.com.
- Compare against previous ppc-2day-*.md report for the Part C deltas.
