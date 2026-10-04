# Capstone: produce a Linux platform design for a stated workload, including distro/support rationale, image and patch strategy, identity and security controls, storage/network layout, observability, capacity assumptions, HA/DR, threat/failure analysis, and an operational acceptance checklist.

**Syllabus objective (exact wording):** Capstone: produce a Linux platform design for a stated workload, including distro/support rationale, image and patch strategy, identity and security controls, storage/network layout, observability, capacity assumptions, HA/DR, threat/failure analysis, and an operational acceptance checklist.

**Role extension:** Linux / platform architect. This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `015` `Capstone: produce a Linux platform design for a stated workload, including distro/support rationale, image and patch strategy, identity and security controls, storage/network layout, observability, capacity assumptions, HA/DR, threat/failure analysis, and an operational acceptance checklist.`

## What

Architect capstone is a workload-specific platform decision/design with explicit distro support rationale, image/patch, security/identity, storage/network, observability, capacity, HA/DR and threat/failure analysis.

## Why

This matters operationally: Design a supported Linux platform for an API and database, then review canary patch, storage-loss recovery, access, SLO telemetry and measured RTO/RPO. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases.

## How

1. **Establish the relevant boundary:** Architect capstone is a workload-specific platform decision/design with explicit distro support rationale, image/patch, security/identity, storage/network, observability, capacity, HA/DR and threat/failure analysis. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases.
3. **Exercise the scenario:** Design a supported Linux platform for an API and database, then review canary patch, storage-loss recovery, access, SLO telemetry and measured RTO/RPO.
4. **Verify this outcome:** use `cat /etc/os-release` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Design a supported Linux platform for an API and database, then review canary patch, storage-loss recovery, access, SLO telemetry and measured RTO/RPO. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /etc/os-release
uname -r
lsblk -f
ip route
date -Is
```

## Do's and Don'ts

- **Do:** Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Design a supported Linux platform for an API and database, then review canary patch, storage-loss recovery, access, SLO telemetry and measured RTO/RPO. **Operator response:** Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Architect capstone is a workload-specific platform decision/design with explicit distro support rationale, image/patch, security/identity, storage/network, observability, capacity, HA/DR and threat/failure analysis.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /etc/os-release` and follow the evidence path: Deliver a decision record plus acceptance checklist, diagrams, assumptions and validation evidence; have an operator challenge rollback, restore, ownership and failure cases.

**Q: How would you verify or falsify the working diagnosis?**

A: Design a supported Linux platform for an API and database, then review canary patch, storage-loss recovery, access, SLO telemetry and measured RTO/RPO. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
