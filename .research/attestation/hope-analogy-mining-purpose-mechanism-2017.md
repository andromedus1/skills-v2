---
source_handle: hope-analogy-mining-purpose-mechanism-2017
fetched: 2026-10-20
source_url: https://arxiv.org/abs/1706.05585
provenance: source-direct
substrate_confidence: source-direct
source_class: peer-reviewed conference paper with retrieval evaluation and controlled ideation experiment (KDD '17, Halifax; DOI 10.1145/3097983.3098038 read off the PDF)
---

# Accelerating Innovation Through Analogy Mining (Hope, Chan, Kittur & Shahaf)

## Source structure and scope
Tom Hope (Hebrew University), Joel Chan (CMU), Aniket Kittur (CMU), Dafna Shahaf (Hebrew University). KDD '17.
arXiv 1706.05585 PDF, 9 pages. Read: abstract, §1, §4 (inspiration generation, experiment design, results),
§5 discussion.

## Anchored details
- **Abstract:** finding analogies in "large, messy, real-world repositories remains a persistent challenge";
  information-retrieval similarity metrics "struggle to account for structural similarity, which is central to
  analogy"; learns "problem schemas", which "specify the purpose of a product and the mechanisms by which it
  achieves that purpose", via crowdsourcing plus RNNs; "higher precision and recall than traditional
  information-retrieval methods"; in an ideation experiment retrieved analogies "significantly increased people's
  likelihood of generating creative ideas compared to analogies retrieved by traditional methods."
- **§1:** "In humans, memory retrieval is highly sensitive to surface similarity, favoring near, within-domain
  analogs that share object attributes over far, structurally similar analogs that share object relations";
  analogical processing "incurs a heavy cognitive load". Baselines: TF-IDF, LSA, LDA, GloVe; corpus of Quirky
  product descriptions.
- **§4.1 retrieval move:** find pairs with "high (near purpose)" purpose similarity and "low (far mechanism)"
  mechanism similarity; cluster by purpose, then diversify by mechanism using a MAX-MIN dispersion selection
  (greedy GMM) "to avoid displaying too-similar results".
- **§4.2:** 38 Amazon Mechanical Turk workers, product-redesign task, 12 seed products, within-subjects;
  conditions: ANALOGY (near-purpose far-mechanism, diversified), SURFACE (TF-IDF top-12, "meant to simulate current
  search engines"), RANDOM (12 random products).
- **§4.3:** "good" idea = different mechanism (novelty) + same purpose (quality) + implementable (feasibility); five
  graduate-student judges, Fleiss κ = 0.51. 749 ideas. For k = 2 on seeds in all conditions: good-idea proportion
  46% analogy vs 37% random vs 30% TF-IDF (p ≤ .01); k = 3: 38% vs 22% vs 21%. Mixed model: pr(good) 0.71
  [0.48, 0.87] vs TF-IDF 0.28 and random 0.27 (k = 2). "confidence intervals ... are relatively wide";
  replications "could yield results somewhere in between".
- **§5:** benefit attributed to sampling "diverse yet still structurally similar inspirations"; "The TF-IDF approach
  yielded inspirations likely to be relevant, but also likely to be redundant and homogeneous, while the random
  sampling approach yields diversity but not relevance." Limits: vectors do not distinguish higher/lower-level or
  core/peripheral purposes and mechanisms; generalising to complex data such as scientific papers may need
  hierarchical representations.
