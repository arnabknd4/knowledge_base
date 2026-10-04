# Linux Architect-Level Study Library

Objective-level material for the role-based DevOps, SRE, and Linux/platform architect syllabus. This is a practical learning library, not an official certification blueprint.

## How to use the library

- Domains 01–12 cover the shared Linux outcomes.
- Domain 13 contains explicit role-track extensions and capstones; these complement rather than duplicate shared outcomes.
- Domain 14 contains the lab-safety and practical-readiness checklist outcomes.
- Every syllabus `- [ ]` maps to one guide; the exact objective wording is prominent in that guide and linked from its domain index.
- Start with read-only inspection and a disposable lab. Destructive or disruptive operations are lab-only unless separately approved through production change management.
- Linux behavior, commands, paths, and support policies vary by distribution, release, kernel, and installed packages. Check local manuals and official release-specific documentation.

## Syllabus

[Linux syllabus](copilot-Linux-syllabus.md)

## Domain indexes and objective guides

### 01. Linux foundations, distributions, and lifecycle

[Open domain index](01-linux-foundations-distributions-and-lifecycle/index.md)
- [Explain kernel, system calls, user space, libraries, shells, services, and the boundary between kernel and distribution.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/001-explain-kernel-system-calls-user-space-libraries-shells-services/study-guide.md)
- [Identify CPU architecture, kernel release, distribution, release lifecycle, and support policy; distinguish upstream kernel version from vendor-maintained kernels.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/002-identify-cpu-architecture-kernel-release-distribution-release-li/study-guide.md)
- [Compare RHEL-family systems (RHEL, Rocky Linux, AlmaLinux), Debian/Ubuntu, Amazon Linux, and minimal/container-focused distributions; understand support and compatibility implications.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/003-compare-rhel-family-systems-rhel-rocky-linux-almalinux-debian-ub/study-guide.md)
- [Compare package formats and tools: RPM/DNF and `rpm`; DEB/APT and `dpkg`; repositories, signing, metadata, dependency resolution, pinning/version locks, and package provenance.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/004-compare-package-formats-and-tools-rpm-dnf-and-rpm-deb-apt-and-dp/study-guide.md)
- [Understand the Filesystem Hierarchy Standard and the roles of `/etc`, `/var`, `/usr`, `/opt`, `/home`, `/run`, `/proc`, `/sys`, and `/dev`.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/005-understand-the-filesystem-hierarchy-standard-and-the-roles-of-et/study-guide.md)
- [Describe BIOS/UEFI, firmware, bootloader (commonly GRUB), kernel and initramfs, root filesystem handoff, and PID 1.](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/006-describe-bios-uefi-firmware-bootloader-commonly-grub-kernel-and/study-guide.md)
- [Recognize rescue/emergency boot paths, kernel command-line parameters, initramfs purpose, and recovery considerations (P1).](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/007-recognize-rescue-emergency-boot-paths-kernel-command-line-parame/study-guide.md)
- [Learn kernel modules, module dependencies/signing at a conceptual level, and the distinction between loading a module and installing its package (P2).](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/008-learn-kernel-modules-module-dependencies-signing-at-a-conceptual/study-guide.md)
- [Identify architecture-dependent and cloud-image differences that affect boot, devices, firmware, and package availability (A).](01-linux-foundations-distributions-and-lifecycle/01-foundations-and-lifecycle/009-identify-architecture-dependent-and-cloud-image-differences-that/study-guide.md)

### 02. Shell, command-line operations, and automation

[Open domain index](02-shell-command-line-operations-and-automation/index.md)
- [Use Bash safely: quoting, globbing, variables, environment, command substitution, exit status, pipes, redirection, file descriptors, and `set` behavior.](02-shell-command-line-operations-and-automation/01-shell-and-automation/001-use-bash-safely-quoting-globbing-variables-environment-command-s/study-guide.md)
- [Navigate and inspect files with core utilities; use `find`, `grep`/`rg`, `xargs`, `sort`, `uniq`, `cut`, `awk`, `sed`, `tee`, and regular expressions.](02-shell-command-line-operations-and-automation/01-shell-and-automation/002-navigate-and-inspect-files-with-core-utilities-use-find-grep-rg/study-guide.md)
- [Understand pipelines, text versus binary data, locale effects, and robust handling of whitespace and filenames.](02-shell-command-line-operations-and-automation/01-shell-and-automation/003-understand-pipelines-text-versus-binary-data-locale-effects-and/study-guide.md)
- [Use `man`, `info`, `--help`, shell built-ins, and package documentation; locate relevant manual sections and distinguish local documentation from online versions.](02-shell-command-line-operations-and-automation/01-shell-and-automation/004-use-man-info-help-shell-built-ins-and-package-documentation-loca/study-guide.md)
- [Edit files with a terminal editor; use Git for versioned configuration and change review.](02-shell-command-line-operations-and-automation/01-shell-and-automation/005-edit-files-with-a-terminal-editor-use-git-for-versioned-configur/study-guide.md)
- [Package and transfer data with `tar`, compression tools, `rsync`, and checksums; understand metadata preservation and integrity verification.](02-shell-command-line-operations-and-automation/01-shell-and-automation/006-package-and-transfer-data-with-tar-compression-tools-rsync-and-c/study-guide.md)
- [Write maintainable shell scripts with arguments, functions, validation, logging, traps, exit codes, idempotence, and safe failure handling (P1).](02-shell-command-line-operations-and-automation/01-shell-and-automation/007-write-maintainable-shell-scripts-with-arguments-functions-valida/study-guide.md)
- [Test scripts with disposable inputs, lint/static checks where available, and controlled execution; avoid blindly piping downloaded content to a privileged shell.](02-shell-command-line-operations-and-automation/01-shell-and-automation/008-test-scripts-with-disposable-inputs-lint-static-checks-where-ava/study-guide.md)
- [Distinguish interactive shell startup files from login/non-login and system-wide shell configuration.](02-shell-command-line-operations-and-automation/01-shell-and-automation/009-distinguish-interactive-shell-startup-files-from-login-non-login/study-guide.md)
- [Automate repeatable tasks through reviewed scripts and configuration-management tools; keep secrets out of source and logs (D, S).](02-shell-command-line-operations-and-automation/01-shell-and-automation/010-automate-repeatable-tasks-through-reviewed-scripts-and-configura/study-guide.md)

### 03. Files, permissions, identities, and remote access

[Open domain index](03-files-permissions-identities-and-remote-acces/index.md)
- [Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/001-explain-file-types-inode-metadata-hard-and-symbolic-links-owners/study-guide.md)
- [Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).](03-files-permissions-identities-and-remote-acces/01-identity-and-access/002-apply-least-privilege-conceptually-owner-group-other-access-setu/study-guide.md)
- [Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/003-understand-etc-passwd-etc-shadow-etc-group-local-identity-tools/study-guide.md)
- [Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/004-explain-sudo-policy-scoped-privilege-auditability-secure-sudoers/study-guide.md)
- [Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).](03-files-permissions-identities-and-remote-acces/01-identity-and-access/005-understand-pam-as-a-configurable-authentication-stack-know-where/study-guide.md)
- [Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/006-operate-ssh-conceptually-host-keys-versus-user-keys-authorized-k/study-guide.md)
- [Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/007-apply-ssh-hardening-principles-minimize-exposure-use-managed-ide/study-guide.md)
- [Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.](03-files-permissions-identities-and-remote-acces/01-identity-and-access/008-identify-ownership-permission-acl-mount-option-and-security-poli/study-guide.md)
- [Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).](03-files-permissions-identities-and-remote-acces/01-identity-and-access/009-understand-file-attributes-acl-portability-and-ownership-mode-be/study-guide.md)

### 04. Processes, scheduling, boot, and services

[Open domain index](04-processes-scheduling-boot-and-services/index.md)
- [Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.](04-processes-scheduling-boot-and-services/01-processes-and-services/001-explain-process-creation-and-lifecycle-pid-ppid-threads-process/study-guide.md)
- [Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.](04-processes-scheduling-boot-and-services/01-processes-and-services/002-inspect-processes-open-files-sockets-and-resource-limits-underst/study-guide.md)
- [Distinguish graceful termination from forced termination and understand the operational consequences of each.](04-processes-scheduling-boot-and-services/01-processes-and-services/003-distinguish-graceful-termination-from-forced-termination-and-und/study-guide.md)
- [Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).](04-processes-scheduling-boot-and-services/01-processes-and-services/004-understand-cpu-scheduling-priorities-nice-affinity-real-time-sch/study-guide.md)
- [Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.](04-processes-scheduling-boot-and-services/01-processes-and-services/005-compare-cron-at-style-scheduling-with-systemd-timers-account-for/study-guide.md)
- [Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.](04-processes-scheduling-boot-and-services/01-processes-and-services/006-understand-systemd-units-dependencies-targets-service-types-rest/study-guide.md)
- [Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.](04-processes-scheduling-boot-and-services/01-processes-and-services/007-read-service-state-and-journal-logs-correlate-boot-id-timestamps/study-guide.md)
- [Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.](04-processes-scheduling-boot-and-services/01-processes-and-services/008-understand-sysv-init-runlevel-compatibility-as-legacy-context-no/study-guide.md)
- [Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.](04-processes-scheduling-boot-and-services/01-processes-and-services/009-diagnose-boot-failures-using-console-access-previous-boot-logs-r/study-guide.md)
- [Plan safe service changes, validation, rollback, and health checks before deployment (D, S).](04-processes-scheduling-boot-and-services/01-processes-and-services/010-plan-safe-service-changes-validation-rollback-and-health-checks/study-guide.md)

### 05. CPU, memory, performance, and observability

[Open domain index](05-cpu-memory-performance-and-observability/index.md)
- [Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.](05-cpu-memory-performance-and-observability/01-performance-and-observability/001-interpret-load-average-in-context-distinguish-runnable-work-cpu/study-guide.md)
- [Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.](05-cpu-memory-performance-and-observability/01-performance-and-observability/002-understand-virtual-memory-page-cache-reclaim-swap-overcommit-oom/study-guide.md)
- [Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.](05-cpu-memory-performance-and-observability/01-performance-and-observability/003-inspect-cpu-memory-pressure-disk-and-network-symptoms-using-stan/study-guide.md)
- [Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.](05-cpu-memory-performance-and-observability/01-performance-and-observability/004-read-proc-and-sys-as-kernel-interfaces-recognize-that-values-and/study-guide.md)
- [Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.](05-cpu-memory-performance-and-observability/01-performance-and-observability/005-understand-latency-throughput-utilization-saturation-errors-and/study-guide.md)
- [Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).](05-cpu-memory-performance-and-observability/01-performance-and-observability/006-use-logs-metrics-traces-profiling-and-events-as-complementary-ob/study-guide.md)
- [Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).](05-cpu-memory-performance-and-observability/01-performance-and-observability/007-learn-vmstat-iostat-sar-pidstat-top-ps-free-ss-lsof-strace-and-p/study-guide.md)
- [Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).](05-cpu-memory-performance-and-observability/01-performance-and-observability/008-understand-ebpf-based-observability-and-its-kernel-privilege-too/study-guide.md)
- [Evaluate kernel and service tuning using workload measurements, documented tradeoffs, staged rollout, and rollback; avoid copying generic tuning recipes.](05-cpu-memory-performance-and-observability/01-performance-and-observability/009-evaluate-kernel-and-service-tuning-using-workload-measurements-d/study-guide.md)
- [Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).](05-cpu-memory-performance-and-observability/01-performance-and-observability/010-relate-kernel-counters-and-host-symptoms-to-application-slos-and/study-guide.md)

### 06. Storage, filesystems, and data protection

[Open domain index](06-storage-filesystems-and-data-protection/index.md)
- [Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/001-distinguish-block-file-and-object-storage-understand-local-ephem/study-guide.md)
- [Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/002-trace-storage-layers-device-partition-table-raid-encryption-lvm/study-guide.md)
- [Understand GPT/partition concepts; inspect block devices and capacity without modifying them.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/003-understand-gpt-partition-concepts-inspect-block-devices-and-capa/study-guide.md)
- [Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/004-compare-ext4-xfs-btrfs-tmpfs-and-network-filesystems-by-operatio/study-guide.md)
- [Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/005-understand-mount-points-mount-namespaces-mount-options-etc-fstab/study-guide.md)
- [Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/006-explain-lvm-pv-vg-lv-concepts-allocation-growth-snapshots-and-th/study-guide.md)
- [Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/007-understand-raid-levels-software-raid-hardware-raid-rebuild-risk/study-guide.md)
- [Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/008-understand-swap-purpose-and-behavior-use-workload-and-memory-evi/study-guide.md)
- [Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).](06-storage-filesystems-and-data-protection/01-storage-and-recovery/009-learn-filesystem-capacity-versus-inode-exhaustion-reserved-block/study-guide.md)
- [Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).](06-storage-filesystems-and-data-protection/01-storage-and-recovery/010-understand-nfs-and-iscsi-fundamentals-recognize-permissions-iden/study-guide.md)
- [Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/011-plan-backups-around-recovery-point-and-recovery-time-objectives/study-guide.md)
- [Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.](06-storage-filesystems-and-data-protection/01-storage-and-recovery/012-compare-snapshots-replication-backups-and-disaster-recovery-test/study-guide.md)
- [Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).](06-storage-filesystems-and-data-protection/01-storage-and-recovery/013-evaluate-cloud-block-and-object-storage-durability-performance-a/study-guide.md)

### 07. Networking and network troubleshooting

[Open domain index](07-networking-and-network-troubleshooting/index.md)
- [Explain Ethernet, IP addressing/subnets, IPv4/IPv6, TCP/UDP, ports, sockets, ARP/neighbor discovery, MTU, and path MTU.](07-networking-and-network-troubleshooting/01-networking/001-explain-ethernet-ip-addressing-subnets-ipv4-ipv6-tcp-udp-ports-s/study-guide.md)
- [Inspect links, addresses, routes, rules, and sockets; distinguish local, routed, and name-resolution failures.](07-networking-and-network-troubleshooting/01-networking/002-inspect-links-addresses-routes-rules-and-sockets-distinguish-loc/study-guide.md)
- [Understand default and policy routing, gateways, source selection, forwarding, NAT, and asymmetric routing.](07-networking-and-network-troubleshooting/01-networking/003-understand-default-and-policy-routing-gateways-source-selection/study-guide.md)
- [Explain DNS resolution paths, search domains, caching, split DNS, resolver configuration, and service discovery.](07-networking-and-network-troubleshooting/01-networking/004-explain-dns-resolution-paths-search-domains-caching-split-dns-re/study-guide.md)
- [Compare NetworkManager/nmcli, Netplan, systemd-networkd, and distribution-specific network configuration; avoid assuming one control plane everywhere.](07-networking-and-network-troubleshooting/01-networking/005-compare-networkmanager-nmcli-netplan-systemd-networkd-and-distri/study-guide.md)
- [Understand firewall concepts and packet flow; distinguish nftables, firewalld, and UFW interfaces, plus legacy iptables compatibility.](07-networking-and-network-troubleshooting/01-networking/006-understand-firewall-concepts-and-packet-flow-distinguish-nftable/study-guide.md)
- [Understand bridges, VLANs, bonding/teaming, virtual interfaces, tunnels, and overlay networks (P1).](07-networking-and-network-troubleshooting/01-networking/007-understand-bridges-vlans-bonding-teaming-virtual-interfaces-tunn/study-guide.md)
- [Explain network namespaces, veth pairs, container networking, and host/container port publishing.](07-networking-and-network-troubleshooting/01-networking/008-explain-network-namespaces-veth-pairs-container-networking-and-h/study-guide.md)
- [Use packet capture and connection tests thoughtfully; understand capture scope, permissions, privacy, and production impact.](07-networking-and-network-troubleshooting/01-networking/009-use-packet-capture-and-connection-tests-thoughtfully-understand/study-guide.md)
- [Diagnose with layered, hypothesis-driven checks; correlate DNS, routing, firewall, socket, TLS, and application health.](07-networking-and-network-troubleshooting/01-networking/010-diagnose-with-layered-hypothesis-driven-checks-correlate-dns-rou/study-guide.md)
- [Understand time synchronization (chrony/NTP), clock drift, certificates, and distributed-system consequences (S).](07-networking-and-network-troubleshooting/01-networking/011-understand-time-synchronization-chrony-ntp-clock-drift-certifica/study-guide.md)

### 08. Security, compliance, and patching

[Open domain index](08-security-compliance-and-patching/index.md)
- [Apply least privilege, defense in depth, secure defaults, attack-surface reduction, and threat modeling to hosts and images.](08-security-compliance-and-patching/01-security-and-patching/001-apply-least-privilege-defense-in-depth-secure-defaults-attack-su/study-guide.md)
- [Understand discretionary access control (DAC), mandatory access control (MAC), Linux Security Modules, and how SELinux and AppArmor enforce policy.](08-security-compliance-and-patching/01-security-and-patching/002-understand-discretionary-access-control-dac-mandatory-access-con/study-guide.md)
- [Distinguish SELinux modes, labels, policy, and audit denials from ordinary file permissions; distinguish AppArmor profiles and enforcement modes.](08-security-compliance-and-patching/01-security-and-patching/003-distinguish-selinux-modes-labels-policy-and-audit-denials-from-o/study-guide.md)
- [Learn Linux capabilities and their relationship to root privilege; understand why broad capabilities can undermine isolation.](08-security-compliance-and-patching/01-security-and-patching/004-learn-linux-capabilities-and-their-relationship-to-root-privileg/study-guide.md)
- [Understand seccomp, namespaces, cgroups, syscall filtering, and host/container boundary limitations.](08-security-compliance-and-patching/01-security-and-patching/005-understand-seccomp-namespaces-cgroups-syscall-filtering-and-host/study-guide.md)
- [Secure boot and update lifecycle conceptually: signed packages, repository trust, kernel updates, reboot planning, live-patching constraints, and rollback strategy.](08-security-compliance-and-patching/01-security-and-patching/006-secure-boot-and-update-lifecycle-conceptually-signed-packages-re/study-guide.md)
- [Understand vulnerability and configuration management, supported release windows, emergency patching, and staged validation.](08-security-compliance-and-patching/01-security-and-patching/007-understand-vulnerability-and-configuration-management-supported/study-guide.md)
- [Learn audit records and system logging, auditd concepts, time integrity, retention, and centralized tamper-resistant log collection (P1).](08-security-compliance-and-patching/01-security-and-patching/008-learn-audit-records-and-system-logging-auditd-concepts-time-inte/study-guide.md)
- [Protect secrets, private keys, credentials, and certificates using managed secret stores, access control, rotation, and redaction.](08-security-compliance-and-patching/01-security-and-patching/009-protect-secrets-private-keys-credentials-and-certificates-using/study-guide.md)
- [Understand TLS certificate chains, key permissions, expiry, trust stores, and service renewal; avoid exposing private key material.](08-security-compliance-and-patching/01-security-and-patching/010-understand-tls-certificate-chains-key-permissions-expiry-trust-s/study-guide.md)
- [Use security baselines such as CIS or applicable organizational/regulatory baselines as review inputs, not blindly applied scripts.](08-security-compliance-and-patching/01-security-and-patching/011-use-security-baselines-such-as-cis-or-applicable-organizational/study-guide.md)
- [Understand host firewalls, SSH policy, disk encryption, secure boot, identity integration, and audit requirements in context.](08-security-compliance-and-patching/01-security-and-patching/012-understand-host-firewalls-ssh-policy-disk-encryption-secure-boot/study-guide.md)
- [Treat security controls as observable and testable; verify that hardening does not silently break service health.](08-security-compliance-and-patching/01-security-and-patching/013-treat-security-controls-as-observable-and-testable-verify-that-h/study-guide.md)

### 09. Containers and virtualization foundations

[Open domain index](09-containers-and-virtualization-foundations/index.md)
- [Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/001-understand-virtual-machines-hypervisors-kvm-guest-kernels-images/study-guide.md)
- [Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/002-explain-namespaces-for-pid-mount-network-user-uts-and-ipc-isolat/study-guide.md)
- [Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/003-explain-cgroups-v1-versus-v2-at-a-conceptual-and-operational-lev/study-guide.md)
- [Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/004-understand-container-image-layers-registries-overlay-filesystems/study-guide.md)
- [Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/005-distinguish-containerd-cri-o-runc-and-higher-level-orchestration/study-guide.md)
- [Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/006-inspect-the-relationship-between-systemd-cgroups-container-runti/study-guide.md)
- [Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/007-understand-container-capabilities-seccomp-lsm-integration-user-n/study-guide.md)
- [Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.](09-containers-and-virtualization-foundations/01-virtualization-and-containers/008-know-when-a-workload-requires-a-vm-or-stronger-isolation-boundar/study-guide.md)
- [Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).](09-containers-and-virtualization-foundations/01-virtualization-and-containers/009-investigate-host-level-causes-of-container-failures-disk-pressur/study-guide.md)

### 10. Cloud operations, configuration management, and immutable systems

[Open domain index](10-cloud-operations-configuration-management-and/index.md)
- [Understand cloud-init stages, datasource/metadata, user data, instance identity, first-boot behavior, and cloud-image customization.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/001-understand-cloud-init-stages-datasource-metadata-user-data-insta/study-guide.md)
- [Keep bootstrap configuration idempotent and safe to rerun; handle secrets and metadata-service access deliberately.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/002-keep-bootstrap-configuration-idempotent-and-safe-to-rerun-handle/study-guide.md)
- [Compare imperative administration with declarative configuration management; understand desired state, drift detection, inventory, and convergence.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/003-compare-imperative-administration-with-declarative-configuration/study-guide.md)
- [Use reviewed configuration changes, version control, staged rollout, canaries, health checks, and rollback.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/004-use-reviewed-configuration-changes-version-control-staged-rollou/study-guide.md)
- [Understand immutable image workflows, golden images, image pipelines, signed/provenance-aware artifacts, and replacement rather than ad hoc repair.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/005-understand-immutable-image-workflows-golden-images-image-pipelin/study-guide.md)
- [Distinguish mutable host administration from container/image and fleet management; know when each pattern is appropriate.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/006-distinguish-mutable-host-administration-from-container-image-and/study-guide.md)
- [Understand fleet identity, centralized logging/metrics, patch orchestration, access lifecycle, and configuration ownership.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/007-understand-fleet-identity-centralized-logging-metrics-patch-orch/study-guide.md)
- [Plan for cloud-specific device naming, transient disks, metadata, network interfaces, and provider-managed agents.](10-cloud-operations-configuration-management-and/01-cloud-operations-and-configuration/008-plan-for-cloud-specific-device-naming-transient-disks-metadata-n/study-guide.md)

### 11. Reliability, high availability, and capacity

[Open domain index](11-reliability-high-availability-and-capacity/index.md)
- [Relate Linux host availability to application dependencies, failure domains, redundancy, health checks, and graceful degradation.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/001-relate-linux-host-availability-to-application-dependencies-failu/study-guide.md)
- [Understand HA primitives: service supervision, load balancing, failover, fencing, quorum, VIP/VRRP, and cluster membership.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/002-understand-ha-primitives-service-supervision-load-balancing-fail/study-guide.md)
- [Compare active-active and active-passive designs; account for split brain, state replication, and recovery behavior.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/003-compare-active-active-and-active-passive-designs-account-for-spl/study-guide.md)
- [Design capacity around CPU, memory, I/O, network, file descriptors, connection tracking, disk growth, and workload peaks.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/004-design-capacity-around-cpu-memory-i-o-network-file-descriptors-c/study-guide.md)
- [Use measured utilization, headroom, growth forecasts, and load tests to plan scaling; distinguish average from tail demand.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/005-use-measured-utilization-headroom-growth-forecasts-and-load-test/study-guide.md)
- [Understand kernel and service resource limits, noisy neighbors, NUMA, cgroup controls, and cloud instance sizing.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/006-understand-kernel-and-service-resource-limits-noisy-neighbors-nu/study-guide.md)
- [Define RTO/RPO, backup/restore procedures, multi-zone/region strategy, and disaster-recovery exercises.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/007-define-rto-rpo-backup-restore-procedures-multi-zone-region-strat/study-guide.md)
- [Document lifecycle and support choices: LTS/vendor support, kernel cadence, upgrade windows, package repositories, and compatibility.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/008-document-lifecycle-and-support-choices-lts-vendor-support-kernel/study-guide.md)
- [Treat tuning as a hypothesis-driven change with baseline, measurable outcome, bounded blast radius, and rollback.](11-reliability-high-availability-and-capacity/01-reliability-and-capacity/009-treat-tuning-as-a-hypothesis-driven-change-with-baseline-measura/study-guide.md)

### 12. Incident response and operational readiness

[Open domain index](12-incident-response-and-operational-readiness/index.md)
- [Use a consistent triage loop: establish impact and scope; check recent changes; preserve evidence; gather host, service, and dependency signals; form and test hypotheses.](12-incident-response-and-operational-readiness/01-incident-response/001-use-a-consistent-triage-loop-establish-impact-and-scope-check-re/study-guide.md)
- [Prioritize reversible, low-risk diagnostic actions before remediation; communicate impact, owners, timeline, and uncertainty.](12-incident-response-and-operational-readiness/01-incident-response/002-prioritize-reversible-low-risk-diagnostic-actions-before-remedia/study-guide.md)
- [Investigate service down, boot failure, disk full, inode exhaustion, memory pressure, CPU saturation, I/O latency, DNS, routing, certificate expiry, and permission failures.](12-incident-response-and-operational-readiness/01-incident-response/003-investigate-service-down-boot-failure-disk-full-inode-exhaustion/study-guide.md)
- [Correlate journal/syslog, application logs, metrics, audit records, kernel messages, cloud events, and deployment history.](12-incident-response-and-operational-readiness/01-incident-response/004-correlate-journal-syslog-application-logs-metrics-audit-records/study-guide.md)
- [Understand containment, safe recovery, escalation, and when not to restart or kill processes before evidence is captured.](12-incident-response-and-operational-readiness/01-incident-response/005-understand-containment-safe-recovery-escalation-and-when-not-to/study-guide.md)
- [Maintain runbooks with preconditions, expected output, privilege requirements, impact warnings, verification, and rollback.](12-incident-response-and-operational-readiness/01-incident-response/006-maintain-runbooks-with-preconditions-expected-output-privilege-r/study-guide.md)
- [Conduct blameless post-incident reviews; turn contributing factors into tests, automation, observability, and design changes (S).](12-incident-response-and-operational-readiness/01-incident-response/007-conduct-blameless-post-incident-reviews-turn-contributing-factor/study-guide.md)
- [Practice incident handoffs and communicate operational risks to engineering and architecture stakeholders.](12-incident-response-and-operational-readiness/01-incident-response/008-practice-incident-handoffs-and-communicate-operational-risks-to/study-guide.md)

### 13. Role-based learning tracks

[Open domain index](13-role-based-learning-tracks/index.md)
- [Prioritize shell scripting, Git, package/repository operations, systemd, SSH, cloud-init, image building, and configuration management.](13-role-based-learning-tracks/01-devops-engineer/001-prioritize-shell-scripting-git-package-repository-operations-sys/study-guide.md)
- [Automate provisioning and patching with idempotence, review, tests, secrets handling, and rollback.](13-role-based-learning-tracks/01-devops-engineer/002-automate-provisioning-and-patching-with-idempotence-review-tests/study-guide.md)
- [Understand container host fundamentals, cgroups/namespaces, image provenance, service health checks, and deployment lifecycle.](13-role-based-learning-tracks/01-devops-engineer/003-understand-container-host-fundamentals-cgroups-namespaces-image/study-guide.md)
- [Build runbooks and CI checks for Linux configuration, image baselines, and operational readiness.](13-role-based-learning-tracks/01-devops-engineer/004-build-runbooks-and-ci-checks-for-linux-configuration-image-basel/study-guide.md)
- [Capstone: create a disposable Linux VM/image, provision a least-privilege service account and systemd-managed sample service, apply a versioned configuration, emit useful logs/metrics, and demonstrate safe upgrade and rollback.](13-role-based-learning-tracks/01-devops-engineer/005-capstone-create-a-disposable-linux-vm-image-provision-a-least-pr/study-guide.md)
- [Prioritize Linux performance diagnosis, observability, networking, storage failure modes, systemd recovery, cgroups, and incident response.](13-role-based-learning-tracks/02-site-reliability-engineer-sre/006-prioritize-linux-performance-diagnosis-observability-networking/study-guide.md)
- [Relate host-level signals to user-visible symptoms, SLOs, error budgets, capacity forecasts, and alert quality.](13-role-based-learning-tracks/02-site-reliability-engineer-sre/007-relate-host-level-signals-to-user-visible-symptoms-slos-error-bu/study-guide.md)
- [Practice evidence preservation, timelines, mitigations, safe recovery, and blameless learning.](13-role-based-learning-tracks/02-site-reliability-engineer-sre/008-practice-evidence-preservation-timelines-mitigations-safe-recove/study-guide.md)
- [Design and test backup/restore, HA, failure injection in an isolated lab, and operational runbooks.](13-role-based-learning-tracks/02-site-reliability-engineer-sre/009-design-and-test-backup-restore-ha-failure-injection-in-an-isolat/study-guide.md)
- [Capstone: diagnose a deliberately constrained or misconfigured lab service from symptoms and telemetry; document evidence, root cause, risk-controlled mitigation, recovery verification, and follow-up actions.](13-role-based-learning-tracks/02-site-reliability-engineer-sre/010-capstone-diagnose-a-deliberately-constrained-or-misconfigured-la/study-guide.md)
- [Prioritize distro and lifecycle selection, fleet architecture, security boundaries, identity, storage tiers, network design, HA/DR, and capacity.](13-role-based-learning-tracks/03-linux-platform-architect/011-prioritize-distro-and-lifecycle-selection-fleet-architecture-sec/study-guide.md)
- [Evaluate tradeoffs across cloud images, kernel support, compliance, workload isolation, patching cadence, immutable operations, and vendor support.](13-role-based-learning-tracks/03-linux-platform-architect/012-evaluate-tradeoffs-across-cloud-images-kernel-support-compliance/study-guide.md)
- [Define standards for host baselines, observability, access, secrets, image provenance, configuration ownership, and exception handling.](13-role-based-learning-tracks/03-linux-platform-architect/013-define-standards-for-host-baselines-observability-access-secrets/study-guide.md)
- [Model failure domains and recovery objectives; validate assumptions through workload tests and restore/DR exercises.](13-role-based-learning-tracks/03-linux-platform-architect/014-model-failure-domains-and-recovery-objectives-validate-assumptio/study-guide.md)
- [Capstone: produce a Linux platform design for a stated workload, including distro/support rationale, image and patch strategy, identity and security controls, storage/network layout, observability, capacity assumptions, HA/DR, threat/failure analysis, and an operational acceptance checklist.](13-role-based-learning-tracks/03-linux-platform-architect/015-capstone-produce-a-linux-platform-design-for-a-stated-workload-i/study-guide.md)

### 14. Safe lab and readiness plan

[Open domain index](14-safe-lab-and-readiness-plan/index.md)
- [Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/001-use-disposable-vms-snapshots-or-isolated-cloud-accounts-with-no/study-guide.md)
- [Keep a verified recovery route (console/snapshot/known-good image), and document how to restore before testing boot, network, storage, or security changes.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/002-keep-a-verified-recovery-route-console-snapshot-known-good-image/study-guide.md)
- [Begin with read-only inspection. Never experiment on production or on a device containing needed data.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/003-begin-with-read-only-inspection-never-experiment-on-production-o/study-guide.md)
- [Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/004-treat-partitioning-formatting-filesystem-repair-lvm-raid-changes/study-guide.md)
- [Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/005-confirm-target-devices-mount-points-access-paths-impact-backup-a/study-guide.md)
- [Record baseline, change, verification, and rollback results for each exercise.](14-safe-lab-and-readiness-plan/01-lab-setup-and-safety/006-record-baseline-change-verification-and-rollback-results-for-eac/study-guide.md)
- [Explain the likely cause and next safe observation for a boot, permissions, DNS, disk, memory, or service failure without relying on a memorized fix.](14-safe-lab-and-readiness-plan/02-readiness-checklist/007-explain-the-likely-cause-and-next-safe-observation-for-a-boot-pe/study-guide.md)
- [Identify which details are distro/release-specific and find authoritative local documentation.](14-safe-lab-and-readiness-plan/02-readiness-checklist/008-identify-which-details-are-distro-release-specific-and-find-auth/study-guide.md)
- [Make a reviewed, reversible change and verify both intended effect and absence of regressions.](14-safe-lab-and-readiness-plan/02-readiness-checklist/009-make-a-reviewed-reversible-change-and-verify-both-intended-effec/study-guide.md)
- [Restore data or service from a tested recovery path and state its measured RTO/RPO.](14-safe-lab-and-readiness-plan/02-readiness-checklist/010-restore-data-or-service-from-a-tested-recovery-path-and-state-it/study-guide.md)
- [Communicate impact, evidence, confidence, risk, and next steps clearly.](14-safe-lab-and-readiness-plan/02-readiness-checklist/011-communicate-impact-evidence-confidence-risk-and-next-steps-clear/study-guide.md)
- [Demonstrate automation or design that is repeatable, observable, least-privileged, and maintainable.](14-safe-lab-and-readiness-plan/02-readiness-checklist/012-demonstrate-automation-or-design-that-is-repeatable-observable-l/study-guide.md)

## Authoritative references

- [Linux kernel documentation](https://docs.kernel.org/)
- [Linux man-pages project](https://www.kernel.org/doc/man-pages/)
- [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/)
- [RHEL 9 documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9)
- [Ubuntu Server documentation](https://ubuntu.com/server/docs)
