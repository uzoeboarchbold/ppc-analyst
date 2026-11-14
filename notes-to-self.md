# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## Environment / API facts (verified 2026-11-14)
- Credentials come from env vars AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN, AMZ_PROFILE_ID. Token refresh at https://api.amazon.com/auth/o2/token works fine.
- **AMZ_PROFILE_ID is unusable**: it is a 50-char non-numeric string that does NOT match any real profile. Do not use it as the Amazon-Advertising-API-Scope header — it will not work. Instead call GET /v2/profiles and pick the right profile.
- Real profiles on this account (NA region only; EU/FE hosts are blocked 403 by the proxy):
  - US seller = **26765323558215** (marketplace ATVPDKIKX0DER) ← primary, use this for the FBA business
  - CA seller = 2840235221595557 (no campaigns)
  - MX seller = 3892485344323414 (no campaigns)
- Use Reporting API v3 (POST /reporting/reports, poll GET /reporting/reports/{id}, download gzip JSON from the url).
  - Content-Type/Accept: application/vnd.createasyncreportrequest.v3+json
  - **Invalid columns**: roasClicks7d and acosClicks7d are NOT valid for spCampaigns. Compute ACOS = cost/sales and ROAS = sales/cost manually. Valid base columns used: campaignName, campaignId, impressions, clicks, cost, costPerClick, clickThroughRate, purchases7d, sales7d, topOfSearchImpressionShare.
  - Report date range max ~31 days per request (a 57-day range returned HTTP 400). Keep daily reports <= 31 days.
  - Report types used: spCampaigns (groupBy campaign), spTargeting (groupBy targeting), spSearchTerm (groupBy searchTerm).
- Campaign management: POST /sp/campaigns/list with Content-Type application/vnd.spCampaign.v3+json gives state/budget/startDate.

## Standing findings
- As of 2026-11-14 the US account is DORMANT: zero impressions / clicks / spend / sales on every day from 2026-10-13 to 2026-11-11 (checked). 54 campaigns total: 15 ENABLED (budgets $1.50–$2.50/day), 32 PAUSED, 7 ARCHIVED. The enabled campaigns are live but win no auctions — likely bids too low and/or product not buyable (out of stock / no Buy Box). When a report shows all zeros, this is REAL, not a bug — report it plainly, do not invent numbers.
- Two products advertised: B0FXW3GW5F (cat deterrent spray / pet odor eliminator) and a "Cat Tunnel Bed" line (all paused/archived).

## Process reminders
- Window logic (2-day report): data lags 48h. Cover the 2 full finalised days ending 48h before run. For a run on 2026-11-14 23:09 UTC this = 2026-11-10 and 2026-11-11.
- Save reports/ppc-2day-latest.md + dated copy reports/ppc-2day-[run-date].md; commit on branch claude/great-hopper-954nu5.
- Deliver: upload to Google Drive folder "PPC Reports" + email uzoebo.archbold@gmail.com.
- Previous 2-day report to compare against: look for the prior reports/ppc-2day-*.md (excluding today's). First run = no prior report = baseline.
