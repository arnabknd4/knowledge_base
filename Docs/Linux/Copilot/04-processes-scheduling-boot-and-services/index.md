# 04. Processes, scheduling, boot, and services

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Processes and services

- [Explain process creation and lifecycle, PID/PPID, threads, process states, zombies, signals, sessions, and process groups.](01-processes-and-services/001-explain-process-creation-and-lifecycle-pid-ppid-threads-process/study-guide.md)
- [Inspect processes, open files, sockets, and resource limits; understand `ulimit`, PAM limits, and per-service limits.](01-processes-and-services/002-inspect-processes-open-files-sockets-and-resource-limits-underst/study-guide.md)
- [Distinguish graceful termination from forced termination and understand the operational consequences of each.](01-processes-and-services/003-distinguish-graceful-termination-from-forced-termination-and-und/study-guide.md)
- [Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).](01-processes-and-services/004-understand-cpu-scheduling-priorities-nice-affinity-real-time-sch/study-guide.md)
- [Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.](01-processes-and-services/005-compare-cron-at-style-scheduling-with-systemd-timers-account-for/study-guide.md)
- [Understand systemd units, dependencies, targets, service types, restart policies, environment files, drop-ins, sockets, timers, mounts, and generators.](01-processes-and-services/006-understand-systemd-units-dependencies-targets-service-types-rest/study-guide.md)
- [Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.](01-processes-and-services/007-read-service-state-and-journal-logs-correlate-boot-id-timestamps/study-guide.md)
- [Understand SysV init/runlevel compatibility as legacy context, not the default design assumption.](01-processes-and-services/008-understand-sysv-init-runlevel-compatibility-as-legacy-context-no/study-guide.md)
- [Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.](01-processes-and-services/009-diagnose-boot-failures-using-console-access-previous-boot-logs-r/study-guide.md)
- [Plan safe service changes, validation, rollback, and health checks before deployment (D, S).](01-processes-and-services/010-plan-safe-service-changes-validation-rollback-and-health-checks/study-guide.md)

## Domain scope

This is domain `04` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
