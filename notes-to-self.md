# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest lessons at top.

## Account / credentials
- **`AMZ_PROFILE_ID` env var is WRONG** — it contains an *application* id
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), not a numeric Ads
  profile id. Do NOT pass it as the API scope. Instead call `/v2/profiles` and
  use the numeric profile id.
- Seller profiles found (all "Uzoebo Archbold E-Commerce"):
  - **US = 26765323558215** (marketplace ATVPDKIKX0DER, USD) — PRIMARY, use this.
  - CA = 2840235221595557 (CAD) — no SP campaigns.
  - MX = 3892485344323414 (MXN) — no SP campaigns.
- Use the **US** profile for reports unless told otherwise.

## API mechanics that work
- Token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token
  + client_id/secret. Works fine.
- Region endpoint: **NA `https://advertising-api.amazon.com` works.**
  EU/FE endpoints are BLOCKED by the outbound proxy (403 CONNECT tunnel). Don't
  bother with them for this account (it's NA-based anyway).
- v3 reporting: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  Poll `GET /reporting/reports/{id}` (PENDING→PROCESSING→COMPLETED, ~1-3 min),
  then download the presigned `url` (plain GET, NO auth headers), gzip-decompress.
- Report types used: `spCampaigns` (groupBy campaign, has topOfSearchImpressionShare),
  `spTargeting` (groupBy targeting), `spSearchTerm` (groupBy searchTerm).
- Reports return only rows that have data — expect an empty `[]` when there was
  no activity in the window.
- Working scripts saved in scratchpad: pull.py / poll.py / verify.py.

## Business state (watch this)
- As of the 2026-07-03..04 window, the US account had **TWO enabled SP campaigns**
  ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day budget each) but they
  generated **ZERO impressions** — no traffic at all, also zero across the prior
  2 weeks (Jun 21–Jul 04). Likely: bids too low to win auctions, campaigns newly
  created / not serving, or product not buyable/out of stock. If this persists,
  keep flagging it — enabled + zero spend = zero visibility, the top issue.

## Reports / comparison
- Save to `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-YYYY-MM-DD.md`
  (dated by RUN date).
- To compare a 2-day report, read the previous `ppc-2day-*.md` (by date) or the
  prior `ppc-2day-latest.md` content. First run had no prior 2-day report.
- Date window rule: cover the 2 full calendar days ending 48h before run time.
  Run 2026-07-07 ~23:00 UTC → window July 3 + July 4, 2026.

## Delivery
- Reports folder in Google Drive is named 'PPC Reports'. Upload the .md there.
- Email final report to uzoebo.archbold@gmail.com.
