# Voices API operations

Reviewed 2026-10-29. 9 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createVoiceCloneUpload` | `POST /voices/clone/uploads` | `famulor create-voice-clone-upload` | [Prepare voice clone uploads](https://docs.famulor.io/api-reference/introduction) |
| `deleteVoiceClone` | `DELETE /voices/clone/{cloneId}` | `famulor delete-voice-clone` | [Delete cloned voice](https://docs.famulor.io/api-reference/introduction) |
| `getVoiceClone` | `GET /voices/clone/{cloneId}` | `famulor get-voice-clone` | [Get cloned voice](https://docs.famulor.io/api-reference/introduction) |
| `getVoiceCloneCapability` | `GET /voices/clone/capability` | `famulor get-voice-clone-capability` | [Check voice cloning capability](https://docs.famulor.io/api-reference/introduction) |
| `getVoiceCloneJob` | `GET /voices/clone/jobs/{jobId}` | `famulor get-voice-clone-job` | [Get voice clone job](https://docs.famulor.io/api-reference/introduction) |
| `getVoicePreview` | `GET /voices/{id}/preview` | `famulor get-voice-preview` | [Play a stored voice preview](https://docs.famulor.io/api-reference/introduction) |
| `listVoiceClones` | `GET /voices/clone` | `famulor list-voice-clones` | [List cloned voices](https://docs.famulor.io/api-reference/introduction) |
| `listVoices` | `GET /voices` | `famulor list-voices` | [List voices](https://docs.famulor.io/api-reference/voices/list-voices) |
| `submitVoiceCloneJob` | `POST /voices/clone` | `famulor submit-voice-clone-job` | [Submit voice clone job](https://docs.famulor.io/api-reference/voices/submit-voice-clone-job) |
