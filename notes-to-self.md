# Notes to Self — PPC Analyst (automated runs)

Living memory. Read at the start of every run; append lessons at the end.

## Account setup (verified 2026-09-18)
- **AMZ_PROFILE_ID is WRONG.** It is set to an *application ID*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a numeric advertising
  profile ID. Do NOT pass it as `Amazon-Advertising-API-Scope` — it will fail.
- Real profiles on this account (from GET /v2/profiles, NA endpoint):
  - **US seller = `26765323558215`  ← use this one (all activity is here)**
  - CA seller = `2840235221595557` (no SP activity)
  - MX seller = `3892485344323414` (no SP activity)
- Region endpoint: **NA** = `https://advertising-api.amazon.com`. EU/FE endpoints are
  blocked by the proxy (403) and aren't needed — all three profiles are NA.
- Business: cat/pet products, main ASIN **B0FXW3GW5F** (Pet Odor Eliminator / cat litter
  line) plus a "Cat Tunnel Bed" campaign.

## API how-to (works)
- LWA token: POST `https://api.amazon.com/auth/o2/token`, grant_type=refresh_token,
  client_id/secret/refresh_token from env. Token lasts 3600s.
- Reports: v3 async. POST `/reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, plus Authorization,
  `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope`=<profileId>.
  Config: adProduct=SPONSORED_PRODUCTS, timeUnit=SUMMARY, format=GZIP_JSON.
  Report types used: `spCampaigns` (groupBy [campaign]), `spTargeting` (groupBy [targeting]),
  `spSearchTerm` (groupBy [searchTerm]). Poll GET `/reporting/reports/{id}` until
  status=COMPLETED, then download the `url` (gzip JSON). Takes ~15–45s.
- ToS impression share column = `topOfSearchImpressionShare`. Attribution cols used:
  purchases14d, sales14d, acosClicks14d, roasClicks14d.

## Data-state lessons
- **Empty targeting/search-term reports usually mean zero delivery, not a bug.** If
  spCampaigns has rows but they're all zero, the account simply didn't serve ads. Confirm
  by pulling a wider window (e.g. 30 days) before reporting an error.
- As of 14–15 Sep 2026 the account is **effectively dormant**: 30-day totals were only
  1,626 impressions / 16 clicks / $3.77 spend / $0.00 sales. If future windows are also
  zero, keep flagging "campaigns not delivering" (paused/budget/bids/Buy Box) rather than
  treating it as a data failure.

## Date window (2-day report)
- Data lags ~48h. Cover the 2 full days ending 48h before the run.
  Run 2026-09-18 → covered 2026-09-14 and 2026-09-15. Prev window = 09-12/09-13.

## Reports
- Save to `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-<RUNDATE>.md`.
- Dated copy uses the RUN date (YYYY-MM-DD), not the window date. Keep this consistent so
  future comparisons find the right prior file.
- First 2-day report saved = 2026-09-18. Next run: compare against `ppc-2day-latest.md`.

## Delivery
- Google Drive folder target: "PPC Reports". Email to uzoebo.archbold@gmail.com,
  subject "PPC 2-Day Report — <dates>".
