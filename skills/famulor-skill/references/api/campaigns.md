# Campaigns API operations

Reviewed 2026-10-27. 12 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createCampaign` | `POST /campaigns` | `famulor create-campaign` | [Create a campaign](https://docs.famulor.io/api-reference/campaigns/create-a-campaign) |
| `deleteCampaign` | `DELETE /campaigns/{id}` | `famulor delete-campaign` | [Delete a campaign](https://docs.famulor.io/api-reference/campaigns/delete-a-campaign) |
| `getCampaign` | `GET /campaigns/{id}` | `famulor get-campaign` | [Get a campaign](https://docs.famulor.io/api-reference/campaigns/get-a-campaign) |
| `getCampaignStats` | `GET /campaigns/{id}/stats` | `famulor get-campaign-stats` | [Get campaign stats](https://docs.famulor.io/api-reference/campaigns/get-campaign-stats) |
| `listCampaignAudienceConnections` | `GET /campaigns/external-audience/connections` | `famulor list-campaign-audience-connections` | [List campaign audience connections](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignAudienceProducts` | `GET /campaigns/external-audience/products` | `famulor list-campaign-audience-products` | [List campaign replenishment products](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignAudienceSegments` | `GET /campaigns/external-audience/segments` | `famulor list-campaign-audience-segments` | [List campaign audience segments](https://docs.famulor.io/api-reference/introduction) |
| `listCampaignDeliveries` | `GET /campaigns/{id}/deliveries` | `famulor list-campaign-deliveries` | [List campaign deliveries](https://docs.famulor.io/api-reference/campaigns/list-campaign-deliveries) |
| `listCampaigns` | `GET /campaigns` | `famulor list-campaigns` | [List campaigns](https://docs.famulor.io/api-reference/campaigns/list-campaigns) |
| `startCampaign` | `POST /campaigns/{id}/start` | `famulor start-campaign` | [Start a campaign](https://docs.famulor.io/api-reference/campaigns/start-a-campaign) |
| `stopCampaign` | `POST /campaigns/{id}/stop` | `famulor stop-campaign` | [Stop a campaign](https://docs.famulor.io/api-reference/campaigns/stop-a-campaign) |
| `updateCampaign` | `PATCH /campaigns/{id}` | `famulor update-campaign` | [Update a campaign](https://docs.famulor.io/api-reference/campaigns/update-a-campaign) |
