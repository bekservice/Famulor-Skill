# Installing Famulor Skill for OpenClaw

Two ways to install — ClawHub (recommended) or directly from GitHub.

## Prerequisites

- Python 3.10+
- A Famulor API key (create one at https://app.famulor.de → API Keys)

## Option A: Install from ClawHub (recommended)

```bash
openclaw skills install famulor-skill
```

Install for all local agents instead of just the current workspace:

```bash
openclaw skills install famulor-skill --global
```

## Option B: Install from GitHub

```bash
openclaw skills install git:bekservice/Famulor-Skill@main
```

## Configure the API key

```bash
export FAMULOR_API_KEY="your-api-key"
```

Or add it to your OpenClaw environment so it is available in every session.

## Verify

```bash
openclaw skills verify famulor-skill
python3 skills/famulor-skill/scripts/famulor_client.py list_assistants
```

Then ask OpenClaw to perform a Famulor task (for example: "Create an outbound assistant in Famulor").

## Bonus: Famulor MCP server

For direct API tool access (66 tools), add the hosted MCP server as well:

```bash
openclaw mcp add famulor --url https://mcp.famulor.io/mcp --transport streamable-http --auth oauth
openclaw mcp login famulor
```

## Updating

```bash
openclaw skills update --all
```
