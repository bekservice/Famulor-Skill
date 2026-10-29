# Callbacks API operations

Reviewed 2026-10-29. 2 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `cancelScheduledCallback` | `PATCH /scheduled-callbacks/{id}` | `famulor cancel-scheduled-callback` | [Cancel a scheduled callback](https://docs.famulor.io/api-reference/callbacks/cancel-a-scheduled-callback) |
| `listScheduledCallbacks` | `GET /scheduled-callbacks` | `famulor list-scheduled-callbacks` | [List scheduled callbacks](https://docs.famulor.io/api-reference/callbacks/list-scheduled-callbacks) |
