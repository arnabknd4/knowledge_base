# Capstone: diagnose a deliberately constrained or misconfigured lab service from symptoms and telemetry; document evidence, root cause, risk-controlled mitigation, recovery verification, and follow-up actions.

**Syllabus objective (exact wording):** Capstone: diagnose a deliberately constrained or misconfigured lab service from symptoms and telemetry; document evidence, root cause, risk-controlled mitigation, recovery verification, and follow-up actions.

**Role extension:** Site reliability engineer (SRE). This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `010` `Capstone: diagnose a deliberately constrained or misconfigured lab service from symptoms and telemetry; document evidence, root cause, risk-controlled mitigation, recovery verification, and follow-up actions.`

## What

The SRE capstone presents a constrained/misconfigured lab service and tests diagnosis from telemetry, preservation, root cause, mitigation risk, recovery and follow-up.

## Why

This matters operationally: A lab service has injected latency plus a CPU quota; correlate cgroup/host signals with request latency, propose a bounded fix and prove rollback. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action.

## How

1. **Establish the relevant boundary:** The SRE capstone presents a constrained/misconfigured lab service and tests diagnosis from telemetry, preservation, root cause, mitigation risk, recovery and follow-up. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action.
3. **Exercise the scenario:** A lab service has injected latency plus a CPU quota; correlate cgroup/host signals with request latency, propose a bounded fix and prove rollback.
4. **Verify this outcome:** use `cat /sys/fs/cgroup/cpu.max 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A lab service has injected latency plus a CPU quota; correlate cgroup/host signals with request latency, propose a bounded fix and prove rollback. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /sys/fs/cgroup/cpu.max 2>/dev/null
cat /proc/pressure/cpu 2>/dev/null
journalctl -u <service> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A lab service has injected latency plus a CPU quota; correlate cgroup/host signals with request latency, propose a bounded fix and prove rollback. **Operator response:** Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: The SRE capstone presents a constrained/misconfigured lab service and tests diagnosis from telemetry, preservation, root cause, mitigation risk, recovery and follow-up.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /sys/fs/cgroup/cpu.max 2>/dev/null` and follow the evidence path: Give a reviewer initial symptoms without the answer, preserve the evidence trail, show a falsifiable hypothesis test, then demonstrate recovery and a blameless corrective action.

**Q: How would you verify or falsify the working diagnosis?**

A: A lab service has injected latency plus a CPU quota; correlate cgroup/host signals with request latency, propose a bounded fix and prove rollback. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
