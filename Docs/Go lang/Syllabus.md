# Golang for DevOps + SRE: Core Topics (Architect Level)

**Flags:** **R** = Required | **O** = Optional | **E** = Exam-oriented | **L** = Real-life use

## 1. Language Basics
| Topic | Flag |
|---|---|
| Go toolchain (`go run/build/test/fmt/vet/mod`) | R, L |
| Packages & imports | R, E |
| Variables, constants, `iota` | R, E |
| Basic types, zero values | R, E |
| Control flow (`if`, `for`, `switch`) | R |
| Functions, multiple returns, variadics | R, E |
| `defer`, `panic`, `recover` | R, E, L |
| Pointers | R, E |
| Exported vs unexported identifiers | R, E |
| Closures, anonymous functions | O, E |

## 2. Data Structures
| Topic | Flag |
|---|---|
| Arrays vs slices (len/cap, append) | R, E |
| Maps | R, E, L |
| Structs, embedding | R, E, L |
| Struct tags (json/yaml) | R, L |
| Strings, runes, bytes | R, E |

## 3. Types & Abstraction
| Topic | Flag |
|---|---|
| Methods (value vs pointer receivers) | R, E |
| Interfaces, implicit satisfaction | R, E, L |
| Empty interface / `any` | R, E |
| Type assertions, type switches | R, E |
| Generics (type parameters, constraints) | O, E |
| Composition over inheritance | R, E |

## 4. Error Handling
| Topic | Flag |
|---|---|
| `error` interface | R, E, L |
| Error wrapping (`%w`, `errors.Is/As`) | R, E, L |
| Custom error types, sentinel errors | R, L |

## 5. Concurrency (Core for SRE)
| Topic | Flag |
|---|---|
| Goroutines | R, E, L |
| Channels (buffered/unbuffered, directional) | R, E, L |
| `select` | R, E, L |
| `sync` (WaitGroup, Mutex, RWMutex, Once) | R, E, L |
| `sync/atomic` | O, E |
| `context` (cancellation, timeout, deadline) | R, E, L |
| Worker pool, fan-in/fan-out, pipeline patterns | R, L |
| `errgroup` | O, L |
| Race condition, deadlock, goroutine leak | R, E, L |
| Race detector (`-race`) | R, L |
| Go scheduler (GMP model) | O, E |

## 6. Modules & Project Structure
| Topic | Flag |
|---|---|
| Go modules (`go.mod`, `go.sum`) | R, L |
| Semantic versioning, module proxy | R, L |
| Vendoring | O, L |
| Workspaces (`go.work`) | O |
| Standard project layout (`cmd/`, `internal/`, `pkg/`) | R, L |
| Build tags, cross-compilation (`GOOS/GOARCH`) | R, L |
| Static binaries (`CGO_ENABLED=0`) | R, L |

## 7. Standard Library (DevOps/SRE Relevant)
| Topic | Flag |
|---|---|
| `fmt`, `strings`, `strconv` | R |
| `io`, `bufio`, `os` | R, L |
| `net/http` (client, server, middleware) | R, E, L |
| `encoding/json`, YAML handling | R, L |
| `flag` / Cobra / Viper (CLI tooling) | R, L |
| `log/slog` (structured logging) | R, L |
| `time` (durations, tickers, timers) | R, L |
| `os/exec` | R, L |
| `os/signal` (graceful shutdown) | R, E, L |
| `net` (TCP/UDP basics) | O, L |
| `regexp` | O |
| `embed` | O |
| `text/template` | O, L |

## 8. Testing & Quality
| Topic | Flag |
|---|---|
| `testing` package, table-driven tests | R, E, L |
| Benchmarks | O, E |
| Mocks / interface-based test doubles | R, L |
| `httptest` | R, L |
| Test coverage | R, L |
| Fuzzing | O |
| Linting (`golangci-lint`, `go vet`) | R, L |

## 9. Performance & Observability
| Topic | Flag |
|---|---|
| `pprof` profiling | R, E, L |
| Memory model, escape analysis | O, E |
| Garbage collector basics (GOGC, GOMEMLIMIT) | R, E, L |
| Prometheus client library | R, L |
| OpenTelemetry (traces, metrics) | R, L |
| Health checks, readiness/liveness endpoints | R, L |
| Graceful shutdown | R, L |

## 10. DevOps/SRE Ecosystem in Go
| Topic | Flag |
|---|---|
| Why Go for infra (single binary, fast, concurrency) | R, E |
| `client-go` (Kubernetes API) | R, L |
| Kubernetes Operators / controller-runtime / Kubebuilder | R, L |
| Custom Resource Definitions (CRDs) in Go | O, L |
| Terraform provider / plugin SDK | O, L |
| Docker / containerd SDKs | O, L |
| gRPC & Protocol Buffers | R, E, L |
| REST API design in Go (Gin / Echo / Chi) | R, L |
| Writing CLIs and automation tools | R, L |
| Reading Go-based tools' source (K8s, Docker, Prometheus, Terraform, Argo) | O, L |

## 11. Design Patterns & Architecture
| Topic | Flag |
|---|---|
| Idiomatic Go ("accept interfaces, return structs") | R, E |
| Dependency injection (manual/wire) | R, L |
| Functional options pattern | R, L |
| Clean / hexagonal architecture in Go | O, E |
| Retry, backoff, circuit breaker, rate limiting | R, E, L |
| Configuration management (env,