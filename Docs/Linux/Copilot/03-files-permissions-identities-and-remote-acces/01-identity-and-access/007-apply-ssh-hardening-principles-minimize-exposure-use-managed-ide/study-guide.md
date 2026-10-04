# Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.

**Syllabus objective (exact wording):** Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.

**Mapping:** `03` → `007` `Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.`

## What

SSH hardening balances reduced attack surface with recoverable administration: restrict identities/sources and use managed short-lived credentials where feasible. Server options and defaults differ by OpenSSH version/distro.

## Why

This matters operationally: Disabling password login can lock out an operator if key distribution or PAM policy is broken; test a second session and out-of-band access before applying. The decision hinges on these mechanics: Server options and defaults differ by OpenSSH version/distro.

## How

1. **Establish the relevant boundary:** SSH hardening balances reduced attack surface with recoverable administration: restrict identities/sources and use managed short-lived credentials where feasible. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect effective `sshd` configuration and authorized-key options; validate syntax, open a second authenticated session and verify console/bastion access before reload.
3. **Exercise the scenario:** Disabling password login can lock out an operator if key distribution or PAM policy is broken; test a second session and out-of-band access before applying.
4. **Verify this outcome:** use `sshd -T 2>/dev/null | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers)'` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Server options and defaults differ by OpenSSH version/distro.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Disabling password login can lock out an operator if key distribution or PAM policy is broken; test a second session and out-of-band access before applying. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
sshd -T 2>/dev/null | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers)'
sshd -t
```

## Do's and Don'ts

- **Do:** Inspect effective `sshd` configuration and authorized-key options; validate syntax, open a second authenticated session and verify console/bastion access before reload.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Disabling password login can lock out an operator if key distribution or PAM policy is broken; test a second session and out-of-band access before applying. **Operator response:** Inspect effective `sshd` configuration and authorized-key options; validate syntax, open a second authenticated session and verify console/bastion access before reload. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SSH hardening balances reduced attack surface with recoverable administration: restrict identities/sources and use managed short-lived credentials where feasible.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `sshd -T 2>/dev/null | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers)'` and follow the evidence path: Inspect effective `sshd` configuration and authorized-key options; validate syntax, open a second authenticated session and verify console/bastion access before reload.

**Q: How would you verify or falsify the working diagnosis?**

A: Disabling password login can lock out an operator if key distribution or PAM policy is broken; test a second session and out-of-band access before applying. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
