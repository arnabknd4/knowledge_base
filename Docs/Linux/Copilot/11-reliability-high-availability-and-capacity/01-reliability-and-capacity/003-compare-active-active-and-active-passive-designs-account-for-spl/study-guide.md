# Compare active-active and active-passive designs; account for split brain, state replication, and recovery behavior.

**Syllabus objective (exact wording):** Compare active-active and active-passive designs; account for split brain, state replication, and recovery behavior.

**Mapping:** `11` → `003` `Compare active-active and active-passive designs; account for split brain, state replication, and recovery behavior.`

## What

Active-active distributes work but needs concurrent state semantics; active-passive shifts ownership and may reduce conflict at cost of failover delay. Replication does not automatically mean consistency.

## Why

This matters operationally: A stateful API fails over with stale replicated sessions; choose consistency/session strategy and test behavior at the declared RPO. The decision hinges on these mechanics: Replication does not automatically mean consistency.

## How

1. **Establish the relevant boundary:** Active-active distributes work but needs concurrent state semantics; active-passive shifts ownership and may reduce conflict at cost of failover delay. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare conflict handling, write ownership, replication lag, recovery order, capacity under failure and split-brain prevention using workload tests.
3. **Exercise the scenario:** A stateful API fails over with stale replicated sessions; choose consistency/session strategy and test behavior at the declared RPO.
4. **Verify this outcome:** use `systemctl status <cluster-service> --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Replication does not automatically mean consistency.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A stateful API fails over with stale replicated sessions; choose consistency/session strategy and test behavior at the declared RPO. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status <cluster-service> --no-pager
ss -s
journalctl -u <cluster-service> --since '30 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Compare conflict handling, write ownership, replication lag, recovery order, capacity under failure and split-brain prevention using workload tests.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A stateful API fails over with stale replicated sessions; choose consistency/session strategy and test behavior at the declared RPO. **Operator response:** Compare conflict handling, write ownership, replication lag, recovery order, capacity under failure and split-brain prevention using workload tests. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Active-active distributes work but needs concurrent state semantics; active-passive shifts ownership and may reduce conflict at cost of failover delay.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status <cluster-service> --no-pager` and follow the evidence path: Compare conflict handling, write ownership, replication lag, recovery order, capacity under failure and split-brain prevention using workload tests.

**Q: How would you verify or falsify the working diagnosis?**

A: A stateful API fails over with stale replicated sessions; choose consistency/session strategy and test behavior at the declared RPO. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
