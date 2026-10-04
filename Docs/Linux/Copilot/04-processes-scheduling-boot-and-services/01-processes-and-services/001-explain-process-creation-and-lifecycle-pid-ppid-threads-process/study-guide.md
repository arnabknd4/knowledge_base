# Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.

**Syllabus objective (exact wording):** Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.

**Mapping:** `04` → `001` `Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.`

## What

Processes have PID/PPID, threads, signal state, session/process-group relationships and lifecycle states; a zombie has exited and awaits reaping. `/proc` is a snapshot, not proof of an application's health.

## Why

This matters operationally: A parent accumulates zombies after a worker exits; inspect parent/reaping behavior and service logs instead of repeatedly signaling the defunct child. The decision hinges on these mechanics: `/proc` is a snapshot, not proof of an application's health.

## How

1. **Establish the relevant boundary:** Processes have PID/PPID, threads, signal state, session/process-group relationships and lifecycle states; a zombie has exited and awaits reaping. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect state, parent, cgroup and open resources over time; distinguish blocked I/O from runnable CPU demand and identify the supervisor responsible for lifecycle.
3. **Exercise the scenario:** A parent accumulates zombies after a worker exits; inspect parent/reaping behavior and service logs instead of repeatedly signaling the defunct child.
4. **Verify this outcome:** use `ps -eo pid,ppid,stat,ni,comm` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `/proc` is a snapshot, not proof of an application's health.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A parent accumulates zombies after a worker exits; inspect parent/reaping behavior and service logs instead of repeatedly signaling the defunct child. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ps -eo pid,ppid,stat,ni,comm
pstree -ap <pid> 2>/dev/null
cat /proc/<pid>/status 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect state, parent, cgroup and open resources over time; distinguish blocked I/O from runnable CPU demand and identify the supervisor responsible for lifecycle.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A parent accumulates zombies after a worker exits; inspect parent/reaping behavior and service logs instead of repeatedly signaling the defunct child. **Operator response:** Inspect state, parent, cgroup and open resources over time; distinguish blocked I/O from runnable CPU demand and identify the supervisor responsible for lifecycle. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Processes have PID/PPID, threads, signal state, session/process-group relationships and lifecycle states; a zombie has exited and awaits reaping.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ps -eo pid,ppid,stat,ni,comm` and follow the evidence path: Inspect state, parent, cgroup and open resources over time; distinguish blocked I/O from runnable CPU demand and identify the supervisor responsible for lifecycle.

**Q: How would you verify or falsify the working diagnosis?**

A: A parent accumulates zombies after a worker exits; inspect parent/reaping behavior and service logs instead of repeatedly signaling the defunct child. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
