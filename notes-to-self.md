# Notes to Self — PPC Analyst

Running log of lessons so each run is smoother than the last. Newest notes at top.

## Key facts about this account
- **Account:** "Uzoebo Archbold E-Commerce" (Amazon seller id `A1C2I8MOP52E35`).
- The Amazon Ads token grants **3 profiles**, all the same seller, different marketplaces:
  - US (USD) — profileId `26765323558215` — **this is the active one** (has a real $40/day budget). `validPaymentMethod: false` as of 2026-11-13.
  - CA (CAD) — profileId `2840235221595557` — placeholder budget (999999999), no real activity.
  - MX (MXN) — profileId `3892485344323414` — placeholder budget, no real activity.
- **Use the US profile `26765323558215`** for reports unless told otherwise. It holds the 15 Sponsored Products campaigns (ASIN B0FXW3GW5F "Cat Deterrent Spray / Pet Odor Eliminator", plus a Cat Tunnel Bed campaign).

## IMPORTANT config problems to flag until fixed
- **`AMZ_PROFILE_ID` env var is INVALID.** It is a 50-char non-numeric string that matches none of the 3 real profiles. Real Amazon profile IDs are ~14–16 digit numbers. Until the user fixes this env var, do NOT trust it — instead call `GET /v2/profiles` and pick the US seller profile (`26765323558215`). Flag this at the top of every report.
- **Email step cannot run automatically.** The Gmail connector is installed/connected at the org level but `enabledInChat: false`, so no Gmail send/draft tool is available in the automated session. The report is still delivered to the repo and to Google Drive. To enable auto-email, the user must enable the Gmail connector (and its tools) for this chat/automation in their claude.ai connector settings. Flag this until resolved.

## How to pull the data (works)
- Token: `POST https://api.amazon.com/auth/o2/token` with grant_type=refresh_token + AMZ_CLIENT_ID/SECRET/REFRESH_TOKEN. Works.
- Region endpoint: **NA = `https://advertising-api.amazon.com`**. The EU and FE ad API hosts are BLOCKED by the egress proxy (403/connect_rejected) — do not bother trying them; the account is NA anyway.
- v2 endpoints like `/v2/sp/campaigns` return 404 (deprecated). Use the **v3 reporting API**: `POST /reporting/reports` (content-type `application/vnd.createasyncreportrequest.v3+json`), poll `GET /reporting/reports/{id}` every 10s (reports finish in ~60–90s), download the gzipped JSON from the `url`.
- Report types used: `spCampaigns` (groupBy `campaign`, has `topOfSearchImpressionShare`), `spTargeting` (groupBy `targeting`), `spSearchTerm` (groupBy `searchTerm`). timeUnit `SUMMARY` for the window, `DAILY` (add `date` column) for trend diagnostics.
- Reports take >120s end-to-end for 3 of them — run the pull as a **background** bash job and poll the output/JSON files.
- Never echo credentials/secrets to the shell — the auto classifier blocks "Credential Materialization". Read env vars inside python only; print only non-sensitive diagnostics. Run scripts that read creds with `python3 -I`.

## Lessons / history
- **2026-11-13 (first run, 2-day report for Nov 9–10):** Account is completely DARK. Zero impressions/clicks/spend/sales across all 15 campaigns — and a 21-day diagnostic (Oct 20–Nov 10) showed zero delivery every single day. Root cause almost certainly `validPaymentMethod: false` on the US profile (billing/payment method invalid → Amazon stops serving ads), and/or campaigns not enabled. This is the headline for the user: **their ads are not running and haven't been for weeks.** No previous report existed to compare against (this was the first run).
- Date window logic (2-day report): data lags 48h. window = the 2 full days ending ~48h before run. Run Fri 2026-11-13 23:10 UTC → anchor Wed 11-11 → last fully-finalized day = Nov 10 → window = **Nov 9–10**. Keep this logic.
