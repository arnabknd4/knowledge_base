# 5b — Describe variable scope within modules

## What

Each module is a scope boundary. Its input variables are parameters, its outputs are the values it deliberately returns, and its local values are private derived expressions. Terraform does not implicitly inherit caller variables or locals; callers pass inputs in a `module` block, and consumers access child outputs as `module.<call-label>.<output-name>`.

```hcl
# Root module
variable "region" { type = string }
locals { environment = "production" }

module "cluster" {
  source      = "./modules/cluster"
  region      = var.region
  environment = local.environment
}

output "cluster_name" {
  value = module.cluster.name
}
```

The child declares its own interface:

```hcl
variable "region"      { type = string }
variable "environment" { type = string }

locals {
  name = "${var.environment}-cluster"
}

output "name" {
  value = local.name
}
```

The child's `var.region` is distinct from the root's `var.region`; the caller supplies its value through the module argument. Filenames within a module directory do not create scopes.

## Why

Explicit contracts make module dependencies and data flow visible, enable independent testing and reuse, and keep implementation details private. Typed and validated inputs document invariants. Outputs create intentional public surfaces rather than exposing child resources or locals directly.

Sensitive values require additional care: `sensitive = true` redacts many CLI displays, but does not encrypt state or guarantee a value is absent from logs or plans. State access and storage must still be secured.

## How

Declare each input variable in the receiving module. A required input without a default must be supplied by the caller; optional inputs may have safe, intentional defaults. The module author declares which outputs to expose, and callers reference only those outputs. A same-named variable or local in the caller and child does not create shared scope. Provider configurations have their own inheritance and alias rules; they are not ordinary module input variables.

## Features

- Child inputs are assigned through named arguments in the caller's `module` block.
- Child outputs are referenced by the caller as `module.<label>.<output>`.
- Locals are private to the module in which they are declared.
- Input types, validations, defaults, and sensitive markings help define the interface.
- Provider requirements/configurations are distinct from the ordinary variable interface.

## Do's and Don'ts

**Do**
- Define a small, intentional interface using precise types and validations.
- Pass caller values explicitly to child inputs.
- Expose only outputs consumers need and document compatibility expectations.
- Secure state and logs even when values are marked sensitive.

**Don't**
- Expect a child to read a caller's variables or locals automatically.
- Treat an output as a global variable or a way to access arbitrary child internals.
- Use defaults for required production decisions when doing so would hide unsafe assumptions.
- Pass secrets unnecessarily or assume `sensitive = true` encrypts them.

## Real-life implementation

In a production cluster module, accept the region, environment, network identifiers, and explicitly approved sizing options as typed inputs; validate required naming and CIDR invariants at the boundary. Derive internal names and tags with child locals. Return only stable consumer values such as cluster name, endpoint, and security-group IDs. The root module obtains credentials and supplies the intended region and network outputs from other modules. Document state sensitivity and use a protected backend with least-privilege access; do not treat output redaction as a secrets-management system.

## Q&A

1. **Can a child read `local.region` from its caller?** No. Pass the value to a child input declared by that module.
2. **How does the caller consume a child value?** Through `module.<call-label>.<output-name>`.
3. **Does `sensitive = true` encrypt a value in state?** No. It is a display-redaction signal; storage and access still need protection.
4. **Where are an input's type and default declared?** In the module receiving that input.

**Official references:**

- [Input variables](https://developer.hashicorp.com/terraform/language/values/variables)
- [Local values](https://developer.hashicorp.com/terraform/language/values/locals)
- [Output values](https://developer.hashicorp.com/terraform/language/values/outputs)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
