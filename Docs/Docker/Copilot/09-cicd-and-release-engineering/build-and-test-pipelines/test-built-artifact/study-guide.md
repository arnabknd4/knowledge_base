# Test the built artifact at unit, integration, and image levels

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Test the built artifact at unit, integration, and image levels](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Test the same image intended for release. Unit tests validate code; integration tests exercise contracts; image-level checks validate startup, configuration, permissions, and runtime health behavior.

## Why
Testing source while deploying a separately rebuilt image leaves gaps: packaging defects, missing runtime files, or build-time differences can escape validation.

## How
Build the candidate once, capture its digest, run unit tests, then integration and image checks against that exact artifact. Preserve reports and bind results to the digest.

## Features
BuildKit supports build/test workflows; disposable containers can provide explicit network, resource, and cleanup boundaries. Tests should not require production credentials.

## Code snippets (if any)
```sh
docker run --rm --network test-net registry.example/app:candidate ./smoke-test
```

## Do's and Don'ts
Do: test the packaged image and record its digest. Don’t: assume source tests prove runtime behavior or give untrusted tests deployment credentials.

## Real-life implementation
Unit tests run before packaging, followed by integration and smoke checks using ephemeral dependencies. Only the tested digest is eligible for promotion.

## Q&A
- **Q: What is the invariant?** Tests and deployment reference the same digest.
- **Q: Should PR tests have production credentials?** No; use isolated test credentials.
- **Q: Why image-level tests?** They catch packaging and runtime defects.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/building/testing/)
- [Docker documentation](https://docs.docker.com/build/ci/)
