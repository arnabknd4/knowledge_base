# Distinguish interactive shell startup files from login/non-login and system-wide shell configuration.

**Syllabus objective (exact wording):** Distinguish interactive shell startup files from login/non-login and system-wide shell configuration.

**Mapping:** `02` → `009` `Distinguish interactive shell startup files from login/non-login and system-wide shell configuration.`

## What

Login, interactive and non-interactive shell startup differ; Bash reads different files depending on mode and distribution policy. Cron/systemd environments are not an interactive profile.

## Why

This matters operationally: A command works in an SSH terminal but fails in a timer because PATH and locale are absent; declare the service environment instead of sourcing a whole interactive profile. The decision hinges on these mechanics: Cron/systemd environments are not an interactive profile.

## How

1. **Establish the relevant boundary:** Login, interactive and non-interactive shell startup differ; Bash reads different files depending on mode and distribution policy. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Determine invocation mode and shell; inspect system/global and user startup files, then reproduce the actual scheduler/service environment with a harmless diagnostic.
3. **Exercise the scenario:** A command works in an SSH terminal but fails in a timer because PATH and locale are absent; declare the service environment instead of sourcing a whole interactive profile.
4. **Verify this outcome:** use `bash --login -c 'shopt -q login_shell` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Cron/systemd environments are not an interactive profile.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A command works in an SSH terminal but fails in a timer because PATH and locale are absent; declare the service environment instead of sourcing a whole interactive profile. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
bash --login -c 'shopt -q login_shell
echo login:$?'
bash -c 'shopt -q login_shell
echo login:$?'
systemctl show <unit> -p Environment
```

## Do's and Don'ts

- **Do:** Determine invocation mode and shell; inspect system/global and user startup files, then reproduce the actual scheduler/service environment with a harmless diagnostic.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A command works in an SSH terminal but fails in a timer because PATH and locale are absent; declare the service environment instead of sourcing a whole interactive profile. **Operator response:** Determine invocation mode and shell; inspect system/global and user startup files, then reproduce the actual scheduler/service environment with a harmless diagnostic. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Login, interactive and non-interactive shell startup differ; Bash reads different files depending on mode and distribution policy.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `bash --login -c 'shopt -q login_shell` and follow the evidence path: Determine invocation mode and shell; inspect system/global and user startup files, then reproduce the actual scheduler/service environment with a harmless diagnostic.

**Q: How would you verify or falsify the working diagnosis?**

A: A command works in an SSH terminal but fails in a timer because PATH and locale are absent; declare the service environment instead of sourcing a whole interactive profile. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
