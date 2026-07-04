# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest lessons at the top.

## Environment / API (learned 2026-07-04, first run)
- **Auth works via NA endpoints.** Token: `POST https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token + AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN). Access token
  lasts 3600s. Ads API base: `https://advertising-api.amazon.com`.
- **AMZ_PROFILE_ID is WRONG/unusable.** The env var contains an *application id*
  (`amzn1.application.…`), NOT a numeric advertising profile id. Passing it as
  `Amazon-Advertising-API-Scope` fails with `profile ID required` (HTTP 400).
  **Fix:** call `GET /v2/profiles` and use the numeric profile. The live
  US (USD) seller profile is **26765323558215** — that is the one with real
  activity (CA/MX profiles are placeholders with $9.99e8 budgets). Use it as
  the scope for all reporting calls.
- **Reporting is async and can be slow.** `POST /reporting/reports` (v3,
  Content-Type `application/vnd.createasyncreportrequest.v3+json`) returns a
  reportId with status PENDING. Generation sometimes takes 1–3 minutes.
  **Do NOT create + poll in one bash call** — the 120s shell timeout kills it.
  Instead: create requests (fast), save the reportIds, then poll in a separate
  step. Download `url` (GZIP_JSON) and `zcat`.
- Useful report types: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm). Metric columns that
  work: impressions, clicks, cost, purchases7d, sales7d, topOfSearchImpressionShare,
  campaignName, keyword, matchType, searchTerm. CTR/CPC/ACOS/ROAS are derived.

## Account status (as of 2026-07-04)
- **SP ads stopped delivering after 2026-06-09.** Daily impressions are ZERO
  every day from 2026-06-10 through 2026-07-01 (the whole reporting window and
  weeks before it). Last delivery: Jun 1, 2, 8, 9 only. June total was just
  $114.12 cost / $25.98 sales.
- Only two campaigns show up in recent windows, both at zero:
  "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales". Likely paused, out of
  budget, out of stock, or bids too low. **If future runs still show zero,
  the account needs a human to check campaign status / budget / inventory.**

## Report bookkeeping
- This report type: 2-day. Latest file: `reports/ppc-2day-latest.md`.
  Dated copies: `reports/ppc-2day-YYYY-MM-DD.md`.
- Date window rule: 48h data lag. 2-day report covers the 2 full days ending
  48h before the run. Run 2026-07-04 → window 2026-06-30 & 2026-07-01.
- Compare each new 2-day report against the previous 2-day report.
- Delivery targets: save to repo, upload to Google Drive folder "PPC Reports",
  email uzoebo.archbold@gmail.com.
