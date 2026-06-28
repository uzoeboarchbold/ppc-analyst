# Notes to Self — PPC Analyst

Lessons learned across runs. Read this first, every run, and apply it. Add to it whenever something trips you up.

## Credentials & account setup
- OAuth token refresh works against `https://api.amazon.com/auth/o2/token` with `AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`. Tokens last 3600s.
- **`AMZ_PROFILE_ID` is WRONG / misleading.** It contains an application ID (`amzn1.application....`), NOT a numeric Ads profile ID. Do not pass it as the API scope — it will fail.
- The correct profiles come from `GET /v2/profiles` on `advertising-api.amazon.com` (North America endpoint). There are three: CA (2840235221595557), MX (3892485344323414), US (26765323558215).
- **Use the US profile `26765323558215`** (USD). It is the only one with a real daily budget ($40); CA and MX have placeholder budgets (9.99E8) and look inactive. If this ever changes, re-check `/v2/profiles`.
- Only the NA endpoint (`advertising-api.amazon.com`) is reachable; the EU and FE endpoints return 403 (CONNECT tunnel failed) through the proxy. That's expected — NA is the right one for this account anyway.

## Reporting API
- Use the v3 reporting flow: `POST /reporting/reports` → poll `GET /reporting/reports/{id}` until status `COMPLETED` → download the `url` (GZIP_JSON, gzip-decompress it).
- Campaign report: `reportTypeId=spCampaigns`, `groupBy=["campaign"]`, `timeUnit=SUMMARY`. `topOfSearchImpressionShare` is available here.
- Search-term report: `reportTypeId=spSearchTerm`, `groupBy=["searchTerm"]`. Returns 0 rows when there were no clicks/impressions — that's normal, not an error.
- Metric column names are suffixed: `purchases30d`, `sales30d`, `acosClicks14d`, `roasClicks14d`, `clickThroughRate`, `costPerClick`. ACOS/ROAS/CTR/CPC come back `null` when there's no spend — present them as "—" in the report, don't invent numbers.

## Date window (2-day report)
- Data lags ~48h. End the window 48h before the run, then take the 2 full days ending there.
- Worked example: run 2026-06-28 → window = 2026-06-24 to 2026-06-25.

## Account state history (so future runs have context)
- **1–9 June 2026:** account ran an active SP structure (Odor Root / Isolated / Cat Deterrent / Pet Odor Eliminator / Cat Tunnel Bed campaigns) with real spend and occasional sales.
- **~9 June 2026 onward:** that structure went dark. Two new campaigns ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales") replaced it but have delivered ~0 impressions since (78 on 9 June, zero after). As of the 24–25 June report the account is effectively NOT delivering ads. If this is still true in later runs, keep flagging it — it's the #1 issue for the owner to fix.

## Delivery channels
- **No email/Gmail MCP tool is available** in this environment. The task asks to email the report, but there is no SMTP/Gmail tool. Workaround used: save to repo + upload to Google Drive ("PPC Reports" folder) + send a PushNotification (which reaches the owner's phone and inbox) with the summary. If an email tool appears in future, use it for the real email.
- Google Drive: use `mcp__Google-Drive__search_files` to find the "PPC Reports" folder (create it if missing via `create_file` with folder mime type), then `create_file` with `parentId` set and `text_content` + `content_mime_type: text/markdown` (set `disable_conversion_to_google_type: true` to keep it as markdown rather than converting to a Google Doc).
- Git: develop/commit/push on branch `claude/great-hopper-tccm5a`.
