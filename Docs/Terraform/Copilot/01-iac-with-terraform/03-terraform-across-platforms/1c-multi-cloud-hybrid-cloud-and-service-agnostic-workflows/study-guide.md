# 1c — Explain Terraform's multi-cloud, hybrid-cloud, and service-agnostic workflows

## What

Terraform uses **providers**—plugins that implement resource and data-source types and translate Terraform operations into interactions with a platform or service. “Multi-cloud” means managing resources across cloud platforms through a shared Terraform workflow. “Hybrid cloud” can span cloud and on-premises or private infrastructure. “Service-agnostic” means providers can also manage SaaS, identity, networking, and other service APIs.

## Why

A common initialize, plan, review, apply, and state workflow can coordinate systems through one configuration. This is useful when cross-platform orchestration is valuable, but it does not make platforms interchangeable or services portable. The common layer is Terraform's configuration and execution model, not a universal resource model.

## How

```hcl
terraform {
  required_providers {
    alpha = {
      source  = "example.org/acme/alpha"
      version = "~> 1.0"
    }
    beta = {
      source  = "example.org/acme/beta"
      version = "~> 2.0"
    }
  }
}

resource "alpha_network" "app" {
  name = "app-network"
}

resource "beta_service" "app" {
  network_id = alpha_network.app.id
}
```

This is illustrative, not real registry packages or resource schemas. A reference can express a dependency across providers, allowing Terraform to order operations. A real configuration requires valid provider addresses, supported versions, provider configurations, and resource arguments.

## Features

- Multiple provider requirements and resource types can participate in one dependency graph.
- Cross-provider references can establish ordering dependencies.
- Providers target services beyond public cloud infrastructure.
- Providers have distinct APIs, schemas, lifecycle behavior, and capabilities; shared workflow does not unify those semantics.

## Do's and Don'ts

### Do

- Use multiple platforms when they meet actual architecture or orchestration needs.
- Evaluate team ownership, state boundaries, outage independence, provider maturity, rate limits, blast radius, and credential boundaries.
- Pin and review provider selections, and upgrade deliberately to maintain security and compatibility.
- Retain provider-specific operational knowledge and account for platform/API limitations.

### Don't

- Claim seamless portability or identical security, availability, or replacement behavior between equivalent-looking resources.
- Add a platform merely to claim portability.
- Assume one configuration/state is always safer; it may couple dependencies and failure boundaries.
- Confuse service-agnostic with provider-free: each managed service still needs an appropriate provider.

## Real-life implementation

A hybrid application might provision a cloud network and configure an identity or SaaS service from one Terraform workflow. First verify actual provider maturity and supported schemas; define whether the cross-system dependency belongs in one state or separate ownership/state boundaries. Apply least-privilege credentials, review provider versions and plans, and assess outage coupling, rate limits, and blast radius. The code above is illustrative; concrete resources and credentials are provider-dependent.

## Q&A

1. **What connects Terraform to platforms/services?** Provider plugins.
2. **What is unified across providers?** Core workflow and configuration/state mechanisms, not service semantics.
3. **Can one configuration reference resources across providers?** Yes, and references can establish dependencies.
4. **Does “service-agnostic” mean provider-free?** No, each managed service is accessed through an appropriate provider.
5. **Does multi-cloud support imply seamless portability?** No; provider APIs and service capabilities differ.

## Official references

- [Providers overview](https://developer.hashicorp.com/terraform/language/providers)
- [Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [Provider configuration](https://developer.hashicorp.com/terraform/language/providers/configuration)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
