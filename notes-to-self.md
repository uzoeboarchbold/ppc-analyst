# Notes to Self — PPC Analyst

Running log of lessons so each run is smoother than the last. Newest at top.

## 2026-10-21 (first 2-day run)

**Credentials / profile**
- Amazon Ads token exchange works at `https://api.amazon.com/auth/o2/token` with
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` / `AMZ_REFRESH_TOKEN`. Token lives ~1h.
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It holds an *application* id
  (`amzn1.application.…`), NOT a numeric profile id. Do not pass it as
  `Amazon-Advertising-API-Scope` — it will not work.
- The refresh token has access to 3 NA seller profiles under account
  "Uzoebo Archbold E-Commerce" (`A1C2I8MOP52E35`):
  - US `26765323558215` (USD, dailyBudget 40, **validPaymentMethod: false**) ← active ad account, use this
  - CA `2840235221595557` (CAD, placeholder max budget)
  - MX `3892485344323414` (MXN, placeholder max budget)
- Only the **NA** endpoint (`https://advertising-api.amazon.com`) is reachable.
  EU/FE endpoints are blocked by the egress proxy (403) — don't bother.
- Use the **US profile `26765323558215`** unless told otherwise. It's the one
  with real campaigns (product ASIN B0FXW3GW5F, cat deterrent / pet odor).

**Reports API (v3)** — this works:
- Submit: `POST /reporting/reports`, header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Body config: `adProduct:"SPONSORED_PRODUCTS"`, `timeUnit:"SUMMARY"`,
  `format:"GZIP_JSON"`, `reportTypeId` + matching `groupBy`/`columns`.
  - campaign: reportTypeId `spCampaigns`, groupBy `["campaign"]`
  - keyword/target: reportTypeId `spTargeting`, groupBy `["targeting"]`
  - search terms: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`
- Poll `GET /reporting/reports/{id}` until status `COMPLETED` (~60–120s each),
  then download the presigned `url` (NO auth header) and gunzip.
- Compute CTR/CPC/ACOS/ROAS myself from base columns (impressions, clicks,
  cost, purchases30d, sales30d) — more reliable than requesting derived cols.
  `topOfSearchImpressionShare` is accepted on spCampaigns.

**Key finding this run**
- US account shows **ZERO impressions/clicks/cost/sales for all of Oct 1–18**
  across all 15 campaigns, even though they're ENABLED. Almost certainly because
  **validPaymentMethod is false** on the US profile — Amazon won't serve ads
  without a valid payment method. This is a business problem to surface, not a
  data bug. The pull is healthy; the account is simply not spending.
- Running CA/MX check to confirm spend isn't happening on another marketplace.

**Workflow**
- Reports folder: `reports/`. Overwrite `ppc-2day-latest.md`, save dated copy
  `ppc-2day-YYYY-MM-DD.md`. Commit to branch `claude/great-hopper-j486iz`.
- Google Drive folder "PPC Reports" id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo` (upload
  as text/markdown, disableConversionToGoogleType=true to keep the table intact).
- **EMAIL CANNOT BE SENT from this session.** The Gmail connector is connected but
  `enabledInChat: false`, so no gmail send tool is available. Report is saved to repo +
  Drive instead. To fix: user must enable Gmail in chat (connectors settings). Until then,
  state in every report that email was not sent and point to the Drive copy.
- Confirmed CA (`2840235221595557`) and MX (`3892485344323414`) profiles have 0 campaigns
  and 0 activity — all advertising lives on the US profile.
- Date window (2-day): data lags 48h, so cover the 2 full calendar days before
  the day that falls 48h prior to run time. 2026-10-21 run → Oct 17 & 18.
- No previous 2-day report existed on this run (first run) → no comparison.
