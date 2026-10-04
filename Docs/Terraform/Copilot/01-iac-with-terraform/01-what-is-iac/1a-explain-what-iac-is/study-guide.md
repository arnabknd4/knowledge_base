# 1a — Explain what IaC is

## What

Infrastructure as Code (IaC) describes infrastructure in machine-readable files and uses software tools to create, change, and observe it. Terraform is one IaC tool: it reads configuration, compares desired resources with state and available observations, and proposes actions to reconcile them.

Terraform is primarily **declarative**: state the desired objects and important properties, and Terraform determines an operation sequence. This differs from imperative instructions such as “create a network, then create a subnet, then attach a gateway.”

## Why

IaC replaces an operator's memory or a sequence of console actions as the only record with an inspectable, repeatable description of intended infrastructure. Configuration can be reviewed, versioned, and used consistently across environments. It supports safer change proposals, but does not guarantee that the live environment always matches the files.

## How

```hcl
terraform {
  required_version = ">= 1.12.0"
}

resource "example_network" "app" {
  name       = "app-network"
  cidr_block = "10.20.0.0/16"
}
```

The resource block declares an intended managed object; it does not issue hand-authored API calls or create anything until Terraform applies a plan. `example_network` is illustrative, not usable without a provider that defines it. In Terraform, references express data relationships and normally establish implicit dependencies; Terraform's graph determines ordering where possible. Lifecycle rules, provider behavior, and API constraints still affect execution.

## Features

- Desired-state declarations and dependency graphs, rather than a required hand-written execution sequence.
- Configuration that can be versioned and reviewed; `terraform plan` previews proposed work and `terraform apply` executes it.
- A repeatable workflow for managing represented resources, with state mapping configuration instances to remote objects.
- Drift can arise from human edits or external automation; Terraform may discover it during refresh and planning.

## Do's and Don'ts

### Do

- Keep configuration in version control and review plans before applying.
- Define clear ownership boundaries, validate changes, and use peer review, least privilege, controlled apply permissions, and state protection.
- Use declarative configuration for reviewable convergence; use imperative scripting where a procedural one-off or unmanaged system is a better fit.

### Don't

- Treat configuration as proof that live infrastructure matches it.
- Assume that declaring a resource immediately creates it; a plan previews and an apply performs operations.
- Assume declarative means order and behavior never matter, or that Terraform is the only IaC tool.

## Real-life implementation

For an application network, define the intended network and dependent objects in version-controlled Terraform configuration. Let references express dependencies, run formatting/validation and a plan in CI, have an authorized reviewer inspect the planned impact, and allow a suitably scoped identity to apply. Track manual changes through an agreed drift and ownership process. Resource schemas and execution details depend on the selected provider; the example above is illustrative.

## Q&A

1. **Declarative vs. imperative?** Declarative states desired configuration; imperative specifies steps.
2. **Does declaring a resource immediately create it?** No; an apply operation executes an approved plan.
3. **Why use references between resources?** They express data relationships and normally establish implicit dependencies.
4. **Can manual changes remain invisible?** They can cause drift that Terraform may discover during refresh/planning.
5. **What does a plan do?** It previews proposed work; it does not perform it.

## Official references

- [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- [Terraform overview](https://developer.hashicorp.com/terraform/intro)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
