---
source_handle: review-coverage-participation-defects
fetched: 2026-10-18
source_url: https://rebels.cs.uwaterloo.ca/papers/msr2014_mcintosh.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, introduction (RQ summaries), metric definitions (Table 2), RQ1 and RQ2 results text; regression tables skimmed"
---

# The Impact of Code Review Coverage and Code Review Participation on Software Quality: A Case Study of the Qt, VTK, and ITK Projects

## Source structure and scope
Shane McIntosh (Queen's University), Yasutaka Kamei (Kyushu University), Bram Adams (Polytechnique
Montréal), Ahmed E. Hassan (Queen's University). ACM notice on the PDF: "MSR '14, May 31 - June 1, 2014,
Hyderabad, India". Author-hosted PDF. Observational case study: regression models of post-release defect
counts per component in Qt, VTK and ITK releases (Gerrit-based review), controlling for size, complexity,
churn, prior defects and ownership-type metrics.

## Anchored details
- **Abstract:** "Low code review coverage and participation are estimated to produce components with up to two
  and five additional post-release defects respectively."
- **Section 1, RQ1 summary:**

  > Review coverage is negatively associated with the incidence of post-release defects in all of our models. However, it only provides significant explanatory power to two of the four studied releases, suggesting that review coverage alone does not guarantee a low incidence rate of post-release defects.

- **Section 1, RQ2 summary:** "components with lax code review participation will contain up to five additional
  post-release defects."
- **Table 2, participation metrics:** "Proportion of self-approved changes" is "The proportion of changes to a
  component that are only approved for integration by the original author", with the rationale that such changes
  "have essentially not been reviewed." Hastily reviewed changes use a threshold drawn from the best-practice rate
  of "200 lines per hour".
- **RQ2 results:** "the proportion of changes without discussion has a statistically significant impact on the
  models of all three of the studied releases"; self-approval is significant in the Qt 5.0.0 model and hasty review
  in the Qt 5.1.0 model; "components that integrate more insufficiently discussed, hastily reviewed, and/or
  self-approved patches tend to be more defect-prone."
- The design is correlational (defect models on observational data); it does not randomize review.
