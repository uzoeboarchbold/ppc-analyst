# Notes to Self — PPC Analyst (automated runs)

Living memory for the automated PPC reporting routines. Read this first on every
run and apply the lessons. Add to it whenever something breaks or surprises you.

## Account facts (verified 2026-08-16)
- Business: **Uzoebo Archbold E-Commerce** (seller ID `A1C2I8MOP52E35`).
- Three profiles exist under the account:
  - **US** — profileId `26765323558215`, USD, daily budget $40 → **the active
    advertising account. Use this one.**
  - CA — profileId `2840235221595557`, CAD, no real budget (default max). Inactive.
  - MX — profileId `3892485344323414`, MXN, no real budget (default max). Inactive.
- API region: **NA** → base URL `https://advertising-api.amazon.com`.

## Known issues / gotchas
- **`AMZ_PROFILE_ID` is invalid.** It contains a ~50-char "amzn…" string, NOT a
  numeric profile ID. Do not pass it to the API as-is. Fall back to the US profile
  `26765323558215`. Flag this in the report so the owner fixes the env var. If it
  ever becomes a valid numeric ID, prefer the env var.
- Token refresh works via `https://api.amazon.com/auth/o2/token` with
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`. Access token lasts
  3600s — plenty for one run.
- Reporting API v3: POST `/reporting/reports` with content-type
  `application/vnd.createasyncreportrequest.v3+json`; poll GET
  `/reporting/reports/{id}` (~15s cadence, usually COMPLETED within ~1–2 min);
  download the gzip URL and gunzip → JSON. Report types used: `spCampaigns`
  (groupBy campaign), `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy
  searchTerm). Use `timeUnit: SUMMARY` for the window; do NOT include a `date`
  column with SUMMARY. Attribution columns used: `purchases7d`, `sales7d`.
  `topOfSearchImpressionShare` is available on the spCampaigns report.
- Empty reports: `spSearchTerm` returns `[]` when there are no clicks in the
  window (no clicks → no search-term rows). That's normal, not an error.
- Compute CTR, CPC, ACOS, ROAS yourself from impressions/clicks/cost/sales — the
  API columns for these are attribution-window specific and easy to get wrong.
  When cost or sales is 0, show "—" (undefined), don't divide by zero.

## Date window logic
- Data lags ~48h. 2-day report = the 2 full days ending 48h before run time (UTC).
- Example: run 2026-08-16 23:04 UTC → window 2026-08-13 to 2026-08-14.

## Report history (this type: 2-day)
- 2026-08-16: FIRST run / baseline. Window 13–14 Aug 2026. Near-zero activity:
  72 impressions total, 0 clicks, $0.00 spend, $0.00 sales across 6 SP campaigns.
  Flagged near-zero ad delivery (bids/eligibility, not budget — $40 budget unspent)
  and the invalid `AMZ_PROFILE_ID`. No previous report to compare against.

## Delivery
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`.
- Commit to branch `claude/great-hopper-qkvw8h`.
- Upload the report file to Google Drive folder **"PPC Reports"** (MCP: search the
  folder by name, then create/update the file inside it).
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
