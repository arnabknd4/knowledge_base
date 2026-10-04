# Distinguish SELinux modes, labels, policy, and audit denials from ordinary file permissions; distinguish AppArmor profiles and enforcement modes.

**Syllabus objective (exact wording):** Distinguish SELinux modes, labels, policy, and audit denials from ordinary file permissions; distinguish AppArmor profiles and enforcement modes.

**Mapping:** `08` → `003` `Distinguish SELinux modes, labels, policy, and audit denials from ordinary file permissions; distinguish AppArmor profiles and enforcement modes.`

## What

SELinux associates labels with objects and enforces policy by domain; AppArmor confines by profile and mode. Audit denials differ from DAC errors, and remediation should target the label/profile rule.

## Why

This matters operationally: A web service denial follows a content-directory move; verify expected SELinux context and restore labeling in a lab instead of setting permissive mode. The decision hinges on these mechanics: Audit denials differ from DAC errors, and remediation should target the label/profile rule.

## How

1. **Establish the relevant boundary:** SELinux associates labels with objects and enforces policy by domain; AppArmor confines by profile and mode. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Read the specific AVC/AppArmor denial, confirm process domain/profile and object label, then use distribution tools to restore expected context or review narrow policy.
3. **Exercise the scenario:** A web service denial follows a content-directory move; verify expected SELinux context and restore labeling in a lab instead of setting permissive mode.
4. **Verify this outcome:** use `getenforce 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Audit denials differ from DAC errors, and remediation should target the label/profile rule.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A web service denial follows a content-directory move; verify expected SELinux context and restore labeling in a lab instead of setting permissive mode. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
getenforce 2>/dev/null
ausearch -m AVC -ts recent 2>/dev/null
ls -Z <path> 2>/dev/null
aa-status 2>/dev/null
```

## Do's and Don'ts

- **Do:** Read the specific AVC/AppArmor denial, confirm process domain/profile and object label, then use distribution tools to restore expected context or review narrow policy.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A web service denial follows a content-directory move; verify expected SELinux context and restore labeling in a lab instead of setting permissive mode. **Operator response:** Read the specific AVC/AppArmor denial, confirm process domain/profile and object label, then use distribution tools to restore expected context or review narrow policy. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SELinux associates labels with objects and enforces policy by domain; AppArmor confines by profile and mode.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getenforce 2>/dev/null` and follow the evidence path: Read the specific AVC/AppArmor denial, confirm process domain/profile and object label, then use distribution tools to restore expected context or review narrow policy.

**Q: How would you verify or falsify the working diagnosis?**

A: A web service denial follows a content-directory move; verify expected SELinux context and restore labeling in a lab instead of setting permissive mode. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
