# QA API operations

Reviewed 2026-10-21. 3 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createQaRun` | `POST /qa/runs` | `famulor create-qa-run` | [Create QA run](https://docs.famulor.io/api-reference/qa/create-qa-run) |
| `getQaRun` | `GET /qa/runs/{id}` | `famulor get-qa-run` | [Get QA run](https://docs.famulor.io/api-reference/qa/get-qa-run) |
| `listQaRuns` | `GET /qa/runs` | `famulor list-qa-runs` | [List QA runs](https://docs.famulor.io/api-reference/qa/list-qa-runs) |
