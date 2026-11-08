# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each run is smarter than the last. Append, don't delete.

## Account facts (verified)
- Credentials in env (`AMZ_CLIENT_ID`, `AMZ_CLIENT_SECRET`, `AMZ_REFRESH_TOKEN`) are **valid**. LWA token refresh at `https://api.amazon.com/auth/o2/token` works.
- **`AMZ_PROFILE_ID` env var is INVALID** (a 50-char non-numeric string). A scoped API call with it returns HTTP 400 "profile ID required". DO NOT trust it.
  - **Workaround that works:** call `GET /v2/profiles` (NA endpoint, no scope header) and pick the profile that actually has Sponsored Products campaigns.
  - The correct profile is **US seller `26765323558215`** (USD). CA `2840235221595557` and MX `3892485344323414` are empty.
  - If `AMZ_PROFILE_ID` ever becomes numeric, re-verify it; otherwise keep using `26765323558215`.
- **Region = NA** (`https://advertising-api.amazon.com`). EU/FE endpoints are blocked by the network proxy (403 tunnel) — expected, this is a US account, ignore.
- Business: single ASIN **B0FXW3GW5F** (pet odor eliminator / cat deterrent spray), 54 SP campaigns (varies), ~15 enabled.

## How to pull data (works)
- Async reporting v3: `POST /reporting/reports` with content-type `application/vnd.createasyncreportrequest.v3+json`, body has `configuration` with `adProduct=SPONSORED_PRODUCTS`, `timeUnit=SUMMARY` (or `DAILY`), `format=GZIP_JSON`.
- Report types used: `spCampaigns` (groupBy `campaign`), `spTargeting` (groupBy `targeting`), `spSearchTerm` (groupBy `searchTerm`).
- `topOfSearchImpressionShare` is valid on `spCampaigns` only.
- Poll `GET /reporting/reports/{id}` until `COMPLETED`, then download the presigned `url` (plain GET, NO auth headers), gunzip, parse JSON.
- Reports take ~30–90s to finish.
- Scripts from the 2026-11-08 run are reusable patterns (token refresh + call helpers).

## Data/health lessons
- **2026-11-08 run (window Nov 4–5):** ALL campaigns returned 0 impressions/clicks/spend/sales — and 0 for the whole Oct 20–Nov 5 span. Campaigns are ENABLED with $1.50–$2.50 daily budgets since May 2026, so the blocker is NOT the ad settings. When EVERY campaign (incl. Auto) is simultaneously at zero impressions, the cause is almost always the **listing** (out of stock / lost Buy Box / suppressed-ineligible ASIN). Report framed it that way.
- **Before reporting "zero spend," always sanity-check with a wider DAILY pull** (e.g. last 2–3 weeks) to prove it's a true zero and not a date-window or attribution artifact. Did this; confirmed real zero.
- Don't invent numbers. If genuinely zero, say so and explain the likely cause + next steps.

## Report mechanics
- Reports saved to `reports/`: overwrite `ppc-2day-latest.md` + dated `ppc-2day-[YYYY-MM-DD].md` (date = run date).
- Previous-report comparison (Part C): find the prior `ppc-2day-*.md` (not -latest) before overwriting. On 2026-11-08 there was none → first run, nothing to compare.
- Also: upload to Google Drive folder "PPC Reports" + email to uzoebo.archbold@gmail.com, subject `PPC 2-Day Report — [dates]`.
- Date window rule: data lags 48h; 2-day window = the 2 full days ending 48h before run. Run Sun 2026-11-08 23:10 UTC → window Nov 4–5.

## Delivery lessons
- **Google Drive upload WORKS.** "PPC Reports" folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`. Upload with `create_file` (contentMimeType `text/markdown`, `disableConversionToGoogleType=true`).
- **EMAIL step could NOT be done (2026-11-08 run).** The Gmail connector is installed & connected at the org level but `enabledInChat: false` in this automated session, so no `mcp__Gmail__*` send tool is available. I could not send the email to uzoebo.archbold@gmail.com.
  - **To fix:** enable the Gmail connector's tools for this chat/automation in claude.ai connector settings (grant it send/compose permission for the scheduled session). Until then, reports are delivered via the repo commit + Google Drive only, and findings via push notification.
  - Possible alternative if email stays unavailable: use Drive `share_file` to share the dated report with the user's email (sends a Drive notification email with a link) — not a true email of the body, but reaches the inbox.
