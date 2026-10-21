# Settings API operations

Reviewed 2026-10-21. 29 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `addCustomDomain` | `POST /custom-domain` | `famulor add-custom-domain` | [Add custom domain](https://docs.famulor.io/api-reference/settings/add-custom-domain) |
| `createSupportRequest` | `POST /support/requests` | `famulor create-support-request` | [Create a support request](https://docs.famulor.io/api-reference/settings/create-a-support-request) |
| `deletePasskey` | `DELETE /settings/passkeys` | `famulor delete-passkey` | [Delete a passkey](https://docs.famulor.io/api-reference/settings/delete-a-passkey) |
| `getAiInferenceSettings` | `GET /settings/ai-inference` | `famulor get-ai-inference-settings` | [Get AI inference settings](https://docs.famulor.io/api-reference/settings/get-ai-inference-settings) |
| `getConsentComplianceSettings` | `GET /settings/consent-compliance` | `famulor get-consent-compliance-settings` | [Get consent compliance mode](https://docs.famulor.io/api-reference/settings/get-consent-compliance-mode) |
| `getCustomDomainStatus` | `GET /custom-domain` | `famulor get-custom-domain-status` | [Get custom domain status](https://docs.famulor.io/api-reference/settings/get-custom-domain-status) |
| `getDarkWindowSettings` | `GET /settings/dark-windows` | `famulor get-dark-window-settings` | [Get Dark Windows settings](https://docs.famulor.io/api-reference/settings/get-dark-windows-settings) |
| `getMarketingIntegrations` | `GET /settings/marketing` | `famulor get-marketing-integrations` | [Get marketing integrations](https://docs.famulor.io/api-reference/settings/get-marketing-integrations) |
| `getMemorySettings` | `GET /settings/memory` | `famulor get-memory-settings` | [Get memory settings](https://docs.famulor.io/api-reference/settings/get-memory-settings) |
| `getOutboundLimits` | `GET /settings/outbound-limits` | `famulor get-outbound-limits` | [Get outbound call limits](https://docs.famulor.io/api-reference/settings/get-outbound-call-limits) |
| `getRetentionSettings` | `GET /settings/retention` | `famulor get-retention-settings` | [Get data retention settings](https://docs.famulor.io/api-reference/settings/get-data-retention-settings) |
| `getSupportRequest` | `GET /support/requests/{reference}` | `famulor get-support-request` | [Get a support request](https://docs.famulor.io/api-reference/settings/get-a-support-request) |
| `getWorkspaceCountry` | `GET /settings/workspace-country` | `famulor get-workspace-country` | [Get workspace country](https://docs.famulor.io/api-reference/introduction) |
| `listAccountSessions` | `GET /settings/sessions` | `famulor list-account-sessions` | [List active account sessions](https://docs.famulor.io/api-reference/settings/list-active-account-sessions) |
| `listEmailSenders` | `GET /email-senders` | `famulor list-email-senders` | [List email sender choices](https://docs.famulor.io/api-reference/settings/list-email-sender-choices) |
| `listPasskeys` | `GET /settings/passkeys` | `famulor list-passkeys` | [List passkeys](https://docs.famulor.io/api-reference/settings/list-passkeys) |
| `listSupportRequests` | `GET /support/requests` | `famulor list-support-requests` | [List support requests](https://docs.famulor.io/api-reference/settings/list-support-requests) |
| `removeCustomDomain` | `DELETE /custom-domain` | `famulor remove-custom-domain` | [Remove custom domain](https://docs.famulor.io/api-reference/settings/remove-custom-domain) |
| `replyToSupportRequest` | `POST /support/requests/{reference}/messages` | `famulor reply-to-support-request` | [Reply to a support request](https://docs.famulor.io/api-reference/settings/reply-to-a-support-request) |
| `requestOutboundLimitIncrease` | `POST /settings/outbound-limits/requests` | `famulor request-outbound-limit-increase` | [Request an outbound call limit increase](https://docs.famulor.io/api-reference/settings/request-an-outbound-call-limit-increase) |
| `signOutAccountSession` | `DELETE /settings/sessions` | `famulor sign-out-account-session` | [Sign out an account session](https://docs.famulor.io/api-reference/settings/sign-out-an-account-session) |
| `updateAiInferenceSettings` | `PATCH /settings/ai-inference` | `famulor update-ai-inference-settings` | [Update AI inference settings](https://docs.famulor.io/api-reference/settings/update-ai-inference-settings) |
| `updateConsentComplianceSettings` | `PATCH /settings/consent-compliance` | `famulor update-consent-compliance-settings` | [Update consent compliance mode](https://docs.famulor.io/api-reference/settings/update-consent-compliance-mode) |
| `updateDarkWindowSettings` | `PATCH /settings/dark-windows` | `famulor update-dark-window-settings` | [Update Dark Windows settings](https://docs.famulor.io/api-reference/settings/update-dark-windows-settings) |
| `updateMarketingIntegrations` | `PUT /settings/marketing` | `famulor update-marketing-integrations` | [Update marketing integrations](https://docs.famulor.io/api-reference/settings/update-marketing-integrations) |
| `updateMemorySettings` | `PATCH /settings/memory` | `famulor update-memory-settings` | [Update memory settings](https://docs.famulor.io/api-reference/settings/update-memory-settings) |
| `updateRetentionSettings` | `PATCH /settings/retention` | `famulor update-retention-settings` | [Update data retention settings](https://docs.famulor.io/api-reference/settings/update-data-retention-settings) |
| `updateWorkspaceCountry` | `PATCH /settings/workspace-country` | `famulor update-workspace-country` | [Update workspace country](https://docs.famulor.io/api-reference/introduction) |
| `verifyCustomDomain` | `POST /custom-domain/verify` | `famulor verify-custom-domain` | [Check custom domain DNS](https://docs.famulor.io/api-reference/settings/check-custom-domain-dns) |
