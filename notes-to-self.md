# Notes to Self — PPC Analyst

Running log of lessons so future automated runs go smoothly. Newest at top.

## Run log
- 2026-07-23 (2-day, covering 07-19/07-20): Data pulled cleanly but account had
  ZERO SP activity (0 impressions/clicks/spend/sales). Only 2 of ~55 US campaigns
  are ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day each); both
  served 0 impressions. All others PAUSED/ARCHIVED. CA/MX have no SP campaigns.
  Likely advertising intentionally paused OR the 2 live campaigns aren't serving
  (low bids / no active targets / ASIN out of stock or lost Buy Box). First report
  of this type → no prior baseline for Part C comparison.

## Environment / setup facts
- Amazon Ads API region for this account: **NA** (`https://advertising-api.amazon.com`).
  The proxy CANNOT reach the EU/FE hosts — only NA resolves. Always use NA.
- Token refresh endpoint: `https://api.amazon.com/auth/o2/token` (works fine).
- **AMZ_PROFILE_ID is MISCONFIGURED.** The env var contains an application ID
  (`amzn1.application.…`), NOT a numeric advertising profile ID. The reporting
  API needs the numeric `Amazon-Advertising-API-Scope`. Real numeric profiles on
  this account (from `/v2/profiles`):
    - US: `26765323558215` (USD, ATVPDKIKX0DER)  ← primary FBA marketplace, used for reports
    - CA: `2840235221595557` (CAD)
    - MX: `3892485344323414` (MXN)
  Until the env var is fixed, hard-select the US profile. Note this in every report.
- Don't name any scratch Python file `token.py` — it shadows the stdlib `token`
  module and breaks `requests` import.

## Reporting API workflow (SP v3)
- POST `/reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Reports are ASYNC and can take 3–6+ minutes to move PENDING→COMPLETED.
  Poll patiently (every 10–15s, up to ~10 min) rather than timing out at 2 min.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`,
  `timeUnit=SUMMARY`. `topOfSearchImpressionShare` is a valid column here.
- Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`.
- Download URL returns GZIP JSON.

## Date window logic (2-day report)
- Data lags ~48h. Window = the two full finalized days ending 48h before run.
- A Thursday run (e.g. 2026-07-23) → covers Sat/Sun? No: covers the days 3–4 days
  prior = 2026-07-19 and 2026-07-20 (mirrors the spec example: Sunday run → Wed+Thu).

## Delivery
- Save reports/ppc-2day-latest.md + reports/ppc-2day-YYYY-MM-DD.md; commit+push
  to branch `claude/great-hopper-8grheg`.
- Upload to Google Drive folder 'PPC Reports' (folder id 1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo).
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Delivery gotchas (learned 2026-07-23)
- **EMAIL BLOCKED:** The Gmail connector is installed but `enabledInChat: false`
  for this scheduled session, so NO email tool loads and the report cannot be
  emailed automatically. Nothing I can do in-session fixes this — the user must
  enable the Gmail connector for this scheduled run. Until then: rely on Drive +
  the push notification. Don't waste time retrying; just note it and notify.
- **Google Drive create_file has NO update/delete counterpart** in this session.
  Re-uploading makes DUPLICATES. So: (1) FINALISE the report fully (incl. any
  delivery caveats) BEFORE the first Drive upload, and (2) pass the real content
  on the first call — never a placeholder. On 2026-07-23 I left 1 stray 30-byte
  placeholder + an interim copy in the folder because I uploaded before finalising.
