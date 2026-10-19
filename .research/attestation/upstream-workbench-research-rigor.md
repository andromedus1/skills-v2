---
source_handle: upstream-workbench-research-rigor
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/plugins/workbench/skills/research/references/verification-rigor.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects via the upstream remote (verification-rigor.md, 52 lines, read in full; research/SKILL.md lines 1-80; 60c6390d diff of .research/CONVENTIONS.md)
---

# Workbench research verification rigor and provider ownership

## Anchored passages

- "Verification rigor controls which semantic checks a completed research
  brief must pass. It does not control source count, investigation breadth,
  research duration, or agent fan-out."
- Resolution: "explicit user instruction, then `.research/CONVENTIONS.md`,
  then `adaptive`"; "`adaptive` selects the lowest level that credibly fits
  the decision's relevance, consequence, uncertainty, novelty, source
  disagreement, synthesis complexity, and corpus breadth. Do not use fixed
  source-count or agent-count thresholds."
- Floor: grounding discipline, "deterministic lint and index checks", lead
  spot-check of "each load-bearing conclusion". Standard: "one semantic
  source-support pass"; "when the lead performs the pass inline, disclose
  that it was not independent". Full: "an isolated evaluator"; "If no
  isolated evaluator is available, do not claim the full gate passed".
- Convergence: "Stop after the same failure recurs twice without material
  progress and surface the blocker instead of looping." Principles "are
  never source evidence".
- research/SKILL.md: "If `.research/CONVENTIONS.md` exists, it must declare
  `owner: workbench-research`; otherwise defer to the named provider and do
  not interpret, lint, index, or modify its substrate." "Do not expose
  separate quick, deep, or program workflows to the user."
- Upstream `.research/CONVENTIONS.md` (60c6390d) gains frontmatter
  `owner: workbench-research`, `schema: 1`, `verification_rigor: adaptive`;
  attestations "ground fetched external sources, not repository files or
  credentialed references".
