# Diagnose failed workflow runs

## What
A failed GitHub Actions run is evidence that the workflow reached a broken state somewhere in the lifecycle: trigger setup, job scheduling, runner provisioning, step execution, action installation, or cleanup. The failure signal is often the symptom, not the root cause. Successful diagnosis depends on identifying the first incorrect condition or missing dependency rather than only reading the final red line.

## Why
Workflow failures can originate outside the code itself: runner availability, permission restrictions, network outages, service-side rate limits, matrix conditions, or token problems. You need a disciplined method to decide whether the issue is configuration, environment, permissions, external dependency state, or a genuine application bug.

## How
1. Classify the result: failed, cancelled, skipped, timed out, or never started. Each outcome narrows the likely layer.
2. Find the first failing step in the job log and read the surrounding context, not just the last line.
3. Compare run metadata: commit SHA, event type, ref, actor, matrix values, runner OS, action versions, and permissions.
4. Compare with the previous successful run to isolate changes in workflow YAML, dependency versions, external services, or runner images.
5. Form one testable hypothesis and validate it with a minimal rerun or targeted debug log. Avoid changing multiple variables at once.
6. Preserve evidence and document the durable fix, preferring explicit configuration and controlled retries over repeated blind reruns.

## Features
- Run classification: failed, cancelled, skipped, and timed out are all different failure modes.
- Context triage: runner, branch, ref, SHA, event, actor, and matrix values matter.
- Timeline comparison: last good run is often the strongest diagnostic reference.
- Security-safe debugging: avoid printing secrets or tokens in logs.
- Guardrails: permissions, concurrency, and timeouts are common sources of non-code failures.

## Do's and Don'ts
### Do
- Capture the failing job, step, and earliest error before editing YAML.
- Compare the failing run with a nearby successful run on the same branch or commit family.
- Check permissions, runner conditions, and external service availability when the failure is auth- or network-related.
- Preserve a clean log trail and redact secrets.

### Don't
- Don't rerun a deterministic failure repeatedly without a hypothesis.
- Don't treat a cancelled run as an application failure without checking concurrency or timeout rules.
- Don't print secrets, tokens, or environment dumps into logs.
- Don't assume a “works on rerun” result proves the fix; it may simply reveal a flaky job, race, or dependency issue.

## Real-life implementation
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - run: ./deploy.sh
```

If the deploy job fails with `not authorized`, the important evidence is not only the final error line. Check the workflow’s permissions block, the token type in use, the environment configuration, and the caller repo or environment policy before changing the script.

### Official references
- [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)
- [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs)
- [Enabling debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging)
- [Workflow syntax: permissions, concurrency, and timeouts](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)

## Q&A
### Q: A deployment step fails with “not authorized.” What should I check before changing the script?
A: Check the workflow permissions, the token type, the environment protection rules, and the repo or org policies that govern the action. The failure is often an auth boundary problem, not a code bug.

### Q: A job fails only on one matrix leg. What evidence do you compare?
A: Compare the runner OS, runtime version, action version, dependency versions, and environment variables for the failing leg versus the successful ones.

### Q: A rerun passes. Does that mean the workflow is fixed?
A: Not necessarily. The rerun may have been transient, infrastructure-related, or a race. Validate the root cause, inspect the control variables, and avoid treating “works on rerun” as proof of a durable fix.

### Q: What is the difference between a failed job and a cancelled job?
A: A failed job means a step or condition reported a failure. A cancelled job typically resulted from timeout, concurrency cancellation, or a manual cancel, which points to a different layer than code-level execution.
