# PPC Analyst — Notes to Self

Running log of lessons so future automated runs work better. Newest at top.

## 2026-09-19 (first run)

### Environment / credentials
- **`AMZ_PROFILE_ID` is misconfigured.** It contains an LWA *application* id
  (`amzn1.application....`), NOT a numeric Amazon Ads profile id. The API's
  `Amazon-Advertising-API-Scope` header needs the numeric profile id or every
  data call fails.
- The account (`get /v2/profiles`, region **NA** = `advertising-api.amazon.com`)
  has three seller profiles under "Uzoebo Archbold E-Commerce":
  - **US: `26765323558215`** (USD)  ← primary marketplace, used for reports
  - CA: `2840235221595557` (CAD)
  - MX: `3892485344323414` (MXN)
- Until the env var is fixed, hardcode/select the **US** profile `26765323558215`.
  If a future run should cover CA/MX too, pull each profile separately.
- Auth works fine: refresh token → `https://api.amazon.com/auth/o2/token`
  (grant_type=refresh_token). Access token lasts 3600s.

### Amazon Ads reporting API (v3 async)
- Endpoint: `POST /reporting/reports`, then poll `GET /reporting/reports/{id}`
  until `COMPLETED`, then download the gzipped JSON from the `url`.
- Content-Type must be `application/vnd.createasyncreportrequest.v3+json`.
- **Column gotcha:** at CAMPAIGN level (`reportTypeId: spCampaigns`,
  groupBy `campaign`) `acosClicks7d`/`roasClicks7d` are INVALID — use
  `acosClicks14d`/`roasClicks14d`. At TARGETING level (`spTargeting`,
  groupBy `targeting`) the `...7d` columns ARE allowed.
- If a campaign/target has zero activity in the window, the targeting report
  can come back with 0 rows — that's normal, not an error.

### Account state (context for future comparisons)
- Account is in very early ramp-up. 30-day window ending 2026-09-16:
  ~1,580 impressions, 16 clicks, **$3.77** spend, **0 sales, 0 orders**.
- For the 2-day window Sep 15–16, every metric was genuinely **zero**
  (0 impressions/clicks/spend/sales). Reported the real zeros — did not invent.
- Because everything is ~zero, ACOS/ROAS/CTR are undefined (n/a).

### Report bookkeeping
- Reports live in `reports/`. Naming: `ppc-2day-latest.md` (overwrite each run)
  + dated `ppc-2day-YYYY-MM-DD.md` (run date).
- To compare next time: previous 2-day report = the most recent
  `ppc-2day-YYYY-MM-DD.md` before today's.
- Date window rule: 2-day report covers the 2 full days ending 48h before the
  run. Run 2026-09-19 → covered Tue 2026-09-15 & Wed 2026-09-16.

### Delivery
- Google Drive: upload report file to folder named **"PPC Reports"**.
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.

### Email delivery (blocker)
- **Could NOT email the report.** Gmail connector is `connected` at org level
  but `enabledInChat: false`, so no Gmail/send tool is loaded in the automated
  session. No email tool was reachable via ToolSearch either.
- Workaround used: saved to repo + uploaded to Drive "PPC Reports" folder.
- Fix: enable the Gmail connector for this session/chat (claude.ai connector
  settings) so future runs can email uzoebo.archbold@gmail.com.
