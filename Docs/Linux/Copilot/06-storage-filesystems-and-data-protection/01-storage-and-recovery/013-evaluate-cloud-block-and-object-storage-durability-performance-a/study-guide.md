# Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).

**Syllabus objective (exact wording):** Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).

**Mapping:** `06` → `013` `Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).`

## What

Cloud block/object durability, latency tiers, IAM, lifecycle deletion and regional failure domains are provider contracts. Storage class names alone do not specify recovery behavior.

## Why

This matters operationally: An architect places archival data in object storage with lifecycle deletion; test IAM denial, retrieval delay and retention policy using synthetic objects. The decision hinges on these mechanics: Storage class names alone do not specify recovery behavior.

## How

1. **Establish the relevant boundary:** Cloud block/object durability, latency tiers, IAM, lifecycle deletion and regional failure domains are provider contracts. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare provider docs for availability/durability, replication, encryption, access policy, lifecycle and snapshots; validate a restore in a separate failure domain.
3. **Exercise the scenario:** An architect places archival data in object storage with lifecycle deletion; test IAM denial, retrieval delay and retention policy using synthetic objects.
4. **Verify this outcome:** use `lsblk -o NAME,SIZE,SERIAL` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Storage class names alone do not specify recovery behavior.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An architect places archival data in object storage with lifecycle deletion; test IAM denial, retrieval delay and retention policy using synthetic objects. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -o NAME,SIZE,SERIAL
findmnt
cloud-init status --long 2>/dev/null
```

## Do's and Don'ts

- **Do:** Compare provider docs for availability/durability, replication, encryption, access policy, lifecycle and snapshots; validate a restore in a separate failure domain.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An architect places archival data in object storage with lifecycle deletion; test IAM denial, retrieval delay and retention policy using synthetic objects. **Operator response:** Compare provider docs for availability/durability, replication, encryption, access policy, lifecycle and snapshots; validate a restore in a separate failure domain. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Cloud block/object durability, latency tiers, IAM, lifecycle deletion and regional failure domains are provider contracts.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -o NAME,SIZE,SERIAL` and follow the evidence path: Compare provider docs for availability/durability, replication, encryption, access policy, lifecycle and snapshots; validate a restore in a separate failure domain.

**Q: How would you verify or falsify the working diagnosis?**

A: An architect places archival data in object storage with lifecycle deletion; test IAM denial, retrieval delay and retention policy using synthetic objects. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
