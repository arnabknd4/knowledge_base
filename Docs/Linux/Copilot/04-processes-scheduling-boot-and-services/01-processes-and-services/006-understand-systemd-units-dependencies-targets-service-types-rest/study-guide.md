# Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.

**Syllabus objective (exact wording):** Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.

**Mapping:** `04` → `006` `Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.`

## What

A systemd unit's type, dependencies, ordering, restart policy, environment, drop-ins and activation mechanism determine service lifecycle. `After=` orders jobs but does not itself pull in a dependency.

## Why

This matters operationally: A service starts before its dependency is available because ordering was mistaken for requirement; model `Requires=`/`Wants=` and readiness separately. The decision hinges on these mechanics: `After=` orders jobs but does not itself pull in a dependency.

## How

1. **Establish the relevant boundary:** A systemd unit's type, dependencies, ordering, restart policy, environment, drop-ins and activation mechanism determine service lifecycle. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Read merged unit and effective properties; validate daemon reload, dependency graph, environment and readiness semantics on a test unit before deployment.
3. **Exercise the scenario:** A service starts before its dependency is available because ordering was mistaken for requirement; model `Requires=`/`Wants=` and readiness separately.
4. **Verify this outcome:** use `systemctl cat <unit>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `After=` orders jobs but does not itself pull in a dependency.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service starts before its dependency is available because ordering was mistaken for requirement; model `Requires=`/`Wants=` and readiness separately. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl cat <unit>
systemctl show <unit> -p Type -p Wants -p Requires -p After -p Restart
systemd-analyze verify <file> 2>/dev/null
```

## Do's and Don'ts

- **Do:** Read merged unit and effective properties; validate daemon reload, dependency graph, environment and readiness semantics on a test unit before deployment.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service starts before its dependency is available because ordering was mistaken for requirement; model `Requires=`/`Wants=` and readiness separately. **Operator response:** Read merged unit and effective properties; validate daemon reload, dependency graph, environment and readiness semantics on a test unit before deployment. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A systemd unit's type, dependencies, ordering, restart policy, environment, drop-ins and activation mechanism determine service lifecycle.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl cat <unit>` and follow the evidence path: Read merged unit and effective properties; validate daemon reload, dependency graph, environment and readiness semantics on a test unit before deployment.

**Q: How would you verify or falsify the working diagnosis?**

A: A service starts before its dependency is available because ordering was mistaken for requirement; model `Requires=`/`Wants=` and readiness separately. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
