# Notes to Self — PPC Analyst (automated runs)

Living memory. Read this first every run and add lessons at the bottom.

## Account / API facts (confirmed 2026-09-07)
- Amazon Ads API works from env vars AMZ_CLIENT_ID / AMZ_CLIENT_SECRET /
  AMZ_REFRESH_TOKEN. Token refresh endpoint: https://api.amazon.com/auth/o2/token
  (LWA refresh_token grant). Returns a 1-hour access token. This works.
- **API host: https://advertising-api.amazon.com (North America).** The seller is
  North-America based (US/CA/MX marketplaces).
- **IMPORTANT — AMZ_PROFILE_ID is MISCONFIGURED.** It contains an *application id*
  (`amzn1.application....`), NOT a numeric advertising profile id. The Ads API needs
  the numeric profile id in the `Amazon-Advertising-API-Scope` header.
  - Workaround that works: call `GET /v2/profiles` to list profiles, then use the
    **US seller profile `26765323558215`** (currency USD). It is the only profile with
    Sponsored Products campaigns. CA (`2840235221595557`) and MX (`3892485344323414`)
    have zero campaigns.
  - Action for owner: fix the AMZ_PROFILE_ID secret to `26765323558215` so runs don't
    have to auto-discover it.
- Seller/account: "Uzoebo Archbold E-Commerce". Main product/ASIN B0FXW3GW5F
  (Cat Deterrent Spray / Pet Odor Eliminator). SKU token 6K-PZMX-MTDZ.
- **US profile shows `validPaymentMethod: false`.** This matters — see below.

## Reporting API (v3) how-to
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  Body: {name, startDate, endDate (YYYY-MM-DD), configuration:{adProduct:"SPONSORED_PRODUCTS",
  groupBy, columns, reportTypeId, timeUnit:"SUMMARY"|"DAILY", format:"GZIP_JSON"}}.
- Report types used: `spCampaigns` (groupBy ["campaign"]), `spSearchTerm`
  (groupBy ["searchTerm"]), `spTargeting` (groupBy ["targeting"]).
- topOfSearchImpressionShare column lives in spCampaigns. Returns null when 0 impressions.
- Poll `GET /reporting/reports/{id}` until status COMPLETED (usually <2 min), then
  download the `url` — it's a **presigned S3 URL: fetch it with NO Amazon auth headers**,
  and gunzip the body. (Sending the auth headers to S3 breaks the download.)
- Date-range limit per report request is ~31 days. Data lags ~48h, so end the window
  48h before run time.

## Data-window rule (data lags 48h)
- 2-day report: cover the 2 full days ending 48h before the run.
  Run Mon 2026-09-07 00:00 → 48h back = Sat 00:00 → covers Thu 09-03 & Fri 09-04. Verified.

## Lessons learned
- 2026-09-07 (first run): Reports pulled fine but **the covered window (Sep 3–4) had
  ZERO impressions/clicks/spend on every campaign.** This is NOT an API error — a wide
  probe (Aug 5–Sep 4) shows the account was active but tiny (cents/day, tens of imps/day),
  then impressions collapsed: ~234 on Sep 1 → 53 on Sep 2 → 0 on Sep 3 & Sep 4. Ads have
  gone dark. Likely cause: **US profile has no valid payment method
  (`validPaymentMethod:false`)**, so Amazon stopped serving ads. Flag this to the owner.
  When a window is all-zero, always run a wide probe to prove whether it's a real pause
  or a config/window bug before writing the report.
- This was the FIRST report of any type, so there was no previous 2-day report to compare
  against (Part C). Next run: compare against reports/ppc-2day-latest.md (this run).
- **Google Drive upload works** (Drive connector enabled). Folder "PPC Reports"
  id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with create_file, contentMimeType
  text/markdown, disableConversionToGoogleType=true, and put the FULL report in
  textContent (create_file's update_file only edits metadata, not content — so create
  the file already populated; don't create-then-update).
- **EMAIL STEP COULD NOT RUN.** The Gmail connector is connected at org level but
  `enabledInChat: false`, so no Gmail send tool is loaded in this automated session.
  There is no other email tool available. Result: the report was saved to the repo and
  uploaded to Drive, but NOT emailed. Fix: the owner needs to enable the Gmail connector
  for this chat/automation in claude.ai connector settings. Until then, delivery = repo +
  Drive only, and the run should flag the missing email via push notification.
