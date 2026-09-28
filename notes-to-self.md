# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / API facts (verified 2026-09-28)
- **Region:** North America. Use host `advertising-api.amazon.com`. EU/FE hosts are
  blocked by the proxy (403) and are not relevant — this is an NA seller account.
- **Profiles** (from `/v2/profiles`):
  - US = `26765323558215` (USD) — **THIS IS THE ACTIVE ACCOUNT**, 50+ SP campaigns.
  - CA = `2840235221595557` (CAD) — 0 campaigns.
  - MX = `3892485344323414` (MXN) — 0 campaigns.
  - Always run reports against the **US** profile.
- **Business:** "Uzoebo Archbold E-Commerce". Main product = cat deterrent spray /
  pet odor eliminator (ASIN B0FXW3GW5F, SKU 6K-PZMX-MTDZ).

## ⚠️ Misconfigured env var (IMPORTANT)
- `AMZ_PROFILE_ID` is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`
  — that is an **application ID, NOT a profile ID**. Do NOT use it as the
  `Amazon-Advertising-API-Scope`. Hardcode/resolve the US numeric profile
  `26765323558215` instead. Token refresh + client id/secret all work fine.

## How to pull data (works)
1. Refresh token: POST `https://api.amazon.com/auth/o2/token` with grant_type=
   refresh_token + client_id + client_secret + refresh_token → access_token (1h).
2. SP reports v3: POST `/reporting/reports` with `Amazon-Advertising-API-Scope: <US profile>`,
   Content-Type `application/vnd.createasyncreportrequest.v3+json`.
   - Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`,
     columns incl. `topOfSearchImpressionShare` (only valid with timeUnit SUMMARY).
   - Targeting report: reportTypeId `spTargeting`, groupBy `["targeting"]`.
   - Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
   - Use `purchases30d`/`sales30d` for conversions/sales. timeUnit SUMMARY, format GZIP_JSON.
3. Poll GET `/reporting/reports/{id}` until status COMPLETED, then download the
   signed `url` (gzip JSON). Reports take ~1-3 min to generate.

## Date window rule
- Data lags ~48h. For the 2-day report cover the 2 full days ending 48h before run.
- Script currently hardcodes START/END — **update these each run** (or compute).

## Deliverables each run
- Save `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-YYYY-MM-DD.md`; commit + push to branch `claude/great-hopper-dudz2t`.
- Upload same report to Google Drive folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Email / Drive delivery
- **Gmail connector is INSTALLED but OFF for the automated session** (`enabledInChat:false`),
  so no send tool loads and email CANNOT be sent from here. Report is still saved
  to repo + Google Drive. To fix: user must enable Gmail for this chat/session.
- Google Drive connector IS enabled — upload via `mcp__Google-Drive__create_file`
  into the "PPC Reports" folder (find its folder id with `search_files`).

## Dated-copy naming
- Using the LAST covered day as the date suffix, e.g. window 09-24..09-25 →
  `ppc-2day-2026-09-25.md`. Keep this convention consistent.

## Account health flags to watch
- US ad account `validPaymentMethod:false` → Amazon halts delivery. When ads show
  zero impressions across all campaigns, check this first before assuming a bug.
- Campaign mix (2026-09-28): 54 total = 15 ENABLED, 32 PAUSED, 7 ARCHIVED.

## Run history
- 2026-09-28: First run. Set up structure. Covered 2026-09-24..25.
  RESULT: ZERO delivery in window (0 imp/clicks/spend/sales). Account has had no
  delivery since ~Sep 10-11; only $0.35 spend + 782 imp + $0 sales across the
  prior 28 days. Root cause almost certainly the missing valid payment method.
  Email could not send (Gmail off). No previous report to compare against.
