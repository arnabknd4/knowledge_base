# Package and transfer data with `tar`, compression tools, `rsync`, and checksums; understand metadata preservation and integrity verification.

**Syllabus objective (exact wording):** Package and transfer data with `tar`, compression tools, `rsync`, and checksums; understand metadata preservation and integrity verification.

**Mapping:** `02` → `006` `Package and transfer data with `tar`, compression tools, `rsync`, and checksums; understand metadata preservation and integrity verification.`

## What

Archive correctness includes contents, path safety, ownership, modes, ACLs/xattrs, timestamps, compression and integrity. `rsync` options can delete destination content, so inspect dry-run scope and never assume default metadata behavior.

## Why

This matters operationally: A restore has files but loses ownership needed by a daemon; test archive creation and restoration as the intended privileged/nonprivileged operator before relying on it. The decision hinges on these mechanics: `rsync` options can delete destination content, so inspect dry-run scope and never assume default metadata behavior.

## How

1. **Establish the relevant boundary:** Archive correctness includes contents, path safety, ownership, modes, ACLs/xattrs, timestamps, compression and integrity. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** List archive paths before extraction, choose a controlled destination, preserve only required metadata, and compare checksums/metadata after a disposable restore.
3. **Exercise the scenario:** A restore has files but loses ownership needed by a daemon; test archive creation and restoration as the intended privileged/nonprivileged operator before relying on it.
4. **Verify this outcome:** use `tar -tf archive.tar` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `rsync` options can delete destination content, so inspect dry-run scope and never assume default metadata behavior.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A restore has files but loses ownership needed by a daemon; test archive creation and restoration as the intended privileged/nonprivileged operator before relying on it. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
tar -tf archive.tar
sha256sum archive.tar
rsync --dry-run --archive source/ destination/
```

## Do's and Don'ts

- **Do:** List archive paths before extraction, choose a controlled destination, preserve only required metadata, and compare checksums/metadata after a disposable restore.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A restore has files but loses ownership needed by a daemon; test archive creation and restoration as the intended privileged/nonprivileged operator before relying on it. **Operator response:** List archive paths before extraction, choose a controlled destination, preserve only required metadata, and compare checksums/metadata after a disposable restore. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Archive correctness includes contents, path safety, ownership, modes, ACLs/xattrs, timestamps, compression and integrity.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `tar -tf archive.tar` and follow the evidence path: List archive paths before extraction, choose a controlled destination, preserve only required metadata, and compare checksums/metadata after a disposable restore.

**Q: How would you verify or falsify the working diagnosis?**

A: A restore has files but loses ownership needed by a daemon; test archive creation and restoration as the intended privileged/nonprivileged operator before relying on it. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
