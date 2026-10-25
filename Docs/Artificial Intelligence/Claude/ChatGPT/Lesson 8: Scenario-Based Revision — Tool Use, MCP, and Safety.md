### Lesson 8: Scenario-Based Revision — Tool Use, MCP, and Safety

This lesson tests whether you can distinguish a model's decision to call a tool from the application's responsibility to execute that call safely. It also reinforces when MCP is useful and how to handle failures without making unsupported claims.

### 1\. The tool-use lifecycle

In a typical Claude Messages API tool-use cycle:

* Your application sends Claude the conversation and available tool definitions.

* Claude may return a tool-use request with a tool name and arguments.

* Your application validates the request and executes the corresponding operation.

* Your application sends the tool result back to Claude.

* Claude interprets the result and either responds or requests another tool call.

The application must not treat a requested tool call as proof that the operation happened. It must also distinguish an actual tool result from a model-generated claim about that result.

For example, Claude requesting `cancel_order` does not mean an order was cancelled. The order service must confirm the outcome.

### 2\. Scenario: A tool can change production data

A customer-support agent has two tools:

* `get_order_status` — read an order's status.

* `cancel_order` — cancel an order.

The agent receives a request to cancel an order. Which design is safest?

A. Allow Claude to call either tool without application-side checks because the model understands the user's intent.

B. Use clear tool definitions, authenticate the user, verify access to the specific order, enforce cancellation rules, and confirm the result from the order service.

C. Put “only cancel authorised orders” in the system prompt and rely on that instruction as the security control.

D. Allow the application to report success immediately when Claude requests the cancellation.

Check answer

### Correct.

Application-side authentication, authorisation, and business-rule enforcement protect the operation. The order service's result determines what the application can truthfully report.

### 3\. Scenario: Should you use MCP?

A company has built an internal documentation service. Three compatible AI applications need access to its search functionality.

The team could build a separate custom integration for each application or expose the search capability through an MCP server.

Best reasoning: MCP is a strong candidate because it standardises how compatible clients discover and use the service's capabilities. Each host still needs an MCP client or compatible integration, and the service still needs appropriate access controls.

MCP does not automatically guarantee security, and it is not mandatory when a direct integration is simpler and sufficient.

### 4\. Scenario: A tool call times out

An agent submits a refund request. The connection times out, and the application cannot determine whether the refund was processed.

What should it do?

Production reasoning

* Do not interpret the timeout as proof of failure.

* Check the authoritative refund status if possible.

* Avoid blindly repeating a potentially consequential operation.

* Use idempotency controls where available and retry only under a safe policy.

* Report the outcome as unknown until it can be verified.

This scenario tests two principles together: bounded failure handling and evidence-based reporting.

### 5\. Key distinctions

| Exam clue                                             | Strong architectural response                                              |
| ----------------------------------------------------- | -------------------------------------------------------------------------- |
| Multiple applications need a standardised integration | Consider MCP                                                               |
| Tool arguments may be malformed                       | Validate the input schema                                                  |
| A user may request an unauthorised action             | Enforce authorisation in application logic                                 |
| A state-changing tool times out                       | Verify the outcome before retrying                                         |
| Claude requests a tool call                           | Execute it through the application or appropriate tool server              |
| A tool reports an error                               | Pass the accurate result back and apply bounded recovery or stopping rules |

### Your checkpoint

You should now be able to explain the difference between tool selection, tool execution, MCP integration, and application-side enforcement.

The next lesson will revise Prompt Engineering, Structured Output, and Context Management together, focusing on a common exam trap: a response can be structurally valid while still being factually incorrect or unsafe to use.
