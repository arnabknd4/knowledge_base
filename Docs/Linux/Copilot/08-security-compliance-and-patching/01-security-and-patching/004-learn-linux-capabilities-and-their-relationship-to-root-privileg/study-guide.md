# Learn Linux capabilities and their relationship to root privilege; understand why broad capabilities can undermine isolation.

**Syllabus objective (exact wording):** Learn Linux capabilities and their relationship to root privilege; understand why broad capabilities can undermine isolation.

**Mapping:** `08` → `004` `Learn Linux capabilities and their relationship to root privilege; understand why broad capabilities can undermine isolation.`

## What

Linux capabilities divide some root powers into per-process privileges, but broad capabilities (for example SYS_ADMIN) can approach root-level authority. Effective, permitted and bounding sets matter.

## Why

This matters operationally: A container needs a low port but runs privileged; evaluate `CAP_NET_BIND_SERVICE` and user/port alternatives rather than granting all host capabilities. The decision hinges on these mechanics: Effective, permitted and bounding sets matter.

## How

1. **Establish the relevant boundary:** Linux capabilities divide some root powers into per-process privileges, but broad capabilities (for example SYS_ADMIN) can approach root-level authority. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect the service's effective capabilities and remove only those not required; test binding, file access and management behavior after restriction.
3. **Exercise the scenario:** A container needs a low port but runs privileged; evaluate `CAP_NET_BIND_SERVICE` and user/port alternatives rather than granting all host capabilities.
4. **Verify this outcome:** use `getcap -r <path> 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Effective, permitted and bounding sets matter.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A container needs a low port but runs privileged; evaluate `CAP_NET_BIND_SERVICE` and user/port alternatives rather than granting all host capabilities. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
getcap -r <path> 2>/dev/null
grep '^Cap' /proc/<pid>/status
capsh --print 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect the service's effective capabilities and remove only those not required; test binding, file access and management behavior after restriction.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A container needs a low port but runs privileged; evaluate `CAP_NET_BIND_SERVICE` and user/port alternatives rather than granting all host capabilities. **Operator response:** Inspect the service's effective capabilities and remove only those not required; test binding, file access and management behavior after restriction. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Linux capabilities divide some root powers into per-process privileges, but broad capabilities (for example SYS_ADMIN) can approach root-level authority.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getcap -r <path> 2>/dev/null` and follow the evidence path: Inspect the service's effective capabilities and remove only those not required; test binding, file access and management behavior after restriction.

**Q: How would you verify or falsify the working diagnosis?**

A: A container needs a low port but runs privileged; evaluate `CAP_NET_BIND_SERVICE` and user/port alternatives rather than granting all host capabilities. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
