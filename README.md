# Famulor Agent Plugin

A portable agent skill plus hosted Famulor MCP connections for Claude Code, Cursor, Codex, Gemini CLI, OpenCode, OpenClaw, and other Agent Skills-compatible clients.

The repository has two deliberate distributions. The portable Agent Plugin and developer skill cover the complete 282-tool customer-facing MCP surface. The Claude community-store plugin is restricted to an Assistant & History profile with exactly 11 read-only tools.

## What is included

- `skills/famulor-skill/SKILL.md`: short operating workflow, authorization rules, and toolset router
- `skills/famulor-skill/references/toolsets/`: all 282 current tools split across 13 progressively loaded references
- `skills/famulor-skill/references/assistant-design.md`: assistant onboarding and prompt-design guidance without fixed model or voice IDs
- `plugin.json` and `mcp.json`: portable Agent Plugins v1 package
- `claude-skills/famulor-assistants-history/SKILL.md`: Claude-specific read-only Assistant & History workflow
- `.claude-plugin/plugin.json` and `.mcp.json`: native Claude plugin metadata and restricted OAuth MCP connection
- `.cursor-plugin/plugin.json`: native Cursor plugin metadata
- `.plugin/plugin.json`: Open Plugins compatibility
- `famulor.skill`: standalone packaged Agent Skill archive

The portable Agent Plugin, Cursor, Codex, Gemini CLI, OpenCode, and OpenClaw use the full hosted endpoint:

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

Claude Code loads the restricted skill and `.mcp.json`. Open `/mcp` to complete OAuth when prompted. The Claude plugin connects only to:

```text
https://app.famulor.io/mcp?profile=assistant-history
```

It exposes exactly these 11 read-only tools: `list_assistants`, `get_assistant`, `list_assistant_versions`, `get_assistant_version`, `list_prompt_templates`, `get_languages`, `get_models`, `get_voices`, `list_history`, `get_call`, and `get_email_history_item`.

`list_history` provides an omnichannel overview across calls, email, and connected messaging channels such as Instagram or Messenger when present. Messaging results may be previews rather than complete transcripts. The Claude plugin cannot modify assistants, send messages, place calls, run campaigns, purchase numbers, manage billing, or perform any other write action.

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
python3 /path/to/skill-creator/scripts/quick_validate.py claude-skills/famulor-assistants-history
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
