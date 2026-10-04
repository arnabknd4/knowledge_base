# Apply IP allow lists and networking settings

## What
Network design determines whether a workflow can reach private services, package registries, or internal infrastructure. The goal is to keep runner connectivity explicit, least-privilege, and resistant to accidental broad access.

## Why
GitHub Actions jobs often need to talk to internal APIs, registries, or cluster control planes. If your network design is vague, even a valid workflow can fail or create an unsafe egress path for production systems.

## How
- Place self-hosted runners in dedicated subnets or security groups with restricted outbound access.
- Use NAT, proxies, or VPNs when the runner must reach private or regulated systems.
- Validate DNS, firewall policies, and target service reachability before production rollout.
- Understand that GitHub-hosted runner IPs are not a stable fixed allowlist; design network access using service-based trust and explicit egress rules when possible.

## Features
- Self-hosted runner communication requirements and private networking patterns.
- NAT, proxy, and VPN connectivity options for enterprise systems.
- Explicit egress control and service allowlists.
- Hybrid patterns for public and private workloads.

## Do's and Don'ts
- Do: map the full network path from runner to target service.
- Do: keep outbound rules narrow and service-specific.
- Do: validate firewall, DNS, and proxy assumptions in staging before production.
- Do: structure private workloads around a dedicated security boundary.
- Don't: assume GitHub-hosted runner addresses are fixed or static.
- Don't: rely on one broad firewall rule for every job.
- Don't: forget that both GitHub connectivity and target service access matter.
- Don't: let private-only applications run on public egress patterns.

## Real-life implementation
A deployment workflow to an on-prem Kubernetes cluster runs on a self-hosted runner in a private VLAN. The runner is allowed only to reach the cluster API server, package mirror, and GitHub endpoints required by the runner, with no broad outbound access. This preserves least privilege and reduces the attack surface.

## Q&A
### Q: Why are networking rules a critical part of runner design?
A: Because runner connectivity defines the allowed trust paths for workflows, including access to private APIs, registries, and deployed systems.

### Q: What is different about GitHub-hosted runners from self-hosted runners in this context?
A: GitHub-hosted runners rely on public egress and a shared model, while self-hosted runners can be placed behind private networking and tighter corporate policy.

### Q: What should you validate before production rollout?
A: DNS resolution, firewall allowlists, outbound paths, and the expected network behavior of the target service or API.

### Q: When should you use a proxy or NAT?
A: When you need centralized logging, more controllable egress, or a private network path to internal systems.

## Official docs
- [About self-hosted runners and communication requirements](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#communication-requirements-for-self-hosted-runners)
- [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [Managing self-hosted runner groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-runners/about-self-hosted-runner-groups)
- [GitHub Actions network and firewall guidance](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#network-configuration)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
