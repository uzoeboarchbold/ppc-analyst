# Notes to Self — PPC Analyst

Running log of lessons so future automated runs go smoothly. Append, don't rewrite history.

## Account / API facts (verified 2026-10-10)
- **`AMZ_PROFILE_ID` env var is WRONG.** It holds an *application* id
  (`amzn1.application....`), not a numeric advertising profile id. Do **not**
  pass it as `Amazon-Advertising-API-Scope`.
- Real profiles under these creds (region NA, host `advertising-api.amazon.com`):
  - US `26765323558215` (USD) — **the only account with campaigns (54; 15 enabled)**. Use this.
  - CA `2840235221595557` (CAD) — no campaigns.
  - MX `3892485344323414` (MXN) — no campaigns.
- EU (`-eu`) and FE (`-fe`) hosts are **blocked by the agent proxy (403)**. All
  three profiles are NA anyway, so this does not matter.
- LWA token refresh works: POST `https://api.amazon.com/auth/o2/token`.
  Use the proxy CA bundle `/root/.ccr/ca-bundle.crt` for SSL.
- Reporting = Ads API **v3** async: POST `/reporting/reports`, poll
  `/reporting/reports/{id}`, download presigned GZIP_JSON. Helper lives in
  `scripts/pull_ppc.py` (reusable; US profile hard-coded as default).
- Report type ids used: `spCampaigns` (groupBy campaign), `spTargeting`
  (groupBy targeting), `spSearchTerm` (groupBy searchTerm). Top-of-search
  impression share is only available at the **campaign** level.
- Attribution: using 14-day columns (`sales14d`, `purchases14d`). For very
  recent windows 14d attribution is still maturing — note this when conversions
  look low on recent dates.

## Product
- Single ASIN in play: **B0FXW3GW5F** — a cat deterrent spray / pet odor
  eliminator (plus one older "Cat Tunnel Bed" campaign).

## Standing observations
- **2026-10-10 (first run): ZERO activity.** All 15 enabled campaigns returned
  **0 impressions / 0 clicks / 0 cost / 0 sales** over the whole window AND over
  a 23-day probe (Sep 15–Oct 7). API is healthy (returns the 15 campaign rows) —
  the account genuinely is not serving. Enabled since May 2026, budgets mostly
  $1.50/day ($23.50/day total). Zero *impressions* (not just zero clicks) points
  to a listing-eligibility problem (out of stock / suppressed listing / lost Buy
  Box) or bids far below market — NOT a reporting bug. Flag this every run until
  impressions appear.
- When everything is zero, say so plainly and do not fabricate numbers. The
  comparison section should still run (vs. the previous report of the same type).

## Delivery channels
- **Google Drive: works.** Folder "PPC Reports" id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with `create_file`, `textContent=<report>`, `contentMimeType=text/markdown`,
  `disableConversionToGoogleType=true`. NOTE: `textContent` is literal — do NOT
  pass shell like `$(cat ...)`; paste the actual text (a `$(cat)` upload made a
  6-byte junk file that had to be trashed and re-created on the first run).
- **Email: BLOCKED (2026-10-10).** A Gmail connector exists and is connected at
  org level but `enabledInChat: false`, so no gmail tools load in this headless
  session and I cannot send the report by email. No other email/SMTP tool is
  available. User must enable the Gmail connector for this chat/automation (chat
  connector settings) for email delivery to work. Until then, deliver via repo +
  Drive and flag the missing email in the run notification.

## Housekeeping
- No previous 2-day report existed on the first run (2026-10-10) — created
  `reports/` fresh. Compare future runs against `reports/ppc-2day-latest.md`
  BEFORE overwriting it (read it first, then overwrite).
- Deliverables each run: overwrite `reports/ppc-2day-latest.md`, write dated
  `reports/ppc-2day-YYYY-MM-DD.md`, commit+push branch `claude/great-hopper-wtoh4c`,
  upload to Google Drive folder "PPC Reports", email uzoebo.archbold@gmail.com.
