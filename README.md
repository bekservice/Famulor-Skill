# Famulor Agent Plugin

A portable agent skill plus the hosted Famulor MCP connection for Claude Code, Cursor, Codex, Gemini CLI, OpenCode, OpenClaw, and other Agent Skills-compatible clients.

The plugin operates real workspace resources through OAuth-secured MCP tools. It covers the complete customer-facing Famulor surface: assistants, omnichannel history, calls, campaigns, messaging, telephony, knowledge, dashboards, automations, billing, settings, authorized reseller administration, migrations, and durable tasks.

## What is included

- `skills/famulor-skill/SKILL.md`: short operating workflow, authorization rules, and toolset router
- `skills/famulor-skill/references/toolsets/`: all 282 current tools split across 13 progressively loaded references
- `skills/famulor-skill/references/assistant-design.md`: assistant onboarding and prompt-design guidance without fixed model or voice IDs
- `plugin.json` and `mcp.json`: portable Agent Plugins v1 package
- `.claude-plugin/plugin.json` and `.mcp.json`: native Claude Code plugin metadata and OAuth MCP connection
- `.cursor-plugin/plugin.json`: native Cursor plugin metadata
- `.plugin/plugin.json`: Open Plugins compatibility
- `famulor.skill`: standalone packaged Agent Skill archive

The default MCP connection is the full hosted endpoint:

```text
https://app.famulor.io/mcp
```

The server applies the authenticated workspace, approved scopes, role, plan, consent, and retention rules to every request. For smaller discovery results, append one or more toolsets, for example:

```text
https://app.famulor.io/mcp?toolsets=assistants,calls
```

## Install

### Universal Agent Skills installer

```bash
npx skills add bekservice/Famulor-Skill
```

This installs the skill instructions. If the client does not also discover the repository's MCP configuration, add `https://app.famulor.io/mcp` as a remote Streamable HTTP server and complete OAuth.

### Claude Code

Test directly from a clone:

```bash
git clone https://github.com/bekservice/Famulor-Skill.git
claude --plugin-dir ./Famulor-Skill
```

Claude Code loads the skill and `.mcp.json`. Open `/mcp` to complete OAuth when prompted. The repository is also prepared for Claude's community plugin directory.

### Cursor

Install the repository as a plugin:

```text
/add-plugin https://github.com/bekservice/Famulor-Skill
```

For local testing, symlink or copy the repository to `~/.cursor/plugins/local/famulor`, reload Cursor, and authenticate the `famulor` MCP server. Cursor discovers `skills/` and `mcp.json` from the plugin root.

### Codex

See [.codex/INSTALL.md](.codex/INSTALL.md), or use:

```bash
npx skills add bekservice/Famulor-Skill
codex mcp add famulor --url https://app.famulor.io/mcp
codex mcp login famulor
```

### Gemini CLI, OpenCode, and OpenClaw

Use the universal installer above. Client-specific notes are in `GEMINI.md`, `.opencode/INSTALL.md`, and `.openclaw/INSTALL.md`.

## How the skill behaves

- Uses live MCP schemas instead of stale REST examples or fixed IDs
- Loads only the reference for the relevant toolset
- Reads current state before mutation and verifies results afterward
- Keeps read-only requests read-only
- Requires explicit targets for calls, messages, campaign starts, payments, number changes, credit transfers, migrations, and destructive actions
- Preserves workspace isolation, consent, suppression, roles, scopes, plan gates, and personal-data boundaries

The 282-tool catalog is a dated navigation snapshot. The live MCP `tools/list` response remains authoritative for arguments, availability, annotations, and gating.

## Validate locally

```bash
claude plugin validate . --strict
python3 /path/to/skill-creator/scripts/quick_validate.py skills/famulor-skill
```

Also validate every JSON file, confirm the packaged archive matches `skills/famulor-skill/`, and check that the live endpoint returns OAuth metadata rather than a server error.

## Security

- Do not commit API keys or OAuth tokens.
- Prefer OAuth for interactive clients.
- Treat transcript, recording, message, email, contact, and customer-memory data as personal data.
- Review tool annotations and returned impact before external or destructive actions.

## Documentation and support

- [Famulor MCP documentation](https://docs.famulor.io/en/mcp/client)
- [Famulor API documentation](https://docs.famulor.io/en/api-reference/introduction)
- [Famulor support](https://www.famulor.io/support)
- [Privacy policy](https://www.famulor.io/privacy)
- [Terms](https://www.famulor.io/terms)

Licensed under the [MIT License](LICENSE).
