### Lesson 7: Scenario-Based Revision — Architecture and Orchestration

We will now shift from learning individual concepts to applying them in exam-style scenarios. For each question, focus on the requirement, identify the simplest design that satisfies it, and eliminate options that add unnecessary complexity or weaken reliability.

The first revision topic is agentic architecture and orchestration.

### 1\. Choose the right architecture

A common architectural decision is whether a task needs a deterministic workflow, a single agent, or multiple cooperating agents.

Deterministic workflow

Use when the steps and decision rules are known in advance. Ordinary code handles predictable operations; Claude can handle language-dependent steps.

Single agent with tools

Use when the task requires flexible reasoning, selecting tools, and adapting to the information returned at runtime.

Coordinator with subagents

Use when a complex task benefits from decomposing work into distinct specialist investigations and combining their findings.

The exam-relevant principle is not “agents are better than workflows.” It is match the orchestration pattern to the uncertainty, dependencies, and complexity of the task.

For example, processing a fixed expense-claim sequence usually favours a workflow. Investigating an unfamiliar production incident may justify an agent with diagnostic tools. Parallel specialist investigations may be appropriate when the incident spans several independent systems.

### 2\. Practice scenario

A company is building an invoice-processing system. Every invoice must pass through the same stages: extract fields, validate required information, calculate totals, and store the result. Some invoices contain ambiguous descriptions that require language understanding.

The system must be auditable, and invalid invoices must never be stored as approved invoices.

Which architecture is the best fit?

A. Give Claude full autonomy to decide which stages to run and whether an invoice should be approved.

B. Use a deterministic workflow for the fixed stages, Claude for ambiguous language interpretation, and application-side validation and approval controls.

C. Create a coordinator and four subagents, one for each stage, regardless of the task's complexity.

D. Use a single large prompt and trust Claude to perform all calculations and enforce every invariant.

Check answer

### Correct.

The stages are known and repeatable, so a deterministic workflow provides control and auditability. Claude adds value when interpreting ambiguous descriptions. The application should validate fields and calculations, and enforce the rule that invalid invoices cannot be approved or stored as approved.

### 3\. The architectural reasoning to remember

When you see an exam scenario, ask these questions in order:

* Are the steps predetermined? If yes, start with a deterministic workflow.

* Where is language understanding or flexible reasoning genuinely needed? Use Claude for those parts.

* Are tasks independent? Parallelise them when doing so improves latency and the resource trade-off is acceptable.

* Is the task complex enough to justify delegation? Use coordinator–subagent orchestration only when decomposition provides real value.

* Which outcomes must never be left to model judgement alone? Enforce authorisation, business invariants, and consequential state changes in application logic.

The next revision scenario will focus on tool use and MCP, including tool failures, permissions, and safe handling of side effects.
