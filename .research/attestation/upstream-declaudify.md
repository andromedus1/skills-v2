---
source_handle: upstream-declaudify
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/tree/638867b65e35057518865e0ece29e980468b0a94/plugins/declaudify
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects via the upstream remote (638867b6:plugins/declaudify README, hooks.json, declaudify.py)
---

# declaudify plugin (new, 0.1.1)

## Anchored passages

- README: "A Claude Code-only hook that injects a writing guide on every user
  turn"; "not registered in the Codex or Antigravity catalogs"; Pi support
  "is not provided or claimed".
- `hooks/hooks.json`: one `UserPromptSubmit` command hook, timeout 5.
- `declaudify.py` emits static `additionalContext` whose first bullet is
  "Do not talk like Claude. You are not Claude."; other bullets: "Use simple,
  direct technical language"; "treat the visible chat stream as the only
  shared context"; "When referring to the codebase, frame the reference for
  the user"; "Separate observed facts from inferences, decisions, and
  unknowns." The script docstring: "This hook is deliberately static."
- Introduced by 06aa9e55 (2026-08-20) with no commit-message body.
