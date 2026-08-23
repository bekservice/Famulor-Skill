# Install Famulor for Codex

Install the skill:

```bash
npx skills add bekservice/Famulor-Skill
```

Add the hosted MCP server and complete OAuth:

```bash
codex mcp add famulor --url https://app.famulor.io/mcp
codex mcp login famulor
codex mcp get famulor
```

Restart the Codex session so skill discovery and the MCP connection are both available. Ask Codex to list Famulor assistants as a read-only verification.

For a smaller catalog, remove the server and re-add a scoped URL such as:

```bash
codex mcp remove famulor
codex mcp add famulor --url 'https://app.famulor.io/mcp?toolsets=assistants,calls'
codex mcp login famulor
```

Never put a Famulor API key directly in the command. Server-to-server users can set a secret environment variable and use Codex's bearer-token environment option instead.
