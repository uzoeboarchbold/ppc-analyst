# Notes to self — PPC Analyst runs

Running log of lessons so future runs are faster and more reliable.

## Account / API setup (learned 2026-10-02)
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** Its value is
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`, which is an LWA
  *application* ID, not a numeric Amazon Ads profile ID. Do NOT pass it as
  `Amazon-Advertising-API-Scope` — it matches no real profile.
- The LWA refresh-token flow works fine (token endpoint
  https://api.amazon.com/auth/o2/token). Region host = NA
  `advertising-api.amazon.com`. EU/FE hosts are BLOCKED by the sandbox
  network policy (403 on CONNECT) — don't waste time on them; this account
  is NA anyway.
- `GET /v2/profiles` on NA returns 3 profiles for this account
  (seller "Uzoebo Archbold E-Commerce", account A1C2I8MOP52E35):
    - CA  profileId 2840235221595557  (CAD) — 0 SP campaigns
    - MX  profileId 3892485344323414  (MXN) — 0 SP campaigns
    - **US  profileId 26765323558215  (USD) — 54 SP campaigns  <-- THE ACTIVE ONE**
  => Always report on the **US profile 26765323558215** unless the owner
  says otherwise. (Empirically confirmed: only US has SP campaigns.)
- Product being advertised: ASIN B0FXW3GW5F — Cat Deterrent Spray / Pet
  Odor Eliminator (campaign SKU prefix 6K-PZMX-MTDZ).

## Data pulling
- Use the v3 async reporting API: POST /reporting/reports (content-type
  `application/vnd.createasyncreportrequest.v3+json`), poll
  GET /reporting/reports/{id} every ~15s until COMPLETED, then download the
  presigned `url` (GZIP_JSON). Works reliably.
- Report types used: `spCampaigns` (campaign table + topOfSearchImpressionShare),
  `spTargeting` (keyword/target level), `spSearchTerm` (search terms to add).
- Metric column names are the 7-day attribution ones: `purchases7d`, `sales7d`.
  ACOS = cost/sales, ROAS = sales/cost, CTR = clicks/impressions,
  CPC = cost/clicks — compute these yourself; the API doesn't return them directly.

## IMPORTANT standing finding (2026-10-02)
- **The US account has `validPaymentMethod: false` and ad delivery has been
  ZERO since ~Sept 3, 2026.** Daily probe Sept 1–29: only Sept 1 (234 imp,
  1 click, $0.08) and Sept 2 (53 imp) had any delivery; Sept 3–29 all zero.
  The campaigns are ENABLED but Amazon is not serving them. Root cause is
  almost certainly the missing/invalid payment method. Until the owner fixes
  billing in Seller Central, every report will show zeros. Flag this loudly
  each run until it changes.

## Reporting mechanics
- reports/ folder: overwrite `ppc-2day-latest.md` + save dated copy
  `ppc-2day-[YYYY-MM-DD].md`. Compare each run against the previous report of
  the SAME type.
- Date window (data lags 48h): 2-day report covers the 2 full days ending 48h
  before run time. For a Friday run, that's the preceding Mon–Tue
  (run_day-4 and run_day-3).
- Delivery targets: commit to repo, upload to Google Drive folder "PPC
  Reports", email uzoebo.archbold@gmail.com.
- Google Drive "PPC Reports" folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
  Upload with mcp__Google-Drive__create_file (textContent, contentMimeType
  text/markdown, disableConversionToGoogleType=true). Works fine.
- **EMAIL CANNOT BE SENT from the scheduled run (as of 2026-10-02).** A Gmail
  connector exists and is authenticated at the org level, but it is
  `enabledInChat: false` for this session, so no gmail send/draft tool loads.
  There is no other email tool. Until the owner enables the Gmail connector
  for this automation's chat/session, the email step will be skipped every run
  — rely on the repo commit + Drive upload + the push notification instead, and
  state in the run summary that email was not sent.
