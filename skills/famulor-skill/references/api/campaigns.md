# Campaigns API operations

Reviewed 2026-11-12. 19 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `cancelCampaignSchedule` | `POST /campaigns/{id}/cancel-schedule` | `famulor cancel-campaign-schedule` | [Cancel a campaign's schedule](https://docs.famulor.io/api-reference/campaigns/cancel-a-campaigns-schedule) |
| `createCampaign` | `POST /campaigns` | `famulor create-campaign` | [Create a campaign](https://docs.famulor.io/api-reference/campaigns/create-a-campaign) |
| `deleteCampaign` | `DELETE /campaigns/{id}` | `famulor delete-campaign` | [Delete a campaign](https://docs.famulor.io/api-reference/campaigns/delete-a-campaign) |
| `duplicateCampaign` | `POST /campaigns/{id}/duplicate` | `famulor duplicate-campaign` | [Duplicate a campaign](https://docs.famulor.io/api-reference/campaigns/duplicate-a-campaign) |
| `getCampaign` | `GET /campaigns/{id}` | `famulor get-campaign` | [Get a campaign](https://docs.famulor.io/api-reference/campaigns/get-a-campaign) |
| `getCampaignAnalytics` | `GET /campaigns/{id}/analytics` | `famulor get-campaign-analytics` | [Get campaign analytics](https://docs.famulor.io/api-reference/campaigns/get-campaign-analytics) |
| `getCampaignStats` | `GET /campaigns/{id}/stats` | `famulor get-campaign-stats` | [Get campaign stats](https://docs.famulor.io/api-reference/campaigns/get-campaign-stats) |
| `launchCampaign` | `POST /campaigns/{id}/launch` | `famulor launch-campaign` | [Launch a campaign](https://docs.famulor.io/api-reference/campaigns/launch-a-campaign) |
| `listCampaignAudienceConnections` | `GET /campaigns/external-audience/connections` | `famulor list-campaign-audience-connections` | [List campaign audience connections](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignAudienceProducts` | `GET /campaigns/external-audience/products` | `famulor list-campaign-audience-products` | [List campaign replenishment products](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignAudienceSegments` | `GET /campaigns/external-audience/segments` | `famulor list-campaign-audience-segments` | [List campaign audience segments](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignDeliveries` | `GET /campaigns/{id}/deliveries` | `famulor list-campaign-deliveries` | [List campaign deliveries](https://docs.famulor.io/api-reference/campaigns/list-campaign-deliveries) |
| `listCampaignTemplates` | `GET /campaign-templates` | `famulor list-campaign-templates` | [List campaign templates](https://docs.famulor.io/api-reference/campaigns/list-campaign-templates) |
| `listCampaigns` | `GET /campaigns` | `famulor list-campaigns` | [List campaigns](https://docs.famulor.io/api-reference/campaigns/list-campaigns) |
| `pauseCampaign` | `POST /campaigns/{id}/pause` | `famulor pause-campaign` | [Pause a campaign](https://docs.famulor.io/api-reference/campaigns/pause-a-campaign) |
| `resumeCampaign` | `POST /campaigns/{id}/resume` | `famulor resume-campaign` | [Resume a campaign](https://docs.famulor.io/api-reference/campaigns/resume-a-campaign) |
| `startCampaign` | `POST /campaigns/{id}/start` | `famulor start-campaign` | [Start a campaign](https://docs.famulor.io/api-reference/campaigns/start-a-campaign) |
| `stopCampaign` | `POST /campaigns/{id}/stop` | `famulor stop-campaign` | [Stop a campaign](https://docs.famulor.io/api-reference/campaigns/stop-a-campaign) |
| `updateCampaign` | `PATCH /campaigns/{id}` | `famulor update-campaign` | [Update a campaign](https://docs.famulor.io/api-reference/campaigns/update-a-campaign) |
