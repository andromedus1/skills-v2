---
source_handle: kirk-rlhf-generalisation-diversity-2023
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2310.06452
provenance: source-direct
substrate_confidence: source-direct
---

# Understanding the Effects of RLHF on LLM Generalisation and Diversity

## Source structure and scope
Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward
Grefenstette, Roberta Raileanu; arXiv 2310.06452 v3 (2024-02-19). Abstract and HTML text on
diversity metrics/results read via extraction.

## Anchored details
- **Abstract:** studies SFT, reward modelling and RL stages on summarization and instruction following
  with two base models; "RLHF generalises better than SFT to new inputs" but "substantially diminishes
  output diversity compared to SFT", described as a generalization-diversity tradeoff.
- **Metrics:** expectation-adjusted distinct n-grams (EAD), Sentence-BERT embedding cosine diversity,
  NLI diversity (more contradictions, fewer entailments = more diverse).
- **Per-input vs across-input diversity:** per-input = diversity of outputs for one input; across-input
  = diversity of outputs across inputs. RLHF had "much lower output diversity than SFT" per-input;
  across-input differences were smaller but persisted — described as "the first rigorous empirical
  demonstration of across-input mode collapse emerging from RLHF training specifically".
