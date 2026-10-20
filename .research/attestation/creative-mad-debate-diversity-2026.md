---
source_handle: creative-mad-debate-diversity-2026
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2609.00683
provenance: source-direct
substrate_confidence: source-direct
---

# Creative Generation via Multi-Agent Debate: Does Debate Suppress Diversity?

## Source structure and scope
Tien Anh Nguyen, Khanh-Binh Nguyen, Van Dai Do, Svetha Venkatesh, Hung Le; arXiv 2609.00683 v1 (2026-09-01),
listed for EMNLP 2026 main. Abstract and HTML text read via extraction.

## Anchored details
- **Abstract:** multi-agent debate's "convergence-driven design actively suppresses output diversity across independent
  runs"; "preserving diversity among agents within each debate session is a necessary condition for achieving diverse
  outputs across independent runs" (Proposition 1).
- **Measured collapse (Table 2, Qwen3-8B, LiveIdea):** semantic diversity homogeneous MAD 2.47 vs direct single-agent
  2.54; lexical 66.62% vs 68.96%. Control: "Voting achieves diversity comparable to Direct despite applying the same
  judge-based consensus mechanism ... isolating debate dynamics as the primary driver."
- **Mechanisms:** identity drift (identically prompted agents drift toward consensus) and majority pull (full peer
  connectivity lets dominant perspectives override minority views). Heterogeneous model families (Appendix I) still
  showed convergence pressure.
- **Creative-MAD:** each agent anchored to a distinct persistent "cognitive lens"; each agent sees only its most
  semantically distant peers. Gains vs homogeneous MAD: 26.2% semantic and 24.0% lexical diversity (Qwen3-8B), quality
  within ~1–2% of best methods; humans judged Creative-MAD's output set more diverse in 35/40 queries.
- **Benchmarks:** LiveIdeaBench (scientific ideation), argumentative essays, MacGyver, Arena Hard v2.0 creative writing.
- **Limitations:** LLM judges may favour conventionally well-formed outputs; consensus collapses each session to one output.
