# Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.

**Syllabus objective (exact wording):** Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.

**Mapping:** `03` → `003` `Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.`

## What

Passwd/group databases describe account names and numeric IDs; shadow holds protected password state. UID/GID ranges and account lock/expiry policies vary with distro and directory integration.

## Why

This matters operationally: A restored data directory maps to an unexpected account because numeric UID differs on the destination; inspect `id` and `getent` and plan a controlled ownership mapping. The decision hinges on these mechanics: UID/GID ranges and account lock/expiry policies vary with distro and directory integration.

## How

1. **Establish the relevant boundary:** Passwd/group databases describe account names and numeric IDs; shadow holds protected password state. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Use account-management tools and NSS-aware lookup; verify UID/GID, shell, home, expiry and service ownership before changing identity. Avoid direct edits to shadow/passwd files.
3. **Exercise the scenario:** A restored data directory maps to an unexpected account because numeric UID differs on the destination; inspect `id` and `getent` and plan a controlled ownership mapping.
4. **Verify this outcome:** use `getent passwd <user>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** UID/GID ranges and account lock/expiry policies vary with distro and directory integration.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A restored data directory maps to an unexpected account because numeric UID differs on the destination; inspect `id` and `getent` and plan a controlled ownership mapping. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
getent passwd <user>
id <user>
getent group <group>
passwd -S <user> 2>/dev/null
```

## Do's and Don'ts

- **Do:** Use account-management tools and NSS-aware lookup; verify UID/GID, shell, home, expiry and service ownership before changing identity. Avoid direct edits to shadow/passwd files.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A restored data directory maps to an unexpected account because numeric UID differs on the destination; inspect `id` and `getent` and plan a controlled ownership mapping. **Operator response:** Use account-management tools and NSS-aware lookup; verify UID/GID, shell, home, expiry and service ownership before changing identity. Avoid direct edits to shadow/passwd files. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Passwd/group databases describe account names and numeric IDs; shadow holds protected password state.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `getent passwd <user>` and follow the evidence path: Use account-management tools and NSS-aware lookup; verify UID/GID, shell, home, expiry and service ownership before changing identity. Avoid direct edits to shadow/passwd files.

**Q: How would you verify or falsify the working diagnosis?**

A: A restored data directory maps to an unexpected account because numeric UID differs on the destination; inspect `id` and `getent` and plan a controlled ownership mapping. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
