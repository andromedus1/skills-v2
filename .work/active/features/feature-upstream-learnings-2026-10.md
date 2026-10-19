---
id: feature-upstream-learnings-2026-10
kind: feature
stage: done
tags: [research-pipeline, agentic-research, upstream]
parent: null
depends_on: []
release_binding: null
gate_origin: null
research_refs: [upstream-learnings-2026-10-landscape]
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

## Research

Scout landscape `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`
(floor rigor: lint pass; lead spot-check by the engagement worker; host
re-checked the decision-bearing claims — agile-workflow 0.16.14 → 0.16.16;
ux-ui-design 1.0.0 is a single `ux-ui` skill; 15 `ux-ui-design:*` calls in our
design skills; sol-calibration writes an AGENTS.md block; declaudify injects
"You are not Claude" each turn). Cross-cutting theme: upstream's direction is
anti-overbuilding (sol-calibration; Workbench overbuilding calibration and
machinery forecast; "receipts and counters" named as likely overbuilding) — in
tension with QVC's receipts and aligned with QVC-E/METH-002 and Andrew's
domain-review jobs.

## Operator decisions (Andrew, 2026-10-19)

| Question | Decision | Item |
| --- | --- | --- |
| Sync upstream-owned plugins | **Sync all, keep patches**: agile-workflow 0.16.16, ux-ui-design 1.0.0, prose-craft, code-audit, small manifest touches; update RP design skills to the `ux-ui` concierge; preserve fork patches; skip upstream's Workbench-only bump test group; smoke-check UI triggers on both hosts | `feature-upstream-sync-2026-10` |
| Workbench | **Sync tree, keep disabled** (0.5.0 → 0.26.11; prior art only) | `feature-upstream-sync-2026-10` |
| Adapt ideas | **Overbuild calibration** (CONVENTIONS section + machinery forecast in RP feature/epic-design; re-examine receipts against it) and **delegation safety rule** | `feature-overbuild-calibration` |
| | **AR research rigor ideas** (adaptive rigor option, `owner:` in `.research/CONVENTIONS.md`, stop after the same failure twice) | `feature-ar-research-rigor-ideas` |
| | **Model notes file** (`.work/MODEL-NOTES.md`, pruned and evidence-graded) | `feature-model-notes` |
| New plugins / channels | **None**: skip sol-calibration, declaudify and Antigravity manifests | — |

Host-added maintenance inside the sync (no decision needed): update Claude's
cached peeragent to 0.8.3 and correct our catalog's peeragent description
("peer and peer-review" → "peer").

## Delivery and closure (2026-10-19)

| Decision | Item | Outcome |
| --- | --- | --- |
| Sync upstream-owned plugins; Workbench tree | `feature-upstream-sync-2026-10` | done — merge `422de5eb` with `638867b6`; callers `af5505c2`; review (env-only block) closed with receipt |
| Overbuild calibration + delegation rule | `feature-overbuild-calibration` | done — 2 blockers, 2 important fixed `edd9573a`; cuts C1–C5 proposed for Andrew |
| AR rigor ideas | `feature-ar-research-rigor-ideas` | done — `adaptive`, owner marker, hybrid stop rule; review env-only block |
| Model notes (Workbench-style) | `feature-model-notes` | done — 2 evidence blockers fixed `edd9573a` |
| New plugins/channels | — | declined |

Research: `story-research-upstream-learnings` (floor rigor) — done. Pending for
Andrew: proposed cuts C1–C5 in `feature-overbuild-calibration`; after merge,
install updates (agile-workflow 0.16.16, ux-ui-design 1.0.0, peeragent 0.8.3 on
Claude) and a `ux-ui` discovery smoke on both hosts.
