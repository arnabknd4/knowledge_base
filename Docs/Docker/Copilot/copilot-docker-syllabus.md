# Docker Real-World Skills Syllabus

This role-oriented syllabus covers Docker knowledge used in real software delivery and operations, from development through production platform design. It is organized around practical capability domains rather than an exam blueprint. Docker's product documentation is the primary reference; no exam weights or pass guarantees are implied.

> - **Target roles:** DevOps engineer, platform engineer, site reliability engineer (SRE), cloud/container architect, application developer, and security engineer
> - **Target level:** Hands-on practitioner through architect
> - **Scope:** Docker Engine, Docker CLI, Docker Desktop, Dockerfile/BuildKit, Docker Compose, registries, image supply chain, runtime, networking, storage, and production operations
> - **Not a replacement for:** Kubernetes, cloud-provider, operating-system, or organization-specific security training

## How to use this syllabus

- **Core** skills are useful to every target role.
- **DevOps / Platform / SRE** skills emphasize automation, operations, repeatability, and production reliability.
- **Architect** skills emphasize system boundaries, platform choices, failure domains, security, and lifecycle trade-offs.
- **Developer** skills emphasize reproducible development, image construction, and local multi-service workflows.
- **Security** skills emphasize threat modeling, least privilege, provenance, and vulnerability management.

Learn each domain in sequence, and practice in a disposable environment. Use production access only through approved change controls. Docker features, defaults, licensing, and platform support evolve; confirm current behavior in the official documentation before adopting it.

## 1. Container and Docker foundations

**Applies to:** Core; all roles

### Container fundamentals

- [ ] Explain containers as isolated processes that share the host operating-system kernel, and compare containers with virtual machines and managed/serverless runtimes.
- [ ] Understand images, containers, tags, digests, registries, layers, and the writable container layer.
- [ ] Explain Linux namespaces and cgroups at a practical level; understand OCI image/runtime standards and the roles of Docker Engine, containerd, and OCI runtimes.
- [ ] Distinguish an image (immutable template) from a running container (a process with runtime configuration and a writable layer).
- [ ] Identify when Docker is a good fit and when a VM, managed platform, or function service is a better boundary.

### Docker architecture and environments

- [ ] Use the client/daemon model and understand that Docker CLI commands operate against a selected Docker context/daemon.
- [ ] Distinguish Docker Engine on Linux from Docker Desktop environments on Windows and macOS, including the Linux VM boundary where applicable.
- [ ] Inspect client/server versions, server configuration, storage, runtimes, and active context using `docker version`, `docker info`, and `docker context`.
- [ ] Understand daemon privileges and why access to the Docker socket/API is highly privileged.
- [ ] Know the differences among development workstation, CI builder, single-host runtime, and clustered/container-platform environments.

### Essential CLI and lifecycle

- [ ] Pull, inspect, tag, run, stop, start, restart, remove, and list containers and images.
- [ ] Use `docker ps`, `docker logs`, `docker exec`, `docker inspect`, `docker events`, and `docker stats` to inspect running workloads.
- [ ] Understand foreground/background execution, exit codes, signals, entrypoint/command behavior, and restart policies.
- [ ] Inspect resource consumption and determine whether an issue is in the application, container configuration, host, or daemon.
- [ ] Prune unused objects deliberately and understand the scope of each prune command.

## 2. Image design and Docker builds

**Applies to:** Core; especially Developer, DevOps / Platform, Security, Architect

### Dockerfile and image composition

- [ ] Write Dockerfiles using `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `ARG`, `USER`, `EXPOSE`, `ENTRYPOINT`, `CMD`, and `HEALTHCHECK` appropriately.
- [ ] Distinguish build-time `ARG` from runtime `ENV`; avoid treating either as a secure secret store.
- [ ] Explain the difference between `ENTRYPOINT` and `CMD`, exec form and shell form, and how signals reach the application process.
- [ ] Use `.dockerignore` to exclude credentials, local artifacts, VCS metadata, and unnecessary build context.
- [ ] Choose base images with regard to compatibility, maintenance, size, package ecosystem, and support—not size alone.
- [ ] Build multi-stage images that separate build dependencies from runtime artifacts.
- [ ] Run the application as a non-root user and include only the runtime dependencies and files needed.

### BuildKit, cache, and reproducibility

- [ ] Explain image layers and build cache invalidation; order Dockerfile steps to keep stable dependencies cacheable.
- [ ] Use BuildKit/buildx for modern builds, multi-platform targets, cache import/export, and build attestations where supported.
- [ ] Use build secrets and SSH forwarding features rather than embedding credentials in Dockerfile instructions or image layers.
- [ ] Understand build context, target stages, platforms, build arguments, and provenance metadata.
- [ ] Make builds repeatable by controlling base-image references, dependency lockfiles, build inputs, and build environment.
- [ ] Diagnose slow, unexpectedly invalidated, or non-reproducible builds.

### Image lifecycle and design

- [ ] Design immutable images: create a new image for a change rather than patching a running container.
- [ ] Tag images with human-readable release identifiers and deploy by digest when immutable identity is required.
- [ ] Understand mutable tags such as `latest` and the risks they pose to rollback and repeatable deployment.
- [ ] Inspect image metadata, layers, size, platform/architecture, labels, and history.
- [ ] Define image deprecation, retention, rebuild, patch, and rollback policies.

## 3. Registries and software supply chain

**Applies to:** Core; especially DevOps / Platform, Security, Architect

### Registry operations

- [ ] Authenticate to Docker Hub and private registries using supported credential mechanisms.
- [ ] Pull, tag, push, promote, mirror, and retain images across development, staging, and production.
- [ ] Design repository naming, access control, network access, replication, availability, and lifecycle policies.
- [ ] Understand the difference between a registry, repository, tag, and content digest.
- [ ] Avoid secrets in command history, source, pipeline logs, and image layers.

### Vulnerability and artifact assurance

- [ ] Generate and interpret software bills of materials (SBOMs) and image vulnerability reports.
- [ ] Use Docker Scout or an approved equivalent to evaluate package inventory, vulnerabilities, and remediation options.
- [ ] Establish vulnerability triage: severity, exploitability, reachability, exception ownership, remediation deadlines, and rebuild triggers.
- [ ] Understand image signing, identity, attestations, build provenance, and verification at release/deployment boundaries.
- [ ] Promote the same tested artifact between environments instead of rebuilding a different image for each environment.
- [ ] Define trusted base-image sources, supported versions, and a process for responding to base-image updates.

## 4. Container runtime and host operations

**Applies to:** Core; especially DevOps / Platform, SRE, Security, Architect

### Runtime configuration and process behavior

- [ ] Configure environment, command/entrypoint, working directory, exposed and published ports, restart behavior, and health checks.
- [ ] Understand that `EXPOSE` documents a container port; it does not publish a host port.
- [ ] Set CPU and memory constraints based on measured demand and host capacity; understand OOM behavior and resource contention.
- [ ] Configure PID limits, ulimits, shared memory, read-only root filesystems, and temporary writable paths where needed.
- [ ] Send and handle termination signals correctly; implement graceful shutdown and readiness/liveness behavior in the application.
- [ ] Use logs, events, metrics, exit codes, and inspect output to diagnose runtime issues.

### Docker Engine operations

- [ ] Install and update Docker Engine/Desktop using current platform-specific guidance.
- [ ] Manage daemon settings, data-root, logging driver, storage backend, proxies, registry mirrors, and live-restore behavior where appropriate.
- [ ] Understand how daemon configuration and system service settings interact; apply configuration through supported OS mechanisms.
- [ ] Monitor host disk, memory, CPU, file descriptors, network, image cache, and container churn.
- [ ] Configure log collection and rotation to prevent unbounded disk use.
- [ ] Manage engine upgrades, compatibility testing, maintenance windows, and rollback/recovery.

### Remote administration and troubleshooting

- [ ] Use Docker contexts to select and name endpoints safely.
- [ ] Secure any remote Engine API using authenticated TLS and network restrictions; never expose an unauthenticated daemon endpoint.
- [ ] Understand the security impact of membership in the Docker group or access to the Engine socket.
- [ ] Troubleshoot daemon startup, image pull/build, container exit, health check, port, DNS, disk pressure, and resource-limit failures.
- [ ] Use platform logs and Docker diagnostics to distinguish host/kernel, daemon, network, image, and application failures.

## 5. Networking

**Applies to:** Core; especially DevOps / Platform, SRE, Architect, Security

### Docker network models

- [ ] Understand bridge, host, none, overlay, macvlan, and ipvlan drivers and their appropriate use cases.
- [ ] Distinguish the default bridge from user-defined bridge networks, including service-name DNS behavior.
- [ ] Attach and detach containers from networks and inspect network configuration.
- [ ] Understand container interfaces, IP addressing, routing, DNS, NAT, firewall interaction, and port publishing.
- [ ] Distinguish a Dockerfile `EXPOSE` declaration from runtime port publishing (`-p`).

### Application and multi-host connectivity

- [ ] Connect services by stable service names rather than hard-coded container IP addresses.
- [ ] Design least-exposure ingress: publish only required ports and place dependent services on appropriate networks.
- [ ] Understand outbound connectivity, host-to-container access, container-to-host access, and cross-network communication.
- [ ] Troubleshoot name resolution, connection refusal, port collisions, routing, firewall rules, and MTU-related failures.
- [ ] Understand overlay networking prerequisites and the operational/security implications of cross-host container networking.
- [ ] Plan service discovery and ingress/load balancing separately from container networking.

## 6. Persistent data and stateful workloads

**Applies to:** Core; especially DevOps / Platform, SRE, Architect

### Storage primitives

- [ ] Explain the container writable layer and why it is not durable application storage.
- [ ] Choose named volumes, anonymous volumes, bind mounts, tmpfs, or other supported mounts based on persistence, portability, performance, and access needs.
- [ ] Create, inspect, back up, restore, and safely remove volumes.
- [ ] Understand volume ownership/permissions, mount propagation, host-path coupling, and data lifecycle.
- [ ] Distinguish Docker's container-data mounts from the daemon's image/layer storage backend.

### Stateful service design

- [ ] Externalize durable state and design database lifecycle independently from application-container lifecycle.
- [ ] Understand that a local Docker volume is generally host-local; it is not automatically replicated or highly available.
- [ ] Design backup consistency, restore testing, encryption, retention, and recovery objectives for persistent data.
- [ ] Avoid concurrent writers or unsafe sharing of filesystem-backed data unless the storage system and application explicitly support it.
- [ ] Decide when to use a managed database/storage service rather than operating a stateful container.

## 7. Docker Compose and workload orchestration

**Applies to:** Core; especially Developer, DevOps / Platform, SRE, Architect

### Compose application model

- [ ] Define multi-service applications in Compose YAML using services, images/build, networks, volumes, configs, secrets, health checks, and dependencies.
- [ ] Run, stop, rebuild, scale where supported, inspect, and clean up Compose applications.
- [ ] Understand variable interpolation, environment files, profiles, project names, and multiple Compose files.
- [ ] Use health checks and readiness-aware application behavior; do not assume `depends_on` means a dependency is ready.
- [ ] Separate development, test, and deployment settings without baking environment-specific secrets into images.
- [ ] Understand Compose implementation differences and verify feature support in the intended environment.

### Production fit and orchestration choices

- [ ] Use Compose to define and operate an application on a single Docker host or in suitable development/CI workflows.
- [ ] Understand Docker Swarm mode concepts: managers/workers, services/tasks, desired state, replicas, placement, rolling updates, rollback, secrets, configs, and overlay networks.
- [ ] Understand that Swarm mode is Docker Engine's cluster orchestrator and is distinct from legacy Docker Classic Swarm.
- [ ] Compare Compose, Swarm, Kubernetes, and managed container platforms by scale, ecosystem, operations, availability, team skill, and portability.
- [ ] Know when to stop using a single-host Compose deployment and move to a supported orchestrator or managed service.
- [ ] Treat clustering as a platform design with control-plane availability, networking, identity, storage, upgrades, monitoring, and recovery requirements.

## 8. Security and isolation

**Applies to:** Core; especially Security, DevOps / Platform, Architect, SRE

### Threat model and least privilege

- [ ] Identify the host kernel, Docker daemon/API/socket, images, registries, runtime configuration, mounts, credentials, and networks as security boundaries.
- [ ] Avoid `--privileged`; grant only required Linux capabilities and device access.
- [ ] Use non-root processes, rootless mode or user namespace remapping where compatible with the workload and operational constraints.
- [ ] Use seccomp and AppArmor/SELinux profiles where available; understand their effect and avoid disabling protections without a justified review.
- [ ] Apply read-only filesystems, `no-new-privileges`, resource limits, and network segmentation where appropriate.
- [ ] Keep the host kernel, Docker Engine, base images, packages, and application dependencies patched.

### Secrets, access, and image security

- [ ] Deliver secrets through a dedicated secrets mechanism or runtime-mounted secret facility; do not bake them into images or expose them in `ARG`, `ENV`, logs, or build output.
- [ ] Restrict daemon socket access and secure remote Engine API access; treat daemon control as highly privileged host access.
- [ ] Apply least-privilege registry and host access controls and rotate credentials.
- [ ] Scan images, prioritize and remediate vulnerabilities, and rebuild from maintained base images.
- [ ] Verify image provenance/signatures according to the organization’s supply-chain policy.
- [ ] Understand Swarm mutual TLS and secrets when using Swarm; do not assume those mechanisms apply to standalone Docker.

## 9. CI/CD and release engineering

**Applies to:** Core; especially DevOps / Platform, Security, Architect, Developer

### Build and test pipelines

- [ ] Build images in CI using a controlled builder and a versioned build context.
- [ ] Run unit, integration, and image-level tests against the built artifact.
- [ ] Use build cache safely without allowing untrusted builds to poison trusted release caches.
- [ ] Authenticate to registries using short-lived or tightly scoped credentials where supported.
- [ ] Publish immutable release identifiers and capture build metadata, SBOM, and provenance.
- [ ] Separate pull-request validation from privileged release and deployment workflows.

### Release promotion and rollback

- [ ] Promote a tested image through environments by digest or immutable artifact reference.
- [ ] Define release approvals, policy checks, deployment sequencing, health validation, and rollback criteria.
- [ ] Maintain a traceable link from source revision to build, image digest, scan results, provenance, and deployment.
- [ ] Define retention, cleanup, and incident response for compromised or vulnerable images.
- [ ] Test rollback and recovery; understand that reverting a container image cannot automatically reverse data/schema changes.

## 10. Observability, reliability, and incident response

**Applies to:** Core; especially SRE, DevOps / Platform, Architect

### Workload observability

- [ ] Emit application logs to stdout/stderr or an explicitly configured logging system and collect them centrally.
- [ ] Monitor container/host CPU, memory, restarts, exit status, disk, network, and health.
- [ ] Define useful health checks and distinguish process health from service readiness and user-visible availability.
- [ ] Correlate image digest, deployment version, container instance, logs, metrics, and traces during an incident.
- [ ] Control log volume, retention, sensitive fields, and access.

### Reliability and operations

- [ ] Plan capacity, redundancy, failure domains, service dependencies, and maintenance for the chosen runtime.
- [ ] Design restart and replacement behavior without confusing automatic restart with application recovery or high availability.
- [ ] Test host loss, registry outage, dependency failure, image rollback, storage restore, and network interruption in a controlled environment.
- [ ] Create runbooks for incident triage, safe restart, escalation, image recovery, backup restore, and security response.
- [ ] Measure deployment success, recovery time, failure rate, resource efficiency, and operational toil.

## 11. Architecture and role-specific competency tracks

### DevOps / Platform engineer

- [ ] Standardize Dockerfiles, build actions, registry namespaces, base images, and Compose templates.
- [ ] Design secure CI build, test, scan, attest, sign, promote, and deploy workflows.
- [ ] Operate builders, registries, host pools, runtime configuration, upgrades, logging, and cleanup policies.
- [ ] Offer paved-road templates while preserving clear ownership, versioning, and exceptions.

### SRE

- [ ] Define workload health, SLO signals, resource budgets, restart behavior, and incident diagnostics.
- [ ] Engineer safe deployments, progressive rollout/rollback, capacity management, and recovery testing.
- [ ] Understand where Docker ends and the host, orchestrator, cloud service, or application takes responsibility.

### Cloud / container architect

- [ ] Choose among containers, VMs, serverless, Compose, Swarm, Kubernetes, and managed container platforms using requirements rather than familiarity.
- [ ] Define trust boundaries, tenancy/isolation, identity, network paths, state ownership, failure domains, and operating model.
- [ ] Design registry topology, artifact promotion, data protection, observability, upgrades, support, and cost controls.
- [ ] Produce reference architectures, operational standards, threat models, lifecycle policies, and migration plans.

### Application developer

- [ ] Create small, maintainable, reproducible images and run services locally with Compose.
- [ ] Keep configuration external, handle shutdown signals, expose meaningful health, and avoid reliance on container-local durable state.
- [ ] Debug the application inside its actual container/network/runtime environment.

### Security engineer

- [ ] Threat-model daemon/API access, image sources, build secrets, mounts, capabilities, runtime identity, and network exposure.
- [ ] Define hardened build/runtime baselines, vulnerability SLAs, trusted image policies, signing/provenance verification, and exception processes.
- [ ] Validate that controls are observable, automatable, and compatible with workload requirements.

## 12. Practical portfolio and readiness checklist

- [ ] Build a non-root, multi-stage image for a small service; explain image layers, cache behavior, base-image choice, and signal handling.
- [ ] Run an application and database with Compose using a private network, persistent named volume, health checks, and non-secret configuration.
- [ ] Demonstrate image inspection, digest-based promotion, vulnerability review, SBOM/provenance capture, and a documented remediation decision.
- [ ] Configure and troubleshoot CPU/memory limits, logs, DNS, published ports, and volume persistence in a disposable environment.
- [ ] Create a CI workflow that builds and tests an image, publishes it to a registry using protected credentials, and records the resulting digest.
- [ ] Write a short architecture decision record comparing Compose on one host, Swarm, Kubernetes, and a managed container service for a realistic workload.
- [ ] Demonstrate a recovery exercise: replace a container from a known image, restore required data, validate health, and record recovery gaps.
- [ ] Explain the major risks of mounting the Docker socket, running privileged/root containers, exposing an unauthenticated daemon, and storing secrets in image layers.

## Official Docker references

### Foundations and operations

- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Engine overview](https://docs.docker.com/engine/)
- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/)
- [Docker contexts](https://docs.docker.com/engine/manage-resources/contexts/)
- [Docker Engine security](https://docs.docker.com/engine/security/)
- [Protect access to the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/)
- [Remote access for the Docker daemon](https://docs.docker.com/engine/daemon/remote-access/)
- [Rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- [Logging drivers](https://docs.docker.com/engine/logging/configure/)

### Images and builds

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Build best practices](https://docs.docker.com/build/building/best-practices/)
- [Docker Build](https://docs.docker.com/build/)
- [Build secrets](https://docs.docker.com/build/building/secrets/)
- [Docker Scout](https://docs.docker.com/scout/)
- [Docker Hub](https://docs.docker.com/docker-hub/)

### Networking, storage, Compose, and orchestration

- [Networking overview](https://docs.docker.com/engine/network/)
- [Storage overview](https://docs.docker.com/engine/storage/)
- [Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Compose in production](https://docs.docker.com/compose/how-tos/production/)
- [Swarm mode](https://docs.docker.com/engine/swarm/)

### CI/CD and supply chain

- [Docker with GitHub Actions](https://docs.docker.com/guides/gha/)
- [Build attestations](https://docs.docker.com/build/metadata/attestations/)
- [Docker Scout quickstart](https://docs.docker.com/scout/quickstart/)

## Keeping this syllabus current

This is a broad real-world learning framework, not a vendor-issued certification blueprint. Review linked Docker documentation for current defaults and feature status. Review the target employer/platform requirements separately for Kubernetes, cloud providers, Linux administration, networking, compliance, and CI/CD systems.
