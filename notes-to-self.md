# Notes to Self — PPC Analyst

Running log of lessons so future runs are faster and more reliable.

## Credentials & account (learned 2026-09-30)
- `AMZ_PROFILE_ID` env var is set to `amzn1.application...` — that is an
  **application id, NOT a numeric advertising profile id**. Do not send it in
  the `Amazon-Advertising-API-Scope` header; the API needs a numeric profileId.
- Correct profiles (from `GET /v2/profiles`, NA endpoint):
  - **US seller `26765323558215` (USD)** — the ONLY profile with Sponsored
    Products campaigns. **Use this one.**
  - CA `2840235221595557` and MX `3892485344323414` — 0 campaigns, ignore.
- Region: **NA only** (`advertising-api.amazon.com`). EU/FE hosts are blocked
  by the outbound proxy (403 CONNECT tunnel), so don't try them.
- Token refresh works via `https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token + client_id + client_secret. Access tokens last ~1h.

## Reporting API v3 (learned 2026-09-30)
- Async flow: POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`) → poll GET
  `/reporting/reports/{id}` until `COMPLETED` → download `url` (GZIP JSON).
- **Max date range per report = 31 days.** Split longer look-backs.
- Campaign report (`spCampaigns`, groupBy `campaign`) does **NOT** accept
  `acosClicks7d` / `roasClicks7d` (those are targeting-report columns).
  Pull `cost`, `sales7d`, `purchases7d`, `clicks`, `impressions`,
  `clickThroughRate`, `costPerClick`, `topOfSearchImpressionShare` and
  **compute ACOS = cost/sales, ROAS = sales/cost** yourself.
- Reports return **0 rows when there were genuinely 0 impressions** — that is
  data, not an error. Confirm with a wider diagnostic window before concluding.

## Account health note (2026-09-30)
- Account is effectively **dormant**: trailing 31 days (Aug 28–Sep 27) had only
  ~918 impressions, ~$0.60 spend, **$0 sales** across ~20 enabled campaigns.
  The most recent ~10 days (incl. the report window) show **zero delivery**.
- Likely causes to investigate: bids too low to win any auction, $1.50 daily
  budgets, and/or listings out of stock / suppressed. Flag this prominently —
  it is the real story, not the (empty) 2-day table.

## Delivery channels (learned 2026-09-30)
- **Google Drive: works.** Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with create_file, `contentMimeType: text/markdown`,
  `disableConversionToGoogleType: true` so it stays a .md file.
- **Email: BLOCKED.** The Gmail connector is connected at the org level but
  `enabledInChat: false` — its tools do not load in this automated session, and
  a hands-off run cannot toggle it on. **Action for the user:** enable the Gmail
  connector for this chat/session in connector settings so future runs can email
  the report. Until then, the report reaches you via the Drive upload, the git
  commit, and the push notification. No SMTP fallback is available (no creds).

## Reports of each type
- 2-day: `reports/ppc-2day-latest.md` + dated `reports/ppc-2day-YYYY-MM-DD.md`.
- First 2-day report generated 2026-09-30 (no prior report to compare against).
