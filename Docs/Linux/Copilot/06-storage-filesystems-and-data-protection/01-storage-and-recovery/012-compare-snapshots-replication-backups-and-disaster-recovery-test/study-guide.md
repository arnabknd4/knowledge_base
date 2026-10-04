# Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.

**Syllabus objective (exact wording):** Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.

**Mapping:** `06` → `012` `Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.`

## What

Snapshots capture a point at one layer; replication copies changes; backups preserve recoverable history; DR restores an operating service across failure domains. Application consistency and dependency ordering matter.

## Why

This matters operationally: A database VM snapshot is crash-consistent but not application-consistent; restore it in a lab and run database integrity/recovery checks before calling it a backup. The decision hinges on these mechanics: Application consistency and dependency ordering matter.

## How

1. **Establish the relevant boundary:** Snapshots capture a point at one layer; replication copies changes; backups preserve recoverable history; DR restores an operating service across failure domains. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Document consistency mechanism (quiesce/transaction log), retention and recovery order; test isolated restore without depending on the source system.
3. **Exercise the scenario:** A database VM snapshot is crash-consistent but not application-consistent; restore it in a lab and run database integrity/recovery checks before calling it a backup.
4. **Verify this outcome:** use `lsblk -f` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Application consistency and dependency ordering matter.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A database VM snapshot is crash-consistent but not application-consistent; restore it in a lab and run database integrity/recovery checks before calling it a backup. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -f
findmnt
systemctl status <service> --no-pager
journalctl -u <service> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Document consistency mechanism (quiesce/transaction log), retention and recovery order; test isolated restore without depending on the source system.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A database VM snapshot is crash-consistent but not application-consistent; restore it in a lab and run database integrity/recovery checks before calling it a backup. **Operator response:** Document consistency mechanism (quiesce/transaction log), retention and recovery order; test isolated restore without depending on the source system. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Snapshots capture a point at one layer; replication copies changes; backups preserve recoverable history; DR restores an operating service across failure domains.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -f` and follow the evidence path: Document consistency mechanism (quiesce/transaction log), retention and recovery order; test isolated restore without depending on the source system.

**Q: How would you verify or falsify the working diagnosis?**

A: A database VM snapshot is crash-consistent but not application-consistent; restore it in a lab and run database integrity/recovery checks before calling it a backup. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
