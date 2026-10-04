# 2b — Describe how Terraform uses providers

## What

Terraform's core language describes resources and data sources, but does not include the API implementation for every platform. A provider is a separately distributed plugin that defines resource/data-source schemas and implements operations such as reading, creating, updating, and deleting remote objects. Provider behavior and supported arguments are provider-specific.

## Why

Providers connect Terraform's common configuration and execution model to each target platform or service. They are executable production dependencies with independent releases, permissions, and operational characteristics. Credentials determine what Terraform can affect; permissions, network access, remote constraints, rate limits, and provider bugs can all affect whether an operation succeeds.

## How

Keep four concepts distinct:

1. **Source** identifies the provider package, for example `example.org/acme/example`.
2. **Version requirement** in `required_providers` constrains eligible plugin releases.
3. **Provider configuration** supplies settings for an instance, such as an endpoint or authentication approach.
4. **Initialization** (`terraform init`) selects and installs the plugin, using the dependency lock file where applicable.

```hcl
terraform {
  required_providers {
    example = {
      source  = "example.org/acme/example"
      version = "~> 1.4"
    }
  }
}

provider "example" {
  region = "region-a"
}
```

This is a structural illustration only: address, argument name, and region are placeholders. `required_providers` defines which plugin Terraform should obtain; the `provider` block configures an instance. Terraform invokes the selected provider during planning and applying. Avoid hard-coded secrets; use provider-supported environment, workload identity, or secret-management mechanisms.

## Features

- Provider schemas define the resource and data-source types available to configuration.
- Provider implementations translate Terraform operations to platform/service interactions.
- Requirements name and constrain plugins; provider blocks configure instances; init selects and installs plugins.
- Root modules normally declare requirements and supply provider configurations. Child modules should also declare the provider source/version requirements they need; configurations are generally supplied by the root and can be passed to children.

## Do's and Don'ts

### Do

- Use least-privilege credentials and appropriately separated identities/environments.
- Version and review providers as production dependencies; review lock-file changes.
- Ensure team automation can initialize the same permitted provider versions.
- Make child-module provider requirements and configuration wiring deliberate.

### Don't

- Confuse provider plugins with Terraform resources or backends.
- Confuse source, version, provider configuration, and credentials; they answer different questions.
- Hard-code secrets in provider configuration.
- Assume a syntactically valid configuration guarantees API success.

## Real-life implementation

For a team-managed service, declare its real provider source and version under `required_providers`, initialize and review the lock selection, then configure the provider using supported non-hard-coded credentials with least privilege. The root module can pass the provider configuration to child modules that declare their requirements. Before apply, verify target account/environment, network access, permissions, and provider-specific plan behavior. The example's provider schema and values are placeholders.

## Q&A

1. **What does a provider implement?** Resource/data-source schemas and interactions with a platform or service.
2. **Where specify package address and constraint?** Under `terraform.required_providers`.
3. **What does a `provider` block do?** Supplies configuration for a provider instance.
4. **When is the plugin installed?** During `terraform init`.
5. **What does apply do with the provider?** Terraform invokes provider operations to implement the approved plan.

## Official references

- [Providers overview](https://developer.hashicorp.com/terraform/language/providers)
- [Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [Provider configuration](https://developer.hashicorp.com/terraform/language/providers/configuration)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
