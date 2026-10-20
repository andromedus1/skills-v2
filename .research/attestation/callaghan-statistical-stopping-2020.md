---
source_handle: callaghan-statistical-stopping-2020
fetched: 2026-10-20
source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7700715/fullTextXML
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: Europe PMC full-text XML, tag-stripped and read locally (cross-checked with PMC page via WebFetch)
---

# Statistical stopping criteria for automated screening in systematic reviews

## Source structure and scope
Callaghan MW, Müller-Hansen F. Systematic Reviews 2020; 9: 273 (DOI 10.1186/s13643-020-01521-4,
PMC7700715). Proposes and evaluates a hypothesis-test stopping criterion for active-learning
(ML-prioritised) screening on 21 datasets (284-8,911 documents; relevant proportion 0.01-0.35).
Engagement depth: full text.

## Anchored details
- **Criterion:** after prioritised screening, sample remaining unseen documents (randomly, or
  "ranked quasi-sampling") and test the null hypothesis that recall is below a target
  (e.g. 95%) using the hypergeometric distribution; supports statements like "We reject the null
  hypothesis that we achieve a recall of less than 95% with a significance level of 5%".
- **Why heuristics fail:** "Recall is not simply a function of the proportion of unseen documents
  that are relevant, but also of the number of unseen documents." "Even a perfect estimator of
  the proportion of unseen documents that are relevant is insufficient on its own to provide
  sufficient information about when to stop screening."
- **Baseline inclusion rate (BIR) method:** fails to account for sampling uncertainty; in a
  worked scenario 48% of cases achieve <95% recall. Empirically BIR "misses the 95% recall target
  in 39.67% of cases, while the most common work saving is 0%."
- **Consecutive-irrelevant heuristic (IH50):** "mean work saved for IH50 is 41%, the target is
  missed in 39% of cases."
- **Proposed criterion:** ranked quasi-sampling missed the target in 0.95% of runs with mean 17%
  work saved; random sampling missed in 3.29% with 15% saved. Abstract: "work reductions of on
  average 17%".
- **Requirement stated:** for live reviews "the reliability of and ease of communication about
  recall are paramount, and the results must be independent of model performance"; with this
  criterion a poor model only lowers work saved rather than recall.
- **Limitations:** multiple testing not addressed formally; ranked quasi-sampling assumes ML-chosen
  documents are not less likely to be relevant than random ones.
