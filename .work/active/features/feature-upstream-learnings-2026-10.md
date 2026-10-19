---
id: feature-upstream-learnings-2026-10
kind: feature
stage: drafting
tags: [research-pipeline, agentic-research, upstream]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Learnings from Nathan's current upstream skills and peeragent

## Brief

Andrew (2026-10-19): "check what kevin and nathan have done with their current
versions of skills/agentic-research and see if we want to incorporate any
learnings"; later "let's just look at nathan's stuff (skills, and perhaps
peeragent)". Kevin (Kevoun) is the credited author of agentic-research, which
ships inside `nklisch/skills`, so the upstream comparison covers his work.

Compare `nklisch/skills` `upstream/main` (`638867b6`, 2026-10-02) against this
fork since the last sync merge base `43f7f4bf` (2026-08-01): 224 upstream commits —
Workbench 159, prose-craft 9, sol-calibration 8 (new), agile-workflow 10,
code-audit 5, ux-ui-design 3 (−10k lines), declaudify 2 (new), single-commit
touches elsewhere (agentic-research 1). Plus `nklisch/peeragent` 0.8.1 → 0.8.3.

Output: a decision packet (adopt / adapt / skip, with rationale and the exact
change each choice authorizes) for Andrew. This item owns the comparison and the
decisions; research engagements it commissions own their own verification.
Adopted changes are scoped as their own items and go through normal design,
implementation and review.

Constraints: Workbench is prior art, never a migration target (AGENTS.md). The
fork now owns `research-pipeline` and `agentic-research`; upstream-owned plugins
can be synced or patched with documented fork patches. No sync, merge or
plugin update is authorized by this item.

## Simplification opportunity

Upstream's ux-ui-design slim-down (−10k lines) and any upstream removals may let
the fork drop content it still carries.
