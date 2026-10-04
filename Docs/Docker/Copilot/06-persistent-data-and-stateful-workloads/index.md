# Domain 6 — Persistent data and stateful workloads

Objective-level study guides for Docker storage primitives, data lifecycle, and stateful service architecture.

## Guides

### Storage primitives

- [Explain the container writable layer and why it is not durable application storage](storage-primitives/writable-layer/study-guide.md)
- [Choose named volumes, anonymous volumes, bind mounts, tmpfs, or other supported mounts based on persistence, portability, performance, and access needs](storage-primitives/mount-type-selection/study-guide.md)
- [Create, inspect, back up, restore, and safely remove volumes](storage-primitives/volume-lifecycle/study-guide.md)
- [Understand volume ownership/permissions, mount propagation, host-path coupling, and data lifecycle](storage-primitives/volume-permissions-lifecycle/study-guide.md)
- [Distinguish Docker's container-data mounts from the daemon's image/layer storage backend](storage-primitives/data-mounts-vs-daemon-storage/study-guide.md)
### Stateful service design

- [Externalize durable state and design database lifecycle independently from application-container lifecycle](stateful-service-design/externalize-state/study-guide.md)
- [Understand that a local Docker volume is generally host-local; it is not automatically replicated or highly available](stateful-service-design/local-volume-limits/study-guide.md)
- [Design backup consistency, restore testing, encryption, retention, and recovery objectives for persistent data](stateful-service-design/backup-restore-objectives/study-guide.md)
- [Avoid concurrent writers or unsafe sharing of filesystem-backed data unless the storage system and application explicitly support it](stateful-service-design/concurrent-writer-safety/study-guide.md)
- [Decide when to use a managed database/storage service rather than operating a stateful container](stateful-service-design/managed-vs-self-hosted-state/study-guide.md)

**Syllabus:** [Docker syllabus](../copilot-docker-syllabus.md)
