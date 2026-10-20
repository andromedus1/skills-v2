---
source_handle: chao-colwell-chao2-inequality-2017
fetched: 2026-10-20
source_url: https://gwern.net/doc/statistics/order/capture/2017-chao.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: PDF (third-party mirror of the journal article) text extracted with pypdf; equations partly garbled in extraction, figures not read
---

# Thirty years of progeny from Chao's inequality: Estimating and comparing richness with incidence data and incomplete sampling

## Source structure and scope
Anne Chao and Robert K. Colwell. *Statistics & Operations Research Transactions* (SORT) 41(1),
January–June 2017, pp. 3–54 (as printed on the PDF). Invited review of Chao's (1987) inequality and
the Chao2 incidence-based richness estimator, with Good–Turing justification, sampling-effort
prediction, a class of higher-order lower bounds (iChao2), sample-size-based and coverage-based
rarefaction/extrapolation, and a worked bird example run through SpadeR / iNEXT / PhD. Engagement
depth: full text read for sections 1–3, 7.3–7.5, 8; sections 4–6 (sampling without replacement,
shared species, phylogenetic diversity) skimmed.

## Anchored details
- **Abstract / §1:** Chao (1987) derived "an inequality among capture frequency counts to obtain a
  lower bound" for population size; applied to species incidence data, "the number of undetected
  species can be inferred from the species incidence frequency counts of the uniques (species
  detected in only one sampling unit) and duplicates (species detected in exactly two sampling units)."
  Colwell and Coddington (1994) named "Chao1" (abundance data) and "Chao2" (incidence data).
- **§1:** of the many more sophisticated estimators (ACE/ICE coverage estimators, martingale,
  estimating-function, quasi-likelihood, Horvitz–Thompson types), "Surprisingly, it turns out that the
  earliest and simplest estimators are the most useful ones for biological applications."
- **§1, data types:** distinguishes individual-based abundance data from multiple sampling-unit
  incidence data; incidence data are preferable where individuals are hard to define or count, and
  "replicated incidence records account for spatial (or temporal) heterogeneity".
- **§2.1 model:** each species i has a detection probability πi per sampling unit; incidence entries
  are Bernoulli; Q_k = number of species detected in exactly k of T sampling units; Q0 (undetected)
  is unobservable.
- **§2.2, Eq. 2b (Chao2):** S_obs + ((T−1)/T)·Q1²/(2Q2) if Q2 > 0; S_obs + ((T−1)/T)·Q1(Q1−1)/2 if
  Q2 = 0 (bias-corrected form). "The estimated number of undetected species is based exclusively on the
  information on the least frequent species"; frequent species "carry negligible information about the
  undetected species".
- **§2.2, equality condition:** the Cauchy–Schwarz inequality is an equality "if and only if the species
  detection probabilities are homogeneous" — "a very restrictive condition, one that is almost never
  satisfied"; relaxed condition: "very rare/infrequent species have approximately the same detection
  probabilities, and frequent species are allowed to be highly heterogeneous".
- **§2.2 / Eq. 3c:** if Q1 = 0, Chao2 = S_obs ("sampling is complete"); the estimate's distribution is
  right-skewed, so a log-transformed 95% CI is used whose lower limit is never below S_obs.
- **§2.2, mixture models:** the inequality also holds under binomial-mixture (beta-binomial, negative
  binomial) models describing spatially clustered or temporally aggregated incidence, so "even though
  there is spatial/temporal heterogeneity pattern for species incidences, the lower bound and the
  associated estimation are still valid."
- **§2.3, Good–Turing:** Good–Turing frequency formula originated in Turing and Good's WWII
  cryptanalysis to estimate frequencies of rare (including undetected) code elements; Good (1953) and
  Good and Toulmin (1956) published it (as attributed by the authors). From the Good–Turing view,
  Chao2 "is a nearly unbiased point estimator if all undetected and unique species in samples have the
  same mean detection probabilities".
- **§2.4, effort to completion:** Chao2 "does not indicate how much sampling effort ... would be
  necessary"; Chao et al. (2009) stopping rule: predict additional units t until the expected number of
  uniques in the enlarged sample is < 0.5 (Eq. 6a), and m_g units to reach a fraction g of the Chao2
  estimate (Eq. 6c).
- **§2.5:** higher-order counts (Q3, Q4) give an improved lower bound iChao2 (Chiu et al. 2014, Eq. 6d)
  and a series of lower bounds (Puig and Kokonendji 2017).
- **§3 opening:** "when rare/infrequent species are highly heterogeneous and sample size is not
  sufficiently large, the Chao2 formula can provide only a lower bound, which cannot be compared
  accurately across assemblages". Chao and Jost (2012), as summarised by the authors: equal-size samples
  may compare "a nearly complete sample to a very incomplete one", so differences "will generally be
  underestimated".
- **§3.1:** rarefaction (interpolation) estimator is unbiased (Shinozaki 1963); for short-range
  extrapolation, Ŝ(T + t*) ≈ S_obs + (Q1/T)·t*, "very robust and reliable even though the species
  richness estimator is subject to bias"; "Previous experiences by Colwell et al. (2012) suggested that
  the prediction size can be extrapolated at most to double the observed sample size."
- **§3.2, sample coverage:** Turing and Good's concept of "sample coverage" — for incidence data, "the
  fraction of the total incidence probabilities in the assemblage (including undetected species) that is
  represented by species detected in the reference sample"; estimator Ĉ(T) = 1 − (Q1/U)·[(T−1)Q1 /
  ((T−1)Q1 + 2Q2)] (Eq. 7d), with U the total incidences; modified form when Q2 = 0 (Eq. 7e). A
  "sample completeness curve" shows coverage vs sample size and estimates the size needed for a fixed
  completeness.
- **§7.3 sampling design:** "We treat each point-count as a sampling unit. There were 12 point counts
  conducted along the Barrington Tops Forest Road in the northern part of the national park" (North Site);
  17 point counts formed the South Site reference sample. The North Site frequency table reports
  Sobs = 27, T = 12, U = 102, sample coverage estimate 91.8%. (Added 2026-10-20 on re-read of the fetched
  PDF, extending the substrate for a cited specific.)
- **§7.3 worked example (Australian birds, point counts):** North Site Q1 = 9, Q2 = 4 → Chao2 = 36.3,
  95% CI (29.1, 68.8); South Site Q1 = 12, Q2 = 8 → 46.5, CI (40.3, 69.8); iChao2 38.6 and 48.2.
  Coverage-based comparison: richness difference significant only for coverage up to about 93%.
  "Unlike the sample-sized-based standardization, in which sample size is determined by investigators,
  the coverage-based standardization compares equal population fractions of each assemblage."
- **§8:** "if very rare/infrequent species are heterogeneous and the sample size is not sufficiently
  large, then the data do not contain sufficient information to accurately estimate species richness,
  and the Chao2 formula provides a universal nonparametric lower bound." Where rare species are highly
  heterogeneous (e.g. microbial / DNA-sequencing data), "all estimators derived in this paper
  underestimate the true diversities and can be regarded only as lower bounds"; non-asymptotic
  rarefaction/extrapolation then recommended. Hill numbers (q = 0 richness, q = 1 Shannon, q = 2
  Simpson) also depend on sample size and completeness and need standardization.
