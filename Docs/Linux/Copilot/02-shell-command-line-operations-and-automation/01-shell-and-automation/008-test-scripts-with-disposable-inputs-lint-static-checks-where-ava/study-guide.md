# Test scripts with disposable inputs, lint/static checks where available, and controlled execution; avoid blindly piping downloaded content to a privileged shell.

**Syllabus objective (exact wording):** Test scripts with disposable inputs, lint/static checks where available, and controlled execution; avoid blindly piping downloaded content to a privileged shell.

**Mapping:** `02` → `008` `Test scripts with disposable inputs, lint/static checks where available, and controlled execution; avoid blindly piping downloaded content to a privileged shell.`

## What

Syntax checks catch parsing errors, not destructive semantics, network trust or correctness. Review downloaded code and provenance; privilege should be granted only after the exact script and its effects are understood.

## Why

This matters operationally: A vendor install snippet pipes a mutable download into root: fetch and inspect a pinned/signed artifact, verify its publisher and checksum/signature, then use the documented package workflow. The decision hinges on these mechanics: Review downloaded code and provenance; privilege should be granted only after the exact script and its effects are understood.

## How

1. **Establish the relevant boundary:** Syntax checks catch parsing errors, not destructive semantics, network trust or correctness. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Use disposable fixtures/VMs, static checks, representative success and failure inputs, and a least-privileged execution context; capture expected outcomes before testing.
3. **Exercise the scenario:** A vendor install snippet pipes a mutable download into root: fetch and inspect a pinned/signed artifact, verify its publisher and checksum/signature, then use the documented package workflow.
4. **Verify this outcome:** use `bash -n ./script.sh` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Review downloaded code and provenance; privilege should be granted only after the exact script and its effects are understood.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A vendor install snippet pipes a mutable download into root: fetch and inspect a pinned/signed artifact, verify its publisher and checksum/signature, then use the documented package workflow. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
bash -n ./script.sh
shellcheck ./script.sh 2>/dev/null
git diff --check
```

## Do's and Don'ts

- **Do:** Use disposable fixtures/VMs, static checks, representative success and failure inputs, and a least-privileged execution context; capture expected outcomes before testing.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A vendor install snippet pipes a mutable download into root: fetch and inspect a pinned/signed artifact, verify its publisher and checksum/signature, then use the documented package workflow. **Operator response:** Use disposable fixtures/VMs, static checks, representative success and failure inputs, and a least-privileged execution context; capture expected outcomes before testing. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Syntax checks catch parsing errors, not destructive semantics, network trust or correctness.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `bash -n ./script.sh` and follow the evidence path: Use disposable fixtures/VMs, static checks, representative success and failure inputs, and a least-privileged execution context; capture expected outcomes before testing.

**Q: How would you verify or falsify the working diagnosis?**

A: A vendor install snippet pipes a mutable download into root: fetch and inspect a pinned/signed artifact, verify its publisher and checksum/signature, then use the documented package workflow. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
