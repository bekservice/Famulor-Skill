# Caller IDs API operations

Reviewed 2026-10-29. 4 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createCallerId` | `POST /caller-ids` | `famulor create-caller-id` | [Start caller ID verification](https://docs.famulor.io/api-reference/caller-ids/start-caller-id-verification) |
| `deleteCallerId` | `DELETE /caller-ids/{id}` | `famulor delete-caller-id` | [Delete caller ID](https://docs.famulor.io/api-reference/caller-ids/delete-caller-id) |
| `listCallerIds` | `GET /caller-ids` | `famulor list-caller-ids` | [List caller IDs](https://docs.famulor.io/api-reference/caller-ids/list-caller-ids) |
| `updateCallerId` | `PATCH /caller-ids/{id}` | `famulor update-caller-id` | [Update caller ID](https://docs.famulor.io/api-reference/caller-ids/update-caller-id) |
