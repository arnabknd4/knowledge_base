Here is your structured revision note for the Claude Certified Architect – Foundations exam. It consolidates the concepts we've covered into an exam-focused reference, with production-oriented distinctions limited to the official exam domains.

### Claude Certified Architect – Foundations

Structured Revision Notes · Version 1.0

### 60

Exam questions

### 120 min

Exam duration

### 5

Exam domains

### 720

Scaled passing score

Exam format and weights should be confirmed against the official certification guide before your exam.

### 1\. Official exam domains and weights

Agentic Architecture & Orchestration

### 27%

Claude Code Configuration & Workflows

### 20%

Prompt Engineering & Structured Output

### 20%

Tool Design & MCP Integration

### 18%

Context Management & Reliability

### 15%

Study priority should reflect both domain weight and your weak areas. Do not spend most of your revision time on a domain simply because it is interesting.

### 2\. Agentic Architecture & Orchestration — 27%

### 2.1 Choose the right architecture

| Pattern                | When to use it                                   | Main trade-off                                        |
| ---------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Single model call      | One self-contained task                          | Limited ability to adapt through tool feedback        |
| Deterministic workflow | Steps and business rules are known               | Less flexible for unexpected situations               |
| Agent loop             | Next action depends on intermediate findings     | More complexity, cost and failure modes               |
| Sequential execution   | Tasks depend on previous results                 | Higher elapsed time when steps could run concurrently |
| Parallel execution     | Tasks are independent                            | Coordination, resource use and result aggregation     |
| Coordinator–subagent   | Complex tasks benefit from specialist delegation | Additional model calls and orchestration overhead     |

Exam rule: Choose the simplest architecture that satisfies the requirements.

Examples:

* Invoice extraction followed by fixed tax calculation → deterministic workflow.

* Investigating an incident where each result determines the next diagnostic action → agent loop.

* Independently researching three cloud providers → parallel execution.

* Dividing a complex investigation into specialist tasks and synthesizing findings → coordinator–subagent.

### 2.2 Agent loop

Typical lifecycle:

Receive request and context

Claude decides: answer, request a tool, or continue

Application validates and executes tool request

Return result to Claude

Continue or stop based on result and stopping conditions

Important distinctions:

* Claude requests tool execution; the application executes it.

* A tool request does not prove successful execution.

* Tool results can change the next action.

* An agent must have bounded execution and defined stopping conditions.

### 2.3 Messages API stop reasons

| stop_reason | Meaning                                                       |
| ----------- | ------------------------------------------------------------- |
| end_turn    | Claude finished its turn                                      |
| tool_use    | Claude requested tool use                                     |
| max_tokens  | Generation stopped because the output-token limit was reached |

A `tool_use` response is a handoff point for the application. It is not proof that the requested operation has succeeded.

### 2.4 State and reliability

Distinguish three things:

* Conversation context: information available to Claude.

* Application state: authoritative workflow status, identifiers and decisions.

* Tool result: evidence returned by an external operation.

For example, a summary saying “payment completed” is not a substitute for the payment provider's confirmed transaction status.

For failures:

* Identify whether the outcome is confirmed success, confirmed failure or unknown.

* Verify external state when an operation may have completed despite a timeout.

* Retry only under a safe strategy.

* Use idempotency where supported and appropriate.

* Enforce timeouts, retry limits, iteration limits and stopping conditions.

### 3\. Claude Code Configuration & Workflows — 20%

### 3.1 Know the purpose of each mechanism

| Mechanism       | Purpose                                     | Example                                             |
| --------------- | ------------------------------------------- | --------------------------------------------------- |
| CLAUDE.md       | Persistent project instructions             | Coding conventions and architecture constraints     |
| Skills          | Reusable knowledge and procedures           | Standard code-review checklist                      |
| Subagents       | Delegate bounded work in a separate context | Specialist security investigation                   |
| Hooks           | Run configured actions at lifecycle events  | Automated lint or validation check                  |
| Permissions     | Control access to tools and operations      | Restrict or require approval for sensitive commands |
| Custom commands | Named entry points for repeatable tasks     | Generate a release summary                          |

These mechanisms can work together; they are not substitutes for one another.

### 3.2 Common exam traps

* `CLAUDE.md` guides behavior; it is not, by itself, a security boundary.

* A skill provides a procedure; it does not guarantee that every step was executed.

* A subagent delegates work; it does not automatically grant safe permissions.

* A hook runs a configured action when its event and configuration conditions are met; verify its result.

* Permissions control access to operations; they do not replace business validation.

* A custom command offers a reusable entry point; it is not automatically a mandatory workflow.

### 3.3 Configuration scope

Understand the difference between:

* Managed configuration: organization-controlled policy and settings.

* User configuration: personal preferences across projects.

* Project configuration: settings or instructions shared with a team.

* Local configuration: project-specific personal configuration that is not shared.

If an organization requires a security restriction that individuals must not weaken, choose the appropriate managed policy or enforcement control—not merely a project instruction.

Configuration precedence depends on the specific setting and product behavior. Do not assume every configuration type follows the same precedence rules.

### 3.4 Practical selection guide

* Persistent conventions → `CLAUDE.md`.

* Reusable review procedure → skill.

* Separate specialist investigation → subagent.

* Automated action at a specific event → hook.

* Restricting a tool or command → permissions.

* Repeatable named user action → custom command or skill, depending on the intended workflow.

Official reference: [Claude Code documentation](https://code.claude.com/docs/en/overview?utm_source=chatgpt.com).

### 4\. Prompt Engineering & Structured Output — 20%

### 4.1 Prompt structure

A strong prompt defines:

* Task: What must Claude do?

* Context: What information should it use?

* Constraints: What rules and limitations apply?

* Output format: What structure should the answer follow?

Useful techniques include XML-style tags to separate instructions and context, few-shot examples to demonstrate desired behavior, and explicit handling of missing or ambiguous information.

Do not assume a longer prompt is necessarily a better prompt.

### 4.2 Structured output validation

Remember the three layers:

| Layer                        | Question                                    |
| ---------------------------- | ------------------------------------------- |
| Syntax                       | Can the output be parsed?                   |
| Schema                       | Does it have the required fields and types? |
| Semantics and business rules | Are the values supported and permitted?     |

Example: a model returns valid JSON with `"approved": true`, but the claim exceeds the approval threshold.

The JSON can pass syntax and schema validation while still violating business policy. The application must enforce the approval rule.

Exam rule: Schema compliance does not establish factual correctness or authorization.

### 4.3 Prompt improvement versus application changes

| Failure                              | Likely improvement                                            |
| ------------------------------------ | ------------------------------------------------------------- |
| Ambiguous request misunderstood      | Improve prompt, examples or input handling                    |
| Missing required output field        | Improve structured-output constraints and validate the result |
| Outdated policy supplied to model    | Retrieve current authoritative policy                         |
| Incorrect deterministic calculation  | Fix and test application logic                                |
| Unauthorized operation               | Enforce application-side authorization                        |
| Model regression after prompt change | Run representative evaluation and regression tests            |

Do not solve every failure by adding more prompt instructions.

### 4.4 Evaluation and regression testing

A sound evaluation process includes:

* A representative test dataset.

* Expected outputs or explicit evaluation criteria.

* Metrics relevant to the task.

* Analysis of failure cases.

* Regression tests after prompt, model or configuration changes.

Potential metrics include extraction accuracy, schema compliance, tool-selection accuracy, task success rate and policy-violation rate.

An aggregate score can hide critical failures. A prompt that improves extraction but increases unsupported policy claims may be worse for the application overall.

### 5\. Tool Design & MCP Integration — 18%

### 5.1 Tool design principles

A well-designed tool should have:

* A clear, specific name and description.

* An accurate input schema.

* A clearly defined purpose and expected result.

* Runtime validation and authorization.

* Appropriate timeouts and error handling.

* Safe retry behavior for operations that may have side effects.

* Auditability for consequential operations.

Avoid overly broad tools when distinct operations have different authorization or validation requirements.

### 5.2 Tool-use lifecycle

* Claude requests a tool.

* The application receives the requested tool name and arguments.

* The application validates inputs and authorization.

* The tool executes.

* The result returns to Claude.

* Claude interprets the result and responds or continues.

Critical distinction: Tool invocation is not equivalent to tool success.

### 5.3 Read operations versus side effects

| Type                  | Example          | Key concern                                           |
| --------------------- | ---------------- | ----------------------------------------------------- |
| Read                  | Get order status | Access control and data accuracy                      |
| Side effect           | Cancel an order  | Authorization and operation status                    |
| Financial side effect | Issue a refund   | Business limits, duplicate execution and auditability |

Use appropriate safeguards for consequential actions. Confirmation is required when the workflow or risk warrants it; it is not necessarily required for every tool call.

### 5.4 MCP fundamentals

MCP is a standardized protocol for connecting compatible AI applications to external capabilities and context.

| Component | Role                                           |
| --------- | ---------------------------------------------- |
| Host      | AI application the user interacts with         |
| Client    | Component that communicates with an MCP server |
| Server    | Exposes capabilities or context through MCP    |

Three key concepts:

* Tools: operations the model can request.

* Resources: context or data made available to the application.

* Prompts: reusable prompt templates.

### 5.5 Direct API versus MCP

| Requirement                                        | Likely choice                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------ |
| One application with a simple integration          | Direct API may be simpler                                                |
| Shared capabilities across compatible applications | MCP may improve interoperability                                         |
| Strict authorization or validation                 | Implement appropriate security controls regardless of integration method |
| Uncertain external operation outcome               | Verify status and retry safely regardless of integration method          |

MCP standardizes communication. It does not automatically provide authentication, authorization, business-rule validation or reliability.

Official reference: [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro?utm_source=chatgpt.com).

### 6\. Context Management & Reliability — 15%

### 6.1 Context management

Context can include system instructions, user messages, conversation history, tool definitions, tool results and retrieved documents.

Effective strategies:

* Filter irrelevant information.

* Retrieve relevant source material when needed.

* Summarize completed work when the full history is unnecessary.

* Preserve critical identifiers, decisions and unresolved issues.

* Retrieve the original source for exact details that must be verified.

Remember: More context is not always better. A summary preserves continuity; it is not automatically authoritative evidence.

### 6.2 Failure handling

| Failure                       | Appropriate response                                         |
| ----------------------------- | ------------------------------------------------------------ |
| Tool timeout                  | Verify outcome where possible                                |
| Invalid arguments             | Validate and correct or return a clear error                 |
| Rate limit                    | Apply appropriate backoff and retry limits                   |
| Context limit                 | Reduce or summarize context while preserving essential state |
| Empty retrieval result        | Handle missing evidence explicitly                           |
| Unproductive agent loop       | Stop according to configured limits and report the issue     |
| Uncertain financial operation | Verify status before retrying                                |

### 6.3 Reliability controls

A production-oriented agent should have explicit:

* Timeouts.

* Bounded retries.

* Maximum iterations.

* Token or cost limits where appropriate.

* Stopping conditions.

* Error handling and observability.

* Evaluation and regression tests.

These controls should be implemented in the execution architecture rather than relying entirely on Claude to follow instructions.

### 7\. High-value exam traps

Review these before answering scenario questions.

Valid JSON ≠ correct decision

A schema cannot replace business-rule enforcement.

Tool request ≠ successful execution

The application must execute the tool and inspect its result.

Timeout ≠ confirmed failure

The external operation may have completed.

Parallel ≠ multi-agent architecture

Independent tasks may need only parallel execution and aggregation.

Instruction ≠ enforcement

Use appropriate technical controls for mandatory restrictions.

MCP ≠ security

Authentication, authorization and validation remain necessary.

Summary ≠ source of truth

Retrieve authoritative evidence for critical facts.

Higher average accuracy ≠ safer system

Investigate regressions in critical subsets and policy violations.

More context ≠ better performance

Prioritize relevant, authoritative information.

More complex architecture ≠ better architecture

Use the simplest design that meets the requirements.

### 8\. Final revision checklist

Use this checklist to identify what you can confidently answer without notes.

Revision progress

0 of 15

Choose between single-call, deterministic workflow and agent loop.

Distinguish sequential, parallel and coordinator–subagent orchestration.

Explain the agent tool-use lifecycle and Messages API stop reasons.

Explain application state, stopping conditions and safe retry behavior.

Distinguish CLAUDE.md, skills, subagents, hooks and permissions.

Explain configuration scopes and organization-controlled policies.

Design clear tool descriptions and accurate input schemas.

Explain MCP hosts, clients, servers, tools, resources and prompts.

Choose between direct API integration and MCP based on requirements.

Distinguish syntax, schema, semantic correctness and business validation.

Design prompts with clear tasks, context, constraints and output formats.

Diagnose whether a failure belongs to prompting, retrieval or application logic.

Evaluate prompt changes with representative cases and regression tests.

Manage context through filtering, summarization and source retrieval.

Handle timeouts, invalid results, rate limits and unproductive loops.

Copy checklist

### 9\. Recommended exam strategy

For each scenario question:

* Identify the requirement and the constraint.

* Locate the failing layer: prompt, context, schema, tool, application logic or orchestration.

* Choose the least complex solution that meets the requirement.

* Reject answers that rely on model confidence instead of necessary technical controls.

* For multiple-response questions, evaluate every option independently.

For time management, 120 minutes across 60 questions gives an average of 2 minutes per question. Do not spend excessive time on one difficult item at the expense of easier questions.

Official exam information: [Claude Certified Architect – Foundations](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification?utm_source=chatgpt.com).

This revision note consolidates the concepts we've covered. Before treating it as a complete syllabus, cross-check it against the current official exam guide; this note does not independently verify that every official sub-objective has been covered.
