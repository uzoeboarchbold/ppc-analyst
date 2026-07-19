# Notes to Self — PPC Analyst

Running log of lessons so each run gets smoother. Newest notes at the top.

## Account / environment facts (stable)
- **Business:** Uzoebo Archbold E-Commerce (Amazon FBA), seller id A1C2I8MOP52E35.
- **Region:** North America endpoint `https://advertising-api.amazon.com` (NA). EU/FE endpoints are BLOCKED by the network proxy (403) — do not rely on them.
- **Profiles under this login (all NA):**
  - **US `26765323558215`** (USD) — THE primary advertising profile. Use this one.
  - CA `2840235221595557` (CAD) — placeholder daily budget, no/negligible activity.
  - MX `3892485344323414` (MXN) — no Sponsored Products campaigns at all.
- **Catalogue** centres on ASIN B0FXW3GW5F (cat-deterrent / pet-odour product).

## Gotchas & fixes (apply these)
1. **`AMZ_PROFILE_ID` is MISCONFIGURED.** It holds an *application* id
   (`amzn1.application.…`), not a numeric ad-profile id. Do NOT pass it as the
   `Amazon-Advertising-API-Scope`. Instead hard-select the US profile
   `26765323558215`. (Flag it in the report so the owner can fix the setting.)
2. **No email tool is connected.** Gmail connector exists but is `enabledInChat:false`,
   so no `mcp__*gmail*` tools load. The Step-4 email cannot be sent. Deliver the
   headline via PushNotification instead, and note in the report that email is
   unavailable until a Gmail/email integration is enabled for this automation.
3. **Google Drive works.** Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
   Upload the report there with `mcp__Google-Drive__create_file` (textContent,
   contentMimeType text/markdown). Prior reports live here — use the newest
   `ppc-2day-*.md` as the comparison baseline (the git repo starts empty each run).
4. **API auth:** POST refresh-token grant to `https://api.amazon.com/auth/o2/token`
   with client_id/secret/refresh_token → bearer access_token (1h). Token refresh works fine.
5. **Reports API (v3):** POST `/reporting/reports` with
   `Content-Type: application/vnd.createasyncreportrequest.v3+json`, reportTypeId
   `spCampaigns` (groupBy [campaign]), `spTargeting` (groupBy [targeting]),
   `spSearchTerm` (groupBy [searchTerm]). Async: poll GET `/reporting/reports/{id}`
   until COMPLETED (~1–3 min each), then GET the gzip url and gunzip JSON.
   Use 14d attribution columns: purchases14d, sales14d, acosClicks14d, roasClicks14d,
   plus topOfSearchImpressionShare (campaign level only).

## Standing situation (watch for it to change)
- The account has been **DARK since ~9 June 2026**: the only two ENABLED campaigns
  ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales") serve 0 impressions every day.
  Everything else is Paused/Archived. So every report so far reads all-zeros —
  a *status* problem, not a performance problem. Confirmed 30-day pull to Jul 16
  = 0 impressions. When impressions finally appear, switch back to normal
  best/worst/wasted-spend analysis.
- Because it's an unbroken run of zeros, comparisons keep showing "no change".
  Once it's non-zero, that's newsworthy — notify.

## Date window (2-day report)
- Data lags 48h. Cover the 2 full days ending 48h before the run.
- Run Sunday 2026-07-19 → covered Wed 2026-07-15 + Thu 2026-07-16.
- Pattern: covered days = run_date-4 and run_date-3.
