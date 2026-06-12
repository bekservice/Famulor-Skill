# Publishing & Distribution

How to publish the Famulor skill to the registries so users can install it everywhere.

## 1. ClawHub (OpenClaw)

One-time setup:

```bash
npm i -g clawhub
clawhub login          # browser GitHub auth (account must be ≥ 1 week old)
clawhub whoami         # verify
```

Publish (from the repo root):

```bash
clawhub skill publish ./skills/famulor-skill \
  --slug famulor-skill \
  --name "Famulor Skill" \
  --version 1.2.0 \
  --changelog "OpenClaw support, MCP setup instructions, npx install" \
  --tags latest
```

Publish updates later:

```bash
clawhub sync --all
```

After publishing, users install with:

```bash
openclaw skills install famulor-skill
```

Skill page: `https://clawhub.ai/skills/famulor-skill` — your hub page: `https://clawhub.ai/user/<your-github-username>`.

If the automated scan flags a false positive: `clawhub skill rescan famulor-skill`.

## 2. skills.sh (npx skills add)

No submission needed. Any public GitHub repo with valid `SKILL.md` files is picked up automatically once people install via the CLI:

```bash
npx skills add bekservice/Famulor-Skill
```

Repo page: `https://skills.sh/bekservice/Famulor-Skill`
Badge for the README: `https://skills.sh/b/bekservice/Famulor-Skill`

## 3. npm (famulor-mcp, in the Famulor-MCP repo)

```bash
cd ../Famulor-MCP
npm login
npm publish --access public
```

`prepublishOnly` runs the build automatically. After publishing, `npx -y famulor-mcp` works as a stdio MCP server (requires `FAMULOR_API_KEY` env var).

## Checklist before publishing

- [ ] `skills/famulor-skill/SKILL.md` frontmatter has `name` + `description`
- [ ] Version bumped in `.plugin/plugin.json` and the `clawhub skill publish --version` flag
- [ ] `famulor.skill` archive regenerated if skill contents changed:
      `cd skills && zip -r ../famulor.skill famulor-skill`
- [ ] Changes pushed to GitHub (`git push origin main`) — GitHub installs always serve the latest main
