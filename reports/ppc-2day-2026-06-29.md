# PPC 2-Day Report — 25–26 June 2026

**Report type:** 2-day · **Dates covered:** Thursday 25 June – Friday 26 June 2026
**Generated:** 29 June 2026 (data lags ~48h, so the window ends 48h before the run)

---

## ⚠️ Read this first — no data this run (configuration problem)

This report could **not** pull any advertising numbers, so there is no data
table and no comparison below. Nothing here is estimated or made up — when the
data can't be pulled, the report stays empty on purpose.

**In plain English:** the login worked, but the account "address" the report
uses to find your ads campaigns is set to the wrong kind of value, so Amazon
rejected every request.

**What went wrong, specifically:**
- The setting `AMZ_PROFILE_ID` is currently
  `amzn1.application.dd42b8099dc749e2af846cb301ada5c5`.
- That is an **application ID** (the ID of the software connection), not an
  **advertising profile ID**. A real profile ID is a long string of **numbers**
  (for example `1234567890123456`).
- Amazon's API confirmed this: it replied `Invalid scope: amzn1.application…`
  and `profile ID required`.

**What I tried (so you know it was a real attempt, not a skipped run):**
1. Logged in with the refresh token — **succeeded**, a valid access token was issued.
2. Asked Amazon for the list of advertising profiles on the US/North America
   region — it returned an **empty list**, so I couldn't auto-correct the ID.
3. Tried the US, Europe and Far-East data centres. The **Europe and Far-East**
   endpoints are **blocked by this environment's network policy** (403), so if
   your seller account lives in one of those regions I currently can't reach it.
4. Sent a test report request anyway with the configured ID — Amazon rejected
   it for the reason above.

**What you need to do (one-time fix):**
1. Set `AMZ_PROFILE_ID` to the correct **numeric** Amazon Ads profile ID for
   your account. You can find it in the Amazon Ads console, or via
   `GET /v2/profiles` with these same credentials.
2. If your seller account is in **Europe or the Far East**, also allow outbound
   access to `advertising-api-eu.amazon.com` / `advertising-api-fe.amazon.com`
   in this environment's network policy (only the US endpoint is allowed today).

Once that's fixed, the next scheduled run will pull the data and produce the
full table, summary and comparison automatically.

---

## Part A — Data table
_Not available this run — see the note above._

## Part B — Summary
_Not available this run — see the note above._

## Part C — Comparison to previous 2-day report
No previous 2-day report exists yet (this is the first run), and there is no
data this run, so there is nothing to compare. Once two successful runs have
completed, this section will show the change in spend, sales, ACOS and ROAS as
both a number and a percentage.

---

### What to do next
- **Owner action:** fix `AMZ_PROFILE_ID` (numeric profile ID) and, if needed,
  unblock the EU/FE advertising endpoints — details above.
- **Automatic:** the next run will retry the pull with no changes needed from you.
