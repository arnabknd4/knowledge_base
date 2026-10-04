# Diagnose with layered, hypothesis-driven checks; correlate DNS, routing, firewall, socket, TLS, and application health.

**Syllabus objective (exact wording):** Diagnose with layered, hypothesis-driven checks; correlate DNS, routing, firewall, socket, TLS, and application health.

**Mapping:** `07` → `010` `Diagnose with layered, hypothesis-driven checks; correlate DNS, routing, firewall, socket, TLS, and application health.`

## What

Layered diagnosis isolates DNS, route, firewall, socket, TLS identity and application health. A successful lower layer does not prove a higher layer works.

## Why

This matters operationally: DNS resolves and TCP connects but health check fails certificate verification; inspect SNI, chain, expiry and application response separately. The decision hinges on these mechanics: A successful lower layer does not prove a higher layer works.

## How

1. **Establish the relevant boundary:** Layered diagnosis isolates DNS, route, firewall, socket, TLS identity and application health. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Record client namespace, destination and time; test one boundary at a time and stop at the first failing layer before remediation.
3. **Exercise the scenario:** DNS resolves and TCP connects but health check fails certificate verification; inspect SNI, chain, expiry and application response separately.
4. **Verify this outcome:** use `getent ahosts <host>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A successful lower layer does not prove a higher layer works.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** DNS resolves and TCP connects but health check fails certificate verification; inspect SNI, chain, expiry and application response separately. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
getent ahosts <host>
ip route get <ip>
ss -tn
curl --connect-timeout 3 -I https://<host>/health
```

## Do's and Don'ts

- **Do:** Record client namespace, destination and time; test one boundary at a time and stop at the first failing layer before remediation.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

DNS resolves and TCP connects but health check fails certificate verification; inspect SNI, chain, expiry and application response separately. **Operator response:** Record client namespace, destination and time; test one boundary at a time and stop at the first failing layer before remediation. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Layered diagnosis isolates DNS, route, firewall, socket, TLS identity and application health.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getent ahosts <host>` and follow the evidence path: Record client namespace, destination and time; test one boundary at a time and stop at the first failing layer before remediation.

**Q: How would you verify or falsify the working diagnosis?**

A: DNS resolves and TCP connects but health check fails certificate verification; inspect SNI, chain, expiry and application response separately. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
