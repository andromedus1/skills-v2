---
id: feature-ar-research-rigor-ideas
kind: feature
stage: done
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

## Implementation notes
- Execution capability: one worker; review weight standard (default).
- `adaptive` added as a resolution mode (not a fourth gate set) in ARD SPEC §7,
  CATALOGS table (+ regenerated `catalogs.json` enum), dispatch template,
  orchestrator dials/defaults (omitted rigor → `adaptive`; ask only when the dial
  was omitted and the call is close), refresh re-engagement, README, HANDOFF;
  resolved level and rationale recorded in the engagement record.
- Hybrid stop rule replaces the second-pass rule in the orchestrator (L239–244,
  item-stage rule L378) and `verification-record.md` (outside the listed write
  set, accepted: same rule).
- `.research/CONVENTIONS.md` frontmatter `owner: agentic-research`; convert
  bootstrap writes it; sync declines another provider's tree and reports a
  missing marker as drift (small addition beyond the design).
- Agile Workflow `convert`/`deep-code-scan` do not validate rigor values — no
  patch. Theory positions untouched.
- Verification: conformance 77/77; `gen-contract --check` in sync; AR metadata
  ok; `test_refresh_scan.py` all pass; knowledge-index regen accepts the new
  frontmatter.
- Residue: RP `deep-research/SKILL.md:18` ("propose standard or full only when
  consequence warrants") remains compatible with `adaptive`; left as is.

## Review (2026-10-19)

**Verdict**: Approve (after receiver adjudication; reviewer verdict was Block on an
environment-only verification gap)

**Blockers**: none remaining. Reviewer's only blocker: its sandbox could not run
`skill-metadata.test.sh` (uv cache denied, no PyYAML). Host ran it: agentic-research
skill metadata ok. No implementation change requested.
**Important**: none. **Nits**: none. **Rejected**: none.

**Notes**: standard weight, one independent pass. Reviewer confirmed `adaptive`
resolves consistently to an existing profile, explicit values/hard floor/
cross-specialist `evaluate`/operator authority intact, hybrid stop rule replaces
all second-pass rules, ownership handling coherent, theory positions unchanged;
`gen-contract --check` pass, conformance 77/77, refresh tests 8/8.

**Receipt**
- Reviewed: `e392052f..df9f2356` — agentic-research SPEC, CATALOGS, catalogs.json, dispatch template, orchestrator + references, convert, README, HANDOFF; `.research/CONVENTIONS.md`
- Reviewer: Codex `gpt-6.1-sol` medium via peeragent job `20261019T194925Z-c6cb0ec9`; independent: yes (cross-model; host Claude)
- Weight: standard (source: default)
- Findings: blockers 1 (environmental), important 0, nits 0, rejected 0
- Accepted-fix verification: none required (host ran the blocked test: ok)

**Post-review changes** (`df9f2356..edd9573a`)
- `19c175c8` implement: feature-model-notes — other:feature-model-notes
- `edd9573a` fix: forecast respects autopilot; … — other:feature-overbuild-calibration
