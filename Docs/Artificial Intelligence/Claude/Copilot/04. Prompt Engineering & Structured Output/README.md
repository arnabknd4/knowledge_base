# Domain 4 · Prompt Engineering & Structured Output

**Study status:** Strong alignment with public Claude API documentation; exam coverage and weight are unverified.

## Topic sequence

| # | Topic | Architect outcome |
|---|---|---|
| 1 | [Success criteria and prompt construction](./01-success-criteria-and-prompt-construction.md) | Turn requirements into testable instructions. |
| 2 | [Structured output and tool-use contracts](./02-structured-output-and-tool-use-contracts.md) | Produce parseable outputs without confusing shape with truth. |
| 3 | [Evaluation, retries, and batch processing](./03-evaluation-retries-and-batch-processing.md) | Improve quality empirically and select the right processing mode. |

## Design lens

Define success and test cases before prompt tuning. Schema constraints solve structural problems; evidence checks, business rules, and human review address semantic correctness and risk.

## Quick oral drill

The response parses as valid JSON but invents a missing date. Which layer failed, and what validation or uncertainty representation would prevent downstream harm?
