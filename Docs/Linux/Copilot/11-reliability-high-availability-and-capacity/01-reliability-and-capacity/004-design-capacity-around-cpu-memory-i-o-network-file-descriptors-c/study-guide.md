# Design capacity around CPU, memory, I/O, network, file descriptors, connection tracking, disk growth, and workload peaks.

**Syllabus objective (exact wording):** Design capacity around CPU, memory, I/O, network, file descriptors, connection tracking, disk growth, and workload peaks.

**Mapping:** `11` → `004` `Design capacity around CPU, memory, I/O, network, file descriptors, connection tracking, disk growth, and workload peaks.`

## What

Capacity must include CPU, memory, I/O, network, file descriptors, conntrack, disk bytes/inodes and peak concurrency. Saturation in any one can constrain throughput.

## Why

This matters operationally: A host has CPU headroom but rejects connections at file-descriptor limit; include descriptors and conntrack in service capacity model. The decision hinges on these mechanics: Saturation in any one can constrain throughput.

## How

1. **Establish the relevant boundary:** Capacity must include CPU, memory, I/O, network, file descriptors, conntrack, disk bytes/inodes and peak concurrency. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Map each resource to demand, safe limit, telemetry and scaling mechanism; load test the bottleneck including degraded/failover mode.
3. **Exercise the scenario:** A host has CPU headroom but rejects connections at file-descriptor limit; include descriptors and conntrack in service capacity model.
4. **Verify this outcome:** use `ulimit -n` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Saturation in any one can constrain throughput.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A host has CPU headroom but rejects connections at file-descriptor limit; include descriptors and conntrack in service capacity model. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ulimit -n
cat /proc/sys/fs/file-nr
ss -s
df -hT
df -i
free -h
```

## Do's and Don'ts

- **Do:** Map each resource to demand, safe limit, telemetry and scaling mechanism; load test the bottleneck including degraded/failover mode.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A host has CPU headroom but rejects connections at file-descriptor limit; include descriptors and conntrack in service capacity model. **Operator response:** Map each resource to demand, safe limit, telemetry and scaling mechanism; load test the bottleneck including degraded/failover mode. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Capacity must include CPU, memory, I/O, network, file descriptors, conntrack, disk bytes/inodes and peak concurrency.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ulimit -n` and follow the evidence path: Map each resource to demand, safe limit, telemetry and scaling mechanism; load test the bottleneck including degraded/failover mode.

**Q: How would you verify or falsify the working diagnosis?**

A: A host has CPU headroom but rejects connections at file-descriptor limit; include descriptors and conntrack in service capacity model. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
