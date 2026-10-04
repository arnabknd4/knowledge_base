# GH-200 study guide: generate and verify artifact attestations and provenance

## What

Artifact attestations are verifiable statements about a software artifact, including its digest and build provenance. GitHub Actions can generate attestations with workflow identity and provenance metadata; consumers can verify the attestation and apply policy before accepting an artifact. Provenance describes how and where an artifact was built; it is related to, but not interchangeable with, a signature or a vulnerability scan.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

An artifact copied between build, release, and deployment systems can be replaced or confused with a stale build. Provenance allows a consumer to check whether the artifact digest is linked to the expected repository, source revision, and workflow identity. Generating an attestation alone does not block a deployment: a consumer must verify it and enforce the result.

## How

1. Build the release artifact, compute or obtain its exact digest, and keep the artifact and digest associated.
2. Grant only the permissions needed for attestation, typically `contents: read`, `id-token: write`, and `attestations: write`.
3. Generate a provenance attestation for the artifact. Pin the attestation action to a reviewed full commit SHA in production.
4. In the release or deployment path, verify the attestation against expected source, workflow, and digest before promotion.
5. Record the verification result and fail closed for high-trust releases if evidence is absent or does not match policy.

Illustrative configuration (replace the placeholder with the reviewed full SHA; supply the actual digest or subject path appropriate to the build):

```yaml
permissions:
  contents: read
  id-token: write
  attestations: write

steps:
  - name: Build release artifact
    run: make build
  - name: Attest artifact
    uses: actions/attest-build-provenance@<reviewed-full-commit-sha>
    with:
      subject-path: dist/my-app.tar.gz
```

The subject path must identify the artifact actually released. Do not copy the placeholder literally.

## Features

- **Artifact identity:** attestations bind statements to artifact digests, reducing ambiguity about which bytes were built.
- **Build provenance:** records information about the build context and workflow identity that a verifier can evaluate.
- **Verification:** downstream systems can check the statement and apply their own repository, workflow, source, and policy requirements.
- **SLSA alignment:** provenance can support supply-chain assurance goals; the level of assurance depends on the build and verification design, not merely the presence of metadata.

## Do's and Don'ts

**Do**
- Verify the exact artifact digest before deployment or publication.
- Define expected repository, source ref/revision, workflow, and issuer constraints in the consumer policy.
- Keep attestation permissions limited to the job that creates attestations.
- Pin the generator action and protect the workflow that establishes provenance.

**Don't**
- Treat generation as verification or assume that any valid attestation satisfies your policy.
- Claim provenance proves an artifact is vulnerability-free or that the build process itself is uncompromised.
- Attest one file and deploy a different file, or accept a version label without checking the digest.
- Use a broad permission set or trust an unreviewed workflow merely because it emits provenance.

## Real-life implementation

A release workflow builds a container, records its immutable digest, and creates provenance from a protected release workflow. Before production deployment, a separate gate verifies the attestation and checks that its repository and workflow identity are the approved ones and that the digest matches the image being deployed. If verification fails, deployment stops. This limits artifact substitution risk, while code review, dependency scanning, and controlled build runners address separate threats.

## Q&A

**Q: Is an attestation the same thing as a signature?**

A: They are related but distinct concepts. Attestations make claims about an artifact and its provenance; signatures provide cryptographic evidence over data. The consumer still needs a trust policy.

**Q: Does creating an attestation enforce it during deployment?**

A: No. The deployment or downstream system must verify it and make the result a gate.

**Q: What should be matched during verification?**

A: At minimum, the artifact digest and the expected trusted source/workflow identity; exact policy depends on the release threat model.

**Q: Does provenance guarantee a safe build?**

A: No. It provides evidence about the build context, not proof that source code or dependencies are benign.

### References

- [Artifact attestations](https://docs.github.com/en/actions/security-guides/using-artifact-attestations)
- [Build provenance with GitHub Actions](https://docs.github.com/en/actions/security-guides/using-artifact-attestations)
- [SLSA overview](https://slsa.dev/spec/v1.0/overview)
- [About GitHub artifact attestations](https://docs.github.com/en/actions/security-guides/using-artifact-attestations#about-artifact-attestations)
