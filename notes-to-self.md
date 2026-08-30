# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoother. Newest at top.

## Environment / API setup (learned 2026-08-30)
- **AMZ_PROFILE_ID is MISCONFIGURED.** The env var holds an *application id*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric ads
  profile id. Do NOT pass it as the Advertising-API-Scope. Instead resolve the
  real profile via `GET /v2/profiles`.
- Correct profile to use: **26765323558215** (US, USD, seller
  "Uzoebo Archbold E-Commerce"). This is the only profile with active
  Sponsored Products campaigns (54 of them) and a real daily budget ($40).
  The CA (2840235221595557) and MX (3892485344323414) profiles have 0 SP
  campaigns — ignore them.
- Region endpoint: **North America** = `https://advertising-api.amazon.com`.
  The proxy blocks the EU and FE endpoints (CONNECT tunnel 403) — don't bother
  trying them.
- Token exchange works fine against `https://api.amazon.com/auth/o2/token`
  with the 4 env creds. Access token lasts 3600s.
- Reporting: use the v3 async reporting API (`POST /reporting/reports`), poll
  `GET /reporting/reports/{id}` until COMPLETED, download the GZIP_JSON url.
  Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm). timeUnit SUMMARY.
  Metrics use the 14-day attribution columns (purchases14d, sales14d).

## Email delivery is BLOCKED (learned 2026-08-30)
- The task asks to email the report to uzoebo.archbold@gmail.com, but the
  **Gmail connector is not enabled in this chat session** (ListConnectors:
  enabledInChat=false). No send-email tool is available to this run, so the
  email step could NOT be completed automatically. Google Drive upload works
  fine; only email is blocked.
- Fix at source: enable the Gmail connector for this session/environment (in
  claude.ai this chat's connector settings), then future runs can email.
- Until then: report is delivered via git (reports/ folder) and Google Drive
  ("PPC Reports" folder). Flag the missing email in the run's push
  notification so the owner knows.

## Product / account context
- Main product: Cat Deterrent Spray / Pet Odor Eliminator, ASIN B0FXW3GW5F
  (SKU 6K-PZMX-MTDZ). A second product line exists: Cat Tunnel Bed (Pink).
- Campaign naming: "SP <structure> ... B0FXW3GW5F <matchtype>". Many isolated
  single-keyword campaigns plus Auto and root/broad campaigns.

## Reporting workflow reminders
- Date window for 2-day report: 2 full days ending 48h before run. Run Sunday
  2026-08-30 → covered Wed 2026-08-26 & Thu 2026-08-27. (window = run_date-4
  to run_date-3.)
- Reports live in `reports/`: overwrite `ppc-2day-latest.md` and save dated
  `ppc-2day-[YYYY-MM-DD].md` (date = run date). Compare against the previous
  `ppc-2day-*` dated file (not latest).
- Google Drive: upload same report to folder named "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Observations
- 2026-08-30 run: account was almost dormant over the window (202 impressions,
  1 click, $0.25 spend, 0 sales). Only 6 of 54 campaigns served any
  impressions. If this persists, the account may be budget/bid constrained or
  recently paused — worth flagging in the summary.
