# Milian API operations

Reviewed 2026-10-28. 2 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `askMilian` | `POST /milian/ask` | `famulor ask-milian` | [Ask Milian](https://docs.famulor.io/api-reference/introduction) |
| `createMilianVoiceSession` | `POST /milian/voice-sessions` | `famulor create-milian-voice-session` | [Start a Milian voice session](https://docs.famulor.io/api-reference/introduction) |
