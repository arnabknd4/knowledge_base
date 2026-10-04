# Container Runtime And Host Operations

> Architect-focused guides for each checked objective.

- [Docker syllabus](../copilot-docker-syllabus.md)

## Runtime configuration and process behavior

- [Configure environment, command/entrypoint, working directory, exposed and published ports, restart behavior, and health checks.](runtime-configuration-and-process-behavior/configure-environment-command-entrypoint-working-directory-exposed-and-published/study-guide.md)
- [Understand that `EXPOSE` documents a container port; it does not publish a host port.](runtime-configuration-and-process-behavior/understand-that-expose-documents-a-container-port-it-does/study-guide.md)
- [Set CPU and memory constraints based on measured demand and host capacity; understand OOM behavior and resource contention.](runtime-configuration-and-process-behavior/set-cpu-and-memory-constraints-based-on-measured-demand/study-guide.md)
- [Configure PID limits, ulimits, shared memory, read-only root filesystems, and temporary writable paths where needed.](runtime-configuration-and-process-behavior/configure-pid-limits-ulimits-shared-memory-read-only-root/study-guide.md)
- [Send and handle termination signals correctly; implement graceful shutdown and readiness/liveness behavior in the application.](runtime-configuration-and-process-behavior/send-and-handle-termination-signals-correctly-implement-graceful-shutdown/study-guide.md)
- [Use logs, events, metrics, exit codes, and inspect output to diagnose runtime issues.](runtime-configuration-and-process-behavior/use-logs-events-metrics-exit-codes-and-inspect-output/study-guide.md)

## Docker Engine operations

- [Install and update Docker Engine/Desktop using current platform-specific guidance.](docker-engine-operations/install-and-update-docker-engine-desktop-using-current-platform/study-guide.md)
- [Manage daemon settings, data-root, logging driver, storage backend, proxies, registry mirrors, and live-restore behavior where appropriate.](docker-engine-operations/manage-daemon-settings-data-root-logging-driver-storage-backend/study-guide.md)
- [Understand how daemon configuration and system service settings interact; apply configuration through supported OS mechanisms.](docker-engine-operations/understand-how-daemon-configuration-and-system-service-settings-interact/study-guide.md)
- [Monitor host disk, memory, CPU, file descriptors, network, image cache, and container churn.](docker-engine-operations/monitor-host-disk-memory-cpu-file-descriptors-network-image/study-guide.md)
- [Configure log collection and rotation to prevent unbounded disk use.](docker-engine-operations/configure-log-collection-and-rotation-to-prevent-unbounded-disk/study-guide.md)
- [Manage engine upgrades, compatibility testing, maintenance windows, and rollback/recovery.](docker-engine-operations/manage-engine-upgrades-compatibility-testing-maintenance-windows-and-rollback/study-guide.md)

## Remote administration and troubleshooting

- [Use Docker contexts to select and name endpoints safely.](remote-administration-and-troubleshooting/use-docker-contexts-to-select-and-name-endpoints-safely/study-guide.md)
- [Secure any remote Engine API using authenticated TLS and network restrictions; never expose an unauthenticated daemon endpoint.](remote-administration-and-troubleshooting/secure-any-remote-engine-api-using-authenticated-tls-and/study-guide.md)
- [Understand the security impact of membership in the Docker group or access to the Engine socket.](remote-administration-and-troubleshooting/understand-the-security-impact-of-membership-in-the-docker/study-guide.md)
- [Troubleshoot daemon startup, image pull/build, container exit, health check, port, DNS, disk pressure, and resource-limit failures.](remote-administration-and-troubleshooting/troubleshoot-daemon-startup-image-pull-build-container-exit-health/study-guide.md)
- [Use platform logs and Docker diagnostics to distinguish host/kernel, daemon, network, image, and application failures.](remote-administration-and-troubleshooting/use-platform-logs-and-docker-diagnostics-to-distinguish-host/study-guide.md)
