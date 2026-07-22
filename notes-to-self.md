# PPC Analyst — Notes to Self

Lessons learned across runs. Read this first, every run.

## Account / API facts (confirmed 2026-07-22)
- **AMZ_PROFILE_ID env var is MISCONFIGURED**: it holds an application ID
  (`amzn1.application...`), NOT a numeric Ads profile ID. Do NOT use it directly.
- The account (`Uzoebo Archbold E-Commerce`, seller A1C2I8MOP52E35) has 3 profiles,
  all in the **NA region** (`https://advertising-api.amazon.com`):
  - CA (2840235221595557, CAD) — 0 SP campaigns
  - MX (3892485344323414, MXN) — 0 SP campaigns
  - **US (26765323558215, USD) — the ACTIVE one. 54 SP campaigns. USE THIS.**
- EU and FE region endpoints are blocked by the proxy (403). NA works fine.
- Auth: refresh-token grant at `https://api.amazon.com/auth/o2/token` works.
  Access token lasts 3600s.

## How to pull data
- Use v3 async reporting: `POST /reporting/reports` then poll
  `GET /reporting/reports/{id}` until status COMPLETED, download the gzip url.
- Content-Type for create: `application/vnd.createasyncreportrequest.v3+json`.
- Report types used: spCampaigns (groupBy campaign), spTargeting (groupBy targeting),
  spSearchTerm (groupBy searchTerm).
- `topOfSearchImpressionShare` is available on spCampaigns.
- Attribution: using **7-day** (purchases7d / sales7d) as the headline. NOTE: for a
  window ending only ~2 days ago, 7-day attribution is NOT fully mature, so recent
  sales/purchases may tick up in later runs. Keep the same window for consistency.
- CTR, CPC, ACOS, ROAS computed locally from impressions/clicks/cost/sales/purchases.

## Date window logic (data lags 48h)
- Most recent finalized full day D satisfies: D+3 (00:00) <= now. i.e. D <= today-3days.
- 2-day report = that day and the one before it.
- Example: run Wed 2026-07-22 -> cover Sat 2026-07-18 & Sun 2026-07-19.

## Reports / delivery
- Save to `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-YYYY-MM-DD.md`.
- Commit to branch `claude/great-hopper-q6szrp`.
- Upload to Google Drive folder 'PPC Reports'. Email to uzoebo.archbold@gmail.com.
- Compare against previous 2-day report (previous `ppc-2day-*.md`). First run = no baseline.

## Run history
- 2026-07-22: FIRST RUN. No prior report to compare against (baseline established).
