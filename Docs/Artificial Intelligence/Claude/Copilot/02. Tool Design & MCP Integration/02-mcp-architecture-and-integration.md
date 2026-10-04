# MCP Architecture and Integration · Architect · R / E / L

> **Exam note:** MCP concepts are product-grounded; whether this exam tests specific primitives or transports is unverified.

## 1. In one line
MCP is an open protocol for AI applications to connect with external systems through standardized client/server interactions.

## 2. Problem it solves
- **Without a protocol:** every AI host and service needs bespoke integration glue.
- **With MCP:** compatible clients can discover and use server-provided capabilities through a shared protocol, while deployment and trust remain explicit concerns.

## 3. 30-second architecture sketch
```text
AI host / MCP client
  <-> negotiated MCP connection/transport
      <-> MCP server
          -> tools: perform operations
          -> resources: expose context/data
          -> prompts: reusable prompt templates
```
Exact support depends on the MCP client, server, protocol version, and transport.

## 4. Mental model
MCP standardizes the connector contract; it does not certify the connected server, authorize a user, or decide whether an action is safe.

## 5. Under the hood
1. The host/client connects to a configured server using a supported transport and protocol version.
2. The client discovers capabilities supported by that server and host.
3. Tools represent callable operations; resources expose data/context; prompts provide reusable prompt templates.
4. The host/model uses supported capabilities according to client policy; the server validates and performs its own authorization and business checks.
5. Connection, authentication, consent, logging, and lifecycle vary by host and deployment model.

## 6. Variants and when to use
| Integration | Use when | Trade-off |
|---|---|---|
| Local process/server | Local tool or data integration with controlled environment | Deployment and local trust management |
| Remote server | Shared service or remote data/action boundary | Network, identity, and transport security obligations |
| Claude Code MCP config | Extend developer workflow through configured servers | Claude Code-specific configuration semantics |
| Messages API MCP connector | Use supported remote MCP integration directly through the API | Feature/transport/support limitations; verify current status |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Treating MCP as a trust guarantee | Protocol compatibility says nothing about safety | Vet servers, restrict capabilities, authenticate, authorize |
| Assuming every host supports all primitives | Clients expose different feature subsets | Check host and server support/version |
| Confusing MCP tools with API server tools | Similar names, different execution/configuration model | Draw the actual runtime and data path |
| Overly broad server credentials | Compromise reaches unrelated systems | Use least privilege, scoped credentials, rotation |
| Sending sensitive context indiscriminately | Tool servers become a data exposure boundary | Minimize fields and review retention/logging |

## 8. Performance, memory, and concurrency
- **Latency:** remote calls add network and server latency; use deadlines and surface unavailable services.
- **Concurrency:** bound parallel calls and consider server quotas, ordering, and resource contention.
- **Observability:** correlate host request, MCP call, server operation, and external result without logging secrets.
- **Testing:** verify capability discovery, denied permissions, server outage, malformed result, credential expiry, and protocol mismatch.

## 9. Related topics map
- **Prerequisites:** client/server architecture, tool contracts, identity and authorization
- **Siblings:** Claude API tools, Claude Code tools, resources and prompts
- **Downstream:** secret management, error handling, provenance, audit
- **Contrasts:** one-off bespoke integration, direct API call
- **Tools/frameworks:** Model Context Protocol; Claude Code MCP; API MCP connector (support may vary)

## 10. Cross-domain equivalents
| MCP concept | Architectural analogy | Caveat |
|---|---|---|
| MCP client | Connector/host integration layer | Host controls exposure and consent |
| MCP server | Service adapter | Still owns its security and correctness |
| MCP tool | Callable operation | Must enforce authorization and validate input |
| MCP resource | Addressable context/data | Access and freshness are server-dependent |
| MCP prompt | Reusable prompt template | Not an enforcement mechanism |

## 11. Interview lens
- **30-second answer:** MCP standardizes AI-to-system connectivity; I still treat each server as an external trust boundary, check client feature support, scope credentials and capabilities, and enforce server-side authorization.
- **Q1 → Do resources, tools, and prompts mean the same thing?** No: tools perform operations, resources expose data/context, and prompts provide reusable prompt templates.
- **Q2 → Does MCP handle all authorization?** No. Identity propagation and authorization depend on host, transport, server, and deployment; enforce access where the resource/action is owned.
- **Spot the bug:** A remote server is accepted because it implements MCP.  
  **Problem:** protocol conformance does not establish trust. **Fix:** review source/operator, permissions, auth, network exposure, data handling, and action impact.

## 12. Architect lens
- Map the full data flow: user → host → model → client → server → system of record.
- Specify who authenticates, which identity is forwarded, where consent is collected, and where authorization is enforced.
- **Version note:** MCP spec version, transport, and host support evolve; verify compatibility before implementation.

## 13. Revision summary
- MCP is a standard connector protocol, not a security stamp.
- Tools, resources, and prompts have different roles.
- Support differs by client, server, version, and transport.
- Secure the server and data path end to end.
- **If you remember only one thing:** Standardized connectivity does not remove system-boundary security responsibilities.

## 14. Coverage self-check
- [ ] Can I draw MCP client/server boundaries?
- [ ] Can I distinguish tools, resources, and prompts?
- [ ] Can I explain host-specific support and transport caveats?
- [ ] Can I locate authentication, authorization, consent, and logging?

## Sources
- [MCP introduction](https://modelcontextprotocol.io/introduction)
- [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp)
- [Claude API MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
