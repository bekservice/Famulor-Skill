# Migrations API operations

Reviewed 2026-10-28. 2 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `migrateFamulor1` | `POST /migrations/famulor` | `famulor migrate-famulor1` | [Preview or import Famulor 1.0 data](https://docs.famulor.io/api-reference/migrations/preview-or-import-famulor-10-data) |
| `migrateProviderAssistants` | `POST /migrations/providers` | `famulor migrate-provider-assistants` | [Preview or import provider assistants](https://docs.famulor.io/api-reference/migrate-provider-assistants) |
