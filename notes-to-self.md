# Notes to Self — PPC Analyst (read me first every run)

Purpose: lessons learned so each run is smoother. Append, don't delete.

## Environment / credentials
- Auth works via LWA: POST https://api.amazon.com/auth/o2/token with
  grant_type=refresh_token + AMZ_CLIENT_ID + AMZ_CLIENT_SECRET + AMZ_REFRESH_TOKEN.
  Access token lasts 3600s. Refresh each run.
- **AMZ_PROFILE_ID is MISCONFIGURED.** It contains an *application* id
  (`amzn1.application....`), NOT a numeric Advertising profile id, so any
  reporting call scoped to it is rejected. Self-heal: call GET /v2/profiles
  and pick the profile. This account has 3 seller profiles, all owned by
  "Uzoebo Archbold E-Commerce" (matches the account email):
    - US  profileId 26765323558215   (marketplace ATVPDKIKX0DER)  <- primary, use this
    - CA  profileId 2840235221595557 (marketplace A2EUQ1WTGCTBG2)
    - MX  profileId 3892485344323414 (marketplace A1AM78C64UM0Y8)
  Using US as the report account. If the owner wants CA/MX too, add them.
  ACTION FOR OWNER: fix AMZ_PROFILE_ID to `26765323558215` to remove this workaround.
- Region endpoint: **NA** (https://advertising-api.amazon.com). EU/FE hosts are
  blocked by the proxy (403), and the profiles live on NA anyway.

## Amazon Ads reporting API (v3) gotchas
- Reporting is async: POST /reporting/reports -> poll GET /reporting/reports/{id}
  until status COMPLETED -> download the presigned `url` (GZIP_JSON). The S3
  download works fine through the proxy.
- Reports take ~3–6 min each to go PENDING->PROCESSING->COMPLETED. Create all
  reports first, then poll them together — don't run sequentially with long
  waits or the shell times out. Run the poller as a background job.
- **spCampaigns does NOT allow acosClicks7d / roasClicks7d** — only the *14d*
  variants (acosClicks14d, roasClicks14d). Simplest: pull cost + sales7d +
  purchases7d and compute CTR, CPC, ACOS, ROAS yourself. That keeps every
  table consistent regardless of report type.
- Report type ids used: spCampaigns (groupBy campaign), spTargeting
  (groupBy targeting), spSearchTerm (groupBy searchTerm).
- Attribution: using 7-day (sales7d/purchases7d). For a 2-day-old window the
  7/14/30d windows are still maturing, so sales may tick up slightly later.

## Account state (as of 2026-07-21 run)
- US account has 2 SP campaigns, both **ENABLED**:
  "SP KT | ST w/ Sales" (id 51177386692133) and
  "SP PT | ST w/ Sales" (id 258847863221155).
- **Both have had ZERO impressions for the last 30 days** (Jun 19–Jul 18).
  Enabled but not serving. Likely causes to check: bids too low to win any
  auction, daily budget effectively 0, no products/ASINs attached, or the
  listings are out of stock / suppressed / not Buy-Box eligible. Because there
  is no delivery, targeting & search-term reports return 0 rows — that's
  expected, not an error.
- Consequence: no wasted-spend or search-term-to-harvest analysis is possible
  until the campaigns actually deliver.

## Delivery channels (Drive works, email does NOT yet)
- Google Drive: connector is connected AND enabled in chat. Folder "PPC Reports"
  id = 1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo. Upload with create_file (textContent,
  contentMimeType text/markdown, disableConversionToGoogleType true).
- **Drive connector has NO update or delete tool** — only create/copy/read.
  So DON'T upload a placeholder first; pass the final content on the first
  create_file call (you cannot fix it afterward). (2026-07-21 run left one
  13-byte placeholder file that can't be removed via tools — ignore it.)
- **EMAIL: Gmail connector is installed but `enabledInChat=false`**, so it can't
  send this run. There is no other email/SMTP tool. ACTION FOR OWNER: enable the
  Gmail connector for this chat/session so future runs can email the report to
  uzoebo.archbold@gmail.com. Until then, note in the report that email was
  skipped and rely on Drive + repo.

## Report bookkeeping
- 2-day report files: reports/ppc-2day-latest.md (overwrite) and
  reports/ppc-2day-YYYY-MM-DD.md (dated). Find the previous ppc-2day-*.md to
  compare against. This 2026-07-21 run is the FIRST 2-day report (baseline,
  nothing to compare to).
- Google Drive: upload to folder "PPC Reports". Email to uzoebo.archbold@gmail.com,
  subject "PPC 2-Day Report — [dates]".

## Date window rule
- Data lags ~48h. For the 2-day report, cover the 2 full calendar days ending
  at the day-boundary that is >=48h before the run. Run 2026-07-21 23:03 UTC ->
  covered **2026-07-17 and 2026-07-18**.
