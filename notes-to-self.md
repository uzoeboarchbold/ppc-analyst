# Notes to self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## 2026-07-11 (first run — 2-day report)
- **Region:** Account is North America. Use `https://advertising-api.amazon.com`.
  EU/FE endpoints are blocked by the network proxy (CONNECT 403) — don't bother.
- **PROFILE ID GOTCHA:** The env var `AMZ_PROFILE_ID` holds an *application* id
  (`amzn1.application....`), NOT a numeric advertising profile id. The API needs a
  numeric profile in the `Amazon-Advertising-API-Scope` header. Real profiles on this
  account (from `GET /v2/profiles`):
    - US  seller: `26765323558215` (USD, $40 daily budget) ← the live/active one, USE THIS
    - CA  seller: `2840235221595557`
    - MX  seller: `3892485344323414`
  Hard-coded US profile in the pull script. If a future run should cover CA/MX too, add them.
- **LWA token:** POST https://api.amazon.com/auth/o2/token with grant_type=refresh_token,
  refresh_token, client_id, client_secret. Works, token lasts 3600s.
- **Reporting API v3 column gotcha:** `spCampaigns` groupBy=campaign does NOT accept
  `acosClicks7d` / `roasClicks7d` (400 error). Those are only valid on `spTargeting` /
  `spSearchTerm`. For campaigns, request `cost` + `sales7d` and compute ACOS = cost/sales,
  ROAS = sales/cost yourself. `topOfSearchImpressionShare` IS valid on spCampaigns.
  Content-Type for create must be `application/vnd.createasyncreportrequest.v3+json`.
- **Report flow:** POST /reporting/reports → poll GET /reporting/reports/{id} until
  status COMPLETED → download the gzipped-JSON `url`. Reports finish in <30s here.
- **DATA STATE:** Account is essentially DORMANT. Last 30 days: only 159 impressions total
  (all on 2026-06-09, zero clicks), nothing else. Both campaigns ("SP KT | ST w/ Sales",
  "SP PT | ST w/ Sales") are ENABLED but delivering ZERO impressions. So all-zero reports
  are EXPECTED and REAL, not a bug — do not treat zeros as a pull failure. The real story to
  report is "enabled campaigns are not delivering." Re-verify with a wider-window sanity pull
  before declaring zeros.
- **Date window:** run 2026-07-11 23:03 UTC → 48h lag → covered 2026-07-07 & 2026-07-08.
- **TODO for next run:** find/confirm a Gmail send tool and the Google Drive 'PPC Reports'
  folder id (see report delivery notes in the run log).
