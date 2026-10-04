# Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.

**Syllabus objective (exact wording):** Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.

**Mapping:** `14` → `004` `Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.`

## What

Partition/format/repair, LVM/RAID, recursive permissions, firewall/network, MAC policy, kernel parameters and reboot can destroy data or access; treat them as lab-only absent formal approval.

## Why

This matters operationally: Test an fstab failure only on a disposable VM with console recovery; do not run filesystem repair against a production device as an experiment. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command.

## How

1. **Establish the relevant boundary:** Partition/format/repair, LVM/RAID, recursive permissions, firewall/network, MAC policy, kernel parameters and reboot can destroy data or access; treat them as lab-only absent formal approval. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command.
3. **Exercise the scenario:** Test an fstab failure only on a disposable VM with console recovery; do not run filesystem repair against a production device as an experiment.
4. **Verify this outcome:** use `findmnt` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Test an fstab failure only on a disposable VM with console recovery; do not run filesystem repair against a production device as an experiment. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
findmnt
lsblk -f
systemctl --failed --no-pager
```

## Do's and Don'ts

- **Do:** Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Test an fstab failure only on a disposable VM with console recovery; do not run filesystem repair against a production device as an experiment. **Operator response:** Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Partition/format/repair, LVM/RAID, recursive permissions, firewall/network, MAC policy, kernel parameters and reboot can destroy data or access; treat them as lab-only absent formal approval.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `findmnt` and follow the evidence path: Classify the operation's blast radius and irreversibility; isolate it, snapshot/backup, get peer review, confirm targets and rehearse rollback before the lab command.

**Q: How would you verify or falsify the working diagnosis?**

A: Test an fstab failure only on a disposable VM with console recovery; do not run filesystem repair against a production device as an experiment. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
