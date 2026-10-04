# Domain 1 · Agentic Architecture & Orchestration

**Study status:** Strong alignment with public Claude product documentation; exam coverage and weight are unverified.

## Topic sequence

| # | Topic | Architect outcome |
|---|---|---|
| 1 | [Agent loop and tool-use lifecycle](./01-agent-loop-and-tool-use-lifecycle.md) | Explain the model/application loop and completion vs. tool handoff. |
| 2 | [Decomposition and subagent delegation](./02-decomposition-and-subagent-delegation.md) | Choose boundaries and coordinate isolated workers safely. |
| 3 | [Human control and workflow reliability](./03-human-control-and-workflow-reliability.md) | Handle approvals, hooks, errors, recovery, and verification. |

## Design lens

Prefer the simplest workflow that meets the requirement. Delegate when work is separable and context isolation or specialization is useful—not merely because multiple agents are available. Keep permissions and irreversible actions under deterministic application controls.

## Quick oral drill

For a research agent that fans out to three sources: what is independent, what must be synthesized centrally, how do you handle one failed worker, and what evidence do you retain?
