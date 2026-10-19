---
source_handle: review-measures-defects-replication
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2005.09217
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, section 1, section 3 conclusions 1-2 and review-measure results, section 4 conclusions 3-4, related work on Porter, section 6.1"
---

# Do Code Review Measures Explain the Incidence of Post-Release Defects? Case Study Replications and Bayesian Networks

## Source structure and scope
Andrey Krutauz (Concordia University), Tapajit Dey (University of Tennessee), Peter C. Rigby (Concordia
University), Audris Mockus (University of Tennessee). arXiv 2005.09217 v1, 19 May 2020 (cs.SE); the PDF is a
journal-template manuscript ("Noname manuscript No."), venue not printed. A replication of McIntosh et al.
on the original Qt data plus a differentiated-external replication on Google Chrome, then Bayesian Network
models. The authors state they discussed findings with McIntosh.

## Anchored details
- **Abstract, results:**

  > Both the data from the original study and the Chrome data showed high instability of the influence of code review measures on defects with the results being highly sensitive to variable selection procedure. Models without code review predictors had as good or better fit than those with review predictors.

  Replication "confirms with the bulk of prior work showing that prior defects, module size, and authorship have
  the strongest relationship to post-release defects"; review predictors "do not affect post-release defects
  directly and showed indirect effects".
- **Section 3.4, "Conclusion 1":** "The review measures contributed little to the performance of the model, with the
  R2 remaining almost unchanged from the model that included only the traditional predictors". The text reports that
  McIntosh "stated that he did not believe that review measures could dominate traditional measures."
- **Section 3.5, review measures:** in Qt, measures are "similar to what McIntosh et al. found"; "The self-approved
  changes has low impact on post-release defects"; "For the Chrome dataset the review measures are not statistically
  significant in most cases."
- **Section 4, "Conclusion 3":** "Only prior defects, module size, and minor authors have direct effects on (form a
  Markov blanket for) post-release defects in the combined model".
- **Section 4 (BN discussion):** prior defects relate to "the typical number of reviewers"; the authors suggest "modules
  with prior defects probably invite more scrutiny with a larger review team" (reverse-causation reading).
- **Section 6.1:** "having 5 or more reviewers is seen to increase chance of having post-release defects from 20% to 33%
  through mediating variables allauthors and minorauthors"; "Although individual code reviews find defects, we were unable
  to find any direct effect of review measures on post-release defects."
- **Related work:** attributes to Porter et al. that "the best predictor was the level of expertise of the reviewers.
  Varying the processes had a negligible impact on the number of defects found."
- **Section 5.1, "External validity":** "clearly our results do not generalize beyond these two projects" (Qt and Chrome).
