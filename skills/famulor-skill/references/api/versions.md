# Versions API operations

Reviewed 2026-10-21. 5 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `deleteAssistantVersion` | `DELETE /assistants/{id}/versions/{versionId}` | `famulor delete-assistant-version` | [Delete assistant version](https://docs.famulor.io/api-reference/versions/delete-assistant-version) |
| `getAssistantVersion` | `GET /assistants/{id}/versions/{versionId}` | `famulor get-assistant-version` | [Get assistant version](https://docs.famulor.io/api-reference/versions/get-assistant-version) |
| `listAssistantVersions` | `GET /assistants/{id}/versions` | `famulor list-assistant-versions` | [List assistant versions](https://docs.famulor.io/api-reference/versions/list-assistant-versions) |
| `renameAssistantVersion` | `PATCH /assistants/{id}/versions/{versionId}` | `famulor rename-assistant-version` | [Rename assistant version](https://docs.famulor.io/api-reference/versions/rename-assistant-version) |
| `restoreAssistantVersion` | `POST /assistants/{id}/versions/{versionId}/restore` | `famulor restore-assistant-version` | [Restore assistant version](https://docs.famulor.io/api-reference/versions/restore-assistant-version) |
