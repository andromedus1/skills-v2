---
source_handle: upstream-learnings-observations
fetched: 2026-10-19
source_path: .research/reference/upstream-learnings-2026-10/repository-observations.json
provenance: source-direct
substrate_confidence: source-direct
---

# Upstream delta observation record (nklisch/skills and peeragent)

## Structure and scope

A generated listing (`provenance: generated-listing`) produced from this
checkout's Git objects plus public GitHub API reads of `nklisch/peeragent`.
It records the upstream ref and SHA, merge base, fork head, per-plugin commit
lists, diff shortstats, manifest versions at three revisions, Antigravity
root-manifest presence, add-then-remove file events in Workbench, selected
root-path histories, marketplace additions, a fork grep, two test-file
presence checks, local peeragent cache versions and public peeragent release
and compare listings. It is observation data, not a usage log.

## Anchored observations

- `upstream_sha` 638867b6 (commit date 2026-10-02); `merge_base` 43f7f4bf;
  224 upstream commits since the merge base; total diff 226 files,
  +13842/−12470.
- Per-area upstream commit counts: workbench 159, agile-workflow 10,
  prose-craft 9, sol-calibration 8, code-audit 5, ux-ui-design 3,
  declaudify 2, agentic-research 1, agent-coordination 1, nates-toolkit 1,
  workflow 1, research-pipeline 0.
- Claude manifest versions (merge base → upstream; fork head):
  agile-workflow 0.16.14 → 0.16.16 (fork 0.16.14); code-audit 0.2.0 → 0.2.2
  (fork 0.2.0); ux-ui-design 0.5.0 → 1.0.0 (fork 0.5.0); prose-craft
  0.1.3 → 0.3.1 (fork 0.1.3); workbench 0.5.0 → 0.26.11 (fork 0.5.0);
  agentic-research 0.6.5 → 0.6.5 (fork 0.7.0); sol-calibration absent →
  0.1.3; declaudify absent → 0.1.1 (both absent in fork).
- `agy_root_manifest_present`: upstream true for every listed plugin except
  declaudify and research-pipeline; fork head false for all.
- Workbench: 67 of 159 commits are version-bump commits.
- `workbench_add_then_remove`: `skills/context-scan/` added by 6c82486b
  (2026-09-10, "Add Workbench context scanner with bounded remediation") and
  deleted by d1c1875f (2026-09-16, "Remove context-scan from Workbench");
  `hooks/hooks.json` and `hooks/scripts/session-context.py` added by
  6eebf473 (2026-08-02, "add lightweight SessionStart posture hook") and
  deleted by e492d435 (2026-09-19, "Simplify Workbench activation and
  centralize lifecycle guidance"); the upstream tree has no Workbench hooks.
- Workbench commit subjects include 76fddf96 "bound thorough review passes"
  (2026-08-23), c61d39ae "Allow uncapped Workbench reviews" (2026-08-24) and
  29eb790a "Calibrate Workbench review convergence" (2026-08-24); 3ba8c97b
  "Restore dropped Workbench guidance and add an evidence-depth dial"
  (2026-09-09).
- `claude_marketplace_names_added_upstream`: sol-calibration,
  theatre-feedback, declaudify. theatre-feedback is a `git-subdir` source at
  `https://github.com/nklisch/theatre` (e6634685).
- `root_paths`: `docs/PRINCIPLES.md` was created upstream (+71 lines);
  `.research/CONVENTIONS.md` changed once (60c6390d); `.work/CONVENTIONS.md`
  appears in 64 upstream commits.
- `fork_refs_to_removed_ux_ui_skill_names`: 19 grep lines at fork HEAD under
  `plugins/research-pipeline` and `plugins/agile-workflow/skills`, including
  `plugins/research-pipeline/skills/epic-design/SKILL.md` (`/ux-ui-design:palette`,
  `:screens`, `:flows`, `ux-ui-principles`) and
  `plugins/research-pipeline/skills/feature-design/SKILL.md`
  (`/ux-ui-design:screens`).
- `bump_version_test`: the fork's `bump-version.test.sh` has a
  refuse-on-main guard block using `REPO12`; upstream's adds "Test group 9"
  (Workbench stamp) also using `REPO12`.
- Fork marketplace `peeragent` entry: `git-subdir` source
  `https://github.com/nklisch/peeragent`, path `plugin`, no ref pin; its
  description says it "Ships the peer and peer-review skills".
- Local caches: Claude `peeragent` 0.8.1; Codex `peeragent` 0.8.3; the
  `skills/` directories of the two cached versions are identical (`diff -rq`
  exit 0).
- Public peeragent: plugin `skills/` contains only `peer` at v0.8.1 and
  v0.8.3; four commits v0.8.1…v0.8.3; one commit v0.8.3…main
  (de88d8dc, "chore: refresh committed peeragent binaries [skip ci]").
- `fork_files_at_head`: both fork marketplace catalogs list `workbench`
  (manifest 0.5.0) among 12 plugins; fork `.research/CONVENTIONS.md` has no
  `owner:` frontmatter; fork `.work/CONVENTIONS.md` has no "Overbuilding
  calibration" section, does carry a review **Receipt** template, and states
  "There is **no CI**".
- More `fork_files_at_head`: fork `plugins/workbench` has no
  `skills/ideate/references/provocation.md` (the file upstream code-audit's
  cousin note points to); no file under `plugins/` outside prose-craft
  references `prose-craft`, `prose-draft`, `prose-refine` or `prose-review`;
  fork `plugins/agile-workflow/docs/PRINCIPLES.md` contains "Leave It
  Simpler", "Compatibility Is Earned", "Tests Earn Their Keep" and "Review
  proportionality" but not "Never game", "xfail" or "File real bugs"; fork
  `AGENTS.md` contains the phrase "both Claude and Codex shapes"; one fork
  commit since the merge base touches `scripts/bump-version.sh` (5212d934).
