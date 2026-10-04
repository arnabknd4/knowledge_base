# Terraform Associate 004 Study Library

Architect-oriented learning materials aligned to the [official syllabus](./copilot-terraform-syllabus.md). Each domain folder groups topics and objective-level study pages. A study page teaches the underlying model, shows practical Terraform usage, calls out design consequences and exam traps, and ends with self-check questions.

## Domains

1. [Infrastructure as Code with Terraform](./01-iac-with-terraform/index.md)
2. [Terraform fundamentals](./02-terraform-fundamentals/index.md)
3. [Core Terraform workflow](./03-core-terraform-workflow/index.md)
4. [Terraform configuration](./04-terraform-configuration/index.md)
5. [Terraform modules](./05-terraform-modules/index.md)
6. [Terraform state management](./06-terraform-state-management/index.md)
7. [Maintain infrastructure with Terraform](./07-maintain-infrastructure/index.md)
8. [HCP Terraform](./08-hcp-terraform/index.md)

## Suggested learning approach

1. Start with the syllabus and work through the domains in order. Terraform's workflow, configuration, modules, and state build on the earlier IaC and provider concepts.
2. For each objective, read the study page, run the examples in a disposable local or sandbox environment, and answer the review questions without looking.
3. Explain the design trade-offs aloud as if reviewing an architecture: ownership, state boundaries, credentials, change risk, failure recovery, and team operations.
4. Revisit missed questions by building a minimal example and observing the plan and state changes. Never experiment with destructive commands against production infrastructure.
5. Finish with HashiCorp's official [sample questions](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004), then revisit the official [exam content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) for updates.

Examples are for learning and should be adapted to the provider, security model, and operating requirements of a real environment. Do not place credentials or production secrets in example configuration, plans, logs, or state.
