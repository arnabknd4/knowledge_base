# Build multi-stage images that separate build dependencies from runtime artifacts.

## What

Named build stages separate toolchains from the final runtime image; COPY --from transfers selected artifacts without copying the builder filesystem. Multi-stage builds copy selected artifacts, not toolchain dependencies; validate target architecture, ABI, dynamic libraries, certificates, and final-stage behavior.

## Why

Readable tags simplify release operations, while digest pinning trades convenience for exact promotion and rollback identity.

## How

Compile in a named builder stage, copy only the runtime artifact into a compatible final stage, then test the final image for libraries, permissions, health, and architecture.

## Features

The final stage must still include compatible libraries, certificates, permissions, and runtime data; stages do not guarantee that binaries are static.

## Code snippets (if any)

```dockerfile
FROM golang:1.24 AS build
WORKDIR /src
COPY . .
RUN go build -o /out/app ./cmd/app
FROM gcr.io/distroless/static-debian12
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Copy the entire build environment into the final image or assume every binary is static.

## Real-life implementation

CI tests the final runtime stage, including libraries and permissions, before publishing the smaller image.

## Q&A

- **What is the key concept?** Named build stages separate toolchains from the final runtime image.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Copy the entire build environment into the final image or assume every binary is static.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
