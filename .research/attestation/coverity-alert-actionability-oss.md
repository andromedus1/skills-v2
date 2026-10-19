---
source_handle: coverity-alert-actionability-oss
fetched: 2026-10-18
source_url: https://www.microsoft.com/en-us/research/?p=690690
provenance: source-direct
substrate_confidence: snippet-thin
engagement_depth: abstract
---

# How Do Developers Act on Static Analysis Alerts? An Empirical Study of Coverity Usage

## Source structure and scope
Nasif Imtiaz, Brendan Murphy, Laurie Williams. 2019 IEEE 30th International Symposium on Software Reliability
Engineering (ISSRE), dated October 2019 on the fetched Microsoft Research publication page. Only the landing
page and its abstract were read; the full paper (IEEE Xplore) was not fetched. An empirical mining study of five
open-source projects (Linux, Firefox, Samba, Kodi, Ovirt-engine) that used Coverity for at least five years.
The abstract states that alert occurrences and developer triage were taken "from the Coverity database"; the
abstract does not describe where in the projects' workflow the alerts were shown to developers.

## Anchored details
- **Abstract (method):** the authors "identify the alerts that were fixed through code changes (i.e.
  actionable) by mining the commit history of the projects" and "analyze the time an alert remain in the code
  base (i.e. lifespan)".
- **Abstract (results):**

  > We find that 27.4% to 49.5% (median: 36.7%) of the alerts are actionable across projects, a rate higher than previously reported.

  Fixes are "generally low in complexity (2 to 7 lines of code changes in the affected file, median: 4).
  However, developers still take from 36 to 245 days (median: 96) to fix these alerts." Also: "severity and fix
  complexity may correlate with an alert's lifespan in some of the projects."
- **Definition used:** "actionable" here means fixed through a code change, detected from commit history; it is
  not the developer-perception definition used in some industrial reports.
