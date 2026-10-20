---
source_handle: luminate-design-space-generation-2023
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2310.12953
provenance: source-direct
substrate_confidence: source-direct
---

# Luminate: Structured Generation and Exploration of Design Space with Large Language Models for Human-AI Co-Creation

## Source structure and scope
Sangho Suh, Meng Chen, Bryan Min, Toby Jia-Jun Li, Haijun Xia; arXiv 2310.12953 v3 (2024-03-13), HCI
systems paper. Abstract and HTML full text read via extraction.

## Anchored details
- **Abstract, motivation:** current interaction paradigms guide "users towards rapid convergence on a limited
  set of ideas, rather than empowering them to explore the vast latent design space".
- **Pipeline (Figure 4):** (1) LLM generates the key categorical dimensions (nominal and ordinal; numerical
  excluded) and their values as JSON; (2) the system "randomly selects a value for each dimension to create a
  requirement" and prompts the LLM to write a response meeting it; (3) abstraction layers (title, keywords,
  summary). Study configuration: up to 5 nominal dimensions with up to 8 labels, up to 3 ordinal dimensions with
  5 levels, 40 responses per prompt.
- **Evaluation:** user study with 14 professional writers — qualitative interviews/think-aloud, Creativity
  Support Index 82.16; dimensions rated accurate by most (4 strongly agree, 6 agree, 3 neutral, 1 disagree).
  No quantitative measure of output diversity or coverage and no independent technical evaluation of dimension
  quality was reported.
- **Limitations:** "dimensional reasoning does not happen naturally and that even experts can have difficulties
  answering the dimensions that characterize the problem space"; 40 responses felt overwhelming to some.
