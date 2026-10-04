# Access and use secrets and variables in workflows and actions

## What
Workflows must retrieve secrets and variables in a controlled and explicit way. The goal is to use each value in the correct scope, pass only what is needed, and avoid accidental disclosure in logs or action inputs.

## Why
Runtime misuse of credentials or config values is one of the most common security failures in automation. A secret may be valid and still be exposed if it is printed, passed broadly, or used in the wrong environment.

## How
- Access values with `secrets` and `vars` in the workflow or action input contract, not by hardcoding them.
- Limit secret usage to the job, environment, or action that actually needs the value.
- Validate required values before the workflow runs and fail early if they are missing.
- Avoid printing sensitive material and prefer masked or minimal outputs in debugging.

## Features
- Workflow-level access to repository and environment-scoped values.
- `vars` for non-sensitive metadata and `secrets` for sensitive material.
- Environment-scoped controls tied to deployment targets.
- Clear action input contracts to reduce accidental disclosure.

## Do's and Don'ts
- Do: use variables for non-sensitive metadata like regions, labels, and artifact names.
- Do: keep secrets out of logs, output, and debug traces.
- Do: require the environment before using environment-scoped secrets.
- Do: pass only the minimal value needed to each action.
- Don't: confuse `vars` with `secrets`.
- Don't: print secret values while debugging.
- Don't: assume environment-scoped secrets are available without the target environment.
- Don't: pass broad credentials to every action when only one step needs them.

## Real-life implementation
A deployment workflow reads `vars.ENVIRONMENT_NAME`, `vars.ARTIFACT_BUCKET`, and `secrets.PROD_KUBECONFIG` only in the production environment. The workflow passes only the required values to the deployment action and avoids logging the secret or exposing it in debug output.

## Q&A
### Q: What is the safest way to pass secret values into a workflow?
A: Use the scoped `secrets` context and pass only the exact values required by the job or action, without printing or exposing them in logs.

### Q: What should go in `vars` instead of `secrets`?
A: Non-sensitive runtime metadata like region, cluster name, or artifact bucket identifiers.

### Q: Why does environment selection matter?
A: A job can only access environment-scoped values when the environment is explicitly selected for that job, which is a core security control.

### Q: What is a good troubleshooting technique for secret-related failures?
A: Check whether the job targets the correct environment, the value is defined at the correct scope, and the workflow is not exposing the secret during debug output.

## Official docs
- [Using variables in a workflow](https://docs.github.com/en/actions/learn-github-actions/variables)
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [About environments](https://docs.github.com/en/actions/deployment/using-environments-for-deployment)
- [Context and expression syntax](https://docs.github.com/en/actions/learn-github-actions/contexts)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
