# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each run is smoother. Newest notes at top.

## Environment / account facts
- **`AMZ_PROFILE_ID` env var is MISCONFIGURED.** It contains an LWA
  *application* id (`amzn1.application.…`), NOT a numeric Ads profile scope.
  Do not use it as the `Amazon-Advertising-API-Scope` header — the API needs a
  numeric profile id.
- The refresh token works and resolves via `GET /v2/profiles` (NA endpoint) to
  three **seller** profiles under "Uzoebo Archbold E-Commerce":
  - **US = `26765323558215`**  ← the active account (54 SP campaigns)
  - CA = `2840235221595557`  (0 campaigns — empty)
  - MX = `3892485344323414`  (0 campaigns — empty)
  → **Use the US profile.** All reporting uses scope `26765323558215`.
- Region is **NA** (`https://advertising-api.amazon.com`). The EU/FE hosts are
  blocked by the outbound proxy (403) — don't bother probing them.

## API mechanics that work
- Auth: `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client id/secret → access token (valid ~1h).
- Reports: v3 async reporting API `POST /reporting/reports`, then poll
  `GET /reporting/reports/{id}` until `COMPLETED`, download the `url`
  (GZIP_JSON). Reports usually take a few minutes.
- **Column gotcha:** `spCampaigns` (groupBy `campaign`) REJECTS `acosClicks7d`
  and `roasClicks7d` — only the `*14d` variants exist there. `spTargeting` and
  `spSearchTerm` DO accept the `*7d` variants. Workaround: for the campaign
  table, pull `cost`, `sales7d`, `purchases7d` and compute ACOS = cost/sales,
  ROAS = sales/cost myself. Keep this consistent across runs.
- `topOfSearchImpressionShare` IS valid on `spCampaigns`.
- Attribution used: **7-day** (`purchases7d`/`sales7d`). NOTE: report runs only
  ~48h after the window closes, so the 7-day conversion window is not complete —
  sales/purchases will keep accruing and are slightly understated. Comparisons
  are apples-to-apples because every run has the same lag.

## Delivery channels
- **Google Drive**: connected & enabled. Upload report to folder "PPC Reports".
- **Email / Gmail**: the Gmail connector is installed for the org but is
  **toggled OFF for this chat** (`enabledInChat: false`), so there is NO
  callable send-email tool in the automated session. Cannot email the report.
  → To enable emailing, turn the Gmail connector ON for this chat/automation in
  claude.ai connector settings. Until then, note in the report that email was
  skipped and rely on Drive + repo commit.

## Report window logic (2-day report)
- Data lags ~48h. Window = the 2 full days ending 48h before run time, i.e.
  `[now-4d, now-2d)`. Example given: run Sun 00:00 → cover Wed & Thu.
  Run 2026-07-29 → covered 2026-07-25 and 2026-07-26.

## Files
- `reports/ppc-2day-latest.md` (overwrite each run) + dated
  `reports/ppc-2day-YYYY-MM-DD.md`. Compare against the previous dated 2-day
  report's headline metrics.
