# Notes to Self — PPC Analyst

Lessons carried forward so each run is faster and more reliable. Update this
whenever something breaks or a workaround is found.

## Account / API facts
- **Profile ID env var is WRONG.** `AMZ_PROFILE_ID` holds an *application* ID
  (`amzn1.application.…`), not a numeric advertising profile ID. Do NOT pass it
  to the API. The correct live profile is **US = `26765323558215`** (USD,
  seller, $40 daily account budget). Other profiles exist but have no campaigns:
  Canada `2840235221595557`, Mexico `3892485344323414`.
- **Token refresh works** against `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id + client_secret + refresh_token.
  (Note: in mid-June 2026 the login host `api.amazon.com` was briefly blocked by
  the network allowlist; it is reachable again. If a run gets
  `403 Host not in allowlist: api.amazon.com`, that is a network/egress problem,
  not a credentials problem — report it, don't invent numbers.)
- Reporting is the Amazon Ads **v3 async reporting API**
  (`POST /reporting/reports`, then poll `GET /reporting/reports/{id}`, then
  download the gzipped JSON from the returned URL). Reports typically take
  **5–15 minutes** to move PENDING → COMPLETED, so poll patiently in the
  background; don't give up after 2 minutes.
- Use `purchases30d`, `sales30d`, `acosClicks14d`, `roasClicks14d`,
  `topOfSearchImpressionShare` columns. reportTypeIds: `spCampaigns`,
  `spTargeting`, `spSearchTerm`. Content-Type header:
  `application/vnd.createasyncreportrequest.v3+json`.

## Delivery
- **No email tool is connected** to this automation. The "email to
  uzoebo.archbold@gmail.com" step CANNOT be done here. Deliver instead by:
  (1) committing to the repo `reports/` folder, (2) uploading to the Google
  Drive folder **'PPC Reports'** (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`),
  (3) sending the headline as a push notification. State this limitation plainly
  at the top of the report. To truly enable email, a Gmail/email integration
  must be added to the environment.
- GitHub access is scoped to `uzoeboarchbold/ppc-analyst`. Develop on the
  designated branch, commit both `ppc-2day-latest.md` and the dated copy.

## Account state (as of mid-July 2026)
- Account has been effectively **dark since ~9–10 June 2026**. Only **2
  campaigns are ENABLED** — "SP KT | ST w/ Sales" and "SP PT | ST w/ Sales"
  ($8/day each, launched 9 June) — and both serve **0 impressions**. All other
  ~50+ campaigns are Paused/Archived. Every 2-day report since has read all
  zeros. This is a real account condition (verified), not a data error.
- If zeros again: it's an on/off problem, not a performance problem. Likely
  causes: bids too low to win auctions, something paused inside the ad
  group/ASINs/keywords, or the ASIN (cat-deterrent / pet-odour, B0FXW3GW5F) out
  of stock / lost Buy Box.

## Comparison chain (2-day reports, most recent first)
- Compare each new 2-day report against the previous 2-day report in Drive.
- 2026-07-15 (covers 11–12 Jul): all zeros.
- 2026-07-10 (covers 6–7 Jul): all zeros.
- 2026-06-27 (covers 23–24 Jun): all zeros.
- Earlier June reports: all zeros. Last real spend was 8–9 June (~$46, 9 clicks,
  0 orders); normal activity (~$40–55/day) ended ~2 June.
