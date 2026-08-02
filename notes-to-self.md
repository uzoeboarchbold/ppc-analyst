# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each automated run gets smoother. Newest first.

## 2026-08-02 — First run (2-day report)

### Setup / credentials
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an *application* ID
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a numeric
  advertising **profile** ID. Do **not** pass it as `Amazon-Advertising-API-Scope`.
- The account has **3 profiles** (seller "Uzoebo Archbold E-Commerce"):
  - **US** `26765323558215` (USD, dailyBudget $40) ← **active — use this one**
  - CA `2840235221595557` (CAD, placeholder budget)
  - MX `3892485344323414` (MXN, placeholder budget)
  - Get them any time: `GET /v2/profiles` on the NA endpoint.
- **Region is NA:** `https://advertising-api.amazon.com`. The `-eu` and `-fe`
  hosts are blocked by the proxy (CONNECT 403) — don't bother trying them.
- LWA token exchange works fine: `POST https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token + client_id + client_secret. Token lives ~1h.

### Reporting API v3 (`/reporting/reports`)
- Content-Type for create: `application/vnd.createasyncreportrequest.v3+json`.
- **Column gotcha:** `acosClicks7d` / `roasClicks7d` are **invalid for
  `spCampaigns`** (400 error) but **valid for `spTargeting` and `spSearchTerm`**.
  For campaigns, pull `cost`, `sales7d`, `purchases7d` and **compute ACOS
  (cost/sales) and ROAS (sales/cost) yourself**.
- Working campaign columns: campaignName, campaignId, impressions,
  topOfSearchImpressionShare, clicks, clickThroughRate, cost, costPerClick,
  purchases7d, sales7d.
- `topOfSearchImpressionShare` only meaningful at campaign level / SUMMARY.
  It is a **share metric — do NOT sum it in the totals row** (use "—").
- Reports are async: POST → get reportId → poll `GET /reporting/reports/{id}`
  until status COMPLETED/SUCCESS → download `url` (GZIP_JSON).
- **Transient `Connection reset by peer` on polling** happens — wrap all API
  calls in a retry loop (few tries, short backoff). The report keeps generating
  server-side, so just re-poll the same reportId; don't recreate it.

### Data notes for context next time
- Account is a **cat/pet-odor niche** (product B0FXW3GW5F, plus a cat tunnel bed).
- Activity is **extremely low**: 29–30 Jul had 42 impressions, 1 click, $2.19
  spend, 0 sales across 11 campaigns. Most campaigns get ~0% top-of-search
  share → visibility problem, not a cost problem. If future windows look
  similarly quiet, that's normal for this account, not a data-pull failure.
- Only recurring cost so far: competitor-brand term **"angry orange pet odor
  eliminator"** (exact) — $2.19/click, no conversions. Candidate negative.

### Report bookkeeping
- Reports saved to `reports/`: `ppc-2day-latest.md` (overwrite) + dated
  `ppc-2day-YYYY-MM-DD.md`. Dated file uses the **run date**, not the window.
- Previous-report comparison: find the newest `ppc-2day-*.md` that isn't the
  one being written this run.

### Delivery
- Google Drive: upload to folder **"PPC Reports"** (Google-Drive MCP).
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
  (If no email MCP tool is available, note it here and in the report.)

### Date window recipe (2-day report)
- Data lags ~48h. Window = the 2 full days ending 48h before run time.
- Run Sun 02 Aug 2026 23:04 UTC → 48h back = Fri 31 Jul → cover **Wed 29 +
  Thu 30 Jul**. (Matches the spec's "run Sunday → cover Wed & Thu" example.)
