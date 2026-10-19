---
source_handle: google-tricorder-icse2015
fetched: 2026-10-18
source_url: https://www.cs.umd.edu/class/spring2019/cmsc414/papers/tricorder-building-a-program-analysis-ecosystem.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (11-page PDF, text extracted; plotted figures read only through captions and text)"
---

# Tricorder: Building a Program Analysis Ecosystem

## Source structure and scope
Caitlin Sadowski, Jeffrey van Gogh, Ciera Jaspan, Emma Söderberg, Collin Winter (Google, Inc.). Printed
as "ICSE 2015, Florence, Italy", DOI 10.1109/ICSE.2015.76 (as printed on the fetched PDF, a copy hosted on
a University of Maryland course page). Describes the design philosophy, analyzer-admission criteria, and
feedback mechanism of Google's code-review-time analysis platform, with in-situ usage data from 2014
(Figures 5-7) and a 90-day scalability table (Figure 9). Data are the authors' own deployment logs; no
control group. Tricorder "has been deployed in production since July 2013" (Section VII).

## Anchored details
- **Section III.A "No false positives":** "to a developer, a false positive is any report that they did not
  want to see". Definition:

  > We define an effective false positive as any report from the tool where a user chooses not to take action to resolve the report.

  An incorrect report whose suggested fix "would improve code readability" is "not considered a false
  positive". "The bottom line is that developers will decide whether an analysis tool has high impact, and
  what a false positive is."
- **Section III.B (analyzer contract):** analyzers may be disabled if "No one is fixing bugs filed against the
  analyzer" or "The analyzer results are annoying developers".
- **Section III.C "Make data-driven usability improvements":** "for one analyzer 75% of all bugs filed against
  the tool from TRICORDER were due to misinterpretations of the result wording and were fixed by updating the
  message text and/or linking to additional documentation."
- **Section III.D "Workflow integration is key":** surveyed developers "were twice as likely to say the error
  represented a significant bug when encountered as a compiler error" than when sent a fix changelist.
  Build-breaking analyses need an effective false positive rate "essentially zero";

  > Ideally, we only show results that cause builds to fail, as we have found warnings shown when building are often ignored.

  Code review is the primary integration point, with "peer accountability, where the reviewer will see if the
  author chose to ignore analysis results. We still enforce a very low effective false positive rate here (<
  10%)." Most analyses show results "on changed lines by default". A nightly code-search layer is used little
  but "is effective for analyses that have higher false positive rates and have a dedicated cleanup team to
  sift through the results."
- **Section III.E "Project customization, not user customization":** "We observed teams where a developer
  abandons a tool they were initially using after discovering teammates were committing new instances of code
  containing warnings flagged by the tool."
- **Section IV.C (criteria for new analyzers):** (1) easy to understand, clear fix; (2) "Developers should feel
  that we are pointing out an actual issue at least 90% of the time", measured by manually checking "a
  statistically sound sample size of the results"; footnote 5: "This 10% false positive threshold matches that
  used by other analysis platforms such as Coverity [13]." (3) potential for significant impact; (4) "if a
  warning occurs too frequently, it’s likely that it’s not causing any real problems. We don’t want to
  overwhelm people with too many warnings."
- **Section IV.E "Feedback":** links NOT USEFUL, PLEASE FIX (reviewers only), PREVIEW FIX, APPLY FIX. The
  "not-useful rate" is defined as `NOT USEFUL /(NOT USEFUL + PLEASE FIX + APPLY FIX)`.

  > A rate ≥ 10% puts the analyzer on probation, and the analysis writer must show progress toward addressing the issue. If the rate goes above 25%, we may decide to turn the analyzer off immediately

  "In practice, we typically work with the analyzer writers to fix the problem instead of immediately disabling
  an analyzer."
- **Section V.a "Usability":** the platform-wide weekly not-useful rate "in recent months it is typically at
  around 5%. When we remove analyzers that are on probation, the number goes down to under 4%." The
  DocComments analyzer was on probation until its author "worked to get the not-useful rate under 10%".
  Caveats on clicks: PLEASE FIX and APPLY FIX counts "are known to be low" because developers fix before review
  or in their own editor; "Developers may ignore findings they do not plan to fix, rather than clicking NOT
  USEFUL." "Our most successful analyzers have not-useful rate between 0-3%." The rate of filing bugs per NOT
  USEFUL click "is between 10-60%, depending on the analyzer."
- **Section V.b "Codebase Impact" / Figure 8:** after a ClangTidy check began showing in code review, codebase
  instances "decreased dramatically"; other checks show "drop-off or level-off".
- **Section V.d / Figure 9 (averages over 90 days):** 93K findings/day, 716 "Please fix"/day, 48 "Not
  useful"/day; "An average CL has two please-fix clicks and no not-useful clicks." Most findings "are not
  actually shown in the review as they appear on unchanged lines"; footnote 6: "we do not have the ability to
  measure how many results are viewed by developers."
- **Section VI (related work):** commercial dashboards were found "only useful for analysis writers to help
  them improve the quality of the analyzers."
