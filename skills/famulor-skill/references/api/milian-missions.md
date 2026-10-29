# Milian Missions API operations

Reviewed 2026-10-29. 14 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createRoutine` | `POST /routines` | `famulor create-routine` | [Create a mission](https://docs.famulor.io/api-reference/milian-missions/create-a-mission) |
| `createRoutineVersionDraft` | `POST /routines/{id}/versions` | `famulor create-routine-version-draft` | [Save a mission draft](https://docs.famulor.io/api-reference/introduction) |
| `deleteRoutine` | `DELETE /routines/{id}` | `famulor delete-routine` | [Delete a mission](https://docs.famulor.io/api-reference/milian-missions/delete-a-mission) |
| `getRoutine` | `GET /routines/{id}` | `famulor get-routine` | [Get a mission](https://docs.famulor.io/api-reference/milian-missions/get-a-mission) |
| `getRoutineWebhook` | `GET /routines/{id}/webhook` | `famulor get-routine-webhook` | [Get mission webhook setup](https://docs.famulor.io/api-reference/introduction) |
| `listRoutineRuns` | `GET /routines/{id}/runs` | `famulor list-routine-runs` | [List mission runs](https://docs.famulor.io/api-reference/milian-missions/list-mission-runs) |
| `listRoutineVersions` | `GET /routines/{id}/versions` | `famulor list-routine-versions` | [List mission versions](https://docs.famulor.io/api-reference/introduction) |
| `listRoutines` | `GET /routines` | `famulor list-routines` | [List missions](https://docs.famulor.io/api-reference/milian-missions/list-missions) |
| `pauseRoutine` | `POST /routines/{id}/pause` | `famulor pause-routine` | [Pause a mission](https://docs.famulor.io/api-reference/introduction) |
| `publishRoutineVersion` | `POST /routines/{id}/publish` | `famulor publish-routine-version` | [Publish a mission version](https://docs.famulor.io/api-reference/introduction) |
| `retryRoutineRun` | `POST /routines/{id}/runs/{runId}/retry` | `famulor retry-routine-run` | [Retry a mission run](https://docs.famulor.io/api-reference/introduction) |
| `runRoutine` | `POST /routines/{id}/run` | `famulor run-routine` | [Run a mission now](https://docs.famulor.io/api-reference/milian-missions/run-a-mission-now) |
| `setRoutineWebhookSecret` | `POST /routines/{id}/webhook` | `famulor set-routine-webhook-secret` | [Set or rotate mission webhook secret](https://docs.famulor.io/api-reference/introduction) |
| `updateRoutine` | `PATCH /routines/{id}` | `famulor update-routine` | [Update a mission](https://docs.famulor.io/api-reference/milian-missions/update-a-mission) |
