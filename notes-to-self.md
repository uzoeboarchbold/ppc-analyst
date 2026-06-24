# PPC Analyst — Notes to Self

Lessons learned by past runs. Read this first, every run.

## Credentials & API access
- Env vars present: AMZ_CLIENT_ID, AMZ_CLIENT_SECRET, AMZ_REFRESH_TOKEN, AMZ_PROFILE_ID.
- **IMPORTANT: `AMZ_PROFILE_ID` is NOT a usable advertising profile ID.** It holds an
  application-style id (`amzn1.application.…`). The real profile IDs are numeric.
  Do NOT pass it as `Amazon-Advertising-API-Scope`. Instead call `GET /v2/profiles`
  and pick the account you want.
- Profiles on this account (seller "Uzoebo Archbold E-Commerce", id A1C2I8MOP52E35):
    - US  -> profileId **26765323558215**, USD  <-- primary, use this one
    - CA  -> profileId 2840235221595557, CAD
    - MX  -> profileId 3892485344323414, MXN
- Region/host: **advertising-api.amazon.com** (North America). The EU and FE hosts
  are blocked by the proxy (403) and are not needed for this US account.
- Token: standard refresh-token grant at https://api.amazon.com/auth/o2/token works.

## Reporting API (v3, async)
- Create: POST https://advertising-api.amazon.com/reporting/reports
    Content-Type: application/vnd.createasyncreportrequest.v3+json
    Headers also need Authorization (Bearer), Amazon-Advertising-API-ClientId,
    Amazon-Advertising-API-Scope (= numeric profileId).
- Poll the same id until status == COMPLETED, then download the gzipped JSON `url`.
- **Column gotcha:** `acosClicks7d` / `roasClicks7d` are INVALID for `groupBy:["campaign"]`.
  Compute ACOS = cost / sales7d and ROAS = sales7d / cost yourself. Those two columns
  ARE valid for `groupBy:["targeting"]` and `["searchTerm"]`.
- Useful campaign columns: impressions, topOfSearchImpressionShare, clicks,
  clickThroughRate, cost, costPerClick, purchases7d, sales7d, campaignName,
  campaignStatus, campaignBudgetAmount.
- An empty report (0 rows) means no campaign served impressions in the window —
  it is NOT an error. Verify by pulling a wider DAILY window before concluding.

## Account status observations
- As of the 2026-06-24 run: account is essentially DARK. 52 of 54 campaigns PAUSED;
  only 2 ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day each) but they
  served nothing. Last day with any impressions was 2026-06-09; last real spend ~06-08.
  If future windows are still zero, the headline finding is "ads are turned off".

## Files / workflow
- Reports live in `reports/`. Overwrite `ppc-2day-latest.md` and also save
  `ppc-2day-[YYYY-MM-DD].md`. Compare each run against the previous 2-day report.
- Date window: data lags 48h. 2-day report covers the 2 full days ending 48h before run.
  (Run Wed 06-24 -> covers Sat 06-20 and Sun 06-21.)
- After saving: commit+push to branch claude/great-hopper-5stp20, upload to Google
  Drive folder "PPC Reports", email uzoebo.archbold@gmail.com.

## Email delivery (added 2026-06-24)
- **No email/Gmail tool is connected** to this automated environment — only the
  Google-Drive and github MCP servers are available. The "email the report" step
  therefore cannot be completed automatically. Drive upload + the run notification
  are the working delivery channels. If email is required, a Gmail/SMTP integration
  must be added to the routine; until then, note the gap at the top of the report
  rather than failing the run.
