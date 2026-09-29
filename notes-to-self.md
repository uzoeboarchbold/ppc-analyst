# Notes to Self — PPC Analyst

Running log of lessons so each run goes smoother. Newest lessons at top of each section.

## Account / API essentials
- **Profile ID gotcha:** the `AMZ_PROFILE_ID` env var holds an *application* ID
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric Ads
  profile ID. Do NOT pass it as `Amazon-Advertising-API-Scope`. Instead call
  `GET /v2/profiles` and pick the numeric profile.
- **Active profile = US** `26765323558215` (USD, seller "Uzoebo Archbold
  E-Commerce", marketplace ATVPDKIKX0DER). This is the only profile with SP
  campaigns (54 as of 2026-09). CA (`2840235221595557`) and MX
  (`3892485344323414`) profiles exist but have 0 SP campaigns — ignore them.
- Region endpoint: **NA** `https://advertising-api.amazon.com`.
- Token refresh: `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id + client_secret. Access token lasts 1h.
- Main product/ASIN in flight: **B0FXW3GW5F** (Pet Odor Eliminator / Cat
  Deterrent Spray, SKU 6K-PZMX-MTDZ). Older "Cat Tunnel Bed" campaigns are all
  PAUSED/ARCHIVED.

## Reporting API (v3) lessons
- Endpoint `POST /reporting/reports`, content-type
  `application/vnd.createasyncreportrequest.v3+json`.
- **Campaign report (`spCampaigns`) does NOT allow `acosClicks7d`/`roasClicks7d`
  columns** — only the 14d variants. Just pull `cost`, `sales7d`, `purchases7d`
  and compute ACOS (=cost/sales) and ROAS (=sales/cost) yourself. The
  `spTargeting` and `spSearchTerm` reports DO allow `acosClicks7d`/`roasClicks7d`.
- `topOfSearchImpressionShare` is only available on the `spCampaigns` report
  (campaign groupBy), not on targeting/search-term reports.
- Attribution: using 7-day windows (`sales7d`, `purchases7d`). Note the 48h data
  lag means the most recent day's conversions may still climb slightly.
- Reports are async: poll `GET /reporting/reports/{reportId}` until
  status=COMPLETED, then download the gzipped JSON from the returned `url`.

## Report cadence / comparison
- 2-day report covers the 2 full days ending 48h before the run. First run =
  2026-09-26 to 2026-09-27 (run 2026-09-29 23:19 UTC).
- Previous-report comparison: find the prior `ppc-2day-*.md` in reports/. On the
  FIRST run there is no prior report — say so in the comparison section.

## Delivery
- Save to reports/ppc-2day-latest.md and reports/ppc-2day-YYYY-MM-DD.md; commit
  to branch `claude/great-hopper-iuigvl`.
- Upload to Google Drive folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Run history
- 2026-09-29: first run. Set up notes. Profile-ID gotcha discovered. See above.
