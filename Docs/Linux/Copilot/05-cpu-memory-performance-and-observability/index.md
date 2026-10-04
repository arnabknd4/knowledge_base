# 05. CPU, memory, performance, and observability

Study guides mapped one-to-one to syllabus checkboxes in [the Linux syllabus](../copilot-Linux-syllabus.md).

## Performance and observability

- [Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.](01-performance-and-observability/001-interpret-load-average-in-context-distinguish-runnable-work-cpu/study-guide.md)
- [Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.](01-performance-and-observability/002-understand-virtual-memory-page-cache-reclaim-swap-overcommit-oom/study-guide.md)
- [Inspect CPU, memory, pressure, disk, and network symptoms using standard process and system statistics tools.](01-performance-and-observability/003-inspect-cpu-memory-pressure-disk-and-network-symptoms-using-stan/study-guide.md)
- [Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.](01-performance-and-observability/004-read-proc-and-sys-as-kernel-interfaces-recognize-that-values-and/study-guide.md)
- [Understand latency, throughput, utilization, saturation, errors, and queue depth; form hypotheses from time-correlated metrics rather than a single snapshot.](01-performance-and-observability/005-understand-latency-throughput-utilization-saturation-errors-and/study-guide.md)
- [Use logs, metrics, traces, profiling, and events as complementary observability signals; define useful host-level telemetry and alert context (S).](01-performance-and-observability/006-use-logs-metrics-traces-profiling-and-events-as-complementary-ob/study-guide.md)
- [Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).](01-performance-and-observability/007-learn-vmstat-iostat-sar-pidstat-top-ps-free-ss-lsof-strace-and-p/study-guide.md)
- [Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).](01-performance-and-observability/008-understand-ebpf-based-observability-and-its-kernel-privilege-too/study-guide.md)
- [Evaluate kernel and service tuning using workload measurements, documented tradeoffs, staged rollout, and rollback; avoid copying generic tuning recipes.](01-performance-and-observability/009-evaluate-kernel-and-service-tuning-using-workload-measurements-d/study-guide.md)
- [Relate kernel counters and host symptoms to application SLOs and service-level telemetry (S, A).](01-performance-and-observability/010-relate-kernel-counters-and-host-symptoms-to-application-slos-and/study-guide.md)

## Domain scope

This is domain `05` of the objective library. Role extensions are separated in domain 13; safety and readiness outcomes are separated in domain 14.
