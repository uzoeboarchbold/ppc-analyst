# Notes to Self — PPC Analyst

Running log of lessons so future runs work better. Append, don't overwrite.

## Account facts
- Advertiser: **Uzoebo Archbold E-Commerce** (seller id `A1C2I8MOP52E35`).
- Credentials in env (`AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN`) are VALID. Token
  refresh endpoint `https://api.amazon.com/auth/o2/token` works.
- Reporting region is **NA** (`https://advertising-api.amazon.com`). The EU and
  FE endpoints are blocked by the network proxy (403) — do not bother trying them.
- The account has **3 profiles**, all same seller, different marketplaces:
  - US (`26765323558215`), USD — **the active ad account** (54 SP campaigns, 15 enabled). ← USE THIS.
  - CA (`2840235221595557`), CAD — 0 campaigns.
  - MX (`3892485344323414`), MXN — 0 campaigns.
- Product under advertising: Cat Deterrent Spray / Pet Odor Eliminator, ASIN `B0FXW3GW5F`.

## Known issues / fixes
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** The env value is a 50-character string
  that is NOT a valid numeric profile id and matches none of the 3 real profiles.
  FIX APPLIED: auto-select the US profile `26765323558215` (only marketplace with
  active campaigns + a real daily budget). The user should correct the env var to
  `26765323558215`. If a future run finds `AMZ_PROFILE_ID` still broken, keep using
  the US profile and keep flagging it.
- **US profile `validPaymentMethod: false`.** As of this run the US ad account has
  NO valid payment method on file. Amazon suspends ad delivery in this state, which
  is why campaigns are ENABLED but serving **zero** impressions/clicks/spend.
- **Zero-activity confirmed wide**, not a pull bug: a DAILY report over Oct 15–Nov 7
  2026 returned 0 impressions / 0 cost on every day. So all-zero windows are real
  data, not a request error. Do NOT invent numbers to fill a zero report.

## API gotchas
- v3 reporting (`/reporting/reports`) max date range is **31 days** per request;
  a 38-day range returns HTTP 400. Split longer look-backs.
- SP campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`,
  `timeUnit=SUMMARY`, columns incl. `topOfSearchImpressionShare` work fine.
- Search-term report (`spSearchTerm`, `groupBy=["searchTerm"]`) returns 0 rows when
  there was no ad traffic — expected while the account is dark.
- Report flow: POST create -> poll GET `/reporting/reports/{id}` (status COMPLETED)
  -> download `url` (gzip JSON). Content-Type `application/vnd.createasyncreportrequest.v3+json`.

## Delivery gaps
- **Email could NOT be sent automatically.** The Gmail connector is installed and
  connected at the org level but is **not enabled in this session**
  (`enabledInChat: false`), so no `mail`/`gmail` tool is callable here. The report
  was still saved to the repo and uploaded to the Drive 'PPC Reports' folder, and a
  push notification was sent. To fix: enable the Gmail connector's tools for this
  session/chat in claude.ai connector settings so future runs can email the report.
- Google Drive upload works. 'PPC Reports' folder id: `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.

## Reports
- 2-day report: first one saved 2026-11-10 covering Nov 6–7 2026. No prior 2-day
  report existed, so that run is the baseline for future comparisons.
