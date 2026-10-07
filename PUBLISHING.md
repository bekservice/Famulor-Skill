# Publishing and distribution

This repository is the Famulor agent plugin and skill package. The hosted MCP server itself is registered separately from `bekservice/Famulor-MCP`; do not add or publish a duplicate `server.json` from this repository.

## Release checklist

1. Update the version consistently in `plugin.json`, `.plugin/plugin.json`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json`, `claude-store/.claude-plugin/plugin.json`, and both skill metadata files.
2. Export the canonical Famulor MCP registry and refresh the 14 toolset references with `scripts/sync-catalog.py`; use `--check` to verify the total tool count and exact names.
3. Run:

   ```bash
   claude plugin validate . --strict
   claude plugin validate ./claude-store
   python3 /path/to/skill-creator/scripts/quick_validate.py skills/famulor-skill
   python3 /path/to/skill-creator/scripts/quick_validate.py claude-store/skills/famulor-assistants-history
   ```

   Claude Code 2.1.228 reports the directory-required `privacyPolicyUrl` in the
   isolated Store manifest as an unknown top-level field. The non-strict check
   confirms it still loads; verify the directory's policy scan separately.

4. Validate every JSON file and verify all relative component paths stay inside the plugin root.
5. Regenerate the standalone archive:

   ```bash
   cd skills
   zip -r -X ../famulor.skill famulor-skill
   ```

6. Inspect the archive with `unzip -l famulor.skill` and verify it contains no credentials, caches, or unrelated files.
7. Commit, open a pull request, and merge only after validation and review.
8. Tag the released commit after merge.

## Claude community plugin directory

The Claude Store package is intentionally isolated under `claude-store/` so the full root developer skill is not included in the store capability inventory. Its `.claude-plugin/plugin.json` loads only `claude-store/skills/famulor-assistants-history/`, while its `.mcp.json` connects to `https://app.famulor.io/mcp?profile=assistant-history`. The Gemini CLI gallery uses the repository root, discovers the full skill under `skills/`, and connects to the full MCP endpoint; keep its manifest and context consistent with that capability.

The profile exposes exactly 11 read-only tools: `list_assistants`, `get_assistant`, `list_assistant_versions`, `get_assistant_version`, `list_prompt_templates`, `get_languages`, `get_models`, `get_voices`, `list_history`, `get_call`, and `get_email_history_item`. It supports assistant review plus omnichannel call, email, Instagram, Messenger, and other connected messaging history when those records exist. Messaging history can be an overview or preview; do not advertise complete chat transcripts unless returned by the server. It has no mutation, outbound communication, campaign, telephony-purchase, billing, or administrative tools.

Submit the public repository with `claude-store` as the plugin path, or submit a zip whose root is the contents of `claude-store/`, through [Claude's directory management portal](https://claude.ai/directory/manage). Submit the remote MCP URL separately as a connector; a plugin's MCP configuration does not create a connector listing.

Anthropic runs the same `claude plugin validate` check plus safety screening. This plugin directory is separate from the Claude MCP Connector Directory.

Before submission, confirm `claude --plugin-dir ./claude-store plugin details famulor-assistants-history@inline` reports exactly one skill and one MCP server. Do not submit the repository root to the Store: root `.claude-plugin/plugin.json`, root `.mcp.json`, and `skills/famulor-skill/` intentionally remain the full developer plugin for backward compatibility.

## Cursor

Cursor discovers `.cursor-plugin/plugin.json`, `skills/`, and `mcp.json`. Test locally under `~/.cursor/plugins/local/famulor`, reload Cursor, and verify both the skill and OAuth MCP server appear.

Official marketplace submissions use `https://cursor.com/marketplace/publish`. Review the current publisher terms before submitting a plan-gated service. The public repository can also be shared through community directories that accept open-source agent plugins.

## Google Gemini CLI and Antigravity

Gemini CLI's gallery indexes public GitHub repositories with the `gemini-cli-extension` topic, a root `gemini-extension.json`, and a tag. No separate submission form is used. Check `https://geminicli.com/extensions/` after the daily crawl. This extension includes the full skill under `skills/`, so `GEMINI.md` and the MCP endpoint must match it; the Claude Store's restricted 11-tool profile is separate.

Antigravity uses `serverUrl` in its MCP configuration, while Gemini CLI uses `httpUrl`. The public README contains direct installation instructions for the portable skill and remote MCP server. Google's curated Antigravity marketplace documentation does not currently expose a third-party submission route; do not claim that the repository is listed there.

## Agent Plugins and universal skill installers

The root `plugin.json`, root `mcp.json`, and `skills/famulor-skill/` target Agent Plugins v1 and retain the complete 437-tool developer surface as of 2026-10-07. `npx skills add bekservice/Famulor-Skill` discovers the full skill from the public repository. `skills.sh` indexes compatible public repositories without a separate package upload.

## ClawHub

After authentication, publish the skill folder with the release version and a precise changelog:

```bash
clawhub skill publish ./skills/famulor-skill \
  --slug famulor-skill \
  --name "Famulor" \
  --version 2.1.5 \
  --changelog "Refresh the full MCP catalog to 437 tools, including assistant, knowledge, billing, and settings additions" \
  --tags latest
```

Run the current ClawHub verification or rescan command after publishing.
