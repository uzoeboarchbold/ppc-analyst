# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest notes at the top of each section.

## Account / credentials
- **`AMZ_PROFILE_ID` env var is WRONG.** It holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an LWA *application (client) ID*, not an Amazon Ads profile ID. Do NOT pass it as the
  `Amazon-Advertising-API-Scope` header — the API needs a numeric profile ID.
- **Correct profile to use: `26765323558215`** (US marketplace, USD, seller "Uzoebo Archbold E-Commerce").
  Get it by calling `GET /v2/profiles` on the NA endpoint and picking the US profile with SP campaigns.
- The account has 3 profiles: CA (`2840235221595557`), MX (`3892485344323414`), US (`26765323558215`).
  Only the **US** profile has Sponsored Products campaigns; CA and MX are empty. Always use US.
- The US profile shows **`validPaymentMethod: false`** — this is almost certainly why ads barely serve
  (near-zero impressions/spend and $0 sales). Flag this to the owner every run until it's fixed.

## API mechanics
- Region: **NA only** — endpoint `https://advertising-api.amazon.com`. EU/FE endpoints are blocked by the
  proxy (403 CONNECT tunnel) and the account is US anyway.
- LWA token: `POST https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token` + client id/secret.
  Works fine. Token lasts 1h.
- Reporting = async v3 (`POST /reporting/reports`, then poll `GET /reporting/reports/{id}` until
  `COMPLETED`, then download the `url` which is a GZIP JSON). Reports usually finish in ~30–60s.
- **Campaign groupBy does NOT allow `acosClicks7d`/`roasClicks7d`** — only the 14d variants. Simplest fix:
  don't request ACOS/ROAS columns; pull `cost` + `sales7d` and compute ACOS = cost/sales, ROAS = sales/cost.
  `topOfSearchImpressionShare` IS a valid campaign column (returns null when there are no impressions).
- Targeting (`spTargeting`) and search-term (`spSearchTerm`) groupBys DO allow `acosClicks7d`/`roasClicks7d`.
- Attribution used: **7-day** (`sales7d`, `purchases7d`). Keep consistent across runs for comparability.
- When there are no impressions in the window, the targeting & search-term reports come back as `[]`.

## Reporting workflow
- 2-day window = the 2 full days ending 48h before run time. E.g. run 2026-09-09 → cover Sep 5 & Sep 6.
- Previous-report comparison: find the prior `ppc-2day-*.md` in `reports/`. If none, it's the baseline run.
- Google Drive folder: "PPC Reports". Email goes to uzoebo.archbold@gmail.com.

## Run history
- 2026-09-09 (covers Sep 5–6): First run. All campaigns zero activity in window; 30-day check showed only
  1,909 impressions / 17 clicks / $5.93 spend / $0 sales — account effectively dormant. No valid payment
  method on US profile. Baseline report, nothing to compare against.
