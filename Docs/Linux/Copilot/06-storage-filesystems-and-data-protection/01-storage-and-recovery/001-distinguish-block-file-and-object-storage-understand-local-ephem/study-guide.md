# Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.

**Syllabus objective (exact wording):** Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.

**Mapping:** `06` → `001` `Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.`

## What

Block storage exposes sectors, file storage exposes a shared hierarchy, and object storage exposes API-addressed objects. Ephemeral instance disks may disappear on replacement; persistent/network media have separate failure and performance contracts.

## Why

This matters operationally: A stateless cache can use ephemeral NVMe but a database data directory needs persistent storage and tested restore; document the consequences of instance replacement. The decision hinges on these mechanics: Ephemeral instance disks may disappear on replacement; persistent/network media have separate failure and performance contracts.

## How

1. **Establish the relevant boundary:** Block storage exposes sectors, file storage exposes a shared hierarchy, and object storage exposes API-addressed objects. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Match interface, latency/IOPS, sharing, consistency, lifecycle, access control and recovery needs; verify provider persistence/deletion policy before putting state on a disk.
3. **Exercise the scenario:** A stateless cache can use ephemeral NVMe but a database data directory needs persistent storage and tested restore; document the consequences of instance replacement.
4. **Verify this outcome:** use `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Ephemeral instance disks may disappear on replacement; persistent/network media have separate failure and performance contracts.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A stateless cache can use ephemeral NVMe but a database data directory needs persistent storage and tested restore; document the consequences of instance replacement. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL
findmnt
lsblk -d -o NAME,ROTA,TYPE,SIZE
```

## Do's and Don'ts

- **Do:** Match interface, latency/IOPS, sharing, consistency, lifecycle, access control and recovery needs; verify provider persistence/deletion policy before putting state on a disk.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A stateless cache can use ephemeral NVMe but a database data directory needs persistent storage and tested restore; document the consequences of instance replacement. **Operator response:** Match interface, latency/IOPS, sharing, consistency, lifecycle, access control and recovery needs; verify provider persistence/deletion policy before putting state on a disk. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Block storage exposes sectors, file storage exposes a shared hierarchy, and object storage exposes API-addressed objects.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL` and follow the evidence path: Match interface, latency/IOPS, sharing, consistency, lifecycle, access control and recovery needs; verify provider persistence/deletion policy before putting state on a disk.

**Q: How would you verify or falsify the working diagnosis?**

A: A stateless cache can use ephemeral NVMe but a database data directory needs persistent storage and tested restore; document the consequences of instance replacement. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
