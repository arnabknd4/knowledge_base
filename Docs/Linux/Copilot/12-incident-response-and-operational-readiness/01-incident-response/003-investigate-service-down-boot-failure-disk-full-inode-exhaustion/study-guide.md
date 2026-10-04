# Investigate service down, boot failure, disk full, inode exhaustion, memory pressure, CPU saturation, I/O latency, DNS, routing, certificate expiry, and permission failures.

**Syllabus objective (exact wording):** Investigate service down, boot failure, disk full, inode exhaustion, memory pressure, CPU saturation, I/O latency, DNS, routing, certificate expiry, and permission failures.

**Mapping:** `12` → `003` `Investigate service down, boot failure, disk full, inode exhaustion, memory pressure, CPU saturation, I/O latency, DNS, routing, certificate expiry, and permission failures.`

## What

Linux incident symptoms have distinct signatures: service state, boot stage, bytes versus inodes, memory/CPU/I/O pressure, DNS versus route, TLS expiry and access-policy layers.

## Why

This matters operationally: Disk-full alert but `df -h` appears normal; check inode capacity and deleted-open files before deleting application data. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence.

## How

1. **Establish the relevant boundary:** Linux incident symptoms have distinct signatures: service state, boot stage, bytes versus inodes, memory/CPU/I/O pressure, DNS versus route, TLS expiry and access-policy layers. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence.
3. **Exercise the scenario:** Disk-full alert but `df -h` appears normal; check inode capacity and deleted-open files before deleting application data.
4. **Verify this outcome:** use `df -hT` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence.

    **Distro/release distinction:** Journal persistence, syslog routing, auditd and diagnostic utilities vary with release and configured retention. Preserve logs through approved, access-controlled incident channels. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Disk-full alert but `df -h` appears normal; check inode capacity and deleted-open files before deleting application data. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
df -hT
df -i
free -h
uptime
getent ahosts <name>
timedatectl status
```

## Do's and Don'ts

- **Do:** Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence.
- **Don't:** Do not restart/kill processes or discard logs before assessing transient evidence, write consistency and customer impact.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Disk-full alert but `df -h` appears normal; check inode capacity and deleted-open files before deleting application data. **Operator response:** Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Linux incident symptoms have distinct signatures: service state, boot stage, bytes versus inodes, memory/CPU/I/O pressure, DNS versus route, TLS expiry and access-policy layers.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `df -hT` and follow the evidence path: Choose the symptom's first discriminator, correlate with application signal, and avoid altering the system until a plausible layer is supported by evidence.

**Q: How would you verify or falsify the working diagnosis?**

A: Disk-full alert but `df -h` appears normal; check inode capacity and deleted-open files before deleting application data. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
