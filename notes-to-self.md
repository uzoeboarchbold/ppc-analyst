# Notes to self — PPC Analyst

Running log of lessons so future runs are smoother. Newest first.

## 2026-10-14 — AMZ_PROFILE_ID is malformed (blocker)
- The reporting pipeline works. Auth against the NA token endpoint
  (`https://api.amazon.com/auth/o2/token`) succeeds and the Sponsored
  Products v3 reporting API (`https://advertising-api.amazon.com/reporting/reports`)
  accepts a create-report request (HTTP 200) when given a genuine profile.
- BUT the configured `AMZ_PROFILE_ID` is not a valid Amazon Ads profile ID:
  it is ~50 characters and non-numeric. A real Ads profile ID is a short
  integer (10–12 digits). Amazon returns HTTP 400
  `"profile ID required"` for it.
- The refresh token belongs to a **NA** account exposing **3 profiles:
  CA, MX, US**. The configured value matches none of them.
- EU/FE token endpoints (`api.amazon.co.uk`, `api.amazon.co.jp`) are blocked
  by this environment's network policy (proxy returns 403 on CONNECT), so a
  valid EU/FE profile could not be reached from here anyway.
- ACTION NEEDED FROM OWNER: set `AMZ_PROFILE_ID` to the correct numeric
  profile ID for the account to report on. If it's a US FBA account, it is
  one of the three NA profiles. Once set, this report should produce real
  data with no code changes.
- Did NOT invent numbers and did NOT substitute another profile's data.

## How-to reminders (confirmed working this run)
- Token: POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token.
- Headers for Ads API: `Authorization: Bearer <tok>`,
  `Amazon-Advertising-API-ClientId: <AMZ_CLIENT_ID>`,
  `Amazon-Advertising-API-Scope: <AMZ_PROFILE_ID>`.
- Reporting v3: POST `/reporting/reports` (content-type
  `application/vnd.createasyncreportrequest.v3+json`), poll
  GET `/reporting/reports/{id}` until COMPLETED, download the gz URL.
- Report types used: `spCampaigns` (groupBy campaign; has
  topOfSearchImpressionShare), `spTargeting` (groupBy targeting),
  `spSearchTerm` (groupBy searchTerm) for exact-match candidates.
- Never print credential values — the environment blocks it.
- 2-day window logic: window ends 48h before run; cover the 2 full days
  ending at the last fully-finalised day. This run (Wed 2026-10-14 23:19 UTC)
  → covered 2026-10-10 and 2026-10-11.
