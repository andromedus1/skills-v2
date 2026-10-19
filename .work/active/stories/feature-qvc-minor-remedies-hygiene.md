---
id: feature-qvc-minor-remedies-hygiene
kind: story
stage: done
tags: [methodology-review, research-pipeline, cleanup]
parent: feature-qvc-minor-remedies
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# QVC minor remedies — hygiene

## Brief
Checkpoint for the parent feature's unit covering "hygiene".

## Implementation
See `feature-qvc-minor-remedies` § Implementation Units (hygiene).

## Completion evidence (2026-10-19)
- Tests (`skill-portability.test.sh`, `skill-metadata.test.sh`): `uv run --quiet
  --no-project --with pyyaml python` when uv exists, else python3; yaml pre-check
  prints `PyYAML required: install uv or pip install pyyaml` and exits 2. POSIX
  `set --` instead of a bash array (scripts are `#!/bin/sh`). Verified ok via
  `bash` and `sh`; no-yaml path prints the hint, exit 2.
- `scripts/bump-version.sh`: refuses on `main` before any file change (exit 1,
  tree clean, HEAD unchanged in a scratch clone); non-main behavior unchanged.
- Host follow-up: `plugins/agile-workflow/scripts/tests/bump-version.test.sh`
  (CI-run) seeded scratch repos with plain `git init`, which the guard would break
  where `init.defaultBranch=main`; now `git init -q -b scratch` plus a guard
  regression case. 70/70 pass with default config and with
  `init.defaultBranch=main`. Documented as an Agile Workflow fork patch.
- RP `feature-design`/`epic-design` advisory paragraphs: "Risk-Driven Advisory
  Review (Part IV)"; `peer-review` loop sentence removed; same-class peer falls
  back to a fresh-context reviewer, non-blocking. Grep clean.
- `docs/project-navigation.md`: "Agile Workflow fork patches" section documents
  the `models.md` additions (verified against `upstream/main`, fetched
  2026-08-02) and the bump-version test change.
