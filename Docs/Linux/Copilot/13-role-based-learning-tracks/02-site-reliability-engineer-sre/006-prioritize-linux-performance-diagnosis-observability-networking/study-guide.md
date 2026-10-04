# Prioritize Linux performance diagnosis, observability, networking, storage failure modes, systemd recovery, cgroups, and incident response.

**Syllabus objective (exact wording):** Prioritize Linux performance diagnosis, observability, networking, storage failure modes, systemd recovery, cgroups, and incident response.

**Role extension:** Site reliability engineer (SRE). This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `006` `Prioritize Linux performance diagnosis, observability, networking, storage failure modes, systemd recovery, cgroups, and incident response.`

## What

SRE Linux priorities are performance, telemetry, networking, storage failure modes, systemd recovery, cgroups and evidence-led incident response tied to service outcomes.

## Why

This matters operationally: Introduce a cgroup memory cap in a lab, observe OOM and service SLO effects, then restore baseline and write the detection/runbook change. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria.

## How

1. **Establish the relevant boundary:** SRE Linux priorities are performance, telemetry, networking, storage failure modes, systemd recovery, cgroups and evidence-led incident response tied to service outcomes. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria.
3. **Exercise the scenario:** Introduce a cgroup memory cap in a lab, observe OOM and service SLO effects, then restore baseline and write the detection/runbook change.
4. **Verify this outcome:** use `cat /proc/pressure/memory 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Introduce a cgroup memory cap in a lab, observe OOM and service SLO effects, then restore baseline and write the detection/runbook change. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /proc/pressure/memory 2>/dev/null
cat /sys/fs/cgroup/memory.events 2>/dev/null
journalctl -k -b --no-pager | grep -i oom
```

## Do's and Don'ts

- **Do:** For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Introduce a cgroup memory cap in a lab, observe OOM and service SLO effects, then restore baseline and write the detection/runbook change. **Operator response:** For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SRE Linux priorities are performance, telemetry, networking, storage failure modes, systemd recovery, cgroups and evidence-led incident response tied to service outcomes.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /proc/pressure/memory 2>/dev/null` and follow the evidence path: For one service, map symptoms to host signals and exercise a bounded failure in a disposable environment; document mitigation and recovery criteria.

**Q: How would you verify or falsify the working diagnosis?**

A: Introduce a cgroup memory cap in a lab, observe OOM and service SLO effects, then restore baseline and write the detection/runbook change. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
