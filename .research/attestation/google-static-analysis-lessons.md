---
source_handle: google-static-analysis-lessons
fetched: 2026-10-18
source_url: https://6826.csail.mit.edu/2020/papers/google-analysis-cacm.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (9-page CACM PDF, text extracted; figures and images not read)"
---

# Lessons from Building Static Analysis Tools at Google

## Source structure and scope
Caitlin Sadowski, Edward Aftandilian, Alex Eagle, Liam Miller-Cushon, and Ciera Jaspan (all Google,
per the author notes). Communications of the ACM, vol. 61, no. 4, April 2018, pp. 58-66,
DOI 10.1145/3188720 (as printed on the fetched PDF, a copy hosted on an MIT course page). A
"contributed article": an organizational experience report on static analysis at Google, covering three
failed FindBugs integrations (2006-2011), compiler-error checks (Error Prone, Clang), and code-review
checks (Tricorder). Evidence is a mix of described practice, internal usage counts as of January 2018,
and internal surveys; no controlled comparison is reported. Engagement: whole article read.

## Anchored details
- **"Terminology":** defines the effective false positive by developer action, not analysis correctness:

  > We consider an issue to be an “effective false positive” if developers did not take positive action after seeing the issue.

  It continues: an incorrect report that developers fix anyway for readability "is not an effective false
  positive"; an actual fault the developer did not understand and so did not act on "is an effective false
  positive". Pull quote: "Developers, not tool authors, will determine and act on a tool’s perceived
  false-positive rate."
- **Introduction (list of reasons engineers ignore warnings):** "Not integrated", "Not actionable", "Not
  trustworthy. Users do not trust the results due to, say, false positives", "Not manifest in practice",
  "Too expensive to fix", "Warnings not understood".
- **"What We Learned from FindBugs", Attempt 1 (bug dashboard, 2006):** a nightly whole-codebase run with
  a dashboard; "the dashboard saw little use because a bug dashboard was outside the developers’ usual
  workflow, and distinguishing between new and existing static-analysis issues was distracting."
- **Attempt 2 (filing bugs; May 2009 Fixit week):**

  > They reviewed a total of 3,954 such warnings (42% of 9,473 total), but only 16% (640) were actually fixed, despite the fact that 44% of reviewed issues (1,746) resulted in a bug report being filed.

  "Manually triaging issues and filing bug reports is not sustainable at a large scale."
- **Attempt 3 (code-review integration):** FindBugs results posted as review comments; developers "could
  suppress false positives and apply FindBugs’ confidence in the result to filter comments". Discontinued
  in 2011 for two reasons: "the presence of effective false positives caused developers to lose confidence in
  the tool, and developer customization resulted in an inconsistent view of analysis results."
- **"Make It a Compiler Workflow":** the Clang team fixed all existing instances, then enabled the
  diagnostic "as a compiler error (not a warning, which the Clang team found Google developers ignored) to
  break the build, a report difficult to disregard."
- **Patch survey (Error Prone large-scale fixes):** of developers who received a proposed fix to checked-in
  code, "57% ... were happy to have received it, and 41% were neutral. Only 2% responded negatively".
- **"Reporting issues sooner is better":** "survey participants deemed 74% of the issues flagged at compile
  time as “real problems,” compared to 21% of those found in checked-in code"; the authors attribute this to a
  "survivor effect".
- **"Criteria for compiler checks":** a compiler check must "produce no effective false positives (the
  analysis should never stop the build for correct code)" and report correctness rather than style issues.
- **"Warn During Code Review" / "Criteria for code-review checks":**

  > Unlike compile-time checks, analysis results shown during code review are allowed to include up to 10% effective false positives.

  Criteria include "Be actionable and easy to fix" and "Produce less than 10% effective false positives.
  Developers should feel the check is pointing out an actual issue at least 90% of the time". Footnote c on
  the 10% figure:

  > Although this number was initially chosen by the first author somewhat arbitrarily, it seems to be a sweet spot for developer satisfaction and matches the cutoff for similar systems in other companies.

- **Code review as a reporting context:** stylistic and less-important issues reported "at compile-time is
  frustrating for developers"; "at code-review time, developers are preparing their code to be seen; they are
  already in a critical mindset and more receptive to seeing readability and stylistic details." After
  check-in, "lower severity and less-important issues are unlikely to be addressed."
- **"Iterate on feedback from users":** a "Not useful" button files a bug routed to the analyzer's owning
  team; the Tricorder team computes "the ratio of “Please fix” vs. “Not useful” clicks. If the ratio for an
  analyzer goes above 10%, the Tricorder team disables the analyzer until the author(s) improve it." Example:
  a printf-style check drew about one "Not useful" bug per week although "In every case, the analysis was
  correct"; changing the diagnostic text "stopped getting bugs filed about that check." On disabling: "While
  the Tricorder team has rarely had to permanently disable an analyzer, it has disabled an analyzer (on several
  occasions) while the analyzer author is removing and revising subchecks that were particularly noisy."
- **"Provide fixes and involve reviewers":** reviewers can ask for a fix "simply by clicking a “Please fix”
  button on the analysis result. Reviewers typically withhold approval of a change until all their comments,
  manual and automated, have been addressed."
- **"Scale of Tricorder" (as of January 2018):** about 50,000 code review changes analyzed per day;
  "Reviewers clicked “Please Fix” more than 5,000 times per day, and authors applied the automated fixes
  approximately 3,000 times per day. And Tricorder analyzers received “Not useful” clicks 250 times per day."
- **"Expand Analyzer Reach":** customization is allowed only at the project level because user-level
  customization "caused discrepancies within and across teams and resulted in declining use of tools".
  "Gating commits": "Some teams want specific analyzers to actually block commits, rather than just appear in the
  code-review tool. The ability to block commits is commonly requested by teams that have highly specific custom
  checks with no false positives, usually for a custom DSL or library". Code-browsing layers are off by default and let
  specific teams vet higher-noise results "without disrupting other developers".
- **Status as of January 2018:** "there was a compiler warnings-free default for C++ and Java builds at
  Google, with all analysis results either shown as compiler errors or in code review."
- **"Scale of Tricorder" / "Conclusion" (sweet spot):** "The success of code-review analysis suggests it occupies a
  “sweet spot” in the developer workflow at Google." "Code review is a sweet spot for displaying analysis warnings
  before code is committed."
- **"Conclusion" (ratcheting):** "When possible, checks are enabled as compiler errors. To avoid breaking
  builds, tool writers take on the task of first fixing all the existing issues in the codebase, allowing us to
  “ratchet” the quality of Google’s codebase one small step at a time, without regressions."
- **"Lessons" / "Conclusion":** "Most developers will not go out of their way to use static analysis tools";
  Tricorder "presents issues only when a developer is changing the code in question, before the change is
  committed" and "minimizes effective false positives by disabling misbehaving analyses." On warning
  blindness: Google developers "have a strong bias to ignore static analysis, and any false positives or poor
  reporting give them a justification for inaction." There is "typically no mandate from management that
  engineers use static analysis tools."

## Reference-list entries (recorded for acquisition grounding)
- **References, entry 3:** "Ayewah, N. and Pugh, W. The Google FindBugs fixit. In Proceedings of the
  International Symposium on Software Testing and Analysis (Trento, Italy, July 12–16). ACM Press, New York, 2010."
