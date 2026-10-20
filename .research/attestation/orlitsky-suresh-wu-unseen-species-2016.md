---
source_handle: orlitsky-suresh-wu-unseen-species-2016
fetched: 2026-10-20
source_url: https://arxiv.org/pdf/1511.07428
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: arXiv PDF v3 (3 Mar 2016) text extracted with pypdf; proofs skimmed, figures not read
---

# Estimating the number of unseen species: A bird in the hand is worth log n in the bush

## Source structure and scope
Alon Orlitsky, Ananda Theertha Suresh (UCSD), Yihong Wu (UIUC). arXiv 1511.07428v3, dated March 4,
2016 on the title page. (A PNAS 2016 version titled "Optimal prediction of the number of unseen species"
is indicated by search results; the fetched text is the arXiv version.) Theoretical statistics paper on
how far beyond the observed sample the number of new species can be predicted, with experiments on
synthetic and real data. Engagement depth: abstract, §1–2 (results), §4.3 excerpt, §8 experiments read;
proofs not audited.

## Anchored details
- **Abstract:** Fisher's formulation "uses n samples to predict the number U of hitherto unseen species
  that would be observed if t·n new samples were collected." Good and Toulmin's estimator "predicts U for
  all t ≤ 1, thereby showing that the number of species can be estimated for a population twice as large as
  that observed"; Efron and Thisted's modification "empirically predicts U even for some t > 1, but without
  provable guarantees". The authors' smoothed estimators "provably predict U ... all the way up to t
  proportional to log n", and "this range is the best possible". Guarantees "hold uniformly for all
  distributions" across multinomial, Poisson, hypergeometric and Bernoulli-product sampling models.
- **§1 applications:** species estimation used for ecological diversity, "vocabulary size [Efron–Thisted
  1976; Thisted–Efron 1987], database attribute variation, and password innovation", bacterial/microbial
  diversity, immune receptor diversity, unseen genetic variation (as cited).
- **§1, Corbet/Fisher example:** Corbet's Malayan butterfly table (118 species seen once, 74 twice, ...);
  Good–Toulmin estimate for an equal further sample: 118 − 74 + 44 − 24 + ... = 75 new species. For t > 1
  the plain Good–Toulmin estimator "grows super-linearly in t" and "does not approximate U at all"
  (Zipf simulation, Fig. 1).
- **§2.2, Theorem 2 / Corollary 1:** a matching minimax lower bound — no estimator can do better than
  order n^(−c'/t) normalised error; "Theorems 1 and 2 determine the limit of predictability up to a constant
  multiple."
- **§4.3, support size vs unseen-in-future:** "without any assumption on the distribution it is impossible to
  estimate the support size. For example, regardless how many samples are collected, there could be
  infinitely many symbols with arbitrarily small probabilities that will never be observed." Support-size
  estimation needs an assumed minimum symbol probability 1/k; predicting new species in a future sample
  needs no such assumption because "if there exist a large number of very improbable symbols, most likely
  they will not appear in the new samples anyway."
- **§8 experiments:** Hamlet (31,999 words, 4,804 distinct): "as little as 20% of the data already yields an
  accurate estimate of the total number of distinct words" with the new estimator; similar on human-skin
  bacterial OTUs (1,221 clones, 182 species-level units) and a subsample of US Census surnames.
