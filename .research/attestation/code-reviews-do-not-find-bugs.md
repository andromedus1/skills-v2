---
source_handle: code-reviews-do-not-find-bugs
fetched: 2026-10-18
source_url: https://www.michaelagreiler.com/wp-content/uploads/2019/02/Code-Reviews-Do-Not-Find-Bugs.-How-the-Current-Code-Review-Best-Practice-Slows-Us-Down.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (2-page talk abstract)"
---

# Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down

## Source structure and scope
Jacek Czerwonka, Michaela Greiler, Jack Tilford (Microsoft Corporation). A two-page industry talk abstract
(it says "With this talk, the attendees from industry receive a detailed experience report"); the fetched PDF,
hosted on a co-author's website, prints no venue or year. The Google case study attributes it to ICSE (SEIP)
2015. It reports Microsoft data summaries without methods detail; figures are stated, not derived in the text.

## Anchored details
- **Abstract:** the authors "posit (1) that code reviews often do not find functionality issues that should block a
  code submission; (2) that effective code reviews should be performed by people with specific set of skills; and (3)
  that the social aspect of code reviews cannot be ignored."
- **Section II, "Discussion":**

  > Only about 15% of comments provided by reviewers indicate a possible defect, much less a blocking defect.

  Feedback on long-term maintainability makes up "at least 50% of all" comments.
- **Section II, reviewer experience:** "Without prior exposure to the part of code base being reviewed, on average only
  33% of any reviewer's comments are deemed useful by the author of a change"; reviewing the same area a third time the
  ratio rises "to about 67%".
- **Section II, size:** usefulness falls as review size grows, noticeably "for reviews with 20 or more changed files."
- **Section II, cost:** developers "spend on average six hours a week reviewing changes of others" (cited to Bosu and
  Carver); median time to all sign-offs "is about 24 hours".
- **Section III, "Conclusions":** "We need to be more sophisticated with our guidelines surrounding the code review
  workflow"; the introduction asks "What is the value of consistency of applying code reviews equally to all code changes?"

## Reference-list entries (recorded for acquisition grounding)
- **Section I, Introduction:** code reviews are used "to find defects, to ensure code's long-term maintainability,
  as a knowledge sharing tool, and to broadcast ongoing progress [3]."
- **References, [3]:** "Alberto Bacchelli and Christian Bird. 2013. Expectations, outcomes, and challenges of
  modern code review. In Proceedings of the 2013 International Conference on Software Engineering (ICSE '13).
  IEEE Press, Piscataway, NJ, USA, 712-721."
