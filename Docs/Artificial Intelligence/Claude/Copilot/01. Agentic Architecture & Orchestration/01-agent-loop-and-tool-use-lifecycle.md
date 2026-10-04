# Agent Loop and Tool-Use Lifecycle · Architect · R / E / L

> **Exam note:** This is product-grounded preparation. Inclusion on a particular exam is not verified.

## 1. In one line
An agent repeatedly gathers context, chooses an action, observes its result, and verifies whether the goal is complete.

## 2. Problem it solves
- **Without a loop:** a model can only propose text; it cannot observe changing application state or act on external systems.
- **With a loop:** the application supplies tools and results so the model can make context-informed next decisions.

## 3. 30-second architecture sketch
```text
User goal
  -> model response
      -> final response: stop
      -> tool request: validate -> authorize -> execute -> return result
  -> model observes result and continues
  -> application verifies outcome and responds
```
This is a conceptual flow, not an API transcript. Exact response fields and stop reasons depend on the API/product in use.

## 4. Mental model
The model proposes the next step; the application owns execution, policy enforcement, and the truth about whether an external action succeeded.

## 5. Under the hood
1. The host sends instructions, conversation state, and available tool definitions to the model.
2. The model may return text, a structured tool call, or another non-final response.
3. For client-executed tools, the host validates and authorizes the request, runs it, and returns a tool result. Some server tools execute on Anthropic infrastructure instead.
4. The model consumes the result and may call another tool or finish.
5. The application checks termination, errors, limits, and any required postcondition; it must not infer success solely from a confident final sentence.

## 6. Variants and when to use
| Pattern | Use when | Trade-off |
|---|---|---|
| One model/tool loop | A task needs adaptive selection among a small tool set | Flexible, but requires explicit limits and controls |
| Deterministic workflow | Steps and branching rules are known in advance | Easier to test and audit; less adaptive |
| Hybrid | Model interprets/chooses; code enforces transitions and permissions | Strong control with some flexibility; more integration work |
| Server tool | Anthropic-hosted capability is suitable | Less client execution work; availability and behavior are service-defined |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Treating model output as execution | A request to call a tool is not proof it ran | Execute through a controlled host and return the actual result |
| Assuming one fixed `observe → think → act → respond` sequence | Real loops can repeat, stop, fail, or be interrupted | Model the loop as iterative and handle each response type |
| Unbounded tool loop | Cost, latency, and repeated side effects can grow | Set step/time/token limits, cancellation, and safe stop behavior |
| Trusting the final answer as proof | The model may misunderstand a result | Verify using system state or an independent postcondition |

## 8. Performance, memory, and concurrency
- **Performance:** each model turn and tool call adds latency; batch independent reads only where the API and workflow permit.
- **Concurrency:** parallel tool calls can reduce latency but require correlation, bounded fan-out, and explicit handling of partial failure.
- **Observability:** record request/response IDs, tool names, validated outcomes, latency, and stop/error categories without indiscriminately logging sensitive content.

## 9. Related topics map
- **Prerequisites:** API messages, tool schemas, authorization boundaries
- **Siblings:** subagents, orchestration, human approvals, structured outputs
- **Downstream:** recovery, evaluation, audit trail, user-facing result
- **Contrasts:** single-shot generation, deterministic state machine
- **Tools/frameworks:** Claude Messages API tool use; Claude Code agentic loop

## 10. Cross-domain equivalents
| Concern | This topic | Related design |
|---|---|---|
| Action contract | Tool request/result | MCP tool or Claude Code tool |
| Control | Host validates and authorizes | Permissions, hooks, application policy |
| Completion | Stop/continue/error | Workflow state and postcondition |

## 11. Interview lens
- **30-second answer:** The agent loop lets the model adapt based on tool results, but the host—not the model—executes client tools, enforces policy, limits the loop, and verifies consequential outcomes.
- **Q1 → Is a tool call the same as a tool result?** No. A call is a request; execution and a returned result are separate steps.
- **Q2 → When should the loop stop?** On validated completion, an explicit limit, cancellation, unrecoverable failure, or a required human handoff.
- **Spot the bug:** `if (response.text.includes("Done")) markPaymentComplete();`  
  **Problem:** text is not evidence of payment state. **Fix:** query the payment system and confirm a stable transaction result.

## 12. Architect lens
- **Boundary:** model reasoning vs. host execution vs. external system of record.
- **Control:** authorize every action at execution time; prompts are not access control.
- **Version note:** stop reasons, tool response fields, and tool types are API/product-specific; use the matching current reference.

## 13. Revision summary
- The agent loop is iterative and result-driven.
- Tool calls are requests; the host controls client-side execution.
- Completion requires a verified postcondition for important actions.
- Bound loops, parallelism, and retries.
- **If you remember only one thing:** Model judgment can select actions; application code must enforce and verify them.

## 14. Coverage self-check
- [ ] Can I draw request → tool handoff → result → continuation/final?
- [ ] Can I distinguish client tools from hosted/server tools?
- [ ] Can I explain stop, error, cancellation, and verification behavior?
- [ ] Can I bound cost and side effects?

## Sources
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude API tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
