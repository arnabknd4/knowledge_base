# Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.

**Syllabus objective (exact wording):** Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.

**Mapping:** `05` → `005` `Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.`

## What

Latency, throughput, utilization, saturation, errors and queue depth form a time-series diagnostic, not a single health number. A queue often reveals demand exceeding service rate before throughput falls.

## Why

This matters operationally: API p99 rises while average CPU stays low; inspect downstream queue depth and I/O wait at the same time interval before scaling the web tier. The decision hinges on these mechanics: A queue often reveals demand exceeding service rate before throughput falls.

## How

1. **Establish the relevant boundary:** Latency, throughput, utilization, saturation, errors and queue depth form a time-series diagnostic, not a single health number. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Align metric windows and timestamps; graph request tail latency/errors beside CPU run queue, disk queue and network retransmits to locate onset and bottleneck.
3. **Exercise the scenario:** API p99 rises while average CPU stays low; inspect downstream queue depth and I/O wait at the same time interval before scaling the web tier.
4. **Verify this outcome:** use `sar -u 1 3 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A queue often reveals demand exceeding service rate before throughput falls.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** API p99 rises while average CPU stays low; inspect downstream queue depth and I/O wait at the same time interval before scaling the web tier. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
sar -u 1 3 2>/dev/null
sar -d 1 3 2>/dev/null
ss -s
vmstat 1 3
```

## Do's and Don'ts

- **Do:** Align metric windows and timestamps; graph request tail latency/errors beside CPU run queue, disk queue and network retransmits to locate onset and bottleneck.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

API p99 rises while average CPU stays low; inspect downstream queue depth and I/O wait at the same time interval before scaling the web tier. **Operator response:** Align metric windows and timestamps; graph request tail latency/errors beside CPU run queue, disk queue and network retransmits to locate onset and bottleneck. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Latency, throughput, utilization, saturation, errors and queue depth form a time-series diagnostic, not a single health number.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `sar -u 1 3 2>/dev/null` and follow the evidence path: Align metric windows and timestamps; graph request tail latency/errors beside CPU run queue, disk queue and network retransmits to locate onset and bottleneck.

**Q: How would you verify or falsify the working diagnosis?**

A: API p99 rises while average CPU stays low; inspect downstream queue depth and I/O wait at the same time interval before scaling the web tier. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
