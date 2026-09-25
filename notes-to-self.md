# Notes to self — PPC Analyst (Amazon Ads)

Running log of lessons so future runs work first time. Newest at top.

## 2026-09-25 (2-day report)

**EMAIL STILL BLOCKED (same as 09-24).** Gmail connector is `connected` at org
level but `enabledInChat: false`, so no send tool is loaded — report could NOT
be emailed. Only the user can enable Gmail for this chat. Drive upload works.

**Reports are scattered one-per-branch.** Every run lands on its own
`claude/great-hopper-*` branch, so the previous report is NOT on `main` — find
it by listing all `great-hopper` branches, sorting by commit date, and reading
`reports/` + `notes-to-self.md` from the newest one. The newest before this run
was branch `jv9v2o` (2026-09-24). I seed this branch's notes from there.

**Data lag stuck at ~7 days.** As of this run (2026-09-25), the latest finalised
date is STILL 2026-09-18 — no new data since yesterday's run. A DAILY report
requested for 09-10→09-24 returned rows only through 09-18. Requested 2-day
window (21–22 Sep) was empty. If this persists, widen the buffer to ~7 days.

**DAILY vs SUMMARY behaviour confirmed:** SUMMARY omits all-zero rows (empty
result = no activity). DAILY *does* return zero rows, so it's the reliable way
to prove "data exists but is zero" vs "date not finalised yet" (absent dates =
not finalised). Only 15 campaigns came back in the daily pull this run.

**Account still DARK:** zero impressions/clicks/spend/sales every available day.
Unchanged from 2026-09-24. Headline stays "ads not serving — raise bids / check
campaign eligibility," not a performance comparison.

**Pull script that works** is saved in scratchpad (`pull.py`): token exchange +
reporting v3, profile `26765323558215`, computes ACOS/ROAS locally.

## 2026-09-24 (first run — 2-day report)

**EMAIL STEP BLOCKED.** The Gmail connector is connected at the org level but is
**toggled OFF for this chat/session** (`enabledInChat: false`), so no Gmail send
tool is available and the report could NOT be emailed to uzoebo.archbold@gmail.com.
This is a per-chat setting only the user can change (enable Gmail in this chat's
connector settings). Report was still saved to the repo and uploaded to the
Google Drive "PPC Reports" folder. Future runs: if email is still needed, the
Gmail connector must be enabled for the session, or switch to an SMTP/other send
method.


**Credentials / connection**
- `AMZ_PROFILE_ID` env var is WRONG: it holds an *application id*
  (`amzn1.application....`), not a numeric advertising profile id. Do not use it
  as the `Amazon-Advertising-API-Scope` header — it returns 400.
- The account has 3 profiles (from `GET /v2/profiles`): CA `2840235221595557`,
  MX `3892485344323414`, US `26765323558215`. Only **US `26765323558215`** is a
  real active ad profile ($40 daily budget); CA/MX have placeholder ~1e9 budgets.
  **Use profile id `26765323558215`** until the env var is fixed.
- `GET /v2/profiles` must be called WITHOUT the scope header (scope header -> 400).
- Region endpoint: use **NA** `https://advertising-api.amazon.com`. The EU and FE
  hosts are BLOCKED by the network policy (proxy 403). Do not retry them.
- Token exchange at `https://api.amazon.com/auth/o2/token` works fine with the
  refresh token. Set `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt`.

**Reporting API v3 (`/reporting/reports`)**
- `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
- `acosClicks7d` / `roasClicks7d` are NOT valid columns for `spCampaigns`.
  Pull `cost`, `sales7d`, `purchases7d` and compute ACOS = cost/sales,
  ROAS = sales/cost yourself. `topOfSearchImpressionShare` IS valid.
- SUMMARY reports omit rows where all metrics are zero, so an empty result set
  = no activity in that window (not necessarily an error). Confirm with a DAILY
  report over a wider window before concluding.

**DATA LAG IS LONGER THAN 48h.** As of run on 2026-09-24, the latest date with
any populated data was **2026-09-18**. Dates 2026-09-19/20/21 returned NO rows at
all. The nominal "cover 2 full days ending 48h before now" window (Sep 20–21) had
no data yet. For future runs: still state the requested window, but ALSO pull the
most recent available data and, if the requested window is empty, report the
latest available finalized days and flag the lag. Consider extending the buffer
toward ~72–96h if this persists.

**Business state to watch:** The account has been effectively DARK since
2026-09-03 — zero impressions/clicks/spend/sales every day Sep 3–18. Last real
activity was Sep 1–2 (tiny: 287 impressions total, $0.08 spend, 0 sales).
54 SP campaigns are mostly ENABLED but at $1.50 budgets and apparently bidding
too low to win any placements. If a future run still shows zero delivery, the
headline finding is "ads not being served — raise bids / check campaign health",
not a performance comparison.
