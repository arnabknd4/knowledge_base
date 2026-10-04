# 3c — Validate a Terraform configuration

## What

`terraform validate` checks whether Terraform can parse and internally validate the configuration in the current directory. It catches syntax errors, invalid arguments, incompatible block structure, and many type/reference-shape mistakes. It is a fast feedback step for authoring and CI, especially after `terraform init` has installed the modules and providers whose schemas are needed to validate the configuration.

Validation is intentionally narrower than planning. It does not contact a provider to verify that a credential works, that a remote object exists, that a quota is available, or that an API will accept a proposed value. It does not calculate the real-world consequences of a plan. Terraform can validate a structurally sound configuration that later fails planning or applying because of remote conditions or insufficient permissions.

## Why

Validation should be an inexpensive gate early in a delivery pipeline. It rejects malformed changes before credentials and remote APIs are involved, while preserving a clear separation between static configuration checks and environment-dependent planning. This allows syntax/type feedback to be available in pull requests even when production access is restricted.

Do not interpret a green validation result as a security or correctness certification. It does not establish that resource semantics are safe, that a data lookup is successful, or that the desired change is acceptable. A plan must be reviewed, and policy, tests, and operational controls may be needed for higher assurance. Conversely, a plan can expose issues that validation cannot because it evaluates provider schemas, variables, data sources, and current state in a real execution context.

## How

```shell
terraform init
terraform validate
```

Run validation from the root of the configuration being checked. A common local quality loop is `terraform fmt -check`, `terraform init`, `terraform validate`, then `terraform plan`. For reusable module development, `terraform validate` checks the module configuration in its initialized context; tests and representative root-module plans can add context-specific coverage.

## Features

- `terraform validate` checks syntax and internal consistency; it is not a dry-run of infrastructure changes.
- `terraform plan` is the environment-aware preview. It can reveal provider/API and state-dependent behavior not covered by validation.
- Initialization often precedes validation because modules and provider schemas must be available.
- Formatting and validation are separate: formatting changes layout, while validation checks configuration structure.

## Do's and Don'ts

### Do

- Initialize first so module code and provider schemas are available.
- Use validation as an early static gate, then plan in a representative environment.
- Keep validation results separate from runtime, permission, and policy assurance.

### Don't

- Do not claim validation proves the remote API accepts a change.
- Do not use validation as a substitute for planning or reviewing destructive actions.
- Do not conflate formatting checks with configuration validation.

## Real-life implementation

For a pull request, run `terraform fmt -check -recursive`, initialize the exact module/root under review, and run `terraform validate`. A successful result permits the review to proceed; a deployment pipeline still creates and reviews an environment-specific plan because remote data, credentials, and current state are outside static validation.

## Q&A

**Q:** Does validate contact infrastructure to verify that a resource can be created?  
**A:** No.

**Q:** What does validate primarily catch?  
**A:** Syntax and internal configuration consistency, including many structural/type errors.

**Q:** Why run init first?  
**A:** It makes required providers, modules, and backend setup available to the working directory.

**Q:** What should follow a successful validate before a real change?  
**A:** Plan, review, and then an approved apply.

Further reading: [terraform validate](https://developer.hashicorp.com/terraform/cli/commands/validate), [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
