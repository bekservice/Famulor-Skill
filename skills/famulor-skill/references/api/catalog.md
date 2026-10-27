# Catalog API operations

Reviewed 2026-10-27. 3 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `listLanguages` | `GET /languages` | `famulor list-languages` | [List languages](https://docs.famulor.io/api-reference/catalog/list-languages) |
| `listModels` | `GET /models` | `famulor list-models` | [List models](https://docs.famulor.io/api-reference/catalog/list-models) |
| `listPromptTemplates` | `GET /prompt-templates` | `famulor list-prompt-templates` | [List prompt templates](https://docs.famulor.io/api-reference/catalog/list-prompt-templates) |
