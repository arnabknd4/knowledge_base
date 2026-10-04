# 3b — Initialize a Terraform working directory

## What

`terraform init` prepares a configuration directory for use. It is the safe, repeatable setup step that discovers declared dependencies and makes them available locally; it does not provision resources. Initialization is required when starting a working directory and should be rerun when configuration changes introduce or change providers, modules, or backend requirements.

Terraform initialization has three important dimensions. It installs provider plugins required by `required_providers`, downloads referenced child modules, and configures the backend that stores state. Provider selections and checksums are recorded in `.terraform.lock.hcl`; committing that file helps teams and automation use consistent, verified provider versions. Module installation is also reflected in the local `.terraform` directory. Neither local directory is normally committed as source configuration.

## Why

Initialization establishes dependency and state-access prerequisites for later commands. In CI, use a controlled Terraform version, commit the lock file, and ensure backend credentials and network access are available. Treat backend changes as state operations, not simple plugin updates: migrating to the wrong location can split team history or cause concurrent management from separate states. Keep secrets out of source-controlled backend arguments where possible.

Terraform may initialize successfully while later operations still fail. Provider installation is not proof that credentials, permissions, remote objects, or API-side constraints are correct. Similarly, downloading a module does not validate its behavior against your environment. Run validation and planning after initialization.

## How

```shell
terraform init
terraform init -upgrade
```

The first command resolves declared dependencies using constraints and existing lock selections. `-upgrade` deliberately considers newer provider versions and module versions allowed by their constraints; it is not a routine substitute for the locked install. Review and commit an intentional lock-file change. When changing backend configuration, initialization may offer to migrate state; verify the source, destination, backup, and access before accepting.

Backend configuration is distinct from provider configuration. The backend controls where Terraform state is stored and how Terraform accesses it. A provider communicates with an infrastructure or service API to manage/read objects. Backend configuration can be partly supplied at initialization, while provider configuration belongs to Terraform configuration and is evaluated for provider operations.

## Features

- `init` installs/configures dependencies and backend access; it does not create managed infrastructure.
- `.terraform.lock.hcl` locks provider selections/checksums, not module versions as a universal guarantee and not Terraform state.
- `-upgrade` changes dependency selection intentionally; normal init honors existing provider lock selections when compatible.
- Backend setup is not the same as provider setup.

## Do's and Don'ts

### Do

- Run init in each new working directory and after provider, module, or backend requirements change.
- Commit and review `.terraform.lock.hcl` to make provider selections reproducible.
- Treat backend migration as a state-management operation with backup and destination checks.

### Don't

- Do not use `-upgrade` casually; it intentionally considers newer allowed dependencies.
- Do not commit `.terraform` or credentials embedded in backend configuration.
- Do not infer that successful initialization proves credentials, permissions, or provider operations work.

## Real-life implementation

In a team sandbox repository, commit provider constraints and the lock file, run `terraform init` in CI, and verify that the intended remote backend is selected before any plan. When intentionally upgrading a provider, review the lock-file diff and run validation and representative plans. For backend migration, test the process with a protected backup and verify the destination state before enabling writes.

## Q&A

**Q:** When should init be run?  
**A:** At least for a new working directory and when dependencies/backend configuration change.

**Q:** What does the lock file protect?  
**A:** Consistent provider selections and their checksums.

**Q:** Does `init` apply a resource?  
**A:** No.

**Q:** What deserves special caution during backend reconfiguration?  
**A:** State migration, backups, destination correctness, and avoiding split/concurrent state.

Further reading: [terraform init](https://developer.hashicorp.com/terraform/cli/commands/init), [dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock), [backends](https://developer.hashicorp.com/terraform/language/backend).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
