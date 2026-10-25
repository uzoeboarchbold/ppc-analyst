# Notes to Self — PPC Analyst

Running log of lessons so the automated runs keep improving. Newest notes at the top.

## 2026-10-25 (first run)

### Credentials / profile
- `AMZ_PROFILE_ID` env var is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`.
  That is an **application/client ID, NOT a valid advertising profile ID** — do not pass it
  as the `Amazon-Advertising-API-Scope` header, it will fail.
- The real seller account is **"Uzoebo Archbold E-Commerce"** (seller id A1C2I8MOP52E35),
  region **NA** (`https://advertising-api.amazon.com`). Get profiles via `GET /v2/profiles`.
  Valid profile IDs:
  - **US** `26765323558215` (USD) — primary FBA marketplace. dailyBudget 40, validPaymentMethod=false.
  - **CA** `2840235221595557` (CAD) — validPaymentMethod=true.
  - **MX** `3892485344323414` (MXN).
- EU/FE region hosts are blocked by the proxy (403) and not needed — this account is NA.

### Reporting API (v3, async)
- Flow: POST `/reporting/reports` (Content-Type & Accept =
  `application/vnd.createasyncreportrequest.v3+json`) -> poll GET `/reporting/reports/{id}`
  until status COMPLETED -> download `url` (GZIP_JSON) -> parse.
- Reports are **async and slow** (tens of seconds each); run them in the background.
- Column gotchas (v3):
  - `spCampaigns` does NOT allow `acosClicks7d`/`roasClicks7d` (only the 14d variants).
    So **compute ACOS = cost/sales and ROAS = sales/cost myself** for consistency.
  - `spSearchTerm` does NOT allow `topOfSearchImpressionShare`.
  - `spTargeting` does NOT allow `searchTerm`.
  - `topOfSearchImpressionShare` IS valid on `spCampaigns`.
- Using 7-day attribution (`purchases7d`, `sales7d`). Note: for a window only ~3 days old,
  conversions are still maturing, so sales/ACOS may rise in later runs.

### Date window
- 2-day report: cover the 2 full calendar days ending 48h before run time (data lags 48h).
  Run 2026-10-25 -> covered 2026-10-21 to 2026-10-22.

### Delivery
- Reports saved to `reports/ppc-2day-latest.md` and dated copy; committed to branch.
- Google Drive folder "PPC Reports" exists: id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with
  `mcp__Google-Drive__create_file` (parentId = that id). Google Drive tools ARE enabled here.
- **EMAIL CANNOT BE SENT AUTOMATICALLY**: the Gmail connector is installed/connected at the
  org level but `enabledInChat: false` for these automated sessions, so no Gmail tool loads.
  Workaround until fixed: the report is delivered via repo commit + Google Drive, and the report
  header flags that email was not sent. To enable email, the owner must enable the Gmail
  connector (and its send permission) for Claude Code web sessions in claude.ai connector settings.

### TODO / open questions for future runs
- Confirm which marketplace the owner wants reported (US assumed primary). If multiple have
  spend, report each. This run: report whichever profile(s) actually have SP activity.
