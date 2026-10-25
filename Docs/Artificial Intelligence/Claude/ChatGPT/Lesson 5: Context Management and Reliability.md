### Lesson 5: Context Management and Reliability

This lesson covers how to provide Claude with the right information, keep its context useful over longer tasks, and design agentic systems that behave predictably when something goes wrong.

The central principle is: More context is not automatically better context. A reliable application supplies relevant information, manages context limits, and handles failure explicitly.

### 1\. Understand the context window

Claude's context window is the amount of information the model can process in a request. Depending on the model and API configuration, this can include:

* System instructions and other prompt instructions.

* The current user message.

* Earlier conversation messages.

* Tool definitions and tool results.

* Documents, retrieved passages, and other supplied data.

The context window is finite. As a conversation or agent workflow grows, earlier messages and large tool results can consume space that would be more useful for the current task.

Consider a support agent that investigates a complex production incident. It has accumulated hundreds of log lines, several tool responses, and a long conversation history. Passing all of that material into every subsequent request may increase cost and latency while making the most relevant evidence harder to distinguish.

The goal is not to preserve every token. It is to preserve the information needed for the next correct decision.

### 2\. Manage context deliberately

Three techniques are especially useful.

Relevance filtering

Retrieve and include the evidence relevant to the current task rather than supplying entire databases, documents, or logs.

Summarisation

Compress earlier work into a concise summary containing the objective, established facts, decisions, unresolved questions, and relevant constraints.

External state and retrieval

Keep durable records or large source material outside the immediate prompt, then retrieve the required portions when needed.

These techniques solve different problems. Filtering reduces irrelevant input, summarisation preserves the essential state of a long task, and retrieval makes external information available when needed.

A summary is not a substitute for source evidence when exact details matter. If a later decision depends on a specific error message, transaction identifier, or policy clause, retrieve the original record rather than relying on a compressed summary.

### 3\. Know when to summarise and when to retrieve

These are related but not interchangeable.

| Situation                                             | Better approach                                 |
| ----------------------------------------------------- | ----------------------------------------------- |
| A long conversation contains many completed steps     | Summarise the progress and current state        |
| An agent needs a precise policy clause                | Retrieve the original policy passage            |
| A task needs the current status of an order           | Query the authoritative order system            |
| A workflow must resume after an application restart   | Persist task state outside the conversation     |
| A large tool response contains mostly irrelevant data | Filter the response before passing it to Claude |

Production example: An incident-investigation agent has examined 20 services. Instead of carrying all 20 services' complete logs into every turn, it can maintain a structured investigation summary:

* Objective: identify the cause of elevated API latency.

* Evidence: database latency increased shortly before API latency.

* Ruled out: recent frontend deployment.

* Unresolved: whether database connection-pool saturation caused the increase.

* Next action: inspect connection-pool metrics for the affected time interval.

The agent can then retrieve the original metrics when it needs to verify a hypothesis.

One important distinction: conversation context is not durable application state. If a workflow must survive restarts, store its progress, results, and identifiers in an appropriate persistence layer.

### 4\. Understand context limits and compaction

When the context becomes too large, the application needs a strategy for keeping the next model request within supported limits.

Common strategies include:

* Removing irrelevant history.

* Summarising completed work.

* Retrieving only relevant sections of documents.

* Limiting the size of tool results.

* Preserving important identifiers, decisions, constraints, and unresolved tasks.

For Claude API applications, the exact context limits and available context-management features depend on the model and API configuration. Do not assume every model or endpoint has identical limits or capabilities.

A useful rule is to manage context before reaching the limit. Waiting until the request fails creates avoidable interruptions.

### 5\. Design for failure, not just the happy path

An agentic system depends on several components: the model, application logic, tools, external services, and sometimes databases or MCP servers. Any of them can fail.

A production-grade design distinguishes different failure types and responds appropriately.

| Failure                            | Appropriate response                                                               |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| Tool timeout                       | Apply a bounded retry if safe, or stop and report the failure                      |
| Invalid tool arguments             | Validate them and return a useful error that enables correction                    |
| Rate limit                         | Respect the service's retry guidance and apply bounded backoff                     |
| Context limit exceeded             | Reduce or compact the context, then retry if appropriate                           |
| Tool returns no matching records   | Treat this as a valid empty result, not automatically as an error                  |
| Tool execution status is uncertain | Check the authoritative system before repeating a potentially consequential action |

The distinction between failure and uncertainty is particularly important.

Suppose an agent submits a payment request. The connection times out before the application receives the result. The payment may have succeeded even though the response was lost. Blindly retrying could create a duplicate payment.

Safer handling involves an idempotency key where supported, checking the transaction's authoritative status, and retrying only when the operation can be repeated safely.

### Bounded retries and stopping conditions

An agent should not repeat a failed operation indefinitely. Set appropriate limits for:

* Maximum agent iterations.

* Tool timeouts.

* Retry attempts.

* Total execution time.

* Token or cost budgets.

When a limit is reached, the system should stop safely, preserve useful state, and report what remains unresolved. A stopping condition is a reliability mechanism, not merely a convenience.

### 6\. Keep the agent's claims consistent with evidence

Imagine a tool returns:

```json
{
  "status": "timeout",
  "message": "No confirmation received from the order service."
}
```

The agent must not tell the user, “Your order was cancelled successfully.”

The result establishes only that confirmation was not received. It does not establish whether cancellation succeeded or failed.

A reliable system should distinguish among:

* Confirmed success: The authoritative service confirms the operation.

* Confirmed failure: The service establishes that the operation failed.

* Unknown outcome: The available evidence cannot establish either result.

This is a core connection between context management and reliability: Claude must receive accurate tool results, and the application must preserve the difference between known facts and unresolved outcomes.

### 7\. Exam practice

An agent submits a refund request through a tool. The tool call times out before returning a result. The refund service does not support guaranteed idempotency, and the agent cannot determine whether the refund was processed.

What is the safest next step?

A. Retry the refund immediately until the tool returns success.

B. Tell the user the refund failed because the tool timed out.

C. Check the authoritative refund status if possible, avoid a potentially duplicate submission, and report the outcome as unresolved until it can be verified.

D. Ask Claude to infer whether the refund probably succeeded from the conversation history.

Check answer

### Correct.

A timeout does not prove that the operation failed. Verify the state using an authoritative source, avoid duplicate side effects, and communicate uncertainty accurately.

### Lesson 5 summary

Remember these five principles:

* Supply relevant context rather than maximising context size.

* Summarise completed work, but retrieve original evidence when exact details matter.

* Persist workflow state externally when tasks must survive restarts.

* Use bounded retries, timeouts, and explicit stopping conditions.

* Never treat a timeout or missing confirmation as proof of success or failure.

That completes the introductory pass through the five exam domains covered in this learning plan: agentic architecture and orchestration, Claude Code configuration and workflows, prompt engineering and structured output, tool design and MCP integration, and context management and reliability.

The next step is consolidation and exam practice: revisit the distinctions from these lessons through scenario-based questions, identify weak areas, and deepen only the exam-relevant concepts that need more work.
