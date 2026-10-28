# Public API operation index

Reviewed 2026-10-28: **501 operations across 40 areas**. Every operation is cross-checked against the generated CLI catalog and TypeScript SDK descriptors.

Use this index to find the right endpoint. Open only the relevant area; use [API, CLI and SDK guidance](../api-and-sdk.md) for authentication, execution and verification. Public reseller operations remain subject to the authenticated workspace's entitlement and permissions.

Inspect a request's parameters, body constraints, actual CLI flags and response media types without network access:

```bash
python3 skills/famulor-skill/scripts/find-operation.py createAssistant
python3 skills/famulor-skill/scripts/find-operation.py --search whatsapp
```

When installed separately, run the script from your installed skill folder as `python3 scripts/find-operation.py ...`. The lookup includes only reachable request-schema definitions. It omits examples, default values and response properties; the live public OpenAPI and installed client's help remain authoritative.

The full API uses `https://app.famulor.io/api/v1` plus the relative paths shown here. The SDK method is always `client.api.<operationId>`. MCP tool names and schemas are separate; use the [MCP toolset references](../toolsets/assistants.md) to discover them instead of translating API names.

| Area | Operations | Reference |
| --- | ---: | --- |
| API Keys | 4 | [API Keys](api-keys.md) |
| Account | 4 | [Account](account.md) |
| Assistants | 21 | [Assistants](assistants.md) |
| Automations | 43 | [Automations](automations.md) |
| Avatars | 7 | [Avatars](avatars.md) |
| Billing | 15 | [Billing](billing.md) |
| Bookings | 13 | [Bookings](bookings.md) |
| Callbacks | 2 | [Callbacks](callbacks.md) |
| Caller IDs | 4 | [Caller IDs](caller-ids.md) |
| Calls | 13 | [Calls](calls.md) |
| Campaigns | 12 | [Campaigns](campaigns.md) |
| Carrier Connections | 9 | [Carrier Connections](carrier-connections.md) |
| Catalog | 3 | [Catalog](catalog.md) |
| Dashboards | 12 | [Dashboards](dashboards.md) |
| Famulor Loop | 38 | [Famulor Loop](famulor-loop.md) |
| History | 13 | [History](history.md) |
| Integrations | 16 | [Integrations](integrations.md) |
| Knowledge Bases | 31 | [Knowledge Bases](knowledge-bases.md) |
| Leads | 16 | [Leads](leads.md) |
| Messaging | 36 | [Messaging](messaging.md) |
| Migrations | 2 | [Migrations](migrations.md) |
| Milian | 2 | [Milian](milian.md) |
| Milian Missions | 14 | [Milian Missions](milian-missions.md) |
| Phone Numbers | 15 | [Phone Numbers](phone-numbers.md) |
| QA | 3 | [QA](qa.md) |
| SIP Trunks | 5 | [SIP Trunks](sip-trunks.md) |
| SMS | 1 | [SMS](sms.md) |
| Segments | 6 | [Segments](segments.md) |
| Settings | 29 | [Settings](settings.md) |
| Shopify | 16 | [Shopify](shopify.md) |
| Simulations | 6 | [Simulations](simulations.md) |
| Suppression | 3 | [Suppression](suppression.md) |
| Tools | 18 | [Tools](tools.md) |
| Translation | 7 | [Translation](translation.md) |
| Versions | 5 | [Versions](versions.md) |
| Voices | 9 | [Voices](voices.md) |
| Webhook Subscriptions | 4 | [Webhook Subscriptions](webhook-subscriptions.md) |
| White Label | 29 | [White Label](white-label.md) |
| Widgets | 7 | [Widgets](widgets.md) |
| Workspaces | 8 | [Workspaces](workspaces.md) |
