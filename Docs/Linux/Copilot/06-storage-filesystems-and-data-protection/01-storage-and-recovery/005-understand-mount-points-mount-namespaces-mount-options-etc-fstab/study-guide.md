# Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.

**Syllabus objective (exact wording):** Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.

**Mapping:** `06` → `005` `Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.`

## What

Mounts connect a filesystem into a namespace; UUIDs avoid unstable device names, but fstab options determine boot dependency and failure behavior. Mount namespaces may differ between host and service.

## Why

This matters operationally: A missing NFS mount causes boot delay; decide whether it is required or automount/optional, and verify service ordering and timeout policy. The decision hinges on these mechanics: Mount namespaces may differ between host and service.

## How

1. **Establish the relevant boundary:** Mounts connect a filesystem into a namespace; UUIDs avoid unstable device names, but fstab options determine boot dependency and failure behavior. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare fstab with active `findmnt`; verify UUID, options, systemd-generated mount dependencies and namespace view before editing; test syntax in lab.
3. **Exercise the scenario:** A missing NFS mount causes boot delay; decide whether it is required or automount/optional, and verify service ordering and timeout policy.
4. **Verify this outcome:** use `findmnt --verify --verbose 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Mount namespaces may differ between host and service.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A missing NFS mount causes boot delay; decide whether it is required or automount/optional, and verify service ordering and timeout policy. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
findmnt --verify --verbose 2>/dev/null
findmnt
systemctl list-units --type=mount --all --no-pager
cat /etc/fstab
```

## Do's and Don'ts

- **Do:** Compare fstab with active `findmnt`; verify UUID, options, systemd-generated mount dependencies and namespace view before editing; test syntax in lab.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A missing NFS mount causes boot delay; decide whether it is required or automount/optional, and verify service ordering and timeout policy. **Operator response:** Compare fstab with active `findmnt`; verify UUID, options, systemd-generated mount dependencies and namespace view before editing; test syntax in lab. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Mounts connect a filesystem into a namespace; UUIDs avoid unstable device names, but fstab options determine boot dependency and failure behavior.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `findmnt --verify --verbose 2>/dev/null` and follow the evidence path: Compare fstab with active `findmnt`; verify UUID, options, systemd-generated mount dependencies and namespace view before editing; test syntax in lab.

**Q: How would you verify or falsify the working diagnosis?**

A: A missing NFS mount causes boot delay; decide whether it is required or automount/optional, and verify service ordering and timeout policy. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
