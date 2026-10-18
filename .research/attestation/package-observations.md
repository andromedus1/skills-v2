---
source_handle: package-observations
fetched: 2026-10-18
source_path: .research/reference/research-package-boundary/repository-observations.json
provenance: source-direct
substrate_confidence: source-direct
---

# Repository inventory and resolver observation

## Structure and scope

The JSON record contains timestamp, baseline commit, per-plugin skill-directory
listings and full manifests with SHA-256 hashes, a reverse-reference text scan,
a historical Git change summary, resolver hash, and isolated probe results.
It is generated observation data, not a transcript of actual user sessions.

## Anchored observations

- `plugins.research-pipeline`: 24 skill directories; Claude manifest version
  0.2.0, author andrewclark88, repository andrewclark88/skills-v2. Description
  declares a project-process and knowledge overlay using Agentic Research.
- `plugins.agentic-research`: four skill directories; Claude manifest version
  0.6.5, author Kevoun, repository nklisch/skills. Description declares grounded
  research with selectable verification and a `.research/` substrate.
- Both plugins' Claude and Codex manifest contents omit a `dependencies` field.
- `skill_name_intersection` is empty. Names alone cannot measure semantic overlap.
- `reverse_reference_scan`: scanning Markdown, Python, shell and JSON files under
  Agentic Research for `research-pipeline` returns one test-label reference and
  no other match. This is a bounded literal scan, not a runtime dependency proof.
- `composition_commit`: commit 88775f35's stat records 32 changed files, 194
  insertions and 4,258 deletions, including removed Pipeline ARD copies. Those
  counts are commit scope, not a deduplication or quality metric.
- `resolver_probe`: two minimally valid cached directories, versions 1.9.0 and
  1.10.0, with no explicit root or sibling engine and an isolated child-process
  HOME. Exit code 0; selected version 1.9.0. No active-version registry was
  provided; this probes fallback selection rather than host activation.

## Source passage

Anchor `resolver_probe.selected_version`: `"selected_version": "1.9.0"`.

## Supplemental observations, 2026-10-18

- `distribution`: both repository marketplace catalogs distribute both plugins
  from local `./plugins/<name>` paths under `andrewclark88-skills-v2`.
- `engine_fork_diff`: against the recorded local `upstream/main` revision
  7056fdb2e14acd452c2b5b4d2da74ed46516beb0, two Agentic Research files differ:
  the orchestrator's Codex invocation policy changes from false to true and a
  regression test enforces it. `engine_patch_commit` records c7d0de75. This is a
  comparison with that pinned revision, not a claim about today's upstream HEAD.
  The reverse-scan's test-label match therefore guards a substantive fork patch.
- `resolver_references`: the only non-test caller found in Pipeline is
  `skills/gate-citations/SKILL.md:72`; other hits are in its resolver test.
- `pipeline_ard_named_paths`: no current Pipeline file named `discipline.md` or
  `lint-citations.py`, or under an `ard-core` path. This bounded filename check
  does not establish absence of every semantic duplicate.
- `portable_root_manifest_exists`: neither plugin has root `plugin.json`.
- `resolver_cross_host_probe`: with configured Claude cache, default Claude cache
  and default Codex root populated at version 0.6.5, fallback selected the default
  Codex root. It overrides the configured Claude cache in that fixture. This is
  simulated host-root precedence, not a measurement of installed-host activation.

## Revisions

Correction: added distribution, fork-policy, current-tree and cross-host probe
observations to cover previously omitted implementation context.
