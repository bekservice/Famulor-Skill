# Famulor.io Skill

Famulor.io skill for AI agents to build and manage assistants, campaigns, knowledge bases, and messaging workflows directly through the Famulor API.

## What This Skill Does

This skill connects an agent directly to the Famulor platform so it can execute tasks, not just explain them:

- Create and configure AI assistants (inbound, outbound, chat, WhatsApp)
- Set up outbound campaigns and manage leads
- Connect knowledge bases and documents
- Create mid-call tools (HTTP tools) for live integrations
- Run WhatsApp and SMS workflows
- Support testing and iterative prompt/voice optimization

## When To Use This Skill

Use this skill when users ask about topics like:

- "Famulor", "famulor.io", "assistant setup", "phone bot"
- Campaigns, leads, outbound calling
- WhatsApp bots, WhatsApp templates, SMS sending
- Knowledge bases, RAG documents, webhooks
- Famulor API integrations

## Requirements

- A valid API key as an environment variable:

```bash
export FAMULOR_API_KEY="your-api-key"
```

- Create your API key at [https://app.famulor.de](https://app.famulor.de) in the API Keys section.

## Skill Structure

- `SKILL.md` - Main instructions for the agent
- `references/api_reference.md` - Endpoint and field reference
- `scripts/famulor_client.py` - Python client with API methods
- `scripts/example.py` - Example usage
- `templates/example_template.txt` - Prompt/template example

## Example Workflows

1. **Build an assistant**  
   The agent gathers requirements, loads available voices/models/languages, and creates the assistant.

2. **Start a campaign**  
   The agent selects an outbound assistant, configures time windows and retry logic, adds leads, and starts the campaign.

3. **Enable a knowledge base**  
   The agent creates a knowledge base, imports documents, and links it to an assistant.

## Skill Description Quality Principles

This skill file follows common discoverability best practices:

- Clear trigger keywords from real user requests
- Explicit guidance on when to use the skill
- Concrete actions instead of generic claims
- Short, specific frontmatter description

## License

See `LICENSE`.
