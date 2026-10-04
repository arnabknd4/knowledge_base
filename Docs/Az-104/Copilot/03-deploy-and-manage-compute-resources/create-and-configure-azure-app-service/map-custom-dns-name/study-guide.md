# Map an existing custom DNS name to an App Service

## What
Map a registered hostname to an App Service by creating the required DNS record and validating domain ownership before adding the hostname and TLS binding.

## Why
Custom DNS supports brand and stable service names independent of Azure-generated hostnames. DNS choice (CNAME, A, or alias where applicable) affects apex-domain support, IPv4 address changes, verification, and cutover. DNS alone does not configure HTTPS or guarantee that traffic reaches the intended app.

## How
In App Service, add the custom domain to see required records and ownership verification. At the authoritative DNS provider, create the indicated CNAME for a subdomain or A/alias records for a zone apex as supported; add the TXT verification record to prevent hostname takeover. Wait for propagation, validate ownership, add the hostname, then bind TLS and enforce HTTPS. For migration, lower TTL ahead of cutover and preserve the old service during propagation.

## Features
App Service domain validation uses DNS records; a TXT verification token establishes ownership independently of routing. CNAME is generally used for subdomains; apex/root records need provider-supported alias/flattening or an A record and require attention to IP changes. DNS TTL affects caching, not certificate or app readiness.

## Code snippets (if any)
No snippet required: exact DNS values are generated for the app and vary by domain/provider. Copy records from the App Service custom-domain wizard and verify them with the authoritative DNS provider.

## Do's and Don'ts
**Do** add the verification TXT record and test DNS before switching production traffic. **Don't** assume a CNAME can be placed at a standard zone apex or forget to bind TLS after hostname validation.

## Real-life implementation
Before moving a production subdomain, lower its TTL, add required ownership verification, validate the new app and certificate, then update the routing record. Keep the old endpoint available through the TTL and rollback window.

## Q&A
1. **Which record commonly maps `www` to App Service?** A CNAME, plus the prescribed TXT ownership record.
2. **Why use a TXT verification record?** To prove domain ownership and reduce risk of another tenant claiming the hostname.
3. **Does custom-domain validation create TLS automatically?** No; certificate issuance/import and binding are separate configuration steps.

**References:** [Map an existing custom DNS name](https://learn.microsoft.com/azure/app-service/app-service-web-tutorial-custom-domain) · [App Service custom domains](https://learn.microsoft.com/azure/app-service/app-service-web-tutorial-custom-domain)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
