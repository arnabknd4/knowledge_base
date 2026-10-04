# 1. Container and Docker foundations

[Docker syllabus](../copilot-docker-syllabus.md)

Objective-level study guides, grouped by the exact topic headings in the syllabus.

## Container fundamentals

- [Explain containers as isolated processes that share the host operating-system kernel, and compare containers with virtual machines and managed/serverless runtimes.](./container-fundamentals/explain-containers-as-isolated-processes-that-share-the-host-operating/study-guide.md)
- [Understand images, containers, tags, digests, registries, layers, and the writable container layer.](./container-fundamentals/understand-images-containers-tags-digests-registries-layers-and-the/study-guide.md)
- [Explain Linux namespaces and cgroups at a practical level; understand OCI image/runtime standards and the roles of Docker Engine, containerd, and OCI runtimes.](./container-fundamentals/explain-linux-namespaces-and-cgroups-at-a-practical-level-understand/study-guide.md)
- [Distinguish an image (immutable template) from a running container (a process with runtime configuration and a writable layer).](./container-fundamentals/distinguish-an-image-immutable-template-from-a-running-container-a/study-guide.md)
- [Identify when Docker is a good fit and when a VM, managed platform, or function service is a better boundary.](./container-fundamentals/identify-when-docker-is-a-good-fit-and-when-a-vm-managed-platform-or/study-guide.md)

## Docker architecture and environments

- [Use the client/daemon model and understand that Docker CLI commands operate against a selected Docker context/daemon.](./docker-architecture-and-environments/use-the-client-daemon-model-and-understand-that-docker-cli-commands/study-guide.md)
- [Distinguish Docker Engine on Linux from Docker Desktop environments on Windows and macOS, including the Linux VM boundary where applicable.](./docker-architecture-and-environments/distinguish-docker-engine-on-linux-from-docker-desktop-environments-on/study-guide.md)
- [Inspect client/server versions, server configuration, storage, runtimes, and active context using `docker version`, `docker info`, and `docker context`.](./docker-architecture-and-environments/inspect-client-server-versions-server-configuration-storage-runtimes/study-guide.md)
- [Understand daemon privileges and why access to the Docker socket/API is highly privileged.](./docker-architecture-and-environments/understand-daemon-privileges-and-why-access-to-the-docker-socket-api-is/study-guide.md)
- [Know the differences among development workstation, CI builder, single-host runtime, and clustered/container-platform environments.](./docker-architecture-and-environments/know-the-differences-among-development-workstation-ci-builder-single/study-guide.md)

## Essential CLI and lifecycle

- [Pull, inspect, tag, run, stop, start, restart, remove, and list containers and images.](./essential-cli-and-lifecycle/pull-inspect-tag-run-stop-start-restart-remove-and-list-containers-and/study-guide.md)
- [Use `docker ps`, `docker logs`, `docker exec`, `docker inspect`, `docker events`, and `docker stats` to inspect running workloads.](./essential-cli-and-lifecycle/use-docker-ps-docker-logs-docker-exec-docker-inspect-docker-events-and/study-guide.md)
- [Understand foreground/background execution, exit codes, signals, entrypoint/command behavior, and restart policies.](./essential-cli-and-lifecycle/understand-foreground-background-execution-exit-codes-signals/study-guide.md)
- [Inspect resource consumption and determine whether an issue is in the application, container configuration, host, or daemon.](./essential-cli-and-lifecycle/inspect-resource-consumption-and-determine-whether-an-issue-is-in-the/study-guide.md)
- [Prune unused objects deliberately and understand the scope of each prune command.](./essential-cli-and-lifecycle/prune-unused-objects-deliberately-and-understand-the-scope-of-each/study-guide.md)
