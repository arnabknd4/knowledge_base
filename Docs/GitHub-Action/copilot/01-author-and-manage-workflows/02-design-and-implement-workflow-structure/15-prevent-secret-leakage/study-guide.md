# Objective: Prevent secret leakage in logs and expressions.

## What

Secrets are privileged values. They must be handled as exit-guarded information: only exposed to the narrowest scope and never written to logs, summaries, or shell traces.

## Why

- Masking is useful but cannot replace careful design.
- Using secrets in environment variables is preferable to hardcoding them in scripts.
- The safest pattern is to use them only where needed and never print them.

## How

Scope credentials to the job or step that needs them and avoid rendering secret-derived values in commands, logs, outputs, or reports.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}
        run: |
          echo "Deploying using a protected token"
          # never print $TOKEN
```

## Features

Secrets are sensitive inputs, not safe-to-print values. GitHub masks recognized secret values in logs as a safeguard, but masking is not guaranteed for transformed, fragmented, or otherwise unrecognized data.

**Official references**

- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep secrets at the smallest scope possible.
- Use OIDC or workload identity where supported instead of long-lived cloud secrets.

**Don't**

- Don't assume GitHub masks every secret automatically.
- Don't print variables that happen to contain a secret value.
- Don't overlook that shell tracing can reveal secret contents even when they were never meant to appear in logs.

- Don't include secret values in `echo`, `set -x`, or markdown summaries.

## Real-life implementation

Minimize secret exposure by limiting scope and lifetime. Prefer OIDC or another short-lived identity mechanism when supported; inspect logs, shell tracing, artifacts, and summaries as possible leakage paths.

## Q&A

**Q: Can a debug step accidentally print a secret value?**

**A:** Yes. Do not echo credentials or enable shell tracing around secret-bearing commands; masking is best effort and should not be relied upon.

**Q: Are there any script flags or commands that would expose secret material in plain text?**

**A:** Review verbose/debug flags, process arguments, generated files, and error output; pass credentials through the narrowest supported channel.

**Q: Should the workflow use an identity-based alternative instead of a stored secret?**

**A:** Use OIDC where the cloud/provider supports a correctly scoped trust relationship, reducing long-lived credential storage.
