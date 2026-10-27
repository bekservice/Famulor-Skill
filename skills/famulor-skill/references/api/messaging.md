# Messaging API operations

Reviewed 2026-10-27. 36 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `checkEmailAddressAvailability` | `GET /email/availability` | `famulor check-email-address-availability` | [Check hosted email name](https://docs.famulor.io/api-reference/messaging/check-hosted-email-name) |
| `completeMessengerFacebookLogin` | `POST /messenger/facebook-login` | Browser flow / raw API | [Complete Messenger Facebook Login](https://docs.famulor.io/api-reference/messaging/complete-messenger-facebook-login) |
| `completeWhatsAppEmbeddedSignup` | `POST /whatsapp/embedded-signup` | `famulor complete-whatsapp-embedded-signup` | [Complete WhatsApp Embedded Signup](https://docs.famulor.io/api-reference/messaging/complete-whatsapp-embedded-signup) |
| `createEmailAddress` | `POST /email/addresses` | `famulor create-email-address` | [Create an email address](https://docs.famulor.io/api-reference/messaging/create-an-email-address) |
| `createEmailDomain` | `POST /email/domains` | `famulor create-email-domain` | [Connect an email domain](https://docs.famulor.io/api-reference/messaging/connect-an-email-domain) |
| `createMessagingConnector` | `POST /messaging-connectors` | `famulor create-messaging-connector` | [Create messaging connector](https://docs.famulor.io/api-reference/messaging/create-messaging-connector) |
| `deleteEmailAddress` | `DELETE /email/addresses/{id}` | `famulor delete-email-address` | [Delete an email address](https://docs.famulor.io/api-reference/messaging/delete-an-email-address) |
| `deleteEmailDomain` | `DELETE /email/domains/{id}` | `famulor delete-email-domain` | [Disconnect an email domain](https://docs.famulor.io/api-reference/messaging/disconnect-an-email-domain) |
| `deleteMessagingConnector` | `DELETE /messaging-connectors/{id}` | `famulor delete-messaging-connector` | [Delete messaging connector](https://docs.famulor.io/api-reference/messaging/delete-messaging-connector) |
| `deleteWhatsAppConnectorAsset` | `DELETE /whatsapp/connectors/{id}/assets` | `famulor delete-whatsapp-connector-asset` | [Remove WhatsApp sender logo / banner](https://docs.famulor.io/api-reference/messaging/remove-whatsapp-sender-logo-banner) |
| `getEmailChannelOptions` | `GET /email/options` | `famulor get-email-channel-options` | [Get email channel options](https://docs.famulor.io/api-reference/messaging/get-email-channel-options) |
| `getEmailDomain` | `GET /email/domains/{id}` | `famulor get-email-domain` | [Get an email domain](https://docs.famulor.io/api-reference/messaging/get-an-email-domain) |
| `getEmailSettings` | `GET /email/settings` | `famulor get-email-settings` | [Get email channel defaults](https://docs.famulor.io/api-reference/messaging/get-email-channel-defaults) |
| `getMessengerFacebookLoginConfig` | `GET /messenger/facebook-login` | Browser flow / raw API | [Messenger Facebook Login public config](https://docs.famulor.io/api-reference/messaging/messenger-facebook-login-public-config) |
| `getSlackOauthConfig` | `GET /slack/oauth` | `famulor get-slack-oauth-config` | [Slack Add to Slack public config](https://docs.famulor.io/api-reference/messaging/slack-add-to-slack-public-config) |
| `getWhatsAppCallingReadiness` | `GET /whatsapp/calling` | `famulor get-whatsapp-calling-readiness` | [WhatsApp calling readiness](https://docs.famulor.io/api-reference/messaging/whatsapp-calling-readiness) |
| `getWhatsAppEmbeddedSignupConfig` | `GET /whatsapp/embedded-signup` | `famulor get-whatsapp-embedded-signup-config` | [WhatsApp Embedded Signup public config](https://docs.famulor.io/api-reference/messaging/whatsapp-embedded-signup-public-config) |
| `getWhatsAppSenderProfile` | `GET /whatsapp/connectors/{id}/profile` | `famulor get-whatsapp-sender-profile` | [Get WhatsApp sender profile](https://docs.famulor.io/api-reference/messaging/get-whatsapp-sender-profile) |
| `listEmailAddresses` | `GET /email/addresses` | `famulor list-email-addresses` | [List email addresses](https://docs.famulor.io/api-reference/messaging/list-email-addresses) |
| `listEmailDomains` | `GET /email/domains` | `famulor list-email-domains` | [List email domains](https://docs.famulor.io/api-reference/messaging/list-email-domains) |
| `listMessagingConnectorWatchOptions` | `GET /messaging-connectors/{id}/watch-options` | `famulor list-messaging-connector-watch-options` | [List mailbox watch options](https://docs.famulor.io/api-reference/messaging/list-mailbox-watch-options) |
| `listMessagingConnectors` | `GET /messaging-connectors` | `famulor list-messaging-connectors` | [List messaging connectors](https://docs.famulor.io/api-reference/messaging/list-messaging-connectors) |
| `listMessengerFacebookPages` | `POST /messenger/facebook-login/pages` | `famulor list-messenger-facebook-pages` | [List Facebook Pages for a user access token](https://docs.famulor.io/api-reference/messaging/list-facebook-pages-for-a-user-access-token) |
| `listWhatsAppTemplates` | `GET /whatsapp/templates` | `famulor list-whatsapp-templates` | [List WhatsApp message templates](https://docs.famulor.io/api-reference/messaging/list-whatsapp-message-templates) |
| `runWhatsAppCallingAction` | `POST /whatsapp/calling` | `famulor run-whatsapp-calling-action` | [Enable / resubscribe WhatsApp calling](https://docs.famulor.io/api-reference/messaging/enable-resubscribe-whatsapp-calling) |
| `startSlackOauth` | `POST /slack/oauth` | Browser flow / raw API | [Start Slack OAuth (Add to Slack)](https://docs.famulor.io/api-reference/messaging/start-slack-oauth-add-to-slack) |
| `testMessagingConnectorEndedWebhook` | `POST /messaging-connectors/{id}/ended-webhook-test` | `famulor test-messaging-connector-ended-webhook` | [Send a test conversation.ended webhook](https://docs.famulor.io/api-reference/messaging/send-a-test-conversationended-webhook) |
| `updateEmailAddress` | `PATCH /email/addresses/{id}` | `famulor update-email-address` | [Update an email address](https://docs.famulor.io/api-reference/messaging/update-an-email-address) |
| `updateEmailSettings` | `PUT /email/settings` | `famulor update-email-settings` | [Replace email channel defaults](https://docs.famulor.io/api-reference/messaging/replace-email-channel-defaults) |
| `updateMessagingConnector` | `PATCH /messaging-connectors/{id}` | `famulor update-messaging-connector` | [Update messaging connector](https://docs.famulor.io/api-reference/messaging/update-messaging-connector) |
| `updateWhatsAppSenderProfile` | `PATCH /whatsapp/connectors/{id}/profile` | `famulor update-whatsapp-sender-profile` | [Update WhatsApp sender profile](https://docs.famulor.io/api-reference/messaging/update-whatsapp-sender-profile) |
| `uploadWhatsAppConnectorAsset` | `POST /whatsapp/connectors/{id}/assets` | `famulor upload-whatsapp-connector-asset` | [Upload WhatsApp sender logo / banner](https://docs.famulor.io/api-reference/messaging/upload-whatsapp-sender-logo-banner) |
| `uploadWhatsAppTemplateReviewSample` | `POST /whatsapp/templates/media` | `famulor upload-whatsapp-template-review-sample` | [Upload a WhatsApp template review sample](https://docs.famulor.io/api-reference/introduction) |
| `verifyEmailDomain` | `POST /email/domains/{id}/verify` | `famulor verify-email-domain` | [Verify an email domain](https://docs.famulor.io/api-reference/messaging/verify-an-email-domain) |
| `whatsAppSenderProfileAction` | `POST /whatsapp/connectors/{id}/profile` | `famulor whatsapp-sender-profile-action` | [Run a WhatsApp sender profile action](https://docs.famulor.io/api-reference/messaging/run-a-whatsapp-sender-profile-action) |
| `whatsAppTemplatesAction` | `POST /whatsapp/templates` | `famulor whatsapp-templates-action` | [Create / update / submit / sync / send / delete WhatsApp templates](https://docs.famulor.io/api-reference/messaging/create-update-submit-sync-send-delete-whatsapp-templates) |
