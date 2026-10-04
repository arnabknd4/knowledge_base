# Security and isolation

Objective-level study guides for every checkbox skill in this domain.

## Threat Model And Least Privilege
- [Identify Docker security boundaries and trust relationships](threat-model-and-least-privilege/security-boundaries/study-guide.md)
- [Minimize Linux capabilities and device access; avoid privileged mode](threat-model-and-least-privilege/capabilities-and-devices/study-guide.md)
- [Use non-root processes, rootless mode, and user namespace remapping appropriately](threat-model-and-least-privilege/nonroot-rootless-userns/study-guide.md)
- [Apply seccomp and AppArmor or SELinux profiles where available](threat-model-and-least-privilege/seccomp-apparmor-selinux/study-guide.md)
- [Use read-only filesystems, no-new-privileges, resource limits, and network segmentation](threat-model-and-least-privilege/runtime-hardening/study-guide.md)
- [Patch the host kernel, Docker Engine, base images, and application dependencies](threat-model-and-least-privilege/patching-host-and-images/study-guide.md)

## Secrets Access And Image Security
- [Deliver secrets at runtime without baking them into images or build output](secrets-access-and-image-security/runtime-secret-delivery/study-guide.md)
- [Restrict Docker socket access and secure remote Engine API access](secrets-access-and-image-security/daemon-api-and-socket/study-guide.md)
- [Apply least-privilege registry and host access controls and rotate credentials](secrets-access-and-image-security/registry-and-host-access/study-guide.md)
- [Scan images, prioritize vulnerabilities, and rebuild maintained artifacts](secrets-access-and-image-security/image-scanning-and-remediation/study-guide.md)
- [Verify image provenance and signatures according to organizational policy](secrets-access-and-image-security/image-provenance-signatures/study-guide.md)
- [Understand Swarm mutual TLS and secrets without assuming standalone Docker support](secrets-access-and-image-security/swarm-specific-security/study-guide.md)
