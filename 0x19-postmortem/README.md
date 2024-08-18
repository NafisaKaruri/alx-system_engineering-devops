# My first postmortem

Using task **0x17. Web stack debugging #3** issue, I wrote a postmortem according to the below format.

## Issue Summary

- Duration of the outage with start and end times with timezones.
- Impact: what service was down/slow? What were user experiencing? How many % of the users were affected?
- Root Cause of the issue.

---

## Timeline

Bullet points, format: time - keep it short, 1 or 2 sentences
- When was the issue detected
- How was the issue detected (monitoring alert, an engineer noticed something, a customer complained...)
- Actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
- Misleading investigation/debugging paths that were taken
- Which team/individuals was the incident escalated to
- How the incident was resolved

---

## Root Cause and Resolution

- Explain in detail what was causing the issue
- Explain in detail how the issue was fixed

---

## Correction and Prevention Measures

- What are the things that can be improved/fixed (broadly speaking)
- A list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory...)
