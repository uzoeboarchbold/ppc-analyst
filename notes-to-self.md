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
  the S3 download), gunzip, parse JSON. Reports usually take ~1–3 min, BUT the
  queue can be slow — on 2026-07-14 the spCampaigns + spSearchTerm reports sat
  in PENDING for 20+ min while spTargeting finished in <1 min. Poll in the
  background with a generous cap (~25 min).
- **Don't re-POST an identical report config** to "retry" a slow one — Amazon
  returns HTTP 425 `{"detail":"The Request is a duplicate of : <reportId>"}`
  and gives you back the SAME pending reportId. Just keep polling the original.
- **Zero-delivery shortcut:** if the spTargeting report returns 0 rows for the
  window, there was no ad delivery at all, so spCampaigns will be all-zeros too
  (targets are what serve). You can write the report confidently from that even
  if the campaign report is still stuck in the queue — just say so plainly.

## Date window logic (data lags 48h)
- 2-day report covers the 2 full days ending 48h before run time.
- Run 2026-07-14 → window = 2026-07-10 and 2026-07-11.

## Delivery
- Save reports to `reports/`: overwrite `ppc-2day-latest.md` + dated
  `ppc-2day-YYYY-MM-DD.md`. Commit to branch `claude/great-hopper-5zrqfe`.
- Upload to Google Drive folder "PPC Reports" (folder id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Use create_file with
  contentMimeType `text/markdown` + disableConversionToGoogleType=true to keep
  it as a real .md file.
- **Email step NOT possible:** there is NO email/Gmail connector in this
  environment (only Google-Drive + github MCP). Can't send the email. Save to
  repo + Drive and send a PushNotification to the owner instead. If an email
  connector is added later, wire it up.

## Run history
- 2026-07-14 (this run): 2-day report for window 2026-07-10→2026-07-11.
  Account STILL DARK — 2 enabled campaigns, 0 impressions/clicks/spend/sales.
  54 campaigns total (2 ENABLED, 45 PAUSED, 7 ARCHIVED). Compared against the
  previous 2-day report (9–10 Jul, generated 07-13) which was also all-zeros —
  no change. spTargeting=0 rows confirmed zero delivery; spCampaigns report was
  stuck PENDING 20+ min so wrote Part A from the confirmed zeros. Prior Drive
  history exists back to mid-June (repo `reports/` was empty this run, so the
  comparison baseline came from the Drive copy ppc-2day-2026-07-13.md).
