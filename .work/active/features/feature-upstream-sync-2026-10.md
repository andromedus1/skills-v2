---
id: feature-upstream-sync-2026-10
kind: feature
stage: review
tags: [upstream, agile-workflow, ux-ui-design]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Sync upstream-owned plugins to nklisch/skills 638867b6

## Brief

Bring agile-workflow (0.16.16), ux-ui-design (1.0.0, breaking), prose-craft, code-audit, Workbench (tree only, stays disabled) and small manifest touches up to upstream; update research-pipeline feature/epic-design and any other fork callers to the ux-ui concierge; preserve documented fork patches (models.md, bump-version guard and test); skip upstream's Workbench-only bump test group and Antigravity manifests; correct the catalog's peeragent description and update Claude's peeragent install to 0.8.3. Smoke-check UI triggers on both hosts. Decided by Andrew 2026-10-19 — see `feature-upstream-learnings-2026-10`,
"Operator decisions"; research: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.

## Simplification opportunity

ux-ui-design 1.0.0 removes ~10k lines of pipeline skills; drop fork callers to retired skills rather than shimming them.

## Design decisions
All directional choices were made by Andrew (see Brief). Method follows the
August baseline sync (`8d8a41ff`): merge `upstream/main` pinned at `638867b6` to
preserve ancestry, then resolve by ownership. Trial merge: 13 conflicted paths
(`.knowledge/index.json`, `.research/CONVENTIONS.md`, `.work/CONVENTIONS.md`,
7 upstream `.work/backlog` items, `AGENTS.md`, `README.md`,
`plugins/agile-workflow/scripts/tests/bump-version.test.sh`).

## Architectural choice
Merge (A) vs path-by-path checkout without ancestry (B) vs cherry-picking
per plugin (C). A keeps future syncs cheap (merge base advances) and matches the
previous sync; B/C lose ancestry and repeat this work next time. Choose **A**.

## Resolution rules (implementation units)

### Unit 1 — merge and ownership resolution
- **Ours (fork-owned / fork state):** `.work/**`, `.research/**`, `.knowledge/**`,
  `AGENTS.md`, `README.md`, `docs/project-navigation.md`,
  `plugins/research-pipeline/**`, `plugins/agentic-research/**`. Upstream
  `.work/` items are not imported.
- **Theirs (upstream-owned trees, byte-identical to `638867b6`):**
  `plugins/{agile-workflow,ux-ui-design,prose-craft,code-audit,workbench,nates-toolkit,agent-coordination,workflow}/**`,
  except documented fork patches: `agile-workflow/skills/principles/references/models.md`
  (re-apply fork additions onto upstream's file) and
  `agile-workflow/scripts/tests/bump-version.test.sh` (upstream's file plus our
  named-branch seed and refuse-on-main case; drop upstream's Workbench-only group
  9 only if it conflicts with the guard, otherwise keep it).
- **Declined:** delete `plugins/sol-calibration/`, `plugins/declaudify/` and every
  root Antigravity `plugins/*/plugin.json` the merge adds; remove their and
  `theatre-feedback` catalog entries; drop Antigravity handling from
  `scripts/bump-version.sh` if upstream added it.
- **Catalogs** (`.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`):
  keep the fork identity and research-pipeline/agentic-research entries; take
  upstream's entries/descriptions for synced plugins; peeragent description
  "peer and peer-review" → "peer".
- **`scripts/bump-version.sh`:** keep the fork guard; accept upstream's other
  changes that apply to retained channels.
- **Root `docs/`** upstream foundation docs: take upstream (they are retained
  upstream context); fork process docs stay ours.

### Unit 2 — fork callers of retired ux-ui-design skills
`plugins/research-pipeline/skills/{feature-design,epic-design}/SKILL.md` (and any
other fork-owned caller found by `rg 'ux-ui-design:(palette|screens|flows|components|motion|adopt)'`):
mirror upstream's agile-workflow caller changes — offer the `/ux-ui-design:ux-ui`
concierge instead of `:palette`/`:screens`/`:flows`.

### Unit 3 — verification
- No conflict markers; `git diff upstream/main -- plugins/<upstream-owned>` shows
  only the documented fork patches.
- `rg` finds no fork-owned call to retired ux-ui-design skills.
- Catalog/manifest JSON valid; Claude/Codex manifest version parity per plugin.
- Tests: bump-version, RP portability, AR metadata, resolver, ARD conformance,
  `python3 scripts/check-workbench-sync.py` if applicable.
- After merge to main: update installs (Claude: agile-workflow, ux-ui-design,
  peeragent 0.8.3; Codex: agile-workflow, ux-ui-design) and smoke-check that the
  `ux-ui` concierge is discoverable on both hosts.

## Risks
- **ux-ui-design 1.0.0 trigger regression** (upstream's named top risk) —
  smoke-check discovery on both hosts after install.
- **Hidden fork patches lost** in upstream-owned trees — diff against
  `upstream/main` must show only the two documented patches.
- **Workbench re-enabled accidentally** — `.claude/settings.json` keeps it false.

## Implementation notes
- Execution capability: one worker for the merge and caller updates; host for
  doc follow-ups. Review weight: standard (default).
- Commits: merge `422de5eb` (parents `41954477`, `638867b6`); callers `af5505c2`;
  docs follow-up (fork-patch documentation, PRINCIPLES frontmatter, ux-ui guide
  summary).
- Resolution: fork kept `.work/`, `.research/`, `.knowledge/`, AGENTS.md, README,
  CONVENTIONS, research-pipeline, agentic-research, `scripts/bump-version.sh`;
  upstream-owned trees equal `638867b6` except documented patches; declined
  sol-calibration, declaudify, theatre-feedback, Antigravity root manifests and
  `.agents/plugins.json`; upstream `.work/` additions not imported; upstream root
  docs taken with fork knowledge-index frontmatter; `.work/bin/work-view` refreshed
  to 0.16.16 via `install-work-view.sh`.
- Discrepancies from design: kept `plugins/workbench/plugin.json` (Workbench's
  validator, tests and CI read it; no Antigravity catalog exists); kept three
  undocumented macOS test fixes in agile-workflow (now documented as fork patches);
  skipped upstream's Workbench-only bump test group 9 and its version-stamping in
  `bump-version.sh` (operator decision).
- Callers: RP feature-design Phase 4.6 renamed "alignment" (reuse epic/.mockups
  mocks; offer `/ux-ui-design:ux-ui` only when uncovered); RP epic-design uses
  upstream's concierge-offer paragraph.
- Known residue: `docs/SPEC.md` (upstream text, titled as upstream context) still
  lists sol-calibration.

## Integrated verification (2026-10-19)
No conflict markers; no fork-owned calls to retired ux skills; all catalogs and
manifests parse with Claude/Codex parity; bump-version 70/70; RP portability ok;
AR metadata ok; resolver ok; ARD conformance 77/77; agile-workflow tests
agent-metadata 11, convert-content-integrity 42, convert-install-routing 12,
convert-review-weight 13, install-work-view 47, work-board-shim 16,
work-view-dist-version 16, hooks unittest OK; Workbench unittest 84 OK;
`work-view-fallback-readiness.test.sh` fails on macOS bash 3.2 identically before
the merge (pre-existing); knowledge index regenerated (24 docs, no warnings).
Owed after merge: install updates and `ux-ui` discovery smoke on both hosts.
