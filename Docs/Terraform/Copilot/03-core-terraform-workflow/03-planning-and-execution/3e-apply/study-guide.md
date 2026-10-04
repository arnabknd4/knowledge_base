# 3e — Apply changes to infrastructure with Terraform

## What

`terraform apply` executes the actions in an execution plan through the configured providers. When invoked without a saved plan, Terraform calculates a fresh plan and, by default in an interactive CLI workflow, asks the operator to approve it. After approval, Terraform performs dependency-ordered operations, reports progress, and records resulting object identities and attributes in state.

Applying is not an all-or-nothing database transaction. A provider operation may fail after earlier resources have already changed. Terraform records progress in state so a subsequent plan can reconcile the partial result. Never assume a failed apply rolled back completed operations; inspect the error and state, then create a new plan before retrying.

## Why

Apply is the deployment boundary: provider credentials are used to make real changes. Use least-privilege identities, environment separation, approval gates appropriate to risk, and state locking where the backend supports it. Concurrency and partial failure should be part of the operational design. After apply, inspect outputs, monitoring, and infrastructure health; successful API operations do not necessarily prove application-level readiness.

The dependency graph permits independent resources to progress concurrently while preserving required order. An apply may stop on an error, leaving some actions completed and others pending. The next plan is the authoritative way to determine what remains to be done.

## How

```shell
terraform apply
terraform plan -out=tfplan
terraform apply tfplan
```

The first command calculates a plan and prompts for approval. Applying a saved plan executes the saved action set without a second confirmation prompt: the meaningful approval happens when the operator authorizes that plan artifact. Keep plan generation, review, and execution in a controlled pipeline; secure the artifact and ensure its variables, workspace, provider credentials, and state context are correct.

`-auto-approve` suppresses the interactive approval step and should be used only when an external control (for example, a protected CI deployment gate) provides the intended review/authorization. It does not make a change safer or create a review by itself.

## Features

- `terraform apply` can create its own plan; passing a saved plan means execute that plan.
- Applying a saved plan does not prompt again for confirmation.
- `-auto-approve` removes interactive confirmation; it is not an approval mechanism.
- Failure does not imply automatic rollback of resources already changed.

## Do's and Don'ts

### Do

- Review the exact plan, target environment, credentials, and state context before approval.
- Replace interactive approval in automation only with an explicit protected review gate.
- After partial failure, inspect state and produce a fresh plan before retrying.

### Don't

- Do not assume apply is transactional or that completed provider operations roll back after failure.
- Do not use `-auto-approve` as a substitute for authorization.
- Do not apply a saved plan in a different or unintended environment.

## Real-life implementation

In an isolated sandbox, generate and review a saved plan, then let a protected CI stage run `terraform apply tfplan` using the same backend/workspace context. Verify the resulting state and application health. If an operation fails partway, stop automated retries, inspect the error and current state, and review a fresh plan to determine what remains.

## Q&A

**Q:** What happens with bare `terraform apply`?  
**A:** Terraform plans, displays the proposal, and asks for approval by default.

**Q:** How does applying a saved plan differ?  
**A:** It executes that plan directly without another confirmation prompt.

**Q:** What is the correct response to a partial apply failure?  
**A:** Investigate, then produce and review a fresh plan; do not assume rollback.

**Q:** What must replace an interactive prompt in safe automation?  
**A:** A deliberate external review and authorization gate.

Further reading: [terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply), [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
