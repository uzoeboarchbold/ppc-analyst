# Notes to Self — PPC Analyst

Running log of lessons so each automated run gets smoother. Newest lessons on top.

## Key facts about this account
- **Account:** Uzoebo Archbold E-Commerce (seller). Amazon Ads API works via refresh-token OAuth.
- **Correct US profile ID:** `26765323558215` (USD, US marketplace, daily budget $40). This is the active account to report on.
- Other profiles exist but are dormant defaults: CA `2840235221595557` (CAD), MX `3892485344323414` (MXN). Ignore unless asked.
- Products/campaigns seen: Pet Odor Eliminator (ASIN B0FXW3GW5F) and Cat Tunnel Bed. 6 SP campaigns total as of Aug 2026.

## Lessons learned (apply these)
1. **`AMZ_PROFILE_ID` env var is WRONG.** It contains an application ID (`amzn1.application....`), not a numeric advertising profile ID. Do NOT use it as the API scope. Instead call `GET https://advertising-api.amazon.com/v2/profiles` and pick the US/USD seller profile (currently `26765323558215`). If profiles change, re-derive from that endpoint.
2. **Auth flow that works:** POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token + AMZ_CLIENT_ID + AMZ_CLIENT_SECRET + AMZ_REFRESH_TOKEN → `access_token` (1h). Then Reporting API v3.
3. **Reporting API v3 works** (v2 is deprecated). Endpoint `POST /reporting/reports` with Content-Type `application/vnd.createasyncreportrequest.v3+json`, header `Amazon-Advertising-API-Scope: <profileId>`. Poll `GET /reporting/reports/{id}` until COMPLETED (usually <1 min), then download the gzipped-JSON `url`.
   - Campaign report: reportTypeId `spCampaigns`, groupBy `["campaign"]`. `topOfSearchImpressionShare` IS available here.
   - Target/keyword report: reportTypeId `spTargeting`, groupBy `["targeting"]`.
   - Search-term report: reportTypeId `spSearchTerm`, groupBy `["searchTerm"]`.
   - Useful columns: impressions, clicks, clickThroughRate, cost, costPerClick, purchases30d, sales30d, acosClicks14d, roasClicks14d.
4. **Email is NOT wired up.** Gmail connector is installed but `enabledInChat: false` in the automated session, so its tools don't load and the report can't be emailed automatically. Until someone enables the Gmail connector for this chat, note the gap at the top of the report and rely on repo + Google Drive delivery. Do not fail the run over this.
5. **Google Drive works** (connected + enabled). Upload the report to the "PPC Reports" folder. If the folder doesn't exist, create it or upload to root and note it.
6. **Repo home is `/home/user/ppc-analyst`, but `$HOME` is `/root`.** Always use the absolute repo path; `cd $HOME/ppc-analyst` fails.
7. **Date window (2-day report):** end 48h before run, floored to midnight, cover the 2 full days before that. E.g. run Mon 17 Aug → cover Thu 13 + Fri 14 Aug.
8. **Account is currently very low-activity.** As of 13–14 Aug 2026: 72 impressions, 0 clicks, $0 spend, $0 sales. Real data, not an error — report it honestly. If future runs also show $0, flag it as a possible paused/underfunded-campaign issue, not a data failure.

## Previous reports of each type (for comparison)
- 2-day: first one is `reports/ppc-2day-2026-08-17.md` (baseline, no prior to compare).
