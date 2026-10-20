---
source_handle: artificial-hivemind-homogeneity-2025
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2510.22954
provenance: source-direct
substrate_confidence: source-direct
---

# Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)

## Source structure and scope
Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten
Sap, Alon Albalak, Yejin Choi; arXiv 2510.22954 v2 (2026-10-06); NeurIPS 2025 Datasets & Benchmarks
(oral). Abstract and HTML full text read via extraction.

## Anchored details
- **Dataset:** Infinity-Chat, 26K real-world open-ended queries with no single ground truth; taxonomy of
  6 top-level categories (including brainstorm & ideation) and 17 subcategories.
- **Measurement:** OpenAI text-embedding-3-small pairwise similarity; 50 responses per query on
  Infinity-Chat100; 70+ models (25 detailed). Decoding top-p 0.9, temperature 1.0; alternative min-p 0.1,
  temperature 2.0.
- **Intra-model repetition:** "In 79% of cases, the average similarity exceeds 0.8"; under min-p decoding
  "81% of response pairs still exceed 0.7 similarity and 61.2% exceed 0.8".
- **Inter-model homogeneity:** average pairwise similarity between different models' responses "ranges
  from 71% to 82%"; ~8 unique models per top-50 cluster.
- **Example:** "Write a metaphor about time" responses cluster around "time is a river" and a smaller
  "time is a weaver" cluster.
- **Mitigation:** min-p reduces extreme repetition but substantial similarity persists ("mode collapse even
  under diversity-oriented decoding"); "model ensembles may not yield true diversity when their
  constituents share overlapping alignment and training priors".
- **Judges:** 31,250 human annotations (25 per example); correlations between human ratings and LMs,
  reward models and LM judges "drop significantly on similar-quality subsets".
- **Limitations:** English-only snapshot of queries; embedding similarity "may lack sufficient
  expressiveness"; mechanism of homogenization not established.
