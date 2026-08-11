# Notes to Self — PPC Analyst Routine

Running log of lessons so each run gets smoother. Newest notes at top.

## Environment / credentials
- **`AMZ_PROFILE_ID` is WRONG type.** The env var holds an *application ID*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric advertising
  profile scope. The Amazon-Advertising-API-Scope header needs the numeric `profileId`.
- **Correct profiles** (from `GET /v2/profiles` on the NA endpoint):
  - US (Amazon.com), USD, profileId `26765323558215` — **ACTIVE, $40/day budget → USE THIS ONE.**
  - CA, CAD, profileId `2840235221595557` — default/unset budget (9.99e8), inactive.
  - MX, MXN, profileId `3892485344323414` — default/unset budget, inactive.
  - Account: "Uzoebo Archbold E-Commerce", seller, id A1C2I8MOP52E35.
- Token refresh works against `https://api.amazon.com/auth/o2/token` with the 3 env creds.
  Access token lasts 3600s.

## Amazon Ads API (v3 reporting) gotchas
- Endpoint base: `https://advertising-api.amazon.com` (NA region works for this US account).
- Async reports: `POST /reporting/reports` then poll `GET /reporting/reports/{id}` until
  `status == COMPLETED`, then download the `url` (GZIP JSON).
- **`groupBy` MUST be a JSON array**, e.g. `["campaign"]` — a bare string returns
  `400 Invalid or malformed request body`.
- Content-Type header for create: `application/vnd.createasyncreportrequest.v3+json`.
- Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`.
  Targeting report: reportTypeId `spTargeting`, groupBy `["targeting"]`.
- Useful columns: impressions, clicks, cost, purchases7d, sales7d,
  topOfSearchImpressionShare, campaignName, campaignId, keyword, matchType, targeting.
- `timeUnit: "SUMMARY"` gives one aggregated row per entity (no `date` column allowed).
- ToS impression share comes back as a number that reads as a percent (e.g. 1.04 = 1.04%);
  it is per-campaign and does NOT sum into a totals row — leave totals ToS blank.
- Reports usually complete within ~30–45s (2–3 polls at 15s).

## Report conventions
- Date window (2-day): data lags ~48h. Window = the 2 most-recent fully-finalized days
  ending before the 48h cutoff. e.g. run Tue Aug 11 23:04 UTC → cutoff Sun Aug 9 23:04 →
  cover Fri Aug 7 + Sat Aug 8. (Same as example: run Sun 00:00 → cover Wed+Thu.)
- Campaign names contain literal `|` chars → **escape as `\|`** in markdown tables or cells break.
- Files: overwrite `reports/ppc-2day-latest.md` + dated copy `reports/ppc-2day-[run-date].md`.
- Previous report to compare against = the prior `ppc-2day-*.md` (the latest dated one that
  isn't today's). First run has none → state it's the baseline.

## Delivery
- Google Drive: upload to folder named "PPC Reports" (Google-Drive MCP). Folder id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Use `create_file` with `contentMimeType: text/markdown`
  and `disableConversionToGoogleType: true`. WORKS.
- **Email: BLOCKED as of 2026-08-11.** There is NO email/Gmail send tool available in the automated
  session. The Gmail connector exists but is `enabledInChat: false` (and only "drafts replies").
  ToolSearch for gmail/email/send returns nothing. Cannot self-enable a connector (needs user action
  in connector settings). => Report is saved to repo + Drive; email is NOT sent. Add a delivery note
  at the top of the report each run until Gmail is enabled in-session, and flag it via PushNotification.
  To fix permanently: user must enable the Gmail connector for this session/schedule.

## History
- 2026-08-11: First run. Very low activity Aug 7–8: 119 impressions, 1 click, 1 sale,
  $2.65 spend, $13.99 sales, ACOS 18.9%, ROAS 5.28. Only "pet odor eliminator" (phrase) converted.
