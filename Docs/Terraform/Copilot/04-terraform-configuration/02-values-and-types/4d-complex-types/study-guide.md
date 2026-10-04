# 4d — Understand and use complex types

## What

Terraform values have primitive or compound types. Primitive types are `string`, `number`, and `bool`. Collection types hold values of a common element type: `list(T)` is ordered and indexable, `set(T)` is unordered and unique, and `map(T)` associates string keys with values of one element type. Structural types describe a fixed shape: `object({ ... })` has named attributes that can have different types, while `tuple([ ... ])` has a fixed number of elements whose types can differ by position.

Type constraints make module interfaces explicit. A value's shape influences how expressions work: lists and tuples support index access, maps and objects support key/attribute access, and sets do not promise stable ordering or duplicate entries. Terraform may perform some automatic conversions, so use explicit constraints and inspect actual values rather than rely on accidental coercion.

## Why

Choose types that describe the consumer's actual need. Use a map when stable semantic keys matter, such as `for_each` resource identity; use a list when order matters; use a set when membership and uniqueness matter but order does not. Objects give complex inputs a documented schema and help callers discover required attributes. Tuples are useful for fixed positional structures but tend to be less readable as public module interfaces.

Type design affects changes. A `for_each` map keyed by durable names gives stable instance addresses; a positional `count` list can shift addresses when elements are inserted or reordered. Optional object attributes and conversions should be used intentionally, with defaults that preserve clear semantics.

## How

```hcl
variable "services" {
  type = map(object({
    port    = number
    enabled = bool
  }))
}

locals {
  enabled_services = {
    for name, service in var.services : name => service
    if service.enabled
  }
}
```

An example input could be `services = { api = { port = 8080, enabled = true } }`. The outer map is keyed by service name; each value is an object with a numeric port and boolean flag. A separate `list(string)` would preserve caller order, whereas `set(string)` would represent distinct values without an ordering contract.

## Features

- Lists are ordered; sets are unordered and unique; maps are key/value collections.
- `object` is a named-attribute structure; `tuple` is positional with per-position types.
- A set should not be treated as an ordered sequence.
- Terraform type conversions do not make unrelated shapes equivalent; the declared contract still matters.

## Do's and Don'ts

### Do

- Choose list, set, map, object, or tuple based on ordering, uniqueness, keys, and shape.
- Use documented object constraints for structured module inputs.
- Prefer durable semantic map keys for repeated resource identities.

### Don't

- Do not depend on set ordering or treat a set as a stable sequence.
- Do not use positional `count` identity when list reordering would unintentionally change which object an index represents.
- Do not rely on accidental type conversion instead of declaring the input contract.

## Real-life implementation

A sandbox module can accept a `map(object(...))` keyed by stable service names, with each object describing a port and enabled flag. Feed enabled entries to `for_each` so adding a service creates a keyed instance instead of shifting numeric indexes. Use a list only where order is semantically meaningful; use a set for unique membership without order.

## Q&A

**Q:** Which type supports unique membership without ordering?  
**A:** `set(T)`.

**Q:** Which compound type has named attributes of possibly different types?  
**A:** `object`.

**Q:** Which type uses a fixed sequence of possibly different element types?  
**A:** `tuple`.

**Q:** Why use durable map keys for repeated resources?  
**A:** They provide stable, meaningful instance addresses for `for_each`.

Further reading: [Type constraints](https://developer.hashicorp.com/terraform/language/expressions/type-constraints), [Values and types](https://developer.hashicorp.com/terraform/language/expressions/types).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
