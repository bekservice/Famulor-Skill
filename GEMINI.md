# Famulor plugin context

Use the bundled `skills/famulor-skill/SKILL.md` for Famulor tasks. Gemini CLI discovers that skill from this extension and connects to the full hosted MCP endpoint declared in `gemini-extension.json`.

The live MCP schemas, authenticated workspace, granted OAuth scopes, and selected toolsets determine which tools are available. Read the current state before any change. Follow the skill's consent, billing, and external-action safeguards; do not infer permission to send messages, place calls, spend credits, or change resources from a read-only request.
