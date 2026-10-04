# Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.

**Syllabus objective (exact wording):** Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.

**Mapping:** `06` → `002` `Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.`

## What

Storage layers can include device, partition, RAID, encryption, LVM/pool, filesystem, mount and application path. Each layer has separate capacity and recovery behavior.

## Why

This matters operationally: A filesystem reports full although the cloud volume was enlarged; inspect partition, PV/LV and filesystem sizes in order and use release-specific grow procedure in a disposable copy. The decision hinges on these mechanics: Each layer has separate capacity and recovery behavior.

## How

1. **Establish the relevant boundary:** Storage layers can include device, partition, RAID, encryption, LVM/pool, filesystem, mount and application path. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Draw the stack from `lsblk` and `findmnt`, annotate UUIDs and owners, and identify the exact layer that is constrained before planning growth.
3. **Exercise the scenario:** A filesystem reports full although the cloud volume was enlarged; inspect partition, PV/LV and filesystem sizes in order and use release-specific grow procedure in a disposable copy.
4. **Verify this outcome:** use `lsblk -f` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Each layer has separate capacity and recovery behavior.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A filesystem reports full although the cloud volume was enlarged; inspect partition, PV/LV and filesystem sizes in order and use release-specific grow procedure in a disposable copy. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -f
findmnt
df -hT
pvs 2>/dev/null
vgs 2>/dev/null
lvs 2>/dev/null
```

## Do's and Don'ts

- **Do:** Draw the stack from `lsblk` and `findmnt`, annotate UUIDs and owners, and identify the exact layer that is constrained before planning growth.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A filesystem reports full although the cloud volume was enlarged; inspect partition, PV/LV and filesystem sizes in order and use release-specific grow procedure in a disposable copy. **Operator response:** Draw the stack from `lsblk` and `findmnt`, annotate UUIDs and owners, and identify the exact layer that is constrained before planning growth. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Storage layers can include device, partition, RAID, encryption, LVM/pool, filesystem, mount and application path.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -f` and follow the evidence path: Draw the stack from `lsblk` and `findmnt`, annotate UUIDs and owners, and identify the exact layer that is constrained before planning growth.

**Q: How would you verify or falsify the working diagnosis?**

A: A filesystem reports full although the cloud volume was enlarged; inspect partition, PV/LV and filesystem sizes in order and use release-specific grow procedure in a disposable copy. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
