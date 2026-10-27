# Translation API operations

Reviewed 2026-10-27. 7 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `callTranslationSpeaker` | `POST /translation-sessions/{id}/call` | `famulor call-translation-speaker` | [Call a translation participant](https://docs.famulor.io/api-reference/translation/call) |
| `createTranslationSession` | `POST /translation-sessions` | `famulor create-translation-session` | [Create a translation room](https://docs.famulor.io/api-reference/translation/create) |
| `endTranslationSession` | `POST /translation-sessions/{id}/end` | `famulor end-translation-session` | [End a translation room](https://docs.famulor.io/api-reference/translation/end) |
| `getTranslationSession` | `GET /translation-sessions/{id}` | `famulor get-translation-session` | [Get a translation room](https://docs.famulor.io/api-reference/translation/get) |
| `inviteTranslationGuest` | `POST /translation-sessions/{id}/invite` | `famulor invite-translation-guest` | [Invite the external guest](https://docs.famulor.io/api-reference/translation/invite) |
| `listTranslationSessions` | `GET /translation-sessions` | `famulor list-translation-sessions` | [List translation rooms](https://docs.famulor.io/api-reference/translation/list) |
| `startTranslationSession` | `POST /translation-sessions/{id}/start` | `famulor start-translation-session` | [Start a translation room](https://docs.famulor.io/api-reference/translation/start) |
