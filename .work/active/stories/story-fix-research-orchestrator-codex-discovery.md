---
id: story-fix-research-orchestrator-codex-discovery
kind: story
stage: done
tags: [bug, agentic-research, codex, plugins]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-08-11
updated: 2026-08-11
---

# Restore Codex discovery of the research orchestrator

## Symptom

Codex discovers the installed `agentic-research` plugin and its `convert`,
`research-discipline`, and `research-handoff` skills, but omits
`agentic-research:research-orchestrator`. Research Pipeline therefore reports its
required cross-plugin research engine as unavailable even though the skill is present
in the installed plugin cache.

## Root cause

`skills/research-orchestrator/agents/openai.yaml` sets
`allow_implicit_invocation: false`. That policy hides the skill from implicit Codex
discovery, contradicting Research Pipeline's public pairing contract, which routes its
research entrypoints to the orchestrator without requiring the user to name the
underlying skill explicitly.

## Fix approach

Allow implicit invocation for `research-orchestrator`. Keep its explicit default prompt
and all orchestration behavior unchanged.

## Regression test

`plugins/agentic-research/scripts/tests/skill-metadata.test.sh` asserts that the
orchestrator's Codex metadata names the skill and enables implicit invocation for
cross-plugin routing.

## Implementation notes

- **Execution capability:** focused local repair. The defect is one invocation-policy
  value with a narrow cross-plugin discovery contract; broader implementation or
  independent review would add no useful coverage.
- **Files changed:** enabled implicit invocation in the orchestrator's Codex metadata
  and added the plugin-owned metadata regression test.
- **Failing reproduction:** the new regression initially failed with
  `research-orchestrator must allow implicit invocation for research-pipeline
  cross-plugin routing` while the policy was `false`.
- **Verification:** the new regression passes; Research Pipeline portability and
  companion-plugin resolution tests pass; ARD conformance passes 57/57 checks. The
  research-view parity test exited successfully after its documented skip because no
  local prebuilt binary or Cargo toolchain was available.
- **Installed-path confirmation:** `codex plugin add
  agentic-research@andrewclark88-skills-v2` refreshed the local-marketplace cache, and
  the installed `research-orchestrator/agents/openai.yaml` now contains
  `allow_implicit_invocation: true`. A new Codex session is required to rebuild the
  session's discovered-skill catalog.
- **Adjacent issues parked:** none.

## Review

Bounded inline standalone-story review: **approved**. The change is limited to the
Codex invocation policy that caused the reproduced discovery failure; explicit skill
invocation remains available, Claude packaging is untouched, and the new regression
pins the cross-plugin requirement. No material blockers, important findings, or nits.
No independent, fresh-context, or cross-model reviewer ran, as required for a
standalone fix story.
