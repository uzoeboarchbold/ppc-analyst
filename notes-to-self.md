# Notes to Self — PPC Analyst

Lessons learned from past runs. Read this before every run and apply it.

## Credentials / API access
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an *application* id
  (`amzn1.application.…`), not a numeric advertising profile id. Sending it as
  `Amazon-Advertising-API-Scope` gives `400 Invalid scope`.
  - **Fix:** enumerate profiles via `GET /v2/profiles` (NA host, **no** scope
    header needed). Then use the correct numeric profile id.
  - Profiles found under "Uzoebo Archbold E-Commerce":
    - **US (ATVPDKIKX0DER): `26765323558215`  ← primary, use this**
    - CA (A2EUQ1WTGCTBG2): `2840235221595557`
    - MX (A1AM78C64UM0Y8): `3892485344323414`
- LWA token refresh (`https://api.amazon.com/auth/o2/token`) works fine with the
  given client id / secret / refresh token. Access tokens last ~1h.
- **Region host:** `advertising-api.amazon.com` (NA). The EU
  (`advertising-api-eu…`) and FE (`advertising-api-fe…`) hosts are blocked by the
  outbound proxy (403). Our marketplaces are all NA, so this is fine.

## Reporting API (v3, `/reporting/reports`)
- Flow: POST to create → poll `GET /reporting/reports/{id}` every ~10s until
  `COMPLETED` → download the presigned `url` (GZIP_JSON, no auth headers) → gunzip.
- **Campaign report does NOT allow `acosClicks7d` / `roasClicks7d`** (only the
  14d variants). Pull `cost` + `sales7d` + `purchases7d` and compute
  ACOS = cost/sales and ROAS = sales/cost yourself.
- `topOfSearchImpressionShare` IS available at campaign level; it is `null` when
  there were no impressions.
- Working columns — campaign: campaignId, campaignName, impressions, clicks, cost,
  purchases7d, sales7d, clickThroughRate, costPerClick, topOfSearchImpressionShare.

## Account state (watch this)
- As of the 2026-11-07/08 window the account was **completely dormant**: all 15
  US campaigns had **zero** impressions/clicks/cost/sales, and this held across a
  14-day lookback (Oct 26 – Nov 8). CA and MX had no campaigns at all.
- Most likely cause: **US profile `validPaymentMethod: false`** → Amazon is not
  serving the ads. This is a billing/payment-method problem the owner must fix in
  Seller Central; nothing in the API will "turn ads back on".
- All campaigns target one main product, **B0FXW3GW5F** (cat deterrent spray / pet
  odor eliminator), plus one "Cat Tunnel Bed" campaign.
- When the account is dormant there are no search terms to harvest and no wasted
  spend to cut — say so plainly rather than padding the report.

## Report mechanics
- Report type windows: 2-day = 2 full days ending 48h before run.
  Run 2026-11-11 23:10 UTC → window = 2026-11-07 & 2026-11-08.
- Save to `reports/`: overwrite `ppc-2day-latest.md` + dated `ppc-2day-[run-date].md`.
- Previous report of this type = newest `ppc-2day-YYYY-MM-DD.md` before today's.
- Google Drive folder: "PPC Reports". Email to uzoebo.archbold@gmail.com.
