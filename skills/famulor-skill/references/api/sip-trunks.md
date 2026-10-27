# SIP Trunks API operations

Reviewed 2026-10-27. 5 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createSipTrunk` | `POST /sip-trunks` | `famulor create-sip-trunk` | [Create a SIP trunk](https://docs.famulor.io/api-reference/sip-trunks/create-a-sip-trunk) |
| `deleteSipTrunk` | `DELETE /sip-trunks/{id}` | `famulor delete-sip-trunk` | [Delete a SIP trunk](https://docs.famulor.io/api-reference/sip-trunks/delete-a-sip-trunk) |
| `getSipTrunk` | `GET /sip-trunks/{id}` | `famulor get-sip-trunk` | [Get a SIP trunk](https://docs.famulor.io/api-reference/sip-trunks/get-a-sip-trunk) |
| `listSipTrunks` | `GET /sip-trunks` | `famulor list-sip-trunks` | [List SIP trunks](https://docs.famulor.io/api-reference/sip-trunks/list-sip-trunks) |
| `updateSipTrunkIdentity` | `PATCH /sip-trunks/{id}` | `famulor update-sip-trunk-identity` | [Update outbound SIP identity](https://docs.famulor.io/api-reference/sip-trunks/update-outbound-sip-identity) |
