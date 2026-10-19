---
source_handle: google-modern-code-review
fetched: 2026-10-18
source_url: https://storage.googleapis.com/gweb-research2023-media/pubtools/4476.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: full PDF text except page 5, which yielded no extractable text (so the opening of section 5 is unread)"
---

# Modern Code Review: A Case Study at Google

## Source structure and scope
Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko (Google, Inc.) and Alberto Bacchelli
(University of Zurich). The PDF's ACM reference format reads "2018. Modern Code Review: A Case Study at
Google. In Proceedings of 40th International Conference on Software Engineering: Software Engineering
in Practice Track" (SEIP). Exploratory mixed-methods study: 12 interviews, a survey with 44 respondents,
and analysis of review logs for 9 million reviewed changes. Describes Google's documented review process
(ownership and readability approvals) and measured log statistics.

## Anchored details
- **"Code Review Flow" paragraph, step 5 "Approving"** (precedes section 5.2; its enclosing heading is on unread page 5):

  > To eventually commit a change, a developer typically must have approval from at least one reviewer. Usually, only one reviewer is required to satisfy the aforementioned requirements of ownership and readability.

- **"Code Review Flow" paragraph (quantifying lightweight-ness):** one iteration is "one instance of the author resolving some
  comments"; "We find that over 80% of all changes involve at most one iteration of resolving comments."
- **"Suggesting Reviewers" paragraph (precedes section 5.2):** "often only one reviewer is required since changes are often authored by
  someone with ownership and/or readability for the files in question."
- **Section 5.2, "Quantifying The Review Process", "Number of reviewers and comments":** "fewer than 25% of changes have more than one reviewer, [footnote marker omitted] and
  over 99% have at most five reviewers with a median reviewer count of 1. Larger changes tend to have more reviewers
  on average." In contrast to Rigby and Bird's report, "At Google, the situation is different: A greater number of
  reviewers results in a greater average number of comments on a change."
- **Section 5.2, "Finding 4":** "one reviewer is often deemed as sufficient, compared to two in the other projects."
- **Section 4.1, "How it All Started" (interviews):** "although it is great if reviewers find bugs, the foremost reason for
  introducing code review at Google was to improve code understandability and" (the sentence continues on page 5,
  which did not extract; its continuation is unread).
- **Section 7.1, "A Truly Lightweight Process":** the authors "posit that having one reviewer helps make reviews fast and lightweight",
  and note low reviewer counts "can also result from small changes".
- **References:** cites Czerwonka, Greiler and Tilford, "Code Reviews Do Not Find Bugs: How the Current Code Review
  Best Practice Slows Us Down", ICSE (SEIP) 2015, as reference [14].
- The paper does not report defect-detection outcomes by reviewer count; reviewer-count statistics are descriptive.
