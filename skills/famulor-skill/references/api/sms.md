# SMS API operations

Reviewed 2026-11-12. 10 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createSmsRcsSender` | `POST /sms/rcs/senders` | `famulor create-sms-rcs-sender` | [Draft a company sender for SMS and RCS](https://docs.famulor.io/api-reference/sms/draft-a-company-sender-for-sms-and-rcs) |
| `getSmsRcsSender` | `GET /sms/rcs/senders/{id}` | `famulor get-sms-rcs-sender` | [Get a company sender application](https://docs.famulor.io/api-reference/sms/get-a-company-sender-application) |
| `listSmsRcsSenders` | `GET /sms/rcs/senders` | `famulor list-sms-rcs-senders` | [List company senders for SMS and RCS](https://docs.famulor.io/api-reference/sms/list-company-senders-for-sms-and-rcs) |
| `refreshSmsRcsSender` | `POST /sms/rcs/senders/{id}/refresh` | `famulor refresh-sms-rcs-sender` | [Refresh company sender verification](https://docs.famulor.io/api-reference/sms/refresh-company-sender-verification) |
| `sendSms` | `POST /sms/send` | `famulor send-sms` | [Send an SMS channel message](https://docs.famulor.io/api-reference/sms/send-an-sms-channel-message) |
| `sendSmsFromConnector` | `POST /sms/connectors/{id}/send` | `famulor send-sms-from-connector` | [Send from an SMS connection](https://docs.famulor.io/api-reference/sms/send-from-an-sms-connection) |
| `setSmsRcsSenderTestNumbers` | `PUT /sms/rcs/senders/{id}/test-numbers` | `famulor set-sms-rcs-sender-test-numbers` | [Set company sender test numbers](https://docs.famulor.io/api-reference/sms/set-company-sender-test-numbers) |
| `submitSmsRcsSender` | `POST /sms/rcs/senders/{id}/submit` | `famulor submit-sms-rcs-sender` | [Book company sender setup](https://docs.famulor.io/api-reference/sms/book-company-sender-setup) |
| `updateSmsRcsSender` | `PATCH /sms/rcs/senders/{id}` | `famulor update-sms-rcs-sender` | [Update a company sender application](https://docs.famulor.io/api-reference/sms/update-a-company-sender-application) |
| `uploadSmsRcsAsset` | `POST /sms/rcs/assets` | `famulor upload-sms-rcs-asset` | [Upload a company sender logo or banner](https://docs.famulor.io/api-reference/sms/upload-a-company-sender-logo-or-banner) |
