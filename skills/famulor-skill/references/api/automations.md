# Automations API operations

Reviewed 2026-10-29. 43 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createAssistantAutomation` | `POST /assistants/{id}/automations` | `famulor create-assistant-automation` | [Create and connect an assistant automation](https://docs.famulor.io/api-reference/automations/create-and-connect-an-assistant-automation) |
| `createAutomation` | `POST /automations` | `famulor create-automation` | [Create automation](https://docs.famulor.io/api-reference/automations/create-automation) |
| `createAutomationConnection` | `POST /automations/connections` | `famulor create-automation-connection` | [Create automation connection](https://docs.famulor.io/api-reference/automations/create-automation-connection) |
| `createAutomationFolder` | `POST /automation-folders` | `famulor create-automation-folder` | [Create automation folder](https://docs.famulor.io/api-reference/introduction) |
| `createCrmSync` | `POST /crm-syncs` | `famulor create-crm-sync` | [Create CRM sync](https://docs.famulor.io/api-reference/automations/create-crm-sync) |
| `deleteAutomation` | `DELETE /automations/{id}` | `famulor delete-automation` | [Delete automation](https://docs.famulor.io/api-reference/automations/delete-automation) |
| `deleteAutomationConnection` | `DELETE /automations/connections/{id}` | `famulor delete-automation-connection` | [Delete automation connection](https://docs.famulor.io/api-reference/automations/delete-automation-connection) |
| `deleteAutomationFolder` | `DELETE /automation-folders/{id}` | `famulor delete-automation-folder` | [Delete automation folder](https://docs.famulor.io/api-reference/introduction) |
| `deleteCrmSync` | `DELETE /crm-syncs/{id}` | `famulor delete-crm-sync` | [Delete CRM sync](https://docs.famulor.io/api-reference/automations/delete-crm-sync) |
| `disconnectAssistantAutomation` | `DELETE /assistants/{id}/automations/{automationId}` | `famulor disconnect-assistant-automation` | [Disconnect an assistant automation](https://docs.famulor.io/api-reference/automations/disconnect-an-assistant-automation) |
| `discoverCrmSyncMetadata` | `POST /crm-syncs/discover` | `famulor discover-crm-sync-metadata` | [Discover CRM objects and fields](https://docs.famulor.io/api-reference/automations/discover-crm-objects-and-fields) |
| `duplicateAutomation` | `POST /automations/{id}/duplicate` | `famulor duplicate-automation` | [Duplicate automation](https://docs.famulor.io/api-reference/automations/duplicate-automation) |
| `exportAutomation` | `GET /automations/{id}/export` | `famulor export-automation` | [Export automation](https://docs.famulor.io/api-reference/introduction) |
| `getAutomation` | `GET /automations/{id}` | `famulor get-automation` | [Get automation](https://docs.famulor.io/api-reference/automations/get-automation) |
| `getAutomationConnection` | `GET /automations/connections/{id}` | `famulor get-automation-connection` | [Get automation connection](https://docs.famulor.io/api-reference/automations/get-automation-connection) |
| `getAutomationRun` | `GET /automations/{id}/runs/{runId}` | `famulor get-automation-run` | [Get automation run](https://docs.famulor.io/api-reference/automations/get-automation-run) |
| `getAutomationShare` | `GET /automations/{id}/share` | `famulor get-automation-share` | [Get automation share link](https://docs.famulor.io/api-reference/introduction) |
| `getAutomationTemplate` | `GET /automation-templates/{slug}` | `famulor get-automation-template` | [Get automation template](https://docs.famulor.io/api-reference/introduction) |
| `getAutomationTriggerTestData` | `POST /automations/trigger-test-data` | `famulor get-automation-trigger-test-data` | [Preview or capture conversation trigger data](https://docs.famulor.io/api-reference/introduction) |
| `getCrmSync` | `GET /crm-syncs/{id}` | `famulor get-crm-sync` | [Get CRM sync](https://docs.famulor.io/api-reference/automations/get-crm-sync) |
| `importAutomation` | `POST /automations/import` | `famulor import-automation` | [Import automation](https://docs.famulor.io/api-reference/introduction) |
| `importAutomationConnection` | `POST /automations/connections/import` | `famulor import-automation-connection` | [Import Agent Tool connection](https://docs.famulor.io/api-reference/automations/import-agent-tool-connection) |
| `importSharedAutomation` | `POST /automation-shares/{token}/import` | `famulor import-shared-automation` | [Import shared automation](https://docs.famulor.io/api-reference/introduction) |
| `listAssistantAutomations` | `GET /assistants/{id}/automations` | `famulor list-assistant-automations` | [List assistant-callable automations](https://docs.famulor.io/api-reference/automations/list-assistant-callable-automations) |
| `listAutomationAiActions` | `GET /automations/ai-actions` | `famulor list-automation-ai-actions` | [List Milian AI automation actions](https://docs.famulor.io/api-reference/automations/list-milian-ai-automation-actions) |
| `listAutomationConnections` | `GET /automations/connections` | `famulor list-automation-connections` | [List automation connections](https://docs.famulor.io/api-reference/automations/list-automation-connections) |
| `listAutomationFolders` | `GET /automation-folders` | `famulor list-automation-folders` | [List automation folders](https://docs.famulor.io/api-reference/introduction) |
| `listAutomationRuns` | `GET /automations/{id}/runs` | `famulor list-automation-runs` | [List automation runs](https://docs.famulor.io/api-reference/automations/list-automation-runs) |
| `listAutomationTemplates` | `GET /automation-templates` | `famulor list-automation-templates` | [List automation templates](https://docs.famulor.io/api-reference/introduction) |
| `listAutomations` | `GET /automations` | `famulor list-automations` | [List automations](https://docs.famulor.io/api-reference/automations/list-automations) |
| `listCrmSyncRuns` | `GET /crm-syncs/{id}/runs` | `famulor list-crm-sync-runs` | [List CRM sync runs](https://docs.famulor.io/api-reference/automations/list-crm-sync-runs) |
| `listCrmSyncs` | `GET /crm-syncs` | `famulor list-crm-syncs` | [List CRM syncs](https://docs.famulor.io/api-reference/automations/list-crm-syncs) |
| `revokeAutomationShare` | `DELETE /automations/{id}/share` | `famulor revoke-automation-share` | [Stop sharing automation](https://docs.famulor.io/api-reference/introduction) |
| `runAutomationAiAction` | `POST /automations/ai-actions` | `famulor run-automation-ai-action` | [Preview or run a Milian AI automation action](https://docs.famulor.io/api-reference/automations/preview-or-run-a-milian-ai-automation-action) |
| `runCrmSync` | `POST /crm-syncs/{id}/runs` | `famulor run-crm-sync` | [Run CRM sync](https://docs.famulor.io/api-reference/automations/run-crm-sync) |
| `shareAutomation` | `POST /automations/{id}/share` | `famulor share-automation` | [Share automation](https://docs.famulor.io/api-reference/introduction) |
| `tidyAutomationGraph` | `POST /automations/{id}/graph/layout` | `famulor tidy-automation-graph` | [Tidy up an automation graph](https://docs.famulor.io/api-reference/automations/tidy-up-an-automation-graph) |
| `triggerAutomation` | `POST /automations/{id}` | `famulor trigger-automation` | [Trigger automation](https://docs.famulor.io/api-reference/automations/trigger-automation) |
| `updateAutomation` | `PATCH /automations/{id}` | `famulor update-automation` | [Update automation](https://docs.famulor.io/api-reference/automations/update-automation) |
| `updateAutomationConnection` | `PATCH /automations/connections/{id}` | `famulor update-automation-connection` | [Update automation connection](https://docs.famulor.io/api-reference/automations/update-automation-connection) |
| `updateAutomationFolder` | `PATCH /automation-folders/{id}` | `famulor update-automation-folder` | [Rename automation folder](https://docs.famulor.io/api-reference/introduction) |
| `updateCrmSync` | `PATCH /crm-syncs/{id}` | `famulor update-crm-sync` | [Update CRM sync](https://docs.famulor.io/api-reference/automations/update-crm-sync) |
| `useAutomationTemplate` | `POST /automation-templates/{slug}/use` | `famulor use-automation-template` | [Use automation template](https://docs.famulor.io/api-reference/introduction) |
