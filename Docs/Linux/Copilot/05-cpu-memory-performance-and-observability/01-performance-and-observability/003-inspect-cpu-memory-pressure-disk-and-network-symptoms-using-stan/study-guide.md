# Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.

**Syllabus objective (exact wording):** Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.

**Mapping:** `05` → `003` `Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.`

## What

CPU, memory, disk and network tools report different scopes and sample intervals. Pair host-wide tools with per-process/cgroup data and application telemetry.

## Why

This matters operationally: A periodic CPU spike is invisible in one `top` snapshot; capture process and pressure samples during the scheduled workload window. The decision hinges on these mechanics: Pair host-wide tools with per-process/cgroup data and application telemetry.

## How

1. **Establish the relevant boundary:** CPU, memory, disk and network tools report different scopes and sample intervals. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Take multiple samples during the symptom; note units and container/host scope, then correlate the top resource with request latency or error rate.
3. **Exercise the scenario:** A periodic CPU spike is invisible in one `top` snapshot; capture process and pressure samples during the scheduled workload window.
4. **Verify this outcome:** use `vmstat 1 5` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Pair host-wide tools with per-process/cgroup data and application telemetry.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A periodic CPU spike is invisible in one `top` snapshot; capture process and pressure samples during the scheduled workload window. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
vmstat 1 5
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head
free -h
ss -s
df -hT
```

## Do's and Don'ts

- **Do:** Take multiple samples during the symptom; note units and container/host scope, then correlate the top resource with request latency or error rate.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A periodic CPU spike is invisible in one `top` snapshot; capture process and pressure samples during the scheduled workload window. **Operator response:** Take multiple samples during the symptom; note units and container/host scope, then correlate the top resource with request latency or error rate. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: CPU, memory, disk and network tools report different scopes and sample intervals.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `vmstat 1 5` and follow the evidence path: Take multiple samples during the symptom; note units and container/host scope, then correlate the top resource with request latency or error rate.

**Q: How would you verify or falsify the working diagnosis?**

A: A periodic CPU spike is invisible in one `top` snapshot; capture process and pressure samples during the scheduled workload window. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
