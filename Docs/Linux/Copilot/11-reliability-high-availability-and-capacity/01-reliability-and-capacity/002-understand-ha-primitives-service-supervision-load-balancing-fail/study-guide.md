# Understand HA primitives: service supervision, load balancing, failover, fencing, quorum, VIP/VRRP, and cluster membership.

**Syllabus objective (exact wording):** Understand HA primitives: service supervision, load balancing, failover, fencing, quorum, VIP/VRRP, and cluster membership.

**Mapping:** `11` → `002` `Understand HA primitives: service supervision, load balancing, failover, fencing, quorum, VIP/VRRP, and cluster membership.`

## What

HA combines supervision, load balancing, failover, fencing, quorum, VIP/VRRP and membership. Fencing prevents unsafe dual ownership; quorum behavior depends on cluster topology.

## Why

This matters operationally: Two nodes lose cluster communication; verify fencing and quorum prevent both from writing shared state before testing recovery. The decision hinges on these mechanics: Fencing prevents unsafe dual ownership; quorum behavior depends on cluster topology.

## How

1. **Establish the relevant boundary:** HA combines supervision, load balancing, failover, fencing, quorum, VIP/VRRP and membership. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** For each primitive, state trigger, authority, split-brain protection, recovery action and operational owner; test node loss only in isolated lab.
3. **Exercise the scenario:** Two nodes lose cluster communication; verify fencing and quorum prevent both from writing shared state before testing recovery.
4. **Verify this outcome:** use `systemctl status pacemaker corosync --no-pager 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Fencing prevents unsafe dual ownership; quorum behavior depends on cluster topology.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Two nodes lose cluster communication; verify fencing and quorum prevent both from writing shared state before testing recovery. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status pacemaker corosync --no-pager 2>/dev/null
pcs status 2>/dev/null
ip address
```

## Do's and Don'ts

- **Do:** For each primitive, state trigger, authority, split-brain protection, recovery action and operational owner; test node loss only in isolated lab.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Two nodes lose cluster communication; verify fencing and quorum prevent both from writing shared state before testing recovery. **Operator response:** For each primitive, state trigger, authority, split-brain protection, recovery action and operational owner; test node loss only in isolated lab. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: HA combines supervision, load balancing, failover, fencing, quorum, VIP/VRRP and membership.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status pacemaker corosync --no-pager 2>/dev/null` and follow the evidence path: For each primitive, state trigger, authority, split-brain protection, recovery action and operational owner; test node loss only in isolated lab.

**Q: How would you verify or falsify the working diagnosis?**

A: Two nodes lose cluster communication; verify fencing and quorum prevent both from writing shared state before testing recovery. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
