# Domain 5 · Context Management & Reliability

**Study status:** Strong alignment with public Claude product documentation; exam coverage and weight are unverified.

## Topic sequence

| # | Topic | Architect outcome |
|---|---|---|
| 1 | [Context lifecycle and memory boundaries](./01-context-lifecycle-and-memory-boundaries.md) | Know what context is available, isolated, and persistent. |
| 2 | [Context budgets, caching, and provenance](./02-context-budgets-caching-and-provenance.md) | Spend context deliberately without losing evidence. |
| 3 | [Reliability, recovery, and observability](./03-reliability-recovery-and-observability.md) | Operate workflows safely through failures and retries. |

## Design lens

Context is an input budget, not durable truth or guaranteed memory. Retain the evidence and uncertainty needed for the next decision; use application persistence and controls for durable state and consequential actions.

## Quick oral drill

A long-running workflow resumes after a timeout. What state must be persisted, what may be re-derived, how do you avoid duplicate actions, and how will you verify recovery?
