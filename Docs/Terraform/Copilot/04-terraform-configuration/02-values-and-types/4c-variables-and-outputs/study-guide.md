# 4c — Use variables and outputs

## What

Input variables parameterize a module; callers provide values without editing the module's implementation. Declare type constraints to validate shape and enable useful conversions, descriptions to communicate intent, and defaults only when there is a meaningful safe default. Root-module values can be supplied by CLI options, variable files, environment variables, or interactive input. Child modules receive arguments explicitly from their caller.

Outputs publish selected values from a module. A root module can display outputs after apply and retrieve them with `terraform output`; a calling module can read child outputs as `module.CHILD.OUTPUT`. Outputs form part of a module's interface and should expose only what consumers need. Marking an output sensitive suppresses normal CLI display, but does not by itself remove its value from state.

## Why

Inputs are a contract: narrow types and descriptions make module use predictable; validation rules can enforce domain-specific constraints. Separate environment data from reusable module logic. A default should not silently select a dangerous production setting. Outputs are also an interface and can be consumed by automation or other modules, so changes to names or shapes can be breaking.

`sensitive = true` is a display/dataflow marking, not encryption or a guarantee that values are absent from persisted state or plan files. Restrict access to state, plans, logs, and CI output. Use secure secret-delivery mechanisms and ephemeral/write-only features where appropriate (objective 4h).

## How

Provider-specific HCL example is illustrative; verify the exact arguments and behavior against the documentation for the selected provider version.

```hcl
variable "instance_count" {
  type        = number
  description = "Number of application instances."
  default     = 2
}

variable "api_token" {
  type      = string
  sensitive = true
}

output "instance_ids" {
  value = aws_instance.app[*].id
}
```

Supply values using an auto-loaded `terraform.tfvars` or `*.auto.tfvars` file, an explicit `-var-file=env.tfvars`, `-var='instance_count=3'`, or an environment variable such as `TF_VAR_instance_count=3`. CLI `-var`/`-var-file` assignments take precedence over lower-precedence sources such as environment values and defaults. Avoid putting secrets directly on command lines or in committed variable files.

## Features

- Input variables enter a module; outputs leave it.
- Child-module inputs are passed explicitly by the caller; they are not automatically inherited from root variables.
- Sensitivity redacts ordinary display but does not prevent state persistence.
- `TF_VAR_name` uses the variable name after the prefix; explicit CLI assignments generally have higher precedence than environment assignments.

## Do's and Don'ts

### Do

- Define narrow input types, clear descriptions, and validation for module contracts.
- Pass child-module values explicitly and expose only intentional outputs.
- Keep state, plan files, variable files, and CI output access-controlled when sensitive values are involved.

### Don't

- Do not place secrets in committed `.tfvars`, command history, or unprotected logs.
- Do not assume child modules inherit root variables without arguments.
- Do not treat `sensitive = true` as encryption or state omission.

## Real-life implementation

For a sandbox module, let the root caller provide a typed instance size and count, pass those values explicitly into a child module, and expose only the created identifiers needed by downstream automation. Provide nonsecret environment values through a protected variable file. Keep any credential out of source and restrict state/plan access; sensitivity redacts normal display but does not remove values from persistence.

## Q&A

**Q:** How does a caller set a child module variable?  
**A:** Pass a named argument in the `module` block.

**Q:** What is the use of a type constraint?  
**A:** It constrains/checks the input shape and improves expression behavior.

**Q:** How does a root module expose a value?  
**A:** Declare an output; callers use `module.NAME.OUTPUT`.

**Q:** Does `sensitive = true` remove a secret from state?  
**A:** No; it primarily controls display and sensitive propagation.

Further reading: [Input variables](https://developer.hashicorp.com/terraform/language/values/variables), [Output values](https://developer.hashicorp.com/terraform/language/values/outputs), [Assigning values](https://developer.hashicorp.com/terraform/language/values/variables#assigning-values-to-root-module-variables).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
