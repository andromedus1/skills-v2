---
id: idea-methodology-research-depth
created: 2026-10-12
updated: 2026-10-12
tags: [methodology-review, research-pipeline]
---

# Assess adaptive research depth in methodology-review

Andrew asked whether methodology-review should explicitly use the research skills'
fractal approach: decompose a topic, research its parts, orchestrate the work,
synthesize the results and evaluate them. Assess the three scales as appropriate
to the question. The current skill reads as leaning heavily on Scout.

Assess this before the first project pilot. Keep the operator's adjudication of
project changes and decisions from the existing review loop. This is a captured
refinement question, not an active implementation commission or a research run.

## Current context

The initial skill implementation is committed on `feat/methodology-review` through
`17ccdde2`; it has not been released or installed. Its
[research step](../../plugins/research-pipeline/skills/methodology-review/SKILL.md#2-research-and-compare)
already delegates comparison to Agentic Research and mentions program coordination,
but the methodology-specific choice of research scale and synthesis responsibilities
is implicit.

The current [research composition](../../plugins/research-pipeline/docs/research-composition.md)
uses one authoritative Agentic Research engine. Focused inquiries, decomposed
specialist campaigns and programs are available execution shapes; verification
rigor is a separate control. Scout maps the landscape;
[deep-research](../../plugins/research-pipeline/skills/deep-research/SKILL.md)
commissions a multi-facet campaign, while
[research-program](../../plugins/research-pipeline/skills/research-program/SKILL.md)
coordinates separately registered engagements and a separately registered cross-arc
synthesis. Agentic Research owns decomposition and its research roles.

Read the installed research orchestrator and its evaluator/specialist role briefs
when assessing the change. Repository instructions reserve the research engine to
Agentic Research; evaluate how methodology-review should commission that engine
and expose its results rather than copying it into Research Pipeline. The skill's
project reassessment and the research engine's isolated synthesis evaluation have
different purposes and inputs; preserve that distinction when deciding the routing.
