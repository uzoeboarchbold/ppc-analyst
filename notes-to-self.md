# Notes to Self — PPC Analyst

Running log of lessons so future automated runs work smoothly. Newest first.

## 2026-08-09 (first run — 2-day report)

**Credentials / API**
- `AMZ_PROFILE_ID` env var is WRONG — it holds an application ID
  (`amzn1.application.…`), NOT a numeric Amazon Ads profile ID. Do not pass it
  as `Amazon-Advertising-API-Scope`; it will fail.
- The real profiles live in the **NA** region (`advertising-api.amazon.com`).
  `GET /v2/profiles` returns three seller profiles for "Uzoebo Archbold
  E-Commerce":
    - US = `26765323558215`  ← primary, use this
    - CA = `2840235221595557`
    - MX = `3892485344323414`
  EU and FE hosts are blocked by the network proxy (403), which is expected —
  the account is NA.
- Token exchange works fine: POST `https://api.amazon.com/auth/o2/token` with
  refresh_token + client_id + client_secret. Access token lasts 3600s.
- Reporting API v3 works: POST `/reporting/reports`, poll `/reporting/reports/{id}`,
  download the gzipped-JSON `url`. `spCampaigns` (groupBy campaign) and
  `spTargeting` (groupBy targeting) both succeed. Reports finished in <1 min.

**Data notes**
- Account delivery is VERY low. In the Aug 5–6 window: 91 impressions, 1 click,
  $0.07 spend, 0 orders across 7 SP campaigns. Most campaigns got single-digit
  impressions. Watch this trend — if it stays near-zero, bids/budgets are likely
  the bottleneck, not creative.
- `topOfSearchImpressionShare` comes back as a fraction (0.58 = 58%). It is a
  per-campaign share, not additive; for a totals row use an impression-weighted
  average and label it as such.
- `acosClicks14d` / `roasClicks14d` are `null` when there are no sales.

**Reports of this type**
- 2-day reports: `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`
  (dated by RUN date). Compare each new one against the previous 2-day report.
- This was the FIRST 2-day report, so there was no prior report to compare to.

**Date window**
- Data lags 48h. 2-day window = the 2 full days ending ~4 days back:
  window = [run_date − 4 days, run_date − 3 days]. Run 2026-08-09 → Aug 5–6.

**Delivery (Drive/email)**
- Google Drive folder target: "PPC Reports". Email to uzoebo.archbold@gmail.com.
