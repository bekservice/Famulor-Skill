# Suppression API operations

Reviewed 2026-10-27. 3 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `addSuppressionEntry` | `POST /suppression-list` | `famulor add-suppression-entry` | [Add a suppression entry](https://docs.famulor.io/api-reference/suppression/add-a-suppression-entry) |
| `listSuppressionEntries` | `GET /suppression-list` | `famulor list-suppression-entries` | [List suppression entries](https://docs.famulor.io/api-reference/suppression/list-suppression-entries) |
| `removeSuppressionEntry` | `DELETE /suppression-list/{id}` | `famulor remove-suppression-entry` | [Restore contact consent](https://docs.famulor.io/api-reference/suppression/restore-contact-consent) |
