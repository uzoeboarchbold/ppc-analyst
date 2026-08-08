# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons first.

## Environment / API facts (learned 2026-08-08)
- **Region is NA**: use `https://advertising-api.amazon.com`. EU/FE hosts are
  blocked by the outbound proxy (CONNECT 403), and the account is North America
  anyway.
- **AMZ_PROFILE_ID env var is WRONG for the Ads API.** It holds an *application*
  ID (`amzn1.application....`), not a numeric Ads profile ID. Ignore it. Fetch
  profiles from `/v2/profiles` and pick the numeric one.
- Account "Uzoebo Archbold E-Commerce" (seller A1C2I8MOP52E35) has 3 profiles:
  - US: `26765323558215` (USD, dailyBudget 40) ← **use this one**, the active ad account
  - CA: `2840235221595557` (CAD, budget unset)
  - MX: `3892485344323414` (MXN, budget unset)
- LWA token endpoint `https://api.amazon.com/auth/o2/token` works with the
  refresh token; access token lasts 3600s.
- Reporting: Amazon Ads **v3 async reporting** (`POST /reporting/reports`,
  Content-Type `application/vnd.createasyncreportrequest.v3+json`). Poll the
  report id until status COMPLETED, then download the GZIP_JSON url.

## Date window logic
- Data lags ~48h. 2-day report = the 2 fully-finalised days ending 48h before
  the run. In practice: window = [run_date - 4 days, run_date - 3 days] inclusive.
  e.g. run Sat 2026-08-08 → cover Tue 2026-08-04 and Wed 2026-08-05.

## Report metric column names (v3)
- impressions, topOfSearchImpressionShare, clicks, clickThroughRate, cost,
  costPerClick, purchases7d, sales7d, acosClicks7d, roasClicks7d,
  campaignName, campaignId. Search-term report adds searchTerm, keywordId,
  keyword, matchType.

## Reporting gotchas (learned 2026-08-08)
- v3 report columns `acosClicks7d`/`roasClicks7d` are INVALID. Valid attribution
  columns are 7d for sales/purchases (`sales7d`,`purchases7d`) but ACOS/ROAS only
  come as `acosClicks14d`/`roasClicks14d`. Simplest: compute ACOS = cost/sales7d
  and ROAS = sales7d/cost yourself for a consistent 7d view.
- spSearchTerm report returns 0 rows when there are no clicks in the window — this
  is normal for a low-activity account, not an error.

## Delivery
- Save reports/ppc-2day-latest.md + dated copy, commit to branch
  claude/great-hopper-ddm2ll.
- Upload to Google Drive folder 'PPC Reports' (Google Drive connector IS enabled).
- Email uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
  **BLOCKER (2026-08-08): the Gmail connector is NOT enabled in the automated
  chat (`enabledInChat:false`), so email cannot be sent from these runs.** Report
  was still saved to repo + Drive. To fix: enable the Gmail connector for this
  scheduled session in claude.ai connector settings. Until then, note in each
  report that email delivery was skipped.

## Account state note (2026-08-08 window Aug 4–5)
- Account is essentially DORMANT: 6 enabled SP campaigns, ~63 impressions total,
  0 clicks, $0 spend, $0 sales over the 2 days. Likely bids too low / very new.
  Watch whether this persists; if spend stays at $0 the campaigns aren't
  competing in auctions.
