# Notes to self — PPC Analyst runs

Keep this short and practical. Add a lesson whenever a run hits a snag.

## Account / environment facts
- **Business:** Uzoebo Archbold E-Commerce. Advertising lives on the **US** marketplace only.
- **Correct advertising profile ID = `26765323558215`** (US, USD). CA (`2840235221595557`) and MX (`3892485344323414`) exist but have **zero** Sponsored Products campaigns — do not report on them.
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` (an *application* ID, ~50 chars), **not** a numeric profile ID. Every run must ignore it and use `26765323558215`. The Aug reports already asked the owner to fix this; still not fixed as of 20 Oct 2026.
- Auth works: POST `https://api.amazon.com/auth/o2/token` with `grant_type=refresh_token` + client id/secret + refresh token → `access_token` (1h). Region endpoint: `https://advertising-api.amazon.com` (North America).

## Reporting API gotchas (SP v3 async reporting)
- Create: POST `/reporting/reports`, header `Content-Type: application/vnd.createasyncreportrequest.v3+json`, header `Amazon-Advertising-API-Scope: <profileId>`.
- **ACOS/ROAS columns:** only `acosClicks14d` / `roasClicks14d` / `...7d` exist. There is **no** `acosClicks30d`/`roasClicks30d` — a 400 lists allowed columns. Compute ACOS = cost/sales, ROAS = sales/cost yourself from `cost` and `sales30d`.
- Conversions/sales use `purchases30d` / `sales30d`.
- Campaign report `reportTypeId: spCampaigns`, groupBy `["campaign"]`; search-term `spSearchTerm`, groupBy `["searchTerm"]`.
- Poll `/reporting/reports/{id}` until `status=COMPLETED`, download the gzipped URL, `gunzip`, parse JSON. Reports take ~1–2 min. A report with no delivery returns an **empty array** (`[]`, fileSize 22).

## Standing problem (as of 20 Oct 2026) — ACCOUNT IS DARK
- **US profile `validPaymentMethod` = false.** With no valid payment method, Amazon will not serve the ads. This is almost certainly why impressions are now **0**.
- History: Aug 13–14 had a trickle (72 impressions, still $0 spend/sales); by Oct 16–17 it is **0 impressions** — delivery has fully stopped, consistent with the payment method lapsing.
- 15 campaigns ENABLED, 32 PAUSED, 7 ARCHIVED. Budget ($40/day) is NOT the cap — spend is $0.
- **Action for owner:** add/fix a valid payment method on the US advertising account, then bids/eligibility.

## Email step — NOT POSSIBLE in this environment
- There is **no email/Gmail send tool** available here (only Google Drive + GitHub MCP). The report cannot be emailed automatically. It IS saved to the repo and uploaded to the Drive "PPC Reports" folder. Flag the missing email in the report header and the owner notification until an email tool is connected.

## Drive
- "PPC Reports" folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Prior 2-day reports are stored there (as Google Docs). Latest before this run: `ppc-2day-2026-08-16.md` (covers 13–14 Aug). NOTE: there is a ~2-month gap — the routine evidently did not run between mid-Aug and 20 Oct.

## Date window logic (2-day report)
- Data lags ~48h. End the window 48h before run time, then take the 2 full days before that. Run 20 Oct 23:10 UTC → cover **16 & 17 Oct 2026**.
