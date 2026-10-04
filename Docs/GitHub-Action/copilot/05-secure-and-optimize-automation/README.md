# Domain 05: Secure and optimize automation

This domain covers the GH-200 security and performance controls that keep workflows safe, compliant, and cost-aware. It is organized strictly around the official objective list in [copilot-github-syllabus.md](../copilot-github-syllabus.md).

## Topic 1: Implement security best practices

- [Environment protections and approval gates](./implement-security-best-practices/environment-protections-and-approval-gates/study-guide.md)
- [Identify and use trustworthy actions from GitHub Marketplace](./implement-security-best-practices/identify-and-use-trustworthy-actions-from-github-marketplace/study-guide.md)
- [Mitigate script injection](./implement-security-best-practices/mitigate-script-injection/study-guide.md)
- [Understand the GITHUB_TOKEN lifecycle and scope](./implement-security-best-practices/understand-github-token-lifecycle-and-scope/study-guide.md)
- [Use OIDC federation for cloud-provider access](./implement-security-best-practices/use-oidc-federation-for-cloud-provider-access/study-guide.md)
- [Pin third-party actions to full commit SHAs](./implement-security-best-practices/pin-third-party-actions-to-full-commit-shas/study-guide.md)
- [Enforce action-usage policies](./implement-security-best-practices/enforce-action-usage-policies/study-guide.md)
- [Generate and verify artifact attestations and provenance](./implement-security-best-practices/generate-and-verify-artifact-attestations-and-provenance/study-guide.md)

## Topic 2: Optimize workflow performance and cost

- [Configure caching and artifact retention](./optimize-workflow-performance-and-cost/configure-caching-and-artifact-retention/study-guide.md)
- [Recommend strategies for scaling and optimizing workflows](./optimize-workflow-performance-and-cost/recommend-strategies-for-scaling-and-optimizing-workflows/study-guide.md)

## Learning path

1. Start with security boundaries: environment approvals, secrets scoping, token permissions, and OIDC.
2. Study supply-chain controls: marketplace trust, policy enforcement, and SHA pinning.
3. Learn execution-safety: script injection defenses, command sanitization, and least privilege.
4. Understand artifact trust: provenance, attestations, verification, and deployment gates.
5. Finish with performance and cost management: caching, retention, matrix tuning, and workflow scale.

## Architects’ lens

Treat this domain as the intersection of identity, supply chain, runtime safety, and operating cost. In production, the strongest automation design is not just a workflow that works; it is a workflow that can be audited, defended, and scaled without hidden trust or runaway spend.

## Official references

- GH-200 syllabus: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200
- GitHub Actions security hardening: https://docs.github.com/en/actions/security-guides
- GitHub Actions documentation: https://docs.github.com/en/actions
- GitHub Actions policy for actions: https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization
- Artifact attestations: https://docs.github.com/en/actions/security-guides/using-artifact-attestations
