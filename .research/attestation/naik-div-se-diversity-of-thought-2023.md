---
source_handle: naik-div-se-diversity-of-thought-2023
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2310.07088
provenance: source-direct
substrate_confidence: source-direct
---

# Diversity of Thought Improves Reasoning Abilities of LLMs

## Source structure and scope
Ranjita Naik, Varun Chandrasekaran, Mert Yuksekgonul, Hamid Palangi, Besmira Nushi; arXiv 2310.07088 v2
(2024-02-23). Abstract and HTML text read via extraction.

## Anchored details
- **Abstract:** existing ensembling "assume[s] that the input prompt is fixed and expect[s] the decoding
  strategies to introduce the diversity"; proposes soliciting the LLM "to ideate approaches that are apt
  for the problem" and ensembling diverse prompts (DIV-SE across calls; IDIV-SE within one call).
- **Approach elicitation:** model asked to name b in [1,5] approaches per call, repeated c = 100 times; the n
  most frequent approaches (n in {3,5}) kept; personas likewise solicited from the model; persona-approach
  combinations chosen greedily on a small held-out validation set.
- **Rationale:** "stochasticity-based methods do not directly guide the diversity at the level of thought or
  method, but rather at the token level ... linguistic token diversity does not always ensure diverse and
  independent solution approaches."
- **Results:** Blocksworld planning +29.6 points; graph coloring 97% vs 15% baseline; AQuA-RAT +16.52
  (GPT-3.5 zero-shot); GSM8K +10.39; better accuracy-cost frontier than self-consistency with temperature
  sampling (Figure 1).
- **Limits:** gains negligible for LLaMA-2 70B zero-shot; small GPT-3.5 planning gains; "instruction following
  capabilities are crucial"; within-call error propagation 5.5–6.2%.
- Note: selecting approaches by frequency keeps the most commonly proposed approaches; evaluation is accuracy on
  tasks with a correct answer, not coverage of an approach space.
