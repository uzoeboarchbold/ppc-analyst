# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work smoothly. Newest at top.

## Environment / credentials
- **AMZ_PROFILE_ID is MISCONFIGURED.** The env var holds an *application* ID
  (`amzn1.application.…`), NOT a numeric advertising profile ID. Do not use it
  directly as the `Amazon-Advertising-API-Scope` header — it will not work.
- The correct profiles under this account (from `GET /v2/profiles`, NA region
  host `advertising-api.amazon.com`):
  - **US / USD → profileId `26765323558215`  ← USE THIS ONE** (holds all 54 SP campaigns)
  - CA / CAD → `2840235221595557` (empty, 0 campaigns)
  - MX / MXN → `3892485344323414` (empty, 0 campaigns)
- Region: **NA** only. The proxy blocks EU (`advertising-api-eu…`) and FE hosts
  with `403 Forbidden`, so don't waste retries there.
- OAuth: refresh-token flow at `https://api.amazon.com/auth/o2/token` works.
  Access token lives 1 hour. Use CA bundle `/root/.ccr/ca-bundle.crt` for TLS.

## Amazon Ads reporting API (v3) gotchas
- Endpoint: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`.
- `configuration.groupBy` MUST be an ARRAY, e.g. `["campaign"]`. A bare string
  → `400 Invalid or malformed request body`.
- For `reportTypeId: spCampaigns`, columns `acosClicks7d`/`roasClicks7d` are
  NOT allowed → compute ACOS (=cost/sales) and ROAS (=sales/cost) yourself from
  `cost` + `sales7d`. (`spTargeting`/`spSearchTerm` DO allow the 7d acos/roas cols.)
- `topOfSearchImpressionShare` is a valid spCampaigns column but returns `None`
  when there are no impressions.
- Async flow: submit → poll `GET /reporting/reports/{id}` until `COMPLETED` →
  download the presigned S3 `url` (NO auth header on that S3 GET) → gunzip → JSON.
- Working column sets that were accepted:
  - spCampaigns: campaignName, campaignId, impressions, clicks, cost,
    costPerClick, clickThroughRate, purchases7d, sales7d, topOfSearchImpressionShare
  - spTargeting: campaignName, keyword, keywordType, targeting, matchType,
    impressions, clicks, cost, costPerClick, clickThroughRate, purchases7d,
    sales7d, acosClicks7d, roasClicks7d
  - spSearchTerm: campaignName, searchTerm, keyword, matchType, impressions,
    clicks, cost, purchases7d, sales7d, acosClicks7d, roasClicks7d

## Data observations
- 2026-09-21 run (window 2026-09-18→19): account is essentially DORMANT.
  15 campaigns ENABLED but ZERO impressions/clicks/spend in the window. Whole
  last 30 days = only $2.60 spend, $0 sales (nearly all on the "Cat Tunnel Bed"
  campaign, and before 2026-09-10). spTargeting/spSearchTerm reports returned 0
  rows because there was no delivery — that's expected here, not a bug.
- When the window is all-zero, the report should say so plainly (not an error).

## Date window logic
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
  Run Mon 2026-09-21 23:19 UTC → window 2026-09-18 & 2026-09-19.

## Delivery pipeline
- Reports saved to `reports/ppc-2day-latest.md` + dated copy, committed to
  branch `claude/great-hopper-dq381h`. ✅ works.
- Google Drive: upload to folder "PPC Reports"
  (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`) via Google-Drive MCP `create_file`
  with `disableConversionToGoogleType:true` so the .md stays a .md. ✅ works.
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
  ⚠️ **BLOCKED 2026-09-21:** Gmail connector is installed & connected at org
  level but `enabledInChat:false` — its tools are NOT loaded in this automated
  session, so email cannot be sent from here. No SMTP creds available either.
  ACTION FOR USER: enable the Gmail connector for this chat/automation (or add
  SMTP creds) so future runs can email. Until then, the report is delivered via
  git + Google Drive only. Don't fabricate a "sent" status.
