# Notes to self — PPC Analyst

Running log of lessons so future runs go smoother. Newest first.

## 2026-10-29 — 2-day run: BLOCKED (network policy on EU/FE Ads API)

**What happened:** Could not pull data for the configured ad profile.
Diagnosis was clean and is worth remembering:

- Auth is FINE. Token refresh at `api.amazon.com` succeeds. The North
  America Ads host `advertising-api.amazon.com` returns HTTP 200 and lists
  **3 profiles** — but **none match `AMZ_PROFILE_ID`**. So the target
  profile is not an NA profile.
- The target profile lives in **EU or Far-East**, and the environment's
  outbound **network policy BLOCKS** those hosts:
  - `advertising-api-eu.amazon.com` → `Tunnel connection failed: 403 Forbidden`
  - `advertising-api-fe.amazon.com` → `Tunnel connection failed: 403 Forbidden`
- A 403 on the proxy CONNECT is a **policy denial**, not an auth/token
  problem. Do NOT retry it and do NOT try to bypass TLS or the proxy —
  retries won't help and bypassing is forbidden.

**What I tried:** refreshed token (worked), probed all 3 regional hosts,
confirmed NA reachable but profile absent, EU/FE blocked at the proxy.
Verified with `curl "$HTTPS_PROXY/__agentproxy/status"` → `recentRelayFailures`
shows `connect_rejected` / `403` for `advertising-api-eu.amazon.com:443`.

**The fix (needs a human — infra/config, not code):**
1. Update the session's **network policy** to allow outbound HTTPS to
   `advertising-api-eu.amazon.com` and `advertising-api-fe.amazon.com`
   (and keep `api.amazon.com` + `advertising-api.amazon.com` allowed).
   The policy is chosen when the environment is created — see
   https://code.claude.com/docs/en/claude-code-on-the-web
   OR
2. If the account really is North America, set `AMZ_PROFILE_ID` to one of
   the 3 NA profiles the API returns.

**For next run:** the pull script lives in scratchpad (`pull.py`). It already
(a) refreshes the token, (b) auto-detects the region by probing profiles,
(c) uses the v3 reporting API (`spCampaigns` + `spTargeting`, SUMMARY,
GZIP_JSON), (d) never prints credential values. Reuse its logic. First
thing to check if a run fails: `curl -sS "$HTTPS_PROXY/__agentproxy/status"`
to see if the Ads host is policy-blocked before assuming an auth issue.

## General reminders
- Data lags ~48h. 2-day report covers the 2 full days ending 48h before run.
- Never invent numbers. On failure, write a plain-English note at the top of
  the report and add a line here.
- Save `reports/ppc-2day-latest.md` + dated copy, commit+push to the
  designated branch, upload to Google Drive 'PPC Reports', email the user.
