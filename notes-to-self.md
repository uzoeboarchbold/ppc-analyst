# Notes to Self — PPC Analyst routine

Lessons learned to make future runs smoother. Read this first, every run.

## Environment / setup

- **`AMZ_PROFILE_ID` is wrong (recurring).** It holds an *application* ID
  (`amzn1.application.…`), NOT a numeric advertising profile ID. Do not use it directly.
  The correct **US** profile is **`26765323558215`** (USD, the only profile with campaigns).
  The other profiles have zero campaigns: Canada `2840235221595557`, Mexico `3892485344323414`.
  Always hard-code / look up the US profile. (Worth asking the owner to fix the env var at source.)

- **Region:** Only the NA endpoint `https://advertising-api.amazon.com` is reachable/needed.
  The EU (`-eu`) and FE (`-fe`) hosts are blocked by the proxy (CONNECT 403) — that's fine, the
  account is US-only, so ignore those errors.

- **Token refresh works:** POST `https://api.amazon.com/auth/o2/token` with grant_type=refresh_token,
  refresh_token, client_id, client_secret. Returns access_token. (Earlier runs once hit a blocked
  login host; not an issue now — `api.amazon.com` is reachable.)

## Reporting API (v3) gotchas

- Use the async reporting API: POST `/reporting/reports` (Content-Type
  `application/vnd.createasyncreportrequest.v3+json`), then poll `/reporting/reports/{id}` every ~15s
  until status COMPLETED, then download the gzipped JSON from the returned `url`.
- **spCampaigns does NOT accept `acosClicks7d` / `roasClicks7d` columns** — the request 400s.
  Valid columns include: impressions, clicks, cost, costPerClick, clickThroughRate, purchases7d,
  sales7d, topOfSearchImpressionShare, campaignName, campaignId, campaignStatus, campaignBudgetAmount.
  **Compute ACOS = cost/sales and ROAS = sales/cost yourself.** (spSearchTerm and spTargeting DO accept
  acosClicks7d/roasClicks7d.)
- When there are zero impressions, the searchTerm and targeting reports come back with 0 rows, and the
  campaigns report returns only a couple of all-zero rows — that's expected, not an error.

## Finding the previous report of this type (IMPORTANT)

- The git repo is a fresh, near-empty clone each run (only README + this branch). **The `reports/`
  folder is empty at the start of every run**, so you will NOT find prior reports there.
- **The real report history lives in Google Drive, folder 'PPC Reports'**
  (id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). Search it with
  `parentId = '1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo'` and find the most recent `ppc-2day-YYYY-MM-DD.md`
  BEFORE today to compare against.
- **Do NOT write "no previous report exists" — that was a repeated mistake in earlier runs** that only
  checked the empty repo. There is a long history in Drive (going back to mid-June). The filename date
  is the *generation/run* date; the covered window is ~4 days earlier.

## Delivery

- **No email/Gmail tool is connected** in this session. The "email to uzoebo.archbold@gmail.com" step
  cannot be completed. Deliver via: (1) commit to repo, (2) upload to Drive 'PPC Reports', (3) push
  notification with the headline. State the email gap plainly in the report's delivery note.
- Upload the report to Drive with `mcp__Google-Drive__create_file`, parentId
  `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`, textContent = the markdown, contentMimeType `text/markdown`,
  title `ppc-2day-YYYY-MM-DD.md`. Set `disableConversionToGoogleType: true` to keep it as markdown
  (otherwise Drive converts it to a Google Doc).

## Account context (as of early July 2026)

- The account has been **dark since ~9 June 2026** — zero impressions/spend/sales for weeks.
  54 campaigns: only 2 ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8/day each), 45 PAUSED,
  7 ARCHIVED. The 2 enabled ones have healthy structure (enabled ad groups, keywords bid $0.82–$2.13,
  ASIN targets bid $1.15–$2.09) yet win **zero** impressions.
- Most likely root cause of zero delivery: **advertised product not eligible to serve** (out of stock /
  lost Buy Box / suppressed listing) rather than bids/budget. Flag this for the owner each run.
- Because it's zero every run, keep reports short and consistent; the key signal to watch is
  impressions rising above zero (delivery resumed).
