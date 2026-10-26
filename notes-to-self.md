# Notes to self — PPC Analyst (automated runs)

Living memory. Read this first every run. Add a dated lesson whenever something
breaks or surprises you.

## Environment / API facts (confirmed 2026-10-26)
- Credentials are in env vars: `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`,
  `AMZ_REFRESH_TOKEN`, `AMZ_PROFILE_ID`.
- **`AMZ_PROFILE_ID` is MISCONFIGURED.** It contains an *application* ID
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), **not** a numeric
  advertising profile ID. Do NOT pass it as the API scope — it will fail.
- The real advertising profiles (from `GET /v2/profiles`, NA region) are:
  - US: `26765323558215` (USD, seller) ← **use this one**. Has 54 SP
    campaigns (15 enabled). This is the active account.
  - CA: `2840235221595557` (CAD, seller) — 0 SP campaigns.
  - MX: `3892485344323414` (MXN, seller) — 0 SP campaigns.
  Account name on all three: "Uzoebo Archbold E-Commerce".
- **Region = NA**, host `https://advertising-api.amazon.com`. The EU/FE hosts
  (`advertising-api-eu`/`-fe.amazon.com`) are BLOCKED by the egress proxy
  (403 connect_rejected) — don't bother trying them.
- Token exchange works: `POST https://api.amazon.com/auth/o2/token` with
  grant_type=refresh_token. Access token lasts ~1h.
- No `requests` library installed. Use stdlib `urllib` with the proxy
  (`HTTPS_PROXY` env) and CA bundle `/root/.ccr/ca-bundle.crt`. Run scripts
  with `python3 -I`.

## Amazon Ads reporting API (v3) facts
- Campaigns list: `POST /sp/campaigns/list` with header
  `Content-Type: application/vnd.spCampaign.v3+json` (v2 `/v2/sp/campaigns`
  returns 404 — deprecated).
- Reports: `POST /reporting/reports` (header
  `application/vnd.createasyncreportrequest.v3+json`), then poll
  `GET /reporting/reports/{id}` until status COMPLETED, then download the
  gzip-JSON `url`.
- **spCampaigns report does NOT allow `acosClicks7d`/`roasClicks7d`** — only
  the 14d variants exist there. Simplest: pull `cost`, `sales7d`,
  `purchases7d` and compute ACOS (= cost/sales) and ROAS (= sales/cost)
  yourself. `clickThroughRate` and `costPerClick` ARE allowed; so is
  `topOfSearchImpressionShare`.
- Report types used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting — keyword/target rows), `spSearchTerm`
  (groupBy searchTerm — customer search terms).
- Reports return ONLY rows with activity; a quiet window legitimately yields
  0 rows. Always sanity-check against a wider/older window before concluding
  "no data" vs "window not ready".

## Date-window logic (data lags ~48h)
- A calendar day D is fully finalized only once now ≥ (D + 3 days at 00:00
  UTC), i.e. 48h after the day ends. For the 2-day report, cover the 2 most
  recent fully-finalized days.
- 2026-10-26 23:10 UTC run → covered **Oct 22 + Oct 23** (Oct 24 not yet 48h
  final because the run was at 23:10, not 00:00).

## Account state (the recurring story)
- **US ad account has NO valid payment method** (`validPaymentMethod: false`
  on the US profile). This means the 15 enabled SP campaigns do NOT serve:
  0 impressions / clicks / spend / sales. This has been true since at least
  late Sep 2026 and remains unresolved. Until it is fixed there is nothing
  to optimise — every report will be zeros. Lead the report with this.
- Always confirm "dark vs quiet" by pulling a wider window (e.g. month-to-
  date) alongside the 2-day window. Oct 1–23 MTD was fully zero.

## Previous reports live in Google Drive, NOT the repo
- The repo `reports/` folder started empty on this branch, but the Drive
  folder 'PPC Reports' (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`) holds the
  history as Google Docs. To find the previous report of a type, search that
  folder, not just the repo. Most recent 2-day before this run:
  "PPC 2-Day Report — 27-28 Sep 2026" (file id
  `13IW3SkPs-nzGN-ns4IvmICRLiuscxlqccIay_PWf0E8`).

## Report history
- 2026-10-26: 2-day report for window Oct 22–23. Account still dark (no
  payment method). All zeros. Compared against 27–28 Sep report (also zeros).
  October MTD fully silent (0 impressions) — slightly worse than Sep which
  had a 287-impression trickle. Saved ppc-2day-latest.md +
  ppc-2day-2026-10-26.md; uploaded to Drive 'PPC Reports'; emailed owner.
