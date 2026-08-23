# Install Famulor for OpenClaw

Install from ClawHub when the current release is available:

```bash
openclaw skills install famulor-skill
```

Or install the public repository with the universal Agent Skills installer:

```bash
npx skills add bekservice/Famulor-Skill
```

Add the hosted MCP server using OpenClaw's current remote Streamable HTTP and OAuth flow:

```text
https://app.famulor.io/mcp
```

If the installed OpenClaw version supports these commands, verify the skill and MCP connection with its `skills verify` and `mcp` status commands. Do not place API keys in the repository or command history.
