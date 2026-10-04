# 2. Image design and Docker builds

[Docker syllabus](../copilot-docker-syllabus.md)

Objective-level study guides, grouped by the exact topic headings in the syllabus.

## Dockerfile and image composition

- [Write Dockerfiles using `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `ARG`, `USER`, `EXPOSE`, `ENTRYPOINT`, `CMD`, and `HEALTHCHECK` appropriately.](./dockerfile-and-image-composition/write-dockerfiles-using-from-workdir-copy-run-env-arg-user-expose/study-guide.md)
- [Distinguish build-time `ARG` from runtime `ENV`; avoid treating either as a secure secret store.](./dockerfile-and-image-composition/distinguish-build-time-arg-from-runtime-env-avoid-treating-either-as-a/study-guide.md)
- [Explain the difference between `ENTRYPOINT` and `CMD`, exec form and shell form, and how signals reach the application process.](./dockerfile-and-image-composition/explain-the-difference-between-entrypoint-and-cmd-exec-form-and-shell/study-guide.md)
- [Use `.dockerignore` to exclude credentials, local artifacts, VCS metadata, and unnecessary build context.](./dockerfile-and-image-composition/use-dockerignore-to-exclude-credentials-local-artifacts-vcs-metadata/study-guide.md)
- [Choose base images with regard to compatibility, maintenance, size, package ecosystem, and support—not size alone.](./dockerfile-and-image-composition/choose-base-images-with-regard-to-compatibility-maintenance-size/study-guide.md)
- [Build multi-stage images that separate build dependencies from runtime artifacts.](./dockerfile-and-image-composition/build-multi-stage-images-that-separate-build-dependencies-from-runtime/study-guide.md)
- [Run the application as a non-root user and include only the runtime dependencies and files needed.](./dockerfile-and-image-composition/run-the-application-as-a-non-root-user-and-include-only-the-runtime/study-guide.md)

## BuildKit, cache, and reproducibility

- [Explain image layers and build cache invalidation; order Dockerfile steps to keep stable dependencies cacheable.](./buildkit-cache-and-reproducibility/explain-image-layers-and-build-cache-invalidation-order-dockerfile/study-guide.md)
- [Use BuildKit/buildx for modern builds, multi-platform targets, cache import/export, and build attestations where supported.](./buildkit-cache-and-reproducibility/use-buildkit-buildx-for-modern-builds-multi-platform-targets-cache/study-guide.md)
- [Use build secrets and SSH forwarding features rather than embedding credentials in Dockerfile instructions or image layers.](./buildkit-cache-and-reproducibility/use-build-secrets-and-ssh-forwarding-features-rather-than-embedding/study-guide.md)
- [Understand build context, target stages, platforms, build arguments, and provenance metadata.](./buildkit-cache-and-reproducibility/understand-build-context-target-stages-platforms-build-arguments-and/study-guide.md)
- [Make builds repeatable by controlling base-image references, dependency lockfiles, build inputs, and build environment.](./buildkit-cache-and-reproducibility/make-builds-repeatable-by-controlling-base-image-references-dependency/study-guide.md)
- [Diagnose slow, unexpectedly invalidated, or non-reproducible builds.](./buildkit-cache-and-reproducibility/diagnose-slow-unexpectedly-invalidated-or-non-reproducible-builds/study-guide.md)

## Image lifecycle and design

- [Design immutable images: create a new image for a change rather than patching a running container.](./image-lifecycle-and-design/design-immutable-images-create-a-new-image-for-a-change-rather-than/study-guide.md)
- [Tag images with human-readable release identifiers and deploy by digest when immutable identity is required.](./image-lifecycle-and-design/tag-images-with-human-readable-release-identifiers-and-deploy-by-digest/study-guide.md)
- [Understand mutable tags such as `latest` and the risks they pose to rollback and repeatable deployment.](./image-lifecycle-and-design/understand-mutable-tags-such-as-latest-and-the-risks-they-pose-to/study-guide.md)
- [Inspect image metadata, layers, size, platform/architecture, labels, and history.](./image-lifecycle-and-design/inspect-image-metadata-layers-size-platform-architecture-labels-and/study-guide.md)
- [Define image deprecation, retention, rebuild, patch, and rollback policies.](./image-lifecycle-and-design/define-image-deprecation-retention-rebuild-patch-and-rollback-policies/study-guide.md)
