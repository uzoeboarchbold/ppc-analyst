# Notes to self — PPC Analyst automation

Running log of lessons so each run gets smoother. Newest at top.

## 2026-08-19 (first run — 2-day report)
- **PROFILE ID IS WRONG IN ENV.** `AMZ_PROFILE_ID` = `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`
  is an *application* ID, not an Ads *profile* ID. The API returns 400 "Invalid scope".
  **Workaround used:** call `GET /v2/profiles` (no scope header) to list profiles, then use the
  **US profile `26765323558215`** (USD, marketplace ATVPDKIKX0DER). Other profiles on this account:
  CA `2840235221595557`, MX `3892485344323414`. Until the env var is fixed, hardcode/lookup the US one.
- **Region = NA only.** The egress proxy allows `advertising-api.amazon.com` (NA) but BLOCKS
  `advertising-api-eu.amazon.com` and `-fe` (403 at CONNECT). This US account lives in NA, so fine.
  Don't waste retries on EU/FE endpoints.
- **Token exchange works** against `https://api.amazon.com/auth/o2/token` with the env client id/secret/refresh token.
  Always pass `s.verify='/root/.ccr/ca-bundle.crt'` on requests or TLS fails through the proxy.
- **Reporting = SP v3 async.** POST `/reporting/reports` with `configuration.reportTypeId` in
  {spCampaigns, spTargeting, spSearchTerm}, `timeUnit:"SUMMARY"`, `format:"GZIP_JSON"`,
  `adProduct:"SPONSORED_PRODUCTS"`. Poll `GET /reporting/reports/{id}` (~6s interval) until
  `status=="COMPLETED"`, then download the presigned `url` and gzip-decompress. Each report takes
  ~1–2 min. Campaign report supports `topOfSearchImpressionShare` with groupBy=["campaign"].
  Used `purchases7d`/`sales7d` for attribution.
- **EMAIL NOT AVAILABLE.** Gmail connector is installed but `enabledInChat:false` for this automated
  session — cannot send email. Report saved to repo + uploaded to Google Drive instead. Ask user to
  enable Gmail connector for the automation, then add the email step back.
- **Reports folder + notes-to-self.md did not exist** on first run; created both.
- **Data volume is tiny.** 15–16 Aug: 81 impressions, 1 click, $2.16 spend, $0 sales across 11 campaigns.
  Almost nothing served. Watch this — likely bids/budgets throttling delivery, not an ads-efficiency issue.
- **Escape `|` in campaign names** before putting them in a markdown table (several campaigns contain `|`).

## Date-window rule (reminder)
- Data lags ~48h. For the 2-day report, cover the 2 full finalised days ending 48h before run time.
  Run 2026-08-19 23:04 UTC → 48h back = 2026-08-17 mid-day → last 2 fully-finalised days = **15–16 Aug**.
