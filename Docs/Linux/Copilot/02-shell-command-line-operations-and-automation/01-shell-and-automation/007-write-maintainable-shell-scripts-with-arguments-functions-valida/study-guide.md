# Write maintainable shell scripts with arguments, functions, validation, logging, traps, exit codes, idempotence, and safe failure handling (P1).

**Syllabus objective (exact wording):** Write maintainable shell scripts with arguments, functions, validation, logging, traps, exit codes, idempotence, and safe failure handling (P1).

**Mapping:** `02` → `007` `Write maintainable shell scripts with arguments, functions, validation, logging, traps, exit codes, idempotence, and safe failure handling (P1).`

## What

A maintainable script has an interface, validation, deterministic outputs, useful diagnostics, cleanup behavior and idempotent state transitions. Traps and `set` options need explicit tests for signals and partial failure.

## Why

This matters operationally: A bootstrap script fails halfway through package/service setup; rerun it in a disposable VM and verify it converges without duplicate users, open ports or stale files. The decision hinges on these mechanics: Traps and `set` options need explicit tests for signals and partial failure.

## How

1. **Establish the relevant boundary:** A maintainable script has an interface, validation, deterministic outputs, useful diagnostics, cleanup behavior and idempotent state transitions. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Specify inputs, exit codes and retry policy; validate before work, log to stderr without secrets, use narrowly scoped temporary state, and test reruns and interruption.
3. **Exercise the scenario:** A bootstrap script fails halfway through package/service setup; rerun it in a disposable VM and verify it converges without duplicate users, open ports or stale files.
4. **Verify this outcome:** use `bash -n ./script.sh` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Traps and `set` options need explicit tests for signals and partial failure.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A bootstrap script fails halfway through package/service setup; rerun it in a disposable VM and verify it converges without duplicate users, open ports or stale files. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
bash -n ./script.sh
shellcheck ./script.sh 2>/dev/null
git diff --check
```

## Do's and Don'ts

- **Do:** Specify inputs, exit codes and retry policy; validate before work, log to stderr without secrets, use narrowly scoped temporary state, and test reruns and interruption.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A bootstrap script fails halfway through package/service setup; rerun it in a disposable VM and verify it converges without duplicate users, open ports or stale files. **Operator response:** Specify inputs, exit codes and retry policy; validate before work, log to stderr without secrets, use narrowly scoped temporary state, and test reruns and interruption. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A maintainable script has an interface, validation, deterministic outputs, useful diagnostics, cleanup behavior and idempotent state transitions.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `bash -n ./script.sh` and follow the evidence path: Specify inputs, exit codes and retry policy; validate before work, log to stderr without secrets, use narrowly scoped temporary state, and test reruns and interruption.

**Q: How would you verify or falsify the working diagnosis?**

A: A bootstrap script fails halfway through package/service setup; rerun it in a disposable VM and verify it converges without duplicate users, open ports or stale files. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
