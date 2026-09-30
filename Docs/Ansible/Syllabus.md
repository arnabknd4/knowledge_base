# Ansible (DevOps): Architect Level Prerequisites

**Flags:** R = Required | O = Optional | E = Exam oriented | L = Real-life use

---

## A. Prerequisites (before Ansible)

| Topic | Flag |
|---|---|
| Linux basics (filesystem, users, permissions, processes, services/systemd) | R, L |
| Package management (apt/yum/dnf) | R, L |
| SSH (keys, key-based auth, known_hosts, ssh-agent) | R, E, L |
| Shell/Bash basics | R, L |
| Networking basics (IP, DNS, ports, firewalls) | R, L |
| YAML syntax | R, E, L |
| Jinja2 basics | R, E, L |
| Python basics (Ansible runtime, modules) | O, L |
| Git and version control | R, L |
| Windows basics (WinRM, PowerShell) | O, L |
| Regex basics | O |

## B. Core Concepts

| Topic | Flag |
|---|---|
| Configuration management vs provisioning vs orchestration | R, E |
| Infrastructure as Code (IaC) | R, E |
| Agentless architecture | R, E |
| Push vs pull model | R, E |
| Idempotency | R, E, L |
| Declarative vs imperative | R, E |
| Control node vs managed nodes | R, E, L |
| Ansible Core vs Ansible Community Package | O, E |

## C. Building Blocks

| Topic | Flag |
|---|---|
| Inventory (static, dynamic) | R, E, L |
| Inventory groups, host/group variables | R, E, L |
| Ad-hoc commands | R, E, L |
| Modules | R, E, L |
| Plugins (connection, lookup, filter, callback, inventory) | O, E |
| Playbooks, plays, tasks | R, E, L |
| Handlers and notify | R, E, L |
| Variables and precedence | R, E, L |
| Facts and gather_facts | R, E, L |
| Conditionals (when) | R, E, L |
| Loops | R, E, L |
| Templates (Jinja2 templating) | R, E, L |
| Filters | R, E, L |
| Tags | R, E, L |
| Privilege escalation (become) | R, E, L |
| ansible.cfg | R, E, L |
| Error handling (block, rescue, always, ignore_errors, failed_when) | R, E, L |
| Delegation (delegate_to, run_once) | O, E, L |
| Rolling updates (serial, strategy) | O, E, L |
| Check mode and diff mode | R, E, L |
| Register and debug | R, E, L |
| Include vs import (static vs dynamic) | R, E |

## D. Reuse and Structure

| Topic | Flag |
|---|---|
| Roles (structure, defaults vs vars) | R, E, L |
| Role dependencies | O, E |
| Collections | R, E, L |
| Ansible Galaxy | R, E, L |
| FQCN (fully qualified collection names) | R, E |
| Directory layout best practices | R, E, L |
| group_vars and host_vars | R, E, L |

## E. Security

| Topic | Flag |
|---|---|
| Ansible Vault | R, E, L |
| Vault IDs | O, E |
| no_log | R, E, L |
| Secrets management integration (HashiCorp Vault, cloud secret managers) | O, L |
| Least privilege and become policies | R, L |

## F. Platform and Scale

| Topic | Flag |
|---|---|
| Ansible Automation Platform (AAP) overview | R, E, L |
| AWX (upstream project) | O, L |
| Automation Controller (formerly Tower) | R, E, L |
| Execution Environments | R, E, L |
| Automation Hub and Private Hub | O, E, L |
| ansible-navigator | O, E |
| Job templates, workflows, surveys | R, E, L |
| RBAC | R, E, L |
| Credentials | R, E, L |
| Instance groups and Automation Mesh | O, E, L |
| Event-Driven Ansible | O, E, L |
| ansible-pull | O, E |
| Performance tuning (forks, pipelining, fact caching, mitogen) | O, E, L |

## G. Integration and Use Cases

| Topic | Flag |
|---|---|
| Cloud modules (AWS, Azure, GCP) | R, L |
| Dynamic inventory for cloud | R, E, L |
| Network automation (network_cli, netconf) | O, L |
| Container and Kubernetes modules | O, L |
| Ansible with Terraform (roles split) | R, L |
| CI/CD integration (Jenkins, GitHub Actions, GitLab CI) | R, L |
| Windows automation | O, L |

## H. Quality and Troubleshooting

| Topic | Flag |
|---|---|
| ansible-lint | R, L |
| Molecule (role testing) | O, L |
| yamllint | O, L |
| Verbosity levels (-v to -vvvv) | R, E, L |
| Debugging playbooks (debugger, debug module) | R, E, L |
| Common connection and permission errors | R, L |

## I. Architect-Level Design Topics

| Topic | Flag |
|---|---|
| Ansible vs Puppet vs Chef vs Salt | R, E |
| Ansible vs Terraform (complementary roles) | R, E, L |
| Multi-environment strategy (dev/test/prod) | R, L |
| Inventory design at scale | R, L |
| Idempotent and immutable infrastructure trade-offs | R, E |
| Compliance and auditing automation | O, L |
| Governance of roles/collections (internal registry, versioning) | O, L |
| High availability and scaling of Automation Platform | O, E, L |