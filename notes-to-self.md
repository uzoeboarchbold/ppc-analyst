# Notes to self — PPC Analyst runs

Running log of lessons so future runs get smarter. Newest first.

## 2026-09-26 (2-day report run)
- **Environment & first run.** Repo was empty (only README). Created `reports/`
  folder and this notes file. No previous 2-day report existed, so no
  comparison was possible this run.
- **Date window logic (confirmed working).** Data finalises ~48h after each day
  ends. Rule that matches the brief's example: the most recent *fully final*
  day is the last calendar day D where `(D end) + 48h <= now`. For a run at
  2026-09-26 23:19 UTC that is D = 2026-09-23, so the 2-day window is
  **2026-09-22 → 2026-09-23**.
- **Amazon Ads API auth: WORKS.** LWA token endpoint
  `https://api.amazon.com/auth/o2/token` with the four `AMZ_*` env vars returns
  a valid access token. Keep using that.
- **BLOCKER — profile is in a region the egress policy blocks.**
  - Auth succeeds. The NA endpoint `advertising-api.amazon.com` is reachable and
    returns 3 profiles (countryCodes CA / MX / US).
  - The configured `AMZ_PROFILE_ID` is **not** one of the NA profiles. Submitting
    an SP report to NA with that scope returns
    `400 "profile ID required"` (Amazon's way of saying the profile is not valid
    for this endpoint). => the profile lives in the **EU** or **FE** region.
  - The EU/FE Ad API hosts (`advertising-api-eu.amazon.com`,
    `advertising-api-fe.amazon.com`) are **blocked by the org egress policy**:
    the agent proxy returns `403 Forbidden` on CONNECT. Per
    `/root/.ccr/README.md`, policy denials (403/407) must NOT be retried or
    routed around — report the blocked host instead.
  - **Net result:** cannot pull data until either (a) the correct NA profile ID
    is supplied, or (b) the egress policy is updated to allow the EU/FE
    advertising-api host that matches the profile's region.
  - **Action for the human:** confirm which marketplace the account is in and
    either set `AMZ_PROFILE_ID` to the matching NA profile, OR ask the admin to
    allow the EU/FE `advertising-api-*.amazon.com` host in the session's network
    policy.
- **Delivery this run.** Google Drive upload to the "PPC Reports" folder
  SUCCEEDED (folder id `1lm39VQ4yqDL0bfEEjl0X4E7w1nTeHzKo`). **Email FAILED —
  no email/Gmail connector is available in this session** (only Google-Drive and
  github MCP servers are connected). To enable auto-email, the human needs to add
  a Gmail/email connector to this automation. Until then, delivery is
  Drive + git commit only, and the human should be notified another way.
- **FUTURE RUN SHORTCUT:** first hit `/v2/profiles` on NA. If the configured
  profile is listed, proceed on NA. If not, and EU/FE are still 403, stop and
  write the blocker note (don't waste time) — the fix is human-side (profile ID
  or egress policy), not code.
