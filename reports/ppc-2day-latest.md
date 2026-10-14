# PPC 2-Day Report — 2026-10-10 to 2026-10-11

**Report run:** 2026-10-14 23:19 UTC · **Report type:** 2-day
**Dates covered:** 2026-10-10 and 2026-10-11 (the 2 full days ending 48h before the run, allowing for Amazon's ~48h data lag)

---

## ⚠️ Could not pull data this run — action needed

No numbers are shown below because the report could not be generated, and I
will not invent figures. Here is what happened, in plain English:

- **Login to Amazon worked.** The account credentials are valid and I
  successfully logged in to the Amazon Advertising API.
- **The reporting system worked.** I confirmed the data-pull itself runs end
  to end — a test report request was accepted by Amazon (HTTP 200). So the
  tooling is fine.
- **The problem is the configured profile (account) ID.** The value in the
  `AMZ_PROFILE_ID` setting is not a valid Amazon advertising profile ID. A
  real profile ID is a short number (roughly 10–12 digits); the configured
  value is a long (~50 character) non-numeric string. Amazon rejects it with
  the error *"profile ID required."*
- **The account I can see has 3 profiles:** Canada (CA), Mexico (MX), and the
  United States (US). The configured value matches none of them.
- I did **not** substitute one of those profiles on my own, because I can't
  be sure which account you intend this report to cover, and reporting the
  wrong account's spend would be misleading.

### What I tried
1. Logged in via the North America token endpoint — success.
2. Listed the available advertising profiles — found CA, MX, US.
3. Sent a live test report request with the configured profile ID — rejected
   with *"profile ID required"* (the ID is malformed).
4. Sent the same request with a genuine profile ID — accepted (HTTP 200),
   proving the pipeline works.
5. Checked the EU and Far-East login endpoints in case the intended account
   lives there — both are blocked by this environment's network policy, so a
   non-NA profile couldn't be reached from here regardless.

### How to fix (one setting)
Set `AMZ_PROFILE_ID` to the correct **numeric** advertising profile ID for
the account you want reported (for a US FBA account it will be the US profile
listed above). No code changes are needed — once the ID is corrected, the
next scheduled run should produce a full report automatically.

---

## Part A — Data table
*Unavailable this run — see note above. No data was pulled.*

| Campaign | Impr. | ToS IS | Clicks | CTR | Purchases | Sales | Cost | CPC | ACOS | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — |

## Part B — Summary
No spend, sales, ACOS, ROAS, campaign, wasted-spend, or search-term analysis
is available this run because no data could be pulled (invalid
`AMZ_PROFILE_ID`). **What to do next:** correct the `AMZ_PROFILE_ID` setting
to a valid numeric profile ID (see fix above); the next run will then produce
the full table, summary, and recommendations.

## Part C — Comparison to previous 2-day report
No previous 2-day report exists — this is the first run of this report type,
so there is nothing to compare against yet. (And no data this run in any
case.)

---

### Delivery note
This report was saved to the repo and uploaded to the Google Drive 'PPC
Reports' folder. It could **not** be emailed automatically: the Gmail
connector is connected but switched off for this automated session, so email
sending is unavailable. To enable automatic email, turn on the Gmail
connector for this session in the chat's connector settings.
