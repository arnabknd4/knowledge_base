# 4h — Manage sensitive data, including secrets management with Vault

## What

Terraform configuration, plans, state, provider logs, and CI output can all become exposure paths for secrets. The `sensitive` marking redacts values from normal CLI/UI display and propagates sensitivity through expressions, but it does **not** encrypt a value, keep it out of state, or prevent an authorized state reader from obtaining it. Protect state and saved plans with access controls, encryption at rest/in transit, short retention, and careful logging.

Terraform's newer ephemeral mechanisms address persistence rather than display. Ephemeral values (including ephemeral input variables/resources where supported) can be used only in permitted contexts and are omitted from state and plan files. Provider **write-only arguments** allow a value to be sent to a remote API without Terraform reading it back into persisted state; support is provider/resource-specific. Neither capability is a universal replacement for secure credential delivery or provider support.

## Why

Prefer short-lived credentials obtained at runtime using workload identity or a secrets manager. HashiCorp Vault can centralize secret lifecycle and policy: Terraform can authenticate to Vault and retrieve a secret or use dynamic credentials with limited lifetime. Minimize the number of secrets Terraform needs to read, never hard-code values, and avoid committing secret-bearing `.tfvars` or plan files. A data source returning a secret may still put it in Terraform's state; “fetched from Vault” does not automatically mean “not persisted.”

Ephemeral values are deliberately constrained; they can flow only to contexts Terraform allows, such as other ephemeral values or supported write-only arguments. Choose a write-only interface where available, and rotate/update associated version markers as required by that provider. Protect logs because diagnostics may reveal request details or configuration.

## How

Provider-specific HCL example is illustrative; verify the exact arguments and behavior against the documentation for the selected provider version.

```hcl
variable "bootstrap_token" {
  type      = string
  sensitive = true
  ephemeral = true
}

resource "example_service" "app" {
  bootstrap_token_wo         = var.bootstrap_token
  bootstrap_token_wo_version = 1
}
```

This illustrates the Terraform 1.12 language concepts; the exact write-only argument names and version field are defined by the resource provider schema and must be checked in that provider's documentation. If a provider has no compatible write-only argument, an ordinary sensitive argument can still be persisted in plan/state.

## Features

- `sensitive = true` controls display; it does not remove a value from state/plan.
- Ephemeral values are intended not to be stored in state or plan, unlike ordinary sensitive values.
- Write-only is a provider argument capability and is distinct from marking an ordinary argument sensitive.
- A Vault-backed lookup can still be persisted when consumed through an ordinary Terraform value/resource argument.

## Do's and Don'ts

### Do

- Prefer short-lived runtime credentials and least-privilege access; minimize secrets Terraform must handle.
- Protect state, saved plans, logs, and CI artifacts even when values are marked sensitive.
- Use ephemeral values and provider-supported write-only arguments when their constraints and schemas fit the use case.

### Don't

- Do not hard-code secrets or commit secret-bearing variable/plan files.
- Do not assume sensitivity encrypts a value, omits it from state, or prevents an authorized state reader from seeing it.
- Do not assume a Vault lookup or write-only feature is universal; verify the actual data flow and provider support.

## Real-life implementation

In a sandbox, obtain a short-lived bootstrap credential at runtime, pass it through an ephemeral variable, and use a provider resource's documented write-only argument if available. Confirm the plan/state handling and secure CI logs/artifacts. If no write-only destination exists, assume an ordinary sensitive argument may persist in state and apply stricter controls or redesign the workflow. The `example_service` argument names are provider-specific placeholders and illustrative only; check the chosen provider's schema.

## Q&A

**Q:** Does sensitive marking encrypt state?  
**A:** No; state security is a backend/storage/access-control responsibility.

**Q:** What persistence distinction does ephemeral provide?  
**A:** Supported ephemeral values are not recorded in state or plan files.

**Q:** What makes a write-only argument different?  
**A:** The provider accepts the value without returning/storing it as a normal readable resource attribute.

**Q:** Does retrieving a credential from Vault guarantee it never reaches state?  
**A:** No; the Terraform data flow and destination arguments determine persistence.

Further reading: [Sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data), [Ephemeral values](https://developer.hashicorp.com/terraform/language/manage-sensitive-data/ephemeral), [Vault provider](https://registry.terraform.io/providers/hashicorp/vault/latest/docs), [Terraform state security](https://developer.hashicorp.com/terraform/language/state/sensitive-data).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
