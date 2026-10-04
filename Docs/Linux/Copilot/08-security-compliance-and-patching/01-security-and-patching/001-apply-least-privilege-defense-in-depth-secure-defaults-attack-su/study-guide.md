# Apply least privilege, defense in depth, secure defaults, attack-surface reduction, and threat modeling to hosts and images.

**Syllabus objective (exact wording):** Apply least privilege, defense in depth, secure defaults, attack-surface reduction, and threat modeling to hosts and images.

**Mapping:** `08` → `001` `Apply least privilege, defense in depth, secure defaults, attack-surface reduction, and threat modeling to hosts and images.`

## What

Least privilege, defense in depth and secure defaults begin with assets, threat actors, trust boundaries and required flows. Attack-surface reduction must retain observability and a tested administration/recovery path.

## Why

This matters operationally: A hardened image closes unused listeners but accidentally removes monitoring access; threat-model the required telemetry and management paths before promotion. The decision hinges on these mechanics: Attack-surface reduction must retain observability and a tested administration/recovery path.

## How

1. **Establish the relevant boundary:** Least privilege, defense in depth and secure defaults begin with assets, threat actors, trust boundaries and required flows. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inventory exposed services, identities and secrets; map threats to controls and owners; prioritize supported, measurable changes with explicit exceptions.
3. **Exercise the scenario:** A hardened image closes unused listeners but accidentally removes monitoring access; threat-model the required telemetry and management paths before promotion.
4. **Verify this outcome:** use `ss -lntup` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Attack-surface reduction must retain observability and a tested administration/recovery path.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A hardened image closes unused listeners but accidentally removes monitoring access; threat-model the required telemetry and management paths before promotion. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ss -lntup
systemctl --type=service --state=running --no-pager
sudo -l
```

## Do's and Don'ts

- **Do:** Inventory exposed services, identities and secrets; map threats to controls and owners; prioritize supported, measurable changes with explicit exceptions.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A hardened image closes unused listeners but accidentally removes monitoring access; threat-model the required telemetry and management paths before promotion. **Operator response:** Inventory exposed services, identities and secrets; map threats to controls and owners; prioritize supported, measurable changes with explicit exceptions. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Least privilege, defense in depth and secure defaults begin with assets, threat actors, trust boundaries and required flows.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ss -lntup` and follow the evidence path: Inventory exposed services, identities and secrets; map threats to controls and owners; prioritize supported, measurable changes with explicit exceptions.

**Q: How would you verify or falsify the working diagnosis?**

A: A hardened image closes unused listeners but accidentally removes monitoring access; threat-model the required telemetry and management paths before promotion. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
