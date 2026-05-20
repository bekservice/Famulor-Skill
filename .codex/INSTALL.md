# Installing Famulor Skill for Codex

Enable Famulor skills in Codex via native skill discovery.

## Prerequisites

- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bekservice/Famulor-Skill.git ~/.codex/famulor-skill
   ```

2. **Create the skills symlink (points at the skill directory inside the repo):**

   **macOS / Linux:**
   ```bash
   mkdir -p ~/.agents/skills
   ln -s ~/.codex/famulor-skill/skills/famulor-skill ~/.agents/skills/famulor-skill
   ```

   **Windows (PowerShell):**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
   cmd /c mklink /J "$env:USERPROFILE\.agents\skills\famulor-skill" "$env:USERPROFILE\.codex\famulor-skill\skills\famulor-skill"
   ```

3. **Restart Codex** (quit and relaunch the CLI).

## Verify

```bash
ls -la ~/.agents/skills/famulor-skill/SKILL.md
```

Then ask Codex to perform a Famulor task (for example: "Create an outbound assistant in Famulor").

## Updating

```bash
cd ~/.codex/famulor-skill && git pull
```

## Uninstalling

```bash
rm ~/.agents/skills/famulor-skill
```

Optionally delete the clone:

```bash
rm -rf ~/.codex/famulor-skill
```
