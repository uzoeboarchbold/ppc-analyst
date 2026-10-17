# Notes to Self — PPC Analyst

Running log of lessons so each automated run is smarter than the last. Append; don't delete history.

## Environment / API
- **Auth works** via LWA refresh token: POST `https://api.amazon.com/auth/o2/token` with
  `grant_type=refresh_token` + `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`.
  Token lasts 1h — fine for a single run.
- **Region = NA** → host `advertising-api.amazon.com`. EU/FE hosts are blocked by the proxy (403) and aren't needed.
- **⚠️ `AMZ_PROFILE_ID` is misconfigured.** It holds an *application* id
  (`amzn1.application.…`), NOT a numeric profile id. Do **not** use it as the
  `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles` and pick the right one.
  As of 2026-10-17 the account has 3 profiles: CA (2840235221595557), MX (3892485344323414),
  **US = 26765323558215 (USD)** — this is the only one with a real daily budget ($40), so it's
  the active one. Use **26765323558215** unless profiles change.
- **Reporting = v3 async.** POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), then poll `GET /reporting/reports/{id}`
  until `COMPLETED`, then download the `url` (GZIP JSON). Reports take ~1–3 min. Allow ~9 min.
  Report types used: `spCampaigns` (groupBy `campaign`), `spSearchTerm`, `spTargeting`.
  Useful columns: impressions, topOfSearchImpressionShare, clicks, clickThroughRate, cost,
  costPerClick, purchases14d, sales14d, acosClicks14d, roasClicks14d.
- v3 SUMMARY reports may return **0 rows** for a window where every entity had zero impressions.
  That does NOT mean the request failed — confirm by probing a wider window and/or listing
  campaigns via `POST /sp/campaigns/list` (Content-Type `application/vnd.spcampaign.v3+json`).

## Date window logic
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
- Run 2026-10-17 23:10 UTC → window = 2026-10-13 and 2026-10-14. Confirmed correct.

## Account state observations
- **2026-10-17:** 54 SP campaigns total — 15 ENABLED, 32 PAUSED, 7 ARCHIVED. Every ENABLED
  campaign delivered **0 impressions / 0 spend / 0 sales** over the whole trailing month, not
  just the report window. Budgets on enabled campaigns are tiny ($1.50–$2.50/day) with auto
  bidding. Likely causes of zero impressions: product ineligible (stock/Buy Box), bids/budgets
  too low to win auctions, or targeting with no reach. Flagged in the report as the headline.
- If a future run finally sees non-zero data, the whole optimisation section (wasted spend,
  negatives, exact-match additions) becomes relevant — currently N/A because nothing serves.

## Delivery
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-[run-date].md`, commit.
- Previous report to compare against = most recent `ppc-2day-*.md` (excluding -latest) before this run.
- Upload same file to Google Drive folder 'PPC Reports' (folder id 1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo);
  email to uzoebo.archbold@gmail.com subject "PPC 2-Day Report — [dates]".
- **⚠️ EMAIL BLOCKED (2026-10-17):** The Gmail connector is connected at the org level but
  `enabledInChat: false` for these automated sessions, so no Gmail send tool loads and the report
  cannot be emailed from the run. Drive upload + git commit both work. To fix: the user must enable
  the Gmail connector for this chat/automation in Claude connector settings. Until then, delivery =
  Drive + repo + the run's push notification. Re-check `ListConnectors` each run; send the email once
  it's enabled.
- 2026-10-17: first run, so no previous 2-day report existed → comparison section said so.
