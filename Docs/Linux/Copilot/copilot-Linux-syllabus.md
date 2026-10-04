# Linux Syllabus for DevOps, SRE, and Architect Roles

**Purpose:** A practical, role-based study syllabus for operating and designing Linux systems in modern production environments.

> This is a role-based learning plan, not a single official certification or exam blueprint. Priorities below are study and operational priorities, not invented exam weights. Linux behavior and available tooling vary by distribution, release, kernel, and installed packages; validate guidance against the target system's official documentation.

## How to use this syllabus

- **P0 — Core:** expected for all three role tracks.
- **P1 — Applied:** needed to operate production systems and investigate common failures.
- **P2 — Advanced / role-dependent:** deepen according to workload, environment, and role.
- **Role tags:** **D** = DevOps, **S** = SRE, **A** = Architect. Untagged topics apply to all.
- Build knowledge in a disposable VM or isolated cloud lab. Read command help and man pages before acting; use read-only inspection first, preserve evidence, and understand rollback before any change.

## 1. Linux foundations, distributions, and lifecycle — P0

- [ ] Explain kernel, system calls, user space, libraries, shells, services, and the boundary between kernel and distribution.
- [ ] Identify CPU architecture, kernel release, distribution, release lifecycle, and support policy; distinguish upstream kernel version from vendor-maintained kernels.
- [ ] Compare RHEL-family systems (RHEL, Rocky Linux, AlmaLinux), Debian/Ubuntu, Amazon Linux, and minimal/container-focused distributions; understand support and compatibility implications.
- [ ] Compare package formats and tools: RPM/DNF and `rpm`; DEB/APT and `dpkg`; repositories, signing, metadata, dependency resolution, pinning/version locks, and package provenance.
- [ ] Understand the Filesystem Hierarchy Standard and the roles of `/etc`, `/var`, `/usr`, `/opt`, `/home`, `/run`, `/proc`, `/sys`, and `/dev`.
- [ ] Describe BIOS/UEFI, firmware, bootloader (commonly GRUB), kernel and initramfs, root filesystem handoff, and PID 1.
- [ ] Recognize rescue/emergency boot paths, kernel command-line parameters, initramfs purpose, and recovery considerations (P1).
- [ ] Learn kernel modules, module dependencies/signing at a conceptual level, and the distinction between loading a module and installing its package (P2).
- [ ] Identify architecture-dependent and cloud-image differences that affect boot, devices, firmware, and package availability (A).

## 2. Shell, command-line operations, and automation — P0

- [ ] Use Bash safely: quoting, globbing, variables, environment, command substitution, exit status, pipes, redirection, file descriptors, and `set` behavior.
- [ ] Navigate and inspect files with core utilities; use `find`, `grep`/`rg`, `xargs`, `sort`, `uniq`, `cut`, `awk`, `sed`, `tee`, and regular expressions.
- [ ] Understand pipelines, text versus binary data, locale effects, and robust handling of whitespace and filenames.
- [ ] Use `man`, `info`, `--help`, shell built-ins, and package documentation; locate relevant manual sections and distinguish local documentation from online versions.
- [ ] Edit files with a terminal editor; use Git for versioned configuration and change review.
- [ ] Package and transfer data with `tar`, compression tools, `rsync`, and checksums; understand metadata preservation and integrity verification.
- [ ] Write maintainable shell scripts with arguments, functions, validation, logging, traps, exit codes, idempotence, and safe failure handling (P1).
- [ ] Test scripts with disposable inputs, lint/static checks where available, and controlled execution; avoid blindly piping downloaded content to a privileged shell.
- [ ] Distinguish interactive shell startup files from login/non-login and system-wide shell configuration.
- [ ] Automate repeatable tasks through reviewed scripts and configuration-management tools; keep secrets out of source and logs (D, S).

## 3. Files, permissions, identities, and remote access — P0

- [ ] Explain file types, inode metadata, hard and symbolic links, ownership, mode bits, umask, and directory traversal permissions.
- [ ] Apply least privilege conceptually: owner/group/other access, setuid/setgid/sticky bits, POSIX ACLs, and default ACLs (P1).
- [ ] Understand `/etc/passwd`, `/etc/shadow`, `/etc/group`, local identity tools, UID/GID ranges, service accounts, and account lifecycle.
- [ ] Explain sudo policy, scoped privilege, auditability, secure sudoers editing/validation, and why shared root access is poor practice.
- [ ] Understand PAM as a configurable authentication stack; know where centralized identity (LDAP, Kerberos, SSSD, directory services) fits (P1).
- [ ] Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.
- [ ] Apply SSH hardening principles: minimize exposure, use managed identities/keys, restrict access, monitor authentication, and preserve a tested recovery path.
- [ ] Identify ownership, permission, ACL, mount-option, and security-policy layers when diagnosing access denied.
- [ ] Understand file attributes, ACL portability, and ownership/mode behavior across filesystems and network mounts (P2).

## 4. Processes, scheduling, boot, and services — P0

- [ ] Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.
- [ ] Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.
- [ ] Distinguish graceful termination from forced termination and understand the operational consequences of each.
- [ ] Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).
- [ ] Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.
- [ ] Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.
- [ ] Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.
- [ ] Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.
- [ ] Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.
- [ ] Plan safe service changes, validation, rollback, and health checks before deployment (D, S).

## 5. CPU, memory, performance, and observability — P0/P1

- [ ] Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.
- [ ] Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.
- [ ] Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.
- [ ] Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.
- [ ] Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.
- [ ] Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).
- [ ] Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).
- [ ] Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).
- [ ] Evaluate kernel and service tuning using workload measurements, documented tradeoffs, staged rollout, and rollback; avoid copying generic tuning recipes.
- [ ] Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).

## 6. Storage, filesystems, and data protection — P0/P1

- [ ] Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.
- [ ] Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.
- [ ] Understand GPT/partition concepts; inspect block devices and capacity without modifying them.
- [ ] Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.
- [ ] Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.
- [ ] Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.
- [ ] Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.
- [ ] Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.
- [ ] Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).
- [ ] Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).
- [ ] Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.
- [ ] Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.
- [ ] Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).

## 7. Networking and network troubleshooting — P0/P1

- [ ] Explain Ethernet, IP addressing/subnets, IPv4/IPv6, TCP/UDP, ports, sockets, ARP/neighbor discovery, MTU, and path MTU.
- [ ] Inspect links, addresses, routes, rules, and sockets; distinguish local, routed, and name-resolution failures.
- [ ] Understand default and policy routing, gateways, source selection, forwarding, NAT, and asymmetric routing.
- [ ] Explain DNS resolution paths, search domains, caching, split DNS, resolver configuration, and service discovery.
- [ ] Compare NetworkManager/nmcli, Netplan, systemd-networkd, and distribution-specific network configuration; avoid assuming one control plane everywhere.
- [ ] Understand firewall concepts and packet flow; distinguish nftables, firewalld, and UFW interfaces, plus legacy iptables compatibility.
- [ ] Understand bridges, VLANs, bonding/teaming, virtual interfaces, tunnels, and overlay networks (P1).
- [ ] Explain network namespaces, veth pairs, container networking, and host/container port publishing.
- [ ] Use packet capture and connection tests thoughtfully; understand capture scope, permissions, privacy, and production impact.
- [ ] Diagnose with layered, hypothesis-driven checks; correlate DNS, routing, firewall, socket, TLS, and application health.
- [ ] Understand time synchronization (chrony/NTP), clock drift, certificates, and distributed-system consequences (S).

## 8. Security, compliance, and patching — P0/P1

- [ ] Apply least privilege, defense in depth, secure defaults, attack-surface reduction, and threat modeling to hosts and images.
- [ ] Understand discretionary access control (DAC), mandatory access control (MAC), Linux Security Modules, and how SELinux and AppArmor enforce policy.
- [ ] Distinguish SELinux modes, labels, policy, and audit denials from ordinary file permissions; distinguish AppArmor profiles and enforcement modes.
- [ ] Learn Linux capabilities and their relationship to root privilege; understand why broad capabilities can undermine isolation.
- [ ] Understand seccomp, namespaces, cgroups, syscall filtering, and host/container boundary limitations.
- [ ] Secure boot and update lifecycle conceptually: signed packages, repository trust, kernel updates, reboot planning, live-patching constraints, and rollback strategy.
- [ ] Understand vulnerability and configuration management, supported release windows, emergency patching, and staged validation.
- [ ] Learn audit records and system logging, auditd concepts, time integrity, retention, and centralized tamper-resistant log collection (P1).
- [ ] Protect secrets, private keys, credentials, and certificates using managed secret stores, access control, rotation, and redaction.
- [ ] Understand TLS certificate chains, key permissions, expiry, trust stores, and service renewal; avoid exposing private key material.
- [ ] Use security baselines such as CIS or applicable organizational/regulatory baselines as review inputs, not blindly applied scripts.
- [ ] Understand host firewalls, SSH policy, disk encryption, secure boot, identity integration, and audit requirements in context.
- [ ] Treat security controls as observable and testable; verify that hardening does not silently break service health.

## 9. Containers and virtualization foundations — P0/P1

- [ ] Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.
- [ ] Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.
- [ ] Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.
- [ ] Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.
- [ ] Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.
- [ ] Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.
- [ ] Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.
- [ ] Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.
- [ ] Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).

## 10. Cloud operations, configuration management, and immutable systems — P0/P1

- [ ] Understand cloud-init stages, datasource/metadata, user data, instance identity, first-boot behavior, and cloud-image customization.
- [ ] Keep bootstrap configuration idempotent and safe to rerun; handle secrets and metadata-service access deliberately.
- [ ] Compare imperative administration with declarative configuration management; understand desired state, drift detection, inventory, and convergence.
- [ ] Use reviewed configuration changes, version control, staged rollout, canaries, health checks, and rollback.
- [ ] Understand immutable image workflows, golden images, image pipelines, signed/provenance-aware artifacts, and replacement rather than ad hoc repair.
- [ ] Distinguish mutable host administration from container/image and fleet management; know when each pattern is appropriate.
- [ ] Understand fleet identity, centralized logging/metrics, patch orchestration, access lifecycle, and configuration ownership.
- [ ] Plan for cloud-specific device naming, transient disks, metadata, network interfaces, and provider-managed agents.

## 11. Reliability, high availability, and capacity — P1/P2

- [ ] Relate Linux host availability to application dependencies, failure domains, redundancy, health checks, and graceful degradation.
- [ ] Understand HA primitives: service supervision, load balancing, failover, fencing, quorum, VIP/VRRP, and cluster membership.
- [ ] Compare active-active and active-passive designs; account for split brain, state replication, and recovery behavior.
- [ ] Design capacity around CPU, memory, I/O, network, file descriptors, connection tracking, disk growth, and workload peaks.
- [ ] Use measured utilization, headroom, growth forecasts, and load tests to plan scaling; distinguish average from tail demand.
- [ ] Understand kernel and service resource limits, noisy neighbors, NUMA, cgroup controls, and cloud instance sizing.
- [ ] Define RTO/RPO, backup/restore procedures, multi-zone/region strategy, and disaster-recovery exercises.
- [ ] Document lifecycle and support choices: LTS/vendor support, kernel cadence, upgrade windows, package repositories, and compatibility.
- [ ] Treat tuning as a hypothesis-driven change with baseline, measurable outcome, bounded blast radius, and rollback.

## 12. Incident response and operational readiness — P0/P1

- [ ] Use a consistent triage loop: establish impact and scope; check recent changes; preserve evidence; gather host, service, and dependency signals; form and test hypotheses.
- [ ] Prioritize reversible, low-risk diagnostic actions before remediation; communicate impact, owners, timeline, and uncertainty.
- [ ] Investigate service down, boot failure, disk full, inode exhaustion, memory pressure, CPU saturation, I/O latency, DNS, routing, certificate expiry, and permission failures.
- [ ] Correlate journal/syslog, application logs, metrics, audit records, kernel messages, cloud events, and deployment history.
- [ ] Understand containment, safe recovery, escalation, and when not to restart or kill processes before evidence is captured.
- [ ] Maintain runbooks with preconditions, expected output, privilege requirements, impact warnings, verification, and rollback.
- [ ] Conduct blameless post-incident reviews; turn contributing factors into tests, automation, observability, and design changes (S).
- [ ] Practice incident handoffs and communicate operational risks to engineering and architecture stakeholders.

## Distro-specific operating differences

| Area | RHEL family | Debian / Ubuntu | Operational note |
|---|---|---|---|
| Packages | RPM; DNF (older systems may expose YUM) | DEB; APT and dpkg | Repository trust, package names, lifecycle, and update workflow differ. |
| Network management | Commonly NetworkManager; tools/config vary by release | NetworkManager, Netplan, or systemd-networkd depending on image/release | Identify the active renderer/control plane before changing configuration. |
| Security MAC | SELinux is a central platform feature and commonly enforcing | AppArmor commonly enabled by default | Learn both; do not disable policy to mask a denial. |
| Firewall administration | firewalld is common; nftables backend varies | UFW is common on Ubuntu; nftables is the kernel framework | Understand packet flow and active ruleset rather than assuming a frontend. |
| Logging / service management | systemd and journald commonly used | systemd and journald commonly used | Unit packaging, defaults, paths, and vendor policies still differ. |
| Enterprise lifecycle | RHEL subscriptions/support and major-version policy | Ubuntu LTS/Pro support and interim/LTS policy | Select based on support commitments, certification, workload, and upgrade policy. |

This table is a starting point, not a guarantee for every release or derivative. Verify the installed system's release notes and configuration.

## Role-based learning tracks

### DevOps engineer

- [ ] Prioritize shell scripting, Git, package/repository operations, systemd, SSH, cloud-init, image building, and configuration management.
- [ ] Automate provisioning and patching with idempotence, review, tests, secrets handling, and rollback.
- [ ] Understand container host fundamentals, cgroups/namespaces, image provenance, service health checks, and deployment lifecycle.
- [ ] Build runbooks and CI checks for Linux configuration, image baselines, and operational readiness.
- [ ] Capstone: create a disposable Linux VM/image, provision a least-privilege service account and systemd-managed sample service, apply a versioned configuration, emit useful logs/metrics, and demonstrate safe upgrade and rollback.

### Site reliability engineer (SRE)

- [ ] Prioritize Linux performance diagnosis, observability, networking, storage failure modes, systemd recovery, cgroups, and incident response.
- [ ] Relate host-level signals to user-visible symptoms, SLOs, error budgets, capacity forecasts, and alert quality.
- [ ] Practice evidence preservation, timelines, mitigations, safe recovery, and blameless learning.
- [ ] Design and test backup/restore, HA, failure injection in an isolated lab, and operational runbooks.
- [ ] Capstone: diagnose a deliberately constrained or misconfigured lab service from symptoms and telemetry; document evidence, root cause, risk-controlled mitigation, recovery verification, and follow-up actions.

### Linux / platform architect

- [ ] Prioritize distro and lifecycle selection, fleet architecture, security boundaries, identity, storage tiers, network design, HA/DR, and capacity.
- [ ] Evaluate tradeoffs across cloud images, kernel support, compliance, workload isolation, patching cadence, immutable operations, and vendor support.
- [ ] Define standards for host baselines, observability, access, secrets, image provenance, configuration ownership, and exception handling.
- [ ] Model failure domains and recovery objectives; validate assumptions through workload tests and restore/DR exercises.
- [ ] Capstone: produce a Linux platform design for a stated workload, including distro/support rationale, image and patch strategy, identity and security controls, storage/network layout, observability, capacity assumptions, HA/DR, threat/failure analysis, and an operational acceptance checklist.

## Safe lab and readiness plan

### Lab setup and safety

- [ ] Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.
- [ ] Keep a verified recovery route (console/snapshot/known-good image), and document how to restore before testing boot, network, storage, or security changes.
- [ ] Begin with read-only inspection. Never experiment on production or on a device containing needed data.
- [ ] Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.
- [ ] Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.
- [ ] Record baseline, change, verification, and rollback results for each exercise.

### Suggested progression

1. **Foundation:** explain boot, package management, file permissions, users, SSH, shell pipelines, and systemd service state on two different distro families.
2. **Operations:** use a lab service to practice logs, timers, limits, networking diagnosis, storage inspection, and a tested backup/restore.
3. **Reliability:** simulate a bounded failure in a disposable environment and write an evidence-based incident report and runbook.
4. **Role capstone:** complete the applicable DevOps, SRE, or Architect track above, then have another practitioner review safety, reproducibility, and recovery steps.

### Readiness checklist

- [ ] Explain the likely cause and next safe observation for a boot, permissions, DNS, disk, memory, or service failure without relying on a memorized fix.
- [ ] Identify which details are distro/release-specific and find authoritative local documentation.
- [ ] Make a reviewed, reversible change and verify both intended effect and absence of regressions.
- [ ] Restore data or service from a tested recovery path and state its measured RTO/RPO.
- [ ] Communicate impact, evidence, confidence, risk, and next steps clearly.
- [ ] Demonstrate automation or design that is repeatable, observable, least-privileged, and maintainable.

## Official references

Use these primary references for deeper study. Online documentation evolves; consult release-specific manuals and vendor documentation for systems you operate. Accessed 2026-10-04.

1. Linux kernel documentation, including user/admin guides, kernel interfaces, filesystems, networking, and cgroup v2: [docs.kernel.org](https://docs.kernel.org/) · [Kernel administrator's guide](https://docs.kernel.org/admin-guide/) · [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) · [kernel sysctl documentation](https://docs.kernel.org/admin-guide/sysctl/)
2. Linux man-pages project: [kernel.org man-pages project](https://www.kernel.org/doc/man-pages/) · [online man-pages index](https://www.man7.org/linux/man-pages/)
3. systemd project manuals: [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/)
4. Red Hat Enterprise Linux 9 documentation: [RHEL documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Managing storage devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/) · [Monitoring and managing system status and performance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/) · [Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
5. Canonical Ubuntu Server documentation: [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [security how-to guides](https://canonical-ubuntu-server-documentation.readthedocs-hosted.com/how-to/security/) · [software management tutorial](https://canonical-ubuntu-server-documentation.readthedocs-hosted.com/tutorial/managing-software/)
