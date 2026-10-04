# Distinguish graceful termination from forced termination and understand the operational consequences of each.

**Syllabus objective (exact wording):** Distinguish graceful termination from forced termination and understand the operational consequences of each.

**Mapping:** `04` → `003` `Distinguish graceful termination from forced termination and understand the operational consequences of each.`

## What

SIGTERM and application-native shutdown allow cleanup; SIGKILL cannot be caught and may interrupt writes. A unit stop policy or supervisor may also send escalation signals.

## Why

This matters operationally: A database process is unresponsive; preserve process and I/O evidence, use its supported shutdown path, and assess transaction recovery before any forced kill. The decision hinges on these mechanics: A unit stop policy or supervisor may also send escalation signals.

## How

1. **Establish the relevant boundary:** SIGTERM and application-native shutdown allow cleanup; SIGKILL cannot be caught and may interrupt writes. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Read service shutdown behavior and inspect logs/open files; send only the documented graceful action, wait a bounded interval, then escalate through the service runbook.
3. **Exercise the scenario:** A database process is unresponsive; preserve process and I/O evidence, use its supported shutdown path, and assess transaction recovery before any forced kill.
4. **Verify this outcome:** use `systemctl show <unit> -p KillSignal -p TimeoutStopUSec -p SendSIGKILL` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A unit stop policy or supervisor may also send escalation signals.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A database process is unresponsive; preserve process and I/O evidence, use its supported shutdown path, and assess transaction recovery before any forced kill. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl show <unit> -p KillSignal -p TimeoutStopUSec -p SendSIGKILL
ps -o pid,stat,wchan:24,cmd -p <pid>
```

## Do's and Don'ts

- **Do:** Read service shutdown behavior and inspect logs/open files; send only the documented graceful action, wait a bounded interval, then escalate through the service runbook.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A database process is unresponsive; preserve process and I/O evidence, use its supported shutdown path, and assess transaction recovery before any forced kill. **Operator response:** Read service shutdown behavior and inspect logs/open files; send only the documented graceful action, wait a bounded interval, then escalate through the service runbook. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SIGTERM and application-native shutdown allow cleanup; SIGKILL cannot be caught and may interrupt writes.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl show <unit> -p KillSignal -p TimeoutStopUSec -p SendSIGKILL` and follow the evidence path: Read service shutdown behavior and inspect logs/open files; send only the documented graceful action, wait a bounded interval, then escalate through the service runbook.

**Q: How would you verify or falsify the working diagnosis?**

A: A database process is unresponsive; preserve process and I/O evidence, use its supported shutdown path, and assess transaction recovery before any forced kill. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
