---
source_handle: deng-brucks-toubia-llm-idea-diversity-barriers-2026
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2602.20408
provenance: source-direct
substrate_confidence: source-direct
---

# Examining and Addressing Barriers to Diversity in LLM-Generated Ideas

## Source structure and scope
Authors as given in the text: Deng, Brucks and Toubia; arXiv 2602.20408 v1 (2026-02-23), preprint. HTML full text
(arxiv.org/html/2602.20408v1) read via extraction.

## Anchored details
- **Abstract:** two mechanisms — "at the individual level, LLMs exhibit fixation just as humans do, where early
  outputs constrain subsequent ideation"; "at the collective level, LLMs aggregate knowledge into a unified
  distribution rather than exhibiting the knowledge partitioning inherent to human populations". CoT "reduces
  fixation ... (only in LLMs, not humans)"; "ordinary personas (versus 'creative entrepreneurs' such as Steve Jobs)
  improve knowledge partitioning by serving as diverse sampling cues"; "Combining both approaches produces the
  highest idea diversity, outperforming humans."
- **Design:** GPT-4o (2024-11-20); fitness-product ideation; 10 ideas per participant/session; 83–99 per condition.
- **Measures:** ideas coded on three explicit dimensions — industry context (9 categories), psychological need (9),
  product form (10); T_cat = unique categories (max 28), T_comb = unique category combinations (max 810), d = mean
  pairwise number of differing dimensions (max 3); supporting embedding analysis (text-embedding-3-small).
- **Study 1:** within-session exploration nearly identical for humans and LLM (12.68 vs 12.46 categories, p = .45);
  across independent first ideas, humans T_cat 14.51 / T_comb 9.17 / d 2.41 vs LLM 8.37 / 5.88 / 1.51 (p < .001).
- **Study 2:** seeding LLM sessions with human first ideas "does not improve downstream idea diversity at all".
- **Study 3 (bootstrap 10 x 10):** human T_comb 59.66; LLM default 39.15; ordinary personas 56.97; creative
  entrepreneurs 50.40 (ordinary > entrepreneur, p < .001). Ordinary personas raise between-participant embedding
  variation to 0.635 vs default 0.241 (human 0.545) but increase within-session fixation (slope 0.876 vs 1.013).
- **Study 4 (aggregate 830 ideas each):** T_comb human 197; LLM default 83; LLM + CoT 152; LLM persona 193;
  LLM persona + CoT 248. CoT raises LLM T_comb 39.15 to 55.49 (bootstrap) but does not recover between-participant
  partitioning (embedding 0.318); CoT has no fixation effect in humans.
- **Temperature:** "A higher temperature brings only slight improvement in idea diversity while often producing
  nonsensical answers".
- **Limitations:** single domain, single model, idea quality not systematically measured, diversity measure depends on
  the chosen categorization scheme, human-CoT procedure differs from LLM-CoT.
