# Notes to Self — PPC Analyst

Running log of lessons so future runs work better. Newest notes at top.

## 2026-10-07 — First run (2-day report)
- **EMAIL COULD NOT BE SENT.** The Gmail connector is installed/authenticated
  but `enabledInChat:false`, so its tools are not loaded in this automated
  session and there's no way to send mail from here. The owner must enable
  the Gmail connector for this chat/session in connector settings for future
  runs to email automatically. Report was still committed, pushed, and
  uploaded to the 'PPC Reports' Google Drive folder.
- **AMZ_PROFILE_ID is misconfigured.** The env var holds an *application* ID
  (`amzn1.application.xxxx`), NOT a numeric Advertising profile ID. The
  reporting API needs the numeric profile ID in the
  `Amazon-Advertising-API-Scope` header. Do not pass AMZ_PROFILE_ID to that
  header — it will fail. Resolve the profile at runtime instead (see below).
- **How to resolve the right profile:** `GET /v2/profiles` on the NA host
  (`https://advertising-api.amazon.com`) returns the account profiles. For
  this account (seller "Uzoebo Archbold E-Commerce", id A1C2I8MOP52E35):
  - US (profileId `26765323558215`, ATVPDKIKX0DER, USD) — has all 15 SP
    campaigns. **Use this profile.** Note: `validPaymentMethod:false`.
  - CA (profileId `2840235221595557`) — no campaigns.
  - MX (profileId `3892485344323414`) — no campaigns.
  - Region is **NA**; EU/FE hosts are blocked by the proxy (403) anyway.
- **Token exchange** at `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id + client_secret works fine.
- **Reporting flow (v3):** POST `/reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`; poll
  `GET /reporting/reports/{id}` until status COMPLETED; download the
  presigned `url` (GZIP JSON, no auth header on the download).
  - Campaigns: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
  - Search terms: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
  - Columns used: impressions, clicks, cost, costPerClick,
    clickThroughRate, purchases30d, sales30d, acosClicks14d,
    roasClicks14d, topOfSearchImpressionShare.
  - Reports take ~1–2 min to generate.
- **KEY FINDING this run:** The US account has 15 SP campaigns but ZERO
  impressions/clicks/spend/sales — not just in the Oct 3–4 window but across
  the whole of Sep 24–Oct 5. Campaigns are not serving. Most likely cause:
  no valid payment method on the US seller account
  (`validPaymentMethod:false`). This is a real business finding, not an API
  error — do NOT invent numbers. If future runs still show all zeros, the
  owner needs to fix billing / check whether campaigns are enabled.
- The helper script used lives in scratch (`pull.py`); re-create as needed.
