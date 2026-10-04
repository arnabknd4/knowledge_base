# Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).

**Syllabus objective (exact wording):** Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).

**Mapping:** `05` → `010` `Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).`

## What

Kernel counters are host/resource clues, not direct user impact. Relate saturation or pressure to service latency/error budget and distinguish shared-host noise from the service's own cgroup.

## Why

This matters operationally: Disk PSI rises on a multi-tenant node; identify affected cgroups and request latency before paging every service owner on the host. The decision hinges on these mechanics: Relate saturation or pressure to service latency/error budget and distinguish shared-host noise from the service's own cgroup.

## How

1. **Establish the relevant boundary:** Kernel counters are host/resource clues, not direct user impact. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Join kernel/host telemetry to service identity and request SLO over matching windows; page only when a host signal predicts or accompanies actionable service impact.
3. **Exercise the scenario:** Disk PSI rises on a multi-tenant node; identify affected cgroups and request latency before paging every service owner on the host.
4. **Verify this outcome:** use `cat /proc/pressure/{cpu,memory,io} 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Relate saturation or pressure to service latency/error budget and distinguish shared-host noise from the service's own cgroup.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Disk PSI rises on a multi-tenant node; identify affected cgroups and request latency before paging every service owner on the host. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /proc/pressure/{cpu,memory,io} 2>/dev/null
cat /proc/<pid>/cgroup
systemctl status <service> --no-pager
```

## Do's and Don'ts

- **Do:** Join kernel/host telemetry to service identity and request SLO over matching windows; page only when a host signal predicts or accompanies actionable service impact.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Disk PSI rises on a multi-tenant node; identify affected cgroups and request latency before paging every service owner on the host. **Operator response:** Join kernel/host telemetry to service identity and request SLO over matching windows; page only when a host signal predicts or accompanies actionable service impact. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Kernel counters are host/resource clues, not direct user impact.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /proc/pressure/{cpu,memory,io} 2>/dev/null` and follow the evidence path: Join kernel/host telemetry to service identity and request SLO over matching windows; page only when a host signal predicts or accompanies actionable service impact.

**Q: How would you verify or falsify the working diagnosis?**

A: Disk PSI rises on a multi-tenant node; identify affected cgroups and request latency before paging every service owner on the host. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
