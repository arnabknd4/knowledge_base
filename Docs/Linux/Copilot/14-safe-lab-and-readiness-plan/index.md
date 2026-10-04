# 14. Safe lab and readiness plan

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Lab setup and safety

- [Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.](01-lab-setup-and-safety/001-use-disposable-vms-snapshots-or-isolated-cloud-accounts-with-no/study-guide.md)
- [Keep a verified recovery route (console/snapshot/known-good image), and document how to restore before testing boot, network, storage, or security changes.](01-lab-setup-and-safety/002-keep-a-verified-recovery-route-console-snapshot-known-good-image/study-guide.md)
- [Begin with read-only inspection. Never experiment on production or on a device containing needed data.](01-lab-setup-and-safety/003-begin-with-read-only-inspection-never-experiment-on-production-o/study-guide.md)
- [Treat partitioning, formatting, filesystem repair, LVM/RAID changes, firewall/network changes, recursive permission changes, SELinux/AppArmor policy edits, kernel parameters, and reboot operations as **lab-only unless separately approved through a production change process**.](01-lab-setup-and-safety/004-treat-partitioning-formatting-filesystem-repair-lvm-raid-changes/study-guide.md)
- [Confirm target devices, mount points, access paths, impact, backup, and rollback before any destructive or disruptive test. Do not paste commands from a syllabus into a privileged shell.](01-lab-setup-and-safety/005-confirm-target-devices-mount-points-access-paths-impact-backup-a/study-guide.md)
- [Record baseline, change, verification, and rollback results for each exercise.](01-lab-setup-and-safety/006-record-baseline-change-verification-and-rollback-results-for-eac/study-guide.md)

## Readiness checklist

- [Explain the likely cause and next safe observation for a boot, permissions, DNS, disk, memory, or service failure without relying on a memorized fix.](02-readiness-checklist/007-explain-the-likely-cause-and-next-safe-observation-for-a-boot-pe/study-guide.md)
- [Identify which details are distro/release-specific and find authoritative local documentation.](02-readiness-checklist/008-identify-which-details-are-distro-release-specific-and-find-auth/study-guide.md)
- [Make a reviewed, reversible change and verify both intended effect and absence of regressions.](02-readiness-checklist/009-make-a-reviewed-reversible-change-and-verify-both-intended-effec/study-guide.md)
- [Restore data or service from a tested recovery path and state its measured RTO/RPO.](02-readiness-checklist/010-restore-data-or-service-from-a-tested-recovery-path-and-state-it/study-guide.md)
- [Communicate impact, evidence, confidence, risk, and next steps clearly.](02-readiness-checklist/011-communicate-impact-evidence-confidence-risk-and-next-steps-clear/study-guide.md)
- [Demonstrate automation or design that is repeatable, observable, least-privileged, and maintainable.](02-readiness-checklist/012-demonstrate-automation-or-design-that-is-repeatable-observable-l/study-guide.md)

## Domain scope

This is domain `14` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
