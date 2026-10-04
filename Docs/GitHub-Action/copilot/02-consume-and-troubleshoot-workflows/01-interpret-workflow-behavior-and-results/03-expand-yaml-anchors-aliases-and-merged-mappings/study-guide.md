# Expand YAML anchors, aliases, and merged mappings

## What
GitHub Actions workflows are YAML files, and YAML has its own reuse features: anchors (`&name`), aliases (`*name`), and merge keys (`<<`). These are not GitHub Actions features; they are resolved by the YAML parser before GitHub evaluates expressions such as `${{ ... }}`. The effective configuration is what matters, not the appearance of a reused block.

## Why
Large workflows often repeat defaults such as runner labels, timeout values, permissions, or environment blocks. Without understanding anchors and merges, you can misread a job configuration, override a value incorrectly, or blame an Actions expression when the real issue is YAML expansion.

## How
1. Identify the anchor node and whether it is a mapping, sequence, or scalar.
2. Follow every alias to its original anchor and determine whether the YAML references are valid and in scope.
3. Expand merge keys by applying all mapped sources and then checking for explicit overrides in the receiving mapping.
4. Validate the effective config against the job that actually ran, not just the anchor definition.
5. Distinguish YAML resolution from GitHub expression evaluation: YAML determines structure, while `${{ }}` resolves values at runtime.

## Features
- Reuse without duplication: anchors and aliases let one value be reused in multiple places.
- Merged mappings: `<<` combines entries from multiple maps and lets a local mapping override earlier values.
- Effective configuration: the final resolved object is what matters when diagnosing a run.
- YAML vs GitHub semantics: YAML parsing is separate from Actions expression evaluation.

## Do's and Don'ts
### Do
- Expand the YAML mentally before reading any conditional logic.
- Check local override precedence when a job merges a mapping and then redefines a key.
- Use explicit maps when the config is security-sensitive and the merge logic is hard to audit.

### Don't
- Don't confuse `*name` with GitHub expressions or workflow calls.
- Don't assume a merge key deep-merges every nested map the same way across all YAML tools.
- Don't rely on an anchor that appears valid but is out of scope or misspelled.

## Real-life implementation
```yaml
defaults: &linux_defaults
  runs-on: ubuntu-latest
  timeout-minutes: 15

jobs:
  test:
    <<: *linux_defaults
    runs-on: ubuntu-22.04
    steps:
      - run: npm test
```

Here, the effective job configuration is `runs-on: ubuntu-22.04` and `timeout-minutes: 15`. The local override wins, and the anchor does not create a second job or trigger a separate workflow.

### Official references
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [YAML 1.2.2 specification: anchors and aliases](https://yaml.org/spec/1.2.2/)
- [YAML 1.2.2 specification: merge key notes](https://yaml.org/spec/1.2.2/)

## Q&A
### Q: A job merges a mapping and then defines a different `runs-on`. Which value is effective?
A: The receiving job’s local key wins. The merge sets defaults, but the explicitly defined key overrides the merged value.

### Q: Does an alias cause the referenced job to run twice?
A: No. An alias is just a YAML reference to the same node; it does not create a duplicate job or a second workflow execution.

### Q: How do you separate an anchor/merge issue from a GitHub expression issue?
A: If configuration looks wrong before runtime, inspect YAML anchors and merge semantics. If a value is correct in YAML but resolves incorrectly at runtime, inspect `${{ }}` expressions, contexts, and environment values.

### Q: Why is YAML merge behavior risky in complex workflows?
A: The visual structure can hide precedence, and not every tool interprets nested mappings the same way. Security-sensitive defaults should be easy to audit.
