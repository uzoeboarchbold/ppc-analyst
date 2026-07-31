# Notes to Self — PPC Analyst (Amazon FBA)

This file is my persistent memory across scheduled runs. Read it first, apply
its lessons, and add new ones whenever something surprises me.

## Report types & schedule
- I produce 2-day, and possibly other (weekly/monthly) reports.
- Each report compares against the PREVIOUS report of the SAME type.
- Reports live in `reports/`. Naming:
  - Latest pointer: `ppc-2day-latest.md`
  - Dated copy: `ppc-2day-[YYYY-MM-DD].md` (date = run date)

## Date window logic (data lags ~48h)
- End the window 48h before the run. For the 2-day report cover the 2 full
  calendar days ending at that 48h mark.
- Example: run Sunday 00:00 -> cover Wednesday & Thursday.
- State exact dates at the top of every report.

## Amazon Ads API (Sponsored Products)
- Credentials from env: AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN,
  AMZ_PROFILE_ID.
- Auth: POST https://api.amazon.com/auth/o2/token
  grant_type=refresh_token -> access_token (valid ~1h).
- Region endpoints (profile determines which one works):
  - NA: https://advertising-api.amazon.com
  - EU: https://advertising-api-eu.amazon.com
  - FE: https://advertising-api-fe.amazon.com
- Reporting v3: POST /reporting/reports (async). Poll GET /reporting/reports/{id}
  until status COMPLETED, then download the gzipped file from the URL.
- Required headers: Amazon-Advertising-API-ClientId, Amazon-Advertising-API-Scope
  (= profile id), Authorization: Bearer <token>, Content-Type: application/json.
- Metrics needed: impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases (purchases30d /
  purchases1d depending on group), sales (sales30d/sales1d), acosClicks*,
  roasClicks*. Compute ACOS = cost/sales, ROAS = sales/cost if not returned.
- Report types: SPONSORED_PRODUCTS. groupBy campaign for Part A; groupBy
  targeting (or searchTerm) for keyword/search-term analysis.

## Delivery
- Save to repo `reports/`, commit & push to branch claude/great-hopper-k1f16m.
- Upload same report to Google Drive folder 'PPC Reports' (MCP: Google-Drive).
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
  NOTE: need an email-sending tool/connector. If none available, note it in
  the report and here.

## Lessons learned
- (2026-07-31, first run) Repo started empty. Created reports/ and this file.
- **CRITICAL — AMZ_PROFILE_ID is WRONG.** The env var holds the LWA application
  id `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, NOT a numeric profile
  id. Reporting calls fail with "profile ID required". Do NOT use that env var
  as the scope. Instead list profiles and use the correct numeric IDs below.
- **Real profile IDs** (from GET /v2/profiles, no scope header):
  - US (USD, main/active): **26765323558215**  <- advertising runs here
  - CA (CAD): 2840235221595557  (no SP activity in this window)
  - MX (MXN): 3892485344323414  (no SP activity in this window)
  Only US has Sponsored Products activity. Report on US unless CA/MX wake up.
- **/v2/profiles must be called WITHOUT the Amazon-Advertising-API-Scope header.**
  Reporting/other calls DO need the scope header set to the numeric profile id.
- **Region:** account is NA -> https://advertising-api.amazon.com works.
  EU/FE endpoints are BLOCKED by the egress proxy (403 CONNECT) — don't try them.
- **Reporting v3 is SLOW today** (campaign reports took 5-10 min; targeting/
  searchTerm reports sometimes >15 min / never returned in a single run).
  Strategy that worked: fire all report POSTs up front so Amazon generates them
  in parallel, then poll. A duplicate config within a short window returns HTTP
  425 with "duplicate of : <reportId>" — reuse that id instead of failing.
  Poll the SAME report id across runs; a report queued in an earlier (killed)
  run is often COMPLETED by the time you re-poll it.
- reportTypeId values used: spCampaigns (groupBy campaign), spTargeting
  (groupBy targeting), spSearchTerm (groupBy searchTerm). timeUnit SUMMARY,
  format GZIP_JSON. Columns that worked incl. topOfSearchImpressionShare,
  clickThroughRate (returned as a percent number, e.g. 12.5 = 12.5%),
  purchases30d, sales30d, acosClicks14d (null when no sales), roasClicks14d.
- Business context: main product is a Pet Odor Eliminator / Cat Deterrent Spray
  (ASIN B0FXW3GW5F) plus a Cat Tunnel Bed. US daily budget ~$40 but spend is
  tiny -> bids too low, top-of-search impression share ~0%.

## Delivery status / TODO
- Google Drive: MCP Google-Drive tools are available (create_file, search_files).
  Need to find/create folder 'PPC Reports' and upload the .md.
- EMAIL: no confirmed email-sending tool found yet. If none exists, note in the
  report footer that email delivery is pending a connector, and record here.
  (Check ListConnectors / Gmail MCP on future runs.)
