# Notes to Self — PPC Analyst routine

Running log of lessons so each run is smoother than the last. Newest at top.

## 2026-08-29 (first run — 2-day report)

**Amazon Ads API — what works**
- Auth: POST `https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token`
  + the 4 env vars. Returns a 1-hour `access_token`. Works fine.
- Region: account lives on the **North America** endpoint
  `https://advertising-api.amazon.com`. The EU (`-eu`) and FE (`-fe`)
  endpoints are BLOCKED by the outbound proxy (403 CONNECT tunnel) — don't
  waste retries on them; NA is the one to use.
- Reporting is the async v3 API: POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), poll
  `GET /reporting/reports/{id}` until `COMPLETED`, then download the
  gzipped-JSON `url`. Reports took ~30–60s to finish.

**Gotchas fixed this run**
- **`AMZ_PROFILE_ID` is wrong.** It holds an *application* ID
  (`amzn1.application.dd42...`), NOT a numeric profile ID. Don't pass it as
  the scope — the API needs a numeric profileId. Get profiles from
  `GET /v2/profiles`. Three exist for this seller (all account
  `A1C2I8MOP52E35`):
    - US  `26765323558215`  (USD, daily budget $40) ← ACTIVE, use this one
    - CA  `2840235221595557` (CAD, budget placeholder 999999999)
    - MX  `3892485344323414` (MXN, budget placeholder 999999999)
  I default to the **US** profile. If the owner fixes the env var to a
  numeric ID, prefer that instead.
- **`spCampaigns` report rejects `acosClicks7d` / `roasClicks7d` columns.**
  Those columns only exist on `spSearchTerm` / `spTargeting` reports. For
  the campaigns report, pull `cost` + `sales7d` + `purchases7d` and compute
  ACOS = cost/sales and ROAS = sales/cost yourself.
- **Campaign names contain `|` characters** (e.g. "SP | Cat Tunnel Bed | ...").
  Escape them as `\|` before putting them in a Markdown table or the table
  breaks.

**Delivery**
- Google Drive connector is connected + enabled → upload to folder "PPC Reports" works.
- **Gmail connector is installed but NOT enabled in the automated session**
  (`enabledInChat: false`), so email cannot be sent. Documented the gap at
  the top of the report and told the owner to enable Gmail for the session.
  Re-check each run; send the email once it's enabled.

**Report bookkeeping**
- Reports live in `reports/`. Latest = `ppc-2day-latest.md`; dated copy uses
  the RUN date: `ppc-2day-YYYY-MM-DD.md`. Compare each run against the
  previous `ppc-2day-*` dated file (not the latest, which you're overwriting).
- This first run is the baseline; no prior report to compare against.

**Data snapshot (baseline, 25–26 Aug 2026):** 209 impr, 3 clicks, $0.75
spend, 0 sales. Account is in launch/warm-up; 8 of 15 campaigns had 0
impressions.
