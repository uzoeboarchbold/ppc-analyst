# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / API facts (verified 2026-06-30)
- **Region is NA** — use `https://advertising-api.amazon.com`. EU/FE hosts are blocked by the proxy (403 CONNECT tunnel).
- **`AMZ_PROFILE_ID` env var is NOT a usable profile ID.** It holds an
  *application* id (`amzn1.application....`). The Amazon Ads API needs a
  **numeric** profileId in the `Amazon-Advertising-API-Scope` header.
  Resolve the real ones by calling `GET /v2/profiles` first.
- Numeric profiles on this account (seller "Uzoebo Archbold E-Commerce"):
  - **US = 26765323558215** (USD) — the only ACTIVE ad account. Use this.
  - CA = 2840235221595557 (CAD) — 0 campaigns.
  - MX = 3892485344323414 (MXN) — 0 campaigns.
- Auth: POST `https://api.amazon.com/auth/o2/token` with refresh_token grant.
  Token good for ~1h.

## Reporting API (v3) notes
- Create: POST `/reporting/reports`, Content-Type
  `application/vnd.createasyncreportrequest.v3+json`.
- Reports are async: poll `GET /reporting/reports/{id}` until
  status == COMPLETED (takes ~1–3 min; sometimes 3–5).
- **Download URL is a presigned S3 link — send NO auth headers to it**
  (extra headers make S3 reject the request / return non-JSON). Output is
  GZIP_JSON.
- Report types used: `spCampaigns` (groupBy campaign, has
  topOfSearchImpressionShare), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm).
- spCampaigns only returns rows for campaigns with activity OR enabled;
  paused/zero-activity campaigns may be omitted.

## Standing observations
- **2026-06-30: Account is DARK.** Only 2 enabled SP campaigns
  ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales") and BOTH served 0
  impressions for the whole of Jun 14–27. All 48 other campaigns PAUSED.
  Zero spend, zero ad sales. If future runs still show 0 impressions on
  enabled campaigns, the likely causes are: no/zero budget, bids too low
  to win placements, no enabled targets in those campaigns, or the ASIN is
  out of the Buy Box / out of stock. Flag it — this is the headline.

## Delivery
- **No email/SMTP tool exists in this environment.** Cannot send a true
  email with a subject line. Deliver the report by: (1) committing to repo
  `reports/`, (2) uploading to Google Drive folder "PPC Reports", and
  (3) the routine PushNotification (its body is emailed to the owner).
  Note this limitation in the report so the owner knows why no inbox email.
- Google Drive: use `mcp__Google-Drive__search_files` to find/confirm the
  "PPC Reports" folder, then `create_file` with parentId. Use
  `disableConversionToGoogleType: true` + content_mime_type `text/markdown`
  to keep it as a .md file (otherwise it converts to a Google Doc).

## Date window logic (2-day report)
- Data lags ~48h. Cover the 2 full days ending 48h before run.
  Run 2026-06-30 23:02 UTC → window = **2026-06-26 to 2026-06-27**.
