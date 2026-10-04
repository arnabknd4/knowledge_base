# Understand seccomp, namespaces, cgroups, syscall filtering, and host/container boundary limitations.

**Syllabus objective (exact wording):** Understand seccomp, namespaces, cgroups, syscall filtering, and host/container boundary limitations.

**Mapping:** `08` → `005` `Understand seccomp, namespaces, cgroups, syscall filtering, and host/container boundary limitations.`

## What

Namespaces isolate views, cgroups account/limit resources, and seccomp filters syscalls; none alone provides complete host isolation. Shared kernel and privileged host interfaces remain relevant.

## Why

This matters operationally: A tenant workload has a private PID namespace but a host bind mount; review mount/capability/LSM boundaries, not only namespace presence. The decision hinges on these mechanics: Shared kernel and privileged host interfaces remain relevant.

## How

1. **Establish the relevant boundary:** Namespaces isolate views, cgroups account/limit resources, and seccomp filters syscalls; none alone provides complete host isolation. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Map which boundary protects each resource and trust domain; inspect container configuration and test access to host devices, mounts, kernel interfaces and resource limits.
3. **Exercise the scenario:** A tenant workload has a private PID namespace but a host bind mount; review mount/capability/LSM boundaries, not only namespace presence.
4. **Verify this outcome:** use `cat /proc/<pid>/cgroup` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Shared kernel and privileged host interfaces remain relevant.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A tenant workload has a private PID namespace but a host bind mount; review mount/capability/LSM boundaries, not only namespace presence. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
cat /proc/<pid>/cgroup
grep -E '^(Cap|Seccomp|NoNewPrivs)' /proc/<pid>/status
findmnt
```

## Do's and Don'ts

- **Do:** Map which boundary protects each resource and trust domain; inspect container configuration and test access to host devices, mounts, kernel interfaces and resource limits.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A tenant workload has a private PID namespace but a host bind mount; review mount/capability/LSM boundaries, not only namespace presence. **Operator response:** Map which boundary protects each resource and trust domain; inspect container configuration and test access to host devices, mounts, kernel interfaces and resource limits. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Namespaces isolate views, cgroups account/limit resources, and seccomp filters syscalls; none alone provides complete host isolation.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /proc/<pid>/cgroup` and follow the evidence path: Map which boundary protects each resource and trust domain; inspect container configuration and test access to host devices, mounts, kernel interfaces and resource limits.

**Q: How would you verify or falsify the working diagnosis?**

A: A tenant workload has a private PID namespace but a host bind mount; review mount/capability/LSM boundaries, not only namespace presence. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
