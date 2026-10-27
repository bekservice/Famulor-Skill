# Tools API operations

Reviewed 2026-10-27. 18 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `archiveTool` | `DELETE /tools/{id}` | `famulor archive-tool` | [Archive an unused tool](https://docs.famulor.io/api-reference/tools/archive-an-unused-tool) |
| `connectMagicline` | `POST /tools/magicline` | `famulor connect-magicline` | [Connect Magicline Open API](https://docs.famulor.io/api-reference/tools/connect-magicline-open-api) |
| `connectMagiclineConnect` | `POST /tools/magicline-connect` | `famulor connect-magicline-connect` | [Connect Magicline Connect API](https://docs.famulor.io/api-reference/tools/connect-magicline-connect-api) |
| `createTool` | `POST /tools` | `famulor create-tool` | [Create a tool](https://docs.famulor.io/api-reference/tools/create-a-tool) |
| `discoverMagiclineConnectStudios` | `POST /tools/magicline-connect/studios` | `famulor discover-magicline-connect-studios` | [Find Magicline Connect API studios](https://docs.famulor.io/api-reference/tools/find-magicline-connect-api-studios) |
| `discoverTool` | `POST /tools/discover` | `famulor discover-tool` | [Discover MCP tool functions](https://docs.famulor.io/api-reference/tools/discover-mcp-tool-functions) |
| `getAssistantTools` | `GET /assistants/{id}/tools` | `famulor get-assistant-tools` | [List assigned tools](https://docs.famulor.io/api-reference/tools/list-assigned-tools) |
| `getTool` | `GET /tools/{id}` | `famulor get-tool` | [Get a tool](https://docs.famulor.io/api-reference/tools/get-a-tool) |
| `getToolUsage` | `GET /tools/{id}/usage` | `famulor get-tool-usage` | [Get tool usage and impact](https://docs.famulor.io/api-reference/tools/get-tool-usage-and-impact) |
| `listPerplexityModels` | `POST /tools/perplexity/models` | `famulor list-perplexity-models` | [List Perplexity models](https://docs.famulor.io/api-reference/tools/list-perplexity-models) |
| `listToolRuns` | `GET /tools/{id}/runs` | `famulor list-tool-runs` | [List reusable tool runs](https://docs.famulor.io/api-reference/tools/list-reusable-tool-runs) |
| `listToolVersions` | `GET /tools/{id}/versions` | `famulor list-tool-versions` | [List tool versions](https://docs.famulor.io/api-reference/tools/list-tool-versions) |
| `listTools` | `GET /tools` | `famulor list-tools` | [List reusable tools](https://docs.famulor.io/api-reference/tools/list-reusable-tools) |
| `reauthorizeTool` | `POST /tools/{id}/reauthorize` | `famulor reauthorize-tool` | [Reauthorize an OAuth MCP tool](https://docs.famulor.io/api-reference/tools/reauthorize-an-oauth-mcp-tool) |
| `restoreToolVersion` | `POST /tools/{id}/versions/{revision}/restore` | `famulor restore-tool-version` | [Restore a tool version](https://docs.famulor.io/api-reference/tools/restore-a-tool-version) |
| `setAssistantTools` | `PUT /assistants/{id}/tools` | `famulor set-assistant-tools` | [Replace assigned tools](https://docs.famulor.io/api-reference/tools/replace-assigned-tools) |
| `testTool` | `POST /tools/test` | `famulor test-tool` | [Test HTTP tool](https://docs.famulor.io/api-reference/tools/test-http-tool) |
| `updateTool` | `PATCH /tools/{id}` | `famulor update-tool` | [Update a tool](https://docs.famulor.io/api-reference/tools/update-a-tool) |
