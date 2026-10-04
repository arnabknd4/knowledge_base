# Success Criteria and Prompt Construction · Architect · R / E / L

> **Exam note:** These are current product-document-backed prompting practices; exam coverage is unverified.

## 1. In one line
Prompt engineering is a measured process for making a task's desired behavior clear and improving it against explicit success criteria.

## 2. Problem it solves
- **Without criteria:** prompt changes are subjective; improvements on one example may break unseen cases.
- **With criteria:** a prompt is evaluated on representative inputs, including edge cases, and changed for a demonstrated reason.

## 3. 30-second prompt frame
```text
Goal: classify the support request for routing.
Evidence: use only the supplied ticket and policy excerpt.
Rules: distinguish confirmed facts from unknowns; do not infer missing data.
Output: category, evidence, uncertainty, next action.
Success: correct route, supported evidence, no invented fields.
```

## 4. Mental model
A prompt is one component in a system: model choice, tools, context, constraints, evaluation, and application validation also determine quality.

## 5. Under the hood
1. Define measurable success, known failure modes, and a representative evaluation set before tuning.
2. Write direct instructions with clear task boundaries, relevant context, and explicit output expectations.
3. Use examples when they clarify edge cases or the target format; select examples based on evaluation, not a universal count.
4. Use structural delimiters (such as XML tags) when they help separate instructions, source documents, and data.
5. For multi-stage work, chain steps with explicit intermediate outputs and checks; do not assume longer prompts automatically improve reasoning.
6. Re-run the same evaluation after edits and inspect regressions, not just the example that motivated the change.

## 6. Variants and when to use
| Technique | Use when | Trade-off |
|---|---|---|
| Direct instructions | Task/rules are clear | Simple; may not resolve examples of ambiguous boundary cases |
| Few-shot examples | Desired behavior or edge cases are hard to state | Examples consume context and can bias output |
| XML/context delimiters | Prompt includes varied source material | Better separation; not a security sandbox |
| Prompt chaining | Workflow has distinct stages/checkpoints | Easier to inspect; adds model calls and error propagation |
| Thinking feature | Supported model/API use case benefits from it | May affect latency/token budget; use current official guidance |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| “Be accurate” with no observable criteria | No measurable target or failure diagnosis | Define correct fields, evidence, abstention, and routing outcomes |
| Adding arbitrary example counts | No universal optimal number | Compare candidate prompts on the eval set |
| Asking for hidden chain-of-thought | Can be inappropriate, unsupported, or unnecessary | Ask for concise conclusions, evidence, and decision-relevant rationale; follow model guidance |
| Treating delimiters as injection protection | Quoted text can still influence behavior | Mark untrusted content and enforce tool permissions outside the prompt |
| Tuning on one happy path | Overfits and misses regressions | Include adversarial, ambiguous, malformed, and out-of-scope cases |

## 8. Performance, memory, and concurrency
- **Context/performance:** examples and long source text consume context and latency; retain only material that changes behavior.
- **Concurrency:** prompt evaluations can run independently across test cases; aggregate metrics and inspect qualitative failures.
- **Observability:** version prompt, model, tool set, and eval dataset together so regressions can be reproduced.
- **Testing:** measure task success, unsupported claims, abstentions, format validity, tool selection, latency, and cost.

## 9. Related topics map
- **Prerequisites:** task definition, product/API model support, representative test data
- **Siblings:** structured output, tool design, prompt chaining, evaluation
- **Downstream:** production release, monitoring, iteration
- **Contrasts:** prompt folklore, one-shot subjective review, model-only safety
- **Tools/frameworks:** Claude prompting best practices, Messages API, eval harness

## 10. Cross-domain equivalents
| Prompt element | Engineering analogue |
|---|---|
| Success criteria | Acceptance tests |
| Examples | Golden/edge-case fixtures |
| Delimited source | Explicitly scoped input data |
| Prompt version | Configuration artifact |
| Regression evaluation | CI test suite |

## 11. Interview lens
- **30-second answer:** I define success and a representative eval set, write clear instructions and relevant examples, then compare prompt versions across quality, safety, latency, and cost.
- **Q1 → How many few-shot examples?** There is no universally correct count; choose based on coverage and evaluation results.
- **Q2 → Does role prompting guarantee expertise?** No. It can set framing but does not replace source evidence, domain validation, or evaluation.
- **Spot the bug:** Add examples until the output looks right on the original ticket.  
  **Problem:** no regression or edge-case measurement. **Fix:** evaluate against a fixed, representative set and retain hard cases.

## 12. Architect lens
- Keep task policy, data, and output contract distinct; identify what is trusted and what is user-provided.
- Use calibrated abstention and route unsupported or ambiguous cases rather than forcing a guess.
- **Version note:** model prompting recommendations and thinking features evolve; consult the current Anthropic guidance.

## 13. Revision summary
- Define success before tuning.
- Use examples to clarify, not as a magic quantity.
- Separate instructions from untrusted data.
- Re-evaluate every change for regressions.
- **If you remember only one thing:** Optimize against evidence from representative tests, not prompt aesthetics.

## 14. Coverage self-check
- [ ] Can I convert a vague goal into observable criteria?
- [ ] Can I design a representative eval including edge/abstention cases?
- [ ] Can I choose examples, delimiters, or chaining for a reason?
- [ ] Can I describe prompt/version evaluation trade-offs?

## Sources
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
