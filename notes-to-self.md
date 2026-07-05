# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Credentials & auth
- Env vars present: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
- **IMPORTANT:** `AMZ_PROFILE_ID` holds an *application* id (`amzn1.application....`), NOT a usable numeric profile id. Do **not** put it in the `Amazon-Advertising-API-Scope` header — the API needs the numeric profileId.
- Resolve the real profile with `GET https://advertising-api.amazon.com/v2/profiles`. Three profiles exist: CA (`2840235221595557`), MX (`3892485344323414`), US (`26765323558215`). **US is the active marketplace** (USD, daily budget $40). Use `26765323558215` in the Scope header.
- Token refresh: `POST https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token`, `refresh_token`, `client_id`, `client_secret`. Works, returns a 1-hour `access_token`.

## Amazon Ads API (v3 reporting)
- Base: `https://advertising-api.amazon.com`. Headers on every call: `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope` (numeric profileId), `Authorization: Bearer <token>`.
- Reports are async: `POST /reporting/reports` (content-type `application/vnd.createasyncreportrequest.v3+json`) → poll `GET /reporting/reports/{id}` → status goes PENDING → PROCESSING → COMPLETED → download gzipped JSON from `url`. Can take 60–150s; poll with backoff (~8s), up to ~15 tries.
- With `timeUnit: SUMMARY` you may **not** request the `date` column — use it only with DAILY.
- At campaign level, ACOS/ROAS are only offered as **14d** (`acosClicks14d`, `roasClicks14d`), not 7d. Simplest: request `cost`, `sales7d`, `purchases7d`, `impressions`, `clicks`, `topOfSearchImpressionShare`, `clickThroughRate`, `costPerClick` and compute ACOS = cost/sales, ROAS = sales/cost yourself.
- Report type ids used: `spCampaigns` (groupBy `campaign`), `spSearchTerm` (groupBy `searchTerm`). Search-term report returns 0 rows when there are no clicks in the window.
- Campaign states: use v3 `POST /sp/campaigns/list` with content-type/accept `application/vnd.spCampaign.v3+json`. The old v2 `POST /v2/sp/campaigns/list` returns 405.

## Account status (as of 2026-07-05 run)
- 50 campaigns total, but **only 2 are ENABLED**: `SP KT | ST w/ Sales` (id 51177386692133) and `SP PT | ST w/ Sales` (id 258847863221155), both started 2026-06-09, $8/day budgets. Everything else is PAUSED or ARCHIVED (mostly a "Cat Tunnel Bed" product and a "6K-PZMX / B0FXW3GW5F" cat-odor product line).
- Account is effectively **dormant**: across Jun 9–Jul 2 the whole account logged only ~159 impressions, **0 clicks, $0 spend, $0 sales**. So zero-value reports are the *correct* result right now, not an error. Do not invent numbers.

## Delivery
- **Google Drive**: connected and usable this session. Upload target folder: `PPC Reports`.
- **Gmail**: the connector is installed but was `enabledInChat: false` on the 2026-07-05 run, so email could NOT be sent from the session. If email is required, the Gmail connector must be enabled for this chat/session. Until then, note in the report that email delivery was skipped.

## Report bookkeeping
- Save to `reports/`: overwrite `ppc-2day-latest.md` and write dated `ppc-2day-[YYYY-MM-DD].md`. Commit + push to branch `claude/great-hopper-8tb6i9`.
- Find the previous report of the same type in `reports/` to build the comparison (Part C). First 2-day report was 2026-07-05 (no prior baseline).

## Date window logic (data lags 48h)
- 2-day report: cover the 2 full days ending 48h before run. Run 2026-07-05 23:03 UTC → window **2026-07-01 to 2026-07-02**.
