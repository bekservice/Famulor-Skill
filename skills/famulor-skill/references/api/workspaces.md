# Workspaces API operations

Reviewed 2026-10-29. 8 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createWorkspace` | `POST /workspaces` | `famulor create-workspace` | [Create a workspace](https://docs.famulor.io/api-reference/workspaces/create-a-workspace) |
| `createWorkspaceApiKey` | `POST /workspaces/{workspace_id}/api-keys` | `famulor create-workspace-api-key` | [Create an API key for a workspace](https://docs.famulor.io/api-reference/workspaces/create-an-api-key-for-a-workspace) |
| `inviteTeamMember` | `POST /team-members` | `famulor invite-team-member` | [Invite team member](https://docs.famulor.io/api-reference/workspaces/invite-team-member) |
| `listTeamMembers` | `GET /team-members` | `famulor list-team-members` | [List team members](https://docs.famulor.io/api-reference/workspaces/list-team-members) |
| `listWorkspaces` | `GET /workspaces` | `famulor list-workspaces` | [List workspaces](https://docs.famulor.io/api-reference/workspaces/list-workspaces) |
| `removeTeamMember` | `DELETE /team-members/{id}` | `famulor remove-team-member` | [Remove team member](https://docs.famulor.io/api-reference/workspaces/remove-team-member) |
| `transferWorkspaceOwnership` | `POST /workspace/transfer-ownership` | `famulor transfer-workspace-ownership` | [Transfer workspace ownership](https://docs.famulor.io/api-reference/workspaces/transfer-workspace-ownership) |
| `updateTeamMemberRole` | `PATCH /team-members/{id}` | `famulor update-team-member-role` | [Change team member role](https://docs.famulor.io/api-reference/workspaces/change-team-member-role) |
