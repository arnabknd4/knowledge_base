# Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.

**Syllabus objective (exact wording):** Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.

**Mapping:** `04` → `002` `Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.`

## What

A process can inherit shell `ulimit`, PAM limits or systemd/cgroup limits; the effective limit is per process and resource. Defaults and configured sources differ by service context.

## Why

This matters operationally: A daemon hits `EMFILE` although an admin shell has a high limit; inspect `/proc/PID/limits` and systemd `LimitNOFILE` rather than changing the interactive shell. The decision hinges on these mechanics: Defaults and configured sources differ by service context.

## How

1. **Establish the relevant boundary:** A process can inherit shell `ulimit`, PAM limits or systemd/cgroup limits; the effective limit is per process and resource. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect the running process limits and its unit/cgroup properties; compare soft/hard values with file/socket demand before changing the correct layer.
3. **Exercise the scenario:** A daemon hits `EMFILE` although an admin shell has a high limit; inspect `/proc/PID/limits` and systemd `LimitNOFILE` rather than changing the interactive shell.
4. **Verify this outcome:** use `ulimit -a` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Defaults and configured sources differ by service context.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A daemon hits `EMFILE` although an admin shell has a high limit; inspect `/proc/PID/limits` and systemd `LimitNOFILE` rather than changing the interactive shell. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ulimit -a
cat /proc/<pid>/limits
systemctl show <unit> -p LimitNOFILE -p TasksMax
```

## Do's and Don'ts

- **Do:** Inspect the running process limits and its unit/cgroup properties; compare soft/hard values with file/socket demand before changing the correct layer.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A daemon hits `EMFILE` although an admin shell has a high limit; inspect `/proc/PID/limits` and systemd `LimitNOFILE` rather than changing the interactive shell. **Operator response:** Inspect the running process limits and its unit/cgroup properties; compare soft/hard values with file/socket demand before changing the correct layer. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A process can inherit shell `ulimit`, PAM limits or systemd/cgroup limits; the effective limit is per process and resource.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ulimit -a` and follow the evidence path: Inspect the running process limits and its unit/cgroup properties; compare soft/hard values with file/socket demand before changing the correct layer.

**Q: How would you verify or falsify the working diagnosis?**

A: A daemon hits `EMFILE` although an admin shell has a high limit; inspect `/proc/PID/limits` and systemd `LimitNOFILE` rather than changing the interactive shell. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
