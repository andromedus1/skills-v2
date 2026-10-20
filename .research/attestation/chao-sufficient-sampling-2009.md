---
source_handle: chao-sufficient-sampling-2009
fetched: 2026-10-20
source_url: https://www.uvm.edu/~ngotelli/manuscriptpdfs/ChaoEcology2009.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: co-author-hosted PDF, text extracted with PyMuPDF; tables partly read, simulation figures via captions
---

# Sufficient sampling for asymptotic minimum species richness estimators

## Source structure and scope
Anne Chao, Robert K. Colwell, Chih-Wei Lin, Nicholas J. Gotelli. *Ecology* 90(4), 2009, pp. 1125–1133
(as printed). Derives a nonparametric estimate of the additional sampling effort needed to detect a chosen
fraction (up to 100%) of the Chao1/Chao2 asymptotic richness estimate; evaluated by subsampling two large
inventories and applied to seven published data sets. Engagement depth: abstract, introduction, method
rationale, applications and simulation summary read.

## Anchored details
- **Abstract:** "a substantial fraction of a biota is often represented by species of very low abundance, which
  typically remain undetected"; "richness estimators do not indicate how much sampling effort ... would be
  necessary to reach the asymptote". The method "performs well but is slightly conservative for small sample
  sizes" and is "robust to nonindependence arising from small-scale spatial aggregation". Across seven published
  data sets, additional effort to capture all estimated species ranged "from 1.05 to 10.67 times the original
  sample (median ≈ 2.23)"; to detect 90% of species, "0.33–1.10 times the original effort; median ≈ 0.80".
- **Introduction:** three estimation families — fitting a statistical abundance distribution (e.g. lognormal
  "veil line"), extrapolating an accumulation curve to its asymptote (e.g. Michaelis–Menten), and nonparametric
  estimators based on frequencies of rare species.
- **Method rationale:** "The Chao1 estimator represents a universal lower bound in the sense that it is valid under
  all types of species abundance distribution. Thus, all estimated sampling effort derived in this paper represents
  minimum effort." If f2 = 0, use S_obs + f1(f1−1)/[2(f2+1)].
- **Heuristic stopping rule:** "Sampling will be complete when every species is represented by at least two
  individuals (no singletons)"; operationalised as estimated undetected species f̂0 < 0.5. "this may require a very
  large additional sample size, because by the time the total sampling effort is extensive enough to reveal two
  individuals of each species found only once in the original sample, single individuals of additional species will
  have inevitably surfaced. For hyperdiverse communities with a large proportion of very rare species, the challenge
  of estimating richness from sample data is daunting."
- **Good–Turing attribution:** per Good (1953, 2000), Turing studied the problem while deciphering intercepted German
  messages (as attributed by the authors).
- **Applications caveat:** pooled data sets "contain a large number of singletons, and it is possible that some of this
  rarity reflects the pooling of heterogeneous samples". Ant example: 18 plots, 33 species, 8 uniques, 5 duplicates →
  estimated 39 species, needing about 62 more plots.
