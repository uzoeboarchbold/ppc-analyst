# Notes to self — PPC Analyst

Persistent lessons so future automated runs work better. Read this first, every run.

## Account / API facts (learned 2026-09-27)
- **The `AMZ_PROFILE_ID` env var is MISCONFIGURED.** Its value is a 50-char
  application ID (`amzn1.application....`), NOT a numeric Amazon Ads profile ID.
  Using it as the `Amazon-Advertising-API-Scope` header fails with
  `Invalid scope` / `profile ID required`. **Do not rely on it.**
- Discover profiles yourself: `GET /v2/profiles` on the NA endpoint with only
  `Amazon-Advertising-API-ClientId` + `Authorization` (NO scope header).
- The account ("Uzoebo Archbold E-Commerce", seller A1C2I8MOP52E35) has 3 profiles:
  - **US / USD → profileId `26765323558215`  ← THIS is the active advertising account. USE THIS.**
  - CA / CAD → `2840235221595557` (no SP activity)
  - MX / MXN → `3892485344323414` (no SP activity)
- Region: **NA only** — `https://advertising-api.amazon.com`. The EU
  (`-eu`) and FE (`-fe`) hosts are BLOCKED by the network proxy (403). Don't retry them.
- Token endpoint: `https://api.amazon.com/auth/o2/token` (refresh_token grant) — works.
- Set `verify=/root/.ccr/ca-bundle.crt` on requests; outbound goes via the agent proxy.

## Reporting API (v3) notes
- Create: `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  Poll `GET /reporting/reports/{id}` until `COMPLETED`, download the presigned URL (GZIP_JSON).
- Valid campaign columns include: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, clickThroughRate, costPerClick, **acosClicks14d, roasClicks14d**
  (NOT `acosClicks7d`/`roasClicks7d` — those are rejected), topOfSearchImpressionShare.
- Campaign management state: `POST /sp/campaigns/list`
  (`Content-Type: application/vnd.spCampaign.v3+json`).

## Business state (as of 2026-09-27 run)
- **Ad delivery is completely OFF.** All campaigns went dark after **2026-09-02**:
  zero impressions/clicks/spend/sales from 2026-09-03 onward (verified through the window).
- The US profile shows **`validPaymentMethod: false`** — almost certainly the cause
  of the delivery halt. Owner needs to fix the billing/payment method in Seller Central.
- Prior 30 days (Aug 26–Sep 2 only had delivery): 1,120 impressions, $0.85 spend, **0 sales**.
  Even when delivering, campaigns got impressions but virtually no clicks/conversions.
- Many campaigns ENABLED at $1.50/day; product line = cat/pet odor products & cat tunnel beds
  (ASIN B0FXW3GW5F etc.). Nothing will spend until payment method is fixed.

## Report-window logic (confirmed correct)
- 2-day report: window = the 2 full days ending 48h before run time.
  Run Sun 2026-09-27 23:20 UTC → window = **Sep 23–24, 2026**. Matches the spec example.
- Previous 2-day window would be Sep 21–22.

## Comparison files
- This 2026-09-27 run is the FIRST 2-day report — no prior report to compare against.
- Future runs: compare against `reports/ppc-2day-latest.md` (previous) before overwriting it.
