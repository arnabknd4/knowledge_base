# Tool Contract and Schema Design · Architect · R / E / L

> **Exam note:** Tool design is documented product capability; exam inclusion is unverified.

## 1. In one line
A good tool contract makes capability, invocation conditions, valid inputs, effects, and result semantics unambiguous to both the model and host.

## 2. Problem it solves
- **Without a clear contract:** the model may select the wrong tool, omit required fields, or misuse a broad capability.
- **With a clear contract:** constrained schemas and descriptions improve selection while host validation and authorization protect execution.

## 3. 30-second tool contract
```json
{
  "name": "lookup_order",
  "description": "Read an order for the authenticated customer. Use when ... Do not use to change an order.",
  "input_schema": {
    "type": "object",
    "properties": {"order_id": {"type": "string"}},
    "required": ["order_id"],
    "additionalProperties": false
  }
}
```
Illustrative shape only. The backend must still verify that the caller owns the requested order.

## 4. Mental model
The description teaches tool selection; the schema constrains shape; the implementation enforces truth, authorization, and effects.

## 5. Under the hood
1. Name tools by stable intent and namespace them when similar operations span services.
2. Describe what the tool does, when to use it, when not to use it, parameter meaning, effects, limitations, and result behavior.
3. Use a constrained input schema with required fields, types, enums/ranges where appropriate, and examples for complex inputs.
4. Use API tool-selection controls, including `tool_choice` where supported, to guide whether/how a tool is selected; selection does not grant permission.
5. Validate again in the host: a model-generated schema-valid value may still be unauthorized, stale, or semantically invalid.
6. Return concise, stable, high-signal results and structured errors that support the next decision.

## 6. Variants and when to use
| Contract style | Use when | Trade-off |
|---|---|---|
| Narrow tool per capability | Distinct permissions or effects need separation | More definitions; clearer boundaries |
| Consolidated tool with action enum | Related operations share security and lifecycle | Fewer tools; action semantics can become broad |
| Read-only tool | Lookup/research workflows | Safer, but cannot complete writes |
| Strict schema/tool use | Invalid inputs must be rejected where supported | Schema constraints vary; backend validation remains necessary |
| Tool-selection control | A workflow must require, prefer, or avoid a tool call | API-specific behavior; execution still needs authorization |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Vague tool description | Model cannot distinguish overlapping tools | Add positive/negative use conditions and behavior |
| Tool named `do_action` | Hides capability and permission boundary | Use a stable, meaningful name |
| One broad admin tool | Excessive blast radius | Split read/write or resource scopes; enforce least privilege |
| Assuming JSON schema is authorization | Shape says nothing about user access | Check identity, resource ownership, and policy at runtime |
| Returning whole database rows | Leaks data and wastes context | Return only fields needed for the decision |

## 8. Performance, memory, and concurrency
- **Performance:** many overlapping tools increase selection ambiguity and schema/context overhead; consolidate related operations only when permissions stay coherent.
- **Concurrency:** define behavior for simultaneous updates and stale versions; use conditional writes/transactions where needed.
- **Observability:** log tool name, validated arguments or redacted identifiers, outcome, error class, and duration.
- **Testing:** test wrong tool selection, missing/extra fields, invalid enum, unauthorized resource, and malformed backend response.

## 9. Related topics map
- **Prerequisites:** agent loop, API request structure, threat boundaries
- **Siblings:** MCP server design, structured output, tool-choice control
- **Downstream:** error handling, authorization, evaluation
- **Contrasts:** free-form prompting, unrestricted shell/admin capability
- **Tools/frameworks:** Claude API tool definitions and JSON Schema

## 10. Cross-domain equivalents
| Concern | Claude tool | MCP/API equivalent |
|---|---|---|
| Capability | Name and description | MCP tool name/description |
| Input | `input_schema` | JSON Schema request arguments |
| Result | Tool result content | MCP tool result |
| Enforcement | Host implementation | Server-side authorization and validation |

## 11. Interview lens
- **30-second answer:** I design narrow tools with explicit invocation guidance and constrained schemas, then validate identity, authorization, business rules, and effects again in the backend.
- **Q1 → Does a detailed description replace examples?** No. Descriptions explain intent; examples can clarify complex input formats, but evaluation is still needed.
- **Q2 → Can strict schemas prevent fabricated facts?** No. They constrain structure, not factual grounding.
- **Q3 → Does `tool_choice` authorize a tool call?** No. It influences selection; the host still validates and authorizes execution.
- **Spot the bug:** Schema requires `customer_id`; backend accepts any ID supplied by the model.  
  **Problem:** a well-formed request can still access another user's data. **Fix:** derive identity from trusted auth context and authorize the resource.

## 12. Architect lens
- Design contracts alongside permission scopes, data classification, effect semantics, and versioning.
- Separate validation errors, permission denials, not-found results, and transient failures.
- **Version note:** supported schema keywords and strict-mode behavior are API/model-specific; verify the current tool reference.

## 13. Revision summary
- Descriptions guide; schemas constrain; implementations enforce.
- Make capability and side effects explicit.
- Return minimal, useful results.
- Revalidate all model-supplied values.
- **If you remember only one thing:** A valid tool call is not necessarily a permitted or correct operation.

## 14. Coverage self-check
- [ ] Can I write a useful tool description and narrow schema?
- [ ] Can I explain why runtime authorization is still required?
- [ ] Can I design high-signal results and structured errors?
- [ ] Can I test tool selection, validation, and access boundaries?

## Sources
- [Claude API: Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- [Claude API: Tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
