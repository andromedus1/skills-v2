---
source_handle: sre-monitoring-distributed-systems
fetched: 2026-10-18
source_url: https://sre.google/sre-book/monitoring-distributed-systems/
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (whole chapter web page, HTML converted to text)"
---

# Monitoring Distributed Systems (Site Reliability Engineering, Chapter 6)

## Source structure and scope
"Chapter 6 - Monitoring Distributed Systems", "Written by Rob Ewaschuk, Edited by Betsy Beyer", in the online
edition of Google's Site Reliability Engineering book; the page footer reads "Copyright © 2017 Google, Inc.
Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0". Practitioner guidance from Google SRE on what
should page a human versus go to tickets, email, or dashboards; includes two short case studies (Bigtable,
Gmail). Normative guidance and narrative, no quantitative study.

## Anchored details
- **"Definitions":** an alert is "A notification intended to be read by a human and that is pushed to a system
  such as a bug or ticket queue, an email alias, or a pager. Respectively, these alerts are classified as tickets,
  email alerts, and pages." Footnote 22 on email alerts: "Sometimes known as "alert spam," as they are rarely read
  or acted on."
- **"Why Monitor?":**

  > When pages occur too frequently, employees second-guess, skim, or even ignore incoming alerts, sometimes even ignoring a "real" page that’s masked by the noise.

  "Effective alerting systems have good signal and very low noise." One "should never trigger an alert simply
  because "something seems a bit weird.""
- **"Tying These Principles Together" (questions for alert rules, "avoid false positives and pager
  burnout"):** "Does this rule detect an otherwise undetected condition that is urgent, actionable, and actively or
  imminently user-visible?" and "Will I ever be able to ignore this alert, knowing it’s benign? When and why will I
  be able to ignore this alert, and how can I avoid this scenario?" Philosophy on pages: "I can only react with a
  sense of urgency a few times a day before I become fatigued." "Every page should be actionable." "If a page
  merely merits a robotic response, it shouldn’t be a page."
- **"Bigtable SRE: A Tale of Over-Alerting":** email and paging alerts were "firing voluminously"; the team
  "often missed the problems that actually affected users". Remedy included temporarily relaxing the SLO target
  and: "We also disabled email alerts, as there were so many that spending time diagnosing them was infeasible."
- **"Gmail: Predictable, Scriptable Responses from Humans":** "Pages with rote, algorithmic responses should be a
  red flag."
- **"The Long Run":** page frequency statistics (incidents per shift) are reviewed "in quarterly reports with
  management".
- **"Conclusion":**

  > Email alerts are of very limited value and tend to easily become overrun with noise; instead, you should favor a dashboard that monitors all ongoing subcritical problems for the sort of information that typically ends up in email alerts.
