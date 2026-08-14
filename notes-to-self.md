# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest lessons on top.

## Environment / API access (learned 2026-08-14, first run)
- **Region / base URL:** Account is North America. Use `https://advertising-api.amazon.com`.
  The EU (`-eu`) and FE (`-fe`) hosts are NOT reachable from this container (proxy blocks
  them) — don't waste retries on them.
- **`AMZ_PROFILE_ID` env var is WRONG.** It contains an *application* ID
  (`amzn1.application.…`, 50 chars), NOT an advertising profile ID. Do not use it as the
  `Amazon-Advertising-API-Scope` header — it will fail.
  - Correct approach: call `GET /v2/profiles` and pick the profile. This account
    (`Uzoebo Archbold E-Commerce`, seller `A1C2I8MOP52E35`) has three profiles:
    - **US → profileId `26765323558215` (USD)  ← the only one with Sponsored Products campaigns. USE THIS.**
    - CA → `2840235221595557` (CAD) — no SP campaigns.
    - MX → `3892485344323414` (MXN) — no SP campaigns.
  - So all reports are US / USD until this changes.
- **OAuth:** POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token +
  client_id/secret. Works fine. Access token lasts ~1h.
- **TLS/proxy:** set `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt` for python `requests`,
  otherwise HTTPS through the agent proxy fails verification.

## Reporting API (v3 async) cheatsheet
- Create: `POST /reporting/reports` with header
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`. Response key is
  **`reportId`** (not `id`).
- **Duplicate reports return HTTP 425** with body
  `{"code":"425","detail":"The Request is a duplicate of : <reportId>"}`. Parse that
  reportId out of `detail` and just poll it instead of failing.
- Poll `GET /reporting/reports/{reportId}` until `status == COMPLETED`, then download the
  `url` (GZIP_JSON → gzip-decompress → JSON array). Empty report ⇒ tiny fileSize (~22 bytes)
  and 0 rows.
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`, `timeUnit=SUMMARY`,
  columns incl. `topOfSearchImpressionShare`, `purchases7d`, `sales7d`, `cost`.
- Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`. Returns **0 rows
  when there were no clicks** in the window (normal for this low-volume account).
- Attribution used: 7-day (`purchases7d` / `sales7d`).

## Email delivery — BLOCKED (2026-08-14)
- The task asks to email the report to uzoebo.archbold@gmail.com. **There is no Gmail send
  tool available in-session.** The Gmail connector exists but is `enabledInChat: false`, so
  its tools aren't loaded. Report was saved to repo + uploaded to Drive, but email could NOT
  be sent. FIX: user needs to enable the Gmail connector for this chat/automation, OR provide
  an SMTP/email-sending mechanism. Re-check `ListConnectors` each run in case it gets enabled.

## Account context
- Very low volume / ramp-up phase. Pet products (Pet Odor Eliminator, Cat Tunnel Bed, cat
  litter). Daily impressions ~25–70, clicks 0–1/day, near-zero spend. Ads are winning
  impressions but almost never clicks (top-of-search impression share mostly 0–17%). Likely
  bids too low / poor placement. Real business signal to flag, not a data error.
