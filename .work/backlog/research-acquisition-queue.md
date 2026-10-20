---
id: research-acquisition-queue
created: 2026-10-20
updated: 2026-10-20
tags: [research, acquisition]
---

# Research acquisition queue

This is the standing queue of sources that research engagements could not fetch. It is
append-only, with one section per source; merge `Completes` when another engagement needs the
same source. `plugins/agentic-research/scripts/refresh-scan.py` re-probes the entries and prints
a worklist, and the operator triages them. Accepted re-acquisitions drive the orchestrator's
refresh branch.

Promoted 2026-10-20 with Andrew's approval, from
`.research/analysis/campaigns/solution-space-decomposition/acquisitions.md`. The enriching
candidates stay in that manifest until promoted.

## Siebert & Keeney 2015 (full text)

- **Source:** Siebert J., Keeney R. L., "Creating More and Better Alternatives for Decisions Using Objectives", Operations Research 63(5):1144–1158, 2015, doi 10.1287/opre.2015.1411 — https://doi.org/10.1287/opre.2015.1411
- **Handle:** siebert-keeney-alternatives-2015
- **Class:** primary-doc
- **Web availability:** blocked (publisher 403 and bot challenge; repository record without file)
- **Urgency:** blocking
- **Completes:** solution-space-decomposition: the five study designs, stimulus conditions and effect sizes now held at abstract and press-release depth (decision-option-generation §1.1; generation cluster §2.3; parent §2 and §5 recommendation 1)

## Gettys, Pliske, Manning & Casey 1987

- **Source:** "An evaluation of human act generation performance", Organizational Behavior and Human Decision Processes 39(1), 1987
- **Class:** primary-doc
- **Web availability:** paywalled (ScienceDirect 403; DTIC mirror unavailable)
- **Urgency:** blocking
- **Completes:** solution-space-decomposition: the option-tree completeness measure and the overconfidence-in-completeness claim, held as a cite-through via delmissier-option-generation-ideation-2015
