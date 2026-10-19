---
source_handle: upstream-agy-multichannel
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/commit/3ed9c532fe1c48a123646d4d6fde206255daf7bb
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects via the upstream remote (git show 3ed9c532)
---

# Antigravity (AGY) manifests and multi-channel support (3ed9c532)

## Structure and scope

Nathan Klisch, 2026-08-15. 15 files, +177/−34: a root `plugin.json` in nine
plugins, `.agents/plugins.json`, `AGENTS.md`, `README.md`, `docs/SPEC.md`,
`docs/ARCHITECTURE.md`, `scripts/bump-version.sh`. No commit-message body.

## Anchored passages

- AGENTS.md heading becomes "Multi-channel distribution support (Claude Code,
  Codex, Antigravity, Pi via bridge)"; "`plugins/<name>/plugin.json` — for
  Google Antigravity (`agy`)"; "`.agents/plugins.json` — registers local
  workspace plugins for Antigravity discovery".
- Parity posture: "Codex and Antigravity get the equivalent in the same
  change unless a channel capability is impossible".
- `docs/SPEC.md`: "Each local plugin ... has three channel manifests".
- `scripts/bump-version.sh`: adds `agy_json="plugins/$plugin/plugin.json"`,
  refuses on a version mismatch, and bumps it with the other manifests.
- README install for Antigravity: "Clone or vendor the repository and add the
  desired plugins to your project (`.agents/plugins.json`) or global
  (`~/.gemini/config/plugins.json`) configuration".
- For agentic-research, agent-coordination, nates-toolkit and workflow this
  manifest is the only change in the range.
