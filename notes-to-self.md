# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so future runs are faster and more reliable.

## Account / credentials
- `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN` are valid. Token
  refresh works against `https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token). Access tokens last 3600s.
- **`AMZ_PROFILE_ID` is MISconfigured.** It contains an *application* ID
  (`amzn1.application...`), NOT the numeric advertising profile ID the Ads API
  needs. Passing it as `Amazon-Advertising-API-Scope` returns
  `400 Invalid scope` / "profile ID required".
  - Fix used: call `GET /v2/profiles` WITHOUT the scope header to list profiles,
    then use the numeric profile.
  - Profiles on this account (seller "Uzoebo Archbold E-Commerce", seller id
    A1C2I8MOP52E35):
    - **US (ATVPDKIKX0DER): profileId `26765323558215`** ← the active store, use this.
    - CA: `2840235221595557` (0 campaigns)
    - MX: `3892485344323414` (0 campaigns)
  - TODO for owner: set `AMZ_PROFILE_ID=26765323558215` so runs don't have to
    auto-discover.

## Endpoints / region
- NA Ads host: `https://advertising-api.amazon.com` (works).
- EU (`-eu`) and FE (`-fe`) hosts are BLOCKED by the egress proxy (403). Don't
  bother trying them.

## SP v3 Reporting API gotchas
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Body config: `adProduct":"SPONSORED_PRODUCTS"`, `timeUnit":"SUMMARY"`,
  `format":"GZIP_JSON"`, `reportTypeId` = `spCampaigns` / `spTargeting` /
  `spSearchTerm`, with matching `groupBy`.
- **Invalid columns:** `acosClicks7d` and `roasClicks7d` are NOT allowed.
  `roasClicks14d` exists but there is no 7d ROAS/ACOS column. **Compute ACOS and
  ROAS yourself** from `cost` and `sales7d` (ACOS = cost/sales, ROAS = sales/cost).
- Valid columns used: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare, clickThroughRate, costPerClick.
- SP campaign list: `POST /sp/campaigns/list`, header
  `application/vnd.spCampaign.v3+json`, paginate with `nextToken`.
- Download URL from a completed report is a presigned S3 link — fetch with NO
  auth headers, then gunzip.

## Current account status (as of 2026-10-13 run)
- US profile has **54 SP campaigns**: 15 ENABLED, 32 PAUSED, 7 ARCHIVED.
  Products are cat-deterrent / pet-odor items (ASIN B0FXW3GW5F etc.).
- **ZERO delivery:** impressions/clicks/cost/sales = 0 for the 2-day window AND
  for the trailing 30 days.
- Likely cause: **US account `validPaymentMethod` = false.** Amazon won't serve
  ads without a valid payment method. If future runs keep seeing all-zero data,
  this is almost certainly why — flag it, don't treat it as a pull failure.

## Email delivery (BLOCKED as of 2026-10-13)
- The Gmail connector IS installed and connected to the account, but it is
  **toggled OFF for this chat/session** (`enabledInChat: false`), so its email
  tools are not loaded and I cannot send the report by email from the run.
- Fix for owner: enable the **Gmail** connector for this session's chat (chat
  connector settings), or enable it for the scheduled task, so future runs can
  send the "PPC 2-Day Report" email automatically.
- Until then: report is still saved to `reports/`, committed/pushed, and
  uploaded to the "PPC Reports" Drive folder; the run notifies the owner via
  push notification in lieu of email.

## Report bookkeeping
- Reports live in `reports/`. This type: `ppc-2day-latest.md` (overwrite) +
  dated `ppc-2day-[YYYY-MM-DD].md`. Compare each run against `ppc-2day-latest.md`
  BEFORE overwriting it.
- Google Drive target folder: "PPC Reports". Email to uzoebo.archbold@gmail.com.
