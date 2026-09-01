# Notes to Self — PPC Analyst (automated runs)

Memory file for the hands-off Amazon PPC reporting routine. Read this at the
start of every run and apply the lessons. Append new lessons as you learn them.

## Account facts (confirmed 2026-09-01)
- **Business:** Uzoebo Archbold E-Commerce (Amazon FBA), seller ID A1C2I8MOP52E35.
- **Active marketplace:** US. Use Amazon Ads **profileId `26765323558215`** (USD,
  $40/day budget). This is the operating account.
- CA (`2840235221595557`) and MX (`3892485344323414`) profiles also exist under
  the same account but carry placeholder budgets (~$1B) and no real activity —
  ignore unless told otherwise.
- **Region/endpoint:** North America → `https://advertising-api.amazon.com`.
  EU and FE endpoints are BLOCKED by the network proxy (403 CONNECT tunnel) —
  don't waste retries on them.
- Products seen: B0FXW3GW5F (Cat Deterrent Spray / Pet Odor Eliminator) and a
  "Cat Tunnel Bed" product. Many campaigns are newly built and barely serving.

## Gotchas / lessons
1. **AMZ_PROFILE_ID env var is WRONG.** It's set to an *application* ID
   (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT a numeric profile
   ID. Do NOT pass it as the API scope. Instead, call `GET /v2/profiles` and use
   the US numeric profileId (`26765323558215`). Flag this in the report each run
   until the env var is fixed.
2. **Token exchange works:** POST `https://api.amazon.com/auth/o2/token` with
   grant_type=refresh_token + client_id + client_secret. Access token lasts 1h.
3. **Reporting = v3 async.** POST `/reporting/reports` with header
   `Content-Type: application/vnd.createasyncreportrequest.v3+json`, scope header =
   numeric profileId. Report types: `spCampaigns` (groupBy `campaign`) and
   `spSearchTerm` (groupBy `searchTerm`). Poll `/reporting/reports/{id}` until
   status COMPLETED, then download the gzipped-JSON `url`.
4. **Column names that work:** impressions, topOfSearchImpressionShare, clicks,
   clickThroughRate, cost, costPerClick, purchases30d, sales30d, campaignName,
   campaignId (campaign report); add keyword/keywordType/matchType/searchTerm for
   the search-term report. Compute ACOS = cost/sales, ROAS = sales/cost yourself
   (safer than relying on acosClicksNd fields).
5. **Escape `|` in campaign names** before putting them in a markdown table —
   several campaign names contain literal pipes (e.g. "SP | Cat Tunnel Bed …").
6. **topOfSearchImpressionShare is null** when a campaign served 0 impressions —
   render as "—", not 0%.

## Date window rule (2-day report)
Cover the 2 full days ending 48h before the run. A day counts only if its END is
≥48h before run time. Run 2026-09-01 23:05 UTC → window = 28–29 Aug 2026.

## Report history (for comparison chaining)
- 2026-09-01: FIRST 2-day report (baseline). Window 28–29 Aug. Totals:
  300 impressions, 2 clicks, $0.27 spend, 0 sales, 0 purchases. Account was near-
  dormant — impressions barely served; likely bids/budgets too low, not a perf
  problem. Next run: compare against these numbers.

## Delivery
- Save `reports/ppc-2day-latest.md` (overwrite) + dated `reports/ppc-2day-YYYY-MM-DD.md`; commit on branch `claude/great-hopper-6n32mz`. ✅ works.
- Upload same file to Google Drive folder "PPC Reports" (folder id
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). ✅ works via Google-Drive create_file
  with base64Content + disableConversionToGoogleType=true. NOTE: update_file only
  changes metadata, not content — to replace content, create a new file and trash
  the old one.
- Email to uzoebo.archbold@gmail.com, subject "PPC 2-Day Report — [dates]".
  ⚠️ BLOCKED (2026-09-01): the **Gmail connector is installed but NOT enabled in
  chat** (`enabledInChat:false`), so no email-send tool is available in the
  session — the report could not be auto-emailed. FIX: enable the Gmail connector
  for Claude Code sessions (claude.ai → connector settings for this chat). Until
  then, delivery falls back to the git commit + Drive upload + the run's push
  notification. Re-check `ListConnectors` each run; send the email once Gmail is
  enabled.
