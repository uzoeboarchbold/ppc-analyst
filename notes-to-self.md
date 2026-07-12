# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest lessons at top.

## Environment / setup facts
- **Business:** Uzoebo Archbold E-Commerce (Amazon seller account `A1C2I8MOP52E35`).
- **Profiles available** (via `/v2/profiles`, NA endpoint `advertising-api.amazon.com`):
  - **US** — profileId `26765323558215`, USD, daily budget $40. **This is the active ad account — use this one.**
  - CA — profileId `2840235221595557`, CAD, budget defaulted to max (idle).
  - MX — profileId `3892485344323414`, MXN, budget defaulted to max (idle).
- Auth works: refresh-token exchange at `https://api.amazon.com/auth/o2/token` → access token (1h). All creds present in env.

## IMPORTANT gotchas (fix these automatically)
1. **`AMZ_PROFILE_ID` is MISCONFIGURED.** It holds an application id
   (`amzn1.application.…`), NOT a numeric profileId. Do NOT pass it as the
   Advertising-API-Scope — it will fail. Instead use the US numeric profileId
   `26765323558215` (resolved from `/v2/profiles`, the only account with real
   ad activity). Re-verify via `/v2/profiles` each run in case it changes.
2. **Reporting API v3** (`POST /reporting/reports`): `acosClicks7d` and
   `roasClicks7d` are NOT valid columns. Pull `cost`, `sales7d`, `purchases7d`
   and compute ACOS = cost/sales, ROAS = sales/cost yourself.
3. **Duplicate reports (HTTP 425):** identical report configs within a short
   window are deduped. The 425 body says "duplicate of : <reportId>" — parse
   that id and just poll it instead of erroring.
4. **Reports are slow to generate.** PENDING → COMPLETED can take 10–30 min.
   Poll every 15s with a generous timeout (>=45 min). Run the poller in the
   background and check back; don't let a 2-min foreground timeout kill it.
5. Valid v3 report types used: `spCampaigns` (groupBy campaign) and
   `spSearchTerm` (groupBy searchTerm). Column `topOfSearchImpressionShare`
   is valid on spCampaigns.

## Date window logic (2-day report)
- Data lags ~48h. Cover the 2 most recent FULLY-finalized days.
- A day is safe only if its last moment is >=48h old. For a run late on
  Sun Jul 12 23:04 UTC, the safe window was **Jul 8 – Jul 9** (Jul 10 had not
  cleared 48h yet).
- Attribution note: for very recent days the 7-day conversion window is not
  fully mature, so sales/ACOS may still tick up later. Note this in the report.

## Delivery
- **NO EMAIL TOOL is connected** in this environment (searched: no Gmail/SMTP/
  compose tool). The "email it to uzoebo.archbold@gmail.com" step CANNOT be done
  automatically yet. Deliver via repo + Drive and note the gap in the report.
  If a Gmail/email MCP tool appears in future, wire it in.
- Google Drive folder **'PPC Reports'** id: `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
- Repo `reports/` folder: overwrite `ppc-2day-latest.md` + dated copy
  `ppc-2day-YYYY-MM-DD.md`. Email to uzoebo.archbold@gmail.com.
- Previous report of this type: look in `reports/` for the newest
  `ppc-2day-*.md` (excluding -latest) to compare against.

## Run history
- 2026-07-12: FIRST RUN of the 2-day report. No prior report to compare
  against (comparison section noted as baseline). Window Jul 8–9, 2026.
  KEY FINDING: account is effectively OFF — 54 SP campaigns, only 2 ENABLED
  (both zero impressions in window), 45 PAUSED, 7 ARCHIVED. Spend/sales = $0.
  Delivered to repo + Drive; email skipped (no email tool). Notified owner.
