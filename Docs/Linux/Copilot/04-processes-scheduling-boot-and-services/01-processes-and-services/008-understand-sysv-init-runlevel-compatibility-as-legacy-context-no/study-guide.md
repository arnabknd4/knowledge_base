# Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.

**Syllabus objective (exact wording):** Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.

**Mapping:** `04` → `008` `Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.`

## What

SysV runlevels and init scripts may be exposed through systemd compatibility, but service ordering, daemonization, environment and status semantics differ. Native unit migration must model the real behavior.

## Why

This matters operationally: A legacy service is marked active while its child died because the init script's status/fork contract is wrong; verify the actual process and migrate semantics deliberately. The decision hinges on these mechanics: Native unit migration must model the real behavior.

## How

1. **Establish the relevant boundary:** SysV runlevels and init scripts may be exposed through systemd compatibility, but service ordering, daemonization, environment and status semantics differ. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect the init script and compatibility unit; document dependencies, forking, PID file and exit codes before authoring or enabling a native unit.
3. **Exercise the scenario:** A legacy service is marked active while its child died because the init script's status/fork contract is wrong; verify the actual process and migrate semantics deliberately.
4. **Verify this outcome:** use `systemctl status <service> --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Native unit migration must model the real behavior.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A legacy service is marked active while its child died because the init script's status/fork contract is wrong; verify the actual process and migrate semantics deliberately. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status <service> --no-pager
systemctl cat <service>
service <service> status 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect the init script and compatibility unit; document dependencies, forking, PID file and exit codes before authoring or enabling a native unit.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A legacy service is marked active while its child died because the init script's status/fork contract is wrong; verify the actual process and migrate semantics deliberately. **Operator response:** Inspect the init script and compatibility unit; document dependencies, forking, PID file and exit codes before authoring or enabling a native unit. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SysV runlevels and init scripts may be exposed through systemd compatibility, but service ordering, daemonization, environment and status semantics differ.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status <service> --no-pager` and follow the evidence path: Inspect the init script and compatibility unit; document dependencies, forking, PID file and exit codes before authoring or enabling a native unit.

**Q: How would you verify or falsify the working diagnosis?**

A: A legacy service is marked active while its child died because the init script's status/fork contract is wrong; verify the actual process and migrate semantics deliberately. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
