# Notes to Self — PPC Analyst (read before each run)

## Environment persistence
- **The repo is re-cloned fresh each run** (this branch had only the initial commit despite prior runs committing reports). Repo-side history does NOT reliably carry across runs. **Google Drive folder 'PPC Reports' is the durable memory/history** — always check it for the previous report of this type to compare against. (Folder ID: `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.)
- Still commit/push reports to the repo as instructed, but rely on Drive for continuity.

## Credentials & API
- Auth works. Access token from `https://api.amazon.com/auth/o2/token` (refresh_token grant). Access token TTL ~1h.
- **AMZ_PROFILE_ID env var is WRONG** — it holds an LWA *application* ID (`amzn1.application.…`), not a numeric profile. Do not pass it as the scope. Auto-detect via `/v2/profiles` on the NA host.
- Profiles: **US = 26765323558215 (USD, the only active one — use this)**; CA = 2840235221595557 (no campaigns); MX = 3892485344323414 (no campaigns).
- Region: only **NA** (`https://advertising-api.amazon.com`) is reachable through the proxy. EU/FE hosts are blocked (proxy tunnel fails) — not needed for this US account.

## Reporting API (v3) gotchas
- Create report: POST `/reporting/reports`, Content-Type `application/vnd.createasyncreportrequest.v3+json`, header `Amazon-Advertising-API-Scope: 26765323558215`.
- **spCampaigns report does NOT accept `acosClicks7d` / `roasClicks7d` columns** (400 error). Derive ACOS = cost/sales7d and ROAS = sales7d/cost yourself. (`roasClicks14d` is allowed but easier to just compute.) The spSearchTerm report DOES accept acosClicks7d/roasClicks7d.
- `topOfSearchImpressionShare` is valid on spCampaigns; comes back `null` when there were no impressions.
- Good campaign columns: campaignId, campaignName, impressions, clicks, cost, purchases7d, sales7d, clickThroughRate, costPerClick, topOfSearchImpressionShare.
- Reports usually COMPLETE within ~20–60s. Poll every 15–20s.

## Date window (2-day report)
- Data lags ~48h. Established cadence: **run date D → window = [D-3, D-2]** (i.e. last day = D-2). E.g. Jul 3 run → 30 Jun–1 Jul. Jul 2 run → 29–30 Jun. Do NOT be over-conservative and shift a day earlier — keep the rolling cadence so comparisons line up with the prior report.

## Account status (as of 3 Jul 2026)
- **Account has been DARK since ~9 June 2026.** Last ad delivery 9 Jun; last real spend 8 Jun (~$46). Every 2-day report since has been all-zero.
- 54 campaigns: ~45 paused, 2 enabled, 7 archived. The 2 enabled ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day each) win essentially no impressions — likely bids too low / targeting too narrow / ASIN eligibility.
- Main product: Cat Deterrent / Pet Odor Eliminator spray, ASIN B0FXW3GW5F. Historic spend campaigns are the now-paused "Odor Root / Litter+Urine Root / Home+Eliminator" set.
- **When delivery resumes**, the report will finally have real performance, wasted-spend flags and exact-match candidates — watch for the first non-zero window.

## Delivery
- No email/Gmail tool is connected. Cannot send a real email with subject. Deliver via: repo commit + Google Drive upload + PushNotification (its body also emails the user). State this limitation in the report's top note each run.
- Upload to Drive with `mcp__Google-Drive__create_file`, parentId = the 'PPC Reports' folder ID, textContent = markdown, contentMimeType `text/markdown`, `disableConversionToGoogleType: true` to keep it as a .md file.
