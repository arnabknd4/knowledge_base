# Decomposition and Subagent Delegation · Architect · R / E / L

> **Exam note:** This is product-grounded preparation. Specific orchestration patterns or exam coverage are not verified.

## 1. In one line
Decomposition turns a broad goal into bounded tasks; delegation assigns suitable tasks to isolated workers and integrates their evidence.

## 2. Problem it solves
- **Without decomposition:** one agent may mix research, decisions, and actions in an oversized context with unclear ownership.
- **With decomposition:** independent work can be specialized or parallelized, with explicit inputs, outputs, and integration checks.

## 3. 30-second architecture sketch
```text
Goal -> coordinator defines subtasks + contracts
     -> worker A: independent source research
     -> worker B: independent source research
     -> coordinator checks evidence, reconciles conflicts, decides
     -> verified answer with provenance
```
Workers must not receive broader permissions or sensitive data than their assignment requires.

## 4. Mental model
Delegation is a controlled API boundary between workers: task, context, permission, result contract, and failure status must all be explicit.

## 5. Under the hood
1. Decompose by separable outcomes, not merely by file, topic count, or desire for parallelism.
2. Give each worker a bounded task, relevant context, permitted tools, and expected result format.
3. Use parallel execution only where tasks do not depend on one another; sequence dependent work.
4. Treat worker summaries as claims requiring evidence and integration—not as ground truth.
5. The coordinator resolves conflicts, checks completeness, handles missing/failed work, and owns the final response.

## 6. Variants and when to use
| Pattern | Use when | Trade-off |
|---|---|---|
| Sequential chain | Later task depends on earlier result | Clear dependencies; longer wall-clock time |
| Parallel fan-out/fan-in | Tasks are independent and mergeable | Lower latency; partial failures and conflicts need handling |
| Coordinator/worker | Central policy, synthesis, or user interaction is needed | Central control; coordinator can bottleneck |
| Single agent | Task is small or tightly coupled | Simpler state and fewer handoffs |
| Deterministic orchestration | Transitions and gates are known | More predictable; less flexible for open-ended tasks |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Parallelizing dependent steps | Workers race or use stale assumptions | Encode dependencies; sequence dependent tasks |
| Vague worker assignment | Overlap, gaps, incompatible outputs | Specify scope, evidence, exclusions, output schema |
| Passing the full conversation everywhere | Wastes context and may leak unrelated data | Minimize and purpose-limit context |
| Trusting the summary alone | Uncertainty and source conflicts disappear | Return citations/evidence and have coordinator validate |
| No partial-failure plan | One worker timeout stalls or corrupts synthesis | Define timeout, retry, degraded result, or human escalation |

## 8. Performance, memory, and concurrency
- **Performance:** parallelism reduces wall time only if coordination and model/tool capacity do not dominate; it can increase total tokens and cost.
- **Context:** isolated subagent context limits main-session noise, but requires careful context handoff.
- **Concurrency:** use bounded fan-out, stable task IDs, cancellation, and deterministic aggregation; do not let concurrent workers perform conflicting writes.
- **Testing:** evaluate incomplete worker sets, contradictory findings, duplicate work, and coordinator omission.

## 9. Related topics map
- **Prerequisites:** agent loop, task success criteria, tool permissions
- **Siblings:** human handoff, session state, context compaction
- **Downstream:** synthesis, reliability, provenance, evaluation
- **Contrasts:** monolithic agent, fixed pipeline, decentralized peer mesh
- **Tools/frameworks:** Claude Code subagents; application-level agent orchestration

## 10. Cross-domain equivalents
| Concern | Delegation design | Related area |
|---|---|---|
| Task contract | Worker instructions and output | Tool input/output schema |
| Context isolation | Separate worker context | Context-window management |
| Permission scope | Worker tool access | MCP/Claude Code security |
| Aggregation | Coordinator synthesis | Structured output and provenance |

## 11. Interview lens
- **30-second answer:** I delegate only separable work, pass minimum sufficient context and permissions, require evidence-backed outputs, bound parallelism, and make the coordinator handle conflicts and partial failure.
- **Q1 → When not to use subagents?** For small, tightly coupled work or when coordination cost, privacy, or consistency outweighs context isolation.
- **Q2 → How do you parallelize safely?** Split independent reads/research; serialize shared writes and dependent decisions; aggregate using an explicit contract.
- **Spot the bug:** Three workers each update the same customer record, then the coordinator accepts the last write.  
  **Problem:** race and uncontrolled side effects. **Fix:** keep workers read-only; centralize validated writes behind authorization and idempotency.

## 12. Architect lens
- **Choice criteria:** coupling, separability, data sensitivity, latency, cost, permissions, and merge complexity.
- **Failure semantics:** distinguish failed, timed-out, partial, and successful worker results.
- **Version note:** Claude Code subagents and Agent SDK/application orchestrators are distinct surfaces; verify each API's current semantics.

## 13. Revision summary
- Decompose around independent outcomes and explicit contracts.
- Parallelize independent work; sequence dependencies.
- Isolate context and scope permissions.
- Integrate evidence and handle partial failures explicitly.
- **If you remember only one thing:** A coordinator is responsible for verifying what its workers return.

## 14. Coverage self-check
- [ ] Can I justify single agent vs. sequential vs. parallel vs. delegated design?
- [ ] Can I specify a worker contract and least-privilege tool scope?
- [ ] Can I handle timeout, conflict, incomplete result, and synthesis?
- [ ] Can I explain cost and context trade-offs?

## Sources
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code feature overview](https://code.claude.com/docs/en/features-overview)
