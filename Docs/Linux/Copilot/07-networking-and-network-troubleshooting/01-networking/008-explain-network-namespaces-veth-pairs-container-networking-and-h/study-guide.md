# Explain network namespaces, veth pairs, container networking, and host/container port publishing.

**Syllabus objective (exact wording):** Explain network namespaces, veth pairs, container networking, and host/container port publishing.

**Mapping:** `07` → `008` `Explain network namespaces, veth pairs, container networking, and host/container port publishing.`

## What

Network namespaces isolate interfaces, routes, sockets and firewall state; veth pairs connect namespaces, while publishing maps ports through host networking rules.

## Why

This matters operationally: The container process listens correctly but host cannot reach its port; verify namespace route and published-port forwarding before changing the app bind address. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address.

## How

1. **Establish the relevant boundary:** Network namespaces isolate interfaces, routes, sockets and firewall state; veth pairs connect namespaces, while publishing maps ports through host networking rules. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address.
3. **Exercise the scenario:** The container process listens correctly but host cannot reach its port; verify namespace route and published-port forwarding before changing the app bind address.
4. **Verify this outcome:** use `ip netns list` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** The container process listens correctly but host cannot reach its port; verify namespace route and published-port forwarding before changing the app bind address. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ip netns list
lsns -t net
ss -lnt
ip link show type veth
```

## Do's and Don'ts

- **Do:** Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

The container process listens correctly but host cannot reach its port; verify namespace route and published-port forwarding before changing the app bind address. **Operator response:** Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Network namespaces isolate interfaces, routes, sockets and firewall state; veth pairs connect namespaces, while publishing maps ports through host networking rules.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ip netns list` and follow the evidence path: Compare `ip`/`ss` from host and target namespace, inspect veth peer and port mapping, and identify whether the listener binds to the container or host address.

**Q: How would you verify or falsify the working diagnosis?**

A: The container process listens correctly but host cannot reach its port; verify namespace route and published-port forwarding before changing the app bind address. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
