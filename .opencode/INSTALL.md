# Install Famulor for OpenCode

Install the skill with the universal Agent Skills installer:

```bash
npx skills add bekservice/Famulor-Skill
```

Configure `https://app.famulor.io/mcp` as a remote Streamable HTTP MCP server using OAuth in the current OpenCode MCP settings. Restart the session, then verify with a read-only request such as listing Famulor assistants.

The skill does not require a local Python wrapper or an undocumented REST endpoint.
