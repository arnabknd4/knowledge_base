# Understand GPT/partition concepts; inspect block devices and capacity without modifying them.

**Syllabus objective (exact wording):** Understand GPT/partition concepts; inspect block devices and capacity without modifying them.

**Mapping:** `06` → `003` `Understand GPT/partition concepts; inspect block devices and capacity without modifying them.`

## What

GPT defines partition metadata and boundaries; inventory tools can safely report layout and free space. Any write to a partition table can affect all data on that device.

## Why

This matters operationally: Before replacing a volume, prove which guest device maps to its provider ID and that no required mount/swap/RAID member depends on it. The decision hinges on these mechanics: Any write to a partition table can affect all data on that device.

## How

1. **Establish the relevant boundary:** GPT defines partition metadata and boundaries; inventory tools can safely report layout and free space. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Match serial/cloud-volume ID to guest device, inspect partition boundaries and mount consumers, and stop before any write command in an operational review.
3. **Exercise the scenario:** Before replacing a volume, prove which guest device maps to its provider ID and that no required mount/swap/RAID member depends on it.
4. **Verify this outcome:** use `lsblk -o NAME,TYPE,SIZE,START,FSTYPE,UUID,MOUNTPOINTS,SERIAL` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Any write to a partition table can affect all data on that device.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Before replacing a volume, prove which guest device maps to its provider ID and that no required mount/swap/RAID member depends on it. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -o NAME,TYPE,SIZE,START,FSTYPE,UUID,MOUNTPOINTS,SERIAL
blkid
findmnt
```

## Do's and Don'ts

- **Do:** Match serial/cloud-volume ID to guest device, inspect partition boundaries and mount consumers, and stop before any write command in an operational review.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Before replacing a volume, prove which guest device maps to its provider ID and that no required mount/swap/RAID member depends on it. **Operator response:** Match serial/cloud-volume ID to guest device, inspect partition boundaries and mount consumers, and stop before any write command in an operational review. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: GPT defines partition metadata and boundaries; inventory tools can safely report layout and free space.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -o NAME,TYPE,SIZE,START,FSTYPE,UUID,MOUNTPOINTS,SERIAL` and follow the evidence path: Match serial/cloud-volume ID to guest device, inspect partition boundaries and mount consumers, and stop before any write command in an operational review.

**Q: How would you verify or falsify the working diagnosis?**

A: Before replacing a volume, prove which guest device maps to its provider ID and that no required mount/swap/RAID member depends on it. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
