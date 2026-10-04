# Use Bash safely: quoting, globbing, variables, environment, command substitution, exit status, pipes, redirection, file descriptors, and `set` behavior.

**Syllabus objective (exact wording):** Use Bash safely: quoting, globbing, variables, environment, command substitution, exit status, pipes, redirection, file descriptors, and `set` behavior.

**Mapping:** `02` → `001` `Use Bash safely: quoting, globbing, variables, environment, command substitution, exit status, pipes, redirection, file descriptors, and `set` behavior.`

## What

Bash expands variables, performs word splitting/globbing, and applies redirections before execution; quote data and deliberately handle exit status. `set -e` has context-sensitive behavior and is not a complete error model.

## Why

This matters operationally: A cleanup script unexpectedly deletes similarly named files when a variable is empty; reproduce with a temp fixture, validate arguments and refuse empty/root paths before any mutation. The decision hinges on these mechanics: `set -e` has context-sensitive behavior and is not a complete error model.

## How

1. **Establish the relevant boundary:** Bash expands variables, performs word splitting/globbing, and applies redirections before execution; quote data and deliberately handle exit status. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Test quoting, empty values, spaces, glob characters, failed commands and pipelines with disposable fixtures; explicitly capture critical statuses and use `pipefail` only with understood semantics.
3. **Exercise the scenario:** A cleanup script unexpectedly deletes similarly named files when a variable is empty; reproduce with a temp fixture, validate arguments and refuse empty/root paths before any mutation.
4. **Verify this outcome:** use `bash --version` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `set -e` has context-sensitive behavior and is not a complete error model.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A cleanup script unexpectedly deletes similarly named files when a variable is empty; reproduce with a temp fixture, validate arguments and refuse empty/root paths before any mutation. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
bash --version
bash -n ./script.sh
printf '<%s>\n' "$HOME"
bash -c 'false | true
echo status:$?'
```

## Do's and Don'ts

- **Do:** Test quoting, empty values, spaces, glob characters, failed commands and pipelines with disposable fixtures; explicitly capture critical statuses and use `pipefail` only with understood semantics.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A cleanup script unexpectedly deletes similarly named files when a variable is empty; reproduce with a temp fixture, validate arguments and refuse empty/root paths before any mutation. **Operator response:** Test quoting, empty values, spaces, glob characters, failed commands and pipelines with disposable fixtures; explicitly capture critical statuses and use `pipefail` only with understood semantics. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Bash expands variables, performs word splitting/globbing, and applies redirections before execution; quote data and deliberately handle exit status.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `bash --version` and follow the evidence path: Test quoting, empty values, spaces, glob characters, failed commands and pipelines with disposable fixtures; explicitly capture critical statuses and use `pipefail` only with understood semantics.

**Q: How would you verify or falsify the working diagnosis?**

A: A cleanup script unexpectedly deletes similarly named files when a variable is empty; reproduce with a temp fixture, validate arguments and refuse empty/root paths before any mutation. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
