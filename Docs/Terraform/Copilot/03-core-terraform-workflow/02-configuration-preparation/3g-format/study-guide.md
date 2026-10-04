# 3g — Apply formatting and style adjustments

## What

`terraform fmt` rewrites Terraform language files into Terraform's canonical style. It standardizes indentation, spacing, and layout so reviewers can focus on configuration intent instead of formatting differences. Formatting is a source-code hygiene operation: it does not change desired infrastructure semantics, initialize dependencies, validate a configuration, or execute a plan.

The formatter applies consistent conventions across a directory. A canonical file can still contain an invalid argument, an incorrect type, a dangerous destroy, or a secret. Formatting is therefore complementary to validation, planning, policy checks, and secret scanning rather than a replacement for them.

## Why

Consistent formatting reduces review noise across teams and makes code ownership easier when many modules and environments share a repository. A formatter check in CI makes style deterministic instead of relying on individual editor settings. It is safe to run repeatedly: once formatted, the file remains unchanged on subsequent runs.

The canonical style should not be mistaken for architectural quality. A well-formatted monolith can still have unsafe state boundaries, broad credentials, needless dependencies, or poorly designed modules. Keep diffs focused: format files, review the resulting changes, then inspect the Terraform plan for infrastructure behavior.

## How

```shell
terraform fmt
terraform fmt -check -recursive
```

The default command formats Terraform files in the current directory. `-recursive` traverses subdirectories, useful for a repository containing modules. `-check` reports whether files differ from canonical formatting and exits nonzero if changes are needed without rewriting them; CI should typically use this mode. `-diff` can show the changes, and `-write=false` suppresses writes when appropriate.

Run the formatter before reviewing or committing configuration. If it modifies files, inspect the diff to make sure the change is formatting-only and that an automated editor has not mixed unrelated edits into the same review.

## Features

- `fmt` modifies textual formatting; it neither validates syntax nor applies changes to infrastructure.
- `fmt -check` is suitable for CI because it detects noncanonical formatting without writing changes.
- Formatting can be applied recursively; do not assume the default scans every module directory.
- A successful formatter run does not prove that the configuration is valid or safe.

## Do's and Don'ts

### Do

- Run `terraform fmt` before review and use recursive check mode in repositories with child modules.
- Inspect formatting diffs and keep style-only edits separate from behavioral edits when practical.
- Enforce canonical style consistently in editor workflows and CI.

### Don't

- Do not interpret a successful formatting run as validation or a safety check.
- Do not let a broad formatting diff conceal unrelated configuration changes.
- Do not assume the default command traverses every nested module directory.

## Real-life implementation

A module team can run `terraform fmt -recursive` locally and configure CI to run `terraform fmt -check -recursive`. If CI fails, format only the relevant Terraform files, inspect the diff, then run validation and review the plan separately; formatting does not change the plan's intended semantics.

## Q&A

**Q:** What does `terraform fmt` change?  
**A:** Terraform source-file formatting.

**Q:** Which mode checks style without rewriting files?  
**A:** `terraform fmt -check` (optionally with `-recursive`).

**Q:** Does fmt establish that provider arguments are valid?  
**A:** No; use validation and planning.

**Q:** Why enforce formatting in CI?  
**A:** To make diffs predictable and reduce review noise.

Further reading: [terraform fmt](https://developer.hashicorp.com/terraform/cli/commands/fmt), [Terraform language style conventions](https://developer.hashicorp.com/terraform/language/syntax/style).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
