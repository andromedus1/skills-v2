---
id: feature-ar-research-rigor-ideas
kind: feature
stage: implementing
tags: [agentic-research]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Agentic Research rigor ideas from upstream Workbench research

## Brief

In fork-owned agentic-research, evaluate and adapt: an 'adaptive' verification-rigor option, an owner: field in .research/CONVENTIONS.md, and 'stop after the same failure twice' for correction loops. Keep ARD's floor and gate catalog intact; closed enums change only with conformance and doc updates. Decided by Andrew 2026-10-19 — see `feature-upstream-learnings-2026-10`,
"Operator decisions"; research: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.

## Simplification opportunity

An adaptive option may replace manual rigor selection at kickoff.

## Design decisions (Andrew, 2026-10-19)
- **Adopt `adaptive`** as a `verification_rigor` value: the orchestrator selects the
  lowest level that credibly fits the decision's consequence, uncertainty,
  novelty, source disagreement, synthesis complexity and breadth (no fixed
  source/agent-count thresholds), states the resolved level and why in the
  engagement record and report, and asks only when no default is set and the call
  is genuinely close. Explicit `floor`/`standard`/`full` win. Hard-floor and
  reachability rules (e.g. `evaluate` for cross-specialist synthesis) still apply
  to the resolved level.
- **Owner marker:** `.research/CONVENTIONS.md` declares `owner: agentic-research`;
  the convert scaffold writes it for new trees.
- **Hybrid stop rule:** after an accepted finding, revise and rerun deterministic
  checks plus only the affected semantic gate and scope; surface to the user when
  the same failure recurs twice without material progress, or when a revision
  introduces new material errors a second time. Replaces "a second-pass
  NEEDS-REVISION is surfaced".

## Implementation Units
1. ARD contract: `ard-core/SPEC.md` (§ dials / §7 rigor profiles: add `adaptive` as
   a resolution mode over the existing profiles, not a new gate set),
   `ard-core/CATALOGS.md` if it enumerates the values, then
   `tools/gen-contract.py` + `--check`; `kernel/templates/dispatch.md`.
2. Orchestrator: `skills/research-orchestrator/SKILL.md` (dials table, defaults,
   kickoff, verification depth, revision rule, research_dials reading),
   `references/refresh-reengagement.md`, README, `docs/HANDOFF.md`.
3. Ownership: `.research/CONVENTIONS.md` gains frontmatter/line `owner:
   agentic-research`; `agentic-research:convert` scaffold writes it.
4. Upstream-owned readers (`agile-workflow` convert, deep-code-scan): if they
   validate rigor values, add `adaptive` as a documented fork patch; otherwise
   leave untouched.
**Acceptance**: [ ] every fork-owned enum site lists `adaptive` consistently;
[ ] the orchestrator states the resolved level; [ ] hybrid stop rule replaces the
old sentence everywhere it appears; [ ] conformance 77/77, `gen-contract --check`,
AR skill metadata, refresh tests pass; [ ] historical theory positions untouched.
