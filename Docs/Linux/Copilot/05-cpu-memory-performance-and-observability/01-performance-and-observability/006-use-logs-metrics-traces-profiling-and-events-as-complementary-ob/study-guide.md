# Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).

**Syllabus objective (exact wording):** Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).

**Mapping:** `05` → `006` `Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).`

## What

Logs explain discrete events, metrics show trends, traces attribute request paths, profiles expose code/resource cost, and events provide deployment/lifecycle context. Host telemetry needs stable identity and useful alert context.

## Why

This matters operationally: An SRE receives a host-pressure page with no workload name; add instance/service labels, deployment event correlation and a safe first query. The decision hinges on these mechanics: Host telemetry needs stable identity and useful alert context.

## How

1. **Establish the relevant boundary:** Logs explain discrete events, metrics show trends, traces attribute request paths, profiles expose code/resource cost, and events provide deployment/lifecycle context. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Define service/instance labels, clock source, retention and cardinality; connect an actionable alert to a runbook and user-visible SLO rather than alerting on a raw counter.
3. **Exercise the scenario:** An SRE receives a host-pressure page with no workload name; add instance/service labels, deployment event correlation and a safe first query.
4. **Verify this outcome:** use `systemctl status <agent-unit> --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Host telemetry needs stable identity and useful alert context.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An SRE receives a host-pressure page with no workload name; add instance/service labels, deployment event correlation and a safe first query. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status <agent-unit> --no-pager
journalctl -u <agent-unit> --since '15 min ago' --no-pager
date -Is
```

## Do's and Don'ts

- **Do:** Define service/instance labels, clock source, retention and cardinality; connect an actionable alert to a runbook and user-visible SLO rather than alerting on a raw counter.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An SRE receives a host-pressure page with no workload name; add instance/service labels, deployment event correlation and a safe first query. **Operator response:** Define service/instance labels, clock source, retention and cardinality; connect an actionable alert to a runbook and user-visible SLO rather than alerting on a raw counter. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Logs explain discrete events, metrics show trends, traces attribute request paths, profiles expose code/resource cost, and events provide deployment/lifecycle context.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status <agent-unit> --no-pager` and follow the evidence path: Define service/instance labels, clock source, retention and cardinality; connect an actionable alert to a runbook and user-visible SLO rather than alerting on a raw counter.

**Q: How would you verify or falsify the working diagnosis?**

A: An SRE receives a host-pressure page with no workload name; add instance/service labels, deployment event correlation and a safe first query. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
