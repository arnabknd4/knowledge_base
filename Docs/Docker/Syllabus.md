# Docker + DCA: Topic List (Architect Level)

**Legend:** 🟥 Required | 🟨 Optional | 🎯 Exam-oriented | 🛠️ Real-life use

**Exam domains and weights:** Orchestration 25% · Image Creation/Management/Registry 20% · Installation/Configuration 15% · Networking 15% · Security 15% · Storage/Volumes 10%

**Product renames:** UCP is now Mirantis Kubernetes Engine (MKE); DTR is now Mirantis Secure Registry (MSR). The official study guide has not caught up yet. Check the official Mirantis exam page for the current format, duration, and pass mark, since third-party sources disagree.

---

## 0. Foundations (prerequisite to all domains)
| Topic | Flag |
|---|---|
| Container vs VM | 🟥 🎯 🛠️ |
| Docker architecture (client, daemon, containerd, runc) | 🟥 🎯 |
| Images, layers, copy-on-write | 🟥 🎯 🛠️ |
| Container lifecycle and core CLI | 🟥 🎯 🛠️ |
| Namespaces and cgroups | 🟥 🎯 |
| OCI standards | 🟨 |
| Docker Desktop vs Docker Engine | 🟨 🛠️ |

## 1. Image Creation, Management & Registry (20%)
| Topic | Flag |
|---|---|
| Dockerfile instructions (CMD vs ENTRYPOINT, COPY vs ADD, ENV vs ARG, USER, HEALTHCHECK) | 🟥 🎯 🛠️ |
| Layer caching and build optimization | 🟥 🎯 🛠️ |
| Multi-stage builds | 🟥 🎯 🛠️ |
| Tagging, digests, versioning strategy | 🟥 🎯 🛠️ |
| Inspecting and cleaning images (history, inspect, prune) | 🟥 🎯 🛠️ |
| Docker Hub and private registries (login, push, pull) | 🟥 🎯 🛠️ |
| MSR (formerly DTR): RBAC, scanning, promotion, mirroring, immutable tags | 🟥 🎯 🛠️ |
| Image vulnerability scanning | 🟥 🎯 🛠️ |
| Base image choice (alpine, distroless, scratch) | 🟨 🛠️ |
| .dockerignore | 🟨 🛠️ |
| BuildKit / buildx | 🟨 🛠️ |

## 2. Orchestration (25%)
| Topic | Flag |
|---|---|
| Swarm architecture (managers, workers, Raft) | 🟥 🎯 🛠️ |
| Quorum and manager fault tolerance (odd counts: 3, 5, 7) | 🟥 🎯 🛠️ |
| Swarm init/join, tokens, node states (active, pause, drain), labels | 🟥 🎯 🛠️ |
| Services: replicated vs global | 🟥 🎯 🛠️ |
| Placement: constraints, preferences, resource limits | 🟥 🎯 🛠️ |
| Rolling updates and rollback | 🟥 🎯 🛠️ |
| Health checks and restart policies | 🟥 🎯 🛠️ |
| Stacks and Compose files (`deploy` key) | 🟥 🎯 🛠️ |
| Docker Compose (local dev) | 🟥 🎯 🛠️ |
| Swarm secrets and configs | 🟥 🎯 🛠️ |
| Swarm backup, restore, autolock, force-new-cluster | 🟥 🎯 🛠️ |
| Kubernetes basics: Pod, ReplicaSet, Deployment, Service types, Namespace | 🟥 🎯 🛠️ |
| Kubernetes config and storage: ConfigMap, Secret, PV/PVC, probes, `kubectl` basics | 🟥 🎯 🛠️ |
| MKE (formerly UCP): role, deploying workloads | 🟥 🎯 🛠️ |
| Ingress / Layer 7 routing (Interlock) | 🟨 🎯 |

## 3. Installation & Configuration (15%)
| Topic | Flag |
|---|---|
| Installing Docker Engine (supported OS, post-install steps) | 🟥 🎯 🛠️ |
| `daemon.json` (data-root, storage driver, logging, mirrors, insecure registries, live-restore) | 🟥 🎯 🛠️ |
| Logging drivers (json-file, syslog, journald, fluentd, gelf) | 🟥 🎯 🛠️ |
| Resource limits (CPU, memory, OOM behaviour) | 🟥 🎯 🛠️ |
| Enterprise components and sizing (MKE managers, MSR replicas) | 🟥 🎯 🛠️ |
| Remote daemon access (TLS, `DOCKER_HOST`, contexts) | 🟥 🎯 🛠️ |
| Troubleshooting (`info`, `events`, `logs`, `stats`, `system df`, daemon logs) | 🟥 🎯 🛠️ |
| Upgrades (engine and cluster) | 🟨 🎯 🛠️ |
| Backup and restore of MKE / MSR | 🟨 🎯 🛠️ |
| Capacity planning | 🟨 🛠️ |

## 4. Networking (15%)
| Topic | Flag |
|---|---|
| Network drivers (bridge, host, none, overlay, macvlan) | 🟥 🎯 🛠️ |
| Default bridge vs user-defined bridge | 🟥 🎯 🛠️ |
| Overlay networks, VXLAN, required ports (2377, 7946, 4789) | 🟥 🎯 🛠️ |
| Service discovery and embedded DNS | 🟥 🎯 🛠️ |
| Port publishing (ingress vs host mode), EXPOSE | 🟥 🎯 🛠️ |
| Routing mesh and load balancing (VIP vs DNSRR) | 🟥 🎯 🛠️ |
| Encrypted overlay networks | 🟥 🎯 |
| Network troubleshooting (`network inspect`, netshoot) | 🟨 🎯 🛠️ |
| Kubernetes networking basics (Service types, Ingress, CNI) | 🟨 🎯 |
| ipvlan | 🟨 |

## 5. Security (15%)
| Topic | Flag |
|---|---|
| Docker attack surface (daemon socket, privileges) | 🟥 🎯 🛠️ |
| Capabilities, seccomp, AppArmor/SELinux | 🟥 🎯 🛠️ |
| Non-root containers, rootless mode, userns-remap | 🟥 🎯 🛠️ |
| Secrets handling (never in ENV or images) | 🟥 🎯 🛠️ |
| Docker Content Trust (image signing) | 🟥 🎯 🛠️ |
| Mutual TLS in Swarm and daemon TLS | 🟥 🎯 |
| RBAC in MKE (subjects, roles, collections, grants) | 🟥 🎯 🛠️ |
| Swarm autolock | 🟥 🎯 |
| Read-only root filesystem, `no-new-privileges`, dangers of `--privileged` | 🟥 🎯 🛠️ |
| Image scanning and CVE workflow | 🟥 🎯 🛠️ |
| LDAP/SAML/SSO integration in MKE | 🟨 🎯 |
| CIS Docker Benchmark and Docker Bench | 🟨 🛠️ |
| SBOM and provenance | 🟨 🛠️ |

## 6. Storage & Volumes (10%)
| Topic | Flag |
|---|---|
| Volumes vs bind mounts vs tmpfs | 🟥 🎯 🛠️ |
| Named vs anonymous volumes, volume commands | 🟥 🎯 🛠️ |
| Storage drivers (overlay2) and the writable layer | 🟥 🎯 |
| Persistence in Swarm (node-local volumes, NFS, volume plugins) | 🟥 🎯 🛠️ |
| Kubernetes PV, PVC, StorageClass | 🟥 🎯 🛠️ |
| Disk cleanup (`prune`, `system df`) | 🟥 🎯 🛠️ |
| Volume drivers and plugins | 🟨 🎯 |
| Volume backup and restore | 🟨 🛠️ |

## 7. Architect Design Layer (beyond exam objectives, essential for the role)
| Topic | Flag |
|---|---|
| Swarm vs Kubernetes decision criteria | 🟥 🎯 🛠️ |
| HA and DR design (manager placement across failure domains, quorum) | 🟥 🎯 🛠️ |
| Migrating legacy apps to containers (12-factor, stateless vs stateful) | 🟥 🎯 🛠️ |
| CI/CD supply chain (build → scan → sign → promote) | 🟥 🛠️ |
| Registry strategy (mirroring, promotion, retention) | 🟥 🛠️ |
| Observability (logs, metrics, alerts) | 🟥 🛠️ |
| Multi-tenancy and isolation design | 🟨 🛠️ |
| Container vs VM vs serverless trade-offs | 🟨 🛠️ |
| Cost and capacity planning | 🟨 🛠️ |

---

## Safe to Skip (low value for DCA or real-life today)
- Docker Machine, Docker Cloud, legacy `docker-compose` v1 specifics
- Devicemapper deep-dive and other legacy storage drivers
- Advanced Kubernetes (operators, CRDs, Helm, service mesh)
- Notary internals, Docker Desktop extensions
- Windows container deep-dive (unless your role needs it)

## Suggested Study Order
1. Section 0 → Section 1 (images and Dockerfile first)
2. Sections 4 and 6 (networking and storage make Swarm easier)
3. Section 2 (the largest domain, so spend the most time here)
4. Sections 3 and 5 together, then Section 7 for architect thinking