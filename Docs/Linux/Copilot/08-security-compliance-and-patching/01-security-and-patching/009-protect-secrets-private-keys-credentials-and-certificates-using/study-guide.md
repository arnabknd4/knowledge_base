# Protect secrets, private keys, credentials, and certificates using managed secret stores, access control, rotation, and redaction.

**Syllabus objective (exact wording):** Protect secrets, private keys, credentials, and certificates using managed secret stores, access control, rotation, and redaction.

**Mapping:** `08` → `009` `Protect secrets, private keys, credentials, and certificates using managed secret stores, access control, rotation, and redaction.`

## What

Secrets require controlled issuance, narrow retrieval permissions, rotation, audit and redaction. Private keys copied into images, logs, shell history or command arguments can outlive their intended lifetime.

## Why

This matters operationally: A CI-created VM image accidentally contains a cloud credential in shell history; revoke it, rebuild from clean input and add image scanning/redaction tests. The decision hinges on these mechanics: Private keys copied into images, logs, shell history or command arguments can outlive their intended lifetime.

## How

1. **Establish the relevant boundary:** Secrets require controlled issuance, narrow retrieval permissions, rotation, audit and redaction. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Trace where a secret is stored, delivered, read, logged and revoked; use managed stores and short-lived workload identity where available; rotate after suspected exposure.
3. **Exercise the scenario:** A CI-created VM image accidentally contains a cloud credential in shell history; revoke it, rebuild from clean input and add image scanning/redaction tests.
4. **Verify this outcome:** use `grep -RIlE 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY' <approved-config-path> 2>/dev/null | head` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Private keys copied into images, logs, shell history or command arguments can outlive their intended lifetime.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A CI-created VM image accidentally contains a cloud credential in shell history; revoke it, rebuild from clean input and add image scanning/redaction tests. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
grep -RIlE 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY' <approved-config-path> 2>/dev/null | head
systemctl show <unit> -p Environment
```

## Do's and Don'ts

- **Do:** Trace where a secret is stored, delivered, read, logged and revoked; use managed stores and short-lived workload identity where available; rotate after suspected exposure.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A CI-created VM image accidentally contains a cloud credential in shell history; revoke it, rebuild from clean input and add image scanning/redaction tests. **Operator response:** Trace where a secret is stored, delivered, read, logged and revoked; use managed stores and short-lived workload identity where available; rotate after suspected exposure. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Secrets require controlled issuance, narrow retrieval permissions, rotation, audit and redaction.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `grep -RIlE 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY' <approved-config-path> 2>/dev/null | head` and follow the evidence path: Trace where a secret is stored, delivered, read, logged and revoked; use managed stores and short-lived workload identity where available; rotate after suspected exposure.

**Q: How would you verify or falsify the working diagnosis?**

A: A CI-created VM image accidentally contains a cloud credential in shell history; revoke it, rebuild from clean input and add image scanning/redaction tests. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
