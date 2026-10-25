### Lesson 4: Tool Design and MCP Integration

This lesson covers how Claude interacts with external systems through tools, how to design reliable tool interfaces, and what the Model Context Protocol (MCP) contributes to an application.

The central principle is: Claude can request an action through a tool, but your application or tool server must execute it and enforce the relevant permissions.

### 1\. What is a tool?

A tool gives Claude a defined way to interact with data or functionality outside the model itself.

Examples include:

* `get_order_status` — retrieve an order's current status.

* `search_documents` — find relevant internal documents.

* `create_refund_request` — submit a refund request.

* `run_sql_query` — execute an authorised database query.

A tool definition typically specifies a name, description, and input schema. Claude uses these to determine which tool may be relevant and what arguments to provide.

Consider an order-support assistant. The user asks, “Where is order 1234?”

The application provides a `get_order_status` tool. Claude may request that tool with `order_id: "1234"`. The application validates the request, executes the lookup, and returns the result. Claude then explains the status to the user.

The tool definition does not itself execute the operation. In a typical Messages API tool-use flow, the application receives Claude's tool-use response, runs the tool, and sends the result back to Claude.

### 2\. Design tools that Claude can use reliably

A tool is an interface between model reasoning and application functionality. Its design affects whether Claude selects the right action and provides usable arguments.

Suppose you define this tool:

```json
{
  "name": "get_order_status",
  "description": "Retrieve the current status of an order using its order ID.",
  "input_schema": {
    "type": "object",
    "properties": {
      "order_id": {
        "type": "string",
        "description": "The unique identifier of the order."
      }
    },
    "required": ["order_id"]
  }
}
```

This illustrates three important design choices:

* Specific name: `get_order_status` communicates the operation more clearly than `process_order`.

* Action-oriented description: Claude can distinguish a read operation from a cancellation or refund.

* Explicit schema: The required argument and its meaning are clear.

A vague tool description can cause the model to choose the wrong tool. A weak schema can allow missing or incorrectly typed arguments. Good descriptions and schemas reduce ambiguity, but they do not replace runtime validation.

### Keep each tool's responsibility clear

Prefer a small set of focused tools over a single generic tool that can do almost anything.

For example, separate `get_order_status` from `cancel_order`. They have different side effects and should have different permission checks.

Avoid creating excessive tiny tools, however. Each available tool adds descriptions and schemas to the model's context, and overlapping tools can make selection harder.

### 3\. Treat tool execution as a trust boundary

Imagine Claude requests cancellation of order `1234`. A production application should not assume that the request is authorised just because Claude generated it.

A safer execution path is:

1\. Claude requests a tool call

Tool name and arguments

2\. Application validates the request

Schema, identity, permissions, business rules

3\. Tool implementation executes

Call the order service or database

4\. Return the actual result

Success, rejection, or failure

5\. Claude interprets the result

Communicate only what the result supports

The application must independently enforce authorisation. For example, a user should not be able to cancel another customer's order by supplying a different order ID.

For tools that change state, also consider:

* Idempotency: Prevent duplicate effects when a request is retried.

* Timeouts and failure handling: Avoid waiting indefinitely and distinguish failure from success.

* Audit logs: Record important operations and their outcomes.

* Confirmation: Require user approval where the action or its consequences warrant it.

These are implementation controls around tool execution, not guarantees provided by a prompt.

### 4\. What is MCP?

The Model Context Protocol (MCP) is an open standard that allows AI applications to connect to external tools and context providers through a common protocol. Instead of building a separate integration mechanism for every AI application and service, developers can expose capabilities through an MCP server and connect compatible hosts to it.

Understand the three components:

MCP host

The AI application, such as Claude Desktop or your own agent application

MCP client

The component inside the host that communicates using MCP

MCP server

Exposes tools, resources, and prompts to compatible clients

An MCP server does not need to communicate directly with Claude itself. The host manages the model interaction, while the MCP client communicates with the server.

### The three MCP primitives

| Primitive | Purpose                                               | Example                              |
| --------- | ----------------------------------------------------- | ------------------------------------ |
| Tools     | Execute an action or retrieve information when called | get_order_status                     |
| Resources | Expose data or context for the application to read    | An order record or a policy document |
| Prompts   | Provide reusable prompt templates                     | A standard customer-support workflow |

A useful exam distinction is that tools are typically selected by the model, resources are managed by the application, and prompts are commonly invoked by the user.

MCP standardises how capabilities are discovered and accessed. It does not automatically make a connected service secure, reliable, or authorised.

### 5\. Direct tool integration versus MCP

Suppose your application needs to access an internal order service.

Direct integration: Your application defines the tool for Claude and implements the function call itself. This can be a straightforward choice when the integration is limited to one application.

MCP integration: You expose the order service through an MCP server. Compatible hosts can discover and use its advertised capabilities without each host needing a separately designed integration protocol.

MCP is particularly useful when multiple compatible AI applications need to reuse the same service. It introduces its own connection, configuration, and security considerations, so it is not automatically the better choice for every application.

### 6\. Exam practice

A company has an internal knowledge service that needs to be accessed by several compatible AI applications. The team wants a standardised way to expose searchable knowledge and callable operations, rather than building a different integration protocol for each application.

Which approach best fits this requirement?

A. Put all knowledge and operations into a single system prompt.

B. Build a separate, application-specific integration for every AI host.

C. Expose the relevant capabilities through an MCP server and let compatible hosts connect through MCP clients.

D. Give Claude direct database credentials and allow it to execute arbitrary queries.

Check answer

### Correct.

MCP provides a standard integration interface for compatible hosts. It does not eliminate the need for authentication, authorisation, input validation, or least-privilege access.

### Lesson 4 summary

Retain these distinctions:

* A tool definition describes a callable operation; the application or tool server executes it.

* Tool names, descriptions, and schemas help Claude select and invoke tools correctly.

* Validate tool arguments and enforce authorisation outside the model.

* Design state-changing tools with failure handling and duplicate-operation protection.

* MCP standardises connections between AI hosts and external capabilities through clients and servers.

* MCP tools, resources, and prompts have different purposes.

The next lesson is Context Management and Reliability: managing context efficiently, handling failures, and making agentic systems more dependable. These are directly relevant to the remaining certification domain.
