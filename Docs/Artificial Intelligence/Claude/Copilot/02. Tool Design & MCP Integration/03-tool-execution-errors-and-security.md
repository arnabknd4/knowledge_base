# Tool Execution, Errors, and Security · Architect · R / E / L

> **Exam note:** The controls below are architecture guidance; exam emphasis is unverified.

## 1. In one line
Safe tool use requires controlled execution, meaningful error semantics, least privilege, and independent verification of consequential effects.

## 2. Problem it solves
- **Without an execution boundary:** a model-generated request can become an unsafe action or expose data.
- **With a boundary:** the host/server validates, authorizes, executes, and reports outcomes under explicit policy.

## 3. 30-second execution contract
```text
tool request
 -> parse + schema validate
 -> authenticate + authorize resource/action
 -> apply limits / approval / idempotency
 -> execute with timeout
 -> return success data OR typed error
 -> agent decides next step; application verifies writes
```

## 4. Mental model
Treat model-originated tool arguments as untrusted input, even when they are schema-valid and appear in the assistant's own response.

## 5. Under the hood
1. Validate syntax and business invariants independently.
2. Authorize the current user and agent for the specific resource/action at execution time.
3. Apply output filtering, rate limits, timeout, idempotency, and human approval based on action risk.
4. Distinguish recoverable/transient failures from validation, permission, not-found, and permanent errors; for MCP, interpret the protocol error indication (such as `isError`) according to the relevant result type.
5. Return machine-readable error/result information; avoid inventing success-shaped fallbacks.
6. For writes, query or otherwise verify the external system's resulting state.

## 6. Variants and when to use
| Error/control strategy | Use when | Trade-off |
|---|---|---|
| Retry transient read | Network/service may recover | Adds delay; cap attempts and use backoff |
| Idempotent write retry | Operation supports stable deduplication key | Requires downstream support and key lifecycle |
| Human approval | Impact or uncertainty exceeds policy threshold | Slower; requires clear reviewer context |
| Fail closed | Unauthorized or unsafe action | May reduce availability, protects integrity |
| Degraded read-only mode | Safe subset remains useful during outage | Must clearly communicate reduced capability |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Catch-all error returns `{"success": true}` | Hides failure and misleads next model turn | Return explicit typed failure and stop/recover appropriately |
| Retry all errors | Repeats invalid or unauthorized requests | Classify error; retry only known transient/safe cases |
| Shell or broad admin access by default | High blast radius and injection risk | Narrow capability, sandbox, allowlist, permissions, approval |
| Trusting tool output as instructions | External content may be malicious or irrelevant | Treat retrieved data as untrusted evidence; constrain follow-on actions |
| Logging credentials or full sensitive payloads | Creates secondary data exposure | Redact, minimize, set retention, restrict log access |

## 8. Performance, memory, and concurrency
- **Performance:** timeout budgets should cover tool and model round trips; expose latency and error type.
- **Concurrency:** rate-limit fan-out; avoid concurrent writes to the same entity without transactional protection.
- **Reliability:** use circuit breaking or degraded behavior where justified; do not let fallback fabricate a result.
- **Testing:** fault-inject timeout after commit, duplicate request, permission denial, malformed response, and partial success.

## 9. Related topics map
- **Prerequisites:** tool schema, API lifecycle, identity model
- **Siblings:** MCP architecture, human approval, structured output
- **Downstream:** incident response, idempotency, audit and provenance
- **Contrasts:** model-only policy, blind retry, optimistic success fallback
- **Tools/frameworks:** Claude API tool handling; MCP server; Claude Code permissions/hooks

## 10. Cross-domain equivalents
| Security/reliability control | Enforced at |
|---|---|
| Input shape | Schema and host validator |
| User/resource authorization | Application/service of record |
| Tool availability | Host capability/permissions |
| Error semantics | Tool adapter + orchestrator |
| Write confirmation | External system postcondition |

## 11. Interview lens
- **30-second answer:** I treat tool input and returned data as untrusted, enforce authorization at the service boundary, classify errors, retry only safe transient operations, and verify writes from the system of record.
- **Q1 → Should the model decide user authorization?** No. The authenticated application/service enforces it.
- **Q2 → What if a write times out?** The outcome is unknown; reconcile using an idempotency key or transaction lookup before retrying.
- **Spot the bug:** On MCP timeout, return `"Refund completed"` so the conversation can continue.  
  **Problem:** a timeout does not prove completion. **Fix:** return an explicit unknown/pending state and reconcile before claiming success.

## 12. Architect lens
- Use defense in depth: identity, scoped capability, validation, policy, approval, execution, verification, audit.
- Define failure states so the model can recover without receiving secrets or misleading success signals.
- **Version note:** error fields and MCP/tool result semantics differ by API and protocol surface; use the relevant reference.

## 13. Revision summary
- Tool inputs and outputs are untrusted.
- Authorization belongs at execution boundary.
- Retry only classified, bounded, safe operations.
- Unknown outcome is not success.
- **If you remember only one thing:** A timeout after a side effect requires reconciliation, not blind retry.

## 14. Coverage self-check
- [ ] Can I classify errors and set retry policy?
- [ ] Can I secure read and write tools with least privilege?
- [ ] Can I explain timeout-after-commit and idempotency?
- [ ] Can I verify a side effect independently?

## Sources
- [Claude API tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [MCP security considerations](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
