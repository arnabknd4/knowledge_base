# Operating Systems: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How the OS solves it → Where you meet it in real systems
**Baseline:** Linux first (the cloud default), with Windows differences noted where they matter. Verify kernel-version specifics (io_uring, cgroup v2, eBPF features) against the distribution you target.

---

## 1. OS Role, Kernel Architecture & System Calls

### Topics
- Kernel space vs user space, privilege rings — R, E, L
- System calls and the cost of crossing the boundary — R, E, L
- Monolithic vs microkernel vs hybrid kernels — R, E
- Loadable kernel modules, drivers — O, E, L
- Interrupts, exceptions, traps — R, E
- Boot process (firmware, bootloader, init/systemd) — R, E, L
- Linux vs Windows architecture differences — R, E, L
- Virtualisation-aware OS (paravirtualisation, hypervisor types) — R, E, L
- Unikernels, library OSes (awareness) — O

### How the OS solves it
| Problem | OS answer |
|---|---|
| Protect the machine from buggy programs | Privilege separation + system call interface |
| Hardware diversity | Drivers and abstractions (files, sockets, processes) |
| Service management | Init system (systemd) with dependencies and restarts |
| Run many OS instances on one host | Hypervisor + guest kernels, or containers sharing one kernel |

### Where you meet it
- Slow syscalls inflate latency in chatty services (batching, `io_uring`, connection reuse).
- A container shares the host kernel, so a kernel bug is a shared risk.

---

## 2. Processes, Threads & Scheduling

### Topics
- Process vs thread vs coroutine/green thread/goroutine — R, E, L
- Process lifecycle, states, PCB, `fork`/`exec`, zombies and orphans — R, E, L
- Context switch cost (direct and cache/TLB side effects) — R, E, L
- Scheduling algorithms: FCFS, SJF, round robin, priority, MLFQ — R, E
- Linux CFS / EEVDF, priorities, nice values, real-time classes — R, E, L
- CPU affinity, NUMA awareness, pinning — R, E, L
- Multi-core scalability, Amdahl's law — R, E, L
- User-level vs kernel-level threads, M:N models — R, E, L
- Thread pools and sizing (CPU-bound vs I/O-bound) — R, E, L
- Signals and process control — R, L
- Real-time and priority inversion — O, E

### How the OS solves it
| Problem | OS answer |
|---|---|
| Many tasks, few cores | Preemptive time-sliced scheduler |
| Fairness vs latency | Scheduler policy and priorities |
| Cache-hostile migration | CPU affinity, NUMA policy |
| Runaway processes | Signals, limits, OOM killer, cgroups |

### Where you meet it
- Thread pool starvation, too many threads causing context-switch overhead.
- CPU throttling in Kubernetes from CFS quota limits (a classic latency mystery).
- Go/Java virtual threads and .NET async exist because OS threads are costly at scale.

---

## 3. Synchronisation, Concurrency & Deadlocks

### Topics
- Race conditions, critical sections — R, E, L
- Mutex, semaphore, condition variable, monitor, spinlock, read-write lock — R, E, L
- Atomic operations, compare-and-swap, memory ordering — R, E, L
- Lock-free and wait-free structures (awareness) — O, E, L
- Deadlock: four conditions, prevention, avoidance, detection, recovery — R, E, L
- Livelock, starvation, priority inversion — R, E, L
- Classic problems: producer-consumer, readers-writers, dining philosophers — R, E
- Futexes (fast userspace mutexes) — O, E
- Distributed vs local locks (why local lock reasoning does not carry over) — R, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Mutual exclusion | Mutexes/semaphores built on atomics and futexes |
| Waiting without burning CPU | Blocking primitives and wait queues |
| Deadlock | Lock ordering, timeouts, detection, avoidance |
| Cross-thread signalling | Condition variables, events, pipes |

### Where you meet it
- Database deadlocks and connection pool starvation mirror OS deadlock theory.
- Hot locks cap multi-core scaling; sharding state is usually the fix.

---

## 4. Memory Management

### Topics
- Virtual memory, address spaces, isolation — R, E, L
- Paging, page tables, multi-level tables, TLB — R, E, L
- Page faults (minor vs major), demand paging — R, E, L
- Page replacement: FIFO, LRU, Clock, working set — R, E
- Swapping, swap thrashing, swappiness — R, E, L
- Segmentation and fragmentation (internal/external) — R, E
- Memory allocators: malloc, jemalloc, tcmalloc, arenas — O, E, L
- Heap vs stack, stack overflow, memory leaks vs bloat — R, E, L
- `mmap`, shared memory, copy-on-write — R, E, L
- Huge pages, transparent huge pages trade-offs — O, E, L
- Overcommit and the OOM killer — R, E, L
- Cgroup memory limits and container OOM — R, E, L
- NUMA memory placement — O, E, L
- Garbage-collected runtimes and the OS (RSS vs heap) — R, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Isolation between processes | Per-process virtual address spaces |
| More memory than RAM | Paging and swap |
| Cheap process creation | Copy-on-write on `fork` |
| Fast file access | Page cache using free RAM |
| One process starving others | Cgroup limits + OOM killer |

### Where you meet it
- Containers killed with OOM even though the app "looks fine" (heap vs RSS, page cache accounting, limits).
- High major page faults signal memory pressure; swap thrashing destroys latency.
- JVM and Node heap sizing must respect container limits.

---

## 5. File Systems & Storage

### Topics
- File abstraction, inodes, directories, links (hard vs symbolic) — R, E, L
- File system types: ext4, XFS, Btrfs, ZFS, NTFS — R, E, L
- Journaling and crash consistency, copy-on-write file systems — R, E, L
- Page cache, write-back, `fsync` and durability — R, E, L
- Block layer, I/O schedulers, SSD vs HDD behaviour, NVMe — R, E, L
- RAID levels and trade-offs — R, E, L
- Network file systems (NFS, SMB), object stores vs file systems — R, E, L
- Overlay file systems and container image layers — R, E, L
- Disk quotas, inode exhaustion, file descriptor limits — R, E, L
- Logical volumes (LVM), snapshots — O, E, L
- Durability guarantees and database write paths (WAL) — R, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Crash during write | Journaling / copy-on-write |
| Slow disk | Page cache, read-ahead, I/O scheduling |
| Capacity and redundancy | RAID, LVM, replication |
| Shared storage across hosts | NFS/SMB, or object/block storage in the cloud |
| Container image reuse | Union/overlay file systems |

### Where you meet it
- "Disk full" caused by inodes or logs, not bytes.
- Databases call `fsync` because the page cache is volatile; durability settings drive latency.
- Choice between block, file and object storage is an architecture decision with OS-level consequences.

---

## 6. I/O, Networking & Event Models

### Topics
- Blocking vs non-blocking vs asynchronous I/O — R, E, L
- I/O multiplexing: `select`, `poll`, `epoll`, `kqueue`, IOCP — R, E, L
- `io_uring` (modern Linux async I/O) — O, E, L
- Zero-copy (`sendfile`, `splice`) — O, E, L
- Sockets, TCP state machine, backlog, TIME_WAIT, keepalive — R, E, L
- Network stack tuning: buffers, congestion control, MTU — O, E, L
- File descriptors as the universal handle; limits — R, E, L
- Interrupts, DMA, polling vs interrupt-driven I/O — R, E
- Event-loop model (Node, Nginx, Netty) vs thread-per-request — R, E, L
- Reverse proxies, connection pooling, port exhaustion — R, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Thousands of connections | `epoll`/`kqueue`/IOCP readiness or completion models |
| Copy overhead for file serving | Zero-copy syscalls |
| Slow device vs fast CPU | DMA and interrupts |
| Connection state tracking | Kernel TCP stack and socket buffers |

### Where you meet it
- Why Node/Nginx handle high concurrency (epoll event loop) and why thread-per-request needs pools or virtual threads.
- "Too many open files", ephemeral port exhaustion, TIME_WAIT buildup.

---

## 7. Containers, Isolation & Virtualisation

### Topics
- Namespaces (pid, net, mnt, uts, ipc, user) — R, E, L
- Cgroups v1/v2: CPU, memory, I/O limits — R, E, L
- Container vs VM isolation and security trade-offs — R, E, L
- Capabilities, seccomp, AppArmor/SELinux — R, E, L
- Rootless containers, user namespaces — O, E, L
- Container runtimes (containerd, runc), sandboxed runtimes (gVisor, Kata) — O, E, L
- Hypervisors: Type 1 vs Type 2, hardware virtualisation (VT-x), nested virtualisation — R, E, L
- MicroVMs (Firecracker) behind serverless — O, E, L
- Resource requests/limits in Kubernetes mapped to cgroups — R, E, L
- Noisy neighbour, CPU throttling, memory pressure in shared hosts — R, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Process-level isolation without VMs | Namespaces + cgroups |
| Limit blast radius | Capabilities, seccomp, MAC policies |
| Strong tenant isolation | VMs/microVMs, sandboxed runtimes |
| Fair resource sharing | Cgroup quotas and weights |

### Where you meet it
- Multi-tenant platforms choose containers (density) vs microVMs (isolation) by threat model.
- Serverless platforms rely on microVM-style isolation with fast startup.

---

## 8. Security & Access Control

### Topics
- Users, groups, permissions, ACLs, setuid, sudo — R, E, L
- Authentication modules (PAM), SSH key management — R, E, L
- Principle of least privilege on hosts and containers — R, E, L
- Mandatory access control: SELinux, AppArmor — R, E, L
- Process isolation, ASLR, DEP/NX, stack protections — O, E, L
- Kernel hardening, patching and live patching — R, E, L
- Secrets in memory and environment, core dumps — R, E, L
- Audit logging (auditd) — O, L
- Speculative execution vulnerabilities (Spectre/Meltdown) and mitigations cost — O, E
- Supply chain at OS level: base images, package trust — R, E, L
- Windows specifics: Active Directory, ACLs, UAC (awareness) — O, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| Who can do what | Permissions, ACLs, capabilities |
| Compromised process | MAC policies, sandboxing, namespaces |
| Exploit mitigation | ASLR, NX, stack canaries |
| Vulnerable kernel/packages | Patching, minimal base images, live patching |

### Where you meet it
- Hardened minimal images and non-root containers are baseline expectations in audits.

---

## 9. Observability & Troubleshooting

### Topics
- Core signals: CPU, memory, disk, network, load average meaning — R, E, L
- USE method (utilisation, saturation, errors) — R, E, L
- Tools: `top`/`htop`, `vmstat`, `iostat`, `ss`, `lsof`, `strace`, `perf`, `sar` — R, E, L
- `/proc` and `/sys` as diagnostic interfaces — R, E, L
- eBPF-based tracing and observability — O, E, L
- Flame graphs and profiling — O, L
- Logs: journald, syslog, log rotation — R, L
- Core dumps, crash analysis — O, L
- Common incident patterns: CPU saturation, memory leak, disk full, fd exhaustion, network drops — R, E, L

### How the OS solves it
| Problem | OS answer |
|---|---|
| "Why is it slow?" | USE method over CPU/memory/disk/network |
| Trace a hanging process | `strace`, `perf`, eBPF tools |
| Resource exhaustion | `ulimit`, cgroups, quotas, alerts |

### Where you meet it
- Load average includes uninterruptible I/O wait, so it is not only CPU.
- Most production incidents map to one of five resource classes.

---

## 10. Performance & Capacity Architecture

### Topics
- Latency vs throughput vs saturation — R, E, L
- Cache hierarchy, locality, false sharing — R, E, L
- NUMA, CPU frequency, power states — O, E, L
- Kernel tuning (sysctl) and when not to tune — R, E, L
- Right-sizing instances and vCPU meaning (hyperthread vs core) — R, E, L
- Burstable instances and CPU credits — R, E, L
- I/O capacity planning (IOPS, throughput, queue depth) — R, E, L
- Memory-vs-disk trade-offs for caches and databases — R, E, L
- Real-time and low-latency design (isolated cores, busy polling) — O, E

### How the OS solves it
| Problem | OS answer |
|---|---|
| Latency spikes | Core isolation, affinity, reduced context switching |
| Predictable I/O | Provisioned IOPS, scheduler choice, queue sizing |
| Efficient cache use | Page cache, locality-friendly layouts |

### Where you meet it
- Cloud instance sizing, burst credits and noisy neighbours are OS-level resource economics.

---

## Mental Model (one line each)
- **The OS multiplexes and protects:** CPU (scheduler), memory (virtual memory), storage (file systems), devices (drivers, I/O).
- **Everything is a file descriptor:** files, sockets, pipes; limits matter.
- **Cost model:** syscalls, context switches and page faults are the hidden taxes.
- **Containers are not VMs:** shared kernel with namespaces for isolation and cgroups for limits.
- **Debugging lens:** check CPU, memory, disk, network for utilisation, saturation, errors.
- **Durability:** page cache is volatile until `fsync`.

## Top Interview Hotspots
1. Process vs thread vs coroutine and their cost models
2. Context switching and why too many threads hurt
3. Virtual memory, paging, page faults, TLB
4. Deadlock conditions and prevention
5. `epoll`/event loop vs thread-per-request
6. Containers: namespaces + cgroups, and container vs VM isolation
7. OOM killer and container memory behaviour
8. File system durability: page cache, `fsync`, journaling
9. Troubleshooting a slow server with the USE method
10. Kubernetes CPU limits and throttling

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Processes, threads, scheduling and context-switch costs
2. Virtual memory, paging, page cache, OOM behaviour
3. Concurrency primitives and deadlocks
4. I/O models: blocking, non-blocking, `epoll`, event loops
5. Containers: namespaces, cgroups, isolation trade-offs
6. File system durability and storage types
7. Troubleshooting with USE method and core tools
8. Resource limits in Kubernetes and cloud sizing

## Tier 2: Working knowledge (~30%)
- Security basics: permissions, capabilities, MAC, hardening
- Networking stack behaviour (TCP states, port exhaustion)
- Scheduling algorithms (theory) and NUMA basics
- Virtualisation and hypervisor types
- RAID, LVM, snapshots

## Tier 3: Awareness only (~10%)
- eBPF, `io_uring`, unikernels
- Microkernel design, real-time OS
- Speculative execution mitigations
- Windows internals specifics

## Drop for now
- Writing kernel modules or drivers
- Deep boot-loader and firmware details
- Classical algorithms beyond interview awareness (banker's algorithm math)

---

# Steady 4-Week Plan

*Assumes ~1 hr/day. You already have Linux, Docker, Kubernetes and Shell/Bash notes, so this plan focuses on the underlying model and trade-offs, not commands.*

| Week | Focus | Output |
|---|---|---|
| **1** | Kernel/syscalls, processes, threads, scheduling, context-switch cost | One-page notes: process vs thread vs coroutine; explain Kubernetes CPU throttling in OS terms |
| **2** | Memory management, page cache, OOM, swap, containers' memory accounting | Diagnose a container OOM scenario on paper: heap vs RSS vs page cache vs limit |
| **3** | Concurrency, deadlocks, I/O models, `epoll`, sockets, event loops | Compare thread-per-request, event loop and virtual threads in a table with limits of each |
| **4** | File systems and durability, containers (namespaces/cgroups), security, troubleshooting, interview revision | USE-method checklist; container vs VM vs microVM decision table; mock interviews on Top 10 |

## Daily rhythm
- **25 min** concept (one module)
- **20 min** hands-on on a Linux box or container (`vmstat`, `strace`, `/proc`, cgroup files)
- **15 min** revision (5 lines: problem → OS answer → real-system symptom)

## Weekly checkpoints
- **Day 6:** Revise with Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does the OS mechanism solve?
2. **What does it cost** (latency, memory, complexity)?
3. **What symptom** appears in production when it goes wrong?
4. **What design choice** would you make differently because of it?