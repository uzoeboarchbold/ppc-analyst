# Notes to Self — PPC Analyst

Running log of lessons so future automated runs go smoother. Newest first.

## 2026-08-25 (2-day run) — Could not pull data: profile ID + region blocked
- **Auth works.** Refreshing the access token via `AMZ_REFRESH_TOKEN` /
  `AMZ_CLIENT_ID` / `AMZ_CLIENT_SECRET` against
  `https://api.amazon.com/auth/o2/token` succeeds (bearer token, 3600s). So the
  client credentials and refresh token are valid.
- **`AMZ_PROFILE_ID` looks wrong.** Its value starts with `amzn…` and is ~50
  chars. A real Amazon Ads profile ID is a **numeric** integer (roughly 10
  digits). When used as the `Amazon-Advertising-API-Scope` header the API
  returns HTTP 400 `"Invalid Input ... profile ID required"`. The env var
  appears to hold an entity/account identifier, not the numeric profile ID.
- **Region is blocked.** Listing `/v2/profiles` on the **NA** host
  (`advertising-api.amazon.com`) succeeds but returns **0 profiles** — so this
  account has no NA profile. The **EU** (`advertising-api-eu.amazon.com`) and
  **FE** (`advertising-api-fe.amazon.com`) hosts are **blocked by this
  session's outbound network policy** (proxy answers 403 to CONNECT). The
  README says not to retry org policy denials. So if the real profile lives in
  EU/FE, this session cannot reach it at all.
- **What the owner needs to do (one or both):**
  1. Set `AMZ_PROFILE_ID` to the correct **numeric** profile ID. Find it by
     calling `/v2/profiles` in the account's region.
  2. If the account's marketplace is EU or FE, either add the matching
     `advertising-api-eu/fe.amazon.com` host to this environment's allowed
     egress list, or run this routine from an environment whose network policy
     permits that region.
- **Next run:** try `/v2/profiles` on NA first; if 0 profiles, the region/host
  is the issue — surface it rather than guessing. Never fabricate metrics.
- **First run:** no prior 2-day report existed, so no comparison was possible.
