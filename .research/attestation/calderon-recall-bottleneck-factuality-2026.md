---
source_handle: calderon-recall-bottleneck-factuality-2026
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2602.14080
provenance: source-direct
substrate_confidence: source-direct
---

# Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality

## Source structure and scope
Nitay Calderon, Eyal Ben-David, Zorik Gekhman, Eran Ofek, Gal Yona; arXiv 2602.14080 v2 (2026-06-19), preprint.
Abstract and HTML text read via extraction.

## Anchored details
- **Framework:** each fact profiled as encoded or not, and if encoded as directly recalled, recalled only with
  thinking, or not recalled; WikiProfile benchmark; 4 million responses from 13 LLMs.
- **Abstract:** frontier models encode 95–98% of benchmark facts but "recall remains a major bottleneck"; recall
  failures "disproportionately affect long-tail facts and reverse questions".
- **Long tail (Gemini-3-Pro):** encoding popular vs rare 99.5% vs 94.5%, but recall 84.6% vs 63.3% (delta 21.3).
- **Thinking:** "recovers 40–65% of encoded but not directly known facts" in thinking-optimized LLMs but "only 5–20%
  of non-encoded facts"; for rare facts thinking improves recall by 20.1 points vs 11.3 for popular facts.
- **Generation vs verification:** reverse questions are harder in generation (GPT-5 82.9% vs 74%) but "in
  verification, reverse questions are no harder than direct ones".
- **Limitation:** scoped to Wikipedia single-hop facts.
