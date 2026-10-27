# Install Famulor Skill

Choose your client below. There are two parts: **the skill teaches the workflow**; **the MCP connection provides authorized access to your workspace**. Installing either one does not automatically install the other in every client.

For workspace actions you need a Famulor account, a plan that includes Connect AI / MCP, and the relevant permissions. On a white-label workspace, use the domain shown in **Settings → API & MCP** instead of `app.famulor.io`.

## Quick start for coding agents

```bash
npx skills add bekservice/Famulor-Skill --skill famulor-skill
```

Choose your client in the installer. It installs into the current project by default; add `-g` for a global installation. Review the files before installing third-party skills. The installer has its own [Node.js requirements](https://github.com/vercel-labs/skills).

Add a remote **Streamable HTTP** MCP server with this URL and complete OAuth:

```text
https://app.famulor.io/mcp
```

Choose the correct workspace and approve only the groups needed. To keep discovery focused, use `https://app.famulor.io/mcp?toolsets=assistants,calls`. Filtering narrows access; it cannot add permissions to an existing token.

## Claude Code

Install the full plugin from this repository's marketplace:

```text
/plugin marketplace add bekservice/Famulor-Skill
/plugin install famulor@famulor
```

Select the desired installation scope, then open `/mcp` and authenticate Famulor. The plugin bundles the skill and remote server configuration. For local inspection:

```bash
git clone https://github.com/bekservice/Famulor-Skill.git
claude --plugin-dir ./Famulor-Skill
```

Alternatively install only the skill with the universal command and configure MCP separately:

```bash
claude mcp add --transport http famulor https://app.famulor.io/mcp
```

[Official plugin installation](https://code.claude.com/docs/en/discover-plugins) · [Official MCP setup](https://code.claude.com/docs/en/mcp)

## Claude web and desktop

1. Download **`famulor-skill.zip`** from the [latest release](https://github.com/bekservice/Famulor-Skill/releases/latest). Upload the skill ZIP, not the whole repository ZIP.
2. Open **Customize → Skills → + → Create skill → Upload a skill** and select it.
3. Enable the skill. Code execution and skill access must be permitted by your account or organization.
4. Add Famulor in **Customize → Connectors** and complete OAuth. For full workspace tools, add a custom connector using the MCP URL above.
5. Start a new conversation and ask Claude to use Famulor Skill.

The [Famulor Assistants & History connector](https://claude.ai/directory/famulor-assistants-history) is a convenient read-only option. It cannot save prompt changes, place calls or send messages. The separately packaged `claude-store/` plugin retains that restricted profile.

[Official skill upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Official remote connector guide](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

## ChatGPT

For assistant and history review, open the [official Famulor plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a8a46791ed08191a79aa4c98f34d772), install it, connect your Famulor account and choose **@Famulor** in a chat. This listing has **11 read-only tools**. It can inspect assistants and history, but it cannot apply changes or start outreach.

For a custom domain or additional authorized tools:

1. Open **ChatGPT Plugins** on the web.
2. Select **+ → Add custom MCP server**.
3. Enter a recognizable name and the Famulor MCP URL. Choose **OAuth**.
4. Review the connection information and create it as a plugin.
5. Sign in to Famulor, choose the workspace and approve the requested access.
6. Install the resulting plugin and select it with **@** in a chat.

Controls depend on your account and organization. Follow the [current OpenAI custom MCP guide](https://developers.openai.com/api/docs/guides/custom-mcp-server) if the interface differs. Local `npx skills` installation and Codex configuration do not configure ChatGPT web. Do not assume the marketplace listing contains this GitHub release or that installing a skill expands its access.

For prompt drafting without account access, provide the relevant template and business requirements in the chat; describe the result as a draft. [OpenAI plugin documentation](https://learn.chatgpt.com/docs/plugins) explains the available plugin surfaces.

## Codex

```bash
npx skills add bekservice/Famulor-Skill --skill famulor-skill
codex mcp add famulor --url https://app.famulor.io/mcp
codex mcp login famulor
codex mcp get famulor
```

Restart the session after installation. In the IDE, MCP can also be configured through **MCP servers → Add server → Streamable HTTP**, followed by authentication. Ask Codex to use `$famulor-skill` and list your assistants as a read-only check.

[Official MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

## Cursor

Install the skill with the universal installer and select Cursor. Add the remote server in Cursor's MCP settings, or put this in your project's `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "famulor": {
      "url": "https://app.famulor.io/mcp"
    }
  }
}
```

Cursor completes Famulor's OAuth sign-in natively; choose the workspace and tool groups on the consent screen, then verify the server's tools are enabled. An earlier setup that used an API key can switch to OAuth. This repository also includes native Cursor plugin metadata; the direct skill-plus-MCP setup does not depend on a marketplace listing.

[Official skills documentation](https://cursor.com/docs/skills) · [Official MCP documentation](https://cursor.com/docs/context/mcp) · [Plugin documentation](https://cursor.com/docs/plugins)

## Gemini CLI

```bash
gemini extensions install https://github.com/bekservice/Famulor-Skill
```

Review the requested extension capabilities. It bundles the skill, context and MCP configuration. In Gemini CLI, run `/mcp auth famulor` if authentication is requested, then use `/extensions list` to verify installation.

[Official extension installation](https://geminicli.com/docs/extensions/) · [Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)

## Other clients and manual installation

OpenCode, OpenClaw and other Agent Skills-compatible clients can use the universal installer. See the maintained client documentation for remote HTTP MCP and OAuth. If a client cannot authenticate the service, use another supported connection rather than embedding a secret in a shared configuration.

For manual installation, copy **the complete `skills/famulor-skill/` folder**, including references, scripts and assets, into your client's skill directory. Copying only `SKILL.md` loses the channel and endpoint guides. The release includes both a ZIP and the same archive as `famulor.skill` for compatible importers.

## Verify the connection

Start with:

> Use Famulor to list my assistants. Tell me which workspace is connected. Do not change anything.

Then try:

> Use Famulor Skill to review one assistant's prompt for website chat and propose improvements without saving them.

Confirm the client returned actual workspace data. A successful installation, OAuth consent screen or downloaded archive alone does not prove that a tool call succeeded. On the restricted profile, choose assistant/history tasks; toolset discovery and writes are intentionally unavailable.

## Update or remove

- Universal installer: `npx skills check` then `npx skills update`; remove with `npx skills remove famulor-skill`.
- Claude Code: update the Famulor marketplace and plugin from `/plugin`.
- Claude upload: replace your uploaded skill with the latest release ZIP.
- Gemini CLI: `gemini extensions update famulor`.
- MCP permissions: revoke unwanted connections in **Famulor → Settings → API & MCP**. Removing local instructions does not necessarily revoke an OAuth connection.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Skill installed, no Famulor tools | Add MCP separately and restart the client session |
| Only 11 read tools | You connected the public Assistant & History profile; use a separately authorized custom connection for broader tasks |
| Cannot edit an assistant | Check scope, workspace role and plan; reconnect with the required approved groups |
| Wrong workspace | Reconnect and choose the intended workspace; do not merge customer data |
| Too many tools | Use a focused `?toolsets=assistants,calls` URL |
| Expired login | Reauthenticate through the client's OAuth flow |
| Write timed out | Read current state before retrying; the first action may have completed |
| Skill ZIP rejected | Upload `famulor-skill.zip`, check organization skill settings and verify its checksum |

Client instructions were reviewed on 21 October 2026. Refer to the linked official documentation when controls change.
