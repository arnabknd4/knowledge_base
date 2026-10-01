# Helm: Prerequisites and Core Topics (Architect Level)

**Flags:** `R` = Required | `O` = Optional | `E` = Exam oriented | `L` = Real-life use

## 1. Kubernetes Foundations (before Helm)
| Topic | Flag |
|---|---|
| Declarative vs imperative model | R |
| YAML manifests | R |
| kubectl basics, kubeconfig, contexts | R |
| Pods | R |
| Deployments | R |
| Services (ClusterIP / NodePort / LoadBalancer) | R |
| Ingress | R, L |
| ConfigMaps | R |
| Secrets | R, L |
| Namespaces | R, E |
| Labels, selectors, annotations | R |
| RBAC (ServiceAccount, Role, RoleBinding) | R, E, L |
| Resource requests/limits | R, L |
| PV / PVC / StorageClass | O, L |
| StatefulSets / DaemonSets / Jobs / CronJobs | O |
| Probes (liveness/readiness/startup) | O, L |
| HPA | O |
| CRDs | O, L |
| Kustomize | O, L |

## 2. Templating Foundations
| Topic | Flag |
|---|---|
| YAML syntax (indentation, multi-line strings, anchors) | R |
| Go template basics | R |
| Semantic versioning (SemVer) | R, E |
| JSON Schema | O, E |

## 3. Helm Core Concepts
| Topic | Flag |
|---|---|
| Chart / Release / Revision / Repository / Values | R, E |
| Helm 3 client-only architecture (no Tiller) | R, E |
| Helm 2 vs Helm 3 differences | E |
| Release storage (Secrets per namespace) | E |
| Three-way strategic merge patch | O, E |

## 4. Chart Structure
| Topic | Flag |
|---|---|
| Chart.yaml (apiVersion v2, version vs appVersion, type) | R, E |
| values.yaml | R, E |
| templates/ directory | R, E |
| _helpers.tpl | R, L |
| NOTES.txt | O |
| charts/ and Chart.lock | R, E |
| crds/ directory | E, L |
| values.schema.json | O, E |
| .helmignore | O |
| Application vs Library charts | O, E |

## 5. Templating Engine
| Topic | Flag |
|---|---|
| Built-in objects (.Values, .Release, .Chart, .Capabilities, .Template, .Files) | R, E |
| Pipelines and core functions (default, quote, required, toYaml, nindent, include, tpl, lookup) | R, L |
| Control flow (if/else, with, range, variables) | R |
| Whitespace control | R, L |
| Named templates (define / template / include) | R, E |
| Sprig functions | O |

## 6. Values Management
| Topic | Flag |
|---|---|
| Values precedence order | R, E |
| --set / --set-string / --set-file / -f | R, E |
| Global values | R, E |
| Multi-environment values strategy | L |

## 7. Dependencies
| Topic | Flag |
|---|---|
| Subcharts and dependencies block | R, E |
| condition / tags | R, E |
| import-values / alias | O, E |
| Umbrella chart pattern | L |
| helm dependency update / build | R |

## 8. Release Lifecycle
| Topic | Flag |
|---|---|
| install / upgrade / rollback / uninstall | R, E |
| history / status / list | R |
| upgrade --install | L |
| --atomic / --wait / --timeout | R, L |
| --reuse-values vs --reset-values | E, L |
| --force / --dry-run / --debug | R, L |
| helm.sh/resource-policy: keep | O, E |
| Rolling restart on config change (checksum annotation) | L |

## 9. Hooks and Tests
| Topic | Flag |
|---|---|
| Hook types (pre/post install, upgrade, delete, rollback) | R, E |
| Hook weight | E |
| Hook delete policy | E, L |
| helm test / test hooks | E |

## 10. Repositories and Distribution
| Topic | Flag |
|---|---|
| helm repo add / update / search | R |
| index.yaml | E |
| helm package | R |
| OCI registry support (helm push/pull) | R, L |
| Artifact Hub | O |
| Private repos (Harbor / ChartMuseum) | O, L |

## 11. Debugging and Quality
| Topic | Flag |
|---|---|
| helm template | R, L |
| helm lint | R, L |
| helm get (manifest / values / hooks) | R, L |
| chart-testing (ct), kubeconform | O, L |

## 12. Security
| Topic | Flag |
|---|---|
| Provenance and signing (.prov, GPG, helm verify) | E, L |
| Secrets handling (Sealed Secrets, External Secrets, SOPS) | L |
| Image pinning (tag vs digest) | L |
| Helm RBAC / least privilege | L |

## 13. Architect-Level Decisions
| Topic | Flag |
|---|---|
| Helm vs Kustomize vs Operators | R, E |
| GitOps with Helm (ArgoCD / Flux HelmRelease) | R, L |
| Chart versioning and release strategy | L |
| CI/CD pipeline for charts | L |
| CRD lifecycle limitations in Helm | E, L |
| Plugins (helm-diff, helm-secrets) | O, L |
| Policy enforcement (OPA / Kyverno) | O |

**Discard:** Tiller internals (Helm 2 only, keep for comparison in exams), Helm 2 migration plugin details, deep Sprig function catalog.