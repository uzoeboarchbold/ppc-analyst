# Notes to self — PPC Analyst runs

Running log of lessons so future runs are smoother. Newest first.

## 2026-11-05 — 2-day report (FIRST RUN)

**Blocker: Amazon Ads API hosts are blocked by the session network policy.**
- The LWA token endpoint `https://api.amazon.com/auth/o2/token` IS reachable
  through the proxy and the refresh-token exchange SUCCEEDS — so the four
  `AMZ_*` credentials are present and valid.
- BUT every Advertising API data host returns **403 to CONNECT** at the egress
  proxy (a network-policy denial, not an auth error):
  - `advertising-api.amazon.com` (NA)
  - `advertising-api-eu.amazon.com` (EU)
  - `advertising-api-fe.amazon.com` (FE)
  Confirmed via `curl $HTTPS_PROXY/__agentproxy/status` → `recentRelayFailures`
  shows `connect_rejected / gateway answered 403 to CONNECT` for those hosts.
- Per `/root/.ccr/README.md`: a 403 from the proxy means the host is not on the
  allowlist. **Do NOT retry or route around it** — it must be fixed by the
  human in the environment's network settings.
- **ACTION FOR THE HUMAN:** add the Amazon Advertising API host(s) for your
  marketplace region to this environment's outbound network allowlist
  (NA=`advertising-api.amazon.com`, EU=`advertising-api-eu.amazon.com`,
  FE=`advertising-api-fe.amazon.com`). Environment network policy is set when
  the environment is created — see
  https://code.claude.com/docs/en/claude-code-on-the-web
- Until that is done, NO real PPC numbers can be pulled. Do not invent data.

**Delivery channels available this session:**
- Google Drive MCP: AVAILABLE (`mcp__Google-Drive__*`). Folder 'PPC Reports'
  used for uploads.
- Email: **NO email/Gmail tool is available in this session.** Could not send
  the "PPC 2-Day Report" email to uzoebo.archbold@gmail.com. The PushNotification
  (routine notification) goes to the user's phone + inbox instead, which covers
  the alert. If real emailing is required, a Gmail/email MCP connector needs to
  be added to the environment.

**Date window logic (verified):** data lags ~48h. For the 2-day report, cover
the 2 full days ending 48h before run. Run 2026-11-05 23:10 UTC → window
2026-11-01 to 2026-11-02. (anchor = now-48h = Nov 3 23:10; last full day = Nov 2;
first day = Nov 1.)

**Report files:** `reports/ppc-2day-latest.md` (overwrite) +
`reports/ppc-2day-YYYY-MM-DD.md` (dated copy). Compare each run against the
previous report of the SAME type. This was the first run → no prior 2-day
report to compare against.

**Data pull script kept at** (scratchpad, not committed):
pull_ppc.py — uses Amazon Ads API v3 reporting (createAsyncReport):
POST /reporting/reports with reportTypeId spCampaigns (groupBy campaign) and
spTargeting (groupBy targeting), timeUnit SUMMARY, format GZIP_JSON; polls
/reporting/reports/{id}; downloads+gunzips. Ready to use once hosts are allowed.
