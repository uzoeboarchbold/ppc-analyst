# Notes to self — PPC Analyst routine

Running log of lessons so future runs are faster and don't repeat mistakes.
Newest lessons at the top of each section.

## Account / credentials

- **Region is NA.** Use `https://advertising-api.amazon.com`. The EU and FE
  endpoints are blocked by the outbound proxy (403 Forbidden) — do not waste
  time on them.
- **Token refresh works** against `https://api.amazon.com/auth/o2/token` with
  the `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN` env vars.
  Returns a normal access token (status 200).
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It contains an `amzn1.…` account
  identifier (~50 chars, has dots), **not** the numeric advertising profile
  ID the Reporting API needs in the `Amazon-Advertising-API-Scope` header.
  Do NOT pass it as the scope — it will fail.
- **Correct profiles** (from `GET /v2/profiles`, NA endpoint):
  - **US seller `26765323558215` (USD) — THIS IS THE ACTIVE ACCOUNT. Use it.**
  - CA seller `2840235221595557` (CAD) — empty, 0 campaigns.
  - MX seller `3892485344323414` (MXN) — empty, 0 campaigns.
  - All three are "Uzoebo Archbold E-Commerce".
- Primary product/ASIN seen in campaign names: **B0FXW3GW5F** (cat deterrent
  spray / pet odor eliminator). There's also a "Cat Tunnel Bed Pink" campaign.

## Reporting API (v3 async reports)

- Endpoint: `POST /reporting/reports` → poll `GET /reporting/reports/{id}` →
  download gzipped JSON from the returned `url`. Status reaches `COMPLETED`.
- **Max date range is 31 days per report.** A 59-day request returns HTTP 400.
- `reportTypeId: spCampaigns`, `adProduct: SPONSORED_PRODUCTS`,
  `timeUnit: SUMMARY`, `format: GZIP_JSON`. Good columns: campaignId,
  campaignName, impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare, clickThroughRate, costPerClick. Compute
  CTR/CPC/ACOS/ROAS yourself if a column is missing.
- **Quirk:** a short window (2 days) with no delivery returns **0 rows**,
  while a longer window returns rows with zero values. So "0 rows" on a short
  report does NOT necessarily mean an error — confirm by widening the window
  before concluding anything. (Seen 2026-10-28.)
- Campaign list: `POST /sp/campaigns/list` with Content-Type/Accept
  `application/vnd.spCampaign.v3+json`. Use `stateFilter` to get only ENABLED.

## Delivery / data findings

- **2026-10-28 run:** All 15 enabled SP campaigns had ZERO impressions/clicks/
  spend/sales for the 2-day window AND for a 31-day sanity window (25 Sep–25
  Oct). Campaigns are enabled with ~$23.50/day total budget but not serving.
  Most likely cause: ASIN B0FXW3GW5F out of stock / lost Buy Box / suppressed,
  or billing issue. Flagged in the report. **Next run: check whether delivery
  has resumed before assuming a reporting bug.**

## Tooling gaps (environment)

- **No email / Gmail tool is available** in this environment. The task asks to
  email the report to uzoebo.archbold@gmail.com, but there is no email
  connector. Workaround used: delivered the report summary via the routine
  PushNotification (which emails the account owner) and saved the full report
  to the repo + Google Drive. If a Gmail connector becomes available, wire up
  a proper "PPC 2-Day Report — [dates]" email.
- **Google Drive** works. Folder "PPC Reports" exists:
  id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload reports there with
  `mcp__Google-Drive__create_file` (parentId = that id, contentMimeType
  text/markdown, disableConversionToGoogleType true to keep it as .md).
- Printing env-var values (even partial) is blocked by the credential
  classifier. Don't try to echo them — just USE them in API calls and check
  the response.

## Report conventions established

- Reports saved to `reports/`: overwrite `ppc-2day-latest.md` and a dated copy
  `ppc-2day-[YYYY-MM-DD].md` (dated by RUN date).
- 2-day window = the 2 full days ending 48h before the run (data lag).
  e.g. run 2026-10-28 23:10 UTC → window 2026-10-24 to 2026-10-25.
