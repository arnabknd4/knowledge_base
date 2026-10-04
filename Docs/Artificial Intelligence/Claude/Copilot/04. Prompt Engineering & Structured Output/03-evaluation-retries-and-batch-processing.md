# Evaluation, Retries, and Batch Processing · Architect · R / E / L

> **Exam note:** Evaluation/retry patterns are general architecture guidance. Message Batches is a documented API feature, but its exam relevance is not verified.

## 1. In one line
Evaluation measures task quality, bounded retries recover from correctable failures, and batch processing serves independent asynchronous workloads.

## 2. Problem it solves
- **Without evaluation:** teams cannot tell whether a prompt/model change improved real outcomes.
- **Without retry policy:** transient failures either terminate useful work or create unbounded cost and duplicate effects.
- **Without workload fit:** synchronous calls may be wasteful for large jobs that do not need immediate answers.

## 3. 30-second decision flow
```text
Define metric + test set -> evaluate baseline -> change one factor -> compare
Runtime failure?
  transient + safe/idempotent -> bounded retry with backoff
  invalid/ambiguous -> repair input or request review
  permanent/unsafe -> stop and surface explicit failure
Many independent requests, no immediate response needed?
  -> consider asynchronous batch; track, poll, reconcile results
```

## 4. Mental model
Evaluation improves the system before release; retry handles a known runtime failure class; batching changes workload scheduling, not answer quality.

## 5. Under the hood
1. Build representative evaluations that cover expected inputs, edge cases, refusals, ambiguity, and failure.
2. Measure more than format: task correctness, evidence support, routing, safety, latency, cost, and human-review rate.
3. Compare prompt/model/tool changes against a baseline and inspect regressions qualitatively.
4. At runtime, classify failures and retry only if transient, bounded, and safe; preserve attempt correlation.
5. For asynchronous bulk work, use the Message Batches API when its delayed results and lifecycle suit the task; track batch state and reconcile per-request outcomes.

## 6. Variants and when to use
| Technique | Use when | Trade-off |
|---|---|---|
| Offline eval set | Prompt/model/tool changes need regression measurement | May not represent production drift |
| Online monitoring | Need post-release quality/operations signals | Privacy, sampling, and attribution matter |
| Bounded retry | Known transient or correctable failure | Added latency/cost; can amplify load |
| Message Batches | Large independent requests without immediate result requirement | Asynchronous lifecycle; not a real-time interaction |
| Multi-pass review | High-value output benefits from independent checking | More calls; not a guarantee against shared blind spots |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Evaluating only JSON validity | Measures syntax, not task correctness | Include semantic/evidence/human-review metrics |
| Tuning and testing on same examples | Overstates generalization | Hold out cases and expand evaluation with production-like failures |
| Retrying all model/tool errors | Loops, costs, and repeated side effects | Classify failure, cap attempts, use backoff and idempotency |
| Treating batch as parallel synchronous calls | Misses asynchronous status/result lifecycle | Track batch/request IDs and poll/reconcile according to current API |
| Assuming multiple review passes eliminate error | Reviewers/model can share blind spots | Add independent evidence or external checks for critical claims |

## 8. Performance, memory, and concurrency
- **Performance:** retries multiply latency and request volume; use deadlines and avoid retry storms.
- **Concurrency:** batch requests are independently processed; preserve per-request IDs and tolerate partial/error outcomes.
- **Observability:** track eval version, model/prompt version, attempt count, batch state, per-item result, cost, and latency.
- **Testing:** inject throttling, transient outage, invalid output, permanent denial, batch expiry/partial failure, and duplicate submission.

## 9. Related topics map
- **Prerequisites:** success criteria, structured output, tool error taxonomy
- **Siblings:** multi-pass review, prompt chaining, observability
- **Downstream:** release decision, incident recovery, bulk data pipeline
- **Contrasts:** retry vs. evaluation; batch vs. interactive call; confidence vs. correctness
- **Tools/frameworks:** Claude eval approach; Message Batches API; application retry policy

## 10. Cross-domain equivalents
| Need | LLM workflow analogue | Conventional system analogue |
|---|---|---|
| Quality measurement | Prompt/model evaluation | Regression suite |
| Correctable transient fault | Bounded retry | Retry/backoff policy |
| Bulk delayed processing | Message Batches | Asynchronous job queue |
| Output audit | Evidence and reviewer checks | Business validation |

## 11. Interview lens
- **30-second answer:** I test changes against representative held-out cases, measure semantic and operational outcomes, retry only classified safe failures with limits, and use asynchronous batching only when the user does not need an immediate response.
- **Q1 → Is a valid response a successful eval?** Not necessarily; correctness and grounding must be measured.
- **Q2 → Should a batch be used for support chat?** Usually not if the user expects a synchronous answer; batch is for suitable asynchronous independent requests.
- **Spot the bug:** Retry every failed payment/refund call three times.  
  **Problem:** failure may occur after commit, creating duplicates. **Fix:** classify the error and reconcile via idempotency/state before retry.

## 12. Architect lens
- Establish release thresholds and owners; keep eval data protected and versioned.
- Track asynchronous request lifecycle, cancellation/expiry, and item-level outcomes.
- **Version note:** batch limits, pricing, supported features, and retry recommendations change; check current API docs.

## 13. Revision summary
- Evaluate task quality, not only formatting.
- Retries need error classification, limits, and safe semantics.
- Batches are asynchronous bulk processing, not prompt engineering.
- Multiple passes do not prove correctness.
- **If you remember only one thing:** Choose the mechanism for the failure/workload; do not use retries or batching as a substitute for evaluation.

## 14. Coverage self-check
- [ ] Can I define quality metrics and representative evaluation cases?
- [ ] Can I classify retryable vs. permanent/unsafe failures?
- [ ] Can I handle duplicate side effects and retry storms?
- [ ] Can I explain when batch processing is appropriate?

## Sources
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
