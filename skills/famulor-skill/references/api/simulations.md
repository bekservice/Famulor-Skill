# Simulations API operations

Reviewed 2026-10-21. 6 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createAssistantTest` | `POST /assistants/{id}/tests` | `famulor create-assistant-test` | [Create simulation test](https://docs.famulor.io/api-reference/simulations/create-simulation-test) |
| `createAssistantTestFromCall` | `POST /assistants/{id}/tests/from-call` | `famulor create-assistant-test-from-call` | [Create simulation test from call](https://docs.famulor.io/api-reference/simulations/create-simulation-test-from-call) |
| `deleteAssistantTest` | `DELETE /assistants/{id}/tests/{testId}` | `famulor delete-assistant-test` | [Delete simulation test](https://docs.famulor.io/api-reference/simulations/delete-simulation-test) |
| `listAssistantTests` | `GET /assistants/{id}/tests` | `famulor list-assistant-tests` | [List simulation tests](https://docs.famulor.io/api-reference/simulations/list-simulation-tests) |
| `runAssistantTest` | `POST /assistants/{id}/tests/{testId}/run` | `famulor run-assistant-test` | [Run simulation test](https://docs.famulor.io/api-reference/simulations/run-simulation-test) |
| `updateAssistantTest` | `PATCH /assistants/{id}/tests/{testId}` | `famulor update-assistant-test` | [Update simulation test](https://docs.famulor.io/api-reference/simulations/update-simulation-test) |
