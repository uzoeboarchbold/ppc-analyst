# Notes to self — PPC Analyst

Running log of lessons so future runs go smoother. Append; don't delete history.

## Account / credentials
- Env vars present: AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN, AMZ_PROFILE_ID.
- **IMPORTANT: `AMZ_PROFILE_ID` is NOT a valid advertising profile ID.** It holds an
  Amazon *application* identifier (`amzn1.application...`). Using it as the
  `Amazon-Advertising-API-Scope` header returns HTTP 400 "Invalid scope".
- Fix: list profiles with `GET /v2/profiles` (NA host) using ONLY the
  `Authorization` + `Amazon-Advertising-API-ClientId` headers (NO scope header).
  The real numeric profile IDs for this account (seller "Uzoebo Archbold E-Commerce",
  account id A1C2I8MOP52E35):
    - US (amazon.com, USD): **26765323558215**  ← the active/built-out marketplace
    - CA (amazon.ca, CAD): 2840235221595557
    - MX (amazon.com.mx, MXN): 3892485344323414
- Token endpoint: https://api.amazon.com/auth/o2/token (refresh_token grant). Works fine.

## Network / proxy
- Only the NA Ads host is reachable: https://advertising-api.amazon.com
- EU/FE hosts (advertising-api-eu / -fe) are BLOCKED by the egress proxy (403). Don't bother.

## Reporting API (v3 async)
- POST /reporting/reports with configuration {adProduct, groupBy, columns, reportTypeId,
  timeUnit:"SUMMARY" (or "DAILY"), format:"GZIP_JSON"}. Poll GET /reporting/reports/{id}
  until status COMPLETED/SUCCESS, then download the gzip URL.
- Campaign report: reportTypeId "spCampaigns", groupBy ["campaign"].
- Search-term report: reportTypeId "spSearchTerm", groupBy ["searchTerm"].
- With SUMMARY, do NOT include the `date` column (only valid in DAILY).
- topOfSearchImpressionShare and clickThroughRate come back `null` when impressions=0.

## Delivery status (as of 2026-11-03 run)
- **US SP campaigns have ZERO delivery for all of October 2026** (0 impressions,
  0 clicks, 0 spend, 0 sales — checked Oct 4 thru Oct 31). 15 campaigns exist.
- The US profile has `validPaymentMethod: false` → almost certainly a billing /
  payment-method problem is preventing ALL US ads from serving. Flag this every run
  until it's resolved and delivery resumes.
- CA and MX profiles: no Sponsored Products campaigns / no data (0 rows).

## Report conventions
- 2-day report covers the 2 full days ending ~48h before the run (data lags 48h).
  Use the last day that ended >=48h ago. e.g. run 2026-11-03 23:10 UTC -> Oct 30 & 31.
- Save reports/ppc-2day-latest.md (overwrite) + reports/ppc-2day-[YYYY-MM-DD].md (dated copy).
- Previous report of this type to compare against: none existed on the first run (2026-11-03).
- Also: upload to Google Drive folder "PPC Reports" and email uzoebo.archbold@gmail.com.
