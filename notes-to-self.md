# Notes to Self — PPC Analyst (Amazon FBA)

Living memory for the automated PPC reporting runs. Read this first every run and add lessons learned.

## Account / API facts (verified 2026-09-22)

- **Region:** North America. Use endpoint `https://advertising-api.amazon.com`.
  The EU and FE endpoints are blocked by the outbound proxy (403) and aren't needed.
- **Token refresh:** `POST https://api.amazon.com/auth/o2/token` with
  `grant_type=refresh_token` + the 4 env creds. Works. Always pass
  `verify="/root/.ccr/ca-bundle.crt"` on requests (proxy CA bundle).
- **`AMZ_PROFILE_ID` env var is MISCONFIGURED.** It contains an
  `amzn1.application....` LWA *application* ID, **not** a numeric Ads profile ID.
  The v3 reporting `Amazon-Advertising-API-Scope` header needs the *numeric*
  profileId. **Workaround used:** call `GET /v2/profiles` to list the real
  profiles, then pick the active one. Ask the owner to fix the env var to the
  numeric profile id `26765323558215` (US).
- **Profiles on this account** (all seller "Uzoebo Archbold E-Commerce",
  seller id A1C2I8MOP52E35):
  - `26765323558215` — **US / USD / marketplace ATVPDKIKX0DER** ← the ONLY one
    with Sponsored Products campaigns. `validPaymentMethod: false`.
  - `2840235221595557` — CA / CAD — no SP campaigns.
  - `3892485344323414` — MX / MXN — no SP campaigns.
  So all reporting targets the **US profile `26765323558215`**.

## Reporting API gotchas

- Use the **v3 async reporting** API: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, then poll
  `GET /reporting/reports/{id}` until status COMPLETED, then GET the `url`
  (GZIP JSON).
- **Attribution window is 14d, NOT 30d** for this account's allowed columns.
  Use `purchases14d, sales14d, acosClicks14d, roasClicks14d`. (30d variants are
  rejected with HTTP 400 "invalid values".)
- Valid SP campaign columns include: campaignName, campaignId, campaignStatus,
  impressions, topOfSearchImpressionShare, clicks, clickThroughRate, cost,
  costPerClick, purchases14d, sales14d, acosClicks14d, roasClicks14d.
- `SUMMARY` timeUnit must NOT include a `date` column; `DAILY` must include it.
- The v2 `/v2/sp/campaigns` endpoint returns 404 (deprecated) — use v3 reporting.
- Report types available: `spCampaigns`, `spTargeting`, `spSearchTerm`.

## Standing situation (as of 2026-09-22)

- **US Sponsored Products ads are NOT delivering.** Zero impressions/clicks/
  spend/sales every day from at least 2026-09-05 through 2026-09-18, despite all
  15 campaigns being ENABLED. Almost certainly caused by
  `validPaymentMethod: false` on the US profile (Amazon pauses delivery when the
  billing method is invalid/expired). **First thing to check each run:** has the
  payment method been fixed and has delivery resumed? Flag this loudly until
  resolved.

## Date window rule

- Data lags ~48h. 2-day report covers the 2 full finalised days ending 48h
  before run. A day D is finalised at (D + 3 days) 00:00. Pick the most recent
  day whose finalisation instant <= now, and the day before it.
  - Example: run 2026-09-22 23:13 UTC → window = 2026-09-18 & 2026-09-19.

## Delivery targets

- Save reports in `reports/`: overwrite `ppc-2day-latest.md` + dated copy
  `ppc-2day-YYYY-MM-DD.md` (dated by run date). Commit + push to branch
  `claude/great-hopper-1herq4`.
- Upload same file to Google Drive folder **"PPC Reports"** (MCP Google-Drive).
- Email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
  (If no email tool/connector is available, note it in the report and here.)

## Comparison

- Compare each 2-day report against the previous 2-day report
  (`reports/ppc-2day-*.md`, second-newest). 2026-09-22 was the FIRST run — no
  prior report existed, so no comparison was possible.
