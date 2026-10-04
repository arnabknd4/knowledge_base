# Download and manage workflow artifacts

## What
Artifacts are run-scoped bundles of output data preserved for later review, handoff, or release stages. They are not the same as caches: caches speed repeatable dependency restoration, while artifacts preserve data for inspection or transfer.

## Why
A workflow may need to preserve build reports, test results, compiled binaries, or deployment bundles. If the artifact is not managed intentionally, its retention, naming, and security posture can become a gap during incident response or release work.

## How
1. Define the artifact contract clearly: name, files, producer job, consumer, sensitivity, and retention goal.
2. Upload only the required files to avoid leaking credentials or unrelated build output.
3. Use explicit names or naming conventions to distinguish matrix jobs or build variants.
4. Download artifacts from the correct run and verify the commit, job, and repository before using them in release or deployment logic.
5. Retain artifacts for the minimum required time, then delete them when the retention period or compliance policy permits.
6. Treat transferred files as untrusted input: validate structure, provenance, and signing before using them in a privileged action.

## Features
- Upload/download lifecycle: `actions/upload-artifact` and `actions/download-artifact` provide the standard handoff pattern.
- Retention controls: artifact lifetime and deletion are part of operational hygiene and security review.
- Data provenance: artifacts must be tied to the correct run, commit, and producing job.
- API and CLI support: REST and `gh run download` can manage artifacts programmatically.

## Do's and Don'ts
### Do
- Keep artifact payloads focused and minimal.
- Use unique names for matrix jobs or multi-output builds.
- Validate artifacts before using them for deployment or release decisions.
- Delete artifacts when retention is no longer needed and policy allows.

### Don't
- Don't use a cache as the authoritative release artifact.
- Don't upload secrets, tokens, or full workspace directories when only a small output is needed.
- Don't assume any artifact still exists indefinitely; retention and expiration vary by policy and age.

## Real-life implementation
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: app-dist
          path: dist/
          retention-days: 14
```

The artifact should be downloaded and validated in the consuming job or release process before it is used in a deployment. This protects the pipeline from accidental use of stale or manipulated output.

### Official references
- [Store and share data with workflow artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [actions/upload-artifact](https://github.com/actions/upload-artifact)
- [actions/download-artifact](https://github.com/actions/download-artifact)
- [REST API: artifacts](https://docs.github.com/en/rest/actions/artifacts)
- [GitHub CLI: `gh run download`](https://cli.github.com/manual/gh_run_download)

## Q&A
### Q: Which is the right place for a release bundle: an artifact or a dependency cache?
A: A release bundle belongs in an artifact because it represents a persisted output with provenance and retention. A cache is for dependency reuse and is not a trustworthy release record.

### Q: What checks should a deploy job perform before consuming an artifact from an upstream job?
A: Verify the artifact name, run/commit provenance, expected file structure, and any validation or signing step required before using it in a privileged action.

### Q: Why do retention, sensitivity, and investigation requirements matter together?
A: Longer retention helps audit and recovery but increases the exposure window for sensitive output. The right balance depends on compliance and operational recovery requirements.

### Q: Why are artifacts not automatically safe to use in later jobs or release pipelines?
A: They are outputs, not guarantees. They must be validated for contents, provenance, and security before being trusted in a deployment or release flow.
