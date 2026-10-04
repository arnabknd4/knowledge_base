# Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.

**Syllabus objective (exact wording):** Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.

**Mapping:** `03` → `001` `Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.`

## What

A pathname is a sequence of directory lookups; each directory requires search/execute permission. Hard links name the same inode, while symlinks resolve a separate target; metadata belongs to the inode.

## Why

This matters operationally: A daemon can read a file but cannot traverse its parent directory; inspect each path component and test as the daemon UID rather than changing the file mode alone. The decision hinges on these mechanics: Hard links name the same inode, while symlinks resolve a separate target; metadata belongs to the inode.

## How

1. **Establish the relevant boundary:** A pathname is a sequence of directory lookups; each directory requires search/execute permission. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect type, owner, mode, link target and every parent component; compare the file's inode and device before concluding two pathnames are the same object.
3. **Exercise the scenario:** A daemon can read a file but cannot traverse its parent directory; inspect each path component and test as the daemon UID rather than changing the file mode alone.
4. **Verify this outcome:** use `stat -- <path>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Hard links name the same inode, while symlinks resolve a separate target; metadata belongs to the inode.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A daemon can read a file but cannot traverse its parent directory; inspect each path component and test as the daemon UID rather than changing the file mode alone. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
stat -- <path>
namei -l <path>
readlink -f -- <path>
ls -li -- <path>
```

## Do's and Don'ts

- **Do:** Inspect type, owner, mode, link target and every parent component; compare the file's inode and device before concluding two pathnames are the same object.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A daemon can read a file but cannot traverse its parent directory; inspect each path component and test as the daemon UID rather than changing the file mode alone. **Operator response:** Inspect type, owner, mode, link target and every parent component; compare the file's inode and device before concluding two pathnames are the same object. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A pathname is a sequence of directory lookups; each directory requires search/execute permission.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `stat -- <path>` and follow the evidence path: Inspect type, owner, mode, link target and every parent component; compare the file's inode and device before concluding two pathnames are the same object.

**Q: How would you verify or falsify the working diagnosis?**

A: A daemon can read a file but cannot traverse its parent directory; inspect each path component and test as the daemon UID rather than changing the file mode alone. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
