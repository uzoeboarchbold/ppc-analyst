# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons on top.

## Environment / API setup (learned 2026-09-20)
- **Account**: Amazon Ads, Seller. Product in focus: ASIN **B0FXW3GW5F**
  (cat deterrent spray / pet odor eliminator), SKU pattern `6K-PZMX-MTDZ`.
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It is set to an *application*
  id (`amzn1.application....`), NOT a valid advertising profile id. Do not
  pass it as `Amazon-Advertising-API-Scope` — it will fail.
  - The real profiles on this account (from `GET /v2/profiles`, NA endpoint):
    - **26765323558215 — US / USD / seller  ← USE THIS ONE (primary market)**
    - 2840235221595557 — CA / CAD / seller
    - 3892485344323414 — MX / MXN / seller
  - Default to the **US** profile for the report. If a future run needs CA/MX,
    the ids are above. Consider reporting all three only if asked.
- **Region**: All profiles are North America. Use base
  `https://advertising-api.amazon.com`. The EU
  (`advertising-api-eu`) and FE (`advertising-api-fe`) endpoints are
  **blocked by the outbound proxy (403)** — do not waste retries on them.
- **Auth**: refresh-token exchange at `https://api.amazon.com/auth/o2/token`
  works with AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN. Access
  token lasts 3600s.
- **Reporting API v3** (`POST /reporting/reports`, async: poll
  `GET /reporting/reports/{id}` until COMPLETED, then GZIP-download `url`):
  - Content-Type header: `application/vnd.createasyncreportrequest.v3+json`.
  - `spCampaigns` report **rejects `acosClicks7d` / `roasClicks7d`** columns.
    Pull `cost`, `sales7d`, `purchases7d` and **compute ACOS/ROAS yourself**.
    (`spTargeting` and `spSearchTerm` reports DO accept acos/roas columns.)
  - `topOfSearchImpressionShare` is valid on the campaign report; it comes
    back `null` when impressions are 0.
  - Attribution used: 7-day click (`purchases7d`, `sales7d`).
- **Gotcha**: never name a scratch script `token.py` — it shadows the stdlib
  `token` module and breaks `import requests`.

## Data / account state (as of 2026-09-20 run)
- The account is **barely delivering**. Only activity in the last 30 days was
  Aug 19–Sep 2 (74–234 impressions/day, 0–2 clicks/day, ~$3.77 total spend,
  **0 sales**). **From Sep 3 onward there were ZERO impressions.**
- So the 2-day window (Sep 16–17) is legitimately all zeros — not an API
  error. If a future window is also all-zero, that is real: delivery has
  stopped (likely bids too low, tiny/blocked budget, out-of-stock, or the
  listing lost the Buy Box). Report it honestly; do not invent numbers.

## Reports
- First run of the 2-day report was 2026-09-20 (covering Sep 16–17). No prior
  2-day report existed, so no comparison baseline. Future runs: compare
  against `reports/ppc-2day-latest.md`.
