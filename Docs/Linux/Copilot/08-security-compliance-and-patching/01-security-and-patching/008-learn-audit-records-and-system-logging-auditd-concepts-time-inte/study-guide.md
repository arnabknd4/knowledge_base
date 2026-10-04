# Learn audit records and system logging, auditd concepts, time integrity, retention, and centralized tamper-resistant log collection (P1).

**Syllabus objective (exact wording):** Learn audit records and system logging, auditd concepts, time integrity, retention, and centralized tamper-resistant log collection (P1).

**Mapping:** `08` → `008` `Learn audit records and system logging, auditd concepts, time integrity, retention, and centralized tamper-resistant log collection (P1).`

## What

Auditd and system logs capture selected events, but useful records need trusted time, retention, access control and central off-host collection. Audit rules have performance/storage tradeoffs.

## Why

This matters operationally: An incident review lacks sudo/auth events because local logs rotated; test central delivery, retention and clock alignment before relying on host-only records. The decision hinges on these mechanics: Audit rules have performance/storage tradeoffs.

## How

1. **Establish the relevant boundary:** Auditd and system logs capture selected events, but useful records need trusted time, retention, access control and central off-host collection. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Define required events and retention, verify forwarding under disk pressure, restrict access and test time synchronization and tamper-resistant storage.
3. **Exercise the scenario:** An incident review lacks sudo/auth events because local logs rotated; test central delivery, retention and clock alignment before relying on host-only records.
4. **Verify this outcome:** use `systemctl status auditd --no-pager 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Audit rules have performance/storage tradeoffs.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An incident review lacks sudo/auth events because local logs rotated; test central delivery, retention and clock alignment before relying on host-only records. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
systemctl status auditd --no-pager 2>/dev/null
auditctl -s 2>/dev/null
journalctl --disk-usage
timedatectl status
```

## Do's and Don'ts

- **Do:** Define required events and retention, verify forwarding under disk pressure, restrict access and test time synchronization and tamper-resistant storage.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An incident review lacks sudo/auth events because local logs rotated; test central delivery, retention and clock alignment before relying on host-only records. **Operator response:** Define required events and retention, verify forwarding under disk pressure, restrict access and test time synchronization and tamper-resistant storage. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Auditd and system logs capture selected events, but useful records need trusted time, retention, access control and central off-host collection.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status auditd --no-pager 2>/dev/null` and follow the evidence path: Define required events and retention, verify forwarding under disk pressure, restrict access and test time synchronization and tamper-resistant storage.

**Q: How would you verify or falsify the working diagnosis?**

A: An incident review lacks sudo/auth events because local logs rotated; test central delivery, retention and clock alignment before relying on host-only records. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
