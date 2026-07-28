# Notes to Self — PPC Analyst

Running log of lessons so future runs work better. Newest at top.

## 2026-07-28 (first run — 2-day report)
- **Account/region:** The active account is the **US** marketplace. Amazon Ads
  API works via the **NA** endpoints:
  - Token: `https://api.amazon.com/auth/o2/token`
  - API host: `https://advertising-api.amazon.com`
  - EU/FE hosts are blocked by the proxy (403) — do not retry them.
- **PROFILE ID IS MISCONFIGURED.** `AMZ_PROFILE_ID` env var is set to an LWA
  *application* id (`amzn1.application....`), NOT a numeric profile id. Do NOT
  use it as the Advertising-API-Scope. Instead call `GET /v2/profiles` on the
  NA host and pick the profile. Profiles found:
  - **US = `26765323558215`  ← use this one (54 SP campaigns, only active acct)**
  - CA = `2840235221595557` (0 campaigns)
  - MX = `3892485344323414` (0 campaigns)
  If a future run has budget, ask the human to fix the `AMZ_PROFILE_ID` secret
  to `26765323558215`. Until then, hardcode/lookup the US profile.
- **Reporting API:** v3 async reports work well.
  - Create: `POST /reporting/reports` with header
    `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  - Report types used: `spCampaigns` (groupBy `campaign`, has
    `topOfSearchImpressionShare`), `spTargeting` (groupBy `targeting`),
    `spSearchTerm` (groupBy `searchTerm`).
  - Use `sales7d` / `purchases7d` attribution columns.
  - Reports only return rows with impressions > 0, so a short table for a quiet
    window is expected, not an error.
  - Reports finish in ~40–60s; poll `GET /reporting/reports/{id}` then gunzip
    the `url` payload.
- **EMAIL NOT SENT.** Gmail connector exists but is `enabledInChat: false` — no
  Gmail tool is loaded, so I cannot send the email automatically. Delivered via
  Google Drive upload + git commit instead. **Action for human:** enable the
  Gmail connector for this scheduled chat so future runs can email the report.
- **Google Drive:** connected and working. Folder "PPC Reports" id =
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with `create_file` using
  `base64Content` + `contentMimeType: text/markdown` +
  `disableConversionToGoogleType: true` (so it stays a .md, not a Google Doc).
  - **Pitfall:** `create_file` always CREATES a new file — there is NO update
    and NO delete/trash tool. So put the REAL content in the first call; do not
    upload a placeholder. On this run I left a stray 5-byte
    `ppc-2day-2026-07-28.md` dummy in the folder (id `1UfyexxK2Pco...`) that I
    could not remove. Human can delete it manually; harmless.
- **Date window logic (2-day, data lags 48h):** cover the 2 full days ending 48h
  before run. Practically = (run_date − 4) through (run_date − 3). Run 2026-07-28
  → covered **2026-07-24 and 2026-07-25**.
- **Currency:** US profile → USD.
- **Comparison:** No previous 2-day report existed on this run (first run), so
  Part C had no baseline. Next run: compare against `ppc-2day-latest.md`.
