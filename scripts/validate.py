#!/usr/bin/env python3
"""Validate public packaging, local links, versions and publication boundaries."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {'.git', 'dist', '__pycache__'}


def public_files(root):
    return [p for p in root.rglob('*') if p.is_file() and not set(p.relative_to(root).parts).intersection(EXCLUDE)]


def validate(root=ROOT):
    errors = []
    version = (root / 'VERSION').read_text().strip()
    manifests = ['plugin.json', '.plugin/plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json',
                 'gemini-extension.json', 'claude-store/.claude-plugin/plugin.json']
    files = public_files(root)
    for path in files:
        if path.suffix == '.json':
            try:
                json.loads(path.read_text())
            except (ValueError, UnicodeError) as exc:
                errors.append(f'{path.relative_to(root)}: invalid JSON: {exc}')
    for name in manifests:
        if json.loads((root / name).read_text()).get('version') != version:
            errors.append(f'{name}: version must match VERSION')
    for path in (root / 'skills').glob('*/SKILL.md'):
        text = path.read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append(f'{path}: missing frontmatter')
            continue
        front = text.split('---', 2)[1]
        name = re.search(r'^name:\s*(\S+)', front, re.M)
        description = re.search(r'^description:\s*(.+)', front, re.M)
        if not name or name.group(1) != path.parent.name:
            errors.append(f'{path}: skill name must match its directory')
        if not description or len(description.group(1)) > 1024:
            errors.append(f'{path}: missing or oversized description')
        if f'version: "{version}"' not in front:
            errors.append(f'{path}: version must match VERSION')
    restricted = (root / 'claude-store/skills/famulor-assistants-history/SKILL.md').read_text()
    if f'version: "{version}"' not in restricted:
        errors.append('Restricted skill version must match VERSION')
    expected_urls = {
        'mcp.json': 'https://app.famulor.io/mcp',
        '.mcp.json': 'https://app.famulor.io/mcp',
        'claude-store/.mcp.json': 'https://app.famulor.io/mcp?profile=assistant-history',
    }
    for name, url in expected_urls.items():
        servers = json.loads((root / name).read_text())['mcpServers']
        if len(servers) != 1 or next(iter(servers.values())).get('url') != url:
            errors.append(f'{name}: unexpected server/profile')
    marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
    if marketplace['plugins'][0]['source'] != './' or marketplace['plugins'][0]['version'] != version:
        errors.append('Claude marketplace must point to this release at repository root')
    # These patterns catch publication accidents, not every possible secret.
    forbidden = [r'/Users/[^\s]+', r'/api/admin/', r'https://[a-z]{20}\.supabase\.co',
                 r'(?<!\w)gh[pousr]_[A-Za-z0-9]{30,}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                 r'(?<!\w)sk-(?:live-|proj-)?[A-Za-z0-9_-]{24,}']
    for path in files:
        if path.suffix not in {'.md', '.json', '.yaml', '.yml', '.svg', '.py'}:
            continue
        text = path.read_text()
        if path.name != 'validate.py':
            for pattern in forbidden:
                if re.search(pattern, text):
                    errors.append(f'{path.relative_to(root)}: private path, endpoint or credential-like content')
        if path.suffix == '.md':
            for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
                if re.match(r'^[a-z][a-z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                target = target.split('#')[0].split('?')[0]
                if target and not (path.parent / target).resolve().exists():
                    errors.append(f'{path.relative_to(root)}: broken local link {target}')
    return errors


if __name__ == '__main__':
    errors = validate()
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print('Public package, versions, profiles, JSON and local links validated.')
