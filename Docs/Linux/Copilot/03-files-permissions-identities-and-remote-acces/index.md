# 03. Files, permissions, identities, and remote access

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Identity and access

- [Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.](01-identity-and-access/001-explain-file-types-inode-metadata-hard-and-symbolic-links-owners/study-guide.md)
- [Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).](01-identity-and-access/002-apply-least-privilege-conceptually-owner-group-other-access-setu/study-guide.md)
- [Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.](01-identity-and-access/003-understand-etc-passwd-etc-shadow-etc-group-local-identity-tools/study-guide.md)
- [Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.](01-identity-and-access/004-explain-sudo-policy-scoped-privilege-auditability-secure-sudoers/study-guide.md)
- [Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).](01-identity-and-access/005-understand-pam-as-a-configurable-authentication-stack-know-where/study-guide.md)
- [Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.](01-identity-and-access/006-operate-ssh-conceptually-host-keys-versus-user-keys-authorized-k/study-guide.md)
- [Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.](01-identity-and-access/007-apply-ssh-hardening-principles-minimize-exposure-use-managed-ide/study-guide.md)
- [Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.](01-identity-and-access/008-identify-ownership-permission-acl-mount-option-and-security-poli/study-guide.md)
- [Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).](01-identity-and-access/009-understand-file-attributes-acl-portability-and-ownership-mode-be/study-guide.md)

## Domain scope

This is domain `03` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
