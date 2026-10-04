# Edit files with a terminal editor; use Git for versioned configuration and change review.

**Syllabus objective (exact wording):** Edit files with a terminal editor; use Git for versioned configuration and change review.

**Mapping:** `02` → `005` `Edit files with a terminal editor; use Git for versioned configuration and change review.`

## What

Configuration ownership matters: a package manager, generator or configuration-management agent may overwrite hand-edited files. Git review captures intended changes but not generated runtime state.

## Why

This matters operationally: A hand-edited network file vanishes after reboot because Netplan regenerates the backend config; update the source of truth rather than the generated artifact. The decision hinges on these mechanics: Git review captures intended changes but not generated runtime state.

## How

1. **Establish the relevant boundary:** Configuration ownership matters: a package manager, generator or configuration-management agent may overwrite hand-edited files. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify the file owner and generation path; make a narrow tracked change, inspect `git diff`, and validate syntax with the service's non-mutating checker before rollout.
3. **Exercise the scenario:** A hand-edited network file vanishes after reboot because Netplan regenerates the backend config; update the source of truth rather than the generated artifact.
4. **Verify this outcome:** use `git status --short` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Git review captures intended changes but not generated runtime state.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A hand-edited network file vanishes after reboot because Netplan regenerates the backend config; update the source of truth rather than the generated artifact. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git status --short
git diff --check
git diff -- <path>
command -v vi nano
```

## Do's and Don'ts

- **Do:** Identify the file owner and generation path; make a narrow tracked change, inspect `git diff`, and validate syntax with the service's non-mutating checker before rollout.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A hand-edited network file vanishes after reboot because Netplan regenerates the backend config; update the source of truth rather than the generated artifact. **Operator response:** Identify the file owner and generation path; make a narrow tracked change, inspect `git diff`, and validate syntax with the service's non-mutating checker before rollout. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Configuration ownership matters: a package manager, generator or configuration-management agent may overwrite hand-edited files.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git status --short` and follow the evidence path: Identify the file owner and generation path; make a narrow tracked change, inspect `git diff`, and validate syntax with the service's non-mutating checker before rollout.

**Q: How would you verify or falsify the working diagnosis?**

A: A hand-edited network file vanishes after reboot because Netplan regenerates the backend config; update the source of truth rather than the generated artifact. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
