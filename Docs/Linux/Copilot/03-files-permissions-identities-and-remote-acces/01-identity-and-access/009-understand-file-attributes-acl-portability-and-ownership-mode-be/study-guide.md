# Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).

**Syllabus objective (exact wording):** Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).

**Mapping:** `03` → `009` `Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).`

## What

ACLs, xattrs and ownership can be lost or translated by filesystems, archive tools and network protocols. Numeric UID/GID identity is significant when files cross hosts.

## Why

This matters operationally: A tar restore onto NFS changes effective ownership due to ID mapping; compare numeric IDs and export/client mapping instead of applying blanket chown. The decision hinges on these mechanics: Numeric UID/GID identity is significant when files cross hosts.

## How

1. **Establish the relevant boundary:** ACLs, xattrs and ownership can be lost or translated by filesystems, archive tools and network protocols. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inventory source/destination filesystem and protocol; test copying representative metadata and restoring under the receiving identity before a migration.
3. **Exercise the scenario:** A tar restore onto NFS changes effective ownership due to ID mapping; compare numeric IDs and export/client mapping instead of applying blanket chown.
4. **Verify this outcome:** use `stat -c '%u:%g %a %n' <path>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Numeric UID/GID identity is significant when files cross hosts.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A tar restore onto NFS changes effective ownership due to ID mapping; compare numeric IDs and export/client mapping instead of applying blanket chown. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
stat -c '%u:%g %a %n' <path>
getfacl -p <path> 2>/dev/null
findmnt -T <path>
getfattr -d <path> 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inventory source/destination filesystem and protocol; test copying representative metadata and restoring under the receiving identity before a migration.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A tar restore onto NFS changes effective ownership due to ID mapping; compare numeric IDs and export/client mapping instead of applying blanket chown. **Operator response:** Inventory source/destination filesystem and protocol; test copying representative metadata and restoring under the receiving identity before a migration. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: ACLs, xattrs and ownership can be lost or translated by filesystems, archive tools and network protocols.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `stat -c '%u:%g %a %n' <path>` and follow the evidence path: Inventory source/destination filesystem and protocol; test copying representative metadata and restoring under the receiving identity before a migration.

**Q: How would you verify or falsify the working diagnosis?**

A: A tar restore onto NFS changes effective ownership due to ID mapping; compare numeric IDs and export/client mapping instead of applying blanket chown. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
