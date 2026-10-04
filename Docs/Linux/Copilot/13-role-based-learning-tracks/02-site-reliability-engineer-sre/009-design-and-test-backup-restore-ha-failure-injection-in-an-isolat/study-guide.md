# Design and test backup/restore, HA, failure injection in an isolated lab, and operational runbooks.

**Syllabus objective (exact wording):** Design and test backup/restore, HA, failure injection in an isolated lab, and operational runbooks.

**Role extension:** Site reliability engineer (SRE). This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `009` `Design and test backup/restore, HA, failure injection in an isolated lab, and operational runbooks.`

## What

Backup/restore, HA, isolated failure injection and runbooks are reliability properties only when tested end to end against measurable RTO/RPO and data consistency.

## Why

This matters operationally: Simulate loss of a disposable VM's data volume, restore to a clean instance and measure recovery including identity, network, dependencies and service readiness. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity.

## How

1. **Establish the relevant boundary:** Backup/restore, HA, isolated failure injection and runbooks are reliability properties only when tested end to end against measurable RTO/RPO and data consistency. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity.
3. **Exercise the scenario:** Simulate loss of a disposable VM's data volume, restore to a clean instance and measure recovery including identity, network, dependencies and service readiness.
4. **Verify this outcome:** use `date -Is` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Simulate loss of a disposable VM's data volume, restore to a clean instance and measure recovery including identity, network, dependencies and service readiness. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
date -Is
findmnt
df -hT
systemctl is-active <service>
```

## Do's and Don'ts

- **Do:** Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Simulate loss of a disposable VM's data volume, restore to a clean instance and measure recovery including identity, network, dependencies and service readiness. **Operator response:** Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Backup/restore, HA, isolated failure injection and runbooks are reliability properties only when tested end to end against measurable RTO/RPO and data consistency.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `date -Is` and follow the evidence path: Choose a disposable test target, synthetic state and bounded fault; execute recovery from independent backup, time it and verify service/data integrity.

**Q: How would you verify or falsify the working diagnosis?**

A: Simulate loss of a disposable VM's data volume, restore to a clean instance and measure recovery including identity, network, dependencies and service readiness. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
