# Bookings API operations

Reviewed 2026-10-29. 13 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `cancelBooking` | `POST /bookings/{id}/cancel` | `famulor cancel-booking` | [Cancel a booking](https://docs.famulor.io/api-reference/bookings/cancel-a-booking) |
| `createBooking` | `POST /bookings` | `famulor create-booking` | [Create a booking](https://docs.famulor.io/api-reference/bookings/create-a-booking) |
| `createBookingEventType` | `POST /booking-event-types` | `famulor create-booking-event-type` | [Create a booking event type](https://docs.famulor.io/api-reference/bookings/create-a-booking-event-type) |
| `deleteBookingEventType` | `DELETE /booking-event-types/{id}` | `famulor delete-booking-event-type` | [Delete a booking event type](https://docs.famulor.io/api-reference/bookings/delete-a-booking-event-type) |
| `getBooking` | `GET /bookings/{id}` | `famulor get-booking` | [Get a booking](https://docs.famulor.io/api-reference/bookings/get-a-booking) |
| `getBookingEmailTemplates` | `GET /booking-email-templates` | `famulor get-booking-email-templates` | [Get standard booking email templates](https://docs.famulor.io/api-reference/bookings/get-standard-booking-email-templates) |
| `getBookingEventType` | `GET /booking-event-types/{id}` | `famulor get-booking-event-type` | [Get a booking event type](https://docs.famulor.io/api-reference/bookings/get-a-booking-event-type) |
| `listBookingEventTypes` | `GET /booking-event-types` | `famulor list-booking-event-types` | [List booking event types](https://docs.famulor.io/api-reference/bookings/list-booking-event-types) |
| `listBookingSlots` | `GET /booking-event-types/{id}/slots` | `famulor list-booking-slots` | [List free slots](https://docs.famulor.io/api-reference/bookings/list-free-slots) |
| `listBookings` | `GET /bookings` | `famulor list-bookings` | [List bookings](https://docs.famulor.io/api-reference/bookings/list-bookings) |
| `lookupBookings` | `POST /bookings/lookup` | `famulor lookup-bookings` | [Look up upcoming bookings](https://docs.famulor.io/api-reference/bookings/look-up-upcoming-bookings) |
| `rescheduleBooking` | `POST /bookings/{id}/reschedule` | `famulor reschedule-booking` | [Reschedule a booking](https://docs.famulor.io/api-reference/bookings/reschedule-a-booking) |
| `updateBookingEventType` | `PATCH /booking-event-types/{id}` | `famulor update-booking-event-type` | [Update a booking event type](https://docs.famulor.io/api-reference/bookings/update-a-booking-event-type) |
