---
source_handle: zhang-qgs-search-2011
fetched: 2026-10-20
source_url: https://www.cse.chalmers.se/~feldt/advice/zhang_2011_optimal_search_for_se_studies.pdf
provenance: source-direct
substrate_confidence: source-direct
source_class: peer-reviewed methods paper (Information and Software Technology 53 (2011) 625-637) with two participant-observer case studies
---

# Identifying relevant studies in software engineering (Zhang, Babar, Tell, 2011)

## Source structure and scope
He Zhang (NICTA/UNSW), Muhammad Ali Babar and Paolo Tell (IT University of Copenhagen).
Proposes a "quasi-gold standard" (QGS) search approach for systematic literature reviews
(SLRs) and evaluates it in two participant-observer case studies that replicated the search
step of two published SLRs. Engagement depth: full text extracted; method (§3), case studies
(§4-5), discussion (§6) and threats (§7) read.

## Anchored details
- **§3.1.1:** most SE SLRs "developed their search strategies subjectively"; even good ones
  tested strings on "'well-known' samples", which "highly depend on reviewers' knowledge" and
  "cannot replace the gold standard". A QGS is "a set of known studies from the related
  venues ... for a given time span" — a gold standard under two added constraints: venues and
  period.
- **§3.1, Fig. 3:** manual search of selected venues builds the QGS; the QGS elicits or tests
  automated search strings; automated search "expands the coverage". Recommended as an
  integration of manual and automated search rather than either alone.
- **§3.2.3:** two ways to build strings — subjective (domain knowledge) then tested against
  the QGS; or objective: word/phrase frequency analysis of title-abstract-keywords of QGS
  papers (e.g. with WordStat) to find terms that distinguish relevant studies; subjective
  judgement still needed to assemble the final string.
- **§3.2.5:** quasi-sensitivity = QGS papers retrieved by the automated search / QGS size.
  Sensitivity is prioritised over precision. Drawing on medical search-strategy scales
  (Table 2: high sensitivity 85-90%, optimum 80-99%, acceptable 72-80%), they "suggest a
  threshold between 70% and 80% (acceptable)". Rule (Eq. 3): if quasi-sensitivity >= 80%,
  merge results with the QGS and stop; else return to string refinement. The threshold should
  consider "diversity of subject, scope of research questions, and the scattering of the
  descriptive keywords" and "may slightly vary from case to case."
- **§4.2.3 Case study 1:** initial automated search retrieved 13/20 QGS papers (65%); missed
  papers were early SLRs that called themselves e.g. "survey"; adding synonyms raised
  quasi-sensitivity to 85% (17/20). Table 5: manual only found 22 SLRs; automated only (without
  evaluation) 28; the systematic combined process 38.
- **§5.2.3-5.3 Case study 2:** the original published SLR's string retrieved about 40% of a
  52-paper QGS; frequency analysis showed some original terms (e.g. "empirical",
  "experiment", "case study") were absent from QGS papers; the revised string reached 73%
  (38/52); further refinement gave "very slim" gains while irrelevant hits rose "dramatically",
  so the student stopped. The original SLR found only 36% (59/164) of the relevant papers the
  replicated process found; one venue (CSCW) contributed 7% of the QGS yet no paper from it
  appeared in the original SLR.
- **§6:** "neither the automated search with intuitive search terms nor the manual search in
  limited number of literature venues could retrieve an 'acceptable' number of relevant papers
  alone"; the approach "provides a mechanism of quantitatively determining when a researcher
  can stop the iterative refinement of search strings". Prior SLR/mapping results can seed a
  QGS.
- **§7 Threats:** cases were not randomly selected; only search/selection were replicated;
  case study 2 was run by a research student who had seen the original SLR. (Implicit in the
  design: quasi-sensitivity measures recall only relative to the QGS venues and period, not the
  full universe.)
