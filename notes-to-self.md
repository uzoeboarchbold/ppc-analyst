# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / API facts (confirmed 2026-07-14)
- **Region:** North America. Use host `https://advertising-api.amazon.com`.
  EU/FE hosts are blocked by the egress proxy (403) — don't bother trying them.
- **Token refresh:** `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client id/secret. Works. Access tokens are
  short-lived (~1h) — refresh at the start of each script.
- **IMPORTANT — AMZ_PROFILE_ID is malformed.** The env var is set to an LWA
  application id (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), which is
  NOT a valid Ads API profile id. The real numeric profile ids for this account
  (from `GET /v2/profiles`) are:
    - `26765323558215`  US / USD  (seller) — **ACTIVE, ~50 SP campaigns. USE THIS.**
    - `2840235221595557` CA / CAD (seller) — 0 campaigns
    - `3892485344323414` MX / MXN (seller) — 0 campaigns
  So: ignore AMZ_PROFILE_ID, use the US profile `26765323558215` (USD) via the
  `Amazon-Advertising-API-Scope` header. If a future run sees campaigns appear
  in CA/MX, revisit.
- Account name: "Uzoebo Archbold E-Commerce". Product line looks like a pet
  odor / cat deterrent / litter niche (ASIN B0FXW3GW5F).

## Reporting API (v3 async)
- `POST /reporting/reports` with Content-Type
  `application/vnd.createasyncreportrequest.v3+json`.
- Reports used:
    - campaigns: reportTypeId `spCampaigns`, groupBy `["campaign"]`
    - targeting: reportTypeId `spTargeting`, groupBy `["targeting"]`
    - search terms: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`
- `topOfSearchImpressionShare` is a valid column on spCampaigns.
- Purchases/Sales: use `purchases7d` / `sales7d` (7-day attribution) for a
  recent 2-day window.
- timeUnit `SUMMARY`, format `GZIP_JSON`. Poll `GET /reporting/reports/{id}`
  until status=COMPLETED, then download the presigned `url` (NO auth header on
  the S3 download), gunzip, parse JSON. Reports can take ~1–3 min to generate;
  poll in the background so the shell doesn't time out.

## Date window logic (data lags 48h)
- 2-day report covers the 2 full days ending 48h before run time.
- Run 2026-07-14 → window = 2026-07-10 and 2026-07-11.

## Delivery
- Save reports to `reports/`: overwrite `ppc-2day-latest.md` + dated
  `ppc-2day-YYYY-MM-DD.md`. Commit to branch `claude/great-hopper-5zrqfe`.
- Upload to Google Drive folder "PPC Reports".
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".

## Run history
- 2026-07-14: First run. No previous 2-day report to compare against.
