# GH-200 study guide: use OIDC federation for cloud-provider access

## What

OpenID Connect (OIDC) federation lets a GitHub Actions job request a signed identity token and exchange it with a configured cloud identity provider for temporary credentials. The job needs `id-token: write` to request a token; that permission permits token issuance, not arbitrary write access to the cloud. The cloud trust policy must validate claims such as issuer, audience, and subject.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

Long-lived cloud keys stored as repository or environment secrets can be leaked, copied, or reused after a workflow finishes. Federation can reduce that exposure by issuing short-lived credentials only when the workflow identity meets cloud-side conditions. OIDC does not itself guarantee least privilege: a broad trust relationship or overpowered cloud role can still enable compromise.

## How

- Configure a cloud role/provider to trust GitHub's OIDC issuer and the intended audience.
- Restrict claims to the exact repository and trusted branch, tag, or environment; use environment-based subjects when deployment approvals are part of the trust boundary.
- Grant `id-token: write` only to jobs that need federation and keep other token permissions minimal.
- Assign a least-privilege cloud role, use the provider's supported credential action/client, and verify the effective claims and session duration.
- Test rejected identities as well as the intended one; remove static cloud secrets after migration only when no other consumer needs them.

```yaml
permissions:
  contents: read
  id-token: write

jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d8e5b6821dfbee0d # v4.2.2
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@<reviewed-full-commit-sha>
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-prod
          aws-region: us-east-1
```

The AWS trust policy must independently restrict the accepted `sub` and `aud` claims. Pin and review the credential action; replace its placeholder with a verified SHA.

## Features

- **Short-lived federation:** provider-issued sessions can expire after a configured duration rather than relying on a persistent access key.
- **Claim-based trust:** cloud policies can constrain repository, ref, environment, and audience, subject to provider claim support.
- **Workflow-scoped permission:** `id-token: write` enables token requests for that job, not cloud authorization on its own.
- **Deployment integration:** environments and approval gates can contribute to identity conditions where the provider mapping supports them.

## Do's and Don'ts

**Do**
- Restrict issuer, audience, and subject claims to the exact workload that should assume the role.
- Use separate, least-privilege roles for environments and deployment purposes.
- Limit which jobs receive `id-token: write` and review the actions running in those jobs.
- Confirm token claims and provider-side logs during rollout.

**Don't**
- Assume enabling `id-token: write` alone authenticates to a cloud account or makes access safe.
- Trust every branch, repository, or workflow from an organization through a broad subject pattern.
- Expose the cloud role to untrusted pull-request code or use a production role for build/test jobs.
- Store static credentials alongside OIDC indefinitely without a documented need and rotation plan.

## Real-life implementation

A production deployment runs on the protected `main` branch and references the `production` environment. Only that job can request an OIDC token; the cloud role accepts the intended repository/environment subject and audience and grants only deployment rights. Pull-request test jobs have neither `id-token: write` nor cloud credentials. This narrows credential lifetime and blocks other refs from assuming the production role.

## Q&A

**Q: What does `id-token: write` allow?**

A: It allows the job to request an OIDC token from GitHub; cloud access still depends on provider trust and role permissions.

**Q: Why restrict the `sub` claim?**

A: It identifies the workflow context, allowing the cloud provider to reject tokens from unintended repositories, refs, or environments.

**Q: Does OIDC make a cloud role least-privilege automatically?**

A: No. The role's permissions and trust conditions must both be deliberately constrained.

**Q: Can OIDC eliminate every stored cloud secret?**

A: Not necessarily. Some providers or integrations may not support federation, and unrelated consumers may still need credentials; inventory and migrate those cases separately.

### References

- [OIDC with GitHub Actions](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [Configuring OIDC in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
- [Configuring OIDC in Azure](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure)
- [Configuring OIDC in Google Cloud Platform](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform)
