# Leads API operations

Reviewed 2026-10-29. 16 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `addLeads` | `POST /campaigns/{id}/leads` | `famulor add-leads` | [Add leads](https://docs.famulor.io/api-reference/leads/add-leads) |
| `assignLeadsToCampaign` | `POST /campaigns/{id}/leads/assign` | `famulor assign-leads-to-campaign` | [Assign leads to a campaign](https://docs.famulor.io/api-reference/leads/assign-leads-to-a-campaign) |
| `createAudienceContact` | `POST /leads` | `famulor create-audience-contact` | [Create an Audience contact](https://docs.famulor.io/api-reference/leads/create-an-audience-contact) |
| `deleteLead` | `DELETE /campaigns/{id}/leads/{leadId}` | `famulor delete-lead` | [Remove a lead from a campaign](https://docs.famulor.io/api-reference/leads/remove-a-lead-from-a-campaign) |
| `eraseCustomerMemory` | `DELETE /contacts/{id}/memory` | `famulor erase-customer-memory` | [Erase customer memory](https://docs.famulor.io/api-reference/leads/erase-customer-memory) |
| `getCustomerMemory` | `GET /contacts/{id}/memory` | `famulor get-customer-memory` | [Get customer memory](https://docs.famulor.io/api-reference/leads/get-customer-memory) |
| `getLead` | `GET /campaigns/{id}/leads/{leadId}` | `famulor get-lead` | [Get a campaign lead](https://docs.famulor.io/api-reference/leads/get-a-campaign-lead) |
| `listAudienceContactChannels` | `GET /leads/{id}/channels` | `famulor list-audience-contact-channels` | [List contact channels](https://docs.famulor.io/api-reference/leads/list-contact-channels) |
| `listAudienceContacts` | `GET /leads` | `famulor list-audience-contacts` | [List Audience contacts](https://docs.famulor.io/api-reference/leads/list-audience-contacts) |
| `listCustomerMemories` | `GET /contacts/memory` | `famulor list-customer-memories` | [List customer memories](https://docs.famulor.io/api-reference/leads/list-customer-memories) |
| `listLeads` | `GET /campaigns/{id}/leads` | `famulor list-leads` | [List leads](https://docs.famulor.io/api-reference/leads/list-leads) |
| `listVariableSources` | `GET /variables/catalog` | `famulor list-variable-sources` | [List campaign variable sources](https://docs.famulor.io/api-reference/leads/list-campaign-variable-sources) |
| `mergeAudienceContacts` | `POST /leads/{id}/merge` | `famulor merge-audience-contacts` | [Merge Audience contacts](https://docs.famulor.io/api-reference/leads/merge-audience-contacts) |
| `replaceAudienceContactChannels` | `PUT /leads/{id}/channels` | `famulor replace-audience-contact-channels` | [Replace contact channels](https://docs.famulor.io/api-reference/leads/replace-contact-channels) |
| `updateCustomerMemory` | `PATCH /contacts/{id}/memory` | `famulor update-customer-memory` | [Update customer memory](https://docs.famulor.io/api-reference/leads/update-customer-memory) |
| `updateLead` | `PATCH /campaigns/{id}/leads/{leadId}` | `famulor update-lead` | [Update a campaign lead](https://docs.famulor.io/api-reference/leads/update-a-campaign-lead) |
