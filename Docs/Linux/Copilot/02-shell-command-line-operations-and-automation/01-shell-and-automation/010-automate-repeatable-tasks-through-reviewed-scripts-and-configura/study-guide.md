# Automate repeatable tasks through reviewed scripts and configuration-management tools; keep secrets out of source and logs (D, S).

**Syllabus objective (exact wording):** Automate repeatable tasks through reviewed scripts and configuration-management tools; keep secrets out of source and logs (D, S).

**Mapping:** `02` → `010` `Automate repeatable tasks through reviewed scripts and configuration-management tools; keep secrets out of source and logs (D, S).`

## What

Automation needs a source of truth, safe convergence, reviewed changes, observability and secret hygiene. A script/configuration manager should report drift and make repeated application predictable.

## Why

This matters operationally: A manual hotfix is overwritten by the next config-management run; commit the intended state, test convergence on a canary, then audit fleet drift. The decision hinges on these mechanics: A script/configuration manager should report drift and make repeated application predictable.

## How

1. **Establish the relevant boundary:** Automation needs a source of truth, safe convergence, reviewed changes, observability and secret hygiene. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Define ownership for each setting; review the desired-state diff, test on disposable/canary hosts, store secrets externally, and verify both convergence and rollback.
3. **Exercise the scenario:** A manual hotfix is overwritten by the next config-management run; commit the intended state, test convergence on a canary, then audit fleet drift.
4. **Verify this outcome:** use `git status --short` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A script/configuration manager should report drift and make repeated application predictable.

    **Distro/release distinction:** GNU coreutils/grep options are not universal on BusyBox/minimal images; Bash may be absent or `/bin/sh` may be dash/ash. Verify interpreter and utility versions before depending on flags. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A manual hotfix is overwritten by the next config-management run; commit the intended state, test convergence on a canary, then audit fleet drift. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git status --short
git diff --check
ansible-playbook --syntax-check site.yml 2>/dev/null
```

## Do's and Don'ts

- **Do:** Define ownership for each setting; review the desired-state diff, test on disposable/canary hosts, store secrets externally, and verify both convergence and rollback.
- **Don't:** Do not run unreviewed downloaded code as root, hide pipeline failures, or apply broad file transformations before testing filenames and inputs in a disposable fixture.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A manual hotfix is overwritten by the next config-management run; commit the intended state, test convergence on a canary, then audit fleet drift. **Operator response:** Define ownership for each setting; review the desired-state diff, test on disposable/canary hosts, store secrets externally, and verify both convergence and rollback. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Automation needs a source of truth, safe convergence, reviewed changes, observability and secret hygiene.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git status --short` and follow the evidence path: Define ownership for each setting; review the desired-state diff, test on disposable/canary hosts, store secrets externally, and verify both convergence and rollback.

**Q: How would you verify or falsify the working diagnosis?**

A: A manual hotfix is overwritten by the next config-management run; commit the intended state, test convergence on a canary, then audit fleet drift. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
