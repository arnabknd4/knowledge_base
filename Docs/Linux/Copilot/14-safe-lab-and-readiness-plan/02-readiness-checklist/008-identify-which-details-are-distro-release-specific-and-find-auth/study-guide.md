# Identify which details are distro/release-specific and find authoritative local documentation.

**Syllabus objective (exact wording):** Identify which details are distro/release-specific and find authoritative local documentation.

**Mapping:** `14` → `008` `Identify which details are distro/release-specific and find authoritative local documentation.`

## What

Distro/release-specific behavior should be verified against installed manuals, vendor release docs and actual active services; do not assume a derivative inherits upstream support.

## Why

This matters operationally: A firewall runbook supports RHEL and Ubuntu; verify firewalld/nftables versus UFW behavior for the installed release rather than assuming common syntax. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon.

## How

1. **Establish the relevant boundary:** Distro/release-specific behavior should be verified against installed manuals, vendor release docs and actual active services; do not assume a derivative inherits upstream support. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon.
3. **Exercise the scenario:** A firewall runbook supports RHEL and Ubuntu; verify firewalld/nftables versus UFW behavior for the installed release rather than assuming common syntax.
4. **Verify this outcome:** use `cat /etc/os-release` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A firewall runbook supports RHEL and Ubuntu; verify firewalld/nftables versus UFW behavior for the installed release rather than assuming common syntax. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
cat /etc/os-release
man systemctl
systemctl --version
nft --version 2>/dev/null
```

## Do's and Don'ts

- **Do:** Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A firewall runbook supports RHEL and Ubuntu; verify firewalld/nftables versus UFW behavior for the installed release rather than assuming common syntax. **Operator response:** Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Distro/release-specific behavior should be verified against installed manuals, vendor release docs and actual active services; do not assume a derivative inherits upstream support.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /etc/os-release` and follow the evidence path: Identify `/etc/os-release`, package and service versions, then locate the applicable documentation and record the exact behavior/option relied upon.

**Q: How would you verify or falsify the working diagnosis?**

A: A firewall runbook supports RHEL and Ubuntu; verify firewalld/nftables versus UFW behavior for the installed release rather than assuming common syntax. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
