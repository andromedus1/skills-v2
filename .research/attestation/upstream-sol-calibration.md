---
source_handle: upstream-sol-calibration
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/tree/638867b65e35057518865e0ece29e980468b0a94/plugins/sol-calibration
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects via the upstream remote (638867b6:plugins/sol-calibration README and three SKILL.md files; commit messages 61e695ba cf123e25 1b2723b9 a9b7f748; closed items at e935454f^ and a622883e^)
---

# sol-calibration plugin (new, 0.1.3)

## Structure and scope

Three skills — `calibrate-posture`, `proportionality-check`,
`overbuilder-review` — with Claude, Codex and Antigravity manifests and
`agents/openai.yaml` per skill. No substrate dependency.

## Anchored passages

- README: calibrate-posture "proposes a spectrum of working postures ...
  from *ship the simplest thing, skip security and verification* to *verify
  at every boundary* — and writes the one you pick into a managed block in
  project and/or global AGENTS.md". "Calibration runs in both directions"
- calibrate-posture inspects "Existing AGENTS.md files (project and global
  `~/AGENTS.md`)" and writes a block delimited by
  `<!-- sol-calibration:start -->` / `<!-- sol-calibration:end -->` after
  asking "project AGENTS.md, global `~/AGENTS.md`, or both".
- proportionality-check: "Not a gate — a glance at the room"; "Name the
  threat or failure, and who it hurts"; "A 25x ratio (500 lines of guards for
  20 lines of feature) is the smell"; "Not a license to skip verification the
  user asked for, a project convention requires, or a written posture
  mandates."
- overbuilder-review: "separates guarantees from proof mechanisms" and
  returns "a ranked packet of cuts, deferrals, and demotions with the smallest
  mechanism that preserves each real guarantee" (a9b7f748). Calibration step
  reads "any written calibration already present: a `sol-calibration`
  posture block, a Workbench `## Overbuilding calibration`". Families
  include "Proof rituals", "Speculative seams", "Configurability without
  configurers", "Duplicate gates and altitude leaks".
- Item story-sol-calibration-stop-boundaries: "Sol often needs reasonable stop
  boundaries"; opt-in "because pre-task questions are friction some users
  don't want".
- Item story-sol-calibration-context-pulls: other context "can over-index the
  agent toward a heavier posture: domain vocabulary ..., heavy test/CI
  infrastructure, harness- or plugin-injected instructions, existing
  AGENTS.md rigor rules, long-session drift".
