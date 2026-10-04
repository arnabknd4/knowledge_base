# Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).

**Syllabus objective (exact wording):** Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).

**Mapping:** `03` → `005` `Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).`

## What

PAM composes service-specific authentication/account/session modules; control flags and ordering change the outcome. LDAP/Kerberos/SSSD typically integrate through PAM and NSS and depend on network, DNS and time.

## Why

This matters operationally: Local SSH works but directory users fail after a DNS outage; distinguish PAM authentication, NSS account lookup, SSSD cache and Kerberos clock dependencies. The decision hinges on these mechanics: LDAP/Kerberos/SSSD typically integrate through PAM and NSS and depend on network, DNS and time.

## How

1. **Establish the relevant boundary:** PAM composes service-specific authentication/account/session modules; control flags and ordering change the outcome. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify the PAM service stack and NSS lookup path; read module controls and logs before editing. Test changes on a noncritical login with console recovery, especially when central identity is unavailable.
3. **Exercise the scenario:** Local SSH works but directory users fail after a DNS outage; distinguish PAM authentication, NSS account lookup, SSSD cache and Kerberos clock dependencies.
4. **Verify this outcome:** use `grep -R '^[^#]' /etc/pam.d/sshd /etc/nsswitch.conf 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** LDAP/Kerberos/SSSD typically integrate through PAM and NSS and depend on network, DNS and time.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Local SSH works but directory users fail after a DNS outage; distinguish PAM authentication, NSS account lookup, SSSD cache and Kerberos clock dependencies. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
grep -R '^[^#]' /etc/pam.d/sshd /etc/nsswitch.conf 2>/dev/null
getent passwd <user>
systemctl status sssd --no-pager 2>/dev/null
```

## Do's and Don'ts

- **Do:** Identify the PAM service stack and NSS lookup path; read module controls and logs before editing. Test changes on a noncritical login with console recovery, especially when central identity is unavailable.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Local SSH works but directory users fail after a DNS outage; distinguish PAM authentication, NSS account lookup, SSSD cache and Kerberos clock dependencies. **Operator response:** Identify the PAM service stack and NSS lookup path; read module controls and logs before editing. Test changes on a noncritical login with console recovery, especially when central identity is unavailable. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: PAM composes service-specific authentication/account/session modules; control flags and ordering change the outcome.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `grep -R '^[^#]' /etc/pam.d/sshd /etc/nsswitch.conf 2>/dev/null` and follow the evidence path: Identify the PAM service stack and NSS lookup path; read module controls and logs before editing. Test changes on a noncritical login with console recovery, especially when central identity is unavailable.

**Q: How would you verify or falsify the working diagnosis?**

A: Local SSH works but directory users fail after a DNS outage; distinguish PAM authentication, NSS account lookup, SSSD cache and Kerberos clock dependencies. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
