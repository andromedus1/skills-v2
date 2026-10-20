---
source_handle: chao-hill-numbers-rarefaction-2014
fetched: 2026-10-20
source_url: https://www.uvm.edu/~ngotelli/manuscriptpdfs/ChaoHill.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: author-hosted PDF (co-author Gotelli's page), text extracted with pypdf; formulas partly garbled, figures read only via captions
---

# Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies

## Source structure and scope
Anne Chao, Nicholas J. Gotelli, T. C. Hsieh, Elizabeth L. Sander, K. H. Ma, Robert K. Colwell, Aaron
M. Ellison. *Ecological Monographs* 84(1), 2014, pp. 45–67 (as printed on the PDF). Extends
sample-size-based and coverage-based rarefaction/extrapolation from species richness to Hill numbers
of any order q, for abundance and incidence data; simulation tests (Appendix F, not read) and two
empirical examples (spiders, tropical ants). Engagement depth: abstract, introduction, model section,
species-richness extrapolation, coverage subsection, Box 1 heading, Discussion read.

## Anchored details
- **Abstract:** "empirical estimates of Hill numbers, including species richness, tend to be an
  increasing function of sampling effort and, thus, tend to increase with sample completeness."
  "The proposed estimators are accurate for both rarefaction and short-range extrapolation. For
  long-range extrapolation, the performance of the estimators depends on both the value of q and on the
  extrapolation range."
- **Introduction:** observed species richness "is known to be a biased underestimate of true species
  richness"; "from a statistical perspective, species richness is very difficult to estimate accurately
  from a finite sample." Richness also ignores relative abundance ("the abundance problem").
- **Model section (abundance data):** f1 = singletons (species with exactly one individual), f2 =
  doubletons; f0 (unobserved species) is unobservable; multinomial sampling model where detection
  probability equals relative abundance.
- **Species richness extrapolation:** requires an estimated asymptote; Colwell et al. (2012), as
  reported by the authors, "noted that extrapolation gives reliable estimates only up to approximately
  double or triple the reference sample size. This limitation is primarily a consequence of the fact that
  the asymptotic estimator is only a lower bound (Chao 1984)."
- **Tests summary:** rarefaction/extrapolation estimators "match perfectly with the corresponding
  theoretical values for rarefied and extrapolated samples up to double the reference sample size";
  beyond double, performance "depends on extrapolated range and the order q".
- **Sample coverage subsection:** Turing and Good's coverage = "the total relative abundances of the
  observed species"; simple estimator "one minus the proportion of singletons"; Robbins (1968) showed
  its average squared error ≈ 1/n (as attributed). "A tiny percentage of coverage can contain an infinite
  number of rare species. The estimated complement of coverage is not an estimate of the number of
  unseen species, but rather it estimates the proportion of the total individuals in the assemblage that
  belong to undetected species." This "explains why the estimation of species richness in highly diverse
  assemblages is a statistically difficult issue, whereas sample coverage can be accurately estimated."
- **Coverage standardisation:** Alroy (2010) and Jost (2010) proposed standardising samples to common
  completeness; Chao and Jost (2012) derived analytic coverage-based rarefaction/extrapolation and argued
  equal-coverage richness satisfies a "replication principle or doubling property" that equal-size richness
  does not (as summarised by the authors).
- **Discussion:** for q ≥ 1 extrapolation is nearly unbiased "so the extrapolation can be safely extended
  to the asymptote. However, for q = 0, extrapolation is reliable up to no more than double the reference
  sample size", because Chao1/Chao2 "is a lower bound only". Box 1 gives steps for choosing a base sample
  size and a "base coverage" for comparisons. A sample completeness curve "illustrates how much sampling
  effort is needed to achieve a pre-determined level of sample completeness."
