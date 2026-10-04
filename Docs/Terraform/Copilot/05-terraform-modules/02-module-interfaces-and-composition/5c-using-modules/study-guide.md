# 5c — Use modules in configuration

## What

A `module` block creates an instance of a child module. Its label contributes to the caller-side address; `source` selects the module code; named arguments map caller expressions to the child's declared input variables. A child output is read with `module.<label>.<output>`.

```hcl
module "network" {
  source      = "./modules/network"
  environment = var.environment
  cidr_block  = var.vpc_cidr
}

module "service" {
  source     = "./modules/service"
  subnet_ids = module.network.private_subnet_ids
}

output "service_endpoint" {
  value = module.service.endpoint
}
```

## Why

Modules package infrastructure capabilities behind explicit contracts. Good composition makes data flow, dependencies, ownership, and lifecycle boundaries clear. The root module should orchestrate environment-specific choices; child modules implement cohesive capabilities. A module is not inherently remote or published—local modules are common.

Module boundaries should balance reuse and coordination: overly broad modules couple unrelated lifecycles, while excessively tiny modules add indirection and release/version overhead.

## How

Pass values through child inputs and consume declared outputs. A reference from one module's output to another module's input creates an implicit dependency in Terraform's graph. Prefer this data dependency to `depends_on`; explicit dependencies are for genuine ordering relationships that are not represented by values. `for_each` or `count` can instantiate repeated modules, so design stable keys and addresses.

Run `terraform init` after adding or changing module sources, then format, validate, and review a plan. Module call labels appear in resource addresses (`module.network...`). Renaming a label can make Terraform interpret existing objects as different addresses; preserve identity with an appropriate `moved` block when the objects are unchanged. Child modules declare provider requirements, while provider configurations are generally supplied by the root/caller and passed according to provider configuration rules—not as ordinary input values.

## Features

- Named module arguments bind caller expressions to child input variables.
- Module outputs are the public values available to other modules or the root.
- Output references form implicit graph dependencies and enable parallel planning where possible.
- `count` and `for_each` support repeated module instances, with address/key lifecycle consequences.
- Module labels are part of state addresses and should be treated as meaningful identifiers.

## Do's and Don'ts

**Do**
- Organize modules around a coherent capability, clear owner, interface, and expected change cadence.
- Prefer output-to-input references for normal dependency ordering.
- Test interfaces and review plans after source or module-label changes.
- Make resource keys and module addresses stable when using repeated instances.

**Don't**
- Expect callers to access child resources, variables, or locals directly.
- Add broad, redundant `depends_on` relationships that hide data flow or suppress parallelism.
- Assume a module call is a provider configuration.
- Rename labels or alter `for_each` keys without understanding address changes and state migration.

## Real-life implementation

A production root can compose network, identity, and service modules: create the network, pass its subnet outputs to the service module, and pass identity outputs where needed. Each reusable module owns a bounded capability and exposes typed, documented inputs and outputs; the root chooses environment-specific sizing and version/source policy. Validate in CI and review plan addresses before rollout. If a module label or internal resource address must change without replacing live objects, include and test the corresponding `moved` mappings, coordinate them across all state instances, and retain the mappings until every relevant workspace has applied the refactor.

## Q&A

1. **What does the module label determine?** Its caller-side address and the name used in `module.<label>...` references.
2. **What normally orders a consumer after a producer module?** A reference to the producer's output, which forms an implicit dependency.
3. **Can a root reference a child resource directly?** No. The child must expose an output that the root consumes.
4. **What should follow adding a module source?** Run `terraform init`, then validate and inspect the plan.

**Official references:**

- [Modules overview and composition](https://developer.hashicorp.com/terraform/language/modules)
- [Module block syntax](https://developer.hashicorp.com/terraform/language/modules/syntax)
- [Module output values](https://developer.hashicorp.com/terraform/language/values/outputs)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
