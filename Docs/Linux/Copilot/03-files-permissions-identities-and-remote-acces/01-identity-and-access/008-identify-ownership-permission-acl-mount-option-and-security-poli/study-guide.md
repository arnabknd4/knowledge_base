# Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.

**Syllabus objective (exact wording):** Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.

**Mapping:** `03` → `008` `Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.`

## What

An access denial can arise from identity, path traversal, DAC/ACL, mount flags, remote ID mapping or MAC policy. Diagnose layers in order and correlate denials with timestamps.

## Why

This matters operationally: A file is mode 0644 yet service access is denied; inspect parent directories, `noexec`/read-only mount, NFS IDs and SELinux/AppArmor records before changing permissions. The decision hinges on these mechanics: Diagnose layers in order and correlate denials with timestamps.

## How

1. **Establish the relevant boundary:** An access denial can arise from identity, path traversal, DAC/ACL, mount flags, remote ID mapping or MAC policy. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare the failing process identity with the path's metadata, mount options and policy audit; test the smallest read/write operation as that identity.
3. **Exercise the scenario:** A file is mode 0644 yet service access is denied; inspect parent directories, `noexec`/read-only mount, NFS IDs and SELinux/AppArmor records before changing permissions.
4. **Verify this outcome:** use `id <user>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Diagnose layers in order and correlate denials with timestamps.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A file is mode 0644 yet service access is denied; inspect parent directories, `noexec`/read-only mount, NFS IDs and SELinux/AppArmor records before changing permissions. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
id <user>
namei -l <path>
findmnt -T <path>
getfacl -p <path> 2>/dev/null
ausearch -m AVC -ts recent 2>/dev/null
```

## Do's and Don'ts

- **Do:** Compare the failing process identity with the path's metadata, mount options and policy audit; test the smallest read/write operation as that identity.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A file is mode 0644 yet service access is denied; inspect parent directories, `noexec`/read-only mount, NFS IDs and SELinux/AppArmor records before changing permissions. **Operator response:** Compare the failing process identity with the path's metadata, mount options and policy audit; test the smallest read/write operation as that identity. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: An access denial can arise from identity, path traversal, DAC/ACL, mount flags, remote ID mapping or MAC policy.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `id <user>` and follow the evidence path: Compare the failing process identity with the path's metadata, mount options and policy audit; test the smallest read/write operation as that identity.

**Q: How would you verify or falsify the working diagnosis?**

A: A file is mode 0644 yet service access is denied; inspect parent directories, `noexec`/read-only mount, NFS IDs and SELinux/AppArmor records before changing permissions. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
