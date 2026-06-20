# Notes to Self — PPC Analyst

Running log of lessons so future runs go smoothly. Newest at top.

## 2026-06-20 (first run — 2-day report)

**Account / credentials**
- Token refresh works fine against `https://api.amazon.com/auth/o2/token` with
  `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`. Region = **NA**
  (`https://advertising-api.amazon.com`). EU/FE hosts are NOT in the network
  allowlist (403 "Host not in allowlist") — don't bother trying them.
- **IMPORTANT — `AMZ_PROFILE_ID` is WRONG.** It is set to
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, which is an *application
  ID*, not an Ads profile ID. The Reporting API rejects it with
  "profile ID required". The correct **numeric** profile for this seller
  ("Uzoebo Archbold E-Commerce", US/USD marketplace) is **`26765323558215`**.
  I get it from `GET /v2/profiles`. There are 3 profiles:
    - US  `26765323558215`  (USD, daily budget $40 — the ACTIVE ad account) ← use this
    - CA  `2840235221595557` (CAD, budget unset)
    - MX  `3892485344323414` (MXN, budget unset)
  Future runs: ignore `AMZ_PROFILE_ID`, pull profiles and select the US one
  (or whichever has a real budget / activity). Ask owner to fix the env var.
- Tip to check env values: `${#VAR}` measures the NAME length, not the value.
  Use `printf '%s' "$VAR" | wc -c` to check value length.

**Reporting API (v3, async)**
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: `reportTypeId: spCampaigns`, groupBy `["campaign"]`.
- Targeting: `reportTypeId: spTargeting`, groupBy `["targeting"]`.
- Search terms: `reportTypeId: spSearchTerm`, groupBy `["searchTerm"]`.
- Poll `GET /reporting/reports/{id}` until status COMPLETED, then GET the `url`
  (gzipped JSON). Reports take ~30-90s to generate.
- Metric columns used: impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare. NOTE: `topOfSearchImpressionShare` is only valid
  with timeUnit SUMMARY (not DAILY) and may be null when there are no impressions.
- Derive CTR, CPC, ACOS, ROAS myself from the raw columns.

**Data finding this run**
- Window 2026-06-16 → 2026-06-17 returned ZERO activity (empty `[]`). Verified
  it's real, not a query bug: broad Jun 1-17 report shows real spend (~$140, 2
  sales) but a daily breakdown shows activity stopped before ~Jun 10. Of 54
  campaigns only 2 are ENABLED and they got basically no impressions. **The ad
  account has gone dark / been paused.** Future runs: if a window is empty,
  always confirm with a broader report before reporting "no data".

**Delivery gaps in this environment (need owner action)**
- **No email tool** is available (no Gmail/SMTP MCP connected), so I cannot send
  the email. I save to repo + upload to Google Drive instead, and flag this.
- `PushNotification` is referenced for routines but is not exposed as a callable
  tool here — could not send a phone notification.
- Google Drive MCP IS available; 'PPC Reports' folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.

**Report bookkeeping**
- Previous 2-day report to compare against: look for `reports/ppc-2day-latest.md`.
  This run is the FIRST, so there was nothing to compare to.
