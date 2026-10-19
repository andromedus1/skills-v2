#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
plugin_root=$(CDPATH= cd -- "$script_dir/../.." && pwd)

# PyYAML: prefer an ephemeral uv environment; fall back to the system python3.
if command -v uv >/dev/null 2>&1; then
  set -- uv run --quiet --no-project --with pyyaml python
else
  set -- python3
fi
if ! "$@" -c 'import yaml' >/dev/null 2>&1; then
  printf '%s\n' 'PyYAML required: install uv or pip install pyyaml' >&2
  exit 2
fi

"$@" - "$plugin_root" <<'PY'
from pathlib import Path
import sys
import yaml

root = Path(sys.argv[1])
metadata = root / "skills" / "research-orchestrator" / "agents" / "openai.yaml"
document = yaml.safe_load(metadata.read_text(encoding="utf-8"))

prompt = document.get("interface", {}).get("default_prompt")
if not isinstance(prompt, str) or "$research-orchestrator" not in prompt:
    raise AssertionError(f"{metadata}: default prompt does not name the skill")

policy = document.get("policy", {}).get("allow_implicit_invocation")
if policy is not True:
    raise AssertionError(
        f"{metadata}: research-orchestrator must allow implicit invocation for "
        "research-pipeline cross-plugin routing"
    )
PY

printf '%s\n' 'agentic-research skill metadata: ok'
