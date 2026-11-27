# Notes to self — PPC Analyst runs

Running log of lessons so future runs are faster and more accurate.

## Environment / API access
- **Credentials work.** Token exchange at `https://api.amazon.com/auth/o2/token` with
  AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN succeeds and returns an access token.
- **`AMZ_PROFILE_ID` is INVALID.** The env var is a ~50-character string; real Amazon Ads
  profile IDs are 13–16 digit numbers. It matches no profile on the account. Do NOT pass it as
  the Scope header — it will fail. Instead resolve the real profile from `GET /v2/profiles`.
- **Reachable region = North America only.** `advertising-api.amazon.com` works. The EU
  (`advertising-api-eu.amazon.com`) and FE (`advertising-api-fe.amazon.com`) endpoints are
  **blocked by the egress proxy (403, not retryable)**. If the real business is in EU/FE we
  cannot reach it from this session — report that, don't work around it.
- **Profiles on this account (NA):**
  - `2840235221595557` — CA, seller — 0 campaigns
  - `3892485344323414` — MX, seller — 0 campaigns
  - `26765323558215` — **US, seller — 50 campaigns (this is the real one to use)**

## The US account data situation
- US profile `26765323558215` has 50 SP campaigns (≈14–15 ENABLED, ~29 PAUSED, 7 ARCHIVED),
  all for ASIN **B0FXW3GW5F** (cat deterrent / pet odor eliminator / cat tunnel bed), budgets
  $1.50–$2.50/day, started 2026-05-18.
- **But every performance report returns ZERO** (0 impressions, 0 clicks, 0 cost, 0 sales) —
  checked Nov 23–24, Nov 10–24, and all of October. So it is NOT a date-window/48h-lag artifact.
  The campaigns are enabled but not serving. Likely causes to flag: bids too low to win any
  auction, item out of stock / lost Buy Box, or this is a sandbox/test account.
- Because there is no activity, there is nothing to optimise yet. Do not invent numbers.

## Reporting API that works (NA, v3)
- POST `/reporting/reports` with body `configuration`: adProduct `SPONSORED_PRODUCTS`,
  reportTypeId `spCampaigns` (groupBy `["campaign"]`) or `spSearchTerm` (groupBy `["searchTerm"]`),
  timeUnit `SUMMARY`, format `GZIP_JSON`. Poll `/reporting/reports/{id}` until `COMPLETED`,
  then GET the signed `url` and gunzip JSON. Content-Type/Accept:
  `application/vnd.createasyncreportrequest.v3+json`.

## Delivery (Drive + email)
- **Google Drive works.** Folder "PPC Reports" id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`
  (owner uzoebo.archbold@gmail.com). Upload with `create_file`, parentId = that folder,
  contentMimeType `text/markdown`, `disableConversionToGoogleType: true` to keep it a .md file.
- **No email tool is connected.** Only the Google-Drive and github connectors exist in this
  session — there is no Gmail/email/SMTP tool, so the "email the report" step cannot be done
  automatically. Report delivery = Drive + repo commit, and flag the missing email in the run
  notification until an email connector is added.

## Housekeeping
- `reports/` folder did not exist on first run; create it.
- Date window rule (2-day report): end 48h before run, cover the 2 full finalised days before
  that cutoff. First run was 2026-11-27 23:09 UTC → window **2026-11-23 to 2026-11-24**.
- Previous-report comparison: the 2-day report file is `reports/ppc-2day-latest.md`; dated copies
  are `reports/ppc-2day-YYYY-MM-DD.md`. First run had no prior report to compare against.
