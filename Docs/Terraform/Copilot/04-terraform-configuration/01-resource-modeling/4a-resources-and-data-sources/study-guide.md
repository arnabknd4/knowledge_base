# 4a — Use and differentiate `resource` and `data` blocks

## What

A `resource` block declares an object Terraform should manage: Terraform can create it, update it, replace it, or destroy it according to configuration and lifecycle behavior. A `data` block declares a read-only lookup of information supplied by a provider or another source. Data sources are useful for discovering objects managed elsewhere or obtaining values needed to configure resources; they do not transfer lifecycle ownership to the current configuration.

Both blocks use provider-defined types and arguments, so resource/data schemas vary by provider. The first label is the provider-specific type and the second is the local name. Within the module, the address of a resource is `TYPE.NAME`; the address of a data source begins `data.TYPE.NAME`.

## Why

Be explicit about ownership. Use resources for objects whose lifecycle this state should control; use data sources to consume externally managed objects. Accidentally declaring a duplicate resource rather than looking up a shared object can create competing ownership. Conversely, relying on a data source for something the stack should own leaves its lifecycle outside Terraform's change graph.

Data source reads still rely on provider credentials and remote availability. Their values can change between runs, so constrain lookups appropriately and consider whether reproducibility requires pinning or passing a stable identifier. A data source's outputs can also appear in state and plans; read-only does not mean non-sensitive.

## How

Provider-specific HCL example is illustrative; verify the exact arguments and behavior against the documentation for the selected provider version.

```hcl
data "aws_ami" "approved" {
  most_recent = true
  owners      = ["123456789012"]
  filter {
    name   = "name"
    values = ["approved-linux-*"]
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.approved.id
  instance_type = "t3.small"
}
```

Here the data source queries an image; the resource declares a virtual machine that this configuration owns. A data-source result may be read during planning when its inputs are known, or deferred until apply if it depends on values that are not yet known.

## Features

- `resource` manages lifecycle; `data` reads/queries and does not manage the looked-up object.
- `data` is part of the resource graph and can provide inputs/dependencies.
- A successful data lookup does not mean Terraform owns or will destroy that object.
- `data.TYPE.NAME` addresses a data source; ordinary `TYPE.NAME` is a managed resource.

## Do's and Don'ts

### Do

- Choose `resource` only when this state should own the object's lifecycle; use `data` to read externally owned information.
- Constrain lookups and use stable identifiers where reproducibility matters.
- Review data-source values for sensitivity even though the lookup is read-only.

### Don't

- Do not declare a shared externally owned object as a competing managed resource.
- Do not expect Terraform to destroy an object read through a data source.
- Do not equate read-only with local-only or nonsensitive; provider queries contact APIs and values can enter state.

## Real-life implementation

For a sandbox application, use a data source to select an approved image owned by the platform team, then use a resource for the disposable VM that the sandbox stack owns. Confirm the data lookup is constrained to the intended account/owner and inspect the plan to distinguish the read from the managed create. The AWS HCL is provider-specific and illustrative; use the schema and version required by the selected AWS provider.

## Q&A

**Q:** Which block should declare a new object this stack owns?  
**A:** `resource`.

**Q:** Which block looks up an existing or externally provided value?  
**A:** `data`.

**Q:** Does Terraform destroy an object read through a data block?  
**A:** No, the data source is read-only.

**Q:** Why can a data source still fail during plan?  
**A:** Provider access, lookup constraints, remote availability, or unknown inputs may prevent the read.

Further reading: [Resources](https://developer.hashicorp.com/terraform/language/resources), [Data sources](https://developer.hashicorp.com/terraform/language/data-sources).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
