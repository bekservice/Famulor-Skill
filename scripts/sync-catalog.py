#!/usr/bin/env python3
"""Refresh the portable skill's navigation snapshot from Famulor's MCP registry JSON.

Export the canonical registry in Famulor-Multi-Tenancy with:
  node --import tsx -e "import('./src/lib/mcp/tool-registry.generated.ts').then(m=>console.log(JSON.stringify(m.MCP_GENERATED_TOOL_REGISTRY)))" > /tmp/famulor-mcp-registry.json
Then run this script with that JSON path. The live MCP schema remains authoritative.
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/famulor-skill/SKILL.md"
REFERENCES = ROOT / "skills/famulor-skill/references/toolsets"
GROUPS = {
    "assistants": ("Assistants, versions, models, voices, reusable tools, bookings, tests, and integrations", "Assistants, models, voices, reusable tools, bookings, integrations, tests, and simulations."),
    "calls": ("Calls, unified history, transcripts, QA, callbacks, and live control", "Calls, unified history, transcripts, QA, callbacks, and live control."),
    "campaigns": ("Campaigns, Audience contacts, leads, segments, consent, suppression, and outbound limits", "Campaigns, Audience contacts, leads, segments, consent, suppression, and outbound limits."),
    "messaging": ("WhatsApp, Messenger, email, Slack, connectors, templates, and sender profiles", "Messaging, email, connected channels, templates, and sender profiles."),
    "telephony": ("Phone numbers, SIP trunks, caller IDs, carriers, and number verification", "Phone numbers, SIP, caller IDs, routing, and verification."),
    "knowledge": ("Knowledge bases, documents, FAQs, websites, and connected drives", "Knowledge bases, documents, FAQs, websites, and connected drives."),
    "dashboards": ("Dashboards, analytics, widgets, and layout", "Dashboards, analytics, widgets, and layout."),
    "automations": ("Automations, connections, CRM sync, routines, and runs", "Automations, connections, CRM sync, routines, and runs."),
    "billing": ("Balance, usage, transactions, invoices, billing recovery, and referrals", "Balance, usage, transactions, invoices, billing recovery, and referrals."),
    "settings": ("Account, workspaces, API keys, retention, memory, domains, and sessions", "Account, workspaces, API keys, retention, memory, domains, and sessions."),
    "platform": ("Authorized reseller customer administration", "Authorized reseller customer administration."),
    "migration": ("Previewing and importing supported Famulor 1.0 resources", "Previewing and importing supported Famulor 1.0 resources."),
    "tasks": ("Durable exports, simulations, crawls, and campaign preparation", "Durable exports, simulations, crawls, and campaign preparation."),
    "milian": ("Milian workspace questions and voice sessions with additional credits", "Milian workspace questions and voice sessions. Both require explicit approval for additional credits."),
}


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ").strip()


def render_reference(group, tools, date):
    intro = GROUPS[group][1]
    lines = [
        f"# {group.capitalize()} toolset",
        "",
        f"{intro} Connect only this group with `https://app.famulor.io/mcp?toolsets={group}`.",
        "",
        f"This {date} snapshot covers all {len(tools)} tools assigned to `{group}` in the canonical {sum(COUNTS.values())}-tool registry. The live MCP `tools/list` response is authoritative for arguments, current availability, annotations, and plan or role gating. Never invent fields from this catalog.",
        "",
        "| Tool | Effect | Accepted scope | Execution | Purpose snapshot |",
        "| --- | --- | --- | --- | --- |",
    ]
    for tool in sorted(tools, key=lambda x: x["name"]):
        annotations = tool["annotations"]
        effect = "Read-only" if annotations["readOnlyHint"] else ("Delete/destructive" if annotations["destructiveHint"] else "Write/action")
        scopes = " or ".join(tool["scopes"]) or "None"
        execution = {"forbidden": "Immediate", "optional": "Task optional", "required": "Task required"}[tool["taskSupport"]]
        lines.append(f"| `{tool['name']}` | {effect} | `{cell(scopes)}` | {execution} | {cell(tool['description'])} |")
    return "\n".join(lines) + "\n"


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("registry_json", type=Path)
parser.add_argument("--check", action="store_true", help="fail if the checked-in catalog differs")
parser.add_argument("--date", default="2026-09-29")
args = parser.parse_args()
registry = json.loads(args.registry_json.read_text())
names = [entry["name"] for entry in registry]
if len(names) != len(set(names)):
    raise SystemExit("duplicate MCP tool names")
COUNTS = Counter(entry["toolset"] for entry in registry)
if set(COUNTS) != set(GROUPS):
    raise SystemExit(f"toolset mismatch: {set(COUNTS) ^ set(GROUPS)}")

updates = {}
for group in GROUPS:
    path = REFERENCES / f"{group}.md"
    updates[path] = render_reference(group, [entry for entry in registry if entry["toolset"] == group], args.date)

skill = SKILL.read_text()
table = ["| Toolset | Use for | Current tools | Reference |", "| --- | --- | ---: | --- |"]
for group, (purpose, _) in GROUPS.items():
    table.append(f"| `{group}` | {purpose} | {COUNTS[group]} | [{group}](references/toolsets/{group}.md) |")
skill, replacements = re.subn(
    r"\| Toolset \| Use for \| Current tools \| Reference \|\n.*?(?=\nThe full snapshot contains)",
    "\n".join(table) + "\n",
    skill,
    count=1,
    flags=re.S,
)
if replacements != 1:
    raise SystemExit("could not find skill toolset table")
skill = re.sub(r"The full snapshot contains \d+ tools", f"The full snapshot contains {len(registry)} tools", skill)
updates[SKILL] = skill

stale = [str(path.relative_to(ROOT)) for path, content in updates.items() if not path.exists() or path.read_text() != content]
if args.check:
    if stale:
        raise SystemExit("stale catalog: " + ", ".join(stale))
else:
    for path, content in updates.items():
        path.write_text(content)
print(f"{len(registry)} tools across {len(GROUPS)} toolsets; {'stale: ' + ', '.join(stale) if args.check and stale else 'catalog current'}")
