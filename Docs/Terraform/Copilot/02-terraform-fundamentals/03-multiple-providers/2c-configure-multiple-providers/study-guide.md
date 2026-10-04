# 2c — Write Terraform configuration using multiple providers

## What

A Terraform configuration may require multiple provider packages or multiple configurations of one provider. Each requirement has a local name, source address, and version constraint. An unaliased provider configuration is the default; an `alias` names an additional configuration of that provider.

## Why

Multiple provider configurations let a configuration target distinct contexts such as regions, accounts, or environments. Explicit selection makes topology visible, but also increases configuration complexity and the credential contexts to protect. A wrong but syntactically valid mapping may target the wrong tenancy or environment.

## How

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

provider "example" {
  alias  = "secondary"
  region = "region-b"
}

resource "example_network" "primary" {
  name = "primary"
}

resource "example_network" "secondary" {
  provider = example.secondary
  name     = "secondary"
}
```

Addresses and schema arguments are illustrative. The unaliased block is the default; `provider = example.secondary` selects the aliased instance, not a resource type or a new package. Distinct provider packages follow the same requirement/configuration principle. Cross-provider resource references can establish ordering dependencies.

## Features

- Resources use the default provider configuration when no `provider` meta-argument is set.
- The `provider` meta-argument selects a specific provider configuration for a resource.
- A module can declare provider requirements and expected aliases in `required_providers`.
- A caller can pass configurations explicitly using the module block's `providers` map. Child modules normally use configurations supplied by callers rather than defining credentials or platform settings themselves.

## Do's and Don'ts

### Do

- Name aliases by meaningful role or boundary, such as `production` or `audit`.
- Verify that each provider mapping matches the intended tenancy, region, or environment; inspect plans and permissions.
- Make child-module provider requirements and alias mapping explicit so reusable modules are not tied to hard-coded account/region choices.
- Consider separate states or workspaces when teams, lifecycle, or blast-radius boundaries differ substantially.

### Don't

- Assume an alias identifies a second provider package; it can be another configuration of the same provider.
- Assume an omitted `provider` argument selects an alias; it selects the default configuration.
- Use opaque alias names that conceal impact or hard-code credentials in reusable modules.
- Assume syntactic validity proves a provider mapping is operationally correct.

## Real-life implementation

For a service deployed in two regions, define the provider's default and aliased configurations with securely supplied credentials. Bind each resource to its intended configuration, review the plan for correct target regions/accounts, and ensure automation identities have only required access. If a child module needs both configurations, declare the required aliases and pass them from the caller's `providers` map. Use real provider schemas and arguments in production; this sample is schematic.

## Q&A

1. **How select a non-default configuration for a resource?** Set `provider = local_name.alias`.
2. **Does an alias require a second provider source?** No, it can be another configuration of the same provider.
3. **What is an unaliased provider block?** The default provider configuration.
4. **Why pass providers to a module explicitly?** To make configuration and environment wiring intentional and reusable.
5. **What happens if a resource omits `provider`?** Terraform uses the default provider configuration.

## Official references

- [Provider configuration](https://developer.hashicorp.com/terraform/language/providers/configuration)
- [Providers within modules](https://developer.hashicorp.com/terraform/language/modules/develop/providers)
- [Module block reference](https://developer.hashicorp.com/terraform/language/block/module)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
