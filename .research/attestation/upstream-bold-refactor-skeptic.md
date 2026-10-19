---
source_handle: upstream-bold-refactor-skeptic
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/commit/4cb428ae2480c480f5b9da0cab083d424d559117
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects of the same commits via the upstream remote (git show 4cb428ae, 870c8ab9)
---

# Bold-refactor family: open lenses and skeptical review (4cb428ae, 870c8ab9)

## Structure and scope

Commit 4cb428ae (Nathan Klisch, 2026-08-02) changes
`plugins/agile-workflow/skills/bold-refactor/SKILL.md`,
`plugins/code-audit/skills/bold-refactor/SKILL.md` and Workbench's
`skills/ideate/references/provocation.md`. Commit 870c8ab9 (same day) adds
Workbench's provocation reference and a cousin note in code-audit.

## Anchored passages

- Message, 4cb428ae: produced by a "prose-refine cycle (GPT-5.6 Terra +
  GLM-5.2, two rounds, converged on micro-edits)". Two framing changes:
  lens tables "are now explicitly a starting set, not a closed list"; and
  "All provocation/bold-refactor skills now require a fresh-context,
  cross-model skeptical reviewer before proposals reach the human. The
  reviewer defaults to no and checks that proposals are real ..., feasible
  ..., and a net simplification". Verdicts "(kill/narrow/pass with reasons)
  travel with each proposal". "The deprecated workflow plugin's
  bold-refactor is intentionally untouched."
- code-audit `bold-refactor` gains a "Skeptical review" paragraph:
  "preferably a different model class than the one that generated them, or a
  starkly skeptical persona when only one class is available" ... "Generate
  without caution; let the reviewer do the filtering."
- Message, 870c8ab9: Workbench ideate gains the lens table; user guardrail:
  "Provocation applied to an existing, established system always routes
  through deliberate human discussion before becoming work". code-audit
  gains a cousin note so "the relationship is intentional adaptation, not
  drift".
- Neither commit records a use of the skeptic on a real refactor proposal;
  no later upstream commit message in the range mentions "skeptic".
