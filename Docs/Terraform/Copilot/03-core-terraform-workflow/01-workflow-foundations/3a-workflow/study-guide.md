# 3a — Describe the Terraform workflow

## What

Terraform's core loop is **write → plan → apply**. In *write*, configuration declares the desired infrastructure and relationships. In *plan*, Terraform compares that configuration with its state and refreshed observations of remote objects, then calculates a proposed set of actions. In *apply*, Terraform executes the approved actions through providers and records the resulting object identities and attributes in state. This is a declarative workflow: operators describe the target, rather than scripting every API call and recovery step.

The three inputs to a useful plan are not interchangeable. Configuration expresses intent; state records Terraform's mapping of resource addresses to remote objects and last-known attributes; refresh queries providers for current remote information. A discrepancy may indicate drift, a configuration change, or an out-of-band deletion. Terraform reconciles these inputs and proposes a change; it does not blindly replay configuration.

## Why

Treat plans as change artifacts. Teams can review the proposed create, update, replace, and destroy operations in code review or a deployment gate before execution. Reproducibility improves when the configuration, provider selections, variables, Terraform version, and plan context are controlled. A plan can become stale if relevant configuration, state, or remote infrastructure changes; regenerate and review it rather than assuming an old preview remains valid.

Terraform's graph allows independent operations to run concurrently and orders dependent operations. A workflow therefore expresses dependencies in configuration (usually via references), not by manually sequencing every command. State is central to this model and must be backed up/protected according to the chosen backend and collaboration design.

## How

Start in a working directory with configuration and initialize it before planning. Typical commands are:

```shell
terraform init
terraform fmt -check
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
```

`terraform plan` is a preview, not an infrastructure mutation, although normal planning can read remote APIs and update local/remote state metadata depending on backend and options. Applying a saved plan executes that exact reviewed plan rather than prompting Terraform to calculate a fresh one. Without a saved plan, `terraform apply` creates a plan and asks for approval interactively by default.

## Features

- `write / plan / apply` describes the stages, not three mandatory commands in every invocation.
- `validate` checks configuration structure; it does not prove that remote APIs will accept a change. A plan is not the same as validation.
- A plan is a proposed action set based on configuration, state, and observed information—not a guarantee that apply will succeed.
- `terraform apply <saved-plan>` does not ask for a second approval; the saved plan itself is the reviewed approval artifact.

## Do's and Don'ts

### Do

- Keep configuration, state/backend, and refreshed remote reality distinct when diagnosing a proposed change.
- Review the plan in the correct environment and treat apply as a controlled deployment boundary.
- Protect shared state and use a repeatable workflow in local and CI environments.

### Don't

- Do not treat `validate` or `plan` as equivalent to applying or as guarantees that APIs will succeed.
- Do not assume a saved plan remains valid after its configuration, state, or remote context changes.
- Do not manage shared infrastructure from an uncoordinated state copy.

## Real-life implementation

For a disposable sandbox, initialize a small configuration, format and validate it, create a saved plan, inspect every action, and apply only after confirming the sandbox backend/workspace and credentials. Then inspect state and remote health. If the sandbox is no longer needed, review a separate destroy plan before teardown. This illustrates the full write → plan → apply loop without using production resources.

## Q&A

**Q:** What three sources inform a plan?  
**A:** Configuration, state, and refreshed/observed infrastructure.

**Q:** Which stage mutates managed infrastructure?  
**A:** Apply.

**Q:** Why might a reviewed plan need regeneration?  
**A:** Relevant config, state, or remote conditions may have changed, making it stale.

**Q:** Does Terraform require operators to script API call order?  
**A:** No; the dependency graph determines valid ordering and parallelism.

Further reading: [Terraform workflow](https://developer.hashicorp.com/terraform/intro/core-workflow), [Terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [Terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
