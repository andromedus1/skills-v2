---
source_handle: peeragent-v081-v083-compare
fetched: 2026-10-19
source_url: https://github.com/nklisch/peeragent/compare/v0.8.1...v0.8.3
provenance: source-direct
substrate_confidence: source-direct
acquisition: GitHub API compare (commit list, file list, patches for README.md, internal/executil/exec.go, internal/executil/exec_other.go)
---

# peeragent v0.8.1…v0.8.3 compare

## Anchored passages

- Four commits: fae254ed (2026-09-29, refresh committed binaries), a6aeebe2
  (2026-10-11, "Fix Windows npm shim launches and release v0.8.2"), dbbe38c7
  (refresh binaries), 1bb09448 (2026-10-11, "Preserve multiline Windows shim
  tasks and release v0.8.3").
- Files: version fields in manifests and `package.json`; new
  `internal/executil/{batch,exec_windows,exec_other}.go` and tests; Windows
  and Unix test splits; new `.github/workflows/test.yml`; rebuilt
  `plugin/bin/{darwin,linux}-{amd64,arm64}/peeragent`. No file under
  `plugin/skills/` changed.
- `exec.go`: `exec.CommandContext(ctx, name, args...)` is replaced by
  `commandContext(ctx, name, args)`; `exec_other.go` (`//go:build !windows`)
  defines `commandContext` as `return exec.CommandContext(ctx, name, args...), nil`.
- README additions describe Windows `.cmd` shim handling only, and bump the
  Pi install pin and release examples from 0.8.1 to 0.8.3.
