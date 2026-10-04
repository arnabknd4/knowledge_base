# Kubernetes Syllabus for Real-World Operations

This document is a role-based Kubernetes syllabus for DevOps, SRE, Platform, and Architect work. It is not an official Kubernetes certification blueprint and not an official CNCF exam study guide. It is a practical production-oriented checklist based on the current official Kubernetes documentation and current cloud-native operations patterns.

Important: if you compare this to CKA/CKAD/CKS, treat that only as optional exam alignment based on official certification pages, not as a blueprint for this syllabus.

## 1) Scope and design principles

This syllabus is designed around real cluster operations, not exam memorization.

- Core subscription: official Kubernetes documentation for concepts, tasks, production environment, architecture, networking, workloads, security, storage, and administration.
- Role lens: DevOps, SRE, Platform, and Architect tracks differ in depth and decision-making, not in core Kubernetes fundamentals.
- Real-world emphasis: cluster security, autoscaling, resilience, ingress/gateway strategy, backup/restore, reliability, cost, and operational automation.
- Production nuances: ambiguous or optional runtime capabilities are called out as such; managed control plane ownership is separated from application and platform responsibilities.

Official sources referenced throughout:

- Kubernetes overview: https://kubernetes.io/docs/concepts/overview/
- Architecture: https://kubernetes.io/docs/concepts/architecture/
- Workloads: https://kubernetes.io/docs/concepts/workloads/
- Scheduling and eviction: https://kubernetes.io/docs/concepts/scheduling-eviction/
- Services and networking: https://kubernetes.io/docs/concepts/services-networking/
- Gateway API: https://kubernetes.io/docs/concepts/services-networking/gateway/
- Storage: https://kubernetes.io/docs/concepts/storage/
- Security: https://kubernetes.io/docs/concepts/security/
- Production environment: https://kubernetes.io/docs/setup/production-environment/
- Tasks: https://kubernetes.io/docs/tasks/
- kubectl reference: https://kubernetes.io/docs/reference/kubectl/
- Custom Resource Definitions: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- Network plugins: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
- Admission controllers: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/
- etcd backup documentation: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
- etcd docs: https://etcd.io/docs/

## 2) Role map: what changes by role

| Role | Primary focus | Must be strong in | Should understand deeply |
|---|---|---|---|
| DevOps | Deployment, automation, pipelines, reliability | kubectl, YAML, Deployments, Jobs, ConfigMaps, Secrets, Service/Ingress, observability, GitOps basics | RBAC, release strategy, autoscaling, cluster upgrades, cost governance |
| SRE | Reliability, incident response, performance, safety | cluster health, logging/metrics, troubleshooting, SLOs, PDB, HPA, autoscaling, node maintenance, network/DNS debugging | control plane resilience, capacity planning, failure modes, chaos/DR drills |
| Platform | Golden paths, developer experience, internal platforms | RBAC, namespaces, policy, ingress/gateway, Helm/Kustomize, CRDs, GitOps, security guardrails, platform standards | multi-tenancy, cluster lifecycle, cost, environment isolation, self-service with policy control |
| Architect | Platform decisions, scale, security, cloud strategy | cluster architecture, control plane/worker separation, multi-cluster, storage/network choices, DR, managed services, API lifecycle | cloud-managed services, cost/performance trade-offs, vendor strategy, platform governance, security boundaries |

## 3) Core production checklist

Use the labels below:

- Core = expected of most Kubernetes operators and engineers.
- DevOps = important for delivery and operational automation.
- SRE = important for availability, observability, and troubleshooting.
- Platform = important for internal platform and policy management.
- Architect = important for high-level design decisions and cluster strategy.
- Optional = useful but not mandatory for every role.

### 3.1 Kubernetes fundamentals and architecture

- [ ] Understand the problem Kubernetes solves: declarative orchestration, self-healing, scaling, and service discovery. [Core]
- [ ] Know the control plane vs worker node split and production HA topology. [Core]
- [ ] Understand kube-apiserver, etcd, kube-scheduler, kube-controller-manager, kubelet, kube-proxy, and cloud-controller-manager responsibilities. [Core]
- [ ] Know the API server role as the front end for cluster state and the control-plane authority for API access. [Core]
- [ ] Understand etcd as the backing store for Kubernetes cluster state and the requirement for backups and restore plans. [Core]
- [ ] Understand CRI, CNI, and CSI as extension boundaries; Kubernetes APIs are not the implementations themselves. [Core]
- [ ] Distinguish container runtime interface (CRI), network plugins (CNI), and storage drivers (CSI). [Core]
- [ ] Understand cluster components and how they communicate, including API access patterns, node agents, and pod lifecycle management. [Core]
- [ ] Know how kube-proxy works and when a CNI plugin may provide alternative service proxying behavior. [Core]
- [ ] Understand that control plane responsibility differs between self-managed and managed Kubernetes offerings. [Architect]
- [ ] Know the node lifecycle, node conditions, taints, and upgrade implications for workloads. [Core]
- [ ] Understand namespaces as logical isolation boundaries for workloads, policies, and resources. [Core]
- [ ] Be able to read and explain API groups, versions, resources, and basic kubectl behavior. [Core]
- [ ] Know how to use kubectl with context switching, explain, dry-run, and resource output filters. [Core]
- [ ] Practice `kubectl get`, `describe`, `logs`, `exec`, `top`, `apply`, `create`, `delete`, `run`, `explain`, and JSONPath/custom-columns. [Core]

Official references:

- https://kubernetes.io/docs/concepts/architecture/
- https://kubernetes.io/docs/reference/kubectl/
- https://kubernetes.io/docs/concepts/overview/

### 3.2 Pods, workloads, controllers, and jobs

- [ ] Understand Pod semantics, restart policy, container lifecycle, and termination behavior. [Core]
- [ ] Understand multi-container Pods, init containers, sidecars, and when each pattern is appropriate. [Core]
- [ ] Know ReplicaSet, Deployment, StatefulSet, DaemonSet, Job, and CronJob responsibilities and common use cases. [Core]
- [ ] Know rollout, revision history, rollout strategy, and rollback procedures for Deployments. [Core]
- [ ] Be able to reason about StatefulSet persistence, identity, and stable network identities. [Core]
- [ ] Understand DaemonSet behavior for node-local services and cluster agents. [Core]
- [ ] Know Job and CronJob semantics for finite and scheduled workloads. [Core]
- [ ] Use labels, selectors, and annotations correctly for service discovery, grouping, policy scoping, and automation. [Core]
- [ ] Configure readiness, liveness, and startup probes correctly for production workloads. [Core]
- [ ] Understand what `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, `Failed`, and `Evicted` mean in practice. [SRE]
- [ ] Understand pod disruption and eviction, including PDBs and maintenance semantics. [SRE]
- [ ] Understand Jobs with parallelism, completions, backoff limits, and retries. [DevOps]
- [ ] Understand Pod affinity/anti-affinity, topology spread, and topological constraints for scheduling quality. [Platform]

Official references:

- https://kubernetes.io/docs/concepts/workloads/
- https://kubernetes.io/docs/concepts/scheduling-eviction/
- https://kubernetes.io/docs/concepts/workloads/pods/

### 3.3 Configuration, Secrets, and policy inputs

- [ ] Use ConfigMap and Secret as the standard configuration and secret management APIs. [Core]
- [ ] Know the difference between environment variables and mounted files. [Core]
- [ ] Understand secret usage patterns, secret types, and operational cautions around storing sensitive values. [Core]
- [ ] Understand image pull secrets and registry access patterns. [DevOps]
- [ ] Understand admission, policy, and policy enforcement points before an object reaches runtime. [Platform]
- [ ] Be familiar with Kubernetes-native policy and security APIs beyond plain resource manifests. [Platform]
- [ ] Know that encryption at rest and secret protection are separate concerns from application-level secret handling. [Architect]
- [ ] Understand the role of Secret objects in configuration, but not assume they are a complete secret management system by themselves. [Architect]

Official references:

- https://kubernetes.io/docs/concepts/configuration/secret/
- https://kubernetes.io/docs/concepts/configuration/configmap/
- https://kubernetes.io/docs/concepts/security/

### 3.4 Resource management, scheduling, autoscaling, and disruption

- [ ] Set requests and limits appropriately for CPU and memory to support QoS and scheduling decisions. [Core]
- [ ] Understand QoS classes, eviction behavior, and the relationship between resource requests, limits, and node pressure. [Core]
- [ ] Understand LimitRange and ResourceQuota for multi-tenant and shared clusters. [Platform]
- [ ] Use nodeSelector, affinity, anti-affinity, taints, tolerations, and topology spread constraints correctly. [Core]
- [ ] Understand priority classes and preemption as part of scheduling policy. [Platform]
- [ ] Know the scheduling flow and how controllers, scheduler, and kubelet interact during placement. [Core]
- [ ] Configure HorizontalPodAutoscaler to scale based on observed metrics. [DevOps]
- [ ] Understand VPA and Cluster Autoscaler as additional scaling tools, not a replacement for workload design. [Architect]
- [ ] Design for disruption budgets and safe maintenance windows, including drain, cordon, uncordon, node replacement, and rolling upgrades. [SRE]
- [ ] Understand PodDisruptionBudget semantics and expected availability behavior. [SRE]
- [ ] Be able to reason about capacity planning, saturation, queue-depth risk, and node churn. [SRE]

Official references:

- https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- https://kubernetes.io/docs/concepts/scheduling-eviction/
- https://kubernetes.io/docs/concepts/workloads/pods/disruptions/

### 3.5 Services, networking, DNS, Ingress, Gateway, and CNI

- [ ] Understand the Kubernetes network model: pod network, service abstraction, and the cluster-level communication model. [Core]
- [ ] Know the difference between Pod IP, Service IP, node IP, and external load balancer/service exposure. [Core]
- [ ] Understand ClusterIP, NodePort, LoadBalancer, ExternalName, and headless Services. [Core]
- [ ] Understand EndpointSlice and how Service backends are discovered and updated. [Core]
- [ ] Know CoreDNS and how cluster DNS enables stable internal service discovery. [Core]
- [ ] Understand Ingress and Ingress controllers as a common entry point for HTTP(S) traffic. [Core]
- [ ] Understand that the Ingress API is effectively frozen for new core features and that Gateway API is the recommended path for new routing capabilities. [Core]
- [ ] Know Gateway API roles (GatewayClass, Gateway, HTTPRoute, GRPCRoute) and why it is more expressive than Ingress. [Core]
- [ ] Understand the relationship between Gateway API and controller implementations, and not confuse it with core Kubernetes itself. [Architect]
- [ ] Understand NetworkPolicy as a Kubernetes API, but note its enforcement depends on the underlying network plugin and CNI implementation. [Core]
- [ ] Know the difference between network policy enforcement and general cluster networking; not all CNI plugins implement policy equally. [Core]
- [ ] Understand that CNI plugins and Service proxy behavior are external to core Kubernetes and are implementation-specific. [Core]
- [ ] Know how to troubleshoot DNS, service reachability, port exposure, and broken pod-to-service routing. [SRE]
- [ ] Understand when a service mesh is useful versus when simpler L4/L7 routing and platform policies are sufficient. [Optional]

Official references:

- https://kubernetes.io/docs/concepts/services-networking/
- https://kubernetes.io/docs/concepts/services-networking/gateway/
- https://kubernetes.io/docs/concepts/services-networking/network-policies/
- https://kubernetes.io/docs/concepts/cluster-administration/addons/
- https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/

### 3.6 Storage, CSI, volumes, and stateful workloads

- [ ] Understand volumes, persistent volumes, claims, storage classes, and dynamic provisioning. [Core]
- [ ] Know basic volume types, emptyDir, hostPath, ConfigMap/Secret mounts, and their correct use cases. [Core]
- [ ] Choose between local storage, network storage, and cloud block/object storage based on workload requirements. [Architect]
- [ ] Understand access modes, reclaim policies, and storage class behavior in cluster operations. [Core]
- [ ] Know CSI drivers and why storage is implementation-specific rather than a single Kubernetes storage API. [Core]
- [ ] Understand snapshot, expansion, and backup implications for stateful workloads. [Platform]
- [ ] Align storage strategy with workload durability, backup/restore, and DR requirements. [Architect]
- [ ] Understand stateful workloads requiring stable identity and persistent storage in relation to StatefulSet design. [Core]

Official references:

- https://kubernetes.io/docs/concepts/storage/
- https://kubernetes.io/docs/concepts/storage/persistent-volumes/
- https://kubernetes.io/docs/concepts/storage/storage-classes/

### 3.7 Security: identity, RBAC, workloads, admission, and supply chain

- [ ] Understand the difference between authentication, authorization, and admission control. [Core]
- [ ] Use RBAC correctly: Roles, ClusterRoles, RoleBindings, ClusterRoleBindings, and service accounts. [Core]
- [ ] Separate workload identity from human identity and understand service account usage and least privilege. [Core]
- [ ] Understand Pod security standards, securityContext, privilege boundaries, and runtime isolation choices. [Core]
- [ ] Know admission controllers and their role in validating and mutating API objects. [Platform]
- [ ] Understand policy engines and validation strategies for cluster governance. [Platform]
- [ ] Understand secret management requirements beyond Kubernetes Secret objects, including centralized secret stores and external secret patterns. [Architect]
- [ ] Know security baselines for container images, artifact provenance, and supply-chain controls. [Architect]
- [ ] Understand Kubernetes audit logging and how to review security-relevant events. [SRE]
- [ ] Recognize runtime security controls such as seccomp/AppArmor/RuntimeClass as ecosystem controls, not core Kubernetes primitives alone. [Optional]
- [ ] Understand cluster-level security boundaries in multi-tenant environments, including namespaces, network policy, and policy-as-code. [Platform]

Official references:

- https://kubernetes.io/docs/concepts/security/
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/
- https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- https://kubernetes.io/docs/concepts/security/pod-security-standards/

### 3.8 Cluster lifecycle, upgrades, high availability, backup, and recovery

- [ ] Understand self-managed cluster lifecycle from bootstrap to node join/leave, maintenance, and decommission. [Core]
- [ ] Be familiar with kubeadm concepts for installation, joining, upgrades, and control-plane topologies. [Core]
- [ ] Understand the difference between control plane HA, worker node scaling, and cluster-level availability engineering. [Core]
- [ ] Understand the need for multi-control-plane setups and not conflating them with generic workload redundancy. [Core]
- [ ] Back up etcd and restore procedures as part of disaster recovery planning. [Core]
- [ ] Know how to drain, cordon, uncordon, and replace nodes safely without creating surprise downtime. [Core]
- [ ] Understand Kubernetes version skew expectations and upgrade sequencing. [Core]
- [ ] Design production cluster topology for resilience, observability, security boundaries, and upgrade strategy. [Architect]
- [ ] Understand managed control plane responsibilities in cloud environments and the remaining workload/platform responsibilities. [Architect]
- [ ] Apply recovery drills, DR testing, and operational runbooks for control plane and data-plane failures. [SRE]
- [ ] Understand that cloud-managed control planes reduce operational burden, but app, policy, and cluster security responsibilities remain. [Architect]

Official references:

- https://kubernetes.io/docs/setup/production-environment/
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
- https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
- https://etcd.io/docs/

### 3.9 Observability, SLOs, monitoring, logging, and troubleshooting

- [ ] Use metrics, logs, and events to debug workloads and cluster health. [Core]
- [ ] Know kubectl troubleshooting tools: logs, describe, get, exec, top, events, and API inspection patterns. [Core]
- [ ] Understand how to diagnose Pending, CrashLoopBackOff, ImagePullBackOff, OOMKilled, Evicted, NotReady, and network policy-related failures. [SRE]
- [ ] Know the role of kubelet, node conditions, and container runtime health in node troubleshooting. [SRE]
- [ ] Understand control plane component failure modes and the distinction between control plane issues and workload issues. [SRE]
- [ ] Know how to diagnose service reachability, DNS failures, and ingress/backend issues. [SRE]
- [ ] Understand metrics-server, Prometheus, Grafana, Loki, OpenTelemetry, and related visibility stacks at a practical level. [Core]
- [ ] Define SLOs, SLIs, error budgets, and alerting patterns for Kubernetes services. [SRE]
- [ ] Be able to distinguish alerts from actionable runbooks, and communicate incidents with evidence. [SRE]
- [ ] Understand the operating difference between cluster-level logs and app-level telemetry in multi-service systems. [Architect]

Official references:

- https://kubernetes.io/docs/tasks/debug/
- https://kubernetes.io/docs/concepts/cluster-administration/logging/
- https://kubernetes.io/docs/concepts/cluster-administration/proxies/

### 3.10 Packaging, extensibility, GitOps, CRDs, and operators

- [ ] Know Helm and Kustomize as common packaging and configuration workflows. [DevOps]
- [ ] Understand how Helm charts and values are used to package applications and platform components. [DevOps]
- [ ] Understand Kustomize overlays and the separation of base and environment-specific configuration. [DevOps]
- [ ] Know when CRDs and Operators are appropriate for platform extension and custom controllers. [Platform]
- [ ] Understand the difference between a CRD and a full runtime controller/operator model. [Platform]
- [ ] Be familiar with GitOps patterns (Argo CD, Flux) for reconciliation and cluster state management. [Platform]
- [ ] Know that GitOps does not eliminate the need for RBAC, policy, secret handling, or observability. [Architect]
- [ ] Understand how platform teams use CRDs and Operators to create self-service abstractions without exposing every raw API. [Platform]

Official references:

- https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/

### 3.11 Cloud-managed Kubernetes, multi-cluster, capacity, costs, and architecture choices

- [ ] Understand the major managed Kubernetes operating models and where they fit: managed control plane, managed nodes, and fully managed services. [Architect]
- [ ] Understand cluster cost drivers: compute, storage, network, observability, backups, and platform overhead. [Architect]
- [ ] Understand the trade-offs between single-cluster, multi-cluster, and region-aware architecture choices. [Architect]
- [ ] Plan for multi-cluster topology, workload isolation, and DR/BCP strategies. [Architect]
- [ ] Understand that managed Kubernetes can simplify control-plane operations while not removing responsibilities for workload behavior, security policy, monitoring, and cost management. [Architect]
- [ ] Design for capacity management, node pools, taints, autoscaling, and workload spread across failure domains. [Architect]
- [ ] Understand the design trade-offs between platform standardization and flexibility in enterprise environments. [Platform]
- [ ] Be able to explain active/active vs active/passive, regional failover, and workload dependencies across clusters. [Architect]

Official references:

- https://kubernetes.io/docs/setup/production-environment/
- https://kubernetes.io/docs/concepts/architecture/

## 4) Role-specific tracks

### 4.1 DevOps track

Focus: shipping reliable workloads and automation.

- [ ] kubectl fundamentals and YAML authoring [Core]
- [ ] Deployment, rollout, rollback, canaries, and release gating [Core]
- [ ] ConfigMap, Secret, and image pull configuration [Core]
- [ ] Service discovery, Ingress/Gateway routing, and DNS awareness [Core]
- [ ] HPA and workload autoscaling [DevOps]
- [ ] Helm/Kustomize workflows [DevOps]
- [ ] CI/CD integration with Kubernetes deployment patterns [DevOps]
- [ ] Basic cluster health checks, service validation, and rollback runbooks [SRE]

### 4.2 SRE track

Focus: reliability, availability, and incident response.

- [ ] Cluster health and node-level troubleshooting [Core]
- [ ] Control plane and worker node failure modes [SRE]
- [ ] Observability: metrics, logs, events, tracing, and SLO-driven alerts [Core]
- [ ] Pod disruption, eviction, PDBs, scheduling failures, and capacity constraints [SRE]
- [ ] Service/DNS/network debugging and ingress/backend outage diagnosis [SRE]
- [ ] Backup and restore planning for etcd and stateful workloads [SRE]
- [ ] Chaos/DR rehearsal and incident communications [SRE]
- [ ] Capacity management and scaling policy design [Architect]

### 4.3 Platform track

Focus: cluster guardrails, self-service, and governance.

- [ ] RBAC, namespaces, quotas, policies, and admission control [Core]
- [ ] Workload isolation, tenant boundaries, and policy-as-code [Platform]
- [ ] Ingress/Gateway strategy and service exposure policy [Platform]
- [ ] Helm/Kustomize/CRDs/Operators as internal platform primitives [Platform]
- [ ] GitOps workflows and merge-to-cluster automation [Platform]
- [ ] Secret management integration and externalized secret patterns [Platform]
- [ ] Security baseline enforcement and image policy [Platform]
- [ ] Developer experience, golden paths, and platform documentation [Platform]

### 4.4 Architect track

Focus: design at cluster and platform level.

- [ ] Control plane topology and HA design [Core]
- [ ] Network architecture: CNI, service forwarding, ingress/gateway, policy, DNS [Core]
- [ ] Storage architecture: CSI, persistence, backup, DR, performance [Core]
- [ ] Multi-cluster, regional, and DR strategy [Architect]
- [ ] Managed vs self-managed control plane decision model [Architect]
- [ ] Cost, capacity, node pool strategy, and platform governance [Architect]
- [ ] Security architecture: identity, network boundaries, workload isolation, policy [Architect]
- [ ] Platform design: standardization, golden paths, internal developer platform choices [Architect]

## 5) Practical lab and capstone path

Recommended progression:

1. Build a local or lab cluster and learn control plane/node basics. [Core]
2. Deploy a stateless app with Service and Ingress or Gateway. [Core]
3. Add ConfigMap, Secret, probes, scaling, and rollout/rollback. [Core]
4. Add a StatefulSet with persistent storage and storage class configuration. [Core]
5. Add RBAC, service accounts, and NetworkPolicy to enforce least privilege. [Core]
6. Add HPA, PDB, and resource limits to simulate production load. [SRE]
7. Create a Helm chart or Kustomize overlay flow and compare deployment patterns. [DevOps]
8. Design a platform guardrail set with policy and GitOps automation. [Platform]
9. Design a multi-cluster or multi-region cluster topology with DR and cost model. [Architect]
10. Run a formal incident review on a failed rollout, service outage, or node issue. [SRE]

## 6) Official CKA/CKAD/CKS alignment: optional and separate from this syllabus

This section documents only official certification sources. It is optional and does not create a blueprint for this role-based syllabus.

- CKA official page: https://www.cncf.io/training/certification/cka/
  - Official exam description states the domains are: Cluster Architecture, Installation & Configuration; Workloads & Scheduling; Services & Networking; Storage; Troubleshooting.
  - Official source also lists the published exam weights: 25%, 15%, 20%, 10%, 30%.

- CKAD official page: https://www.cncf.io/training/certification/ckad/
  - Official exam description states the domains are: Application Design and Build; Application Deployment; Application Observability and Maintenance; Application Environment, Configuration and Security; Services and Networking.
  - Official source also lists the published exam weights: 20%, 20%, 15%, 25%, 20%.

- CKS official page: https://www.cncf.io/training/certification/cks/
  - Official source states that CKS is a performance-based security certification focused on securing container-based applications and Kubernetes platforms during build, deployment, and runtime.
  - The official page explicitly states CKS candidates must pass CKA before attempting CKS.
  - This page does not publish a weight breakdown on the same page, so this syllabus does not invent one.

Do not treat these exam domains as a substitute for the operational syllabus above. They are separate certification artifacts.

## 7) Production nuances and anti-patterns to remember

- [ ] NetworkPolicy enforcement depends on the CNI implementation; the API can exist even when the plugin does not enforce it. [Core]
- [ ] Ingress is a core API, but current docs and Gateway API guidance point to Gateway API for newer routing features and more expressive traffic shaping. [Core]
- [ ] Distinguish core Kubernetes APIs from ecosystem add-ons such as CNI plugins, ingress controllers, service meshes, secret backends, and custom controllers. [Core]
- [ ] Do not assume managed Kubernetes removes responsibility for workload design, policy, security posture, backup, monitoring, capacity, or incident readiness. [Architect]
- [ ] Understand where vendor-specific responsibilities begin and end for control plane, nodes, networking, storage, and identity services. [Architect]
- [ ] Treat Kubernetes as a platform control plane, not a complete security or operations system by itself. [Architect]

## 8) Core references

- Kubernetes overview: https://kubernetes.io/docs/concepts/overview/
- Architecture: https://kubernetes.io/docs/concepts/architecture/
- Workloads: https://kubernetes.io/docs/concepts/workloads/
- Scheduling and eviction: https://kubernetes.io/docs/concepts/scheduling-eviction/
- Services, load balancing, and networking: https://kubernetes.io/docs/concepts/services-networking/
- Gateway API: https://kubernetes.io/docs/concepts/services-networking/gateway/
- Storage: https://kubernetes.io/docs/concepts/storage/
- Security: https://kubernetes.io/docs/concepts/security/
- Production environment: https://kubernetes.io/docs/setup/production-environment/
- Tasks: https://kubernetes.io/docs/tasks/
- kubectl reference: https://kubernetes.io/docs/reference/kubectl/
- Network plugins: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
- CRDs: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- PodSecurity: https://kubernetes.io/docs/concepts/security/pod-security-standards/
- Admission controllers: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- etcd docs: https://etcd.io/docs/

This checklist is intentionally practical. A strong Kubernetes engineer in production is not measured only by exam recall, but by the ability to operate a secure, observable, resilient, and cost-aware Kubernetes platform.
