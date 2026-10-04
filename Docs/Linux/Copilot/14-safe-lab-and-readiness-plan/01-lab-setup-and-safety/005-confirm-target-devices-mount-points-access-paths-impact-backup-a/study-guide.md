# Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.

**Syllabus objective (exact wording):** Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.

**Mapping:** `14` → `005` `Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.`

## What

Target confirmation means matching device IDs, mountpoints and consumers to actual data ownership; backup and rollback must cover the same layer affected by the proposed operation.

## Why

This matters operationally: Before a lab volume-growth exercise, match provider volume ID to guest serial and mountpoint; verify no needed test data resides on another disk. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan.

## How

1. **Establish the relevant boundary:** Target confirmation means matching device IDs, mountpoints and consumers to actual data ownership; backup and rollback must cover the same layer affected by the proposed operation. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan.
3. **Exercise the scenario:** Before a lab volume-growth exercise, match provider volume ID to guest serial and mountpoint; verify no needed test data resides on another disk.
4. **Verify this outcome:** use `lsblk -o NAME,SIZE,SERIAL,UUID,MOUNTPOINTS` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Before a lab volume-growth exercise, match provider volume ID to guest serial and mountpoint; verify no needed test data resides on another disk. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
lsblk -o NAME,SIZE,SERIAL,UUID,MOUNTPOINTS
findmnt
df -hT
```

## Do's and Don'ts

- **Do:** Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Before a lab volume-growth exercise, match provider volume ID to guest serial and mountpoint; verify no needed test data resides on another disk. **Operator response:** Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Target confirmation means matching device IDs, mountpoints and consumers to actual data ownership; backup and rollback must cover the same layer affected by the proposed operation.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -o NAME,SIZE,SERIAL,UUID,MOUNTPOINTS` and follow the evidence path: Use serial/UUID and `findmnt` to confirm target, inspect access route, obtain independent backup, describe impact, then have a second person verify plan.

**Q: How would you verify or falsify the working diagnosis?**

A: Before a lab volume-growth exercise, match provider volume ID to guest serial and mountpoint; verify no needed test data resides on another disk. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
