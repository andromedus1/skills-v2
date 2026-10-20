---
source_handle: schmitz-rahmann-richness-estimation-review-2025
fetched: 2026-10-20
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11986355/
provenance: source-direct
substrate_confidence: snippet
source_class: peer-reviewed review and benchmark (Briefings in Bioinformatics, 2025; DOI 10.1093/bib/bbaf158 as shown on the PMC page)
extraction_pipeline: PMC article page fetched through a model-mediated extractor (direct HTTP fetch was blocked); abstract recovered in full, body findings only as quoted excerpts; tables and figures not read
---

# A comprehensive review and evaluation of species richness estimation

## Source structure and scope
Johanna Elena Schmitz and Sven Rahmann. *Briefings in Bioinformatics*, 2025, DOI 10.1093/bib/bbaf158 (as
shown on the PMC page). Review plus benchmark of richness estimators on simulated data with different mixes of
rare and abundant species and on downsampled real data (immune repertoires, microbiome, global reef fish).
Engagement depth: abstract in full; selected result sentences via extractor; tables/figures not read.

## Anchored details
- **Abstract:** "Accurately estimating the true richness from very small samples is challenging, in particular for highly
  diverse populations with many rare species." Methods "incorporate explicit or implicit assumptions about either the
  species distribution or about the sampling process" and "are scattered across the literature".
- **Abstract, main finding:** "depending on species composition, different methods provide the most accurate richness
  estimates. Simple methods based on the observed number of singletons yield accurate asymptotic lower bounds for several
  of the tested simulated species compositions, but tend to underestimate the true richness for heterogeneous populations
  and small samples containing 1% to 5% of the population."
- **Abstract, extrapolation:** "When the population size is known, upsampling (extrapolating) estimators such as PreSeq and
  RichnEst yield accurate estimates of the total species richness in a sample that is up to 10 times larger than the
  observed sample."
- **Body excerpts (via extractor):** Chao1 and ACE, "often referred to as a lower bounds, yield accurate lower bounds close
  to the true species richness for most species compositions"; breakaway estimators "both over- and underestimate the true
  richness and have large estimation intervals for repeated samples"; Good–Turing and jackknife-type estimators are reported
  as failing "if singletons or doubletons are zero" (extractor-reported; not verified against the article text).
