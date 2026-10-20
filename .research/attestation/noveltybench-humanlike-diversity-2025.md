---
source_handle: noveltybench-humanlike-diversity-2025
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2504.05228
provenance: source-direct
substrate_confidence: source-direct
---

# NoveltyBench: Evaluating Language Models for Humanlike Diversity

## Source structure and scope
Yiming Zhang, Harshita Diddee, Susan Holm, Hanchen Liu, Xinyue Liu, Vinay Samuel, Barry Wang, Daphne Ippolito;
arXiv 2504.05228 v4 (2025-08-09). Abstract and HTML full text read via extraction.

## Anchored details
- **Distinct metric:** generations partitioned into equivalence classes by a fine-tuned DeBERTa classifier
  (1,000 annotated pairs; 79% accuracy, F1 0.811) rather than embedding/n-gram distance, which may
  "overemphasize trivial differences (e.g., paraphrasing)". Two generations count as different if "a user who has
  seen one generation would likely benefit from seeing the other". distinct_k counts classes among k samples.
- **Utility metric:** combines novelty and quality (Skywork reward model) with patience p = 0.8, k = 10.
- **Results (distinct out of 10):** Claude 3.5 Sonnet 1.76; GPT-4o 2.88; Gemini 2.0 Pro 2.25; Gemma 2-2B 5.66;
  Llama 3.2-1B 6.74. Abstract: "larger models within a family often exhibit less diversity than their smaller
  counterparts"; current systems generate "significantly less diversity than human writers".
- **Prompting strategies (NB-Curated):** resampling, paraphrased prompts, a system prompt to give each user a
  novel answer, and in-context regeneration (show previous outputs, ask for a different one). In-context
  regeneration was most effective, matching or exceeding human diversity for the three tested models — "LLMs can
  indeed generate diverse answers when explicitly constrained by their previous outputs in context".
- **Alignment:** across OLMo 2 post-training stages "each alignment stage progressively reduces model diversity",
  with significant drops at DPO.
- **Limitation:** does not settle whether users want diversity in every context.
