# Famulor.io Skill

[Open Plugins](https://open-plugins.com)–compliant skill that lets AI coding agents build and manage assistants, campaigns, knowledge bases, and messaging workflows on the [Famulor](https://www.famulor.io) platform — through real API calls, not just explanations.

## What This Skill Does

Connects an agent directly to the Famulor platform so it can execute tasks:

- Create and configure AI phone assistants (inbound, outbound, chat, WhatsApp)
- Set up outbound campaigns and manage leads
- Connect knowledge bases and documents (RAG)
- Create mid-call tools (HTTP tools) for live integrations
- Run WhatsApp and SMS workflows
- Iterate prompts, voices, and webhooks based on test calls

## When To Use This Skill

The agent should activate this skill on prompts like:

- "Famulor", "famulor.io", "assistant setup", "phone bot", "voice agent"
- "Onboarding", "neuer Kunde", "Bot erstellen", "Telefonbot einrichten"
- Campaigns, leads, outbound calling
- WhatsApp bots, WhatsApp templates, SMS sending
- Knowledge bases, RAG documents, webhooks
- Famulor API integrations

## Requirements

- Python 3.10+
- A valid Famulor API key:

  ```bash
  export FAMULOR_API_KEY="your-api-key"
  ```

  Create your API key at [https://app.famulor.de](https://app.famulor.de) → API Keys.

## Repository Layout (Open Plugins spec)

```
.
├── .plugin/plugin.json              # Canonical Open Plugins manifest
├── .claude-plugin/plugin.json       # Claude Code manifest (mirror)
├── .cursor-plugin/plugin.json       # Cursor manifest (mirror)
├── .codex/INSTALL.md                # Codex install instructions
├── .opencode/INSTALL.md             # OpenCode install instructions
├── .openclaw/INSTALL.md             # OpenClaw install instructions
├── gemini-extension.json            # Gemini CLI manifest
├── GEMINI.md                        # Gemini context entry point
├── skills/
│   └── famulor-skill/
│       ├── SKILL.md                 # Main agent instructions
│       ├── references/
│       │   └── nischen_intelligenz.md   # Niche/branche knowledge
│       ├── scripts/
│       │   └── famulor_client.py    # Python API client
│       └── templates/
│           └── example_template.txt
├── famulor.skill                    # Packaged skill archive (zip)
├── README.md
└── LICENSE
```

The skill itself lives at `skills/famulor-skill/`, matching the Open Plugins component layout (`skills/{skill-name}/SKILL.md`).

## Installation

### Universal: skills CLI (recommended)

Works with Claude Code, Cursor, Codex, OpenClaw, Hermes Agent and 12+ other agents:

```bash
npx skills add bekservice/Famulor-Skill
```

Global install for a specific agent, non-interactive:

```bash
npx skills add bekservice/Famulor-Skill -g -y
```

### OpenClaw

Install from ClawHub:

```bash
openclaw skills install famulor-skill
```

Or from GitHub:

```bash
openclaw skills install git:bekservice/Famulor-Skill@main
```

Details: [.openclaw/INSTALL.md](.openclaw/INSTALL.md). Skill page on ClawHub: `https://clawhub.ai/skills/famulor-skill`.

### Hermes Agent

```bash
hermes skills install skills-sh/bekservice/Famulor-Skill/famulor-skill
```

Or via the universal skills CLI above (`npx skills add bekservice/Famulor-Skill`).

### Claude Code

Plugin auto-detection picks up `.claude-plugin/plugin.json` and the skill under `skills/famulor-skill/`. Drop the repo into your plugins directory (or install via your marketplace UI), then restart the session.

### Cursor

In Cursor Agent chat:

```text
/add-plugin https://github.com/bekservice/Famulor-Skill
```

If your workspace setup does not support direct URL plugin install, import `famulor.skill` manually and restart the chat session.

### Codex

Tell Codex:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/bekservice/Famulor-Skill/refs/heads/main/.codex/INSTALL.md
```

### OpenCode

Tell OpenCode:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/bekservice/Famulor-Skill/refs/heads/main/.opencode/INSTALL.md
```

### Gemini CLI

```bash
gemini extensions install https://github.com/bekservice/Famulor-Skill
```

Update:

```bash
gemini extensions update famulor-skill
```

### Universal Manual Installation (Fallback)

1. Download `famulor.skill` from this repository (it extracts to `famulor-skill/`).
2. Place the extracted folder in your agent's skills directory.
3. Restart the agent session.
4. Set `FAMULOR_API_KEY`.
5. Ask the agent to do a Famulor task.

## Local Developer Quickstart

```bash
git clone https://github.com/bekservice/Famulor-Skill.git
cd Famulor-Skill
export FAMULOR_API_KEY="your-api-key"
python3 skills/famulor-skill/scripts/famulor_client.py list_assistants
```

If your key is valid, you get a JSON response from the API.

## Verify Installation

- `echo $FAMULOR_API_KEY` returns a non-empty value
- `python3 skills/famulor-skill/scripts/famulor_client.py list_assistants` returns API data
- No `401 Unauthorized` error

## Example Workflows

1. **Build an assistant** — the agent gathers requirements, loads voices/models/languages, generates a system prompt, and creates the assistant.
2. **Start a campaign** — the agent selects an outbound assistant, configures time windows and retry logic, adds leads, and starts the campaign.
3. **Enable a knowledge base** — the agent creates a knowledge base, imports documents, and links it to an assistant.

## Standard Build Flow

1. Clarify the use case and desired assistant behavior.
2. Load available options (models, voices, languages, numbers).
3. Create or update the resource (assistant/campaign/knowledge base/tool).
4. Run a test conversation or dry-run.
5. Iterate prompt, voice, and webhook settings.

## Troubleshooting

| Issue | Likely Cause | Fix |
|---|---|---|
| `FAMULOR_API_KEY` missing | Env var not set in current shell | Run `export FAMULOR_API_KEY="..."` again |
| `401 Unauthorized` | Invalid or expired API key | Create a new key in Famulor dashboard and retry |
| Empty/failed API response | Temporary API or network issue | Retry; verify connectivity |
| Assistant creation fails | Incompatible mode/model combination | Re-check mode-specific model requirements in SKILL.md |
| `405 Method Not Allowed` on create | Wrong endpoint | Use `POST /user/assistant` (singular) |
| `field must not be greater than 16 characters` | Long post_call_schema field name | Use a short alias (e.g. `wunsch_mitarb`) |
| `initial_message may not be greater than 200 characters` | Greeting too long | Shorten the welcome message |
| WhatsApp send error | Sender/template/session mismatch | Fetch valid senders/templates and re-check session status |

## Security Notes

- Never commit API keys to Git.
- Prefer local environment variables or a `.env` file excluded via `.gitignore`.
- Rotate API keys immediately if exposed.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Update docs or implementation with clear examples.
4. Open a pull request with a short test/verification note.

## Updating

1. Pull the latest repository changes.
2. Re-import or refresh `famulor.skill` in your agent platform.
3. Start a new session so updated instructions load.

## Support

- Issues: open a GitHub issue in this repository.
- Platform: [https://www.famulor.io](https://www.famulor.io)

## License

See [LICENSE](LICENSE).
