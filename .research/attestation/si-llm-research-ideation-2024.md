---
source_handle: si-llm-research-ideation-2024
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2409.04109
provenance: source-direct
substrate_confidence: source-direct
---

# Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

## Source structure and scope
Chenglei Si, Diyi Yang, Tatsunori Hashimoto; arXiv 2409.04109 v1 (2024-09-06). Abstract plus HTML
§7.1–7.2 read via extraction; the human-study sections were engaged at abstract depth only.

## Anchored details
- **Abstract:** 100+ NLP researchers wrote ideas and blind reviews; LLM-generated ideas "are judged as more
  novel (p < 0.05) than human expert ideas while being judged slightly weaker on feasibility"; open
  problems include "failures of LLM self-evaluation and their lack of diversity in generation".
- **§7.1 LLMs lack diversity:** the agent generated 4000 seed ideas per topic; dedup with all-MiniLM-L6-v2
  cosine similarity threshold 0.8 "based on manual inspection"; "out of the 4000 generated seed ideas,
  there are only 200 non-duplicate unique ideas"; per Figure 4 the share of non-duplicates in each new
  batch keeps decreasing and accumulated non-duplicates plateau. "This sets a bottleneck on our
  inference-time scaling since increasing the number of generated ideas simply leads to repeating
  duplicate ideas."
- **§7.2 LLMs cannot evaluate ideas reliably:** best LLM pairwise ranker (Claude-3.5) 53.3% agreement with
  human reviewers versus human inter-reviewer 56.1%; other LLM judges lower.
