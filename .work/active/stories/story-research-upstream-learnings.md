---
id: story-research-upstream-learnings
kind: story
stage: implementing
tags: [research]
parent: feature-upstream-learnings-2026-10
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
research_dials:
  scope_authority: mixed
  verification_rigor: floor
  intent: map-landscape
  output_kind: landscape-brief
---

# Scout: what changed upstream since 2026-08-01 and what could transfer

## Commission

Breadth survey (research-pipeline `scout` intent) of `nklisch/skills`
`upstream/main` (`638867b6`) against this fork since merge base `43f7f4bf`, plus
`nklisch/peeragent` 0.8.1 → 0.8.3 (latest release 2026-10-11). Sources are
first-party: `git log`/`git diff 43f7f4bf..upstream/main -- plugins/<name>` in
this repo, upstream `.work/` items and docs at `upstream/main`, and the public
peeragent repository/releases.

For each area, describe the upstream change in its own terms (what, why — from
commit messages, items and docs — and evidence of use), then map it to this fork:
already have / conflicts with fork policy / could adopt / could adapt / not
relevant, with the files a change would touch and who owns them (upstream-owned
plugin vs fork-owned `research-pipeline`/`agentic-research`). Areas:
agile-workflow (10 commits), code-audit (5), ux-ui-design (3; large removal),
prose-craft (9), new plugins sol-calibration and declaudify, single-commit
touches (agentic-research, agent-coordination, nates-toolkit, workflow), peeragent,
and **Workbench as an ideas pass only** (159 commits): map themes and process
ideas that could transfer to agile-workflow/research-pipeline, never as a
migration target, no per-commit analysis. Seek evidence against adopting as well
as for.

Consumer: Andrew via `feature-upstream-learnings-2026-10` decision packet.
Decision relevance: which upstream changes to adopt, adapt or skip. Dials set
with Andrew 2026-10-19: mixed scope, **floor** rigor. Per ARD SPEC §3.1/§7, if
the engagement fans out to several specialists, the isolated `evaluate` gate
re-enters the floor for the cross-specialist synthesis.

## Full registration

```yaml
intent: map-landscape
output_kind: landscape-brief
consumer: methodology-revisers
verification_rigor: floor
temporal_contract: write-once-on-converge
```
