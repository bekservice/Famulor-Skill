# Publishing and distribution

This repository is the Famulor agent plugin and skill package. The hosted MCP server itself is registered separately from `bekservice/Famulor-MCP`; do not add or publish a duplicate `server.json` from this repository.

## Release checklist

1. Update the version consistently in `plugin.json`, `.plugin/plugin.json`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json`, and the skill metadata.
2. Refresh the 13 toolset references from the canonical Famulor MCP registry and verify the total tool count.
3. Run:

   ```bash
   claude plugin validate . --strict
   python3 /path/to/skill-creator/scripts/quick_validate.py skills/famulor-skill
   ```

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

The repository includes `.claude-plugin/plugin.json`, `.mcp.json`, and `skills/` at the plugin root. Submit the public repository or a zip through:

- `https://platform.claude.com/plugins/submit` for individual authors
- `https://claude.ai/admin-settings/directory/submissions/plugins/new` for Team/Enterprise organization owners or directory managers

Anthropic runs the same `claude plugin validate` check plus safety screening. This plugin directory is separate from the Claude MCP Connector Directory.

## Cursor

Cursor discovers `.cursor-plugin/plugin.json`, `skills/`, and `mcp.json`. Test locally under `~/.cursor/plugins/local/famulor`, reload Cursor, and verify both the skill and OAuth MCP server appear.

Official marketplace submissions use `https://cursor.com/marketplace/publish`. Review the current publisher terms before submitting a plan-gated service. The public repository can also be shared through community directories that accept open-source agent plugins.

## Agent Plugins and universal skill installers

The root `plugin.json` and `mcp.json` target Agent Plugins v1. `npx skills add bekservice/Famulor-Skill` discovers the skill from the public repository. `skills.sh` indexes compatible public repositories without a separate package upload.

## ClawHub

After authentication, publish the skill folder with the release version and a precise changelog:

```bash
clawhub skill publish ./skills/famulor-skill \
  --slug famulor-skill \
  --name "Famulor" \
  --version 2.0.0 \
  --changelog "Full 282-tool MCP coverage, progressive references, and tenant-safe workflows" \
  --tags latest
```

Run the current ClawHub verification or rescan command after publishing.
