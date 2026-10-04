# Understand time synchronization (chrony/NTP), clock drift, certificates, and distributed-system consequences (S).

**Syllabus objective (exact wording):** Understand time synchronization (chrony/NTP), clock drift, certificates, and distributed-system consequences (S).

**Mapping:** `07` → `011` `Understand time synchronization (chrony/NTP), clock drift, certificates, and distributed-system consequences (S).`

## What

NTP/chrony synchronization controls wall-clock offset and drift; certificate validation, Kerberos, leases and distributed ordering depend on time. Abrupt clock steps may disrupt running workloads.

## Why

This matters operationally: TLS begins failing on one node after a VM pause; compare chrony tracking, kernel time and certificate validity before rotating certificates. The decision hinges on these mechanics: Abrupt clock steps may disrupt running workloads.

## How

1. **Establish the relevant boundary:** NTP/chrony synchronization controls wall-clock offset and drift; certificate validation, Kerberos, leases and distributed ordering depend on time. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect synchronization source/offset and drift, then compare affected logs/certificate validity. Correct time through the approved time service, not manual date changes.
3. **Exercise the scenario:** TLS begins failing on one node after a VM pause; compare chrony tracking, kernel time and certificate validity before rotating certificates.
4. **Verify this outcome:** use `timedatectl status` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Abrupt clock steps may disrupt running workloads.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** TLS begins failing on one node after a VM pause; compare chrony tracking, kernel time and certificate validity before rotating certificates. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
timedatectl status
chronyc tracking 2>/dev/null
chronyc sources -v 2>/dev/null
date -Is
```

## Do's and Don'ts

- **Do:** Inspect synchronization source/offset and drift, then compare affected logs/certificate validity. Correct time through the approved time service, not manual date changes.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

TLS begins failing on one node after a VM pause; compare chrony tracking, kernel time and certificate validity before rotating certificates. **Operator response:** Inspect synchronization source/offset and drift, then compare affected logs/certificate validity. Correct time through the approved time service, not manual date changes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: NTP/chrony synchronization controls wall-clock offset and drift; certificate validation, Kerberos, leases and distributed ordering depend on time.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `timedatectl status` and follow the evidence path: Inspect synchronization source/offset and drift, then compare affected logs/certificate validity. Correct time through the approved time service, not manual date changes.

**Q: How would you verify or falsify the working diagnosis?**

A: TLS begins failing on one node after a VM pause; compare chrony tracking, kernel time and certificate validity before rotating certificates. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
