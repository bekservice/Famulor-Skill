# Dashboards API operations

Reviewed 2026-10-21. 12 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createDashboard` | `POST /dashboards` | `famulor create-dashboard` | [Create a custom dashboard](https://docs.famulor.io/api-reference/dashboards/create-a-custom-dashboard) |
| `createDashboardWidget` | `POST /dashboards/{id}/widgets` | `famulor create-dashboard-widget` | [Create or attach a dashboard widget](https://docs.famulor.io/api-reference/dashboards/create-or-attach-a-dashboard-widget) |
| `deleteDashboard` | `DELETE /dashboards/{id}` | `famulor delete-dashboard` | [Delete a custom dashboard](https://docs.famulor.io/api-reference/dashboards/delete-a-custom-dashboard) |
| `getDashboard` | `GET /dashboards/{id}` | `famulor get-dashboard` | [Get a custom dashboard](https://docs.famulor.io/api-reference/dashboards/get-a-custom-dashboard) |
| `getDashboardAnalytics` | `GET /dashboards/{id}/analytics` | `famulor get-dashboard-analytics` | [Get dashboard analytics](https://docs.famulor.io/api-reference/dashboards/get-dashboard-analytics) |
| `listDashboardWidgets` | `GET /dashboards/{id}/widgets` | `famulor list-dashboard-widgets` | [List dashboard widgets](https://docs.famulor.io/api-reference/dashboards/list-dashboard-widgets) |
| `listDashboards` | `GET /dashboards` | `famulor list-dashboards` | [List custom dashboards](https://docs.famulor.io/api-reference/dashboards/list-custom-dashboards) |
| `previewNaturalLanguageDashboard` | `POST /dashboards/{id}/natural-language` | `famulor preview-natural-language-dashboard` | [Preview a natural-language dashboard plan](https://docs.famulor.io/api-reference/dashboards/preview-a-natural-language-dashboard-plan) |
| `removeDashboardWidget` | `DELETE /dashboards/{id}/widgets/{widgetId}` | `famulor remove-dashboard-widget` | [Detach a dashboard widget](https://docs.famulor.io/api-reference/dashboards/detach-a-dashboard-widget) |
| `saveNaturalLanguageDashboard` | `PUT /dashboards/{id}/natural-language` | `famulor save-natural-language-dashboard` | [Save a natural-language dashboard plan](https://docs.famulor.io/api-reference/dashboards/save-a-natural-language-dashboard-plan) |
| `updateDashboard` | `PATCH /dashboards/{id}` | `famulor update-dashboard` | [Update a custom dashboard](https://docs.famulor.io/api-reference/dashboards/update-a-custom-dashboard) |
| `updateDashboardWidget` | `PATCH /dashboards/{id}/widgets/{widgetId}` | `famulor update-dashboard-widget` | [Update a dashboard widget](https://docs.famulor.io/api-reference/dashboards/update-a-dashboard-widget) |
