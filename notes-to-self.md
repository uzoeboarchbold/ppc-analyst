# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest entries on top.

## 2026-06-26 (first run, 2-day report)

**Environment / API mechanics**
- Auth works: LWA token exchange at `https://api.amazon.com/auth/o2/token` with
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`. Returns a ~727-char
  access token, valid ~1h.
- **`AMZ_PROFILE_ID` env var is MALFORMED.** It is set to an *application* ID
  (`amzn1.application.…`), NOT a numeric advertising profileId. The reporting API
  Scope header needs the numeric profileId. Do NOT use the env var directly.
- Resolve the real profile via `GET /v2/profiles` (NA endpoint
  `https://advertising-api.amazon.com`). This account has 3 seller profiles:
    - CA `2840235221595557` (CAD) — **no SP campaigns**
    - MX `3892485344323414` (MXN) — **no SP campaigns**
    - US `26765323558215` (USD) — **the active one; use this.**
- Region endpoint is NA (`advertising-api.amazon.com`).
- Reports v3: `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`, `reportTypeId: spCampaigns`,
  `groupBy:["campaign"]`, `timeUnit:"SUMMARY"`, `format:"GZIP_JSON"`. Poll
  `GET /reporting/reports/{id}` until COMPLETED, then download `url` and gunzip.
  Reports usually finish in ~40–80s.
- **Invalid columns:** `acosClicks7d` and `roasClicks7d` are NOT allowed on
  spCampaigns. ACOS/ROAS must be COMPUTED (ACOS = cost/sales, ROAS = sales/cost).
  Valid revenue/order cols: `purchases7d`, `sales7d`, `cost`, `impressions`,
  `clicks`, `clickThroughRate`, `costPerClick`, `topOfSearchImpressionShare`,
  `campaignName`, `campaignId`, `campaignStatus`. (14d/30d variants also exist.)
- A SUMMARY report only returns rows for campaigns that had records in the window;
  paused/no-record campaigns are omitted. For a full daily picture include `date`
  and use `timeUnit:"DAILY"`.
- File names must not shadow stdlib (don't name a script `token.py`).

**Delivery channels**
- Google Drive upload works: 'PPC Reports' folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
- **No email/Gmail/SMTP tool is available in this environment.** I cannot send the
  email myself. Report is saved to repo + uploaded to Drive; email step is flagged
  as not-deliverable at the top of the report. If email matters, the owner needs to
  wire up a Gmail/SMTP MCP tool.

**Business finding this run**
- Account went DARK. Normal delivery May 25–Jun 8 (~$40–56/day). From Jun 9 onward
  essentially zero. Reporting window Jun 22–23 = 0 impressions, 0 spend, 0 sales.
  Two campaigns ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales") are ENABLED but not
  delivering. Likely budget exhausted/paused, bids too low, or product out of stock.
  Future runs: if window is still zero, keep flagging the dark account until it
  recovers, and compare against this baseline.
