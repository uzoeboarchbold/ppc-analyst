# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Environment / API setup
- **Credentials**: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN` are valid.
  Token endpoint: `https://api.amazon.com/auth/o2/token` (grant_type=refresh_token).
  Access token lasts 3600s.
- **Region**: Account is **North America** → base URL `https://advertising-api.amazon.com`.
  EU (`-eu`) and FE (`-fe`) endpoints are **blocked by the agent proxy** (403 "no rule or
  network setting allows this host"). Only NA is reachable. Don't waste tries on EU/FE.
- **`AMZ_PROFILE_ID` IS MISCONFIGURED** (as of 2026-11-21). The env var holds a 50-char
  alphanumeric string, NOT a numeric Amazon profile ID. It matches none of the real profiles.
  - The account has 3 profiles (all sellers): **US `26765323558215`**, CA `2840235221595557`,
    MX `3892485344323414`.
  - **Only the US profile has advertising activity** (54 SP campaigns; CA/MX have 0).
  - **FIX: always use the US profile `26765323558215`** as `Amazon-Advertising-API-Scope`
    until the env var is corrected. If a future run finds the env var now contains a valid
    numeric profile ID that matches a real profile, prefer that instead.

## API usage notes
- v2 endpoints (e.g. `/v2/sp/campaigns`) return 404 "Method Not Found" — **deprecated**.
  Use **v3**: `POST /sp/campaigns/list` with headers
  `Content-Type: application/vnd.spCampaign.v3+json` and matching `Accept`.
- Reporting uses the **v3 async Offline Reports** API:
  `POST /reporting/reports` → poll `GET /reporting/reports/{id}` until status COMPLETED →
  download the gzipped JSON from the returned URL.
  - Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`,
    `timeUnit=SUMMARY`. `topOfSearchImpressionShare` only available here (campaign level).
  - Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]` — use for
    wasted-spend negatives and well-converting exact-match suggestions.
  - Use `sales7d`, `purchases7d`, `acosClicks7d`, `roasClicks7d` as the conversion columns.

## API gotchas learned
- v3 report columns are report-type specific: `acosClicks7d`/`roasClicks7d` are **invalid for
  `spCampaigns`** (400 error). Just request `cost` + `sales7d` + `purchases7d` and compute
  ACOS (=cost/sales) and ROAS (=sales/cost) yourself. They ARE valid for `spSearchTerm`.
- Report date range max is **31 days per request**; older than ~60 days returns 400 (retention).
  To check long history, loop multiple ≤31-day windows.
- Report status/create content-type: `application/vnd.createasyncreportrequest.v3+json`.

## KEY ACCOUNT FINDING (2026-11-21 run) — ZERO DELIVERY
- The US account has **15 ENABLED SP campaigns** ("SP Isolated ... Exact/Phrase" single-keyword
  builds), started 2026-05-18, daily budgets only **$1.50** (one at $2.50) ~= $23.50/day total.
- They have served **ZERO impressions / clicks / spend / sales for the ENTIRE queryable history**
  (checked Sep 29 – Nov 18 2026, all zero). Not a data bug — reports populate fine, values are 0.
- Likely causes to flag: bids too low to ever win auctions at $1.50 budgets; products out of
  stock / not Buy-Box eligible (ads can't serve); or account-level billing/payment/suspension.
  Owner must check Seller Central (stock, Buy Box, billing) and Ad Console (bids, eligibility).
- Because there is no traffic, the search-term report returns 0 rows (expected), so there are no
  negatives or exact-match suggestions to make until delivery resumes.
- **ACTION for future runs**: if still zero, keep flagging it prominently — this is the single
  most important thing to tell the owner until ads actually start serving.

## Date window logic (data lags ~48h)
- End the window 48h before "now", then take full calendar days (UTC) before that boundary.
- 2-day report = the 2 full UTC days ending ~48h before run.
  e.g. run Sat 2026-11-21 23:09 UTC → window 2026-11-17 to 2026-11-18.

## Delivery (Drive + email)
- **Google Drive**: folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo` (owner
  uzoebo.archbold@gmail.com). Upload .md with `create_file` using `base64Content` file-reference
  `sha256:<hash>:/abs/path` + `contentMimeType: text/markdown` + `disableConversionToGoogleType:true`.
  `update_file` is metadata-only — to replace content, trash the old file and create a new one.
- **EMAIL NOT POSSIBLE in this session (2026-11-21)**: Gmail connector is connected at org level
  but `enabledInChat: false`, so NO Gmail/send tool loads here (ListConnectors confirms). There is
  no other email mechanism available. Until the user enables the Gmail connector's tools for this
  automated workflow in claude.ai connector settings, the email step will keep failing. Report this
  each run (note in report footer + notify user) rather than silently skipping.

## Reports / comparison
- Save to `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-[YYYY-MM-DD].md`.
- Compare against the previous 2-day report (previous dated file or the latest before overwrite).
- 2026-11-21: first 2-day run — no prior report to compare against; noted in report.
