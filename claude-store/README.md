# Famulor Assistants & History

Read Famulor assistant configuration and omnichannel conversation history from Claude or Grok Build. This standalone plugin connects to one hosted, OAuth-secured MCP endpoint:

```text
https://app.famulor.io/mcp?profile=assistant-history
```

The package contains one Agent Skill and one remote MCP server. It has no hooks, commands, agents, local executables, install scripts, or telemetry.

## Read-only capability

The server profile exposes exactly these 11 read-only tools:

- `list_assistants`
- `get_assistant`
- `list_assistant_versions`
- `get_assistant_version`
- `list_prompt_templates`
- `get_languages`
- `get_models`
- `get_voices`
- `list_history`
- `get_call`
- `get_email_history_item`

`list_history` can return calls, email, and connected messaging-channel history, including Instagram or Messenger when those records exist in the authenticated workspace. A messaging item may be a preview rather than a complete transcript.

The plugin cannot create or modify assistants, send messages, place calls, run campaigns, buy or configure phone numbers, access billing, or perform administrative actions.

## Authentication and data access

The client connects directly to `app.famulor.io` and completes Famulor OAuth on first use. No API key or other credential belongs in this package. The server enforces the authenticated workspace, OAuth scopes, membership role, plan, retention, and data-access policy.

History can contain personal data such as transcripts, recordings, messages, email threads, contacts, and customer context. Request and summarize only what the user needs.

## Package layout

```text
.claude-plugin/plugin.json
.mcp.json
skills/famulor-assistants-history/SKILL.md
LICENSE
README.md
```

The same directory is intentionally compatible with both marketplaces:

- Claude uses `.claude-plugin/plugin.json` and validates it with `claude plugin validate`.
- The xAI Plugin Marketplace accepts `.claude-plugin/plugin.json` for Claude-ecosystem plugins and indexes the `skills/` and `.mcp.json` components.

## Documentation and support

- [Famulor MCP documentation](https://docs.famulor.io/en/mcp/client)
- [Famulor support](https://www.famulor.io/support)
- [Privacy policy](https://www.famulor.io/privacy)
- [Terms](https://www.famulor.io/terms)

Licensed under the [MIT License](LICENSE).
