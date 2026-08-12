# Notes to Self — PPC Analyst (Amazon FBA)

Running log of lessons so each automated run goes smoother. Newest at top.

## 2026-08-12 (first run — 2-day report)
- **Endpoint / region:** The account lives on the **North America** Ads API host
  `https://advertising-api.amazon.com`. EU/FE hosts are blocked by the proxy (403) — don't waste retries there.
- **PROFILE_ID env var is BAD:** `AMZ_PROFILE_ID` is set to
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, which is **not** a numeric
  Ads profile ID. The API needs the numeric `profileId` in the
  `Amazon-Advertising-API-Scope` header. `GET /v2/profiles` returns three:
  - **US 26765323558215** (USD, $40 daily budget) ← the live ad account. USE THIS.
  - CA 2840235221595557 and MX 3892485344323414 (budgets effectively unset, not used for ads).
  I hardcoded the US numeric profile. **Action for owner:** fix the `AMZ_PROFILE_ID`
  env var to `26765323558215` so future runs don't have to guess.
- **Token refresh:** Standard OAuth refresh at `https://api.amazon.com/auth/o2/token`
  with grant_type=refresh_token works fine. Access token ~724 chars, valid ~1h.
- **Reporting API:** v3 async reporting works. `POST /reporting/reports` with
  `Content-Type: application/vnd.createasyncreportrequest.v3+json`, poll
  `GET /reporting/reports/{id}` until COMPLETED, download the gzip-JSON `url`.
  Report types: `spCampaigns` (groupBy campaign), `spSearchTerm` (groupBy searchTerm).
  `topOfSearchImpressionShare` is a valid column on spCampaigns (returns a % as a number, e.g. 1.04 = 1.04%).
- **Search-term report empty when 0 clicks:** spSearchTerm returned 0 rows because
  the window had 0 clicks/spend — Amazon only reports search terms that drove billable
  clicks. Not an error; expected when the account is dormant.
- **NO EMAIL TOOL:** Only Google-Drive and github MCP servers are connected. There is
  **no** email/Gmail tool, so the "email to uzoebo.archbold@gmail.com" step cannot be
  performed. Report is saved to the repo and uploaded to Google Drive 'PPC Reports'
  instead. **Action for owner:** connect a Gmail/email connector if emailed delivery matters.
- **Account state this window:** 8 enabled SP campaigns, 120 impressions, **0 clicks,
  $0 spend, 0 sales** over Aug 8–9. Ads are technically enabled but essentially not
  serving into clicks — likely bids too low to win the auction, or genuinely tiny volume.

## Standing reminders
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before the run.
  (Run 2026-08-12 → covered Aug 8 & Aug 9.)
- Previous 2-day report to compare against lives in `reports/ppc-2day-latest.md`
  (before you overwrite it, read it for the Part C comparison).
- Never invent numbers. If a pull fails, explain plainly at the top of the report.
