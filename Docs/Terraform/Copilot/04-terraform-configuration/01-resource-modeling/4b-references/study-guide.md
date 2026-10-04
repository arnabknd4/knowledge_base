# 4b — Refer to resource attributes and create cross-resource references

## What

Terraform expressions refer to named values with traversals. A managed resource reference has the form `TYPE.NAME.ATTRIBUTE`; a data source reference begins `data.TYPE.NAME.ATTRIBUTE`. Input variables use `var.NAME`, locals use `local.NAME`, and outputs expose a module result. References let configuration consume provider-returned attributes and other values rather than hard-coding identifiers.

A resource reference has a second meaning: it establishes an **implicit dependency**. If resource B uses an attribute from resource A, Terraform knows A must be created or updated before B can use that value, and generally destroys B before A. Terraform builds this relationship into its dependency graph.

## Why

Prefer references to literals when a value is produced elsewhere in the graph. This preserves the link between configuration and the actual object identity and enables correct ordering, parallelism, and replacement propagation. Avoid building dependency cycles: if A needs an attribute from B and B simultaneously needs one from A, Terraform cannot find a valid creation order.

References also affect value knownness. A provider-generated ID may remain unknown during planning when its producer is not yet created; downstream values can display “known after apply.” A reference should communicate a real data dependency rather than be added solely to force ordering. For a genuine dependency with no suitable value reference, use `depends_on` deliberately (objective 4f).

## How

Provider-specific HCL example is illustrative; verify the exact arguments and behavior against the documentation for the selected provider version.

```hcl
resource "aws_security_group" "app" {
  name = "app-access"
}

resource "aws_instance" "app" {
  ami                    = var.ami_id
  instance_type          = "t3.small"
  vpc_security_group_ids = [aws_security_group.app.id]
}
```

The expression `aws_security_group.app.id` is an attribute reference and tells Terraform that the instance depends on the security group. If repeated with `for_each`, a particular instance address may include a key such as `aws_instance.app["blue"]`; with `count`, it may include an index such as `aws_instance.app[0]`. Address syntax matters when reading plans and state.

## Features

- Resource references yield values **and** implicit graph edges.
- A reference to an attribute does not mean the referenced object is created during validation; planning/apply determine runtime values.
- `data.TYPE.NAME.ATTRIBUTE`, `var.NAME`, and `local.NAME` are distinct namespaces.
- Indexed addresses include keys/indices for repeated instances; they are not just the unindexed block name.

## Do's and Don'ts

### Do

- Reference the producer's actual attribute instead of copying an identifier into configuration.
- Let data references express real ordering and value dependencies; use explicit dependency only when a real prerequisite has no value flow.
- Read indexed or keyed addresses carefully in plans and state.

### Don't

- Do not create cyclic references; Terraform cannot topologically order a dependency cycle.
- Do not add `depends_on` merely to silence uncertainty or force unrelated ordering.
- Do not assume provider-generated attributes are known during planning.

## Real-life implementation

A sandbox network stack can create a security group and pass `aws_security_group.app.id` into an instance's security-group argument. The reference both supplies the value and orders creation; the plan may show the ID as unknown until apply. Confirm the intended resource addresses before applying. This AWS HCL is provider-specific and illustrative; verify arguments against the pinned provider documentation.

## Q&A

**Q:** What is the resource reference pattern?  
**A:** `TYPE.NAME.ATTRIBUTE`.

**Q:** What graph effect does a reference create?  
**A:** An implicit dependency from the consumer to the producer.

**Q:** Why might a referenced attribute be unknown in a plan?  
**A:** Its value is provider-generated or depends on an operation that has not run.

**Q:** When is explicit `depends_on` useful?  
**A:** When a real ordering dependency exists but no value reference expresses it.

Further reading: [References to named values](https://developer.hashicorp.com/terraform/language/expressions/references), [Expressions](https://developer.hashicorp.com/terraform/language/expressions).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
