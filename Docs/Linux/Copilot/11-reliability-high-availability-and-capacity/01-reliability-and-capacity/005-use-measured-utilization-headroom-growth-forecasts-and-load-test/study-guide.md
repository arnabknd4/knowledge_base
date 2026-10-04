# Use measured utilization, headroom, growth forecasts, and load tests to plan scaling; distinguish average from tail demand.

**Syllabus objective (exact wording):** Use measured utilization, headroom, growth forecasts, and load tests to plan scaling; distinguish average from tail demand.

**Mapping:** `11` → `005` `Use measured utilization, headroom, growth forecasts, and load tests to plan scaling; distinguish average from tail demand.`

## What

Scaling from measured utilization requires representative peak/tail data, growth forecasts and headroom. Averages hide bursts, seasonality and degraded-mode requirements.

## Why

This matters operationally: An average CPU of 35% hides daily 99th-percentile saturation; autoscale on appropriate queue/latency signals and reserve failure headroom. The decision hinges on these mechanics: Averages hide bursts, seasonality and degraded-mode requirements.

## How

1. **Establish the relevant boundary:** Scaling from measured utilization requires representative peak/tail data, growth forecasts and headroom. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Measure over a representative interval, load-test expected peak plus failure, define saturation threshold and scale lead time, then compare forecast with capacity.
3. **Exercise the scenario:** An average CPU of 35% hides daily 99th-percentile saturation; autoscale on appropriate queue/latency signals and reserve failure headroom.
4. **Verify this outcome:** use `sar -u 1 3 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Averages hide bursts, seasonality and degraded-mode requirements.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An average CPU of 35% hides daily 99th-percentile saturation; autoscale on appropriate queue/latency signals and reserve failure headroom. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
sar -u 1 3 2>/dev/null
vmstat 1 3
uptime
nproc
```

## Do's and Don'ts

- **Do:** Measure over a representative interval, load-test expected peak plus failure, define saturation threshold and scale lead time, then compare forecast with capacity.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An average CPU of 35% hides daily 99th-percentile saturation; autoscale on appropriate queue/latency signals and reserve failure headroom. **Operator response:** Measure over a representative interval, load-test expected peak plus failure, define saturation threshold and scale lead time, then compare forecast with capacity. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Scaling from measured utilization requires representative peak/tail data, growth forecasts and headroom.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `sar -u 1 3 2>/dev/null` and follow the evidence path: Measure over a representative interval, load-test expected peak plus failure, define saturation threshold and scale lead time, then compare forecast with capacity.

**Q: How would you verify or falsify the working diagnosis?**

A: An average CPU of 35% hides daily 99th-percentile saturation; autoscale on appropriate queue/latency signals and reserve failure headroom. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
