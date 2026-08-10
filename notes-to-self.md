# Notes to Self — PPC Analyst automated runs

Running log of lessons so future runs work better. Newest lessons at the top.

## Environment / setup facts (confirmed 2026-08-10)
- **Auth works.** LWA token refresh at `https://api.amazon.com/auth/o2/token` with
  AMZ_CLIENT_ID / AMZ_CLIENT_SECRET / AMZ_REFRESH_TOKEN succeeds. Access token lasts 3600s.
- **Region:** account lives in **North America** — use `https://advertising-api.amazon.com`.
  EU and FE hosts are blocked by the proxy (CONNECT 403), so don't waste tries on them.
- **Profiles under this account (seller "Uzoebo Archbold E-Commerce", id A1C2I8MOP52E35):**
  - US: `26765323558215` (USD, $40 daily budget) — the ACTIVE advertising profile. Default to this.
  - CA: `2840235221595557` (CAD)
  - MX: `3892485344323414` (MXN)

## KNOWN ISSUES to keep handling
- **AMZ_PROFILE_ID is WRONG in the environment.** It is set to
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5` — that's an *application* ID, not a numeric
  Ads *profile* ID. The Ads API needs the numeric profile ID in the `Amazon-Advertising-API-Scope`
  header. **Workaround:** ignore AMZ_PROFILE_ID and use the US profile `26765323558215`. If the env var
  ever gets fixed to a numeric value, prefer it. Flag this in the report until it's fixed by the owner.
- **Email delivery is blocked in the automated session.** The Gmail connector is authenticated at the
  org level but `enabledInChat: false` for this scheduled chat, so no Gmail tools load and the report
  can't be emailed automatically. Google Drive IS enabled and works. Until the owner enables Gmail for
  this chat, deliver via Drive + repo and note the email gap at the top of the report. Don't burn time
  searching for an SMTP alternative — there isn't one in this environment.

## Date window logic (data lags 48h)
- Rule that matches the spec's example: most-recent covered day D = the latest day whose midnight-end is
  <= (now - 48h). For the 2-day report, cover D and the day before D.
- Worked example: run Mon 2026-08-10 23:04 UTC -> now-48h = Sat Aug 8 23:04 -> most recent full day
  = Fri Aug 7 -> window = **Thu Aug 6 + Fri Aug 7**.

## Reporting API notes (v3 async reports)
- POST `/reporting/reports` with Content-Type/Accept
  `application/vnd.createasyncreportrequest.v3+json`. Body: name, startDate, endDate (YYYY-MM-DD),
  configuration{adProduct:SPONSORED_PRODUCTS, groupBy, columns, reportTypeId, timeUnit:SUMMARY, format:GZIP_JSON}.
- Report types used: `spCampaigns` (groupBy ["campaign"]), `spTargeting` (["targeting"]),
  `spSearchTerm` (["searchTerm"]). Poll GET `/reporting/reports/{id}` until status COMPLETED, then
  download the presigned `url` (gzip JSON). Reports finished in <1 min at this volume.
- Working columns: campaignId, campaignName, impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare (campaign level), keyword/keywordType/matchType/targeting (targeting),
  searchTerm/keyword/matchType (search term). CTR/CPC/ACOS/ROAS are derived in build.py, not requested.
- `topOfSearchImpressionShare` can be null (no eligible impressions) — render as "—".

## Report-building gotchas
- **Escape `|` in campaign names** before putting them in a Markdown table, or columns break.
- Attribution used: 7-day (purchases7d/sales7d).

## Comparison bookkeeping
- Previous 2-day report is `reports/ppc-2day-latest.md` (before it's overwritten) or the dated copy.
  First 2-day report was 2026-08-10 (window Aug 6-7). Baseline: imp 127, clk 2, CTR 1.6%, pur 1,
  sales $13.99, cost $2.72, CPC $1.36, ACOS 19.4%, ROAS 5.14.
