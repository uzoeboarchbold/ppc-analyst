# Notes to self — PPC Analyst (Amazon FBA)

Running log of lessons so each run gets smoother. Newest at top.

## 2026-10-08 (first run — 2-day report)

**Environment / credentials**
- Creds in env: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
  Never print their values — the sandbox blocks credential materialization and
  will deny the command.
- **`AMZ_PROFILE_ID` is MISCONFIGURED** — it is not a valid numeric Amazon
  profile ID (contains letters/punctuation). Had to discover the real profiles
  via `GET /v2/profiles`. The account ("Uzoebo Archbold E-Commerce") has three
  NA profiles:
  - **US  = 26765323558215 (USD)** ← active ads; this is the one to report on.
  - CA  = 2840235221595557 (CAD) — no activity.
  - MX  = 3892485344323414 (MXN) — no activity.
  If `AMZ_PROFILE_ID` is still broken on a future run, default to **US
  26765323558215**. (Flagged to the user to fix the env var.)

**Network / proxy**
- Outbound goes through the agent proxy. `api.amazon.com` (LWA token) and
  `advertising-api.amazon.com` (NA) are ALLOWED. The EU
  (`advertising-api-eu`) and FE (`advertising-api-fe`) hosts are **403 blocked**
  by egress policy — don't bother probing them; the account is NA anyway.
- One transient 403 on the NA host at session start cleared on retry. A single
  retry is fine for a transient tunnel 403; a persistent one is a policy block
  to report, not retry.

**Amazon Ads API v3 reporting gotchas**
- Use async reporting: `POST /reporting/reports` → poll `GET /reporting/reports/{id}`
  until `COMPLETED` → download the gzipped JSON `url`.
- Content-Type / Accept: `application/vnd.createasyncreportrequest.v3+json`.
- **Invalid columns:** `acosClicks7d` and `roasClicks7d` are NOT valid report
  columns and cause a 400. Request `cost`, `sales7d`, `purchases7d`, `clicks`,
  `impressions`, `topOfSearchImpressionShare`, `clickThroughRate`,
  `costPerClick`, `campaignName`, `campaignId` — and **compute ACOS = cost/sales
  and ROAS = sales/cost yourself.**
- Campaign report: `reportTypeId: spCampaigns`, `groupBy: [campaign]`.
  Targeting/keyword report: `reportTypeId: spTargeting`, `groupBy: [targeting]`.
- When there are zero impressions, the targeting report legitimately returns 0
  rows even though the campaign report lists the campaigns.

**Finding this run**
- All 15 ENABLED US campaigns delivered **zero** impressions/clicks/cost/sales
  for 4–5 Oct (and for the whole 22 Sep–5 Oct check). Root cause almost
  certainly **`validPaymentMethod: false` on the US ad account** → Amazon not
  serving ads. Told the user to fix billing + confirm listing B0FXW3GW5F is live.

**Date window logic (2-day report)**
- Data lags ~48h. Cover the 2 full days whose end is ≥48h before run time.
  Run 2026-10-08 23:19 UTC → window = 2026-10-04 and 2026-10-05.

**Delivery**
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`
  (used run date). Commit to branch `claude/great-hopper-3h6vvy`. ✅ done.
- Upload same file to Google Drive folder "PPC Reports" (id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). ✅ done via `create_file` (markdown,
  conversion disabled).
- **EMAIL COULD NOT BE SENT this run.** The Gmail connector is connected at org
  level but `enabledInChat: false` — toggled OFF for this session, so no send
  tool is available. **Action for user: enable the Gmail connector for this
  chat/session** so future runs can email automatically. Until then, the report
  still reaches the user via Drive + the run's push notification.
- Previous-report comparison (Part C): find the prior `ppc-2day-*.md` in reports/
  (excluding latest + today's) to diff headline metrics. First run had none.
