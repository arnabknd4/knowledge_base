# HashiCorp Terraform Associate (004) Exam Syllabus

This checklist is based on HashiCorp's official **Terraform Associate (004)** exam content list and preparation path. It organizes the published objectives into domains, topics, and actionable subtopics; it is a study aid, not a guarantee of passing.

> - **Exam version:** Terraform Associate (004)
> - **Terraform version referenced by the official guide:** Terraform 1.12
> - **Source checked:** October 4, 2026
> - **Important:** HashiCorp states that provider-specific knowledge is not required. The official content list does not assign domain weights, so none are assumed here.

## Exam domains

1. Infrastructure as Code (IaC) with Terraform
2. Terraform fundamentals
3. Core Terraform workflow
4. Terraform configuration
5. Terraform modules
6. Terraform state management
7. Maintain infrastructure with Terraform
8. HCP Terraform

## 1. Infrastructure as Code (IaC) with Terraform

### 1a. Explain what IaC is

- [ ] Describe infrastructure as code and how infrastructure is defined and managed through machine-readable configuration.
- [ ] Distinguish declarative configuration (desired end state) from imperative, step-by-step instructions.

### 1b. Describe the advantages of IaC patterns

- [ ] Explain repeatability, consistency, reviewability, version control, and automation.
- [ ] Describe how plans and configuration changes make infrastructure updates easier to review and reproduce.

### 1c. Explain how Terraform manages multi-cloud, hybrid-cloud, and service-agnostic workflows

- [ ] Explain how providers let Terraform manage different infrastructure platforms and services through one workflow.
- [ ] Describe multi-cloud and hybrid-cloud use cases without relying on knowledge of a specific provider.

## 2. Terraform fundamentals

### 2a. Install and version Terraform providers

- [ ] Understand how Terraform finds, installs, and initializes providers.
- [ ] Specify provider source addresses and version constraints in `required_providers`.
- [ ] Explain the purpose of `.terraform.lock.hcl`, provider selections, and checksums.
- [ ] Understand how to upgrade provider selections deliberately.

### 2b. Describe how Terraform uses providers

- [ ] Explain that providers are plugins that let Terraform interact with platforms and services.
- [ ] Distinguish provider requirements from provider configuration.
- [ ] Recognize provider source, version, configuration, and plugin initialization.

### 2c. Write Terraform configuration using multiple providers

- [ ] Configure more than one provider in a configuration.
- [ ] Understand default and aliased provider configurations and how resources or modules select them.

### 2d. Explain how Terraform uses and manages state

- [ ] Explain how state maps configuration resources to real infrastructure objects.
- [ ] Describe why state is needed for planning, tracking resource identity, and determining changes.
- [ ] Recognize that state can contain sensitive values and must be protected.

## 3. Core Terraform workflow

### 3a. Describe the Terraform workflow

- [ ] Explain the write, plan, and apply stages.
- [ ] Describe how Terraform compares configuration, state, and observed infrastructure to propose changes.

### 3b. Initialize a Terraform working directory

- [ ] Use `terraform init` to initialize a configuration directory.
- [ ] Understand initialization of providers, modules, and backend configuration.

### 3c. Validate a Terraform configuration

- [ ] Use `terraform validate` to check configuration syntax and internal consistency.
- [ ] Distinguish validation from planning and provider-dependent checks.

### 3d. Generate and review an execution plan

- [ ] Use `terraform plan` to preview proposed infrastructure changes.
- [ ] Interpret create, update, replace, and destroy actions in a plan.
- [ ] Understand that a plan is based on configuration, state, and refreshed information.

### 3e. Apply changes to infrastructure with Terraform

- [ ] Use `terraform apply` and understand how Terraform executes the plan.
- [ ] Recognize approval of a proposed plan and the effect of applying a saved plan.

### 3f. Destroy Terraform-managed infrastructure

- [ ] Use `terraform destroy` to remove infrastructure managed by the configuration.
- [ ] Understand the consequences and review planned destruction before approval.

### 3g. Apply formatting and style adjustments to a configuration

- [ ] Use `terraform fmt` to format configuration consistently.
- [ ] Recognize formatting as separate from validation and execution.

## 4. Terraform configuration

### 4a. Use and differentiate `resource` and `data` blocks

- [ ] Use a `resource` block to manage an object.
- [ ] Use a `data` block to read information about an existing object or external source.
- [ ] Distinguish management of an object from querying it.

### 4b. Refer to resource attributes and create cross-resource references

- [ ] Reference resource attributes and other named values using Terraform expressions.
- [ ] Understand resource addresses and how references establish implicit dependencies.
- [ ] Read resource references in configuration and plans.

### 4c. Use variables and outputs

- [ ] Declare and use input variables, including types, descriptions, and defaults.
- [ ] Supply variable values through supported variable files, command-line options, and environment variables.
- [ ] Declare outputs and reference them from the root module or calling modules.
- [ ] Understand which values are sensitive and how marking a value sensitive affects display (not whether it is stored).

### 4d. Understand and use complex types

- [ ] Recognize primitive types and collection/structural types, including list, set, map, object, and tuple.
- [ ] Read type constraints and values in variable and output declarations.
- [ ] Understand how element types and collection shapes affect expressions and configuration.

### 4e. Write dynamic configuration using expressions and functions

- [ ] Read and write references, operators, conditional expressions, and `for` expressions.
- [ ] Understand dynamic resource or module repetition using `count` and `for_each`.
- [ ] Use built-in functions to transform and work with values.
- [ ] Distinguish expressions, functions, and interpolated strings.

### 4f. Define resource dependencies in configuration

- [ ] Understand implicit dependencies created by references and when explicit `depends_on` is appropriate.
- [ ] Understand how dependencies affect Terraform's resource graph and operation order.
- [ ] Explain the `create_before_destroy` lifecycle rule and its effect on replacement ordering.

### 4g. Validate configuration using custom conditions

- [ ] Use variable validation rules to reject invalid input.
- [ ] Understand preconditions and postconditions on resources and data sources.
- [ ] Understand `check` blocks and how custom conditions report failed assumptions.

### 4h. Understand best practices for managing sensitive data, including secrets management with Vault

- [ ] Identify where sensitive values may appear and why Terraform state and plan files need protection.
- [ ] Use sensitive markings to limit display of values, while recognizing that sensitivity markings alone do not remove values from state.
- [ ] Understand ephemeral values and provider write-only arguments, including how they differ from ordinary values persisted in state or plans.
- [ ] Describe secure secret-management practices, including integration with Vault instead of hard-coding secrets.

## 5. Terraform modules

### 5a. Explain how Terraform sources modules

- [ ] Recognize local, registry, and other supported module sources.
- [ ] Understand how Terraform retrieves modules and how a module source is declared.

### 5b. Describe variable scope within modules

- [ ] Distinguish root-module and child-module inputs, outputs, and local values.
- [ ] Understand that child-module inputs are passed explicitly by the calling module.

### 5c. Use modules in configuration

- [ ] Call modules with a `module` block and pass input values.
- [ ] Read module outputs and compose modules through their inputs and outputs.
- [ ] Understand how reusable modules help organize configuration.

### 5d. Manage module versions

- [ ] Specify and understand a module version constraint for registry modules.
- [ ] Distinguish module version selection from provider version selection.
- [ ] Understand why module upgrades should be controlled and reviewed.

## 6. Terraform state management

### 6a. Describe the local backend

- [ ] Understand the default local backend and where local state is stored.
- [ ] Recognize the purpose of the backend block and local backend configuration.

### 6b. Describe state locking

- [ ] Explain why locking prevents concurrent operations from corrupting state.
- [ ] Understand when locking is available and why force-unlocking must be used cautiously.

### 6c. Configure remote state using the backend block

- [ ] Understand remote state storage and backend configuration.
- [ ] Distinguish backend configuration from provider configuration.
- [ ] Understand backend initialization and migration considerations when changing backends.

### 6d. Manage resource drift and Terraform state

- [ ] Explain configuration drift and how refreshed infrastructure information affects a plan.
- [ ] Understand state refactoring, resource addresses, and safe state changes.
- [ ] Distinguish refresh-only operations from normal changes to managed infrastructure.
- [ ] Recognize `moved` and `removed` blocks and their role in changing resource addresses or relinquishing management.

## 7. Maintain infrastructure with Terraform

### 7a. Import existing infrastructure into your Terraform workspace

- [ ] Understand how to bring existing objects under Terraform management.
- [ ] Recognize the Terraform import workflow and the need for matching configuration and state.

### 7b. Use the CLI to inspect state

- [ ] Use Terraform state commands to list, inspect, move, remove, or otherwise manage state entries.
- [ ] Understand resource addresses when inspecting state.
- [ ] Treat state changes as sensitive operations and review their impact.

### 7c. Describe when and how to use verbose logging

- [ ] Understand when diagnostic logging is useful for troubleshooting Terraform.
- [ ] Recognize `TF_LOG` and related logging controls.
- [ ] Protect logs because they may expose configuration details or sensitive information.

## 8. HCP Terraform

### 8a. Use HCP Terraform to create infrastructure

- [ ] Understand HCP Terraform workspaces and how they connect configuration, variables, state, and runs.
- [ ] Describe the HCP Terraform workflow and remote operations.
- [ ] Understand the relationship between CLI-driven runs and remote execution.

### 8b. Describe HCP Terraform collaboration and governance features

- [ ] Recognize collaboration and governance capabilities, including teams and permissions, the private registry, and policy enforcement.
- [ ] Understand variable sets, workspace health and Explorer, change requests, and drift detection.
- [ ] Recognize dynamic provider credentials and their role in reducing long-lived credentials.
- [ ] Understand how governance, policy, and collaboration features support shared infrastructure workflows.

### 8c. Describe how to organize and use HCP Terraform workspaces and projects

- [ ] Explain how projects organize workspaces.
- [ ] Understand run triggers and how they connect workspace runs.
- [ ] Understand how variable sets can be shared and associated with workspaces or projects.

### 8d. Configure and use HCP Terraform integration

- [ ] Connect the Terraform CLI to HCP Terraform, including authentication and CLI-driven workflow setup.
- [ ] Understand how to migrate state to HCP Terraform.
- [ ] Recognize remote operations and Terraform version settings for HCP Terraform workspaces.
- [ ] Explain how HCP Terraform supports collaboration around runs, configuration, and state.

## Readiness check

- [ ] Explain every objective in your own words and identify when the relevant command, block, or feature is appropriate.
- [ ] Practice the full CLI workflow: `init`, `fmt`, `validate`, `plan`, `apply`, and `destroy`.
- [ ] Practice reading plans, references, dependency ordering, state addresses, and module inputs/outputs.
- [ ] Review state safety, locking, backends, drift, imports, and refactoring before working with real infrastructure.
- [ ] Review custom conditions, lifecycle behavior, sensitive values, ephemeral values, and write-only arguments, which are important Associate 004 topics.
- [ ] Review HCP Terraform workspaces, projects, remote operations, collaboration, and governance features.
- [ ] Use HashiCorp's official sample questions to become familiar with question style, and recheck the official content list before booking because exam objectives can change.

## Official sources

- [Terraform Associate 004 exam content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) — official domains, numbered objectives, and mapped documentation/tutorials.
- [Terraform Associate 004 learning path](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004) — official preparation path.
- [Terraform Associate 004 sample questions](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004) — official sample question format.
- [HashiCorp certifications](https://developer.hashicorp.com/certifications) — official certification program and registration information.
- [Terraform documentation](https://developer.hashicorp.com/terraform/docs) — official Terraform product documentation.
