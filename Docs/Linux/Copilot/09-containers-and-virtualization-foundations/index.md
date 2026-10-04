# 09. Containers and virtualization foundations

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Virtualization and containers

- [Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.](01-virtualization-and-containers/001-understand-virtual-machines-hypervisors-kvm-guest-kernels-images/study-guide.md)
- [Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.](01-virtualization-and-containers/002-explain-namespaces-for-pid-mount-network-user-uts-and-ipc-isolat/study-guide.md)
- [Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.](01-virtualization-and-containers/003-explain-cgroups-v1-versus-v2-at-a-conceptual-and-operational-lev/study-guide.md)
- [Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.](01-virtualization-and-containers/004-understand-container-image-layers-registries-overlay-filesystems/study-guide.md)
- [Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.](01-virtualization-and-containers/005-distinguish-containerd-cri-o-runc-and-higher-level-orchestration/study-guide.md)
- [Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.](01-virtualization-and-containers/006-inspect-the-relationship-between-systemd-cgroups-container-runti/study-guide.md)
- [Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.](01-virtualization-and-containers/007-understand-container-capabilities-seccomp-lsm-integration-user-n/study-guide.md)
- [Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.](01-virtualization-and-containers/008-know-when-a-workload-requires-a-vm-or-stronger-isolation-boundar/study-guide.md)
- [Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).](01-virtualization-and-containers/009-investigate-host-level-causes-of-container-failures-disk-pressur/study-guide.md)

## Domain scope

This is domain `09` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
