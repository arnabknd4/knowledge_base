# 06. Storage, filesystems, and data protection

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Storage and recovery

- [Distinguish block, file, and object storage; understand local ephemeral disks versus persistent and network-backed cloud volumes.](01-storage-and-recovery/001-distinguish-block-file-and-object-storage-understand-local-ephem/study-guide.md)
- [Trace storage layers: device, partition table, RAID, encryption, LVM or pool management, filesystem, mount, and application data path.](01-storage-and-recovery/002-trace-storage-layers-device-partition-table-raid-encryption-lvm/study-guide.md)
- [Understand GPT/partition concepts; inspect block devices and capacity without modifying them.](01-storage-and-recovery/003-understand-gpt-partition-concepts-inspect-block-devices-and-capa/study-guide.md)
- [Compare ext4, XFS, Btrfs, tmpfs, and network filesystems by operational characteristics and distribution support.](01-storage-and-recovery/004-compare-ext4-xfs-btrfs-tmpfs-and-network-filesystems-by-operatio/study-guide.md)
- [Understand mount points, mount namespaces, mount options, `/etc/fstab`, UUIDs, automounting, and failure behavior at boot.](01-storage-and-recovery/005-understand-mount-points-mount-namespaces-mount-options-etc-fstab/study-guide.md)
- [Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.](01-storage-and-recovery/006-explain-lvm-pv-vg-lv-concepts-allocation-growth-snapshots-and-th/study-guide.md)
- [Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.](01-storage-and-recovery/007-understand-raid-levels-software-raid-hardware-raid-rebuild-risk/study-guide.md)
- [Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.](01-storage-and-recovery/008-understand-swap-purpose-and-behavior-use-workload-and-memory-evi/study-guide.md)
- [Learn filesystem capacity versus inode exhaustion, reserved blocks, deleted-but-open files, quotas, and storage latency (P1).](01-storage-and-recovery/009-learn-filesystem-capacity-versus-inode-exhaustion-reserved-block/study-guide.md)
- [Understand NFS and iSCSI fundamentals; recognize permissions, identity mapping, network dependency, locking, and failure-mode concerns (P1).](01-storage-and-recovery/010-understand-nfs-and-iscsi-fundamentals-recognize-permissions-iden/study-guide.md)
- [Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.](01-storage-and-recovery/011-plan-backups-around-recovery-point-and-recovery-time-objectives/study-guide.md)
- [Compare snapshots, replication, backups, and disaster recovery; test application consistency and recovery ordering.](01-storage-and-recovery/012-compare-snapshots-replication-backups-and-disaster-recovery-test/study-guide.md)
- [Evaluate cloud block and object storage durability, performance, access control, lifecycle, and failure domains (A).](01-storage-and-recovery/013-evaluate-cloud-block-and-object-storage-durability-performance-a/study-guide.md)

## Domain scope

This is domain `06` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
