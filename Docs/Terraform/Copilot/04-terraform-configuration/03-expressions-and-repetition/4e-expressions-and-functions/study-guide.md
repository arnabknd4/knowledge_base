# 4e — Write dynamic configuration using expressions and functions

## What

Terraform expressions combine literals, references, operators, conditionals, function calls, and `for` expressions to compute values. A conditional has the form `condition ? true_value : false_value`; `for` expressions transform collections into lists, tuples, maps, or objects. Built-in functions perform operations such as lookup, filtering, conversion, and string/list/map transformation. Terraform does not support user-defined functions.

`count` and `for_each` expand one resource or module block into multiple instances. `count` assigns numeric indices, usually fitting a simple quantity. `for_each` uses a map or set of strings and gives instances stable keys, which is usually clearer when each instance has identity or configuration of its own. Instance keys must be known before Terraform performs remote operations.

## Why

Stable keys reduce accidental replacements or state-address churn. If a `count` list is reordered, indexed instances can appear to change identity; inserting/removing map entries with semantic keys more accurately adds or removes a specific instance. `count` is appropriate for homogeneous, numerically addressed replicas. Choose one based on identity, not just syntax preference.

Keep expressions readable and bounded. Complex comprehensions can obscure intent, and overly dynamic configuration is harder to review than a small explicit map. Functions are evaluated in Terraform's expression context; provider-returned values can be unknown during planning, and a `for_each` key set cannot depend on values available only after apply.

## How

```hcl
variable "subnets" {
  type = map(string)
}

variable "large" {
  type    = bool
  default = false
}

resource "terraform_data" "node" {
  for_each = var.subnets
  input = {
    subnet = each.value
    name   = "node-${each.key}"
    size   = var.large ? "large" : "small"
  }
}

locals {
  subnet_ids = [for name, id in var.subnets : id if startswith(name, "app-")]
}
```

`each.key` identifies the map key and `each.value` the associated value. Interpolation (`"node-${each.key}"`) is only needed within a larger string; a standalone expression can be written directly as `value = each.value`. A function call such as `startswith` returns a value used by the `for` expression's filter.

## Features

- A function is called in an expression; it is not an interpolated string.
- `for` expressions transform values; `for_each` repeats resource/module instances.
- `count` instances have numeric indices; `for_each` instances have keys.
- `for_each` keys (and set members) must be known during planning, before remote operations.

## Do's and Don'ts

### Do

- Use expressions, built-in functions, and `for` comprehensions to derive readable values from inputs.
- Choose `for_each` for meaningful stable keys and `count` for simple homogeneous quantities.
- Keep all `for_each` keys/set members known during planning.

### Don't

- Do not confuse a `for` expression (constructs a value) with `for_each` (repeats blocks).
- Do not build keys from values known only after remote creation.
- Do not over-compress logic into nested expressions that obscure the desired configuration.

## Real-life implementation

For a sandbox service catalog, use a map keyed by service name and `for_each` to create one `terraform_data` record per entry; use a `for` expression to derive a filtered list of enabled subnet IDs, and a conditional to select a non-production size. Inspect the plan to confirm stable instance keys. `terraform_data` is a built-in resource type; the example demonstrates Terraform language behavior rather than a cloud-provider schema.

## Q&A

**Q:** When is `for_each` often preferable to `count`?  
**A:** When each instance has a meaningful stable identity/key.

**Q:** What are `each.key` and `each.value`?  
**A:** The current for_each key and associated value.

**Q:** What is the difference between `for` and `for_each`?  
**A:** `for` builds a collection value; `for_each` creates repeated blocks/instances.

**Q:** When is interpolation required?  
**A:** When embedding an expression inside a larger string; a standalone value can be referenced directly.

Further reading: [Expressions](https://developer.hashicorp.com/terraform/language/expressions), [for expressions](https://developer.hashicorp.com/terraform/language/expressions/for), [count](https://developer.hashicorp.com/terraform/language/meta-arguments/count), [for_each](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each), [Functions](https://developer.hashicorp.com/terraform/language/functions).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
