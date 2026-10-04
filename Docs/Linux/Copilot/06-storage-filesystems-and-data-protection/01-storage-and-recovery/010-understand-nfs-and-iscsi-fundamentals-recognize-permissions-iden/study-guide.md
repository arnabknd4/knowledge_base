# Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).

**Syllabus objective (exact wording):** Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).

**Mapping:** `06` → `010` `Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).`

## What

NFS combines network availability, export policy, UID/GID mapping, locking and mount timeout semantics; iSCSI exposes remote block devices requiring initiator/session and filesystem coordination.

## Why

This matters operationally: A service sees `nobody` ownership on NFS after directory integration changes; compare numeric IDs/idmap and export policy before modifying file permissions. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts.

## How

1. **Establish the relevant boundary:** NFS combines network availability, export policy, UID/GID mapping, locking and mount timeout semantics; iSCSI exposes remote block devices requiring initiator/session and filesystem coordination. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts.
3. **Exercise the scenario:** A service sees `nobody` ownership on NFS after directory integration changes; compare numeric IDs/idmap and export policy before modifying file permissions.
4. **Verify this outcome:** use `findmnt -t nfs,nfs4` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service sees `nobody` ownership on NFS after directory integration changes; compare numeric IDs/idmap and export policy before modifying file permissions. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
findmnt -t nfs,nfs4
nfsstat -m 2>/dev/null
iscsiadm -m session 2>/dev/null
id
```

## Do's and Don'ts

- **Do:** Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service sees `nobody` ownership on NFS after directory integration changes; compare numeric IDs/idmap and export policy before modifying file permissions. **Operator response:** Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: NFS combines network availability, export policy, UID/GID mapping, locking and mount timeout semantics; iSCSI exposes remote block devices requiring initiator/session and filesystem coordination.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `findmnt -t nfs,nfs4` and follow the evidence path: Inspect client/server identity mapping and mount/session state; determine application behavior during partition/reconnect and avoid mounting one ordinary filesystem read-write on multiple hosts.

**Q: How would you verify or falsify the working diagnosis?**

A: A service sees `nobody` ownership on NFS after directory integration changes; compare numeric IDs/idmap and export policy before modifying file permissions. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
