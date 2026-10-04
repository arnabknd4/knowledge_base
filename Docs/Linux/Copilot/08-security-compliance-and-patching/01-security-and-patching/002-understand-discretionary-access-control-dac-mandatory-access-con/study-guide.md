# Understand discretionary access control (DAC), mandatory access control (MAC), Linux Security Modules, and how SELinux and AppArmor enforce policy.

**Syllabus objective (exact wording):** Understand discretionary access control (DAC), mandatory access control (MAC), Linux Security Modules, and how SELinux and AppArmor enforce policy.

**Mapping:** `08` → `002` `Understand discretionary access control (DAC), mandatory access control (MAC), Linux Security Modules, and how SELinux and AppArmor enforce policy.`

## What

DAC uses ownership/mode/ACL; MAC applies policy beyond discretionary permissions. SELinux and AppArmor are LSM implementations with different policy models and distro integration.

## Why

This matters operationally: A service can read a mode-0644 file interactively but gets denied under SELinux; compare domain/label and AVC event rather than disabling the LSM. The decision hinges on these mechanics: SELinux and AppArmor are LSM implementations with different policy models and distro integration.

## How

1. **Establish the relevant boundary:** DAC uses ownership/mode/ACL; MAC applies policy beyond discretionary permissions. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify active LSM and enforcement mode; inspect audit evidence and labels/profiles alongside ordinary permissions; preserve enforcing behavior while diagnosing.
3. **Exercise the scenario:** A service can read a mode-0644 file interactively but gets denied under SELinux; compare domain/label and AVC event rather than disabling the LSM.
4. **Verify this outcome:** use `getenforce 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** SELinux and AppArmor are LSM implementations with different policy models and distro integration.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service can read a mode-0644 file interactively but gets denied under SELinux; compare domain/label and AVC event rather than disabling the LSM. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
getenforce 2>/dev/null
aa-status 2>/dev/null
ls -Z <path> 2>/dev/null
namei -l <path>
```

## Do's and Don'ts

- **Do:** Identify active LSM and enforcement mode; inspect audit evidence and labels/profiles alongside ordinary permissions; preserve enforcing behavior while diagnosing.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service can read a mode-0644 file interactively but gets denied under SELinux; compare domain/label and AVC event rather than disabling the LSM. **Operator response:** Identify active LSM and enforcement mode; inspect audit evidence and labels/profiles alongside ordinary permissions; preserve enforcing behavior while diagnosing. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: DAC uses ownership/mode/ACL; MAC applies policy beyond discretionary permissions.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getenforce 2>/dev/null` and follow the evidence path: Identify active LSM and enforcement mode; inspect audit evidence and labels/profiles alongside ordinary permissions; preserve enforcing behavior while diagnosing.

**Q: How would you verify or falsify the working diagnosis?**

A: A service can read a mode-0644 file interactively but gets denied under SELinux; compare domain/label and AVC event rather than disabling the LSM. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
