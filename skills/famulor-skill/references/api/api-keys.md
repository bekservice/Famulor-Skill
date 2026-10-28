# API Keys API operations

Reviewed 2026-10-28. 4 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createApiKey` | `POST /api-keys` | `famulor create-api-key` | [Create an API key](https://docs.famulor.io/api-reference/api-keys/create-an-api-key) |
| `getApiKey` | `GET /api-keys/{id}` | `famulor get-api-key` | [Get an API key](https://docs.famulor.io/api-reference/api-keys/get-an-api-key) |
| `listApiKeys` | `GET /api-keys` | `famulor list-api-keys` | [List API keys](https://docs.famulor.io/api-reference/api-keys/list-api-keys) |
| `revokeApiKey` | `DELETE /api-keys/{id}` | `famulor revoke-api-key` | [Revoke an API key](https://docs.famulor.io/api-reference/api-keys/revoke-an-api-key) |
