# Use `man`, `info`, `--help`, shell built-ins, and package documentation; locate relevant manual sections and distinguish local documentation from online versions.

**Syllabus objective (exact wording):** Use `man`, `info`, `--help`, shell built-ins, and package documentation; locate relevant manual sections and distinguish local documentation from online versions.

**Mapping:** `02` → `004` `Use `man`, `info`, `--help`, shell built-ins, and package documentation; locate relevant manual sections and distinguish local documentation from online versions.`

## What

Man-page sections distinguish executable commands, system calls, library APIs, file formats and administration. Shell built-ins may need `help`; local documentation matches installed packages more closely than online `latest`.

## Why

This matters operationally: An option documented online does not exist on an older fleet release; use `man` on the target host and gate automation on detected supported versions. The decision hinges on these mechanics: Shell built-ins may need `help`; local documentation matches installed packages more closely than online `latest`.

## How

1. **Establish the relevant boundary:** Man-page sections distinguish executable commands, system calls, library APIs, file formats and administration. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Look up the command's installed version, section and options; compare local and vendor online documentation only after noting release/version differences.
3. **Exercise the scenario:** An option documented online does not exist on an older fleet release; use `man` on the target host and gate automation on detected supported versions.
4. **Verify this outcome:** use `man 1 find` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Shell built-ins may need `help`; local documentation matches installed packages more closely than online `latest`.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An option documented online does not exist on an older fleet release; use `man` on the target host and gate automation on detected supported versions. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
man 1 find
man 5 fstab
help test
find --help | head
```

## Do's and Don'ts

- **Do:** Look up the command's installed version, section and options; compare local and vendor online documentation only after noting release/version differences.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An option documented online does not exist on an older fleet release; use `man` on the target host and gate automation on detected supported versions. **Operator response:** Look up the command's installed version, section and options; compare local and vendor online documentation only after noting release/version differences. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Man-page sections distinguish executable commands, system calls, library APIs, file formats and administration.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `man 1 find` and follow the evidence path: Look up the command's installed version, section and options; compare local and vendor online documentation only after noting release/version differences.

**Q: How would you verify or falsify the working diagnosis?**

A: An option documented online does not exist on an older fleet release; use `man` on the target host and gate automation on detected supported versions. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
