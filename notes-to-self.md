# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest first.

## 2026-08-24 (first run, 2-day report)
- **Profile ID gotcha:** `AMZ_PROFILE_ID` env var contains an *application ID*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric Amazon Ads
  profile ID. Do not pass it as the API scope. Instead call
  `GET /v2/profiles` (NA host) and pick the profile. Account has 3 seller profiles:
  - US  = `26765323558215` (USD, daily budget $40 — the live/primary one) ← using this
  - CA  = `2840235221595557` (CAD)
  - MX  = `3892485344323414` (MXN)
- **Region:** Account is North America. Use host `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the proxy (403 CONNECT tunnel) anyway.
- **Token:** `POST https://api.amazon.com/auth/o2/token` with refresh_token grant works.
  Access token lasts 3600s. Refresh at the start of each run.
- **Reporting API:** Use v3 async reporting.
  `POST /reporting/reports` with `configuration.adProduct=SPONSORED_PRODUCTS`,
  `format=GZIP_JSON`, `timeUnit=SUMMARY`.
  - Campaign level: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`.
  - Keyword/target level: `reportTypeId=spTargeting`, `groupBy=["targeting"]`.
  - Poll `GET /reporting/reports/{id}` until status COMPLETED, then download the
    presigned `url` (S3, NO auth headers) and gunzip.
  - Working columns (campaigns): campaignId, campaignName, impressions, clicks, cost,
    purchases7d, sales7d, topOfSearchImpressionShare, campaignStatus.
  - Working columns (targeting): campaignName, keyword, keywordType, matchType,
    targeting, impressions, clicks, cost, purchases7d, sales7d.
  - `topOfSearchImpressionShare` comes back as a percentage-ish number (e.g. 0.18, 1.33)
    and is `null` when there were no impressions.
- **Date window (2-day):** 2 full days ending 48h before run. Run 2026-08-24 →
  covered 2026-08-20 & 2026-08-21.
- **Account state:** Very low activity. This window: 74 impressions total, 0 clicks,
  $0 spend, 0 sales. 14 of 19 campaigns had zero impressions. Likely bids too low to
  win clicks. If future runs still show 0 clicks, the "what to do next" (raise bids /
  check budget) is the recurring message.
- **Reports folder** did not exist on first run — created `reports/`.
- **Google Drive:** WORKS. Folder `PPC Reports` exists (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`).
  Uploaded with `mcp__Google-Drive__create_file`, `parentId`=that folder,
  `contentMimeType=text/markdown`, `disableConversionToGoogleType=true` (keeps it as .md
  instead of converting to a Google Doc).
- **EMAIL — BLOCKED this run.** The Gmail connector is installed at org level but
  `enabledInChat: false` — its tools are NOT loaded in this session, so there is no
  tool to send mail. Could not email the report to uzoebo.archbold@gmail.com.
  FIX: enable the Gmail connector for this chat/automation in claude.ai connector
  settings so a `gmail`/send tool is available. Until then, the report is still
  delivered via the repo commit and the Google Drive upload. Re-check each run and
  send the email once the connector is enabled.
