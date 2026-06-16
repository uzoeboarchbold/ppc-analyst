# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## 2026-06-16 (first run — 2-day report)
- **Environment is set up correctly.** Creds in env vars work:
  AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN, AMZ_PROFILE_ID.
  Token refresh endpoint: `https://api.amazon.com/auth/o2/token` (grant_type=refresh_token).
  Access tokens expire in ~1h — refresh before each batch of calls.
- **WATCH OUT: `AMZ_PROFILE_ID` env var is NOT a usable profile ID.** It is set to
  `amzn1.application.dd42...` (an application/client identifier). Real Amazon Ads
  profile IDs are numeric. I had to look profiles up via `GET /v2/profiles`.
  Profiles on this account (seller "Uzoebo Archbold E-Commerce", entity A1C2I8MOP52E35):
    - **US: 26765323558215 (USD)  <-- the ACTIVE account, use this one**
    - CA: 2840235221595557 (CAD) — no SP campaigns
    - MX: 3892485344323414 (MXN) — no SP campaigns
  Future runs: use **26765323558215** unless told otherwise.
- **Network egress:** only `advertising-api.amazon.com` (NA) and `api.amazon.com`
  are allowlisted. EU/FE hosts are blocked. Fine — this account is North America.
- **Reporting API:** v3 async reports work well.
  `POST /reporting/reports` (Content-Type `application/vnd.createasyncreportrequest.v3+json`),
  poll `GET /reporting/reports/{id}` until status=COMPLETED, download the gzipped JSON `url`.
  - Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
    Useful columns: campaignName, campaignId, campaignStatus, impressions, clicks,
    cost, purchases7d, sales7d, topOfSearchImpressionShare.
  - Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
  - Reports typically finish in 1–3 min. timeUnit SUMMARY for totals, DAILY for trend.
- **Derived metrics** (API gives raw counts): CTR=clicks/impr, CPC=cost/clicks,
  ACOS=cost/sales, ROAS=sales/cost. Guard against divide-by-zero.
- **Data state on this run:** account is essentially DARK. The 2-day window
  (Jun 13–14) had ZERO impressions/clicks/spend/sales. Most campaigns PAUSED;
  only 2 enabled campaigns, both with no delivery. Last real spend was Jun 8
  ($46, no sales). This is genuine zero-data, NOT an API failure — confirmed by
  a 30-day pull showing ~$715 spend earlier in the period. If future runs also
  show zero, the campaigns are still paused — flag it, don't assume a bug.
- **No previous 2-day report existed** → nothing to compare against this run.
- TODO for future runs: compare against `reports/ppc-2day-latest.md` BEFORE
  overwriting it (read it into memory first, then write the new one).
- **EMAIL STEP CANNOT BE DONE AUTOMATICALLY (yet).** No email/Gmail/SMTP tool is
  available in this environment — only the Google-Drive and github MCP servers are
  connected. External SMTP hosts are not in the network allowlist either. So the
  "email the report to uzoebo.archbold@gmail.com" step is currently NOT possible.
  Workarounds delivered instead: report committed to the repo + uploaded to the
  Drive "PPC Reports" folder (the owner can open it there). To enable real email,
  the owner needs to add a Gmail/email MCP server (or an SMTP relay host to the
  egress allowlist + credentials). Flag this each run until fixed; don't pretend
  the email went out.
- Drive "PPC Reports" folder ID: 1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo.
