# Understand containment, safe recovery, escalation, and when not to restart or kill processes before evidence is captured.

**Syllabus objective (exact wording):** Understand containment, safe recovery, escalation, and when not to restart or kill processes before evidence is captured.

**Mapping:** `12` → `005` `Understand containment, safe recovery, escalation, and when not to restart or kill processes before evidence is captured.`

## What

Containment limits spread; recovery restores known service; evidence may be transient. Restarting/killing can erase process state, connection evidence or buffered data and may worsen corruption.

## Why

This matters operationally: A memory leak may tempt immediate restart during an incident; capture process/cgroup state and heap evidence if safe, then mitigate within the agreed impact window. The decision hinges on these mechanics: Restarting/killing can erase process state, connection evidence or buffered data and may worsen corruption.

## How

1. **Establish the relevant boundary:** Containment limits spread; recovery restores known service; evidence may be transient. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Preserve high-value evidence first, assess data consistency and containment authority, then use the documented recovery path and verify user-facing health.
3. **Exercise the scenario:** A memory leak may tempt immediate restart during an incident; capture process/cgroup state and heap evidence if safe, then mitigate within the agreed impact window.
4. **Verify this outcome:** use `ps -eo pid,ppid,stat,%mem,%cpu,comm --sort=-%mem | head` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Restarting/killing can erase process state, connection evidence or buffered data and may worsen corruption.

    **Distro/release distinction:** Journal persistence, syslog routing, auditd and diagnostic utilities vary with release and configured retention. Preserve logs through approved, access-controlled incident channels. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A memory leak may tempt immediate restart during an incident; capture process/cgroup state and heap evidence if safe, then mitigate within the agreed impact window. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ps -eo pid,ppid,stat,%mem,%cpu,comm --sort=-%mem | head
cat /proc/pressure/memory 2>/dev/null
systemctl status <unit> --no-pager
```

## Do's and Don'ts

- **Do:** Preserve high-value evidence first, assess data consistency and containment authority, then use the documented recovery path and verify user-facing health.
- **Don't:** Do not restart/kill processes or discard logs before assessing transient evidence, write consistency and customer impact.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A memory leak may tempt immediate restart during an incident; capture process/cgroup state and heap evidence if safe, then mitigate within the agreed impact window. **Operator response:** Preserve high-value evidence first, assess data consistency and containment authority, then use the documented recovery path and verify user-facing health. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Containment limits spread; recovery restores known service; evidence may be transient.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ps -eo pid,ppid,stat,%mem,%cpu,comm --sort=-%mem | head` and follow the evidence path: Preserve high-value evidence first, assess data consistency and containment authority, then use the documented recovery path and verify user-facing health.

**Q: How would you verify or falsify the working diagnosis?**

A: A memory leak may tempt immediate restart during an incident; capture process/cgroup state and heap evidence if safe, then mitigate within the agreed impact window. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
