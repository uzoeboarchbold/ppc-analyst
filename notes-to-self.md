# Notes to self — PPC Analyst runs

Lessons learned across runs. Read this first, every run.

## Credentials / config
- Env vars present: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
- **IMPORTANT — `AMZ_PROFILE_ID` is misconfigured.** It holds an LWA *application* id
  (`amzn1.application.…`), **not** a numeric advertising *profile* id. The reporting API
  rejects it with `400 "profile ID required"`. Workaround: call `GET /v2/profiles`, then use
  the numeric profile id in the `Amazon-Advertising-API-Scope` header.
- Account has 3 profiles (one seller, "Uzoebo Archbold E-Commerce"):
  - **US `26765323558215` (USD)** ← the only one with campaigns. Use this.
  - CA `2840235221595557` (CAD) — no campaigns.
  - MX `3892485344323414` (MXN) — no campaigns.
- Token refresh endpoint `https://api.amazon.com/auth/o2/token` works; access token lasts 1h.

## API gotchas
- **Do NOT use Python `urllib` for the Ads API.** `urllib.request` capitalizes header names
  (`Amazon-Advertising-API-Scope` → `Amazon-advertising-api-scope`) and Amazon's gateway
  treats the custom headers as case-sensitive → `400 "profile ID required"`. Use `curl`
  (via subprocess) or `requests`, which preserve header case. See `scratchpad/pull.py`.
- Reporting v3 (async): `POST /reporting/reports` with Content-Type/Accept
  `application/vnd.createasyncreportrequest.v3+json`; poll `GET /reporting/reports/{id}`
  until `COMPLETED`; download the presigned `url` (no auth headers) and gunzip.
- Report type ids used: `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy
  `targeting`), `spSearchTerm` (groupBy `searchTerm`). `topOfSearchImpressionShare` is a
  valid column on `spCampaigns`.
- Rows with all-zero metrics are **omitted** from short-window reports (a 2-day pull returns
  `[]` when there was no delivery). A wider window returns the campaign shells with zeros.
  Confirm "no delivery" by listing campaigns and/or pulling a wider window — don't assume the
  pipeline is broken when you get `[]`.

## Business context
- Primary product: ASIN **B0FXW3GW5F** — cat deterrent spray / pet odor eliminator
  (SKU root `6K-PZMX-MTDZ`). 54 SP campaigns total (15 enabled, 32 paused, 7 archived).

## Standing issue — ads not delivering
- As of 2026-10-24, the **US profile has `validPaymentMethod: false`**. This is almost
  certainly why there are zero impressions/clicks/spend/sales. Keep flagging this at the top
  of every report until it's fixed; once a valid payment method is added, ads should start
  serving and real numbers will appear.

## Report mechanics
- 2-day window = the 2 full days ending 48h before run time (data lags ~48h).
- Save `reports/ppc-2day-latest.md` (overwrite) + `reports/ppc-2day-[YYYY-MM-DD].md` (dated,
  use the window END date). Commit. Upload to Google Drive folder "PPC Reports". Email to
  uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
- Compare against the previous 2-day report (previous dated file in `reports/`).

## Email delivery — BLOCKED in this environment
- The **Gmail connector is connected at the org level but NOT enabled in this chat
  session** (`enabledInChat: false`), so no `gmail`/send-email tool is callable here.
  The automated email step (subject `PPC 2-Day Report — [dates]`) could **not** be sent.
- Workaround used: the headline findings were delivered via the routine PushNotification
  (which also emails the run owner), and the full report is in the repo + Google Drive.
- To fix for future runs: enable the Gmail connector's tools for this chat/automation in
  claude.ai connector settings, or add an SMTP/email mechanism. Until then, treat the
  PushNotification + Drive upload as the delivery path and note the email was skipped.
