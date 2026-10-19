# skills-v2

Andrew Clark's cross-host agent workflow suite, forked from
[nklisch/skills](https://github.com/nklisch/skills).

The primary project process is:

```text
agile-workflow        durable delivery state in .work/
      +
research-pipeline     project discovery, planning, architecture, knowledge, quality
      +
agentic-research      authoritative grounded-research engine and .research/ contract
```

This composition works in Claude Code and Codex. It is local-first, file-backed,
and designed to preserve useful context across sessions without making chat
history authoritative.

## Process

1. Orient from the knowledge navigator and `.work/` snapshot.
2. Use `research-pipeline:ideate`; it invokes `scout` for prior art.
3. Commission grounded research through the familiar pipeline intents:
   `research`, `brief`, `deep-research`, or `research-program`.
4. Those intents delegate research execution and verification to
   `agentic-research:research-orchestrator`.
5. Ground architecture, epics, and features in the resulting artifacts.
6. Implement, review, and release through `agile-workflow`.
7. Run `research-pipeline:quality-checkpoint` at release boundaries.

Use [methodology-review](plugins/research-pipeline/skills/methodology-review/SKILL.md)
to compare a project's methods with prior art, adjudicate proposed changes, and
reassess outcomes after authorized work. It selects a focused, coordinated or
program review from mapped decisions, while research adapts to evidence gaps
within each component. Durable child and parent records preserve decisions,
coverage, shared assessment rounds and resume state. A fresh whole-scope
assessment determines the explicit exit status; child completion alone does not
close the parent. See the skill's linked references for the review record and
decomposition protocol.

Use `.work/bin/work-view` to find current work and
`.work/bin/work-view --scope backlog` for parked work, also listed in the
[backlog](.work/backlog/). Completed archive stubs retain a
`git_ref` for recovering the full record at its original active path, as
described by [Agile Workflow's archive guidance](plugins/agile-workflow/skills/review/references/substrate-side-effects.md).

At release boundaries, [quality-checkpoint](plugins/research-pipeline/skills/quality-checkpoint/SKILL.md)
uses configured gates and reconciles their actual outcomes, residual findings
and covering delivery-review evidence. `--pending` applies
`agile-workflow:release-deploy`'s eligibility rules to candidates and is
preflight only. Research, delivery review and other gate owners retain their
own verification and correction rules; a completed standard review with
verified accepted fixes remains covering evidence. The citation gate groups
advisories to improve reporting signal while leaving Agentic Research's
authoritative lint and semantic verification unchanged.

See [build process](plugins/research-pipeline/docs/build-process.md) and
[research composition](plugins/research-pipeline/docs/research-composition.md).

## Workflow ownership

| Capability | Authority |
|---|---|
| Work items, dependencies, stages, gates, release binding, queue draining | `agile-workflow` |
| Prior art, project intent, architecture, design overlays, knowledge index/graph, quality orchestration | `research-pipeline` |
| ARD, source attestations, research decomposition, synthesis, verification, refresh, research handoff | `agentic-research` |
| UI/UX mockups | `ux-ui-design` |
| Standalone audits | `code-audit` |
| Utilities, prose, coordination | their corresponding upstream plugins |

`research-pipeline` does not vendor ARD. Existing legacy research corpora remain
discoverable and are migrated only through the operator-confirmed
`agentic-research:convert` flow.

## Workbench

Workbench ships because it is part of Nathan's current upstream, but it is not
the process used by this fork. Its `.work/`, `.research/`, and `.knowledge/`
schemas are mutually exclusive with this suite's retained substrate.

Workbench is useful prior art. Candidate ideas—outcome-first routing,
proportional ceremony, semantic autonomy, and review weights—may be adopted
individually when they can be expressed through the retained process. Installing
Workbench never converts an existing project automatically.

## Knowledge and hooks

`research-pipeline:knowledge-index` derives three files from project artifacts:

- `docs/knowledge-index-nav.yaml` — compact session orientation;
- `docs/knowledge-index.yaml` — full terse catalog;
- `docs/knowledge-index-detail.yaml` — summaries and relationships.

The navigator and compact `.work/` snapshot load at SessionStart and on
host-supported PostCompact. Codex PostCompact output is side-effect-only, so
Codex relies on its compact/resume SessionStart path for reinjection. Missing
substrates are silent. Navigator generation fails above the 10KB inline budget.

## Plugin catalog

The repository carries Nathan's current plugins plus the fork-owned
`research-pipeline` and `agentic-research`. The two marketplace catalogs are:

- [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json)
- [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json)

Every local plugin has matching Claude and Codex manifests. Upstream-owned
plugin trees track `upstream/main`; fork-specific behavior belongs in the
fork-owned plugins or is documented as a narrow upstream patch.

## Development

- Read [AGENTS.md](AGENTS.md) before editing.
- Track substantive changes in `.work/` using the retained Agile Workflow schema.
- Preserve upstream-owned plugins unless intentionally syncing or applying a
  documented portability/test correction.
- Run plugin tests, marketplace validation, hook tests, and cross-host smoke
  tests before publishing.
- Version plugins independently only after feature changes are committed and
  validation passes.
