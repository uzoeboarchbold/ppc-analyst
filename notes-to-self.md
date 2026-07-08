# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest lessons at top.

## Environment / API access
- **`AMZ_PROFILE_ID` env var is WRONG.** It is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an *application/client identifier*, NOT an advertising profile ID.
  Do NOT pass it as `Amazon-Advertising-API-Scope`.
- **Correct approach:** call `GET /v2/profiles` on the NA endpoint and pick the profile.
  Accounts on this login (seller "Uzoebo Archbold E-Commerce", id A1C2I8MOP52E35):
    - US  `26765323558215` (USD, dailyBudget 40.0)  <-- ACTIVE ad account, USE THIS
    - CA  `2840235221595557` (CAD, dailyBudget effectively unset ~1e9)
    - MX  `3892485344323414` (MXN, dailyBudget effectively unset ~1e9)
  The US profile is the only one with a real daily budget, so it is the live PPC account.
- **Region = NA only.** `advertising-api.amazon.com` works. EU/FE endpoints return
  `403 Tunnel connection failed` from the proxy — do not bother trying them.
- Token refresh endpoint: `https://api.amazon.com/auth/o2/token` (works fine).
  Access token lasts ~1h; refresh again for long-running polls.

## Reporting API (v3, async)
- Use v3 async reports: `POST /reporting/reports`
  Content-Type/Accept: `application/vnd.createasyncreportrequest.v3+json`.
- Reports are SLOW to generate (>2 min). Submit, then poll
  `GET /reporting/reports/{id}` every ~15s. Run polling in the BACKGROUND so a
  2-min shell timeout doesn't kill it. Download the gzipped JSON from the `url`.
- Report configs used:
    - Campaign table: reportTypeId `spCampaigns`, groupBy `["campaign"]`,
      timeUnit SUMMARY. Column `topOfSearchImpressionShare` is available here.
    - Search terms (for negatives + exact-match ideas): reportTypeId `spSearchTerm`,
      groupBy `["searchTerm"]`.
- Attribution columns use 14d window: `purchases14d`, `sales14d`, `acosClicks14d`,
  `roasClicks14d`. Keep consistent across runs for comparability.

## Date window
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run time.
- e.g. run 2026-07-08 -> cutoff 2026-07-06 -> cover 2026-07-04 & 2026-07-05.

## Email delivery — BLOCKED (needs user action)
- The Gmail connector exists and is authenticated at the org level, but it is
  **toggled OFF for the Claude session/chat** (`enabledInChat: false`), so no
  Gmail send/draft tool is loaded and the report CANNOT be emailed automatically.
- Fix (one-time, user must do it): enable the **Gmail** connector for this
  chat/automation in claude.ai connector settings. Once its tools load, email the
  report to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
- Until then: report is still committed to the repo and uploaded to Google Drive.

## Reports / delivery
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated `ppc-2day-YYYY-MM-DD.md`.
- Compare against the previous `ppc-2day-*.md` (excluding latest). FIRST RUN =
  no prior report, so note "no prior report to compare" in Part C.
- Google Drive: upload same file to folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
