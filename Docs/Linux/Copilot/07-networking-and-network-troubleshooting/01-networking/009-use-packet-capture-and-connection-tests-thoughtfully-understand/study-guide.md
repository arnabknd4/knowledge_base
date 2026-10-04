# Use packet capture and connection tests thoughtfully; understand capture scope, permissions, privacy, and production impact.

**Syllabus objective (exact wording):** Use packet capture and connection tests thoughtfully; understand capture scope, permissions, privacy, and production impact.

**Mapping:** `07` → `009` `Use packet capture and connection tests thoughtfully; understand capture scope, permissions, privacy, and production impact.`

## What

Packet capture is point-in-path evidence and may expose payloads, credentials or personal information. Interface, direction, namespace, filter, privilege, file protection and duration matter.

## Why

This matters operationally: For a single failed TCP connection, capture only that endpoint for a few seconds and compare SYN/SYN-ACK path; do not collect broad production payloads. The decision hinges on these mechanics: Interface, direction, namespace, filter, privilege, file protection and duration matter.

## How

1. **Establish the relevant boundary:** Packet capture is point-in-path evidence and may expose payloads, credentials or personal information. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Obtain authorization; choose the correct interface/namespace; apply a narrow host/port filter, bounded duration and protected output; prefer headers when payload is unnecessary.
3. **Exercise the scenario:** For a single failed TCP connection, capture only that endpoint for a few seconds and compare SYN/SYN-ACK path; do not collect broad production payloads.
4. **Verify this outcome:** use `tcpdump -D 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Interface, direction, namespace, filter, privilege, file protection and duration matter.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** For a single failed TCP connection, capture only that endpoint for a few seconds and compare SYN/SYN-ACK path; do not collect broad production payloads. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
tcpdump -D 2>/dev/null
tcpdump -ni <iface> -c 50 'host <approved-ip> and tcp port <port>'
```

## Do's and Don'ts

- **Do:** Obtain authorization; choose the correct interface/namespace; apply a narrow host/port filter, bounded duration and protected output; prefer headers when payload is unnecessary.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

For a single failed TCP connection, capture only that endpoint for a few seconds and compare SYN/SYN-ACK path; do not collect broad production payloads. **Operator response:** Obtain authorization; choose the correct interface/namespace; apply a narrow host/port filter, bounded duration and protected output; prefer headers when payload is unnecessary. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Packet capture is point-in-path evidence and may expose payloads, credentials or personal information.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `tcpdump -D 2>/dev/null` and follow the evidence path: Obtain authorization; choose the correct interface/namespace; apply a narrow host/port filter, bounded duration and protected output; prefer headers when payload is unnecessary.

**Q: How would you verify or falsify the working diagnosis?**

A: For a single failed TCP connection, capture only that endpoint for a few seconds and compare SYN/SYN-ACK path; do not collect broad production payloads. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
