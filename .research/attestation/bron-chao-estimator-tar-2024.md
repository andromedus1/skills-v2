---
source_handle: bron-chao-estimator-tar-2024
fetched: 2026-10-20
source_url: https://arxiv.org/pdf/2404.01176
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: arXiv PDF, text extracted with pypdf (some figure content skipped), read locally
---

# Using Chao's Estimator as a Stopping Criterion for Technology-Assisted Review

## Source structure and scope
Bron MP, van der Heijden PGM, Feelders AJ, Siebes APJM (Utrecht University). arXiv 2404.01176,
dated 2024-03-30; 35 pages. Proposes an ensemble active-learning strategy plus a stopping
criterion from Chao's population size estimator (PSE), evaluated by simulation on several
datasets. Engagement depth: full text (taxonomy section 2.1, method section 3, model
assumptions 3.2.2, results excerpts, discussion, conclusion).

## Anchored details
- **Taxonomy (2.1):** "Heuristic" rules decide from observed patterns and "do not have a formal
  statistical grounding" so "do not offer strong guarantees besides the results of the
  criterion on known datasets"; "Certification rules provide a formal statistical guarantee".
- **Pragmatic rules (2.1.1):** stopping after k consecutive irrelevant documents (k = 50 or 200)
  "often results in low recall or little work savings" and "frequently fails to meet the widely
  used recall target of 95%" (citing Callaghan and Müller-Hansen 2020).
- **Target and Knee methods (2.1.3-2.1.4), attributed to Cormack and Grossman 2016:** the Target
  method randomly samples until k relevant documents (recommended k = 10) are found, then stops
  when all k are rediscovered by the separate TAR run; it "guarantees a recall of at least 70%".
  The Knee method stops at an inflection in the recall curve (slope ratio).
- **PSE for search (3.1.1):** describes Webster and Kemp (2013) - "multiple reviewers conduct
  independent searches" and overlaps are linked to estimate omissions.
- **Ensemble design (3.1):** because classic PSE needs multiple human reviewers, an ensemble of
  differently-trained classifiers acts as independent "committee members".
- **Chao estimator (3.2):** uses only f1 (documents found once) and f2 (found twice): if many are
  seen once relative to twice, "probably there are a lot more that you have missed completely".
- **Assumptions (3.2.2):** heterogeneity model Mh (capture probability varies across items);
  counts treated as zero-truncated Poisson; "contagion" (capture changes later capture
  probability) "violates the Poisson assumption"; independence argued from committee members
  searching independently. "Accounting for the heterogeneity, Chao's estimator provides a lower
  bound on the number of relevant documents."
- **Results excerpts:** "all Optimistic criteria" (point-estimate based) "tend to underestimate
  the number of relevant documents"; at the 100% target the Chao (1987) criterion is triggered
  99.37% of the time vs 55.93% for AUTOSTOP; the method "does not achieve its recall target as
  often as AUTOSTOP" for high targets; a CMH variant "underestimates the recall for a long time".
- **Conclusion:** the estimators "work well" in simulation; "further research ... will improve
  the reliability and applicability".
