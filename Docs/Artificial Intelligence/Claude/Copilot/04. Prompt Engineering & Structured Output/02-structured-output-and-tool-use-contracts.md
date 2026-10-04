# Structured Output and Tool-Use Contracts · Architect · R / E / L

> **Exam note:** Structured outputs and tool use are documented API features; exam coverage is unverified.

## 1. In one line
Structured output constrains response shape; tool-use contracts describe callable capabilities—neither guarantees that values are true or actions are safe.

## 2. Problem it solves
- **Without structure:** downstream parsers face malformed or inconsistent output, and applications may misinterpret free text.
- **With a contract:** required fields and types are explicit, while application logic separately validates meaning and authorizes actions.

## 3. 30-second extraction contract
```json
{
  "status": "found | not_found | ambiguous",
  "date": "YYYY-MM-DD or null",
  "evidence": "source text supporting the date",
  "needs_review": true
}
```
Illustrative schema design: define valid enums, required fields, and `additionalProperties` policy in the actual supported JSON Schema.

## 4. Mental model
Schema validity answers “does it fit the contract?”; semantic validation answers “is it supported and safe to use?”

## 5. Under the hood
1. Define the output contract around downstream decisions, including explicit missing/ambiguous states.
2. Use supported structured JSON output for response bodies or strict tool-use schemas for tool names/inputs where applicable.
3. Parse/validate the result using the SDK or application validator; handle refusal, truncation, or API errors explicitly.
4. Check evidence, domain invariants, ranges, cross-field consistency, and authorization separately.
5. Keep external actions separate from extracted/proposed data; require policy gates before writes.

## 6. Variants and when to use
| Mechanism | Use when | Trade-off |
|---|---|---|
| JSON Schema structured output | Application needs predictable JSON result | Supported schema features/model availability can vary |
| Strict tool use | Tool names and inputs must conform to schema | Does not enforce business permission or correct target |
| Free-form text | Human-facing narrative is primary | Harder to parse reliably |
| Nullable/explicit status fields | Missing or ambiguous values are meaningful | Consumers must correctly handle every status |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Schema-valid means factually correct | A plausible false value can satisfy the type | Validate against source evidence and business rules |
| Empty string for every unknown | Collapses not-found, ambiguity, and missing data | Use explicit status, nullable fields, and evidence |
| Blind retry after parse/validation error | May loop indefinitely or hide systematic issue | Diagnose error class, cap attempts, record result, escalate |
| Ignoring refusal/truncation | Incomplete or policy-refused output may be consumed | Branch explicitly on response status/stop condition and validate completeness |
| `additionalProperties` left accidental | Unexpected fields can break or expand consumers | Set schema policy deliberately and version the contract |

## 8. Performance, memory, and concurrency
- **Performance:** constrained decoding can simplify parsing but schema size and unsupported complexity affect integration; benchmark real workloads.
- **Concurrency:** validate each response independently and correlate it with the originating request, especially in batch jobs.
- **Observability:** record schema/version, validation outcome, refusal/truncation category, and safe evidence references.
- **Testing:** include null/missing, ambiguous, contradictory evidence, invalid enum, extra fields, refusal, and truncated output.

## 9. Related topics map
- **Prerequisites:** tool contracts, JSON Schema basics, output consumer behavior
- **Siblings:** prompt criteria, validation/retry, anti-fabrication and provenance
- **Downstream:** parsers, databases, routing, APIs, human review
- **Contrasts:** free-form prompting, application authorization, factual verification
- **Tools/frameworks:** Claude structured outputs; strict tool use; SDK parsing helpers

## 10. Cross-domain equivalents
| Output concern | Structured-output control | Independent check |
|---|---|---|
| Type/shape | Schema | Parser/schema validator |
| Allowed value | Enum/range | Business rule |
| Factual grounding | Evidence field | Source lookup |
| Permission | Not a schema property | AuthZ service |
| Missing information | Nullable/status representation | Routing policy |

## 11. Interview lens
- **30-second answer:** I use a schema for predictable shape, explicit states for missing or ambiguous data, and separate evidence/business validation before consuming or acting on the result.
- **Q1 → Does strict tool use guarantee safe tool execution?** No; it constrains call shape/name, while host authorization and implementation enforce safety.
- **Q2 → How should extraction represent absent data?** Explicitly—such as nullable value plus a status/evidence field—according to the consumer contract.
- **Spot the bug:** Extracted `amount: 100` passes a numeric schema, so the app issues a refund.  
  **Problem:** type validity is not evidence or authorization. **Fix:** verify the amount from trusted source data and apply refund policy/approval.

## 12. Architect lens
- Design output contracts from consumer requirements and version them compatibly.
- Represent uncertainty explicitly; preserve source evidence and fail visibly on invalid or incomplete results.
- **Version note:** structured-output support and JSON Schema subset/model availability change; consult current API docs.

## 13. Revision summary
- Schema constrains shape, not truth.
- Strict tool schemas do not grant permission.
- Model missing and ambiguous data explicitly.
- Validate evidence and meaning in the application.
- **If you remember only one thing:** A parseable result can still be wrong, unsupported, or unauthorized.

## 14. Coverage self-check
- [ ] Can I design a contract with null/ambiguous states?
- [ ] Can I distinguish JSON outputs from strict tool-use constraints?
- [ ] Can I handle refusal and truncation explicitly?
- [ ] Can I identify the semantic and authorization checks beyond schema?

## Sources
- [Claude structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Claude strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)
