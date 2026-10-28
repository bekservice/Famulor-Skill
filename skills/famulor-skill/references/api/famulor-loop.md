# Famulor Loop API operations

Reviewed 2026-10-28. 38 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `actOnLoopRecall` | `POST /loop/recalls/{id}/actions` | `famulor act-on-loop-recall` | [Act on a personal Loop Recall item](https://docs.famulor.io/api-reference/famulor-loop/act-on-a-personal-loop-recall-item) |
| `createLoopQueue` | `POST /loop/queues` | `famulor create-loop-queue` | [Create a Loop call queue](https://docs.famulor.io/api-reference/famulor-loop/create-a-loop-call-queue) |
| `createLoopRingGroup` | `POST /loop/ring-groups` | `famulor create-loop-ring-group` | [Create a Loop ring group](https://docs.famulor.io/api-reference/famulor-loop/create-a-loop-ring-group) |
| `createLoopRoutingRule` | `POST /loop/routing-rules` | `famulor create-loop-routing-rule` | [Create a Loop routing rule](https://docs.famulor.io/api-reference/famulor-loop/create-a-loop-routing-rule) |
| `deleteLoopNumberRoute` | `DELETE /loop/number-routes/{id}` | `famulor delete-loop-number-route` | [Delete a Loop phone number route](https://docs.famulor.io/api-reference/famulor-loop/delete-a-loop-phone-number-route) |
| `deleteLoopQueue` | `DELETE /loop/queues/{id}` | `famulor delete-loop-queue` | [Delete a Loop call queue](https://docs.famulor.io/api-reference/famulor-loop/delete-a-loop-call-queue) |
| `deleteLoopRingGroup` | `DELETE /loop/ring-groups/{id}` | `famulor delete-loop-ring-group` | [Delete a Loop ring group](https://docs.famulor.io/api-reference/famulor-loop/delete-a-loop-ring-group) |
| `deleteLoopRoutingRule` | `DELETE /loop/routing-rules/{id}` | `famulor delete-loop-routing-rule` | [Delete a Loop routing rule](https://docs.famulor.io/api-reference/famulor-loop/delete-a-loop-routing-rule) |
| `getLoop` | `GET /loop` | `famulor get-loop` | [Get Famulor Loop access and settings](https://docs.famulor.io/api-reference/famulor-loop/get-famulor-loop-access-and-settings) |
| `getLoopAvailability` | `GET /loop/availability` | `famulor get-loop-availability` | [Get personal Loop availability](https://docs.famulor.io/api-reference/famulor-loop/get-personal-loop-availability) |
| `getLoopCall` | `GET /loop/calls/{id}` | `famulor get-loop-call` | [Get a Loop call](https://docs.famulor.io/api-reference/famulor-loop/get-a-loop-call) |
| `getLoopDialingPreferences` | `GET /loop/preferences` | `famulor get-loop-dialing-preferences` | [Get personal Loop dialing preferences](https://docs.famulor.io/api-reference/famulor-loop/get-personal-loop-dialing-preferences) |
| `getLoopNumberRoute` | `GET /loop/number-routes/{id}` | `famulor get-loop-number-route` | [Get a Loop phone number route](https://docs.famulor.io/api-reference/famulor-loop/get-a-loop-phone-number-route) |
| `getLoopPresence` | `GET /loop/presence` | `famulor get-loop-presence` | [Get personal Loop presence](https://docs.famulor.io/api-reference/famulor-loop/get-personal-loop-presence) |
| `getLoopQueue` | `GET /loop/queues/{id}` | `famulor get-loop-queue` | [Get a Loop call queue](https://docs.famulor.io/api-reference/famulor-loop/get-a-loop-call-queue) |
| `getLoopRecording` | `GET /loop/recording` | `famulor get-loop-recording` | [Get Loop call recording](https://docs.famulor.io/api-reference/famulor-loop/get-loop-call-recording) |
| `getLoopRingGroup` | `GET /loop/ring-groups/{id}` | `famulor get-loop-ring-group` | [Get a Loop ring group](https://docs.famulor.io/api-reference/famulor-loop/get-a-loop-ring-group) |
| `getLoopRoutingRule` | `GET /loop/routing-rules/{id}` | `famulor get-loop-routing-rule` | [Get a Loop routing rule](https://docs.famulor.io/api-reference/famulor-loop/get-a-loop-routing-rule) |
| `linkLoopCallContact` | `PATCH /loop/calls/{id}` | `famulor link-loop-call-contact` | [Link a Loop call to a contact](https://docs.famulor.io/api-reference/introduction) |
| `listLoopCalls` | `GET /loop/calls` | `famulor list-loop-calls` | [List Loop calls](https://docs.famulor.io/api-reference/famulor-loop/list-loop-calls) |
| `listLoopDevices` | `GET /loop/devices` | `famulor list-loop-devices` | [List personal Loop devices](https://docs.famulor.io/api-reference/famulor-loop/list-personal-loop-devices) |
| `listLoopDirectory` | `GET /loop/directory` | `famulor list-loop-directory` | [List the Loop directory](https://docs.famulor.io/api-reference/famulor-loop/list-the-loop-directory) |
| `listLoopNumberRoutes` | `GET /loop/number-routes` | `famulor list-loop-number-routes` | [List Loop phone number routes](https://docs.famulor.io/api-reference/famulor-loop/list-loop-phone-number-routes) |
| `listLoopQueues` | `GET /loop/queues` | `famulor list-loop-queues` | [List Loop call queues](https://docs.famulor.io/api-reference/famulor-loop/list-loop-call-queues) |
| `listLoopRecalls` | `GET /loop/recalls` | `famulor list-loop-recalls` | [List personal Loop Recall items](https://docs.famulor.io/api-reference/famulor-loop/list-personal-loop-recall-items) |
| `listLoopRingGroups` | `GET /loop/ring-groups` | `famulor list-loop-ring-groups` | [List Loop ring groups](https://docs.famulor.io/api-reference/famulor-loop/list-loop-ring-groups) |
| `listLoopRoutingRules` | `GET /loop/routing-rules` | `famulor list-loop-routing-rules` | [List Loop routing rules](https://docs.famulor.io/api-reference/famulor-loop/list-loop-routing-rules) |
| `renameLoopDevice` | `PATCH /loop/devices/{id}` | `famulor rename-loop-device` | [Rename a personal Loop device](https://docs.famulor.io/api-reference/famulor-loop/rename-a-personal-loop-device) |
| `revokeLoopDevice` | `DELETE /loop/devices/{id}` | `famulor revoke-loop-device` | [Revoke a personal Loop device](https://docs.famulor.io/api-reference/famulor-loop/revoke-a-personal-loop-device) |
| `setLoopNumberRoute` | `PUT /loop/number-routes/{id}` | `famulor set-loop-number-route` | [Set a Loop phone number route](https://docs.famulor.io/api-reference/famulor-loop/set-a-loop-phone-number-route) |
| `setLoopPresence` | `PATCH /loop/presence` | `famulor set-loop-presence` | [Set personal Loop presence](https://docs.famulor.io/api-reference/famulor-loop/set-personal-loop-presence) |
| `setLoopRecording` | `POST /loop/recording` | `famulor set-loop-recording` | [Start or stop Loop recording](https://docs.famulor.io/api-reference/famulor-loop/start-or-stop-loop-recording) |
| `updateLoopAvailability` | `PATCH /loop/availability` | `famulor update-loop-availability` | [Update personal Loop availability](https://docs.famulor.io/api-reference/famulor-loop/update-personal-loop-availability) |
| `updateLoopDialingPreferences` | `PATCH /loop/preferences` | `famulor update-loop-dialing-preferences` | [Update personal Loop dialing preferences](https://docs.famulor.io/api-reference/famulor-loop/update-personal-loop-dialing-preferences) |
| `updateLoopQueue` | `PATCH /loop/queues/{id}` | `famulor update-loop-queue` | [Update a Loop call queue](https://docs.famulor.io/api-reference/famulor-loop/update-a-loop-call-queue) |
| `updateLoopRingGroup` | `PATCH /loop/ring-groups/{id}` | `famulor update-loop-ring-group` | [Update a Loop ring group](https://docs.famulor.io/api-reference/famulor-loop/update-a-loop-ring-group) |
| `updateLoopRoutingRule` | `PATCH /loop/routing-rules/{id}` | `famulor update-loop-routing-rule` | [Update a Loop routing rule](https://docs.famulor.io/api-reference/famulor-loop/update-a-loop-routing-rule) |
| `updateLoopSettings` | `PATCH /loop` | `famulor update-loop-settings` | [Update Famulor Loop settings](https://docs.famulor.io/api-reference/famulor-loop/update-famulor-loop-settings) |
