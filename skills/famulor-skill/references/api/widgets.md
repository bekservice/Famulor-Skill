# Widgets API operations

Reviewed 2026-10-27. 7 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createWidgetConnector` | `POST /widget-connectors` | `famulor create-widget-connector` | [Create web widget](https://docs.famulor.io/api-reference/widgets/create-web-widget) |
| `deleteWidgetConnector` | `DELETE /widget-connectors/{id}` | `famulor delete-widget-connector` | [Delete web widget](https://docs.famulor.io/api-reference/widgets/delete-web-widget) |
| `deleteWidgetConnectorLogo` | `DELETE /widget-connectors/{id}/logo` | `famulor delete-widget-connector-logo` | [Remove widget header logo](https://docs.famulor.io/api-reference/widgets/remove-widget-header-logo) |
| `getWidgetConnector` | `GET /widget-connectors/{id}` | `famulor get-widget-connector` | [Get web widget](https://docs.famulor.io/api-reference/widgets/get-web-widget) |
| `listWidgetConnectors` | `GET /widget-connectors` | `famulor list-widget-connectors` | [List web widgets](https://docs.famulor.io/api-reference/widgets/list-web-widgets) |
| `updateWidgetConnector` | `PATCH /widget-connectors/{id}` | `famulor update-widget-connector` | [Update web widget](https://docs.famulor.io/api-reference/widgets/update-web-widget) |
| `uploadWidgetConnectorLogo` | `POST /widget-connectors/{id}/logo` | `famulor upload-widget-connector-logo` | [Upload widget header logo](https://docs.famulor.io/api-reference/widgets/upload-widget-header-logo) |
