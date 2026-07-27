# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest first.

## 2026-07-27 (first run, 2-day report)
- **Repo started empty.** Created `reports/` folder and this notes file on first run.
- **AMZ_PROFILE_ID env var is WRONG.** It holds `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`,
  which is an *application/client-id* format, NOT a numeric Amazon Ads profile ID. It cannot be used
  as the `Amazon-Advertising-API-Scope` header. Do not trust it as-is.
  - Fix used: called `GET /v2/profiles` on the NA host and picked the **US seller profile
    `26765323558215`** (USD, has a real daily budget of $40). The other profiles (CA `2840235221595557`,
    MX `3892485344323414`) have default/unset budgets (9.99e8) and appear inactive.
  - Future runs: keep using profile `26765323558215` unless told otherwise. If the env var ever gets
    fixed to a numeric ID, prefer it.
- **API region:** North America only. `advertising-api.amazon.com` works. EU/FE hosts are blocked by the
  proxy (403 CONNECT tunnel) and aren't needed for this US account.
- **Auth:** refresh-token → access-token exchange at `https://api.amazon.com/auth/o2/token` works fine.
- **Reporting API v3:** async flow (POST /reporting/reports → poll GET /reporting/reports/{id} → download
  gzipped JSON from the returned url). reportTypeIds used: `spCampaigns` (groupBy campaign),
  `spSearchTerm` (groupBy searchTerm). timeUnit SUMMARY, format GZIP_JSON.
- **Rate scaling gotcha:** the API returns `clickThroughRate` as a PERCENTAGE-magnitude number
  (e.g. it returned 0.5434 = 100·clicks/impressions for 1 click / 184 impr = 0.54%). So
  `topOfSearchImpressionShare` is likewise a percentage number (0.11 = 0.11%). To avoid ambiguity,
  compute CTR/CPC/ACOS/ROAS yourself from raw impressions/clicks/cost/sales.
- **Data quality:** account is very low-activity right now — over 2 days only $3.51 spend, 1 click, 0
  sales, despite a $40/day budget. Deliverability/bid issue worth flagging in reports.
- **Previous report location:** compare 2-day reports against `reports/ppc-2day-latest.md` (overwritten
  each run) — but this was the FIRST run, so no comparison was possible.

- **EMAIL BLOCKED.** The Gmail connector is installed for the account but **`enabledInChat: false`** —
  its tools are NOT loaded in this automated session, so the report could NOT be emailed to
  uzoebo.archbold@gmail.com this run. No SMTP/mail tool is available either. This needs the user to
  **enable the Gmail connector for automated/scheduled sessions** (in claude.ai connector settings).
  Until then, delivery is: repo commit + Google Drive upload only. Flag this in the run's notification.

## TODO for future runs
- Google Drive upload: ensure a folder named 'PPC Reports' exists; create if missing. (Confirmed folder
  id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo` exists as of first run.)
- Re-check each run whether Gmail is enabled in-chat; if so, send the email. If not, note it wasn't sent.
- If spend stays near-zero, consider noting it prominently — it may mean campaigns are paused,
  out of budget delivery, or bids too low.
