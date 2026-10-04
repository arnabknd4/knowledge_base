# Claude Architect Foundations · Study Pack

> **Scope note:** This pack follows the five-domain study map in [Exam-syllabus-aligned.md](../Exam-syllabus-aligned.md). The map is product-document-aligned, but no first-party exam blueprint was verified. These notes are architect-level preparation, not a promise of exam coverage. Verify exam facts and version-sensitive product behavior against official sources.

## How to use this pack

1. Read each domain map, then work through its topic notes in order.
2. For each pattern, identify the system boundary, the failure mode, and the control that prevents or detects it.
3. Practice explaining trade-offs, not just defining features. A strong architecture answer states the requirement, options, decision, failure handling, and verification.
4. Complete the capstone without looking at the notes; then use the domain checklists to find gaps.

The coding-topic template was adapted: runnable language examples and cross-language comparisons do not fit this Claude architecture syllabus. Notes instead use architecture flows, request/tool pseudocode, decision tables, scenario drills, and cross-domain links.

## Domains

| # | Domain | Start here |
|---|---|---|
| 1 | Agentic Architecture & Orchestration | [Domain map](./01.%20Agentic%20Architecture%20%26%20Orchestration/README.md) |
| 2 | Tool Design & MCP Integration | [Domain map](./02.%20Tool%20Design%20%26%20MCP%20Integration/README.md) |
| 3 | Claude Code Configuration & Workflows | [Domain map](./03.%20Claude%20Code%20Configuration%20%26%20Workflows/README.md) |
| 4 | Prompt Engineering & Structured Output | [Domain map](./04.%20Prompt%20Engineering%20%26%20Structured%20Output/README.md) |
| 5 | Context Management & Reliability | [Domain map](./05.%20Context%20Management%20%26%20Reliability/README.md) |

## Architect practice loop

For any scenario, answer these in order:

1. **Outcome:** What must the system do, and how will success be measured?
2. **Boundary:** What belongs in the model, application, tool/MCP server, or human workflow?
3. **Control:** Which actions are allowed, validated, approved, or denied?
4. **Context:** What evidence does each step need, and what can be summarized or isolated?
5. **Failure:** What happens on timeout, malformed output, tool error, ambiguity, or partial completion?
6. **Verification:** What independent check establishes that the requested outcome actually occurred?
7. **Operations:** What do we log, evaluate, alert on, and retain?

## Capstone: customer-support resolution agent

Design an agent that answers policy questions, looks up an order, and may prepare—but not automatically issue—a refund above a defined threshold.

- Use a read-only policy/order lookup before any action.
- Keep the refund decision criteria explicit and return evidence or an uncertainty state.
- Separate proposed action from execution; require approval where the impact threshold demands it.
- Define typed tool inputs/results, authorization by customer/order, and structured tool failures.
- Bound tool retries; make any execution operation idempotent and record its result.
- Preserve the policy/order evidence and provenance in the final response.
- Route missing identity, conflicting policy, low-confidence classification, or tool outage to a human.
- Evaluate representative success, refusal, ambiguity, and failure cases before release; monitor after deployment.

**Review question:** Which single design change would you make if the agent must now issue small refunds automatically? Explain its authorization, risk limit, idempotency, audit, and rollback implications.

## Readiness self-check

- [ ] I can describe an end-to-end agent/tool/MCP request without conflating their responsibilities.
- [ ] I can justify when to use one agent, a subagent, a deterministic workflow, or a human.
- [ ] I can design tool schemas, permissions, error behavior, and output validation.
- [ ] I can distinguish Claude Code instructions from enforceable controls.
- [ ] I can produce schema-valid output and separately validate its meaning and evidence.
- [ ] I can manage context, provenance, retries, timeouts, idempotency, and observability.
- [ ] I can state what is documented product behavior versus an unverified exam assumption.
