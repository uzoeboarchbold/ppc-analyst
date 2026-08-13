# Notes to Self — PPC Analyst automation

Running log of lessons so future runs go smoothly. Newest lessons on top.

## Credentials / API
- **AMZ_PROFILE_ID env var is WRONG.** It is supplied as an *application* ID
  (`amzn1.application.…`), not a usable numeric Ads profile ID. Do NOT use it.
  Look up real profiles via `GET https://advertising-api.amazon.com/v2/profiles`
  and use the **US seller profile: `26765323558215`** (USD, marketplace ATVPDKIKX0DER).
  (CA `2840235221595557` and MX `3892485344323414` also exist but are not the active account.)
- Token refresh works: `POST https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token + client_id + client_secret + refresh_token.
  Access token lasts 3600s.
- Reporting v3 flow: `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`,
  body `configuration.adProduct=SPONSORED_PRODUCTS`, `reportTypeId` in
  {`spCampaigns` (groupBy campaign), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm)}, `timeUnit=SUMMARY`, `format=GZIP_JSON`.
  Then poll `GET /reporting/reports/{id}` until `COMPLETED`, download `url`,
  gzip-decompress, JSON parse. Reports finish in ~20–60s.
- Metric column names that work: impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases14d, sales14d, acosClicks14d,
  roasClicks14d. topOfSearchImpressionShare comes back as a percent number
  (e.g. 1.04 = 1.04%).
- **spSearchTerm returns 0 rows when there were no clicks.** Expected in
  near-zero-delivery windows — not an error.

## Delivery / Reporting outputs
- **Reports are stored in Google Drive folder 'PPC Reports'**
  (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). On a fresh repo clone the local
  `reports/` folder can be empty, so to compare against the previous report of
  this type, look in that Drive folder (search `parentId = '<folder id>'`) and
  read the most recent `ppc-2day-*` doc. Latest prior at time of writing:
  `ppc-2day-2026-08-09.md` (covered Aug 5–6).
- **Dated report filename uses the RUN date**, not the window date
  (prior convention: `ppc-2day-2026-08-09.md` was generated 2026-08-09).

## Email step — LIMITATION
- **There is NO email / Gmail connector in this environment.** Only
  `Google-Drive` and `github` MCP servers are connected. The "email the report
  to uzoebo.archbold@gmail.com" step therefore cannot be completed
  automatically. Fallback: save to repo + Drive as required, and send a phone
  push notification with the headline. If email is needed, a Gmail/SMTP
  connector must be added to the environment.

## Business context (watch this)
- The account has been in a **delivery-stall** state across multiple windows:
  near-zero impressions, ~0 clicks, essentially $0 spend, 0 sales. Root cause is
  almost certainly bids below the auction floor and/or very low budgets. Each
  report should check whether this has finally been fixed (impression volume up
  AND clicks/sales appearing) rather than re-analysing tiny noise.
