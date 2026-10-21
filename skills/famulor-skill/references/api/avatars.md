# Avatars API operations

Reviewed 2026-10-21. 7 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createAvatarUpload` | `POST /avatars/uploads` | `famulor create-avatar-upload` | [Prepare custom avatar upload](https://docs.famulor.io/api-reference/avatars/prepare-custom-avatar-upload) |
| `deleteAvatar` | `DELETE /avatars/{id}` | `famulor delete-avatar` | [Delete custom avatar](https://docs.famulor.io/api-reference/avatars/delete-custom-avatar) |
| `getAvatar` | `GET /avatars/{id}` | `famulor get-avatar` | [Get custom avatar](https://docs.famulor.io/api-reference/avatars/get-custom-avatar) |
| `getAvatarCapability` | `GET /avatars/capability` | `famulor get-avatar-capability` | [Check custom avatar creation](https://docs.famulor.io/api-reference/avatars/check-custom-avatar-creation) |
| `listAvatarCatalog` | `GET /avatars/catalog` | `famulor list-avatar-catalog` | [Browse avatar library](https://docs.famulor.io/api-reference/avatars/browse-avatar-library) |
| `listAvatars` | `GET /avatars` | `famulor list-avatars` | [List private custom avatars](https://docs.famulor.io/api-reference/avatars/list-private-custom-avatars) |
| `submitAvatar` | `POST /avatars` | `famulor submit-avatar` | [Create private custom avatar](https://docs.famulor.io/api-reference/avatars/create-private-custom-avatar) |
