# Configure Azure DNS

## What

Azure DNS hosts DNS zones and records using Azure infrastructure. Public DNS zones publish internet-resolvable names; private DNS zones resolve names within linked VNets. Azure-provided DNS also resolves names for resources inside VNets, while custom DNS servers can be configured at VNet scope.

## Why

DNS is part of the packet path and a common source of private connectivity failure. Public and private namespaces have distinct visibility and operational ownership. Private DNS is essential for many private endpoint scenarios; wrong links or duplicate records can direct clients to unreachable endpoints.

## How

For public DNS, create a public zone, publish records, and delegate the domain at the registrar to the Azure name servers. For private DNS, create a private zone, link the intended VNets, and manage records or use service integrations such as private endpoint DNS zone groups. VNet DNS configuration may use Azure-provided resolution or custom server IPs; clients may need DHCP renewal/restart to receive updated settings. Hybrid resolution usually needs forwarding/resolver architecture.

Troubleshoot by querying from the actual client context and checking resolver configuration, zone visibility/link state, record TTL and value, forwarding, and network path to the returned address. Changes propagate subject to TTL and caching. Use health checks and controlled change processes for production DNS.

## Features

- Public authoritative DNS hosting and private DNS zones.
- VNet links control which networks can resolve a private zone.
- Record sets include A/AAAA, CNAME, MX, TXT, and other DNS types.
- Azure Private DNS Resolver supports hybrid DNS architectures.

## Code snippets (if any)

```bash
az network dns zone create --resource-group <rg> --name <public-domain.example>
az network dns record-set a add-record --resource-group <rg> --zone-name <public-domain.example> --record-set-name www --ipv4-address <public-ip>
```

For a private zone, use `az network private-dns zone` and link the intended VNet.

## Do's and Don'ts

- **Do** distinguish public zones from private zones and manage delegation/links explicitly.
- **Do** test resolution from the consumer network, not only from an administrator's workstation.
- **Don't** assume a private zone is visible to every VNet.
- **Don't** forget registrar delegation for public authoritative zones.
- **Don't** manually create conflicting records where service-managed DNS integration owns them.

## Real-life implementation

Publish a public application name through an Azure public zone and point it to a stable frontend IP. For private service access, use a private zone linked only to client VNets and forward the relevant namespace from on-premises DNS when needed. Document record owners, TTLs, and rollback values; validate both external and internal answers before a cutover.

## Q&A

1. **What is the key difference between public and private DNS zones?** Public zones are globally resolvable through DNS delegation; private zones resolve only in linked/connected resolver contexts.
2. **Why does a private endpoint still resolve publicly?** Its private DNS zone may be absent, unlinked, or not queried by the client.
3. **What makes an Azure public DNS zone authoritative for a domain?** The domain registrar must delegate the domain to the zone's Azure name servers.
4. **Do DNS updates take effect instantly?** Not necessarily; TTLs and resolver/client caches affect propagation.

---
Source: [Microsoft Learn — Azure DNS overview](https://learn.microsoft.com/azure/dns/dns-overview) · [Microsoft Learn — Private DNS overview](https://learn.microsoft.com/azure/dns/private-dns-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
