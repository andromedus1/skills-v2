---
source_handle: meincke-prompting-idea-variance-2024
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2402.01727
provenance: source-direct
substrate_confidence: source-direct
---

# Prompting Diverse Ideas: Increasing AI Idea Variance

## Source structure and scope
Lennart Meincke, Ethan Mollick, Christian Terwiesch; Wharton School working paper dated
January 27, 2024, posted to arXiv (2402.01727) and SSRN. Not peer-reviewed at fetch. Full PDF
text read (pages 1–15: introduction, hypotheses, strategies, methodology, results, exhaustion,
limitations, conclusion). Appendices not audited.

## Anchored details
- **p.2, research question:** "How might one choose prompts in LLMs to increase the diversity of
  an AI generated pool of ideas?" Outcome metrics: cosine similarity of the idea pool, total number
  of unique ideas a prompt can find, and speed at which generation is exhausted "and ideas start
  repeating themselves (see Kornish and Ulrich 2011)".
- **p.2/p.4–5, framing:** idea generation framed as exploring a rugged solution landscape; "a broad
  exploration of different regions of the solution landscape is called for"; success "is measured
  by the value of the most valuable idea that was generated".
- **p.5–6, design:** domain = new consumer product for US college students, under USD 50. 35 prompting
  strategies in 8 groups (idea-prompted, HBR brainstorming article, Stanford design-thinking article,
  "special techniques" such as tipping/emotional pleas/threats, persona modifiers e.g. Steve Jobs,
  "creative entrepreneur", hybrid brainstorming of 40 sessions x 30 ideas teamed into groups that pick
  top 10, telling the model cosine-similarity information, and Chain-of-Thought). 10 sessions x 100
  ideas per strategy (1000 ideas). Human baseline: 100 ideas aggregated from separate Wharton MBA
  students — authors note this aggregation "gives an edge to the human innovators".
- **p.6–7, measures:** cosine similarity on Google Universal Sentence Encoder embeddings (p.9);
  similarity >= 0.8 treated as an identical idea, "established by testing". Authors caution that
  changing the embedding model "could yield dramatically different results" and that cosine
  similarity "might not capture all the dimensions of idea similarity that a human might consider".
- **p.8, unique-idea estimate:** following Kornish & Ulrich, a "Mark and recapture"-style estimate of
  the total number of unique ideas (T) from the total generated (N) and the unique count (U); authors
  stress "we cannot estimate the total number of ideas in a space, but only the possible number of
  unique ideas that can be found with a particular technique".
- **p.8–9, setup:** gpt4-0314, temperature 0.7, top-p 1.0, no frequency/presence penalties. Exhaustion
  runs used gpt4-1106-preview in 30-idea increments with full history (~1200 ideas, 5 runs).
- **p.11, Table 2 (mean within-pool cosine similarity, lower = more diverse):** group of students 0.243;
  Chain of Thought (gpt4-1106-preview) 0.255; Creative Entrepreneur 0.348; Steve Jobs 0.368; Base
  Prompt 0.377; Harvard Business Review article 0.387; Stanford Design Thinking article 0.392; Hybrid
  Brainstorming 0.393; Previous Top Ideas 0.403; Cosine Information 0.432 (the worst).
- **p.3, p.9:** "prompt crafting does not always have a significant effect on the outcome"; results
  "should hence not be interpreted as a blanket endorsement of one strategy".
- **p.12, CoT prompt:** first list 100 short titles; second, check whether ideas are "different and
  bold" and modify them to be bolder and more different ("No two ideas should be the same"); then
  write descriptions. ~15% of runs where the model skipped step two were removed from aggregation.
- **p.12–13, exhaustion:** CoT's similarity advantage over the base prompt is strongest at 100–500
  ideas and becomes negligible after ~750–800 ideas ("the strategy starts to deplete the pool").
  Estimated unique-idea space: base prompt ~3700 (13.8% repetitive), CoT ~4700 (11.7%).
- **p.13–14, between-pool overlap:** overlap between ideas from different strategies (first 50 ideas
  each) is small; authors suggest "the hybrid practice of running multiple strategies and combining
  their ideas is a good option".
- **p.15, limitations:** link between cosine similarity and human-scored similarity unestablished;
  limited samples per prompt; "Diversity can be obtained by sacrificing idea quality" and diversity is
  treated as the end goal; findings "might be GPT-4 specific" and other domains may reorder strategies.
