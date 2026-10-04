# Human Control and Workflow Reliability · Architect · R / E / L

> **Exam note:** Human-control and reliability practices are sound architecture principles; exact exam coverage is unverified.

## 1. In one line
Reliable agent workflows constrain risky actions, surface uncertainty, and recover safely when tools, models, or assumptions fail.

## 2. Problem it solves
- **Without controls:** a plausible but wrong model decision can trigger an irreversible or unauthorized action.
- **With controls:** application-enforced policies, human approvals, bounded recovery, and verification limit impact and make failures diagnosable.

## 3. 30-second control flow
```text
Proposed action -> validate inputs -> authorize actor/resource
  -> low risk: execute within limits
  -> elevated risk: request human approval
  -> denied / ambiguous / unavailable: do not execute; explain or escalate
  -> verify outcome -> record audit event
```

## 4. Mental model
The model recommends; deterministic controls decide whether the recommendation may be executed.

## 5. Under the hood
1. Classify actions by impact, reversibility, data sensitivity, and scope.
2. Enforce authentication, authorization, limits, and required approvals in the host or service boundary.
3. Use hooks for deterministic event-triggered checks where supported; understand exactly which lifecycle event occurs before or after the action.
4. Define retryable vs. non-retryable errors. Retry only when safe and bounded.
5. Verify the system-of-record result, then record decision, actor, approval, action ID, and outcome with appropriate data minimization.

Claude Code hooks and Claude Agent SDK hooks are not interchangeable by name. Check the exact product and SDK version before relying on hook events or control behavior.

## 6. Variants and when to use
| Control | Use when | Trade-off |
|---|---|---|
| Human approval | High impact, ambiguous, sensitive, or irreversible action | Adds latency and review load |
| Hard policy gate | Action must never violate a rule | Requires policy ownership and testing |
| Reversible/limited action | Automating low-risk work | Still needs bounds, audit, and recovery |
| Escalation | Missing evidence, policy conflict, low calibrated confidence | Human capacity and response time become dependencies |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Relying on prompt instructions for authorization | Model output can ignore or misapply instructions | Check permissions in the executing application/service |
| Retrying a write blindly | Duplicate side effects may occur | Use idempotency keys or query state before retry |
| Treating confidence text as calibrated probability | Fluent certainty can be misleading | Calibrate on representative data; use explicit evidence and thresholds |
| Hook configured after an action | It cannot prevent what has already occurred | Choose a pre-action enforcement point when prevention is required |
| Escalation without a useful packet | Human must repeat investigation | Include concise context, evidence, uncertainty, and proposed next action |

## 8. Performance, memory, and concurrency
- **Latency:** approvals and checks add time; place them at meaningful risk gates rather than every harmless step.
- **Concurrency:** deduplicate approvals and writes; protect shared resources with transactional or service-level controls.
- **Observability:** track approval wait time, denial, retries, duplicate prevention, failures, and verified outcomes.
- **Testing:** inject tool timeouts, permission denials, ambiguous inputs, duplicate requests, and approval rejection.

## 9. Related topics map
- **Prerequisites:** tool execution lifecycle, risk classification, authorization
- **Siblings:** hooks, retries, human handoff, failure propagation
- **Downstream:** incident response, auditability, production operations
- **Contrasts:** model-only guardrail, fully manual workflow, unrestricted autonomy
- **Tools/frameworks:** Claude Code hooks; application policy/approval services

## 10. Cross-domain equivalents
| Concern | Reliability/control concept | Related topic |
|---|---|---|
| Pre-action boundary | Permission/policy check | Tool security |
| Deterministic event | Hook | Claude Code configuration |
| Uncertainty pathway | Human handoff | Prompt and confidence routing |
| Safe retry | Idempotent operation | Reliability engineering |

## 11. Interview lens
- **30-second answer:** I classify actions by impact and reversibility, enforce permissions outside the prompt, require approval at risk thresholds, retry only safe operations, and verify/audit the resulting system state.
- **Q1 → What should trigger a human?** High impact, missing/contradictory evidence, policy ambiguity, low validated confidence, or a control/tool failure that makes safe automation impossible.
- **Q2 → Is a hook always a safety control?** No. Its event timing, output, and blocking semantics matter; it may observe after the action rather than prevent it.
- **Spot the bug:** Retry `POST /refund` after a timeout because no response arrived.  
  **Problem:** the refund may have succeeded despite the timeout. **Fix:** use an idempotency key or reconcile transaction state before retry.

## 12. Architect lens
- Define risk tiers, thresholds, approval owner, fail-closed/fail-open policy, and evidence retained.
- Keep safety claims proportional to tested controls; no single prompt, hook, or confidence score guarantees correctness.
- **Version note:** hook events and blocking semantics are product/version-specific.

## 13. Revision summary
- Prompts guide; application controls enforce.
- Gate high-impact and irreversible actions.
- Retry only with explicit safety semantics.
- Escalate uncertainty with evidence.
- **If you remember only one thing:** Never let an unverified model statement stand in for authorization or proof of execution.

## 14. Coverage self-check
- [ ] Can I place controls before the risky action?
- [ ] Can I explain approval, denial, timeout, retry, and escalation paths?
- [ ] Can I make a write idempotent and verify its outcome?
- [ ] Can I distinguish Claude Code hooks from other SDK hooks?

## Sources
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code memory and controls](https://code.claude.com/docs/en/memory)
- [Claude API tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
