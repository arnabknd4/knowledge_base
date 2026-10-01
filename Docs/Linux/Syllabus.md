# Linux Prerequisites for DevOps / SRE / Cloud Architect (Architect Level)

**Legend:** **R** = Required | **O** = Optional | **E** = Exam oriented | **L** = Real-life use

---

## 1. Fundamentals

| Topic | Flags |
|---|---|
| Linux architecture (kernel, user space, shell) | R, E |
| Distributions (RHEL/CentOS/Rocky, Ubuntu/Debian, Amazon Linux, Alpine) | R, E, L |
| Package managers (apt, dnf/yum, rpm, dpkg) | R, E, L |
| Kernel vs distro vs init | R, E |
| Boot process (BIOS/UEFI, GRUB, kernel, init) | R, E |
| systemd (units, targets, services, timers) | R, E, L |
| Runlevels / SysV init | O, E |
| Kernel modules | O, E |
| Kernel parameters (sysctl) | R, L |

## 2. Filesystem & Storage

| Topic | Flags |
|---|---|
| Filesystem Hierarchy Standard (/etc, /var, /proc, /sys, /dev) | R, E, L |
| Inodes, hard links, soft links | R, E |
| File types and permissions (rwx, octal) | R, E, L |
| Special permissions (SUID, SGID, sticky bit) | R, E |
| ACLs | O, E |
| umask | R, E |
| Filesystem types (ext4, xfs, btrfs, tmpfs) | R, E, L |
| Mounting (fstab, mount, umount) | R, E, L |
| Disk partitioning (fdisk, parted, MBR vs GPT) | R, E |
| LVM (PV, VG, LV, resize, snapshots) | R, E, L |
| RAID levels | R, E |
| Disk quotas | O, E |
| Swap | R, L |
| Block vs object vs file storage concepts | R, L |
| NFS / iSCSI | O, L |
| Disk usage tools (df, du, lsblk, iostat) | R, L |

## 3. Users, Groups & Access

| Topic | Flags |
|---|---|
| User and group management | R, E, L |
| /etc/passwd, /etc/shadow, /etc/group | R, E |
| sudo and sudoers | R, E, L |
| PAM | O, E |
| SSH (keys, config, agent, tunnelling, hardening) | R, E, L |
| su vs sudo | R, E |
| Password policies / account aging | O, E |
| LDAP / SSSD / Kerberos integration | O, L |

## 4. Processes & Services

| Topic | Flags |
|---|---|
| Process lifecycle (fork, exec, states, zombie/orphan) | R, E, L |
| Signals (SIGTERM, SIGKILL, SIGHUP) | R, E, L |
| Process tools (ps, top, htop, kill, nice, renice) | R, L |
| Foreground/background jobs, nohup | R |
| Daemons and services | R, E |
| Cron and at | R, E, L |
| systemd timers | R, L |
| Scheduling and priorities | O, E |
| Core dumps | O, L |

## 5. Memory & Performance

| Topic | Flags |
|---|---|
| Virtual memory, page cache, OOM killer | R, E, L |
| Load average and CPU states | R, L |
| Performance tools (vmstat, iostat, sar, free, perf, strace, lsof) | R, L |
| /proc and /sys inspection | R, L |
| Tuning (sysctl, ulimit, tuned) | R, L |
| Bottleneck analysis (CPU, memory, I/O, network) | R, L |
| eBPF basics | O, L |

## 6. Networking

| Topic | Flags |
|---|---|
| TCP/IP stack on Linux | R, E |
| Interface config (ip, ifconfig, nmcli, netplan) | R, E, L |
| Routing tables and static routes | R, E, L |
| DNS (resolv.conf, systemd-resolved, dig, nslookup) | R, E, L |
| Ports and sockets (ss, netstat, lsof) | R, L |
| Firewalls (iptables, nftables, firewalld, ufw) | R, E, L |
| NAT and IP forwarding | R, E |
| Bridges, VLANs, bonding | O, E |
| Network namespaces | R, L |
| Packet capture (tcpdump, wireshark) | R, L |
| Connectivity tools (curl, wget, ping, traceroute, mtr, nc) | R, L |
| Time sync (NTP, chrony) | R, L |

## 7. Shell & Text Processing

| Topic | Flags |
|---|---|
| Bash basics (variables, quoting, redirection, pipes) | R, E, L |
| Core commands (ls, cp, mv, find, grep, xargs) | R, E, L |
| Text tools (sed, awk, cut, sort, uniq, tr) | R, E, L |
| Regular expressions | R, E, L |
| Environment variables and shell startup files | R, E |
| Aliases and shell config | O |
| Editors (vi/vim, nano) | R, E, L |
| Archiving and compression (tar, gzip, zip, rsync) | R, E, L |
| I/O redirection and file descriptors | R, E |

## 8. Security & Hardening

| Topic | Flags |
|---|---|
| SELinux / AppArmor | R, E, L |
| File integrity and permissions audit | R, L |
| Auditing (auditd) | O, E, L |
| Hardening (CIS benchmarks) | R, L |
| Patch management | R, L |
| Secrets and key handling | R, L |
| TLS/certs on Linux (openssl) | R, L |
| Seccomp | O, L |
| Capabilities (Linux capabilities) | R, L |
| Fail2ban / intrusion basics | O, L |

## 9. Logging & Monitoring

| Topic | Flags |
|---|---|
| Logging (/var/log, rsyslog, journald, journalctl) | R, E, L |
| Log rotation (logrotate) | R, E, L |
| Metrics basics (CPU, memory, disk, network) | R, L |
| Monitoring agents (node_exporter, collectd) | O, L |
| Central logging concepts | R, L |

## 10. Containers & Virtualization Foundations

| Topic | Flags |
|---|---|
| Namespaces (PID, net, mount, user, UTS, IPC) | R, E, L |
| cgroups (v1 vs v2) | R, E, L |
| chroot | O, E |
| Union/overlay filesystems | R, L |
| Virtualization (KVM, hypervisor types) | R, E |
| Linux bridge / veth pairs | R, L |
| Container runtime basics (containerd, runc) | O, L |

## 11. Automation & Operations

| Topic | Flags |
|---|---|
| Shell scripting (conditionals, loops, functions, exit codes) | R, E, L |
| Script debugging and error handling | R, L |
| Git on Linux | R, L |
| Package/repo management (custom repos, mirrors) | R, L |
| Backup and restore (rsync, tar, snapshots) | R, E, L |
| Disaster recovery and rescue mode | R, E, L |
| Configuration management concepts (idempotency, drift) | R, L |
| Immutable infrastructure vs mutable servers | R, L |
| Cloud-init / user data | R, L |

## 12. Architect-Level Concepts

| Topic | Flags |
|---|---|
| Capacity planning and sizing | R, L |
| High availability (keepalived, pacemaker, VRRP) | O, E, L |
| Load balancing concepts (HAProxy, nginx, LVS) | R, L |
| Clustering and quorum | O, E |
| Linux in cloud (EC2/Azure VM/GCP image choices, AMI hardening) | R, L |
| Kernel tuning for high-throughput workloads | O, L |
| Compliance and baselines (CIS, STIG) | R, L |
| Troubleshooting methodology | R, L |
| Choosing distro/LTS strategy | R, L |

---

## Suggested Priority (Architect Level)

1. Processes and systemd
2. Networking
3. Storage / LVM
4. Security (SELinux, SSH, capabilities)
5. Namespaces / cgroups
6. Performance troubleshooting
7. Scripting

> Topics flagged **R + L** together are the ones used daily on the job.