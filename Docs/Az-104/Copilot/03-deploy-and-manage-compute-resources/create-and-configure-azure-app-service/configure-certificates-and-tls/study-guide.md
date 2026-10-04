# Configure certificates and TLS for an App Service

## What
Configure TLS termination for an App Service hostname using a platform-provided hostname or custom domain, including certificate binding, supported TLS protocol settings, and HTTPS redirection/enforcement.

## Why
TLS protects confidentiality and integrity in transit and proves hostname identity. Certificate choice affects renewal, key custody, domain coverage, and cost. TLS only on the client-to-edge hop may be insufficient where end-to-end encryption is required; define each trust boundary.

## How
First map/verify the custom domain, then add or import an eligible certificate (managed certificate where supported, App Service certificate, or uploaded certificate) and bind it with SNI or IP-based TLS as appropriate. Set minimum TLS version according to compatibility policy, enable HTTPS-only, and redirect HTTP at the application if needed. Monitor expiry/renewal, validate the complete chain and hostname, and test clients. For private backends, configure TLS separately for those connections.

## Features
App Service supports managed certificates for eligible hostnames and imported certificates, with tier/domain limitations. SNI TLS binding supports multiple hostnames on an IP; IP-based TLS has additional IP implications. TLS protocol settings and certificate lifecycle vary by platform and tier. HTTPS-only is a site setting; application-level redirection may still be needed for appropriate behavior.

## Code snippets (if any)
No snippet required: certificate import and binding depend on certificate source, custom hostname, and plan tier. Never paste a private key or password into a command example or source file.

## Do's and Don'ts
**Do** automate renewal monitoring and verify hostname/chain. **Don't** treat HTTPS-only as proof all backend traffic is encrypted or reduce TLS minimum without an explicit compatibility need.

## Real-life implementation
A customer-facing site uses an eligible managed certificate for the verified custom domain, SNI binding, HTTPS-only, a modern minimum TLS policy, and an expiry alert. A staging slot is tested after certificate binding changes before production.

## Q&A
1. **What does SNI enable?** Multiple TLS hostnames/certificates can share an IP address.
2. **Does binding a certificate automatically redirect HTTP to HTTPS?** Not necessarily; enable HTTPS-only and configure redirect behavior.
3. **Does browser TLS guarantee encrypted service-to-service traffic?** No. Each backend hop must be configured and validated separately.

**References:** [Secure a custom DNS name with TLS](https://learn.microsoft.com/azure/app-service/configure-ssl-certificate) · [Configure TLS settings](https://learn.microsoft.com/azure/app-service/tls-minimum-version)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
