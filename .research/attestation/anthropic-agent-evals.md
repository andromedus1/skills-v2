---
source_handle: anthropic-agent-evals
fetched: 2026-10-18
source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
provenance: source-direct
---

# Demystifying evals for AI agents

## Source structure and scope
Engineering guidance published 2026-01-09. It describes evaluation structure
and grader tradeoffs rather than certifying any particular agent workflow.

## Anchored details
- **The structure of an evaluation:** an outcome is the final environment state,
  distinct from an agent's transcript claim; a task has explicit success criteria.
- **Types of graders for agents:** code, model and human graders have different
  strengths; model grading is nondeterministic and needs human calibration.
- **Capability vs. regression evals:** improvement targets and protection against
  loss of existing capabilities serve different purposes.
