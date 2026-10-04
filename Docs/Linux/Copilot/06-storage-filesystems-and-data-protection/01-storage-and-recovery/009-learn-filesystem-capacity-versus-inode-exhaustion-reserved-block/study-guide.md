# Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).

**Syllabus objective (exact wording):** Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).

**Mapping:** `06` → `009` `Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).`

## What

Bytes and inodes are independent limits; deleted-but-open files retain blocks until handles close. Reserved blocks, quotas and latency can make apparent free capacity misleading.

## Why

This matters operationally: A mail spool cannot create files with 20% disk bytes free; inode usage is exhausted, so find high-file-count directories and apply retention safely. The decision hinges on these mechanics: Reserved blocks, quotas and latency can make apparent free capacity misleading.

## How

1. **Establish the relevant boundary:** Bytes and inodes are independent limits; deleted-but-open files retain blocks until handles close. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Check `df -h` and `df -i`, open-deleted files, quotas, reserved space and storage latency; identify owning service before cleanup.
3. **Exercise the scenario:** A mail spool cannot create files with 20% disk bytes free; inode usage is exhausted, so find high-file-count directories and apply retention safely.
4. **Verify this outcome:** use `df -hT` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Reserved blocks, quotas and latency can make apparent free capacity misleading.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A mail spool cannot create files with 20% disk bytes free; inode usage is exhausted, so find high-file-count directories and apply retention safely. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
df -hT
df -i
lsof +L1 2>/dev/null | head
quota -s 2>/dev/null
```

## Do's and Don'ts

- **Do:** Check `df -h` and `df -i`, open-deleted files, quotas, reserved space and storage latency; identify owning service before cleanup.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A mail spool cannot create files with 20% disk bytes free; inode usage is exhausted, so find high-file-count directories and apply retention safely. **Operator response:** Check `df -h` and `df -i`, open-deleted files, quotas, reserved space and storage latency; identify owning service before cleanup. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Bytes and inodes are independent limits; deleted-but-open files retain blocks until handles close.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `df -hT` and follow the evidence path: Check `df -h` and `df -i`, open-deleted files, quotas, reserved space and storage latency; identify owning service before cleanup.

**Q: How would you verify or falsify the working diagnosis?**

A: A mail spool cannot create files with 20% disk bytes free; inode usage is exhausted, so find high-file-count directories and apply retention safely. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
