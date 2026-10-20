---
source_handle: fu-absencebench-omission-2025
fetched: 2026-10-20
source_url: https://arxiv.org/pdf/2506.11440
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: arXiv PDF v1 (13 Jun 2025) text extracted with pypdf; appendices skimmed, figures read via captions
---

# AbsenceBench: Language Models Can't Tell What's Missing

## Source structure and scope
Harvey Yiyun Fu, Aryan Shrivastava, Jared Moore, Peter West, Chenhao Tan, Ari Holtzman (University of
Chicago; Stanford). arXiv 2506.11440v1, 13 June 2025, marked "Preprint. Under review." (search results
indicate later acceptance to the NeurIPS 2025 Datasets and Benchmarks track under the title "Absence
Bench: Language Models Can't See What's Missing"; not verified from the fetched PDF). Benchmark of 14
LLMs asked to list deliberately removed elements given both original and edited documents. Engagement
depth: abstract, §1, results table, §4 analyses excerpts, §7 limitations.

## Anchored details
- **Abstract:** "while models excel at recalling surprising information, they still struggle to identify
  clearly omitted information." Three domains: numerical sequences, poetry, GitHub pull requests. "even
  state-of-the-art models like Claude-3.7-Sonnet achieve only 69.6% F1-score with a modest average context
  length of 5K tokens." Proposed cause: "Transformer attention mechanisms cannot easily attend to 'gaps' in
  documents since these absences don't correspond to any specific keys that can be attended to."
- **§1 findings:** inference-time compute boosts performance "by only 7.9% at the cost of generating an
  average of extra 8K thinking tokens"; "Counter-intuitively, a lower rate of omission in the task set-up
  leads to worse model performance"; compared with needle-in-a-haystack, "a massive 56.9% drop in F1-score
  on average"; inserting placeholder strings where content was omitted "boosts the performance by a dramatic
  35.7% on average".
- **§1 implication posed by authors:** "if LLMs cannot properly notice when information is missing, can we
  rely on LLM-as-a-Judge?"
- **Table 3 (micro F1, %):** GitHub PRs hardest — best 40.0 (Claude-3.7-Sonnet with thinking); averages
  range from 71.2 (Gemini-2.5-flash thinking) to 14.7 (Mixtral-8x7B). Exact-match scoring per element plus
  micro-F1, so copying the whole original is penalised as false positives.
- **§4 omission rate:** "models actually perform worse when required to recall fewer lines" — authors
  hypothesise sparse omissions break generation continuity.
- **§7 limitations:** "Surface-form omission only" — does "not capture more subtle or semantic notions of
  absence—such as omitted reasoning steps or missing evidence"; the side-by-side format "may overestimate how
  well models would perform under more realistic situations"; "if a new generation of models solve
  AbsenceBench, that will not be sufficient evidence to say that models can handle omission elegantly";
  other domains/longer contexts expected "to be more difficult, not less".
