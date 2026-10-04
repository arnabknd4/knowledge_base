# 4f — Define resource dependencies in configuration

## What

Terraform constructs a dependency graph from references and explicit meta-arguments. A reference from one resource to another creates an **implicit dependency**: the producer must be available before the consumer can use its value. Terraform can then schedule independent graph nodes in parallel and reverse dependencies during destruction. Prefer implicit dependencies because they express both the value flow and the required order.

Use `depends_on` for a real dependency that cannot be represented by an expression—for example, a consumer needs a service account's permissions to have taken effect, but consumes no attribute from the permission resource. `depends_on` is a list of resource/module references; it adds ordering without passing an attribute value.

## Why

Explicit dependencies should be narrow and rare. Broad `depends_on` entries can make values more conservative/unknown during planning and serialize operations, reducing parallelism. Over-specification hides missing value relationships; cyclic edges make a valid graph impossible. Depend on the smallest object that reflects the actual prerequisite.

`create_before_destroy` can reduce downtime, but it requires the platform to allow old and new objects to coexist—unique names, quotas, and external constraints can prevent it. It may propagate through dependencies so that ordering remains valid. It cannot guarantee zero downtime for applications or a seamless cutover; health checks, traffic shifting, and compatibility remain architectural concerns. Terraform lifecycle settings affect Terraform's graph/actions, not provider capabilities.

## How

```hcl
variable "revision" {
  type = string
}

resource "terraform_data" "policy" {
  input = "policy for ${var.revision}"
}

resource "terraform_data" "service" {
  triggers_replace = var.revision

  lifecycle {
    create_before_destroy = true
  }
}

resource "terraform_data" "deployment" {
  input      = terraform_data.service.id
  depends_on = [terraform_data.policy]
}
```

`terraform_data` is built into Terraform and makes the example provider-independent. The deployment's expression creates an implicit service dependency; its explicit dependency represents the additional policy-before-deployment ordering. Changing `revision` forces the service to be replaced. `create_before_destroy` changes that replacement behavior: Terraform attempts to create a replacement instance before destroying the old one rather than destroy-first.

## Features

- Attribute references create implicit dependencies; they are not merely string substitutions.
- Use `depends_on` when a genuine dependency has no data reference to express it.
- `create_before_destroy` means new-before-old for replacement, not “never destroy.”
- Cycles and unnecessary dependencies can block or over-serialize operations.

## Do's and Don'ts

### Do

- Prefer implicit dependencies through attribute references.
- Add a narrow `depends_on` only for an actual ordering requirement that has no expression representing it.
- Evaluate replacement coexistence, quotas, naming, and cutover before using `create_before_destroy`.

### Don't

- Do not add broad dependencies that serialize unrelated work or make values more conservative.
- Do not assume `create_before_destroy` prevents deletion or guarantees zero downtime.
- Do not introduce cycles; they make graph ordering impossible.

## Real-life implementation

In a sandbox deployment, model a real service-consumption reference so Terraform automatically orders the dependent operation. If a permission activation has no usable output reference but must precede deployment, add a narrowly scoped `depends_on`. Test replacement with `create_before_destroy` only where old/new objects can coexist; the `terraform_data` example is provider-independent, while real provider constraints vary.

## Q&A

**Q:** Which kind of dependency should be preferred?  
**A:** Implicit reference-based dependencies.

**Q:** What does explicit `depends_on` add?  
**A:** An ordering edge when no attribute reference captures the dependency.

**Q:** How does `create_before_destroy` change replacement order?  
**A:** Create replacement first, then destroy the old instance.

**Q:** Name one constraint it cannot solve.  
**A:** The platform may disallow simultaneous instances due to name uniqueness, quota, or application cutover requirements.

Further reading: [Resource dependencies](https://developer.hashicorp.com/terraform/language/resources/behavior#resource-dependencies), [depends_on](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on), [Lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
