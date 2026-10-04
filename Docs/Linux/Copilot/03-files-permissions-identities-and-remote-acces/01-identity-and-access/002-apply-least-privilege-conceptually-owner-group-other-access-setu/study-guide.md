# Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).

**Syllabus objective (exact wording):** Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).

**Mapping:** `03` → `002` `Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).`

## What

DAC combines owner/group/other mode bits, ACL entries/mask, umask and path traversal; setuid/setgid/sticky bits have context-specific semantics. Default ACLs affect newly created descendants.

## Why

This matters operationally: A group ACL appears present but its mask removes effective write access; inspect `getfacl` effective annotations before adjusting ownership or broadening mode bits. The decision hinges on these mechanics: Default ACLs affect newly created descendants.

## How

1. **Establish the relevant boundary:** DAC combines owner/group/other mode bits, ACL entries/mask, umask and path traversal; setuid/setgid/sticky bits have context-specific semantics. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect effective ACL and directory defaults, then test access under the intended UID/GID. Grant the smallest required access and re-check inheritance for newly created files.
3. **Exercise the scenario:** A group ACL appears present but its mask removes effective write access; inspect `getfacl` effective annotations before adjusting ownership or broadening mode bits.
4. **Verify this outcome:** use `id` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Default ACLs affect newly created descendants.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A group ACL appears present but its mask removes effective write access; inspect `getfacl` effective annotations before adjusting ownership or broadening mode bits. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
id
stat -c '%A %a %U:%G %n' <path>
getfacl -p <path> 2>/dev/null
umask
```

## Do's and Don'ts

- **Do:** Inspect effective ACL and directory defaults, then test access under the intended UID/GID. Grant the smallest required access and re-check inheritance for newly created files.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A group ACL appears present but its mask removes effective write access; inspect `getfacl` effective annotations before adjusting ownership or broadening mode bits. **Operator response:** Inspect effective ACL and directory defaults, then test access under the intended UID/GID. Grant the smallest required access and re-check inheritance for newly created files. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: DAC combines owner/group/other mode bits, ACL entries/mask, umask and path traversal; setuid/setgid/sticky bits have context-specific semantics.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `id` and follow the evidence path: Inspect effective ACL and directory defaults, then test access under the intended UID/GID. Grant the smallest required access and re-check inheritance for newly created files.

**Q: How would you verify or falsify the working diagnosis?**

A: A group ACL appears present but its mask removes effective write access; inspect `getfacl` effective annotations before adjusting ownership or broadening mode bits. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
