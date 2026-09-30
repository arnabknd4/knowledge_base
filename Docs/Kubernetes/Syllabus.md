# Kubernetes + CKA: Topic Checklist (Architect Level)

**Flags:** 🔴 Required · 🟡 Optional · 📝 Exam-oriented · 🏭 Real-life use

---

## A. Pre-Kubernetes Foundations

| Topic | Flag |
|---|---|
| Container fundamentals (image, container, registry, layers) | 🔴 |
| OCI standard & container runtimes (containerd, CRI-O) | 🔴 📝 |
| Linux namespaces & cgroups | 🔴 |
| Linux CLI, permissions, processes | 🔴 📝 |
| systemd, journalctl (service/log debugging) | 🔴 📝 |
| Networking basics (IP, CIDR, subnets, ports, NAT) | 🔴 📝 |
| DNS fundamentals | 🔴 📝 |
| L4 vs L7 load balancing | 🔴 🏭 |
| TLS, PKI, certificates | 🔴 📝 |
| YAML & JSON | 🔴 📝 |
| JSONPath / custom-columns output | 📝 |
| Declarative vs imperative, desired state, reconciliation | 🔴 |
| Distributed systems basics (consensus, Raft) | 🔴 |
| vim/nano, tmux, bash aliases | 📝 |
| iptables / IPVS | 🟡 🏭 |
| Cloud basics (VM, VPC, LB, block storage) | 🏭 |
| Git, CI/CD basics | 🏭 |
| Microservices / 12-factor apps | 🟡 |
| Bash scripting | 🟡 |
| Go language | 🟡 |

---

## B. Cluster Architecture

| Topic | Flag |
|---|---|
| Control plane vs worker node | 🔴 📝 |
| kube-apiserver | 🔴 📝 |
| etcd | 🔴 📝 |
| kube-scheduler | 🔴 📝 |
| kube-controller-manager | 🔴 📝 |
| cloud-controller-manager | 🟡 🏭 |
| kubelet | 🔴 📝 |
| kube-proxy | 🔴 📝 |
| CRI / CNI / CSI interfaces | 🔴 📝 |
| Static pods | 📝 |
| Namespaces | 🔴 📝 |
| API groups, versions, resources | 🔴 📝 |
| kubectl (imperative commands, `explain`, dry-run) | 🔴 📝 |
| kubeconfig, contexts | 🔴 📝 |

---

## C. Workloads

| Topic | Flag |
|---|---|
| Pod (lifecycle, multi-container) | 🔴 📝 |
| Init containers, sidecars | 📝 🏭 |
| ReplicaSet | 🔴 📝 |
| Deployment (rollout, rollback, strategies) | 🔴 📝 🏭 |
| StatefulSet | 🔴 📝 🏭 |
| DaemonSet | 🔴 📝 |
| Job, CronJob | 🔴 📝 |
| Labels, selectors, annotations | 🔴 📝 |
| Probes (liveness, readiness, startup) | 🔴 📝 🏭 |
| Resource requests & limits, QoS classes | 🔴 📝 🏭 |
| LimitRange, ResourceQuota | 📝 🏭 |
| HPA | 📝 🏭 |
| VPA, Cluster Autoscaler | 🟡 🏭 |
| PodDisruptionBudget | 🏭 |

---

## D. Configuration

| Topic | Flag |
|---|---|
| ConfigMap | 🔴 📝 |
| Secret (types, encryption at rest) | 🔴 📝 🏭 |
| Env vars, volume-mounted config | 🔴 📝 |
| Image pull secrets | 📝 🏭 |

---

## E. Scheduling

| Topic | Flag |
|---|---|
| Scheduling flow | 🔴 |
| nodeSelector | 🔴 📝 |
| Node affinity / Pod affinity & anti-affinity | 🔴 📝 🏭 |
| Taints & tolerations | 🔴 📝 |
| Manual scheduling (`nodeName`) | 📝 |
| Topology spread constraints | 🏭 |
| Priority & preemption | 🟡 🏭 |
| Multiple schedulers | 🟡 |

---

## F. Services & Networking

| Topic | Flag |
|---|---|
| Kubernetes network model | 🔴 📝 |
| Service (ClusterIP, NodePort, LoadBalancer, ExternalName) | 🔴 📝 🏭 |
| Headless service | 📝 🏭 |
| Endpoints / EndpointSlice | 🔴 📝 |
| CoreDNS | 🔴 📝 |
| Ingress & Ingress controller | 🔴 📝 🏭 |
| Gateway API | 📝 🏭 |
| NetworkPolicy | 🔴 📝 🏭 |
| CNI plugins (Calico, Cilium, Flannel) | 🔴 🏭 |
| Service mesh | 🟡 🏭 |

---

## G. Storage

| Topic | Flag |
|---|---|
| Volumes (emptyDir, hostPath, configMap, secret) | 🔴 📝 |
| PersistentVolume (PV) | 🔴 📝 |
| PersistentVolumeClaim (PVC) | 🔴 📝 |
| StorageClass, dynamic provisioning | 🔴 📝 🏭 |
| Access modes, reclaim policy | 🔴 📝 |
| Volume expansion, snapshots | 🟡 🏭 |
| CSI drivers | 🏭 |

---

## H. Security

| Topic | Flag |
|---|---|
| Authentication vs authorization | 🔴 📝 |
| RBAC (Role, ClusterRole, bindings) | 🔴 📝 🏭 |
| ServiceAccount | 🔴 📝 🏭 |
| Certificates API, CSR | 📝 |
| Cluster certificates & kubeadm cert management | 📝 🏭 |
| SecurityContext | 📝 🏭 |
| Pod Security Standards / Admission | 📝 🏭 |
| Admission controllers | 🏭 |
| Image security & scanning | 🏭 |
| Audit logging | 🟡 🏭 |
| Runtime security (Falco, seccomp, AppArmor) | 🟡 |

---

## I. Cluster Lifecycle & Operations

| Topic | Flag |
|---|---|
| kubeadm: install, bootstrap, join | 🔴 📝 |
| Cluster upgrade with kubeadm | 🔴 📝 🏭 |
| etcd backup & restore | 🔴 📝 🏭 |
| Node maintenance (cordon, drain, uncordon) | 🔴 📝 🏭 |
| HA control plane topology | 🔴 🏭 |
| Managed Kubernetes (EKS, AKS, GKE) | 🏭 |
| Version skew policy | 📝 🏭 |
| Multi-cluster / multi-tenancy | 🟡 🏭 |

---

## J. Troubleshooting

| Topic | Flag |
|---|---|
| `kubectl logs`, `describe`, `events`, `exec` | 🔴 📝 🏭 |
| Pod failure states (CrashLoopBackOff, ImagePullBackOff, Pending) | 🔴 📝 🏭 |
| Node NotReady, kubelet failure | 🔴 📝 |
| Control plane component failure | 🔴 📝 |
| Service / DNS / network debugging | 🔴 📝 🏭 |
| `crictl` | 📝 |
| Monitoring (metrics-server, Prometheus, Grafana) | 📝 🏭 |
| Logging (Fluent Bit, EFK/Loki) | 🏭 |

---

## K. Extensibility & Packaging

| Topic | Flag |
|---|---|
| Helm | 📝 🏭 |
| Kustomize | 📝 🏭 |
| CRD | 📝 🏭 |
| Operators | 🟡 🏭 |
| GitOps (Argo CD, Flux) | 🟡 🏭 |

---

## L. Exam Strategy (CKA-Specific)

| Topic | Flag |
|---|---|
| Exam domains & weightage | 🔴 📝 |
| Allowed docs (kubernetes.io) navigation | 📝 |
| Imperative commands & `--dry-run=client -o yaml` | 📝 |
| Aliases, autocompletion, context switching | 📝 |
| Time management, killer.sh practice | 📝 |