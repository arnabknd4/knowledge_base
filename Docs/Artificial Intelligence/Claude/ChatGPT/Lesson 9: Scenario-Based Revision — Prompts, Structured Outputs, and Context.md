### Lesson 9: Scenario-Based Revision — Prompts, Structured Outputs, and Context

This lesson combines three exam domains that frequently intersect in real systems: prompt engineering, structured output, and context management.

The central principle is valid format does not guarantee correct content. A reliable application must give Claude clear instructions, provide relevant evidence, validate the output, and independently enforce business rules.

### 1\. Scenario: Valid JSON, incorrect decision

An insurance application asks Claude to extract information from a claim and return:

* `claim_amount`: a number.

* `currency`: a currency code.

* `missing_fields`: a list of strings.

* `recommendation`: an allowed value.

Claude returns syntactically valid JSON that conforms to the schema, but it recommends approving a claim that violates a mandatory policy rule.

What went wrong?

The output passed structural validation, but that did not establish business correctness. A schema can restrict field types and allowed values without proving that the underlying reasoning or recommendation is correct.

The appropriate design is to:

* Define the expected output schema.

* Use a structured-output mechanism where supported.

* Validate the returned structure.

* Apply mandatory policy rules in trusted application logic.

* Keep final approval authority in the authorised workflow.

Do not use schema validation as a substitute for business validation.

### 2\. Scenario: The prompt is ambiguous

A developer writes:

> Analyse this claim and return the correct result.

The application receives inconsistent responses. Sometimes Claude invents missing details, sometimes it returns prose instead of JSON, and sometimes it treats a recommendation as a final approval.

A stronger prompt should specify the task, evidence, constraints, and output contract.

For example:

```text
Task:
Extract the claim details and identify relevant policy findings.

Evidence:
Use only the supplied claim and policy.

Constraints:
- Do not invent missing information.
- Represent unknown values as null where the schema permits.
- Separate policy findings from the approval decision.
- Do not claim that a claim has been approved.

Output:
Return the required structured format.
```

This makes the expected behaviour clearer. However, instructions such as “do not invent information” reduce ambiguity; they do not guarantee that hallucinations will never occur. Validate consequential results against authoritative data.

### 3\. Scenario: The context is too large

An agent investigates a production incident. Its conversation contains thousands of log lines, results from several tools, and multiple hypotheses. Later requests become expensive and struggle to focus on the latest evidence.

What is the best response?

A reliable context-management strategy

* Summarise completed investigations, confirmed facts, rejected hypotheses, and unresolved questions.

* Retain important identifiers, constraints, and decisions.

* Retrieve the original logs or metrics when exact evidence is needed.

* Limit tool outputs to relevant information.

* Persist important workflow state outside the conversation if the investigation must survive restarts.

The key distinction is that summarisation preserves useful state, while retrieval recovers source evidence. A summary may omit details, so it should not replace the original record when precision matters.

### 4\. Practice question

An invoice-processing agent returns valid JSON that conforms to the required schema. However, the invoice total conflicts with the total recorded by the authoritative accounting system. The agent's conversation also contains a large amount of irrelevant historical context.

Which approach best addresses both problems?

A. Increase the context window and trust the schema-valid response.

B. Rewrite the prompt to demand greater accuracy and remove all historical information.

C. Verify the total against the authoritative accounting system, apply business validation, and reduce irrelevant context while retaining or retrieving evidence needed for the task.

D. Ask a second Claude agent to confirm the first agent's answer and accept it if both agree.

Check answer

### 5\. What to remember for the exam

| Concept                    | Essential distinction                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Prompt engineering         | Clarifies the task, constraints, evidence, and expected response                           |
| Structured output          | Constrains response structure and, where supported, helps produce schema-conforming output |
| Schema validation          | Checks structure and data types                                                            |
| Business validation        | Checks whether values and decisions satisfy application rules                              |
| Context summarisation      | Compresses prior work into useful state                                                    |
| Retrieval                  | Obtains relevant source information when needed                                            |
| Authoritative verification | Establishes whether important claims agree with the trusted system of record               |

Your revision checkpoint: You should be able to explain why a schema-valid response can still be wrong, why a longer context is not necessarily a better context, and why authoritative verification belongs in the application architecture.

Next, we should move to a mixed-domain assessment that combines architecture selection, orchestration, Claude Code configuration, MCP, structured outputs, and reliability. This will help identify which areas need deeper study before attempting a full mock exam.
