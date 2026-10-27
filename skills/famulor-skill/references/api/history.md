# History API operations

Reviewed 2026-10-27. 13 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createHistoryView` | `POST /history/views` | `famulor create-history-view` | [Create a saved History view](https://docs.famulor.io/api-reference/history/create-a-saved-history-view) |
| `deleteHistoryView` | `DELETE /history/views/{id}` | `famulor delete-history-view` | [Delete a saved History view](https://docs.famulor.io/api-reference/history/delete-a-saved-history-view) |
| `dismissInboxLabel` | `POST /history/inbox-labels/{id}/dismiss` | `famulor dismiss-inbox-label` | [Dismiss a message label](https://docs.famulor.io/api-reference/history/dismiss-a-message-label) |
| `getEmailHistoryItem` | `GET /history/emails/{id}` | `famulor get-email-history-item` | [Get an email conversation](https://docs.famulor.io/api-reference/history/get-an-email-conversation) |
| `getHistoryView` | `GET /history/views/{id}` | `famulor get-history-view` | [Get a saved History view](https://docs.famulor.io/api-reference/history/get-a-saved-history-view) |
| `getInboxLabelSettings` | `GET /inbox-labels/settings` | `famulor get-inbox-label-settings` | [Get message label settings](https://docs.famulor.io/api-reference/history/get-message-label-settings) |
| `getMessagingHistoryItem` | `GET /history/messaging/{id}` | `famulor get-messaging-history-item` | [Get a messaging conversation](https://docs.famulor.io/api-reference/history/get-a-messaging-conversation) |
| `listHistory` | `GET /history` | `famulor list-history` | [List conversation history](https://docs.famulor.io/api-reference/history/list-conversation-history) |
| `listHistoryViews` | `GET /history/views` | `famulor list-history-views` | [List saved History views](https://docs.famulor.io/api-reference/history/list-saved-history-views) |
| `replyToHistoryConversation` | `POST /history/reply` | `famulor reply-to-history-conversation` | [Reply to a conversation](https://docs.famulor.io/api-reference/introduction) |
| `runHistoryActions` | `POST /history/actions` | `famulor run-history-actions` | [Run history actions on any channel](https://docs.famulor.io/api-reference/history/run-history-actions-on-any-channel) |
| `updateHistoryView` | `PATCH /history/views/{id}` | `famulor update-history-view` | [Update a saved History view](https://docs.famulor.io/api-reference/history/update-a-saved-history-view) |
| `updateInboxLabelSettings` | `PATCH /inbox-labels/settings` | `famulor update-inbox-label-settings` | [Update message label settings](https://docs.famulor.io/api-reference/history/update-message-label-settings) |
