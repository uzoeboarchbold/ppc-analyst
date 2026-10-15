# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Account / credentials
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an application-ID string
  (`amzn1.application.…`), NOT a numeric advertising profile ID. Do not pass it
  as the API scope — it will fail. Resolve the real profile yourself.
- **Correct profile to use: `26765323558215`** — US marketplace (ATVPDKIKX0DER),
  USD, seller account "Uzoebo Archbold E-Commerce". This is the only profile with
  Sponsored Products campaigns (54 campaigns). The other two profiles
  (`2840235221595557` = CA, `3892485344323414` = MX) have **0** SP campaigns.
- Region is **NA** → host `https://advertising-api.amazon.com`.
  The EU (`-eu`) and FE (`-fe`) hosts are **blocked by the egress proxy
  (403 Forbidden)** — don't waste retries on them; this account is NA anyway.
- LWA token exchange works: POST `https://api.amazon.com/auth/o2/token` with
  refresh_token grant. Token lasts 3600s. Always pass CA bundle
  `/root/.ccr/ca-bundle.crt` to Python ssl context (proxy re-terminates TLS).

## Reporting API (v3) — working recipe
1. POST `/reporting/reports` with `Content-Type:
   application/vnd.createasyncreportrequest.v3+json`.
2. Body: `{name, startDate, endDate, configuration:{adProduct:"SPONSORED_PRODUCTS",
   groupBy:[...], columns:[...], reportTypeId, timeUnit:"SUMMARY"|"DAILY",
   format:"GZIP_JSON"}}`.
3. Poll GET `/reporting/reports/{id}` until `status==COMPLETED`; typically ready
   in ~1.5–2 min.
4. Download the presigned S3 `url` (NO auth headers), gunzip, `json.loads`.
- Campaign report: `reportTypeId:"spCampaigns"`, `groupBy:["campaign"]`.
  Good columns: campaignName, campaignId, impressions, clicks, cost,
  purchases7d, sales7d, topOfSearchImpressionShare, date (date only if DAILY).
- Search-term report: `reportTypeId:"spSearchTerm"`, `groupBy:["searchTerm"]`.
- CTR, CPC, ACOS, ROAS are NOT returned — compute them:
  CTR=clicks/impr, CPC=cost/clicks, ACOS=cost/sales, ROAS=sales/cost.
- Attribution: used 7-day (`purchases7d`/`sales7d`). For very recent days
  conversions may still mature; note this in reports.

## CRITICAL ongoing issue (first seen run 2026-10-15)
- **The US profile has `validPaymentMethod: false`.** As a result the account is
  serving **ZERO ads** — 0 impressions/clicks/cost/sales across the entire
  account for at least the last month (verified Sep 15 – Oct 12, 2026), despite
  15 campaigns being ENABLED (budgets $1.50–$2.50/day; account daily budget $40).
- This is NOT a data-pull failure — the API returns successfully with all-zero
  rows. Report it as a business problem: **fix the payment method in Seller
  Central / Ad console to restart delivery.**
- Until delivery resumes, every report will be all zeros. Keep flagging it at the
  top of each report and keep checking `validPaymentMethod` on the profile each run.

## Email delivery (run 2026-10-15)
- **Could NOT send the email.** The Gmail connector is installed and connected
  at the org level but is **toggled OFF for this chat/session**
  (`enabledInChat: false`), so no Gmail tools load here and there is no other
  mail tool. Google Drive upload works fine; email does not.
- Fix for future runs: enable the **Gmail** connector for this session/scheduled
  task in the connector settings so its tools load. Until then, the report is
  still delivered via the repo commit and the Drive 'PPC Reports' folder, and the
  owner should be told the email could not be sent.

## Date window logic (data lags ~48h)
- Endpoint = now − 48h. Cover the last fully-finalised calendar days ending at/
  before that point. For the 2-day report, that's the 2 full days whose data is
  ≥48h old. Run 2026-10-15 23:19 UTC → covered **Oct 11–12, 2026**.
