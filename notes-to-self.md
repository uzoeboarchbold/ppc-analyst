# Notes to Self — PPC Analyst (automated runs)

Keep this file updated every run with anything that will make future runs faster or more correct.

## Account / credentials (IMPORTANT)
- **The `AMZ_PROFILE_ID` env var is INVALID.** It holds a 50-char non-numeric string
  (starts "am"), not a real Amazon Ads profile ID. Do NOT use it as the
  `Amazon-Advertising-API-Scope` header — the API returns 400 "profile ID required".
- **Correct profiles** (from `GET /v2/profiles`, all under account "Uzoebo Archbold E-Commerce"):
  - **US = `26765323558215`**  (marketplace ATVPDKIKX0DER) ← primary, the only one with campaigns
  - CA = `2840235221595557`  (0 campaigns, empty)
  - MX = `3892485344323414`  (0 campaigns, empty)
- Other creds (`AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`) are valid.
  `.strip()` all of them — they may carry whitespace.

## Transport / proxy
- Outbound goes through the agent proxy. **Python `urllib` intermittently fails with a
  spurious `403 Forbidden (agent proxy: no rule or network setting allows this host)`**
  even for allowed hosts. **Use `curl` via subprocess instead** — it tunnels reliably.
- Token endpoint: `https://api.amazon.com/auth/o2/token` (allowed).
- Ads API host: `https://advertising-api.amazon.com` (NA, allowed).
- EU (`advertising-api-eu`) and FE (`advertising-api-fe`) hosts are **blocked by the proxy**
  (HTTP 000) — and empty anyway, so ignore them.
- A working puller script lives in the scratchpad: `pull_curl.py` (takes
  start end outdir [profileId]). Re-create it from this repo's report history if lost.

## Amazon Ads API — report recipe (SP v3)
- Create report: `POST /reporting/reports`, header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`.
- Target/keyword report: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
- `timeUnit=SUMMARY`, `format=GZIP_JSON`. Poll `GET /reporting/reports/{id}` until
  `status=COMPLETED`, then download the gzip `url`.
- Columns used: impressions, topOfSearchImpressionShare, clicks, clickThroughRate,
  cost, costPerClick, purchases14d, sales14d, acosClicks14d, roasClicks14d.
- Note: SUMMARY reports omit campaigns that had zero impressions in the window, so a
  short all-zero window can return 0 rows. Cross-check with the campaign list /
  a wider window to tell "no delivery" from "no campaigns".

## Account state observed
- 2026-11-24 run (window Nov 20–21): US has 54 SP campaigns (15 ENABLED, 32 PAUSED,
  7 ARCHIVED), product ASIN **B0FXW3GW5F** (cat deterrent spray / pet odor eliminator,
  SKU 6K-PZMX-MTDZ) plus a cat-tunnel-bed campaign. **ALL 15 enabled campaigns had
  ZERO impressions / clicks / spend / sales for all of November so far.** Account is
  live but not delivering. If this persists, keep flagging it — likely bids too low,
  new listing with no rank, or a listing/inventory/Buy-Box issue.

## Delivery
- Reports folder: `reports/` — overwrite `ppc-2day-latest.md` and save dated
  `ppc-2day-YYYY-MM-DD.md`; commit on branch `claude/great-hopper-mlgdhp`.
- Google Drive: upload to folder **"PPC Reports"** via the Google-Drive MCP.
- **Email: NOT available this run.** No email/Gmail MCP tool is connected (only
  Google-Drive and github). Could not email the report. Flag to the owner to connect
  an email tool, or rely on the Drive copy. (Sharing the Drive file to the owner's
  address is a possible fallback that triggers a Google notification email.)

## Date window logic
- Data lags ~48h. 2-day report = the 2 full days ending 48h before the run.
  Run 2026-11-24 ~23:00 UTC → window = 2026-11-20 and 2026-11-21.
