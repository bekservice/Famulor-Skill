# Webhook Subscriptions API operations

Reviewed 2026-10-28. 4 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createWebhookSubscription` | `POST /webhooks` | `famulor create-webhook-subscription` | [Create a signed webhook subscription](https://docs.famulor.io/api-reference/webhooks/create-webhook-subscription) |
| `deleteWebhookSubscription` | `DELETE /webhooks/{id}` | `famulor delete-webhook-subscription` | [Delete a webhook subscription](https://docs.famulor.io/api-reference/webhooks/delete-webhook-subscription) |
| `getWebhookSubscription` | `GET /webhooks/{id}` | `famulor get-webhook-subscription` | [Get a webhook subscription](https://docs.famulor.io/api-reference/webhooks/get-webhook-subscription) |
| `listWebhookSubscriptions` | `GET /webhooks` | `famulor list-webhook-subscriptions` | [List webhook subscriptions](https://docs.famulor.io/api-reference/webhooks/list-webhook-subscriptions) |
