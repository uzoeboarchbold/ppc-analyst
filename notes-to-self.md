# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest at top.

## 2026-07-01 — First run (2-day report, covering Jun 28–29 2026)

**Credentials / API**
- Token exchange endpoint `https://api.amazon.com/auth/o2/token` with the 4 env
  vars works fine. Access token lasts 3600s.
- **IMPORTANT — `AMZ_PROFILE_ID` env var is WRONG.** It contains a value like
  `amzn1....` (50 chars). That is NOT a valid Amazon Ads profile ID — profile
  IDs are numeric. Calling the API with it will fail.
  - Fix that works: call `GET /v2/profiles` on the NA endpoint. The account has
    3 profiles: CA (2840235221595557), MX (3892485344323414), and
    **US = 26765323558215 (USD)**. Only the US profile has a real daily budget
    ($40); the others are placeholder budgets. Use the **US profile 26765323558215**.
  - If future runs get a real numeric AMZ_PROFILE_ID, prefer it, but validate it
    is numeric first.
- **Region: North America only.** Endpoint `https://advertising-api.amazon.com`
  returns 200. The `-eu` and `-fe` endpoints are BLOCKED by the outbound proxy
  (CONNECT tunnel 403) — do not waste retries on them.

**Reporting API (v3)**
- POST `/reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`. Async: poll
  `/reporting/reports/{id}` until status COMPLETED, then GET the signed `url`
  (GZIP_JSON). Reports took ~2–4 min to go PENDING→PROCESSING→COMPLETED.
- Report types used: `spCampaigns` (groupBy campaign — carries
  `topOfSearchImpressionShare`), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm).
- Compute ACOS = cost/sales, ROAS = sales/cost yourself; CTR/CPC come back as
  `clickThroughRate`/`costPerClick`. Use `sales7d`/`purchases7d` (7-day
  attribution, standard for seller accounts).

**Account state (context for future reports)**
- Almost every campaign is PAUSED or ARCHIVED. As of this run only TWO are
  ENABLED: `SP KT | ST w/ Sales` and `SP PT | ST w/ Sales` (both $8/day, started
  2026-06-09). Both barely deliver (78 & 0 impressions across all of June).
- Result: the Jun 28–29 window had **zero** impressions/clicks/spend/sales on the
  enabled campaigns. This is REAL, not an API error. Verified with a wider
  Jun 1–29 pull that DID return non-zero data for the paused campaigns.
- When a window is all-zero, say so plainly and flag that PPC is effectively
  dark — do not treat it as a failure or invent numbers.

**Delivery (Drive + email)**
- Google Drive: upload the .md into the folder named 'PPC Reports' (search for
  the folder first; create if missing).
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
- Report file naming: overwrite `reports/ppc-2day-latest.md` + dated copy
  `reports/ppc-2day-YYYY-MM-DD.md` (date = run date).
- Previous-report comparison: find the most recent prior `ppc-2day-*.md`
  (excluding latest) in reports/. First run = no baseline.
