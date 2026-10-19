---
source_handle: upstream-agile-workflow-delta
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/tree/638867b65e35057518865e0ece29e980468b0a94/plugins/agile-workflow
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects of the same revision via the upstream remote (git diff 43f7f4bf..638867b6 -- plugins/agile-workflow; git show of listed commits)
---

# nklisch/skills agile-workflow changes, 43f7f4bf..638867b6

## Structure and scope

Ten commits touch `plugins/agile-workflow`. Text changes (binaries excluded):
manifests, a new root `plugin.json`, `scripts/tests/bump-version.test.sh`,
`scripts/work-view.sh`, and the `bold-refactor`, `epic-design`,
`feature-design`, `ideate` and `scope` skills.

## Anchored passages

- **Version:** 0.16.14 → 0.16.16. Commit f4fcf5bb bumped to 0.16.17 and
  4c0476d7 reverted it the same day (2026-08-24).
- **UI callers (2e812a1c):** epic-design Phase 4.6 no longer invokes
  `/ux-ui-design:palette`, `:screens` and `:flows`; it "offer[s] the
  `/ux-ui-design:ux-ui` concierge for visual alignment before child features
  are written" and records mock paths "when mocks are produced".
  feature-design, scope and ideate are rewritten the same way; feature-design's
  phase changes from "UI surface fallback" to "UI surface alignment" that
  offers the concierge "only when upstream coverage is missing".
- **bold-refactor (4cb428ae):** lens table becomes "a starting set, not a
  closed list"; a "Checkpoint pre-pass: the skeptic" hands suggestions to "a
  fresh-context reviewer sub-agent ... a different model class than yours
  when one is available, a starkly skeptical persona when it isn't"; verdicts
  "kill / narrow / pass with reasons". Guardrail: "No suggestion reaches the
  user without the fresh-context, cross-model skeptical review".
- **Antigravity manifest (3ed9c532):** new `plugins/agile-workflow/plugin.json`
  (name, version, description, author, repository, license).
- **Bump test (52c1af44):** adds "Test group 9: Workbench bump projects
  conventions stamp" — a Workbench bump must advance
  `workbench_version` in `.work/CONVENTIONS.md` and stage it.
- **Status context:** at both the merge base and 638867b6,
  `docs/agile-workflow-guide.md` opens with "Maintenance mode (KTLO)":
  "bug fixes and compatibility work land, but no new feature development is
  planned", and `AGENTS.md` says "New workflow capability goes into
  `workbench`; `agile-workflow` is in maintenance mode".
