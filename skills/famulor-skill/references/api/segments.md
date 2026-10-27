# Segments API operations

Reviewed 2026-10-27. 6 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createSegment` | `POST /segments` | `famulor create-segment` | [Create a segment](https://docs.famulor.io/api-reference/segments/create-a-segment) |
| `deleteSegment` | `DELETE /segments/{id}` | `famulor delete-segment` | [Delete a segment](https://docs.famulor.io/api-reference/segments/delete-a-segment) |
| `getSegment` | `GET /segments/{id}` | `famulor get-segment` | [Get a segment](https://docs.famulor.io/api-reference/segments/get-a-segment) |
| `listSegmentLeads` | `GET /segments/{id}/leads` | `famulor list-segment-leads` | [List a segment's leads](https://docs.famulor.io/api-reference/segments/list-a-segments-leads) |
| `listSegments` | `GET /segments` | `famulor list-segments` | [List segments](https://docs.famulor.io/api-reference/segments/list-segments) |
| `updateSegment` | `PATCH /segments/{id}` | `famulor update-segment` | [Update a segment](https://docs.famulor.io/api-reference/segments/update-a-segment) |
