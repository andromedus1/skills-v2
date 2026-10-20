---
source_handle: liang-multi-agent-debate-divergent-2023
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2305.19118
provenance: source-direct
substrate_confidence: source-direct
---

# Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate

## Source structure and scope
Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu;
arXiv 2305.19118 v4 (2024-10-09); EMNLP 2024. Abstract and HTML text read via extraction.

## Anchored details
- **Degeneration-of-Thought (DoT):** "Once the LLM-based agent has established confidence in its answers, it is
  unable to generate novel thoughts later through self-reflection even if the initial stance is incorrect."
  Self-reflection disagreement drops sharply after the first iteration (Figure 1).
- **MAD design:** two debaters argue in "tit for tat" fashion; a judge decides when to stop and extracts the answer.
- **Results:** counter-intuitive arithmetic, GPT-3.5-Turbo + MAD 37.0% vs self-reflect 27.5% and CoT 28.0%;
  commonsense MT gains over self-reflection.
- **Disagreement level:** forcing disagreement on every point underperforms; moderate disagreement is best.
- **Judge bias:** "LLM may not act as an impartial judge when different LLMs are used as debaters."
- **Scope:** tasks have correct answers (translation, arithmetic); not an ideation-coverage evaluation.
