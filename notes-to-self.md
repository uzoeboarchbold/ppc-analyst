# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest notes at the top.

## 2026-10-01 (first run — 2-day report)

**Credentials / environment**
- `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN` are VALID. LWA token
  refresh at `https://api.amazon.com/auth/o2/token` returns 200.
- ⚠️ `AMZ_PROFILE_ID` is MISCONFIGURED. It holds an **application ID**
  (`amzn1.application.…`), not a numeric advertising **profile ID**. Passing it
  as the `Amazon-Advertising-API-Scope` header gives `400 Invalid scope`.
  **Workaround that works:** call `GET /v2/profiles` with NO scope header to
  discover the real profile IDs, then use those. (If the env var ever gets
  fixed to a numeric ID, prefer it.)
- Real profiles on this account (seller "Uzoebo Archbold E-Commerce",
  account A1C2I8MOP52E35):
  - US (USD): `26765323558215`  ← only profile with campaigns
  - CA (CAD): `2840235221595557`  (0 campaigns)
  - MX (MXN): `3892485344323414`  (0 campaigns)

**Networking**
- Only the NA endpoint `https://advertising-api.amazon.com` is reachable
  through the proxy. `-eu` and `-fe` hosts are blocked (ProxyError). Fine —
  all three profiles live on NA.

**Reporting API (v3)**
- Use v3 async reporting: `POST /reporting/reports` with content-type
  `application/vnd.createasyncreportrequest.v3+json`, then poll
  `GET /reporting/reports/{id}` until status `COMPLETED`, then download the
  gzipped JSON from the returned `url`.
- `spCampaigns` report does NOT allow `acosClicks7d` / `roasClicks7d` columns
  (only the 14d variants exist). **Compute ACOS and ROAS yourself** from
  `cost` and `sales7d`: ACOS = cost / sales7d; ROAS = sales7d / cost.
- Valid useful columns: campaignName, campaignId, campaignStatus, impressions,
  clicks, cost, costPerClick, clickThroughRate, purchases7d, sales7d,
  topOfSearchImpressionShare.
- `timeUnit: SUMMARY` is what we want for a single aggregate per campaign over
  the window. `topOfSearchImpressionShare` is available with SUMMARY.

**Account health (important for future reports)**
- The US profile shows `validPaymentMethod: false`. The 15 ENABLED campaigns
  are therefore barely delivering: only **287 impressions, 1 click, $0.08
  spend, $0 sales across ALL of Sep 1–28**. Effectively the whole ad program
  is dark. Until a valid payment method is added, expect near-zero data every
  run. Flag this at the top of every report until it changes.
- For the 2-day window (Sep 27–28) specifically: zero impressions / clicks /
  spend / sales on every profile. The empty report is correct, not a bug.

**Delivery channels**
- Google Drive upload WORKS. Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload the markdown via `create_file` (contentMimeType `text/markdown`) into it.
- ⚠️ EMAIL could NOT be sent. The Gmail connector is connected at org level but
  `enabledInChat: false` for this automated session, so no Gmail tools load and
  there is no other SMTP/email path. I cannot fix this from here — the user must
  enable the Gmail connector for this chat/session in claude.ai connector
  settings. Until then, the push notification (which emails the user) is the
  substitute email delivery, and the report is available in the repo + Drive.
  Try the email step again on the next run in case the connector gets enabled.

**Process**
- Previous-report comparison: none existed on this first run. Going forward the
  previous 2-day report lives at `reports/ppc-2day-latest.md` (dated copies are
  `reports/ppc-2day-YYYY-MM-DD.md`). Read it before writing the comparison.
- Keep the working scripts logic: discover profiles → create report → poll →
  download → compute ACOS/ROAS.
