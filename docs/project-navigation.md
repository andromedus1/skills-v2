---
title: Skills v2 fork navigation
description: Start here to find this fork's current process, research ownership, methodology-review entrypoint and inherited upstream references.
type: module-rules
updated: 2026-10-19
nav_priority: high
summary: Maps the fork's authoritative instructions and plugin documentation, distinguishes upstream Workbench references, and explains how to regenerate the repository knowledge index.
decisions:
  - Follow AGENTS.md, README.md and the work conventions for this fork's process.
  - Use Research Pipeline for project context, Agentic Research for grounded research, and Agile Workflow for delivery.
  - Treat inherited Workbench guidance as upstream context without changing the fork's substrate.
related:
  - {slug: ../AGENTS.md, relationship: depends-on}
  - {slug: ../README.md, relationship: depends-on}
  - {slug: ../plugins/research-pipeline/docs/build-process.md, relationship: depends-on}
  - {slug: ../plugins/research-pipeline/docs/research-composition.md, relationship: depends-on}
  - {slug: ../plugins/research-pipeline/skills/methodology-review/SKILL.md, relationship: parallel-to}
  - {slug: ../plugins/agentic-research/README.md, relationship: parallel-to}
---

# Skills v2 fork navigation

Use [AGENTS.md](../AGENTS.md), the [repository README](../README.md) and
[work conventions](../.work/CONVENTIONS.md) to establish this fork's current
process. The [build process](../plugins/research-pipeline/docs/build-process.md)
connects its research and delivery skills.

## Find the relevant capability

| Need | Source |
|---|---|
| Understand Research Pipeline and Agentic Research ownership | [Research composition](../plugins/research-pipeline/docs/research-composition.md) |
| Choose a project-facing research or planning entrypoint | [Research Pipeline](../plugins/research-pipeline/README.md) |
| Understand research scope, evidence and verification | [Agentic Research](../plugins/agentic-research/README.md) |
| Compare a project's methods and adjudicate improvements | [Methodology Review](../plugins/research-pipeline/skills/methodology-review/SKILL.md) |
| Find delivery state, dependencies and completed work | [Agile Workflow](../plugins/agile-workflow/README.md) and `.work/bin/work-view` |
| Browse document relationships and evidence links | [Knowledge Graph](../plugins/research-pipeline/skills/knowledge-graph/SKILL.md) |

Work items own delivery state. Consult the matching item and Git history for
implementation and review evidence; a skill's presence does not establish that
it has been released or exercised on a real project.

## Read inherited documents in context

[VISION.md](VISION.md), [SPEC.md](SPEC.md), [ARCHITECTURE.md](ARCHITECTURE.md)
and the [Workbench guide](workbench-guide.md) retain Nathan's upstream context.
Their Workbench emphasis describes his workflow and testing direction. This
fork uses the composition selected by its own instructions; those references
do not authorize a substrate conversion.

The [Agile Workflow guide](agile-workflow-guide.md) and
[UI design guide](ux-ui-design-guide.md) provide usage context. Check the relevant
local skill for its operative contract. The [Workflow Suite guide](workflow-guide.md)
documents a separate deprecated plugin.

Research under `docs/research/` retains its source dates and limitations in the
body. Adding or refreshing index metadata is not a new verification of those
external claims.

## Narrow Agentic Research fork patches

This fork retains explicit Codex invocation metadata for the research orchestrator
and a directly linked [verification-record writing aid](../plugins/agentic-research/skills/research-orchestrator/references/verification-record.md).
The latter makes assessed inputs, actual gate outcomes and pending corrections
recoverable without changing ARD's gate catalog, rigor, isolation or stop rules.
The canonical `ard-core/` kernel, discipline, schemas and generated catalogs remain
unchanged. Preserve these documented differences when comparing upstream trees;
implementation and review history belongs to `.work/` and Git.

## Agile Workflow fork patches

Agile Workflow is upstream-owned; this fork patches its
[`principles/references/models.md`](../plugins/agile-workflow/skills/principles/references/models.md).
The patch adds Kimi (Moonshot) as a Pi-native driver class that is not a peeragent target,
and Pi driver settings. It also adds a Kimi row to the host-to-peer and mechanism
tables. The implementation-worker row names Luna only where available, else the
host's strongest verified writing tier, with GLM-5.2 and Kimi as Pi drivers to
evaluate. The fork's `scripts/bump-version.sh` refuses to bump on `main`, so
[`bump-version.test.sh`](../plugins/agile-workflow/scripts/tests/bump-version.test.sh)
seeds its scratch repository on a named branch and covers that guard. Preserve
these additions when syncing upstream.

## Regenerate the knowledge index

From the repository root, run the existing generator with PyYAML available:

```sh
uv run --no-project --with PyYAML python plugins/research-pipeline/skills/knowledge-index/regen.py .
```

Append `--lint-only` for validation without writes. The
[Knowledge Index skill](../plugins/research-pipeline/skills/knowledge-index/SKILL.md)
defines the source metadata and discovery rules.

The three generated files serve different reading costs:

- `knowledge-index-nav.yaml` gives session-start counts and essential pointers.
- `knowledge-index.yaml` catalogs individual documents for on-demand lookup.
- `knowledge-index-detail.yaml` adds summaries, findings, decisions and relationships.

The generator scans `docs/`, eligible `.research/` analyses and `.work/` items.
It does not recursively catalog plugin source trees; use the links above to reach
their documentation. Raw research sources remain under Agentic Research's own
evidence management. Edit source frontmatter and regenerate after knowledge
changes; the session hook reads the generated navigator without regenerating it.
