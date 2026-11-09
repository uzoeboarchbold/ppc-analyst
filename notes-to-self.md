# Notes to Self — PPC Analyst automation

Running log of lessons so each run gets smoother. Newest at top.

## Account / environment facts (verified 2026-11-09)
- Business: **Uzoebo Archbold E-Commerce**, Amazon seller (ASIN seen: B0FXW3GW5F — Cat Deterrent Spray / Pet Odor Eliminator).
- Amazon Ads **region = NA** → host `https://advertising-api.amazon.com`. (EU/FE hosts are blocked by the proxy and irrelevant anyway.)
- Three profiles exist under the account:
  - **US `26765323558215` (USD)** → the ONLY one with campaigns. **Use this one.**
  - CA `2840235221595557` and MX `3892485344323414` → 0 campaigns, ignore.
- Token endpoint `https://api.amazon.com/auth/o2/token` with refresh_token grant works. Access token lasts 3600s.
- Reporting API v3: `POST /reporting/reports` with `Content-Type: application/vnd.createasyncreportrequest.v3+json`; poll `GET /reporting/reports/{id}` until `COMPLETED`; download gzipped JSON from the returned `url`.
  - Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`.
  - Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`.
  - Attribution: using `purchases7d` / `sales7d`.

## IMPORTANT gotcha — `AMZ_PROFILE_ID` is WRONG
- The env var `AMZ_PROFILE_ID` is set to `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` — that is an **application/client ID, NOT a numeric Ads profile ID**.
- Do **not** pass it as the `Amazon-Advertising-API-Scope` header; it will fail.
- Workaround (currently hard-coded in the pull script): call `GET /v2/profiles`, pick the US profile `26765323558215`, use that as scope.
- TODO for a human: fix the env var to the numeric profile ID.

## IMPORTANT finding — ads are NOT serving (as of 2026-11-09)
- US profile has `accountInfo.validPaymentMethod: false`.
- Result: 15 ENABLED campaigns deliver **zero** impressions/clicks/spend/sales. Confirmed zero across the whole of Oct 10 – Nov 6, not just the report window.
- So a zero report is likely REAL, not a bug. Always sanity-check with a wider date window AND the `validPaymentMethod` flag before blaming the API.
- Once billing is fixed this will change; keep comparing to prior reports to confirm ads resumed.
- Campaign census 2026-11-09: 54 total = 15 ENABLED, 32 PAUSED, 7 ARCHIVED.

## Delivery limitation — EMAIL not possible from this session (2026-11-09)
- Google Drive connector works (upload succeeds). Folder 'PPC Reports' id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
- **Gmail connector is connected at org level but `enabledInChat: false`** → its tools are NOT loaded in this session, so the report could not be emailed to uzoebo.archbold@gmail.com.
- Workaround used: pushed to repo, uploaded to Drive, and sent a phone/email push notification via the routine's own notifier.
- TODO for a human: enable the Gmail connector's tools for this automated chat/session so future runs can email.

## Report mechanics
- 2-day window = the 2 full days ending 48h before run (data lags ~48h). E.g. run 2026-11-09 23:10 UTC → cover Nov 5 & Nov 6.
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`; commit to branch `claude/great-hopper-g3v3at`.
- Previous-report comparison: find the newest `reports/ppc-2day-*.md` that is NOT today's dated file / latest. On 2026-11-09 there was none → first baseline run.
- Delivery: upload to Google Drive folder **'PPC Reports'**; email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
