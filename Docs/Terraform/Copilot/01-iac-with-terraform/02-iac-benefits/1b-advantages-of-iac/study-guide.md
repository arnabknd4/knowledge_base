# 1b — Describe the advantages of IaC patterns

## What

IaC patterns describe infrastructure changes in machine-readable configuration and manage them through a repeatable tool workflow. In Terraform, configuration diffs and generated plans make proposed changes visible before execution.

## Why

The same reviewed configuration can establish equivalent environments, subject to inputs, provider behavior, and external constraints. IaC reduces dependence on memory and manual console sequences. Version control records what changed, who proposed it, and how it relates to a release or incident. Automation can format, validate, check policy, and generate plans, with authorized approval before production execution.

## How

```hcl
variable "instance_count" {
  type        = number
  description = "Number of application instances."
  default     = 2
}

resource "example_instance" "app" {
  count = var.instance_count
  name  = "app-${count.index}"
}
```

Changing `instance_count` in a version-controlled commit makes the requested change explicit. A plan can show resulting additions or removals. `example_instance` is schematic and requires a real provider. Reviewers should inspect both diff and plan, including sensitive data, replacement/destruction effects, and the target workspace/environment.

## Features

- **Repeatability and consistency:** reduces one-off manual variation, but does not promise identical outcomes across different external conditions.
- **History and collaboration:** version control captures configuration changes, but does not itself deploy them.
- **Pre-execution review:** plans expose proposed changes but cannot guarantee apply success or prevent later drift.
- **Automation:** checks and approval gates can improve safety, while also scaling mistakes if permissions and design are poor.
- **Traceability:** links infrastructure changes to releases and incidents; state maps managed objects, while configuration records desired declarations.

## Do's and Don'ts

### Do

- Maintain clear ownership for each object and define how out-of-band changes are handled.
- Build maintainable modules and interfaces, control variable values, and scope execution credentials.
- Treat plans as decision artifacts and review changes before apply; protect saved plans because they are sensitive and can become stale.
- Use approvals and least-privilege identities for production automation.

### Don't

- Treat repeatability as absolute identity; inputs, provider versions, APIs, and timing matter.
- Assume version control alone deploys infrastructure or that a successful plan freezes reality.
- Use broad automation identities or poorly designed modules that can amplify mistakes.
- Treat state or version control alone as a complete disaster-recovery or governance strategy.

## Real-life implementation

For a development/test/production fleet, keep the configuration and reviewed environment inputs in version control. A change to instance count should trigger formatting, validation, policy checks, and a plan. Review the plan for replacement/destruction, sensitivity, and correct target; require authorized approval and a scoped identity for production apply. Protect any saved plan, coordinate its execution promptly, and maintain an ownership process for manual changes. The example resource is illustrative and provider-dependent.

## Q&A

1. **What enables review before infrastructure changes?** The configuration diff and generated plan.
2. **How does version control help?** It records and supports collaboration around configuration history.
3. **Does a successful plan freeze reality?** No; live conditions can change before apply.
4. **Name a trade-off of automation.** It scales both correct operations and mistakes, so permissions and gates matter.
5. **Does a plan guarantee that apply will succeed?** No; it reflects information at planning time, and external conditions may change.

## Official references

- [Terraform workflow](https://developer.hashicorp.com/terraform/intro/core-workflow)
- [Terraform plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform apply command](https://developer.hashicorp.com/terraform/cli/commands/apply)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
