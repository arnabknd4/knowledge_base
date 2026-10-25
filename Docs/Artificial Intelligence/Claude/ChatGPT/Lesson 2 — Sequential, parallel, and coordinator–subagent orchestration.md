### Lesson 2 — Sequential, parallel, and coordinator–subagent orchestration

We will continue with the next topic in Agentic Architecture & Orchestration. The objective is to recognise which orchestration pattern fits a problem, understand its trade-offs, and avoid unnecessary complexity.

A useful distinction to carry forward from Lesson 1:

* Workflow: the application defines the sequence of steps.

* Agent: the model can choose actions based on the request and intermediate results.

* Orchestration pattern: the way work is divided, ordered, coordinated, and completed.

There are three patterns to understand first.

### 1\. Sequential orchestration

Sequential orchestration means that one step follows another, usually because the next step depends on the previous step's output.

Step 1 — Extract claim details

Step 2 — Evaluate policy

Step 3 — Calculate eligible reimbursement

Step 4 — Produce decision report

For example, you cannot reliably calculate reimbursement until you have extracted the claim amount and established which policy rules apply.

Advantages: clear data flow, easier debugging, and straightforward validation between stages.

Limitations: total latency can accumulate across steps, and a failure in an early stage can block downstream work.

Sequential execution is appropriate when there are genuine dependencies between steps. It is not necessary to use an LLM for every step; ordinary application code should handle deterministic operations where appropriate.

### 2\. Parallel orchestration

Parallel orchestration means that multiple independent tasks execute at the same time, and their results are combined when necessary.

Imagine an expense-claim system that must perform three independent reviews after extracting the claim details:

* Check whether the expense description matches the policy.

* Verify whether the receipt contains the required information.

* Identify potential duplicate-claim indicators.

Input: extracted expense claim

Policy check

Receipt check

Duplicate check

Combine results and evaluate the claim

The three checks can run concurrently if they have all the information they need and do not depend on one another's results.

### Why parallelism matters

Suppose three independent checks take 2, 4, and 3 seconds respectively.

With sequential execution, their combined execution time is approximately:

T_{\\text{sequential}}=2+4+3=9\\text{ seconds}

With ideal parallel execution:

T_{\\text{parallel}}\\approx\\max(2,4,3)=4\\text{ seconds}

These are illustrative calculations, not benchmarks. Real systems also incur scheduling overhead, network latency, resource contention, and result aggregation time.

Parallelism does not necessarily reduce total cost. If three model calls run concurrently, you still pay for their combined usage. You must also handle partial failures, timeouts, and inconsistent outputs.

Architectural rule: parallelise independent work, not work that depends on another step's result.

### 3\. Coordinator–subagent orchestration

This pattern introduces a coordinator that delegates tasks to specialised subagents and combines their results.

For example, a software engineering assistant might receive the request:

“Investigate why the order-processing service has become slower and recommend a fix.”

The coordinator could delegate:

* Subagent A: investigate database latency.

* Subagent B: inspect application traces and service dependencies.

* Subagent C: analyse recent code changes.

The coordinator then synthesises the findings into one recommendation.

Coordinator

Understands the goal, decomposes work, assigns tasks and integrates findings

Subagent A

Database

Subagent B

Tracing

Subagent C

Code changes

Coordinator synthesises findings

Checks completeness, resolves conflicts and produces the final response

The important distinction is that subagents are not merely parallel function calls. They can be independently prompted model-driven workers with their own bounded tasks, context, and tool access.

A coordinator–subagent design is useful when the problem can be decomposed into meaningful specialist tasks, particularly when those tasks require different expertise or substantial independent investigation.

However, it introduces additional costs and failure modes:

* More model invocations and potentially higher latency and token usage.

* Coordination overhead and possible loss of important context.

* Conflicting or incomplete findings.

* More complicated tracing, error handling, and permission management.

For a simple question, using several agents is usually unnecessary. A single model call or a deterministic workflow may be sufficient.

### 4\. Compare the patterns

| Dimension      | Sequential                   | Parallel                         | Coordinator–subagent                    |
| -------------- | ---------------------------- | -------------------------------- | --------------------------------------- |
| Task execution | Ordered                      | Independent tasks concurrently   | Delegated tasks coordinated by a parent |
| Main benefit   | Clear dependencies           | Lower wall-clock latency         | Specialisation and decomposition        |
| Main risk      | Accumulated latency          | Partial failures and aggregation | Coordination complexity and cost        |
| Best fit       | Each step needs prior output | Several independent checks       | Complex tasks with distinct subtasks    |

These patterns are not mutually exclusive. A production system can use sequential processing at the top level, parallelise independent checks within one stage, and introduce a coordinator only for a genuinely complex investigation.

### 5\. Exam-style practice

Let's apply the distinctions to a new scenario.

QUESTION 3 · ORCHESTRATION PATTERNS

A company wants a Claude-based research assistant to compare three cloud providers. It needs to investigate pricing, security capabilities, and service availability. The investigations can begin independently, but their findings must be combined into one final recommendation.

Which is the best starting design?

A. Run all investigations sequentially because the final answer needs to be combined.

B. Run independent investigations in parallel, then aggregate and validate their findings.

C. Use a coordinator with many subagents for every individual fact, regardless of task complexity.

D. Ask one model call to invent a complete comparison without retrieving evidence.

Check answer

### Correct.

The research tasks are independent, so parallel execution is a reasonable starting point. Their results can then be aggregated and checked for completeness, consistency, and evidential support. A coordinator–subagent design might become useful if the research grows more complex, but the scenario does not require that added complexity yet.

### 6\. What you should remember

The exam skill is not simply memorising the three patterns. It is identifying the shape of the problem:

* Dependencies imply sequencing.

* Independent tasks create an opportunity for parallel execution.

* Complex decomposition and specialist reasoning may justify a coordinator–subagent architecture.

The next item in our learning sequence is prompt engineering and structured outputs. We will examine how to make Claude's outputs predictable enough for applications to consume, how to define output schemas, and why valid structured output does not automatically mean a result is factually correct.
