# Account API operations

Reviewed 2026-10-29. 4 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `getAcademyProgress` | `GET /academy` | `famulor get-academy-progress` | [Get Academy progress](https://docs.famulor.io/api-reference/account/get-academy-progress) |
| `getCreditNotificationPreferences` | `GET /me/credit-notifications` | `famulor get-credit-notification-preferences` | [Get low-credit warning preferences](https://docs.famulor.io/api-reference/account/get-low-credit-warning-preferences) |
| `getMe` | `GET /me` | `famulor get-me` | [Get current credential](https://docs.famulor.io/api-reference/account/get-current-credential) |
| `updateCreditNotificationPreferences` | `PATCH /me/credit-notifications` | `famulor update-credit-notification-preferences` | [Update low-credit warning preferences](https://docs.famulor.io/api-reference/account/update-low-credit-warning-preferences) |
