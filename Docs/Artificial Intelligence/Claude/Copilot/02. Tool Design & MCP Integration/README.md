# Domain 2 · Tool Design & MCP Integration

**Study status:** Strong alignment with public Claude and MCP documentation; exam coverage and weight are unverified.

## Topic sequence

| # | Topic | Architect outcome |
|---|---|---|
| 1 | [Tool contract and schema design](./01-tool-contract-and-schema-design.md) | Create clear, constrained, useful tools. |
| 2 | [MCP architecture and integration](./02-mcp-architecture-and-integration.md) | Place MCP clients, servers, and primitives correctly. |
| 3 | [Tool execution, errors, and security](./03-tool-execution-errors-and-security.md) | Safely execute calls and handle failures and side effects. |

## Design lens

Treat every tool as an API boundary: document intent, authorize the caller, validate inputs, return useful results, and define failure behavior. MCP standardizes communication; it does not make a server trusted or secure by itself.

## Quick oral drill

An agent can read records and create payments. Which permissions, approvals, idempotency protections, and audit evidence belong outside the prompt?
