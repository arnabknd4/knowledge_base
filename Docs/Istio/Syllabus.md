# Istio Prerequisites (Architect Level)

**Legend:** 🔴 Required | 🟡 Optional | 📝 Exam Oriented | 🛠️ Real-Life Use

---

## 1. Kubernetes Fundamentals
- Pod, Container, Sidecar pattern: 🔴 📝 🛠️
- Deployment, ReplicaSet: 🔴 🛠️
- Service (ClusterIP, NodePort, LoadBalancer, Headless): 🔴 📝 🛠️
- Namespace and label/selector: 🔴 📝 🛠️
- Ingress and Ingress Controller: 🔴 📝 🛠️
- Gateway API: 🟡 📝 🛠️
- ConfigMap, Secret: 🔴 🛠️
- ServiceAccount: 🔴 📝 🛠️
- RBAC: 🔴 📝 🛠️
- CRD and Custom Controller/Operator: 🔴 📝
- Admission Controllers (Mutating/Validating Webhook): 🔴 📝 🛠️
- Init Containers: 🔴 📝
- Probes (Liveness, Readiness, Startup): 🔴 🛠️
- HPA: 🟡 🛠️
- Network Policy: 🔴 📝 🛠️
- Helm: 🔴 🛠️
- Kustomize: 🟡 🛠️
- kubectl, kubeconfig, contexts: 🔴 🛠️
- Multi-cluster basics: 🟡 🛠️

## 2. Kubernetes Networking
- Pod-to-Pod, Pod-to-Service networking: 🔴 📝
- CNI: 🔴 📝 🛠️
- kube-proxy, iptables, IPVS: 🔴 📝 🛠️
- CoreDNS, Service discovery: 🔴 📝 🛠️
- Kubernetes DNS naming (FQDN): 🔴 📝
- Endpoints and EndpointSlices: 🟡 📝
- eBPF basics: 🟡 🛠️

## 3. Networking Fundamentals
- OSI model (L4 vs L7): 🔴 📝
- TCP, UDP: 🔴 📝
- HTTP/1.1, HTTP/2: 🔴 📝 🛠️
- gRPC: 🔴 📝 🛠️
- WebSocket: 🟡 🛠️
- DNS: 🔴 📝 🛠️
- Load Balancing algorithms: 🔴 📝 🛠️
- L4 vs L7 Load Balancer: 🔴 📝
- Reverse Proxy, Forward Proxy: 🔴 📝
- NAT, Ports, Sockets: 🟡
- CIDR, Subnets: 🟡 🛠️

## 4. Proxy and Envoy
- Envoy Proxy: 🔴 📝 🛠️
- Listener, Route, Cluster, Endpoint (LDS, RDS, CDS, EDS): 🔴 📝
- xDS API: 🔴 📝
- Filters and Filter Chain: 🟡 📝
- Envoy Admin Interface: 🟡 🛠️
- WebAssembly (Wasm) extensions: 🟡 🛠️

## 5. Security Foundations
- TLS, mTLS: 🔴 📝 🛠️
- PKI, Certificates, CA, Root/Intermediate CA: 🔴 📝 🛠️
- Certificate rotation: 🔴 📝 🛠️
- SPIFFE, SPIRE, SVID: 🔴 📝
- JWT, OIDC, OAuth2: 🔴 📝 🛠️
- AuthN vs AuthZ: 🔴 📝
- Zero Trust: 🔴 📝 🛠️
- RBAC vs ABAC: 🟡 📝
- cert-manager: 🟡 🛠️
- External CA integration (Vault etc.): 🟡 🛠️

## 6. Service Mesh Concepts
- What is Service Mesh: 🔴 📝
- Control Plane vs Data Plane: 🔴 📝
- Sidecar model: 🔴 📝 🛠️
- Ambient mode (ztunnel, waypoint proxy): 🔴 📝 🛠️
- Sidecar vs Ambient trade-offs: 🔴 📝
- East-West vs North-South traffic: 🔴 📝
- Service-to-service communication: 🔴 📝

## 7. Microservices Patterns
- Circuit Breaker: 🔴 📝 🛠️
- Retry, Timeout: 🔴 📝 🛠️
- Rate Limiting: 🔴 📝 🛠️
- Fault Injection: 🔴 📝 🛠️
- Outlier Detection: 🔴 📝
- Canary Deployment: 🔴 📝 🛠️
- Blue-Green Deployment: 🔴 📝 🛠️
- Traffic Mirroring (Shadowing): 🔴 📝 🛠️
- A/B Testing, Header-based routing: 🟡 🛠️
- Bulkhead: 🟡 📝
- API Gateway vs Service Mesh: 🔴 📝

## 8. Observability
- Metrics, Logs, Traces (three pillars): 🔴 📝
- Prometheus: 🔴 📝 🛠️
- Grafana: 🔴 🛠️
- Kiali: 🔴 📝 🛠️
- Jaeger, Zipkin: 🔴 📝 🛠️
- OpenTelemetry: 🟡 🛠️
- Distributed Tracing (trace context propagation): 🔴 📝
- Golden Signals (RED/USE): 🟡 📝
- Access Logs: 🟡 🛠️

## 9. Istio Core (Preview)
- Istiod: 🔴 📝
- VirtualService: 🔴 📝 🛠️
- DestinationRule: 🔴 📝 🛠️
- Gateway (Ingress/Egress): 🔴 📝 🛠️
- ServiceEntry: 🔴 📝 🛠️
- Sidecar resource: 🔴 📝
- PeerAuthentication: 🔴 📝 🛠️
- RequestAuthentication: 🔴 📝 🛠️
- AuthorizationPolicy: 🔴 📝 🛠️
- Telemetry API: 🟡 📝
- EnvoyFilter: 🟡 📝
- WorkloadEntry, WorkloadGroup (VM integration): 🟡 📝
- Sidecar injection (auto/manual): 🔴 📝 🛠️
- istioctl: 🔴 📝 🛠️
- Install/Upgrade (istioctl, Helm, Operator, Revision-based/canary upgrade): 🔴 📝 🛠️
- Install profiles: 🔴 📝
- Multi-cluster topologies (primary-remote, multi-primary): 🟡 📝 🛠️
- Multi-network, Multi-mesh: 🟡 📝

## 10. Good-to-Have Extras
- GitOps (ArgoCD/Flux) with Istio: 🟡 🛠️
- Cloud mesh offerings (EKS/AKS/GKE Istio add-ons, Anthos/ASM): 🟡 🛠️
- Linkerd, Cilium Service Mesh (comparison): 🟡 📝
- Performance and resource overhead tuning: 🟡 🛠️
- Troubleshooting (istioctl analyze, proxy-status, proxy-config): 🔴 📝 🛠️

---

**Suggested learning order:** 1 → 2 → 3 → 5 → 4 → 6 → 7 → 8 → 9 → 10