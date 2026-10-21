# Assistants API operations

Reviewed 2026-10-21. 21 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createAssistant` | `POST /assistants` | `famulor create-assistant` | [Create an assistant](https://docs.famulor.io/api-reference/assistants/create-an-assistant) |
| `deleteAssistant` | `DELETE /assistants/{id}` | `famulor delete-assistant` | [Delete an assistant](https://docs.famulor.io/api-reference/assistants/delete-an-assistant) |
| `deleteAssistantAvatar` | `DELETE /assistants/{id}/avatar` | `famulor delete-assistant-avatar` | [Remove assistant picture](https://docs.famulor.io/api-reference/assistants/remove-assistant-picture) |
| `deleteAssistantGreetingAudio` | `DELETE /assistants/{id}/greeting-audio` | `famulor delete-assistant-greeting-audio` | [Remove audio first message](https://docs.famulor.io/api-reference/assistants/remove-audio-first-message) |
| `getAssistant` | `GET /assistants/{id}` | `famulor get-assistant` | [Get an assistant](https://docs.famulor.io/api-reference/assistants/get-an-assistant) |
| `getAssistantAnnouncementAudio` | `GET /assistants/{id}/announcements/{assetId}/audio` | `famulor get-assistant-announcement-audio` | [Play saved announcement audio](https://docs.famulor.io/api-reference/assistants/play-saved-announcement-audio) |
| `getAssistantAnnouncements` | `GET /assistants/{id}/announcements` | `famulor get-assistant-announcements` | [Get saved announcement audio](https://docs.famulor.io/api-reference/assistants/get-saved-announcement-audio) |
| `getAssistantComplianceReview` | `GET /assistants/{id}/compliance-review` | `famulor get-assistant-compliance-review` | [Get assistant compliance review](https://docs.famulor.io/api-reference/assistants/get-assistant-compliance-review) |
| `getAssistantFallbackVoices` | `GET /assistants/{id}/fallback-voices` | `famulor get-assistant-fallback-voices` | [Get assistant backup voices](https://docs.famulor.io/api-reference/assistants/get-assistant-backup-voices) |
| `getAssistantVariables` | `GET /assistants/{id}/variables` | `famulor get-assistant-variables` | [Get assistant variables](https://docs.famulor.io/api-reference/assistants/get-assistant-variables) |
| `listAssistantAvatarGallery` | `GET /assistants/avatar-gallery` | `famulor list-assistant-avatar-gallery` | [List assistant picture gallery](https://docs.famulor.io/api-reference/introduction) |
| `listAssistants` | `GET /assistants` | `famulor list-assistants` | [List assistants](https://docs.famulor.io/api-reference/assistants/list-assistants) |
| `prepareAssistantAnnouncements` | `POST /assistants/{id}/announcements` | `famulor prepare-assistant-announcements` | [Prepare saved announcement audio](https://docs.famulor.io/api-reference/assistants/prepare-saved-announcement-audio) |
| `replaceAssistant` | `PUT /assistants/{id}` | `famulor replace-assistant` | [Update an assistant (PUT alias)](https://docs.famulor.io/api-reference/assistants/update-an-assistant-put-alias) |
| `requestAssistantComplianceReview` | `POST /assistants/{id}/compliance-review` | `famulor request-assistant-compliance-review` | [Request manual compliance review](https://docs.famulor.io/api-reference/assistants/request-manual-compliance-review) |
| `setAssistantAvatar` | `POST /assistants/{id}/avatar` | `famulor set-assistant-avatar` | [Set assistant picture](https://docs.famulor.io/api-reference/assistants/set-assistant-picture) |
| `setAssistantGreetingAudio` | `POST /assistants/{id}/greeting-audio` | `famulor set-assistant-greeting-audio` | [Set audio first message](https://docs.famulor.io/api-reference/assistants/set-audio-first-message) |
| `tidyAssistantFlow` | `POST /assistants/{id}/flow/layout` | `famulor tidy-assistant-flow` | [Tidy up an assistant flow](https://docs.famulor.io/api-reference/assistants/tidy-up-an-assistant-flow) |
| `updateAssistant` | `PATCH /assistants/{id}` | `famulor update-assistant` | [Update an assistant](https://docs.famulor.io/api-reference/assistants/update-an-assistant) |
| `updateAssistantFallbackVoices` | `PATCH /assistants/{id}/fallback-voices` | `famulor update-assistant-fallback-voices` | [Update assistant backup voices](https://docs.famulor.io/api-reference/assistants/update-assistant-backup-voices) |
| `updateAssistantVariables` | `PATCH /assistants/{id}/variables` | `famulor update-assistant-variables` | [Update assistant variables](https://docs.famulor.io/api-reference/assistants/update-assistant-variables) |
