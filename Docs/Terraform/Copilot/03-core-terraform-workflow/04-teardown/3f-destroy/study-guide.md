# 3f — Destroy Terraform-managed infrastructure

## What

Destroy removes infrastructure objects that Terraform manages in the selected working directory and state. The CLI offers `terraform destroy` as a convenience command; it is equivalent in intent to planning with `terraform plan -destroy` and then applying that destruction plan. Terraform uses the state mapping to identify the managed objects, and the dependency graph determines a safe destruction order (dependents are generally removed before dependencies).

Destroy is not a general-purpose cloud cleanup command. It will not remove unrelated objects merely because they exist in an account; Terraform targets objects tracked by the active state. Conversely, using the wrong workspace, backend, or credentials can target an unexpected environment or fail to find the expected objects.

## Why

Treat teardown as a production change. Data retention, backups, deletion protection, ownership boundaries, downstream consumers, and compliance requirements should be checked before approval. Some provider objects have cascading effects or delayed deletion; the plan may not communicate every business consequence. For critical systems, use explicit approvals, maintenance windows, and out-of-band verification.

Separate state boundaries can limit accidental blast radius: an environment-specific root configuration/state should correspond to a clear lifecycle and ownership boundary. If infrastructure is meant to outlive a stack, avoid destroying its state-owning configuration without first deciding how ownership will transfer.

## How

```shell
terraform plan -destroy
terraform destroy
```

The first command previews destruction without applying it. The second generates and displays a destruction plan and prompts for approval in an interactive CLI. Read the entire plan: confirm state/workspace, object addresses, dependencies, and the scope of irreversible deletion. Use `-target` only for exceptional recovery scenarios; it is not a recommended normal teardown strategy because it can leave the rest of the configuration/state inconsistent with the intended full graph.

Destroy removes managed objects, not the Terraform configuration or necessarily the state backend itself. After a successful full teardown, state remains useful as a record (typically with no managed instances), and configuration files remain available for future recreation.

## Features

- `terraform destroy` removes infrastructure tracked by the selected state, not every object in the account.
- `terraform plan -destroy` previews; it does not execute the destruction.
- Terraform generally destroys dependents before dependencies.
- Destroying resources does not delete HCL files or necessarily delete the backend/state container.
- Review is essential: wrong state/workspace selection can be more dangerous than command syntax.

## Do's and Don'ts

### Do

- Treat teardown as a high-risk deployment and confirm account, backend, workspace, and full target scope.
- Start with `terraform plan -destroy`; require an independent review for valuable environments.
- Use a dedicated, disposable sandbox with nonvaluable data to practice destroy and verify the result.

### Don't

- Do not run destroy against production or an ambiguous state context.
- Do not assume `terraform destroy` deletes every object in an account or deletes the HCL/backend.
- Do not use `-target` as a routine shortcut for full teardown.

## Real-life implementation

Practice only in a dedicated disposable sandbox with isolated state and no valuable data. First run `terraform plan -destroy`, confirm the workspace/backend and every listed address, and obtain approval; then run the interactive destroy and verify the sandbox resources are gone. For production teardown, separately check backups, retention, deletion protection, consumers, and approvals. A destroy plan is a preview; it does not itself delete anything.

## Q&A

**Q:** What does destroy target?  
**A:** Objects managed in the active configuration/state context.

**Q:** Which command previews teardown?  
**A:** `terraform plan -destroy`.

**Q:** What happens to dependency order?  
**A:** Dependents are normally destroyed before the objects they depend on.

**Q:** What remains after infrastructure deletion?  
**A:** Configuration and usually the state/backend record, unless separately removed.

Further reading: [terraform destroy](https://developer.hashicorp.com/terraform/cli/commands/destroy), [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
