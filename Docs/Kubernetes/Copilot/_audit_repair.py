"""Repair objective-to-content archetype mismatches in the Kubernetes library."""
from pathlib import Path
import re

ROOT = Path(__file__).parent

# Map each source objective number to the subject-matched guide section set.
# The exemplars are verified topic-aligned guides; their Objective, path,
# role-specific metadata, and CKA mapping are not copied.
ASSIGNMENTS = {
    "architecture": {2, 3, 6, 7, 8, 83, 84, 88, 127, 142},
    "api": {4, 13, 14, 15, 118, 124},
    "workloads": {16, 17, 18, 21, 22, 23, 27},
    "rollout": {19, 119},
    "probes": {24},
    "config": {29, 30, 31, 32, 36, 120},
    "resources": {37, 38, 39},
    "scheduling": {28, 40, 41, 42},
    "autoscaling": {43, 44, 47, 115, 122, 133},
    "disruption": {26, 45, 46, 86, 129},
    "network": {1, 9, 48, 49, 57, 58, 59, 60, 61, 97, 130, 143, 150},
    "service": {50, 51, 53, 54, 55, 56, 121, 136, 151},
    "dns": {52},
    "storage": {20, 62, 63, 64, 65, 66, 67, 68, 69, 131, 144},
    "security": {12, 33, 34, 35, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 114, 134, 135, 139, 140, 148, 155},
    "lifecycle": {5, 11, 81, 82, 85, 87, 90},
    "observability": {25, 92, 93, 94, 95, 96, 98, 99, 100, 101, 125, 126, 128, 132},
    "extension": {102, 103, 104, 105, 106, 107, 108, 109, 123, 137, 138, 141, 149},
    "architecture-choice": {10, 89, 91, 110, 111, 112, 113, 116, 117, 145, 146, 147, 153, 154},
    "production": {152},
}

EXEMPLARS = {
    "architecture": 3,
    "api": 4,
    "workloads": 17,
    "rollout": 19,
    "probes": 24,
    "config": 30,
    "resources": 37,
    "scheduling": 40,
    "autoscaling": 43,
    "disruption": 45,
    "network": 48,
    "service": 49,
    "dns": 52,
    "storage": 62,
    "security": 70,
    "lifecycle": 82,
    "observability": 92,
    "extension": 102,
    "architecture-choice": 89,
    "production": 152,
}

GUIDES = {}
for path in ROOT.rglob("study-guide.md"):
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^# Objective (\d+):", text, re.M)
    if match:
        GUIDES[int(match.group(1))] = (path, text)
assert len(GUIDES) == 155, f"Expected 155 guides; found {len(GUIDES)}"

CATEGORY_BY_ID = {}
for category, ids in ASSIGNMENTS.items():
    for number in ids:
        assert number not in CATEGORY_BY_ID, f"Objective {number} has multiple assignments"
        CATEGORY_BY_ID[number] = category
assert set(CATEGORY_BY_ID) == set(GUIDES), (
    f"Assignments missing {sorted(set(GUIDES)-set(CATEGORY_BY_ID))}; "
    f"extra {sorted(set(CATEGORY_BY_ID)-set(GUIDES))}"
)

def section(text, heading, next_heading):
    if heading == "Official references":
        found = re.search(r"(?ms)^## Official references\n\n(.*?)(?=\n\n\[Domain index\]|\Z)", text)
        assert found, "Missing section Official references"
        return found.group(1).rstrip()
    pattern = rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## {re.escape(next_heading)}\n|\Z)"
    found = re.search(pattern, text)
    assert found, f"Missing section {heading}"
    return found.group(1).rstrip()

SAMPLES = {category: GUIDES[number][1] for category, number in EXEMPLARS.items()}
SAMPLES["architecture-choice"] = """# Architecture decision reference

## What

Managed-service, single/multi-cluster, regional, node-pool, and active/active/passive choices distribute responsibilities and failure domains differently. Select a model from isolation, compliance, operational capability, workload dependencies, recovery objectives, and cost.

## Why

More clusters can isolate failure but increase upgrade, policy, identity, telemetry, support, and cost overhead. A managed control plane reduces selected operations; it does not automatically transfer responsibility for workload behavior, identity, policy, storage data, backup, monitoring, capacity, or incident readiness. Exact boundaries are provider-specific.

## How

Map tenancy and workload requirements; name provider and customer owners; quantify steady-state and failover capacity; record identity, DNS, network, and data dependencies; compare alternatives against RTO/RPO, compliance, operational effort, and total cost; rehearse failover and failback before production.

**Objective-specific architect checkpoint:** State the assumptions and constraints, show the failure-domain and dependency diagram, identify who operates each layer, and demonstrate evidence that the recovery and cost model works under the selected failure scenario.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm the active context before changes; provider lifecycle and recovery procedures are environment-specific.

## Features

Managed-control-plane and managed-node models; single- and multi-cluster layouts; regions and failure domains; node pools; workload isolation; active/active and active/passive patterns; capacity and cost planning; standardization/flexibility decisions.

## Code snippets (if any)

```text
Decision record:
  requirements | constraints | options | rejected alternatives
  provider/customer owners per control plane, nodes, IAM, network, storage
  data consistency | identity/DNS dependencies | steady/failover capacity
  RTO/RPO | cost model | failover/failback evidence
```

This is an architecture prompt, not a provider guarantee or a deployable Kubernetes manifest.

## Do's and Don'ts

**Do**
- Document shared responsibility, failure modes, data consistency, recovery objectives, failover triggers, and full cost.
- Include identity, DNS, network, storage, observability, and operational capability in cluster-count decisions.

**Don't**
- Do not call multi-cluster a DR solution without tested data recovery, capacity, identity/DNS dependencies, and failback ownership.
- Do not assume managed control planes operate application security, policy, backup, monitoring, or workload recovery for the customer.

## Real life implementation

An architect compares one multi-zone cluster with regional failover clusters for a regulated workload. The record covers provider-managed control-plane scope, data replication semantics, identity and DNS, duplicated failover capacity, recovery drills, service ownership, and the ongoing cost of operating both regions.

## Q&A

**Q: Does multi-cluster automatically improve availability?** No; it adds independent control planes and cross-cluster dependencies. **Q: Who owns application security in a managed cluster?** The customer/platform retains workload and configuration duties; exact control-plane and node responsibilities are provider-specific. **Q: Is active/active always preferable?** No; consistency, conflict handling, and operational complexity may favor active/passive.

## Official references

- [Kubernetes production environment](https://kubernetes.io/docs/setup/production-environment/)
- [Kubernetes architecture](https://kubernetes.io/docs/concepts/architecture/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
"""
SAMPLES["service"] = """# Service and traffic-routing reference

## What

A Service provides a stable virtual access point and selects ready backends; EndpointSlices represent those backend addresses. Service types express internal or external exposure, while Ingress and Gateway APIs express routing intent. The actual dataplane and external load balancer require a cluster/provider integration or controller.

## Why

Stable service identities decouple clients from replaceable Pod IPs. Incorrect selectors, ports, readiness, DNS, or controller ownership can leave apparently valid resources unreachable. External exposure adds TLS, access-control, threat-model, and cost considerations.

## How

Compare Service selectors and ports with Pod labels and container ports; inspect ready EndpointSlices; test DNS and connectivity from the caller's network context. For Ingress or Gateway routes, verify controller class, API version, status, TLS, allowed route attachment, and backend health. Check provider ownership for external load balancers.

**Objective-specific architect checkpoint:** Follow a request from client DNS through the selected exposure controller and Service to a ready EndpointSlice and Pod; name which team owns each hop and its health signal.

**Safe practice:** use read-only inspection first and a reserved test hostname/namespace. Validate provider/controller behavior before exposure changes.

## Features

ClusterIP, NodePort, LoadBalancer, ExternalName, and headless Services; label selectors; ports and targetPorts; EndpointSlices; Ingress resources with controller-specific behavior; Gateway API resources with controller-specific conformance and features.

## Code snippets (if any)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
  namespace: app
spec:
  selector: {app: api}
  ports:
  - name: http
    port: 80
    targetPort: http
  type: ClusterIP
```

The selector must match ready Pod labels; named target ports must exist. External Service and route behavior depends on the selected implementation.

## Do's and Don'ts

**Do**
- Verify selectors, named ports, EndpointSlice readiness, route status, controller health, TLS, and external exposure ownership.
- Use explicit route/controller classes and account for load-balancer cost, source-IP handling, and policy boundaries.

**Don't**
- Do not confuse `port`, `targetPort`, and `nodePort`, or assume that an Ingress/Gateway resource creates a dataplane.
- Do not expose internal services publicly without threat-model and access-control review.

## Real life implementation

An internal API uses ClusterIP and cluster DNS; an approved Gateway controller handles public HTTP listeners. The platform team owns GatewayClass/Gateway configuration and the application team owns permitted routes. SRE checks controller status, listener/route conditions, Service endpoints, and application health independently.

## Q&A

**Q: Why does a Service have no backends?** A selector/label mismatch, incorrect port mapping, or unready Pods are common causes; inspect EndpointSlices. **Q: Is LoadBalancer behavior identical everywhere?** No; cloud/distribution integration and lifecycle differ. **Q: Does Gateway API include its own data plane?** No; a compatible controller implements it.

## Official references

- [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
- [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Kubernetes Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
"""

def checkpoint(number, objective, category):
    t = objective.lower()
    # Most specific matches first; no generic keyword may shadow a more
    # particular design concern (e.g., NetworkPolicy vs admission policy).
    rules = [
        (("declarative orchestration",), "Trace a declarative change from a reviewed manifest through API persistence and controller reconciliation to observed state; compare the desired state with actual state and explain how failed replicas are recovered."),
        (("control plane vs worker", "control plane topology and ha design"), "Draw the control-plane/worker boundary and supported failure domains; distinguish quorum/API availability from workload capacity, then state what redundancy and recovery each layer requires."),
        (("kube-apiserver", "kube-scheduler", "kube-controller-manager"), "For each named component, identify its contract, dependency, observable failure signal, and operating owner; do not infer a component failure from a workload symptom alone."),
        (("api server role",), "Trace an API request through authentication, authorization, admission, persistence, and reconciliation; identify which stage failed rather than treating the API server as the whole control plane."),
        (("etcd",), "Define a version-matched etcd snapshot/restore procedure, key protection, retention, isolated restore drill, and RTO/RPO; back up application volumes and external dependencies separately."),
        (("cri, cni, and csi", "container runtime interface", "network plugins (cni)", "storage drivers (csi)"), "Keep the extension contracts distinct: CRI starts containers, CNI connects Pods, and CSI provisions/attaches storage. Record the actual implementation, version, lifecycle, and upgrade owner for each."),
        (("kube-proxy",), "Verify the deployed Service dataplane: kube-proxy may provide forwarding, while some network implementations replace it. Confirm mode, observability, failure behavior, and upgrade support with the distribution/CNI owner."),
        (("managed control plane responsibilities", "managed control plane responsibility", "managed vs self-managed"), "Create a responsibility matrix for control plane, nodes, patching, identity, networking, storage, backup, workload security, observability, and incident response; verify it against the specific provider contract."),
        (("node lifecycle", "node conditions", "taints"), "Inspect node conditions, labels, taints, workload placement, and local data; validate replacement capacity and the exact drain sequence before node maintenance."),
        (("namespaces",), "Pair namespace scope with RBAC, quotas, admission policy, and CNI-enforced network policy; namespaces are useful administrative boundaries but not hard isolation by themselves."),
        (("api groups", "api versions", "kubectl fundamentals", "kubectl get", "kubectl with context", "kubectl troubleshooting tools"), "Discover the served resource and scope, confirm the target context, use `kubectl explain`, server-side dry-run and diff, and validate structured output without exposing credentials."),
        (("multi-container", "init containers", "sidecars"), "Keep helpers in one Pod only when shared lifecycle/network is intentional; use init containers for ordered setup and budget sidecar resources and termination behavior."),
        (("replicaset, deployment", "statefulset, daemonset", "daemonset behavior", "job and cronjob"), "Select the controller from the run contract: interchangeable replicas, stable identity, per-node coverage, or bounded/scheduled completion; test controller recovery and cleanup."),
        (("rollout", "revision history", "canaries", "release gating"), "Define readiness, traffic, SLO, and rollback gates. A Deployment template rollback cannot reverse schema changes, data writes, or other external side effects."),
        (("statefulset", "stable network identities"), "Pair StatefulSet ordinals with headless-Service discovery and per-replica claims; validate storage topology, ordered rollout, and restore independently from stable identity."),
        (("job", "cronjob", "parallelism", "completions", "backoff limits", "retries"), "Specify idempotency, success/completion semantics, parallelism, deadlines, retry/backoff, concurrency policy, and cleanup for interrupted or duplicate execution."),
        (("labels, selectors, and annotations",), "Treat labels/selectors as contracts used by controllers, Services, policy, and automation. Keep selectors intentional and stable; annotations are not a secret store."),
        (("readiness", "liveness", "startup"), "Use readiness to control traffic, liveness to recover a stuck process, and startup to protect slow initialization; tune thresholds to measured behavior and test dependency failures."),
        (("crashloopbackoff", "imagepullbackoff", "oomkilled", "pending", "failed", "evicted"), "Correlate events, previous-container logs, scheduling constraints, registry authentication, resource pressure, and eviction signals before changing a workload."),
        (("pod disruption", "poddisruptionbudget", "pdb", "disruption budgets", "drain", "cordon", "uncordon"), "Check healthy replicas, PDB allowance, local data, and replacement capacity. PDBs constrain voluntary eviction; they do not prevent involuntary failure."),
        (("configmap", "environment variables", "mounted files", "secret usage", "secret types", "image pull secret", "registry access", "secret objects"), "Choose env versus mounted-file delivery based on reload and exposure behavior; separate non-secret config, least-privileged credentials, at-rest protection, rotation, and external-store ownership."),
        (("admission", "policy engines", "policy-as-code", "security baseline", "image policy"), "Test allowed and denied objects using server-side dry-run and controlled policy tests; identify the actual enforcing admission/webhook/controller and its failure mode."),
        (("encryption at rest",), "Review API-data encryption, key custody, key rotation/recovery, backups, and application-level secret handling as distinct controls."),
        (("requests and limits", "qos classes", "resourcequota", "limitrange"), "Use measured requests/limits and leave system/disruption headroom; understand quota as an allocation guardrail rather than capacity and diagnose throttling/OOM behavior from evidence."),
        (("priority classes", "preemption", "scheduling flow", "affinity", "topology spread", "nodeSelector"), "Trace feasibility and scoring constraints; distinguish hard requirements from preferences, verify failure-domain labels/capacity, and state the impact of preemption and autoscaler lag."),
        (("horizontalpodautoscaler", "hpa", "vpa", "cluster autoscaler", "autoscaling"), "Validate requests, metric availability/freshness, target, min/max and stabilization, downstream limits, scale-up delay, scale-in safety, and provider-specific node provisioning."),
        (("networkpolicy enforcement depends", "networkpolicy as a kubernetes api", "network policy enforcement"), "Identify the CNI/plugin and version, confirm its NetworkPolicy capabilities, and test both permitted and denied flows. API-object presence alone is not evidence of enforcement."),
        (("ingress api", "ingress controller", "ingress/gateway", "gateway api", "gatewayclass", "httproute", "grpcroute"), "Name the installed Ingress/Gateway controller, served API version, owner/route attachment and supported features; an API object alone does not implement TLS or traffic forwarding."),
        (("cni plugins", "service proxy behavior", "network model", "pod ip", "service ip", "cni"), "Map Pod/Service/node/external traffic paths and verify the actual CNI/service dataplane, IPAM, MTU, policy, egress, and provider route limits."),
        (("coredns", "cluster dns", "dns failures", "dns awareness"), "Test FQDN resolution from the caller namespace, then separately verify Service selectors, EndpointSlices, routing, and policy; a DNS answer is not proof of reachability."),
        (("service reachability", "dns, service", "network debugging", "backend outage", "service mesh"), "Isolate DNS, Service selector/EndpointSlice, dataplane route, policy, controller, and backend health as separate hops; compare service-mesh overhead with the actual routing requirement."),
        (("volumes", "persistent volumes", "storage class", "csi", "snapshot", "storage architecture", "stateful workloads"), "Verify PVC/PV lifecycle, CSI support, topology, access/reclaim semantics, expansion and snapshot behavior; test application-consistent backup restore to the required RTO/RPO."),
        (("authentication", "authorization", "rbac", "service account", "workload identity", "security architecture", "audit logging", "runtime security", "cluster-level security"), "Separate caller identity, RBAC authorization, admission, Pod runtime controls, network boundaries, and audit. Enforce least privilege and validate each control independently."),
        (("self-managed cluster lifecycle", "kubeadm", "version skew", "upgrade sequencing", "cluster lifecycle"), "Use the matching distribution/version procedure; verify backups, API deprecations, add-on/CNI/CSI compatibility, capacity, skew rules, staged node replacement, and recovery gates."),
        (("control plane ha", "multi-control-plane", "control plane topology"), "Distinguish control-plane quorum/API availability from worker count and workload redundancy; design independent failure-domain, load-balancer, and etcd recovery paths."),
        (("metrics, logs", "observability", "slo", "sli", "error budget", "alert", "cluster-level logs"), "Correlate user-facing SLI/SLO, events, component/node telemetry, and application logs/traces; define alert ownership, runbook, retention, and actionable recovery criteria."),
        (("gitops does not eliminate",), "Define GitOps field/source ownership, then independently scope controller RBAC, policy enforcement, secret delivery, and application/cluster observability; reconciliation does not provide these controls by itself."),
        (("helm", "kustomize", "gitops", "crd", "operator", "golden path", "developer experience"), "Define one source-of-truth and controller owner; pin/chart or overlay versions, review rendered manifests, sequence CRD/controller upgrades, and observe reconciliation separately from app health."),
        (("managed kubernetes operating models", "managed control plane", "cloud-managed", "active/active", "active/passive", "multi-cluster", "multi-region", "cost drivers", "node pools", "platform standardization", "regional failover"), "Record provider/customer boundary, failure domains, identity and data dependencies, steady/failover capacity, total cost, RTO/RPO, tested failover, and failback ownership."),
        (("chaos/dr rehearsal",), "Design a bounded, approved failure exercise with hypothesis, blast radius, stop conditions, telemetry, comms owner, recovery steps, and a follow-up action; start in isolated/non-production scope."),
        (("ci/cd integration",), "Build and test once, promote an immutable digest with provenance, validate rendered manifests and policy, deploy using scoped short-lived identity, and gate promotion on rollout status and application SLOs."),
        (("developer experience", "golden paths"), "Provide a supported template with owner, version/upgrade contract, security and telemetry defaults, exception route, documentation, and adoption/support measures."),
        (("network architecture",), "Make Pod/service CIDRs, CNI, routing/MTU, DNS, policy enforcement, ingress/gateway ownership, failure domains, and cloud network integration explicit in the design."),
        (("storage architecture",), "Compare CSI/backend choices on durability, latency, throughput, topology, attachment semantics, backup consistency, restore objective, and cost; validate with workload tests."),
        (("platform design",), "Choose abstractions only for stable supported contracts; preserve API transparency and define ownership, security, upgrade, documentation, and exception paths."),
        (("distinguish core kubernetes apis",), "For each capability, record core API, implementation/controller/plugin, supported version, owner, failure mode, upgrade path, and test evidence; do not infer behavior from resource discovery."),
        (("do not assume managed kubernetes", "vendor-specific responsibilities"), "Create and review a provider-specific responsibility matrix spanning control plane, nodes, identity, network, storage, backup, policy, monitoring, capacity, and incident readiness."),
        (("kubernetes as a platform control plane",), "Threat-model workload identity, least privilege, admission, image integrity, CNI-enforced network controls, data protection, observability, and incident operations as separate controls."),
    ]
    for needles, result in rules:
        if any(needle in t for needle in needles):
            return result
    return {
        "architecture": "State the desired-state contract, control/data-plane boundary, failure modes, health evidence, owner, and recovery path for this architecture objective.",
        "api": "Verify resource kind, API group/version, scope, context and authorization; validate with discovery, explain, server-side dry-run, and a reviewed diff.",
        "workloads": "Identify the workload's lifecycle, identity, retry, state, health, and replacement contract; choose a matching controller and test rescheduling.",
        "rollout": "Define rollout strategy, readiness and user-SLO gates, immutable artifact, rollback criteria, and any external state that a template rollback cannot reverse.",
        "probes": "Give readiness, liveness, and startup probes distinct purposes and tune thresholds from measured startup and failure behavior.",
        "config": "Specify value sensitivity, delivery mode, access scope, update/reload behavior, rotation, encryption, and source-of-truth.",
        "resources": "Size from measurements; account for requests, limits, QoS, node allocatable, quotas, and failure/disruption headroom.",
        "scheduling": "State hard versus preferred placement requirements, validate labels and capacity, and assess placement during a failure-domain loss.",
        "autoscaling": "Validate metric quality, requests, target/bounds, response delay, downstream limits, scale-in safety, and cost.",
        "disruption": "Check PDB allowance, healthy replicas, replacement capacity, local data, and whether the operation is voluntary or involuntary.",
        "network": "Map traffic and enforcement end to end; qualify CNI and service-dataplane capabilities and verify them on the target distribution.",
        "service": "Validate route/controller implementation, Service selectors and ports, ready EndpointSlices, exposure, TLS, and backend health.",
        "dns": "Test name resolution from the calling workload, then verify service endpoints and packet path separately.",
        "storage": "Validate driver capabilities, topology, persistence/reclaim, consistency, backup, and a measured restore.",
        "security": "Separate identity, authorization, admission, runtime, network and data controls; document least privilege and enforcement evidence.",
        "lifecycle": "Use the target distribution's documented bootstrap/upgrade/recovery sequence and verify skew, backup, capacity, and plugin compatibility.",
        "observability": "Correlate customer impact with events, logs, metrics, traces and SLOs; make alerts actionable and runbooks testable.",
        "extension": "Define extension/controller ownership, RBAC, versioning, reconciliation, upgrade/rollback, and observable health.",
        "architecture-choice": "Record requirements, alternatives, shared-responsibility boundaries, dependencies, capacity/cost, RTO/RPO, and tested failover.",
        "production": "Verify the core API contract, actual implementation, owner, version, failure behavior, upgrade path, and in-cluster evidence.",
    }[category]

def objective_snippet(number, objective, category):
    t = objective.lower()
    if number == 1:
        return """A declarative Deployment and stable Service illustrate intent, controller reconciliation, replica recovery, and service discovery:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: web, namespace: demo}
spec:
  replicas: 2
  selector:
    matchLabels: {app: web}
  template:
    metadata:
      labels: {app: web}
    spec:
      containers:
      - name: web
        image: nginx:1.27
        resources:
          requests: {cpu: 100m, memory: 64Mi}
---
apiVersion: v1
kind: Service
metadata: {name: web, namespace: demo}
spec:
  selector: {app: web}
  ports:
  - {port: 80, targetPort: 80}
```

In a disposable lab, observe state using `kubectl get deployment,pods,service,endpointslices -n demo`. Use an approved image; do not delete production Pods to test recovery."""
    if category == "architecture":
        if "cri" in t or "cni" in t or "csi" in t:
            return """```text
Contract   Responsibility                         Implementation owner
CRI        kubelet <-> container runtime           distribution/runtime provider
CNI        Pod network attachment/IPAM             selected network plugin/provider
CSI        volume provision/attach/mount           selected storage driver/provider
```

Verify installed implementations and support policy for the target distribution; names in the API do not identify the actual product/version."""
        return """```sh
kubectl cluster-info
kubectl get nodes -o wide
kubectl get --raw=/readyz
```

These are read-only cluster checks. For architecture/topology decisions, document control plane, worker, state-store, network, and failure-domain ownership; managed offerings may restrict component endpoints."""
    if category == "api":
        if "api groups" in t or "api versions" in t:
            return """```sh
kubectl api-resources --api-group=apps
kubectl explain deployment.spec.template.spec
kubectl get --raw=/apis/apps
```"""
        return """```sh
kubectl config current-context
kubectl config get-contexts
kubectl api-resources
kubectl apply --dry-run=server -f app.yaml
kubectl diff -f app.yaml
```"""
    if category == "workloads":
        if "multi-container" in t or "init container" in t or "sidecar" in t:
            return """```yaml
spec:
  initContainers:
  - name: prepare
    image: busybox:1.36
    command: ["sh", "-c", "echo prepare"]
  containers:
  - name: app
    image: nginx:1.27
    resources:
      requests: {cpu: 100m, memory: 64Mi}
```

This illustrates ordered init work; sidecar behavior and native sidecar support depend on Kubernetes version. Use approved images."""
        if "daemonset" in t:
            return """```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata: {name: node-agent, namespace: platform}
spec:
  selector:
    matchLabels: {app: node-agent}
  template:
    metadata:
      labels: {app: node-agent}
    spec:
      containers:
      - name: agent
        image: example.invalid/agent:approved
```

Add only the node access, tolerations, and privileges required by the agent."""
        if "job" in t or "cronjob" in t or "parallelism" in t or "retries" in t:
            return """```yaml
apiVersion: batch/v1
kind: Job
metadata: {name: batch, namespace: app}
spec:
  completions: 4
  parallelism: 2
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: task
        image: example.invalid/task@sha256:REPLACE_WITH_APPROVED_DIGEST
```

Make the task idempotent; configure deadline and cleanup for the actual job."""
        if "label" in t or "selector" in t or "annotation" in t:
            return """```yaml
spec:
  selector:
    matchLabels: {app: api}
  template:
    metadata:
      labels:
        app: api
        team: checkout
      annotations:
        example.invalid/change-ticket: CHG-123
```

The controller selector must match the template labels; annotations are metadata, not selectors or secret storage."""
        if "statefulset" in t or "stateful" in t:
            return """```yaml
spec:
  serviceName: database
  replicas: 3
  selector:
    matchLabels: {app: database}
  template:
    metadata:
      labels: {app: database}
    spec:
      containers:
      - name: database
        image: example.invalid/database:approved
        volumeMounts:
        - {name: data, mountPath: /var/lib/data}
  volumeClaimTemplates:
  - metadata: {name: data}
    spec:
      accessModes: [ReadWriteOnce]
      storageClassName: approved-storage
      resources:
        requests: {storage: 20Gi}
```

This fragment belongs under a StatefulSet `spec`; verify service discovery, CSI topology, and restore behavior."""
        if "rollout" in t or "deployment" in t:
            return """```sh
kubectl rollout status deployment/web -n app --timeout=120s
kubectl rollout history deployment/web -n app
kubectl rollout undo deployment/web -n app
```

Rollback restores a stored workload template; it does not undo external data changes."""
        return """```sh
kubectl get pods -n app -o wide
kubectl describe pod POD -n app
kubectl get rs,deploy,statefulset,daemonset,job,cronjob -n app
```"""
    if category == "rollout":
        return """```sh
kubectl diff -f rendered/
kubectl rollout status deployment/api -n app --timeout=120s
kubectl rollout history deployment/api -n app
kubectl rollout undo deployment/api -n app
```

Use immutable artifacts and independent health gates; template rollback cannot reverse schema/data changes."""
    if category == "probes":
        return """```yaml
startupProbe:
  httpGet: {path: /healthz, port: 8080}
  periodSeconds: 5
  failureThreshold: 30
readinessProbe:
  httpGet: {path: /ready, port: 8080}
  periodSeconds: 5
livenessProbe:
  httpGet: {path: /live, port: 8080}
  periodSeconds: 10
```

Tune timing from measured startup and failure behavior; keep probe endpoints cheap."""
    if category == "config":
        if "image pull" in t or "registry" in t:
            return """```yaml
spec:
  imagePullSecrets:
  - name: registry-credentials
  containers:
  - name: app
    image: registry.example.invalid/team/app@sha256:REPLACE_WITH_APPROVED_DIGEST
```

Create the referenced Secret through an approved credential workflow; do not put credentials in manifests or Git."""
        if "environment variable" in t or "mounted file" in t:
            return """```yaml
envFrom:
- configMapRef: {name: app-config}
volumeMounts:
- {name: runtime-config, mountPath: /etc/app, readOnly: true}
volumes:
- name: runtime-config
  configMap:
    name: app-config
```

Processes generally need an explicit reload/restart strategy after configuration changes."""
        if "secret" in t and ("encryption" in t or "complete secret" in t or "operational cautions" in t):
            return """```text
Secret review: source | RBAC readers | at-rest encryption/key owner
delivery method | rotation trigger | process reload | audit/retention
backup exposure | revocation | recovery owner
```

Do not print secret values to validate delivery; verify access through scoped identity and approved secret-provider telemetry."""
        return """```yaml
apiVersion: v1
kind: ConfigMap
metadata: {name: app-config, namespace: app}
data:
  LOG_LEVEL: info
```

Keep non-confidential settings in ConfigMaps; deliver credentials through an approved secret workflow."""
    if category == "resources":
        if "qos" in t:
            return """```sh
kubectl get pod POD -n app -o jsonpath='{.status.qosClass}{\"\\n\"}'
kubectl describe node NODE
kubectl get events -n app --sort-by=.lastTimestamp
```"""
        if "limitrange" in t or "resourcequota" in t:
            return """```yaml
apiVersion: v1
kind: ResourceQuota
metadata: {name: team-budget, namespace: app}
spec:
  hard:
    requests.cpu: "8"
    requests.memory: 16Gi
    pods: "40"
```

Set limits against measured tenant needs and allocatable cluster capacity."""
        return """```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    memory: 512Mi
```

Tune from workload measurements; CPU-limit choices need latency testing."""
    if category == "scheduling":
        if "priority" in t or "preemption" in t:
            return """```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata: {name: critical}
value: 100000
globalDefault: false
description: "Reserved for approved critical workloads"
```

Creation of PriorityClass is cluster-scoped; preemption policy and quota remain necessary."""
        if "affinity" in t or "nodeselector" in t or "taints" in t:
            return """```yaml
spec:
  nodeSelector:
    nodepool: workload
  tolerations:
  - key: dedicated
    operator: Equal
    value: workload
    effect: NoSchedule
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          topologyKey: topology.kubernetes.io/zone
          labelSelector:
            matchLabels: {app: api}
```

Verify node labels, taints, and actual zone capacity before applying."""
        return """```sh
kubectl describe pod POD -n app
kubectl get nodes --show-labels
kubectl get events -n app --sort-by=.lastTimestamp
```"""
    if category == "autoscaling":
        if "horizontalpodautoscaler" in t or "hpa" in t:
            return """```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: {name: api, namespace: app}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2
  maxReplicas: 12
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 65
```

The target needs resource requests and a working metrics source; test bounds and downstream capacity."""
        return """```text
Scaling review:
  workload signal and freshness | request sizing | min/max
  scale-up lag and startup time | node capacity/provisioner owner
  topology/quotas | downstream saturation limit | safe scale-in
  cost at steady state and failure-domain loss
```

HPA, VPA, and node autoscaling are different control loops; product behavior is environment-specific."""
    if category == "disruption":
        return """```sh
kubectl get pdb -A
kubectl get pods -A -o wide
kubectl get nodes
```

Drain only in an authorized maintenance window after checking PDB allowance, local data, and replacement capacity; do not blindly bypass blocked evictions."""
    if category == "network":
        if "networkpolicy" in t:
            return """```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: {name: allow-api-from-web, namespace: app}
spec:
  podSelector:
    matchLabels: {app: api}
  policyTypes: [Ingress]
  ingress:
  - from:
    - podSelector:
        matchLabels: {app: web}
    ports:
    - {protocol: TCP, port: 8080}
```

This policy has effect only if the selected CNI enforces NetworkPolicy. Test both allowed and denied flows in a lab."""
        if "kube-proxy" in t:
            return """```sh
kubectl -n kube-system get daemonsets,pods -o wide
kubectl get svc,endpointslices -A
```

Some implementations replace kube-proxy; verify the chosen CNI/service dataplane and its supported diagnostics."""
        if "service mesh" in t:
            return """```text
Decision factors: required L7 policy/identity/telemetry | simpler
Service/Gateway capability | latency/resource overhead | upgrades
failure modes | operator ownership | migration/rollback plan
```"""
        if "architecture" in t:
            return """```text
Pod CIDR / Service CIDR | IPAM | CNI + version | routes/MTU
NetworkPolicy semantics | service dataplane | DNS/egress
failure domains | cloud route limits | upgrade and rollback owner
```"""
        return """```sh
kubectl get pods -A -o wide
kubectl get svc,endpointslices,networkpolicy -A
kubectl get nodes -o wide
```

Discovery is not proof of policy enforcement or dataplane health; verify from a workload's network context."""
    if category == "service":
        if "endpointslice" in t:
            return """```sh
kubectl get svc api -n app -o yaml
kubectl get endpointslices -n app -l kubernetes.io/service-name=api -o wide
kubectl describe endpointslice -n app
```"""
        if "gatewayclass" in t or "httproute" in t or "grpcroute" in t or "gateway api" in t:
            return """```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata: {name: app, namespace: app}
spec:
  parentRefs:
  - name: shared-gateway
  hostnames: [\"app.example.invalid\"]
  rules:
  - backendRefs:
    - name: web
      port: 80
```

Requires a compatible Gateway API controller and an existing Gateway/listener that permits route attachment."""
        if "ingress" in t:
            return """```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata: {name: web, namespace: app}
spec:
  ingressClassName: approved-controller
  rules:
  - host: app.example.invalid
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port: {number: 80}
```

An installed controller is required; TLS and controller-specific behavior must be configured and tested."""
        if "service types" in t or "clusterip" in t:
            return """```text
ClusterIP    internal virtual Service address
NodePort     node-address port exposure
LoadBalancer provider/controller integrated external exposure
ExternalName DNS alias; does not proxy traffic
Headless     no ClusterIP; DNS can return endpoint addresses
```

Validate exact exposure and lifecycle behavior with the selected cluster/provider."""
        return """```yaml
apiVersion: v1
kind: Service
metadata: {name: api, namespace: app}
spec:
  selector: {app: api}
  ports:
  - name: http
    port: 80
    targetPort: http
  type: ClusterIP
```

The selector must match ready Pod labels; external routing needs its own implementation."""
    if category == "dns":
        return """```sh
kubectl get svc,endpointslices -n app
kubectl get pods -n kube-system -o wide
# In an approved diagnostic Pod:
nslookup api.app.svc.cluster.local
```"""
    if category == "storage":
        if "volume types" in t or "emptydir" in t or "hostpath" in t:
            return """```yaml
volumes:
- name: scratch
  emptyDir: {}
- name: settings
  configMap:
    name: app-config
containers:
- name: app
  image: example.invalid/app:approved
  volumeMounts:
  - {name: scratch, mountPath: /tmp/work}
  - {name: settings, mountPath: /etc/app, readOnly: true}
```

`hostPath` is node-coupled and privileged-risk; use only when explicitly required and governed."""
        if "statefulset" in t or "stable identity" in t:
            return """```text
Stateful workload design:
  stable ordinal identity | headless Service/DNS
  per-replica PVC and CSI topology | reclaim/retention policy
  application consistency | tested backup, restore, and failover
```"""
        if "access modes" in t or "reclaim" in t:
            return """```sh
kubectl get pv,pvc -A
kubectl get storageclass
kubectl describe pvc CLAIM -n app
kubectl get csidrivers
```

Reclaim policy belongs to the PV/StorageClass provisioning behavior; inspect before deleting claims."""
        if "snapshot" in t or "backup" in t or "restore" in t:
            return """```text
Restore test record:
  source snapshot/backup and integrity check
  CSI/backend/version and consistency guarantee
  encryption keys and credentials
  isolated target and dependency restore order
  measured RPO/RTO | application validation | cleanup
```

Snapshot API and application-consistency support are driver/backend specific."""
        if "choose between" in t or "architecture" in t or "align storage" in t:
            return """```text
Compare storage options by: durability | latency/IOPS | topology
attachment/access semantics | failure domain | backup/restore
expansion/snapshot support | portability | cost | owner
```"""
        return """```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: data, namespace: app}
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: approved-storage
  resources:
    requests: {storage: 20Gi}
```

StorageClass, CSI driver, access semantics, and snapshots are implementation-specific."""
    if category == "security":
        if "rbac" in t or "roles" in t:
            return """```sh
kubectl auth can-i list pods -n app --as=system:serviceaccount:app:reader
kubectl get role,rolebinding -n app
```

Use authorized impersonation and verify effective permissions before granting access."""
        if "service account" in t or "workload identity" in t:
            return """```yaml
apiVersion: v1
kind: ServiceAccount
metadata: {name: app, namespace: app}
automountServiceAccountToken: false
```

Enable token or cloud workload identity only when needed and follow the provider's identity integration guidance."""
        if "pod security" in t or "securitycontext" in t or "privilege boundaries" in t:
            return """```yaml
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: example.invalid/app:approved
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [\"ALL\"]
```

Validate compatibility with the workload and cluster Pod Security policy."""
        if "admission" in t or "policy" in t:
            return """```sh
kubectl apply --dry-run=server -f representative-workload.yaml
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations
```

Dry-run support depends on webhook side-effect declarations; test policy failure modes and availability."""
        if "secret" in t or "encryption" in t:
            return """```text
Secret control review:
  authorized readers | encryption/key owner | delivery/rotation
  audit events | backup exposure | application reload/revocation
```

Never print secret payloads for validation; verify controls through approved audit and provider telemetry."""
        if "image" in t or "supply" in t or "artifact" in t or "provenance" in t:
            return """```yaml
containers:
- name: app
  image: registry.example.invalid/team/app@sha256:REPLACE_WITH_APPROVED_DIGEST
```

Enforce registry, signature/provenance, vulnerability, and promotion policy in the trusted build/admission path."""
        if "audit" in t:
            return """```text
Audit review: identity | verb | resource/scope | timestamp
source/context | decision | correlated change/incident
retention/access | alert/runbook
```

Audit backend and managed control-plane visibility depend on the distribution/provider."""
        if "seccomp" in t or "apparmor" in t or "runtimeclass" in t:
            return """```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault
```

Runtime profile support and enforcement depend on node OS/runtime configuration."""
        return """```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata: {name: pod-reader, namespace: app}
rules:
- apiGroups: [\"\"]
  resources: [\"pods\"]
  verbs: [\"get\", \"list\", \"watch\"]
```

Grant only the verbs/resources and scope the identity actually needs."""
    if category == "lifecycle":
        if "etcd" in t:
            return """```text
Recovery runbook:
  Kubernetes/etcd version and supported topology
  snapshot location/integrity | encryption keys
  isolated restore steps | API/object validation
  separate PV/application-data recovery | measured RTO/RPO
```

Use the exact version-matched etcd procedure; do not experiment against a production endpoint."""
        if "kubeadm" in t:
            return """```sh
# On an authorized kubeadm lab/control-plane host:
kubeadm upgrade plan
```

This is a preflight planning command, not a substitute for the version-specific upgrade sequence."""
        if "version skew" in t or "upgrade" in t:
            return """```sh
kubectl version
kubectl get nodes -o wide
```

Compare every component and add-on to the official version-skew and distribution upgrade policy."""
        return """```sh
kubectl get nodes -o wide
kubectl describe node NODE
kubectl get pods -A --field-selector spec.nodeName=NODE
```

These checks are read-only; perform lifecycle changes only through the supported distribution/provider runbook."""
    if category == "observability":
        if "slo" in t or "sli" in t or "error budget" in t:
            return """```text
SLI: successful valid requests / total valid requests
SLO: target fraction over a defined rolling window
Alert: fast/slow error-budget burn with owner and runbook
```

Choose user-visible indicators and thresholds from service requirements."""
        if "node" in t or "kubelet" in t:
            return """```sh
kubectl describe node NODE
kubectl get pods -A -o wide --field-selector spec.nodeName=NODE
kubectl get events -A --sort-by=.lastTimestamp
```

Host/runtime logs and managed control-plane telemetry require distribution/provider-approved access."""
        if "control plane" in t:
            return """```sh
kubectl get --raw=/readyz?verbose
kubectl get events -A --sort-by=.lastTimestamp
kubectl get nodes -o wide
```

Control-plane endpoints and component logs may be restricted in managed clusters."""
        if "alert" in t or "runbook" in t or "incident" in t or "chaos" in t or "dr rehearsal" in t:
            return """```text
Incident/experiment: impact and hypothesis | blast radius
owner/comms channel | stop conditions | telemetry to capture
mitigation and recovery | verification | review/action owner
```

Run failure exercises only with authorization, bounded scope, and a tested stop/recovery plan."""
        if "metrics-server" in t or "prometheus" in t or "opentelemetry" in t:
            return """```text
Signal pipeline: source -> collector/exporter -> backend
  -> dashboard/alert -> owner/runbook
Record sampling | cardinality | retention | access | cost
```

Prometheus/Grafana/Loki/OpenTelemetry are ecosystem components; provision and support them explicitly."""
        if "cluster-level logs" in t:
            return """```text
Platform logs: API/node/runtime/control-plane evidence
Application telemetry: request, dependency, business and trace context
Correlate with: workload identity | namespace | version | timestamps
```

Access and retention boundaries should follow data classification."""
        return """```sh
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod POD -n NAMESPACE
kubectl logs POD -n NAMESPACE --all-containers --since=15m
kubectl top nodes
```

`top` requires a compatible metrics source; pod/application logs do not replace control-plane telemetry."""
    if category == "extension":
        if "custom resource" in t or "crd" in t or "operator" in t:
            return """```text
Extension review:
  versioned CRD schema | served/storage versions | controller owner
  RBAC scope | reconciliation/status conditions | upgrade/rollback
  deletion/finalizers | availability | backup/migration
```

A CRD defines an API; a controller/operator provides behavior."""
        if "gitops" in t:
            return """```text
GitOps reconciliation contract:
  source/revision | target cluster/namespace | field owner
  sync/prune policy | scoped credentials | health conditions
  drift/override policy | secret source | rollback/recovery
```

Sync status does not prove application SLO health."""
        if "kustomize" in t:
            return """```sh
kubectl kustomize overlays/staging
kubectl apply --dry-run=server -k overlays/staging
```

Inspect rendered output and validate target API/policy before deployment."""
        if "helm" in t:
            return """```sh
helm template app ./chart -f values-staging.yaml
helm lint ./chart
```

Review rendered output and pin chart/dependency versions before promotion."""
        return """```text
Platform product contract:
  supported API/template | owner | security defaults | upgrade policy
  telemetry/runbook | documentation | exception path | adoption measure
```

This is a design checklist, not an applied resource."""
    if category == "architecture-choice":
        return """```text
Decision record:
  requirements | constraints | alternatives | failure domains
  provider/customer owner per layer | identity/DNS/data dependencies
  steady/failover capacity | cost | RTO/RPO | tested failover/failback
```

This is an architecture artifact, not a provider guarantee."""
    if category == "production":
        return """```sh
kubectl get networkpolicy -A
kubectl get ingress,gateway,httproute -A
kubectl get csidrivers
```

API discovery is not evidence of controller conformance, CNI enforcement, driver support, or provider service-level guarantees."""
    return """```text
Objective evidence: implementation/version | owner | assumptions
healthy-state signal | failure test | rollback/recovery | reviewer
```

Use read-only inspection or a disposable environment before any mutation."""

def replace_section(text, heading, content):
    pattern = rf"(?ms)(^## {re.escape(heading)}\n\n).*?(?=^## |\Z)"
    result, count = re.subn(pattern, lambda m: m.group(1) + content.rstrip() + "\n\n", text, count=1)
    assert count == 1, f"Cannot replace section {heading}"
    return result

role_labels = {
    "Core": "Core operators; DevOps; SRE; Platform; Architect",
    "DevOps": "DevOps; delivery/platform teams",
    "SRE": "SRE; operations/platform teams",
    "Platform": "Platform; security; developer-experience teams",
    "Architect": "Architect; platform leadership; SRE",
    "Optional": "Optional specialist competency; validate local need",
}

for number, (path, old_text) in GUIDES.items():
    objective = re.search(r"^> (.+)$", old_text, re.M).group(1)
    role = re.search(r"\[([^\]]+)\]\s*$", objective)
    role = role.group(1) if role else "Role track"
    category = CATEGORY_BY_ID[number]
    sample = SAMPLES[category]
    new_text = old_text
    for heading, next_heading in [
        ("What", "Why"), ("Why", "How"), ("How", "Features"),
        ("Features", "Code snippets (if any)"),
        ("Code snippets (if any)", "Do's and Don'ts"),
        ("Do's and Don'ts", "Real life implementation"),
        ("Real life implementation", "Q&A"), ("Q&A", "CKA alignment (separate from the role syllabus)"),
    ]:
        content = section(sample, heading, next_heading)
        new_text = replace_section(new_text, heading, content)
    new_text = replace_section(
        new_text, "Code snippets (if any)",
        objective_snippet(number, objective, category),
    )
    refs = section(sample, "Official references", "Domain index")
    new_text = replace_section(new_text, "Official references", refs)
    new_text = new_text.rstrip() + "\n\n[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)\n"
    # Update the copied role lens and exemplar-specific checkpoint.
    new_text = re.sub(
        r"(?m)^\*\*Role lens:\*\* .*?$",
        f"**Role lens:** {role_labels.get(role, 'Role-oriented competency')} should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.",
        new_text,
    )
    focus_text = checkpoint(number, objective, category)
    new_text = re.sub(r"(?m)^\*\*Objective-specific architect checkpoint:\*\* .*?$",
                      f"**Objective-specific architect checkpoint:** {focus_text}", new_text)
    path.write_text(new_text, encoding="utf-8", newline="\n")

# A dedicated, non-archetypal guide for Kubernetes' core value proposition. Its
# former network-focused content was the original audit finding.
p001, text001 = GUIDES[1]
text001 = replace_section(text001, "What", """Kubernetes is a declarative orchestration system: operators submit desired objects through the API, and controllers repeatedly reconcile observed state toward that specification. This model supports workload placement, replacement after failures, horizontal replica changes, and stable service discovery; it does not make an application stateless or recover deleted data automatically.

The key design distinction is desired state versus observed state. A Deployment expresses replica intent, a controller creates/updates ReplicaSets and Pods, and a Service provides a stable discovery target for selected ready backends.""")
text001 = replace_section(text001, "Why", """Declarative reconciliation makes operations repeatable and enables the platform to correct many forms of drift and transient failure without imperative per-node scripts. It gives teams a consistent API for scheduling and service discovery across nodes and distributions.

The boundary matters: controller self-healing can recreate a Pod, but durable data, application correctness, dependency health, and regional disaster recovery require separate design. Scaling replicas also helps only when the workload and its dependencies can scale.""")
text001 = replace_section(text001, "How", """Describe the desired workload in version-controlled manifests; submit it through the API; observe controller reconciliation, Pod scheduling/readiness, and Service endpoints. Use declarative apply/diff workflows, define health probes and resource requests, and verify both recovery and scale behavior under a controlled lab failure.

**Objective-specific architect checkpoint:** Demonstrate one desired-state change, observe reconciliation to ready Pods and Service discovery, then remove one disposable replica and show controller replacement. Explain what would not self-heal (for example, corrupted external data or a failed dependency).""")
text001 = replace_section(text001, "Features", """Declarative API objects; reconciliation loops; controller-managed workload lifecycle; self-healing by replacement/restart within policy; replica scaling; stable Service discovery independent of Pod IPs; labels/selectors for grouping and routing.

These are platform mechanisms, not application-level correctness guarantees. Actual networking and service forwarding still depend on the selected distribution and network implementation.""")
text001 = replace_section(text001, "Code snippets (if any)", """A minimal declarative example ties replica intent to a stable service selector:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: demo
spec:
  replicas: 2
  selector:
    matchLabels: {app: web}
  template:
    metadata:
      labels: {app: web}
    spec:
      containers:
      - name: web
        image: nginx:1.27
        resources:
          requests: {cpu: 100m, memory: 64Mi}
---
apiVersion: v1
kind: Service
metadata:
  name: web
  namespace: demo
spec:
  selector: {app: web}
  ports:
  - port: 80
    targetPort: 80
```

Safe disposable-lab observation:

```sh
kubectl get deployment,pods,service,endpointslices -n demo
kubectl describe deployment web -n demo
```

Use an approved image and test namespace; do not delete production Pods to demonstrate self-healing.""")
text001 = replace_section(text001, "Do's and Don'ts", """**Do**
- Keep desired manifests in reviewed version control and observe reconciliation, rollout conditions, and ready endpoints.
- Design replicas, requests, probes, disruption policy, and dependency capacity together; rehearse recovery in a disposable cluster.

**Don't**
- Do not equate Pod replacement with recovery of persistent or external application data.
- Do not assume more replicas solve a stateful bottleneck, application bug, or unhealthy shared dependency.
- Do not infer a working dataplane merely from creation of a Service object.""")
text001 = replace_section(text001, "Real life implementation", """A stateless API is described by a Deployment with multiple replicas and readiness probes, and exposed through a ClusterIP Service. A node or container failure causes reconciliation to replace the Pod; the Service continues to provide a stable name while ready endpoints change. The team separately monitors the API SLO and protects database state with its own backup/restore strategy.""")
text001 = replace_section(text001, "Q&A", """**Q: What is declarative about Kubernetes?** The client records a desired object; controllers continuously compare actual state with that intent and reconcile differences. **Q: Does self-healing recover persistent data?** No; it can replace or restart workloads, but data recovery needs storage/application backup design. **Q: How does service discovery avoid Pod IP coupling?** Clients use Service identity and selectors rather than tracking ephemeral Pod addresses.""")
p001.write_text(text001, encoding="utf-8", newline="\n")

# CI/CD is a distinct DevOps competency; add the delivery-specific operational
# material instead of leaving it under generic Pod-controller teaching.
p124, text124 = GUIDES[124]
text124 = replace_section(text124, "What", """A Kubernetes CI/CD integration connects source changes to tested artifacts and controlled cluster reconciliation. CI builds, tests, scans, and publishes an artifact; delivery promotes that same immutable artifact and applies approved manifests through a deployment identity or a GitOps controller. Kubernetes defines APIs and rollout status, not a mandated pipeline.""")
text124 = replace_section(text124, "Why", """Separating artifact production from environment promotion improves provenance, repeatability, rollback, and auditability. Pipelines are privileged cluster actors; a compromised or over-broad runner can alter workloads or exfiltrate secrets.""")
text124 = replace_section(text124, "How", """Build and test once; publish an immutable image digest with provenance; render manifests and validate schema/policy; obtain required approvals; deploy with namespace-scoped short-lived identity or a scoped GitOps controller; then gate promotion on rollout status and application SLOs. Keep environment configuration separate and define rollback/data-migration limits.

**Objective-specific architect checkpoint:** Draw the artifact and permission path from commit to production, identify who can build, approve, deploy, and reconcile, and show how a failed health gate stops promotion without granting CI cluster-admin.""")
text124 = replace_section(text124, "Features", """Build/test/scan stages; image registry and immutable digests; manifest rendering and server-side validation; provenance/attestation; promotion gates; short-lived workload identity; deployment or GitOps reconciliation; rollout and SLO verification.""")
text124 = replace_section(text124, "Code snippets (if any)", """Read-only/reviewable deployment checks after a controlled pipeline apply:

```sh
kubectl config current-context
kubectl apply --dry-run=server -f rendered/
kubectl diff -f rendered/
kubectl rollout status deployment/api -n app --timeout=120s
```

Use an explicit target context and least-privileged pipeline identity. The dry-run and diff do not deploy; rollout status does not replace application-level health checks.""")
text124 = replace_section(text124, "Do's and Don'ts", """**Do**
- Build once and promote the same digest; record commit, artifact provenance, approvals, deployment identity, and health-gate result.
- Restrict runner or reconciler permissions and rehearse rollback with database/API compatibility constraints.

**Don't**
- Do not store long-lived cluster-admin credentials in CI or rebuild a different image per environment.
- Do not treat successful API apply as successful deployment or service health.""")
text124 = replace_section(text124, "Real life implementation", """A pipeline builds/tests/scans a web image, publishes a digest, and opens a reviewed environment change. A scoped delivery identity applies the rendered manifests; the gate waits for Deployment readiness, Service endpoints, and application error/latency SLOs. If a gate fails, promotion halts and the runbook rolls back the workload template while preserving compatible data state.""")
text124 = replace_section(text124, "Q&A", """**Q: Should each environment rebuild the artifact?** Prefer reproducible build-once promotion of the same digest with environment-specific configuration. **Q: Does `kubectl apply` prove the release is healthy?** No; check controller rollout, ready endpoints, and user-facing SLOs. **Q: Should CI have cluster-admin?** No; use narrow, auditable permissions and separate approval/production boundaries.""")
text124 = re.sub(r"(?m)^\*\*Objective-specific architect checkpoint:\*\* .*?$",
                 "**Objective-specific architect checkpoint:** Draw the artifact and permission path from commit to production, identify who can build, approve, deploy, and reconcile, and show how a failed health gate stops promotion without granting CI cluster-admin.",
                 text124)
p124.write_text(text124, encoding="utf-8", newline="\n")

print(f"repaired={len(GUIDES)} categories={len(ASSIGNMENTS)} exemplar_sections={len(SAMPLES)}")
