# Model failure domains and recovery objectives; validate assumptions through workload tests and restore/DR exercises.

**Syllabus objective (exact wording):** Model failure domains and recovery objectives; validate assumptions through workload tests and restore/DR exercises.

**Role extension:** Linux / platform architect. This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `014` `Model failure domains and recovery objectives; validate assumptions through workload tests and restore/DR exercises.`

## What

Failure-domain modeling exposes shared power/zone/region, network, identity, control-plane and data dependencies. Recovery objectives must be validated by workload and restore exercises.

## Why

This matters operationally: Two nominally separate app zones share one identity dependency; test identity outage and add independent recovery or graceful degradation. The decision hinges on these mechanics: Recovery objectives must be validated by workload and restore exercises.

## How

1. **Establish the relevant boundary:** Failure-domain modeling exposes shared power/zone/region, network, identity, control-plane and data dependencies. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Diagram dependency graph and fault boundaries, perform a controlled restore/failover test, and compare measured recovery and data loss to documented objectives.
3. **Exercise the scenario:** Two nominally separate app zones share one identity dependency; test identity outage and add independent recovery or graceful degradation.
4. **Verify this outcome:** use `getent hosts <dependency>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Recovery objectives must be validated by workload and restore exercises.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Two nominally separate app zones share one identity dependency; test identity outage and add independent recovery or graceful degradation. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
getent hosts <dependency>
systemctl is-active <service>
date -Is
```

## Do's and Don'ts

- **Do:** Diagram dependency graph and fault boundaries, perform a controlled restore/failover test, and compare measured recovery and data loss to documented objectives.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Two nominally separate app zones share one identity dependency; test identity outage and add independent recovery or graceful degradation. **Operator response:** Diagram dependency graph and fault boundaries, perform a controlled restore/failover test, and compare measured recovery and data loss to documented objectives. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Failure-domain modeling exposes shared power/zone/region, network, identity, control-plane and data dependencies.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getent hosts <dependency>` and follow the evidence path: Diagram dependency graph and fault boundaries, perform a controlled restore/failover test, and compare measured recovery and data loss to documented objectives.

**Q: How would you verify or falsify the working diagnosis?**

A: Two nominally separate app zones share one identity dependency; test identity outage and add independent recovery or graceful degradation. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
