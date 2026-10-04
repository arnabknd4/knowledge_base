# 4g — Validate configuration using custom conditions

## What

Custom conditions express assumptions and invariants that Terraform's syntax/type checks cannot know. Three constructs have different enforcement semantics:

- **Variable validation** checks caller-provided input as Terraform evaluates the module. A false condition produces an error and prevents planning/applying with that input.
- **Preconditions** assert that a resource, data source, or output is safe/valid before the associated operation or value is used. A failed precondition is an error and blocks the relevant operation.
- **Postconditions** assert something about a data-source result or managed resource after it is read/created/updated. A failed postcondition is an error; Terraform stops dependent operations from proceeding, though an already completed remote operation is not magically rolled back.
- A **`check` block** evaluates assertions during plan/apply to monitor an assumption. A failed check emits a warning but does not block the operation. It is suited to reporting health assumptions whenever Terraform runs, not to background monitoring or a hard gate.

## Why

Put each rule at the right boundary: variable validation checks input contracts early; preconditions guard an operation against unsafe prerequisites; postconditions verify observed results; checks surface ongoing operational assumptions without making ordinary resource reconciliation fail. Clear `error_message` text should explain the violated rule and remediation.

A postcondition failure occurs after a read or write may already have happened. Plan for partial effects and inspect the subsequent plan/state. Do not use a `check` block as a security or compliance gate expecting a nonzero failure that blocks deployment. For hard policy enforcement, use a blocking condition or a dedicated policy mechanism.

## How

```hcl
variable "port" {
  type = number
  validation {
    condition     = var.port > 0 && var.port < 65536
    error_message = "port must be between 1 and 65535."
  }
}

resource "terraform_data" "app" {
  input = var.port
  lifecycle {
    precondition {
      condition     = var.port != 22
      error_message = "The application service must not use the administration port."
    }
    postcondition {
      condition     = self.output == var.port
      error_message = "The recorded service input does not match the requested port."
    }
  }
}

check "valid_port" {
  assert {
    condition     = var.port > 0 && var.port < 65536
    error_message = "The configured port is outside the valid range."
  }
}
```

A `check` block can include a data-source query and assert a condition about its result, such as endpoint health, reporting a warning without stopping apply. The example uses a direct assertion to make the warning behavior visible. Checks run as part of Terraform plan/apply; they are not a continuously running monitor. Conditions can reference values available in their context; a condition may be deferred when values are unknown until apply.

## Features

- Failed variable validation, preconditions, and postconditions are blocking errors.
- Failed `check` assertions are warnings and do not block Terraform operations.
- Postcondition failure is not a transactional rollback of an already completed provider operation.
- Validation blocks enforce module input constraints; they are not equivalent to CLI `terraform validate`.

## Do's and Don'ts

### Do

- Put input contracts in variable validation, operation safeguards in preconditions, and result assertions in postconditions.
- Use check blocks for non-blocking operational assertions, not enforcement.
- Write actionable error messages and account for values that are unknown until apply.

### Don't

- Do not use a warning-only check as a security or compliance gate.
- Do not assume a failed postcondition rolls back an already completed provider operation.
- Do not confuse a variable validation rule with the CLI `terraform validate` command.

## Real-life implementation

In a safe sandbox module, validate a configurable service port as an input contract, add a precondition that rejects a prohibited administrative port, and use a postcondition to verify a resulting attribute. Add a `check` assertion only for an operational assumption where a warning is acceptable. A failed postcondition can follow an already completed remote action, so inspect state and plan. The `terraform_data` example is built-in and provider-independent.

## Q&A

**Q:** Which construct validates an input variable's value?  
**A:** `validation` inside a `variable` block.

**Q:** Which rule applies before a resource operation?  
**A:** A lifecycle `precondition`.

**Q:** What happens when a `check` assertion fails?  
**A:** Terraform reports a warning and continues rather than blocking.

**Q:** Does failed postcondition undo creation?  
**A:** No; it reports an error and prevents dependent steps, but does not guarantee rollback.

Further reading: [Custom conditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions), [Variable validation](https://developer.hashicorp.com/terraform/language/values/variables#custom-validation-rules), [Lifecycle preconditions and postconditions](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#precondition-and-postcondition), [Check blocks](https://developer.hashicorp.com/terraform/language/checks).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
