# Notes to Self — PPC Analyst

Running log of lessons so future runs are smoother. Newest at top.

## 2026-06-25 (first run — 2-day report)
- **AMZ_PROFILE_ID env var is MISCONFIGURED.** It is set to an *application ID*
  (`amzn1.application.dd42b8099dc749e2af846cb301ada5c5`), NOT an advertising
  profile ID. Do not pass it to the Ads API — it will fail.
- **Resolve the profile at runtime** by calling `GET /v2/profiles` on the NA
  endpoint and picking the right one. Available profiles (seller "Uzoebo
  Archbold E-Commerce"):
    - US: `26765323558215` (USD, dailyBudget 40.0)  ← ACTIVE advertising account
    - CA: `2840235221595557` (CAD, dailyBudget default/unlimited — not active)
    - MX: `3892485344323414` (MXN, dailyBudget default/unlimited — not active)
  Use the **US profile `26765323558215`** — it is the only one with a real
  daily budget, i.e. where ads actually run. Reports are in **USD**.
- **Region = NA** (`advertising-api.amazon.com`). EU and FE endpoints are
  BLOCKED by the network proxy (CONNECT tunnel 403), so only NA is reachable.
- **Token refresh** works against `https://api.amazon.com/auth/o2/token` with
  the env creds. Access token lasts 3600s.
- **Date window logic (2-day):** end 48h before run, cover the 2 full days
  before that cutoff. Run 2026-06-25 23:02 UTC → cutoff 06-23 23:02 → cover
  **06-21 and 06-22**.
- Reports folder + previous report did not exist on first run; created them.
- Reporting API: use v3 async `/reporting/reports` (adProduct
  SPONSORED_PRODUCTS). topOfSearchImpressionShare is available in the campaign
  groupBy report. Compute CTR/CPC/ACOS/ROAS ourselves from raw columns.
- **ACCOUNT IS CURRENTLY DARK.** As of this run, of 54 SP campaigns only 2 are
  ENABLED ("SP KT | ST w/ Sales", "SP PT | ST w/ Sales", $8 budget each) and
  even those served 0 impressions. Everything else PAUSED/ARCHIVED. Zero spend
  the whole week 06-15→06-22. Last real activity was before 06-15 (last 30 days
  did have ~$541 spend / 16,138 impr across 25 campaigns). Future runs: if a
  window is all-zero, confirm with a wider lookback + campaign state list before
  concluding it's real (this is how I verified). Flag the "dark" status loudly.
- **NO EMAIL TOOL in this environment.** Searched gmail/smtp/email — none of the
  connected MCP servers (Google-Drive, github) expose a send-email tool. STEP 4's
  email could NOT be sent. The report is saved to repo + uploaded to the
  'PPC Reports' Drive folder, and the owner is reached via PushNotification
  instead. If an email tool appears later, wire it in. The owner's address is
  uzoebo.archbold@gmail.com, subject format "PPC 2-Day Report — [dates]".
- **Google-Drive MCP has NO delete/update tool** (only create/copy/read/search).
  My first create_file used a placeholder body by mistake → a stray 9-byte file
  ("PPC 2-Day Report — 21-22 Jun 2026.md", id 11r6m7CYYyg2fOLeT2h7XVWjCwakoh6hn)
  remains alongside the correct 4300-byte one (id 1yqhbcShOLphxj9op-sEMRNkmpEFt9WL8).
  Can't remove it via API — clean up manually if it matters. Next time: build the
  full base64/text body FIRST, upload once.
- 'PPC Reports' Drive folder id = `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`.
