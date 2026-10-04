# Secure boot and update lifecycle conceptually: signed packages, repository trust, kernel updates, reboot planning, live-patching constraints, and rollback strategy.

**Syllabus objective (exact wording):** Secure boot and update lifecycle conceptually: signed packages, repository trust, kernel updates, reboot planning, live-patching constraints, and rollback strategy.

**Mapping:** `08` → `006` `Secure boot and update lifecycle conceptually: signed packages, repository trust, kernel updates, reboot planning, live-patching constraints, and rollback strategy.`

## What

Package signatures/repository trust and Secure Boot protect different stages; kernel updates may require reboot, module signing and application compatibility. Live patching has kernel/version/scope limits.

## Why

This matters operationally: A security update is installed but the vulnerable kernel remains running; compare `uname -r` with installed package and plan controlled reboot/rollback. The decision hinges on these mechanics: Live patching has kernel/version/scope limits.

## How

1. **Establish the relevant boundary:** Package signatures/repository trust and Secure Boot protect different stages; kernel updates may require reboot, module signing and application compatibility. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Verify repo trust and vendor errata, identify running versus installed kernel, assess live-patch coverage, schedule a reboot and preserve a known-good boot entry.
3. **Exercise the scenario:** A security update is installed but the vulnerable kernel remains running; compare `uname -r` with installed package and plan controlled reboot/rollback.
4. **Verify this outcome:** use `uname -r` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Live patching has kernel/version/scope limits.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A security update is installed but the vulnerable kernel remains running; compare `uname -r` with installed package and plan controlled reboot/rollback. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
uname -r
rpm -q kernel 2>/dev/null
dpkg-query -W 'linux-image*' 2>/dev/null
mokutil --sb-state 2>/dev/null
```

## Do's and Don'ts

- **Do:** Verify repo trust and vendor errata, identify running versus installed kernel, assess live-patch coverage, schedule a reboot and preserve a known-good boot entry.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A security update is installed but the vulnerable kernel remains running; compare `uname -r` with installed package and plan controlled reboot/rollback. **Operator response:** Verify repo trust and vendor errata, identify running versus installed kernel, assess live-patch coverage, schedule a reboot and preserve a known-good boot entry. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Package signatures/repository trust and Secure Boot protect different stages; kernel updates may require reboot, module signing and application compatibility.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -r` and follow the evidence path: Verify repo trust and vendor errata, identify running versus installed kernel, assess live-patch coverage, schedule a reboot and preserve a known-good boot entry.

**Q: How would you verify or falsify the working diagnosis?**

A: A security update is installed but the vulnerable kernel remains running; compare `uname -r` with installed package and plan controlled reboot/rollback. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
