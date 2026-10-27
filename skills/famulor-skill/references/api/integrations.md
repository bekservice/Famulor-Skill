# Integrations API operations

Reviewed 2026-10-27. 16 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createAcuityOauthUrl` | `POST /integrations/acuity/oauth-url` | `famulor create-acuity-oauth-url` | [Start Acuity OAuth](https://docs.famulor.io/api-reference/integrations/start-acuity-oauth) |
| `createCalendlyOauthUrl` | `POST /integrations/calendly/oauth-url` | `famulor create-calendly-oauth-url` | [Start Calendly OAuth](https://docs.famulor.io/api-reference/integrations/start-calendly-oauth) |
| `createIntegration` | `POST /integrations` | `famulor create-integration` | [Create a calendar integration](https://docs.famulor.io/api-reference/integrations/create-a-calendar-integration) |
| `deleteIntegration` | `DELETE /integrations/{id}` | `famulor delete-integration` | [Delete a calendar integration](https://docs.famulor.io/api-reference/integrations/delete-a-calendar-integration) |
| `executeMeetergoCalendarAction` | `POST /integrations/meetergo/action` | `famulor execute-meetergo-calendar-action` | [Check availability or book with meetergo](https://docs.famulor.io/api-reference/integrations/check-availability-or-book-with-meetergo) |
| `getAssistantIntegrations` | `GET /assistants/{id}/integrations` | `famulor get-assistant-integrations` | [List assistant integrations](https://docs.famulor.io/api-reference/integrations/list-assistant-integrations) |
| `getIntegration` | `GET /integrations/{id}` | `famulor get-integration` | [Get a calendar integration](https://docs.famulor.io/api-reference/integrations/get-a-calendar-integration) |
| `listAcuityAppointmentTypes` | `GET /integrations/acuity/appointment-types` | `famulor list-acuity-appointment-types` | [List Acuity appointment types](https://docs.famulor.io/api-reference/integrations/list-acuity-appointment-types) |
| `listAcuityCalendars` | `GET /integrations/acuity/calendars` | `famulor list-acuity-calendars` | [List Acuity calendars](https://docs.famulor.io/api-reference/integrations/list-acuity-calendars) |
| `listAcuityConnections` | `GET /integrations/acuity/connections` | `famulor list-acuity-connections` | [List connected Acuity accounts](https://docs.famulor.io/api-reference/integrations/list-connected-acuity-accounts) |
| `listCalendlyConnections` | `GET /integrations/calendly/connections` | `famulor list-calendly-connections` | [List connected Calendly accounts](https://docs.famulor.io/api-reference/integrations/list-connected-calendly-accounts) |
| `listCalendlyEventTypes` | `GET /integrations/calendly/event-types` | `famulor list-calendly-event-types` | [List active Calendly event types](https://docs.famulor.io/api-reference/integrations/list-active-calendly-event-types) |
| `listIntegrations` | `GET /integrations` | `famulor list-integrations` | [List calendar integrations](https://docs.famulor.io/api-reference/integrations/list-calendar-integrations) |
| `listMeetergoMeetingTypes` | `POST /integrations/meetergo/meeting-types` | `famulor list-meetergo-meeting-types` | [List meetergo meeting types](https://docs.famulor.io/api-reference/integrations/list-meetergo-meeting-types) |
| `setAssistantIntegrations` | `PUT /assistants/{id}/integrations` | `famulor set-assistant-integrations` | [Replace assistant integrations](https://docs.famulor.io/api-reference/integrations/replace-assistant-integrations) |
| `updateIntegration` | `PATCH /integrations/{id}` | `famulor update-integration` | [Update a calendar integration](https://docs.famulor.io/api-reference/integrations/update-a-calendar-integration) |
