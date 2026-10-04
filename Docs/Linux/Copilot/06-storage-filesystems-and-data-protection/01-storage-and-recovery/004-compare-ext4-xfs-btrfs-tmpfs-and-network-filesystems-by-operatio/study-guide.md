# Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.

**Syllabus objective (exact wording):** Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.

**Mapping:** `06` → `004` `Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.`

## What

ext4, XFS, Btrfs and tmpfs differ in features, operational tooling, growth/shrink behavior, snapshots/checksums and vendor support. NFS and other network filesystems add remote identity/availability dependencies.

## Why

This matters operationally: A log volume needs predictable large-file throughput while a developer snapshot workspace values CoW snapshots; compare supported filesystem features and recovery practices. The decision hinges on these mechanics: NFS and other network filesystems add remote identity/availability dependencies.

## How

1. **Establish the relevant boundary:** ext4, XFS, Btrfs and tmpfs differ in features, operational tooling, growth/shrink behavior, snapshots/checksums and vendor support. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Select against workload semantics, support matrix and restore tooling; confirm online/offline operations and repair tooling for the exact distro/release.
3. **Exercise the scenario:** A log volume needs predictable large-file throughput while a developer snapshot workspace values CoW snapshots; compare supported filesystem features and recovery practices.
4. **Verify this outcome:** use `findmnt -T <path> -o SOURCE,FSTYPE,OPTIONS` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** NFS and other network filesystems add remote identity/availability dependencies.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A log volume needs predictable large-file throughput while a developer snapshot workspace values CoW snapshots; compare supported filesystem features and recovery practices. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
findmnt -T <path> -o SOURCE,FSTYPE,OPTIONS
xfs_info <mount> 2>/dev/null
tune2fs -l <device> 2>/dev/null | head
```

## Do's and Don'ts

- **Do:** Select against workload semantics, support matrix and restore tooling; confirm online/offline operations and repair tooling for the exact distro/release.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A log volume needs predictable large-file throughput while a developer snapshot workspace values CoW snapshots; compare supported filesystem features and recovery practices. **Operator response:** Select against workload semantics, support matrix and restore tooling; confirm online/offline operations and repair tooling for the exact distro/release. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: ext4, XFS, Btrfs and tmpfs differ in features, operational tooling, growth/shrink behavior, snapshots/checksums and vendor support.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `findmnt -T <path> -o SOURCE,FSTYPE,OPTIONS` and follow the evidence path: Select against workload semantics, support matrix and restore tooling; confirm online/offline operations and repair tooling for the exact distro/release.

**Q: How would you verify or falsify the working diagnosis?**

A: A log volume needs predictable large-file throughput while a developer snapshot workspace values CoW snapshots; compare supported filesystem features and recovery practices. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
