# Shopify API operations

Reviewed 2026-10-28. 16 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `disconnectShopifyInstallation` | `DELETE /shopify/installations/{id}` | `famulor disconnect-shopify-installation` | [Disconnect Shopify store](https://docs.famulor.io/api-reference/shopify/disconnect) |
| `getShopifyAssociatedRevenue` | `GET /shopify/installations/{id}/revenue` | `famulor get-shopify-associated-revenue` | [Read associated Shopify payments](https://docs.famulor.io/api-reference/shopify/revenue) |
| `getShopifyCall` | `GET /shopify/installations/{id}/calls/{callId}` | `famulor get-shopify-call` | [Get store conversation](https://docs.famulor.io/api-reference/shopify/call) |
| `getShopifyPrivacyExport` | `GET /shopify/installations/{id}/privacy-exports/{exportId}` | `famulor get-shopify-privacy-export` | [Get prepared privacy report](https://docs.famulor.io/api-reference/shopify/privacy-export) |
| `getShopifySetup` | `GET /shopify/setup` | `famulor get-shopify-setup` | [Read Shopify setup](https://docs.famulor.io/api-reference/shopify/setup) |
| `getShopifyWidgetPicker` | `GET /shopify/installations/{id}/widgets` | `famulor get-shopify-widget-picker` | [Read Shopify widget choices](https://docs.famulor.io/api-reference/shopify/widgets) |
| `listShopifyActions` | `GET /shopify/actions` | `famulor list-shopify-actions` | [List Shopify assistant actions](https://docs.famulor.io/api-reference/shopify/actions) |
| `listShopifyAssistantTools` | `GET /shopify/installations/{id}/tools` | `famulor list-shopify-assistant-tools` | [List Shopify assistant tools](https://docs.famulor.io/api-reference/shopify/tools) |
| `listShopifyHistory` | `GET /shopify/installations/{id}/history` | `famulor list-shopify-history` | [List store activity](https://docs.famulor.io/api-reference/shopify/history) |
| `listShopifyInstallations` | `GET /shopify/installations` | `famulor list-shopify-installations` | [List linked Shopify stores](https://docs.famulor.io/api-reference/shopify/stores) |
| `listShopifyPrivacyExports` | `GET /shopify/installations/{id}/privacy-exports` | `famulor list-shopify-privacy-exports` | [List prepared privacy reports](https://docs.famulor.io/api-reference/shopify/privacy-exports) |
| `listShopifySupportRequests` | `GET /shopify/installations/{id}/requests` | `famulor list-shopify-support-requests` | [List store support requests](https://docs.famulor.io/api-reference/shopify/requests) |
| `provisionShopifyAssistantTools` | `POST /shopify/installations/{id}/tools` | `famulor provision-shopify-assistant-tools` | [Add Shopify assistant tools](https://docs.famulor.io/api-reference/shopify/provision-tools) |
| `resolveShopifySupportRequest` | `PATCH /shopify/installations/{id}/requests` | `famulor resolve-shopify-support-request` | [Record store request resolution](https://docs.famulor.io/api-reference/shopify/resolve-request) |
| `synchronizeShopifyWidgetPicker` | `POST /shopify/installations/{id}/widgets` | `famulor synchronize-shopify-widget-picker` | [Synchronize Shopify widget choices](https://docs.famulor.io/api-reference/shopify/synchronize-widgets) |
| `updateShopifyCapabilities` | `PATCH /shopify/installations/{id}/capabilities` | `famulor update-shopify-capabilities` | [Configure Shopify capabilities](https://docs.famulor.io/api-reference/shopify/capabilities) |
