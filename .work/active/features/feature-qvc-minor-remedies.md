---
id: feature-qvc-minor-remedies
kind: feature
stage: review
tags: [methodology-review, research-pipeline, cleanup]
parent: null
depends_on: [feature-qvc-review-receipts]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# QVC minor remedies: citation gate, doc-review, consolidation, hygiene

## Brief

Fork-only bundle of minor QVC findings accepted by Andrew on 2026-10-19 — see
`feature-claude-methodology-repeat`, "Operator decisions — round 1 packet".
Depends on `feature-qvc-review-receipts` because consolidation touches the same
review-reuse text.

1. **Citation gate tidy-up** (QVC-S/METH-002, QVC-S/METH-003, gate-citations
   incidentals): run the gate with `--exit-code-on` matching its blocking
   policy while keeping the JSON-validity check; one reporting line for
   `campaign_unbound` and `substrate_confidence_omitted` counts (warn-only, no
   items); fix status lists, example paths and the version-advisory caveat.
   The canonical kernel stays unchanged.
2. **doc-review state and scope** (QVC-E/METH-003, QVC-E/METH-004): add
   baseline, iteration and capped fields to its report; limit autonomous fixes
   to mechanical classes and route foundation-doc contradictions to the
   operator; retarget checks that assume the retired roadmap pattern.
3. **Consolidate duplicate rules** (QVC-E/METH-002, QVC-R/METH-004): one
   canonical fork statement of the completion-evidence and review-reuse rules
   with one-line local pointers; drop `research-composition` restatements; weigh
   choices by burden on domain methodology reviews (operator criterion).
4. **Repo hygiene** (QVC incidentals): declare PyYAML for tests; branch guard
   in `bump-version.sh`; fix stale "Cross-Model Advisory Review policy" and
   `peer-review` references in RP feature/epic-design; document the
   `models.md` fork patch in `docs/project-navigation.md`.

Out of scope: matcher changes (QVC-S/METH-001 awaits its experiment), upstream
agile-workflow edits, and new review passes.

## Simplification opportunity

Item 3 is itself a simplification; prefer deleting restatements over rewording them.

## Design decisions

- **doc-review retarget (Andrew, 2026-10-19): full retarget to `.work`.** Andrew:
  "i don't think our current workflow creates roadmap phases, right? which would
  support the second option". Verified: `epicize` emits epics instead of a
  roadmap and `expand` seeds epics "instead of roadmap phases". Roadmap-phase,
  blocking-brief and DONE-phase checks are replaced by `.work`-aware checks; a
  legacy roadmap file is reviewed as an ordinary foundation doc.
- **bump-version guard (Andrew):** refuse on `main` with a clear message;
  otherwise unchanged.
- **PyYAML (Andrew):** tests use `uv run --with pyyaml` when uv is present, else
  python3; a missing yaml module fails with a one-line install hint.
- Consolidation home (judgment, per the round-1 decision text): canonical
  statement in `build-process.md` §Completion; skills keep one local operative
  sentence plus a pointer, because skills load alone.
- Out of scope: Andrew's user-level instructions (`~/.codex/AGENTS.md`
  "Cross-model review") — outside the repo; proposed to Andrew, not edited.
  Stale `roadmap.md` links in `architecture/SKILL.md` — parked.

## Architectural choice

Options: (A) one feature, four checkpoint stories by surface; (B) four separate
features; (C) one inline stride. B adds four review cycles for minor work; C
loses resume points across ~10 files with different acceptance surfaces. Choose
**A**: one feature review covers the bundle (one standard pass), stories are
checkpoints. S3 (consolidation) depends on S2 because both touch
quality-checkpoint's doc-review references.

## Implementation Units

### Unit 1 — Citation gate tidy-up
**File**: `plugins/research-pipeline/skills/gate-citations/SKILL.md`
**Story**: `feature-qvc-minor-remedies-citation-gate`
- Phase 3 command adds `--exit-code-on medium` (the gate's blocking policy:
  high + medium block; thin/low and patterns do not). Interpretation: exit 1
  with valid JSON = blocking findings present; exit 1 without valid JSON or any
  other non-zero = lint execution failure; exit 0 with valid JSON = no blocking
  chains. The JSON-validity check stays mandatory.
- Output adds one line: `Warn-only: campaign_unbound N, substrate_confidence_omitted N`
  (no items, no threshold).
- Status lists consume the lint's `broken_chains` rather than restating
  statuses; where a list is kept for humans it includes `acquisition-candidate`,
  `non-canonical-handle`, `duplicate-frontmatter-key`.
- Example paths use `.research/analysis/briefs/<slug>.md`.
- Version caveat names arXiv IDs, `§x.y` refs and "version N" phrases (until
  `feature-ar-fork-citation-matcher` lands; then shrink).
**Acceptance**: [ ] command runs verbatim on this repo and exits 0 with valid
JSON; [ ] a scratch fixture with a broken chain exits 1 with valid JSON and is
reported as blocking; [ ] no restated status list contradicts `lint-citations.py`.

### Unit 2 — doc-review retarget (trickiest)
**File**: `plugins/research-pipeline/skills/doc-review/SKILL.md`
**Story**: `feature-qvc-minor-remedies-doc-review`
- Discovery: foundation docs from `.work/CONVENTIONS.md` `foundation_docs:` when
  present, plus the knowledge index; `${PLUGIN_ROOT:-${CLAUDE_PLUGIN_ROOT}}`;
  namespaced `research-pipeline:knowledge-index`.
- Replace 2b–2d with: **2b Foundation vs active work** — a foundation assertion
  contradicting an active item's recorded decision; **2c Research refs exist** —
  `research_refs:`/cited research paths in active items resolve on disk;
  **2d Done-item claims** — files a done/archived item's notes name as delivered
  exist. Keep 2a, 2e–2i. Remove MCP/BigQuery/TypeScript module specifics
  (module passes stay generic).
- Severity table examples rewritten without roadmap/phase terms.
- **Autonomous fixes: mechanical classes only** — missing/broken references,
  stale paths, link targets, index regeneration. A contradiction between
  foundation docs or between a doc and an item decision is reported in an
  "Operator decisions needed" list, never auto-resolved.
- Report header adds `Baseline: <commit>`, `Iteration: N of 5`, `Capped: yes|no`.
- One line states the boundary with gate-docs: gate-docs checks a release
  bundle's drift; doc-review audits the whole corpus.
**Acceptance**: [ ] no remaining roadmap/phase/MCP/BigQuery/TypeScript-specific
checks; [ ] autofix scope excludes contradiction resolution explicitly; [ ] report
template has the three fields and quality-checkpoint's capped-baseline rule can
be read from them; [ ] skill-portability passes; [ ] frontmatter unchanged.

### Unit 3 — Consolidate duplicate rules
**Files**: `plugins/research-pipeline/docs/build-process.md` (canonical
§Completion), `docs/research-composition.md` (drop restatements → link),
`skills/quality-checkpoint/SKILL.md`, `skills/methodology-review/SKILL.md`,
`skills/methodology-review/references/review-record.md`,
`plugins/agentic-research/skills/research-orchestrator/references/verification-record.md`
(fork-owned per Andrew), `.work/CONVENTIONS.md`.
**Story**: `feature-qvc-minor-remedies-consolidate` (depends on doc-review story)
- Canonical rule text lives once in build-process §Completion ("missing,
  errored, stale, capped-with-blockers or unverified results are not passes;
  artifact existence, process success or zero items cannot substitute").
- Each skill keeps exactly one operative sentence where it acts on the rule,
  plus a pointer; remove further restatements in the same file.
- `research-composition.md` §Verification ownership reduced to ownership only
  plus a link. Same for "child completion ≠ parent convergence" (keep in
  methodology-review SKILL + decomposition ref; drop from composition and
  build-process).
**Acceptance**: [ ] `rg -n "not a pass|is not a pass|cannot substitute"` across
the listed files shows ≤ 1 occurrence per file and the canonical one in
build-process; [ ] no file loses a rule it operationally applies (reviewed by
diff); [ ] receipt subsection remains the canonical review-reuse statement.

### Unit 4 — Repo hygiene
**Files / Story**: `feature-qvc-minor-remedies-hygiene`
- `plugins/research-pipeline/scripts/tests/skill-portability.test.sh`,
  `plugins/agentic-research/scripts/tests/skill-metadata.test.sh`: choose
  `PY=(uv run --quiet --with pyyaml python)` when `command -v uv`, else
  `PY=(python3)`; pre-check `"${PY[@]}" -c 'import yaml'` and on failure print
  `PyYAML required: install uv or pip install pyyaml` and exit 2.
- `scripts/bump-version.sh`: before committing, if
  `git rev-parse --abbrev-ref HEAD` is `main`, print
  `Refusing to bump on main: bump on the arc branch and merge via PR` and exit 1.
- RP `feature-design/SKILL.md:194`, `epic-design/SKILL.md:231`: "Cross-Model
  Advisory Review policy (Part IV)" → "Risk-Driven Advisory Review (Part IV)";
  remove the "multi-pass `peer-review` loop" sentence; same-class peer → fall
  back to a fresh-context reviewer per principles (non-blocking), not skip.
- `docs/project-navigation.md`: document the fork's `models.md` additions as a
  fork patch alongside the AR patches.
**Acceptance**: [ ] both tests pass via default `bash` invocation with uv and
print the hint when yaml is unavailable (simulated with an empty
`PYTHONPATH` + `python3`); [ ] `bump-version.sh` on `main` exits 1 before any
file change (dry check in a scratch clone); [ ] grep finds no "Cross-Model
Advisory Review policy" or `peer-review` loop references in RP skills.

## Implementation Order
1. Unit 1, Unit 4 (independent). 2. Unit 2. 3. Unit 3 (after Unit 2).
4. Integrated verification, then one standard feature review with a receipt.

## Testing
Structural tests above; behavioral checks per unit (lint exit codes on a scratch
fixture, bump guard in a scratch clone, test hint path). doc-review: a fresh
sub-agent reads the retargeted skill and dry-runs discovery + Pass 1 on this repo
(read-only, no fixes) to confirm the checks are executable against `.work`.

## Risks
- **doc-review retarget breaks an adopter that still keeps roadmaps** —
  Fallback: legacy roadmap is reviewed as an ordinary foundation doc; phase
  checks can be restored behind a "legacy roadmap present" condition.
- **Consolidation drops a locally needed rule** — Fallback: Unit 3 acceptance
  requires per-file review that each operative sentence survives.
- **`--exit-code-on medium` conflates crash and findings (both exit 1)** —
  Fallback: JSON-validity check distinguishes them; documented.
- **Least sure**: Unit 2's new 2b (foundation vs item decision contradictions)
  may be noisy on long-lived items; keep it severity Medium unless the item is
  active and the contradiction is direct.

## Implementation notes
- Execution capability: host-coordinated; two parallel workers (Units 1+4 and
  Unit 2, disjoint write sets), then one worker for Unit 3 after Unit 2; host
  follow-up on the bump-version test. Justified by four heterogeneous surfaces.
- Review weight: standard (default).
- Files changed: gate-citations SKILL; doc-review SKILL; build-process,
  research-composition, quality-checkpoint, methodology-review SKILL +
  review-record, AR verification-record, CONVENTIONS; RP feature/epic-design;
  two skill tests; `scripts/bump-version.sh`;
  `plugins/agile-workflow/scripts/tests/bump-version.test.sh`;
  `docs/project-navigation.md`.
- Tests added/removed: bump-version guard regression case (+4 assertions);
  test scratch repos seeded on a named branch.
- Simplification: doc-review 353 → 326 lines; restated status lists removed from
  gate-citations; ~165 words of duplicated rule prose removed.
- Discrepancies from design: see each story's completion evidence (doc-review
  description edit and mechanical-only loop exit; gate-citations extra lines;
  POSIX `set --`; `--no-project`; bump test patched outside the original unit).
- Adjacent issues parked: `idea-architecture-roadmap-links`.

## Integrated verification (2026-10-19)
RP skill portability ok; AR skill metadata ok; resolver test ok; bump-version
70/70; ARD conformance 57/57; gate lint command (`--exit-code-on medium`) on
this repo exit 0 with valid JSON. Owed at review: a fresh-context doc-review
dry run (the worker's was in-context).
