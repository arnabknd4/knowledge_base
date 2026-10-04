# Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.

**Syllabus objective (exact wording):** Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.

**Mapping:** `03` → `004` `Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.`

## What

Sudo grants scoped privilege through ordered policy and includes; shared root credentials remove attribution and complicate revocation. Policy syntax and include behavior are distribution-specific.

## Why

This matters operationally: A deployment account needs one service restart but has unrestricted root; grant only the documented command/arguments and validate audit evidence and break-glass access. The decision hinges on these mechanics: Policy syntax and include behavior are distribution-specific.

## How

1. **Establish the relevant boundary:** Sudo grants scoped privilege through ordered policy and includes; shared root credentials remove attribution and complicate revocation. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect effective grants with `sudo -l`; use `visudo` for policy edits and test a dedicated account in a second session before removing existing access.
3. **Exercise the scenario:** A deployment account needs one service restart but has unrestricted root; grant only the documented command/arguments and validate audit evidence and break-glass access.
4. **Verify this outcome:** use `sudo -l` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Policy syntax and include behavior are distribution-specific.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A deployment account needs one service restart but has unrestricted root; grant only the documented command/arguments and validate audit evidence and break-glass access. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
sudo -l
sudo visudo -c
grep -R '^[^#]' /etc/sudoers.d 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect effective grants with `sudo -l`; use `visudo` for policy edits and test a dedicated account in a second session before removing existing access.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A deployment account needs one service restart but has unrestricted root; grant only the documented command/arguments and validate audit evidence and break-glass access. **Operator response:** Inspect effective grants with `sudo -l`; use `visudo` for policy edits and test a dedicated account in a second session before removing existing access. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Sudo grants scoped privilege through ordered policy and includes; shared root credentials remove attribution and complicate revocation.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `sudo -l` and follow the evidence path: Inspect effective grants with `sudo -l`; use `visudo` for policy edits and test a dedicated account in a second session before removing existing access.

**Q: How would you verify or falsify the working diagnosis?**

A: A deployment account needs one service restart but has unrestricted root; grant only the documented command/arguments and validate audit evidence and break-glass access. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
