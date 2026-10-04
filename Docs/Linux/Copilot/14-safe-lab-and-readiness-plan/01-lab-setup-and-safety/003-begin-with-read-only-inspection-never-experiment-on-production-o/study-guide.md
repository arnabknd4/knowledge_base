# Begin with read-only inspection. Never experiment on production or on a device containing needed data.

**Syllabus objective (exact wording):** Begin with read-only inspection. Never experiment on production or on a device containing needed data.

**Mapping:** `14` → `003` `Begin with read-only inspection. Never experiment on production or on a device containing needed data.`

## What

Read-only inspection preserves state and evidence while establishing the affected object, owner and scope. Production and needed-data devices are excluded from experimentation.

## Why

This matters operationally: Diagnose a full-filesystem symptom with `df`, `df -i` and open-file checks before any cleanup; reproduce on synthetic data. The decision hinges on these mechanics: Production and needed-data devices are excluded from experimentation.

## How

1. **Establish the relevant boundary:** Read-only inspection preserves state and evidence while establishing the affected object, owner and scope. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Begin with inventory/status/log inspection; write down baseline and hypothesis before any state change, and use a disposable clone for reproduction.
3. **Exercise the scenario:** Diagnose a full-filesystem symptom with `df`, `df -i` and open-file checks before any cleanup; reproduce on synthetic data.
4. **Verify this outcome:** use `df -hT` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Production and needed-data devices are excluded from experimentation.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Diagnose a full-filesystem symptom with `df`, `df -i` and open-file checks before any cleanup; reproduce on synthetic data. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
df -hT
df -i
lsblk -f
journalctl -p warning --since '15 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Begin with inventory/status/log inspection; write down baseline and hypothesis before any state change, and use a disposable clone for reproduction.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Diagnose a full-filesystem symptom with `df`, `df -i` and open-file checks before any cleanup; reproduce on synthetic data. **Operator response:** Begin with inventory/status/log inspection; write down baseline and hypothesis before any state change, and use a disposable clone for reproduction. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Read-only inspection preserves state and evidence while establishing the affected object, owner and scope.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `df -hT` and follow the evidence path: Begin with inventory/status/log inspection; write down baseline and hypothesis before any state change, and use a disposable clone for reproduction.

**Q: How would you verify or falsify the working diagnosis?**

A: Diagnose a full-filesystem symptom with `df`, `df -i` and open-file checks before any cleanup; reproduce on synthetic data. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
