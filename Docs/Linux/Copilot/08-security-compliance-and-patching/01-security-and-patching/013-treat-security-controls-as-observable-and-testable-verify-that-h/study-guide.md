# Treat security controls as observable and testable; verify that hardening does not silently break service health.

**Syllabus objective (exact wording):** Treat security controls as observable and testable; verify that hardening does not silently break service health.

**Mapping:** `08` → `013` `Treat security controls as observable and testable; verify that hardening does not silently break service health.`

## What

Security control observability means enforcement state, drift, denials and service health are measurable. A green compliance scan alone cannot show the application remains healthy.

## Why

This matters operationally: An LSM policy change passes a baseline check but blocks log rotation; test writes, reload and rotation in a staging image and inspect audit events. The decision hinges on these mechanics: A green compliance scan alone cannot show the application remains healthy.

## How

1. **Establish the relevant boundary:** Security control observability means enforcement state, drift, denials and service health are measurable. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Pair each hardening assertion with a functional service probe and alert on drift/denial; compare before and after on a canary.
3. **Exercise the scenario:** An LSM policy change passes a baseline check but blocks log rotation; test writes, reload and rotation in a staging image and inspect audit events.
4. **Verify this outcome:** use `systemctl is-active <service>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A green compliance scan alone cannot show the application remains healthy.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An LSM policy change passes a baseline check but blocks log rotation; test writes, reload and rotation in a staging image and inspect audit events. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
systemctl is-active <service>
journalctl -u <service> --since '10 min ago' --no-pager
ausearch -m AVC -ts recent 2>/dev/null
```

## Do's and Don'ts

- **Do:** Pair each hardening assertion with a functional service probe and alert on drift/denial; compare before and after on a canary.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An LSM policy change passes a baseline check but blocks log rotation; test writes, reload and rotation in a staging image and inspect audit events. **Operator response:** Pair each hardening assertion with a functional service probe and alert on drift/denial; compare before and after on a canary. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Security control observability means enforcement state, drift, denials and service health are measurable.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl is-active <service>` and follow the evidence path: Pair each hardening assertion with a functional service probe and alert on drift/denial; compare before and after on a canary.

**Q: How would you verify or falsify the working diagnosis?**

A: An LSM policy change passes a baseline check but blocks log rotation; test writes, reload and rotation in a staging image and inspect audit events. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
