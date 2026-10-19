---
source_handle: peeragent-v083-release
fetched: 2026-10-19
source_url: https://github.com/nklisch/peeragent/releases/tag/v0.8.3
provenance: source-direct
substrate_confidence: source-direct
acquisition: GitHub API (gh release view v0.8.3 -R nklisch/peeragent); v0.8.1 release body read for the baseline
---

# peeragent v0.8.3 release

## Anchored passages

- Published 2026-10-11T19:01:22Z (latest); target commit
  1bb09448ad2df00bf857c437d3c87a3ee5986db8.
- "Fix Windows npm shim launches from paths containing spaces and
  parentheses. The shared runner forwards quoted arguments, shell
  metacharacters, and multiline prompts through deferred environment
  expansion without interpreting task text as commands. Covers Codex, Claude,
  Antigravity/agy, and Pi through their shared launch path; native
  executables and Unix launches retain direct execution."
- Validation: "full Windows tests and vet from PowerShell and Git Bash ...
  Windows/Linux/macOS CI tests and vet. Live agent tasks were not exercised
  on Linux or macOS."
- "Quoted arguments exceeding cmd.exe's 8191-character limit fail
  explicitly; use a native executable for longer tasks."
- "Use v0.8.3 instead of v0.8.2, whose newline rejection blocked peeragent's
  generated instruction header."
- Baseline v0.8.1 (2026-09-29): "GPT-6.1 Sol is now supported for Codex
  delegation. `--model sol` selects `gpt-6.1-sol`."
