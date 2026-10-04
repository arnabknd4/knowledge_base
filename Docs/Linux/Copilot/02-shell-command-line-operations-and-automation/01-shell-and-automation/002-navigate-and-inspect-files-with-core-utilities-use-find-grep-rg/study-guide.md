# Navigate and inspect files with core utilities; use `find`, `grep`/`rg`, `xargs`, `sort`, `uniq`, `cut`, `awk`, `sed`, `tee`, and regular expressions.

**Syllabus objective (exact wording):** Navigate and inspect files with core utilities; use `find`, `grep`/`rg`, `xargs`, `sort`, `uniq`, `cut`, `awk`, `sed`, `tee`, and regular expressions.

**Mapping:** `02` → `002` `Navigate and inspect files with core utilities; use `find`, `grep`/`rg`, `xargs`, `sort`, `uniq`, `cut`, `awk`, `sed`, `tee`, and regular expressions.`

## What

File tools operate on paths and byte streams; `find`, `xargs`, sorting and text filters need explicit filename, locale and input assumptions. Prefer NUL-delimited paths where names may contain whitespace/newlines.

## Why

This matters operationally: A report generator silently skips filenames containing spaces; compare file counts before and after a NUL-safe pipeline and preserve the original inputs. The decision hinges on these mechanics: Prefer NUL-delimited paths where names may contain whitespace/newlines.

## How

1. **Establish the relevant boundary:** File tools operate on paths and byte streams; `find`, `xargs`, sorting and text filters need explicit filename, locale and input assumptions. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect a representative directory with unusual filenames; use `find ... -print0` with `xargs -0` where supported, and test the same transformation on a fixture before a broad traversal.
3. **Exercise the scenario:** A report generator silently skips filenames containing spaces; compare file counts before and after a NUL-safe pipeline and preserve the original inputs.
4. **Verify this outcome:** use `find . -maxdepth 1 -type f -print0 | xargs -0 -r printf '%s\n'` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Prefer NUL-delimited paths where names may contain whitespace/newlines.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A report generator silently skips filenames containing spaces; compare file counts before and after a NUL-safe pipeline and preserve the original inputs. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
find . -maxdepth 1 -type f -print0 | xargs -0 -r printf '%s\n'
locale
find --help | head
```

## Do's and Don'ts

- **Do:** Inspect a representative directory with unusual filenames; use `find ... -print0` with `xargs -0` where supported, and test the same transformation on a fixture before a broad traversal.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A report generator silently skips filenames containing spaces; compare file counts before and after a NUL-safe pipeline and preserve the original inputs. **Operator response:** Inspect a representative directory with unusual filenames; use `find ... -print0` with `xargs -0` where supported, and test the same transformation on a fixture before a broad traversal. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: File tools operate on paths and byte streams; `find`, `xargs`, sorting and text filters need explicit filename, locale and input assumptions.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `find . -maxdepth 1 -type f -print0 | xargs -0 -r printf '%s\n'` and follow the evidence path: Inspect a representative directory with unusual filenames; use `find ... -print0` with `xargs -0` where supported, and test the same transformation on a fixture before a broad traversal.

**Q: How would you verify or falsify the working diagnosis?**

A: A report generator silently skips filenames containing spaces; compare file counts before and after a NUL-safe pipeline and preserve the original inputs. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
