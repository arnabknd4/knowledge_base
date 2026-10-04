# Understand TLS certificate chains, key permissions, expiry, trust stores, and service renewal; avoid exposing private key material.

**Syllabus objective (exact wording):** Understand TLS certificate chains, key permissions, expiry, trust stores, and service renewal; avoid exposing private key material.

**Mapping:** `08` → `010` `Understand TLS certificate chains, key permissions, expiry, trust stores, and service renewal; avoid exposing private key material.`

## What

TLS validation checks chain to a trusted root, SAN/hostname, validity window, trust store and service key permissions. Renewal needs a supported deploy/reload path; private key material must stay secret.

## Why

This matters operationally: Only one distro family rejects an internal certificate because its trust store lacks the issuing CA; compare trust bundle and chain, not key permissions alone. The decision hinges on these mechanics: Renewal needs a supported deploy/reload path; private key material must stay secret.

## How

1. **Establish the relevant boundary:** TLS validation checks chain to a trusted root, SAN/hostname, validity window, trust store and service key permissions. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect certificate metadata and chain without printing private keys; check file ownership/mode, expiry alerts and renewal logs, then validate from the client trust context.
3. **Exercise the scenario:** Only one distro family rejects an internal certificate because its trust store lacks the issuing CA; compare trust bundle and chain, not key permissions alone.
4. **Verify this outcome:** use `openssl s_client -connect <host>:443 -servername <host> -showcerts </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Renewal needs a supported deploy/reload path; private key material must stay secret.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Only one distro family rejects an internal certificate because its trust store lacks the issuing CA; compare trust bundle and chain, not key permissions alone. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
openssl s_client -connect <host>:443 -servername <host> -showcerts </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
stat <cert-path>
```

## Do's and Don'ts

- **Do:** Inspect certificate metadata and chain without printing private keys; check file ownership/mode, expiry alerts and renewal logs, then validate from the client trust context.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Only one distro family rejects an internal certificate because its trust store lacks the issuing CA; compare trust bundle and chain, not key permissions alone. **Operator response:** Inspect certificate metadata and chain without printing private keys; check file ownership/mode, expiry alerts and renewal logs, then validate from the client trust context. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: TLS validation checks chain to a trusted root, SAN/hostname, validity window, trust store and service key permissions.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `openssl s_client -connect <host>:443 -servername <host> -showcerts </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates` and follow the evidence path: Inspect certificate metadata and chain without printing private keys; check file ownership/mode, expiry alerts and renewal logs, then validate from the client trust context.

**Q: How would you verify or falsify the working diagnosis?**

A: Only one distro family rejects an internal certificate because its trust store lacks the issuing CA; compare trust bundle and chain, not key permissions alone. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
