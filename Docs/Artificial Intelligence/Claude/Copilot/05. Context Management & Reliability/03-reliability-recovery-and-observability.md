# Reliability, Recovery, and Observability · Architect · R / E / L

> **Exam note:** These are cross-cutting architecture practices; exact exam coverage is unverified.

## 1. In one line
Reliable agent systems make failures visible, bound recovery, prevent duplicate effects, and verify outcomes using observable evidence.

## 2. Problem it solves
- **Without reliability design:** tool outages, timeouts, malformed output, or partial completion can become silent incorrect success.
- **With explicit recovery:** each state has a safe next action, including retry, reconcile, degrade, stop, or escalate.

## 3. 30-second recovery state machine
```text
START -> execute -> verified success -> COMPLETE
                    |
             timeout / error
              /      |       \
      safe transient  unknown  permanent/unsafe
          retry      reconcile    stop/escalate
```

## 4. Mental model
An agent workflow is a distributed system with probabilistic decisions at some steps; apply explicit state, deadlines, idempotency, and observability.

## 5. Under the hood
1. Assign workflow/request IDs and persist the minimum state needed to resume.
2. Set deadlines, token/tool-call budgets, bounded retries, cancellation, and clear terminal states.
3. Classify errors by layer: model/API, tool transport, authorization, business validation, and external system.
4. For uncertain write outcomes, reconcile by idempotency key or system-of-record query before retry.
5. Verify completion with explicit postconditions; distinguish completed, partial, pending, rejected, and unknown.
6. Emit privacy-aware traces/metrics/events sufficient to diagnose failures and measure quality.

## 6. Variants and when to use
| Strategy | Use when | Trade-off |
|---|---|---|
| Retry with backoff | Transient failure and safe operation | More latency; must avoid retry amplification |
| Idempotency key | Write may be retried after uncertainty | Key handling/downstream support needed |
| Checkpoint/resume | Long workflow or expensive progress | State schema/version migration needed |
| Degraded mode | Safe subset can continue | Must communicate limitations clearly |
| Human escalation | Policy, evidence, or recovery path is uncertain | Adds operational dependency |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Infinite model/tool retries | Unbounded cost and repeated effects | Attempt/deadline caps and explicit stop state |
| Treating timeout as failure | External action may have committed | Record unknown outcome and reconcile |
| Logging full prompts/results by default | Sensitive data persists in observability systems | Redact/minimize and enforce retention/access controls |
| No trace correlation across agents/tools | Root cause and ownership are unclear | Propagate workflow/task/call IDs and parent relationships |
| Declaring success from model text | Misses partial or failed external action | Verify system-of-record postcondition |

## 8. Performance, memory, and concurrency
- **Performance:** monitor end-to-end latency by model/tool stage; set per-stage deadlines and an overall budget.
- **Concurrency:** cap fan-out, use cancellation, handle partial results, and protect shared writes.
- **Observability:** measure completion/partial/unknown rates, tool errors, retries, human handoffs, latency, cost, and evaluated quality.
- **Testing:** chaos/fault tests for model/API outage, tool timeout after commit, duplicate delivery, invalid response, cancellation, and resume from stale checkpoint.

## 9. Related topics map
- **Prerequisites:** agent loop, state persistence, error taxonomy
- **Siblings:** context lifecycle, human control, tool security, eval
- **Downstream:** SLOs, incident response, audit, safe rollout
- **Contrasts:** blind retry, silent fallback, prompt-only control
- **Tools/frameworks:** application tracing/metrics; Claude API request IDs; workflow store

## 10. Cross-domain equivalents
| Distributed-system control | Agent workflow application |
|---|---|
| Deadline | Bound model/tool orchestration |
| Idempotency | Safe retry of side effects |
| Checkpoint | Resume from explicit validated state |
| Trace ID | Correlate model, subagent, and MCP calls |
| Postcondition | Verify action actually completed |

## 11. Interview lens
- **30-second answer:** I model explicit workflow states, set end-to-end deadlines and bounded retries, make writes idempotent, reconcile ambiguous outcomes, and instrument each model/tool/human boundary.
- **Q1 → What do you do when the tool times out after a write?** Mark the outcome unknown, reconcile with stable operation identity, and retry only if safe.
- **Q2 → What should you log?** Enough redacted identifiers, events, timing, result/error categories, and version data to diagnose—not unrestricted prompts and secrets.
- **Spot the bug:** On exception, return the last successful-looking result and mark the workflow complete.  
  **Problem:** a partial workflow is mislabeled as success. **Fix:** persist explicit state and surface partial/unknown status with next recovery action.

## 12. Architect lens
- Design SLOs and alerts around user outcomes, not only API uptime.
- Measure quality and safety alongside latency/cost; data retention must match privacy commitments.
- **Version note:** API request metadata and product observability capabilities vary; verify current provider behavior.

## 13. Revision summary
- Make every terminal and partial state explicit.
- Bound work and retries.
- Reconcile uncertain side effects; use idempotency.
- Observe each boundary and verify outcomes.
- **If you remember only one thing:** Unknown is a real state—do not convert it into success or failure without evidence.

## 14. Coverage self-check
- [ ] Can I design recovery for timeout, partial result, denial, and cancellation?
- [ ] Can I explain idempotency and reconciliation?
- [ ] Can I describe safe checkpoint/resume state?
- [ ] Can I define privacy-aware metrics and trace data?

## Sources
- [Claude API tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Claude Code sessions](https://code.claude.com/docs/en/sessions)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
