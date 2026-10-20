---
id: feature-agentic-research-pilot-fixes
kind: feature
stage: drafting
tags: [agentic-research]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Agentic Research: fixes from the methodology-review pilot

## Brief

This feature fixes the `agentic-research` defects found during the project-blueprint
Knowledge pilot of `research-pipeline:methodology-review`. The full findings are in
`feature-methodology-review-pilot-learnings` under "Pilot findings". Andrew split
this work out on 2026-10-20 (that item's design decision 5): it changes a separate
plugin and ships in its own PR. `feature-methodology-review-pilot-learnings`
depends on this feature, because F21 and F27 affect the gates of the strategy
research that feature commissions.

Findings in scope:

- **F21 (M). Rigor table vs `evaluate` reachability.** The research-orchestrator
  rigor table shows `evaluate` only at `full`. The reachability rule says
  `evaluate` re-enters the floor of any cross-specialist synthesis. A host that
  followed the table skipped `evaluate` and closed early. Make the table and the
  rule agree.
- **F27 (M). Bare citations pass lint silently.** `lint-citations.py` reported
  "0 resolved · 0 broken" for a brief with 207 bare `{N}` citations, which looks
  clean but checked nothing. Flag bare numeric citations, or resolve them
  through `references.md`.
- **F16. Short-handle citations.** One specialist cited short handles and
  produced 160 broken chains. The specialist role brief should state the
  full-handle citation form.
- **F17. Lint depends on the working directory.** Lint resolves `source_path`
  relative to the working directory, so running it from `.research/` gives false
  `unreachable-source` findings.
- **F8. No concurrency rule for the bibliography.** Parallel specialists share
  one append-only numbered `references.md`. The pilot host reserved number
  blocks and merged per-specialist refs files afterwards. Specify one rule.
- **F15. Discipline inlining is costly.** The verbatim discipline bundle plus
  role brief was inlined into 9 dispatches. Consider a read-the-file handshake
  with a content-hash echo, keeping the same discipline guarantees.
- **F24. No option to delegate a single facet.** The light path (one facet)
  requires the host to author inline. Add a "single delegated specialist"
  option: the same discipline inlining and gates, no cross-synthesis, so
  `evaluate` stays unreachable.

Surfaces involved: `skills/research-orchestrator/` (SKILL.md and references),
`skills/research-discipline/`, and `ard-core/kernel/lint-citations.py` with its
conformance fixtures. Validate both the Claude and Codex plugin shapes. Bumping
agentic-research needs the "Build research-view binaries" workflow.

## Simplification opportunity

- F15 may replace repeated verbatim inlining with one file reference plus a hash
  echo.
- F21 should resolve to a single source of truth for reachability, rather than a
  table and a rule that can drift apart.
- Retain every ARD invariant: the anti-fabrication floor, the verification stack
  and the FR.1 evaluator isolation.
