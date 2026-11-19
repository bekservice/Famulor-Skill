# Carrier Connections API operations

Reviewed 2026-11-19. 12 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createCarrierConnection` | `POST /carrier-connections` | `famulor create-carrier-connection` | [Create a carrier connection](https://docs.famulor.io/api-reference/carrier-connections/create-a-carrier-connection) |
| `deleteCarrierConnection` | `DELETE /carrier-connections/{id}` | `famulor delete-carrier-connection` | [Disconnect a carrier connection](https://docs.famulor.io/api-reference/carrier-connections/disconnect-a-carrier-connection) |
| `getCarrierConnection` | `GET /carrier-connections/{id}` | `famulor get-carrier-connection` | [Get a carrier connection](https://docs.famulor.io/api-reference/carrier-connections/get-a-carrier-connection) |
| `importCarrierNumbers` | `POST /carrier-connections/{id}/import` | `famulor import-carrier-numbers` | [Import carrier numbers](https://docs.famulor.io/api-reference/carrier-connections/import-carrier-numbers) |
| `listCarrierAvailableNumbers` | `GET /carrier-connections/{id}/available-numbers` | `famulor list-carrier-available-numbers` | [List carrier numbers available to import](https://docs.famulor.io/api-reference/carrier-connections/list-carrier-numbers-available-to-import) |
| `listCarrierConnections` | `GET /carrier-connections` | `famulor list-carrier-connections` | [List carrier connections](https://docs.famulor.io/api-reference/carrier-connections/list-carrier-connections) |
| `previewTwilioRegionSwitch` | `GET /carrier-connections/{id}/numbers/{numberId}/region-switch` | `famulor preview-twilio-region-switch` | [Preview a Twilio region switch](https://docs.famulor.io/api-reference/introduction) |
| `removeCarrierNumber` | `DELETE /carrier-connections/{id}/numbers/{numberId}` | `famulor remove-carrier-number` | [Remove an imported carrier number](https://docs.famulor.io/api-reference/carrier-connections/remove-an-imported-carrier-number) |
| `restoreTwilioRegion` | `DELETE /carrier-connections/{id}/numbers/{numberId}/region-switch` | `famulor restore-twilio-region` | [Restore the previous route of a Twilio number](https://docs.famulor.io/api-reference/introduction) |
| `switchTwilioRegion` | `POST /carrier-connections/{id}/numbers/{numberId}/region-switch` | `famulor switch-twilio-region` | [Switch the region of an imported Twilio number](https://docs.famulor.io/api-reference/introduction) |
| `troubleshootCarrierConnection` | `POST /carrier-connections/{id}/troubleshoot` | `famulor troubleshoot-carrier-connection` | [Troubleshoot a carrier connection](https://docs.famulor.io/api-reference/carrier-connections/troubleshoot-a-carrier-connection) |
| `updateCarrierConnection` | `PATCH /carrier-connections/{id}` | `famulor update-carrier-connection` | [Update a carrier connection](https://docs.famulor.io/api-reference/carrier-connections/update-a-carrier-connection) |
