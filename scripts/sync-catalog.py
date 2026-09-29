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
    "campaigns": ("Campaigns, Audience contacts, leads, segments, consent records, and suppression", "Campaigns, Audience contacts, leads, segments, consent records, and suppression. Connect the `settings` group as well when you need workspace consent mode or outbound limits."),
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

SAFETY_NOTES = {
    "assistants": "Creating or changing an assistant can change live customer interactions. Read the current configuration and confirm the intended assistant and change before saving consequential edits.",
    "calls": "Calls and live-call controls can incur charges or disrupt active conversations; history removal can permanently delete data. Confirm the exact call, recipient, and action before execution.",
    "campaigns": "Campaign starts and contact changes affect real recipients. Erasing customer memory is permanent; removing suppression can restore contactability. Verify lawful consent and the exact target before these actions.",
    "messaging": "Sending messages or disconnecting channels has real external effects. Deleting a domain removes its addresses; deleting a synced template may affect its provider copy. Confirm the recipient or resource before execution.",
    "telephony": "Buying numbers or placing calls can incur charges; releasing numbers and changing routing can disrupt service. Confirm the number, target, cost, and intended action first.",
    "knowledge": "Crawls and drive syncs can consume credits; deleting sources or documents may remove indexed content. Review source and cost before running or deleting.",
    "dashboards": "Dashboard, widget, and logo deletion removes workspace resources. Confirm the exact resource and whether it can be recovered before deleting.",
    "automations": "Routines can keep running unattended after a tool call returns, perform workspace actions, and incur charges. Review the prompt, schedule, permissions, and expected side effects; confirm before creating, enabling, or running one.",
    "billing": "Billing and reseller-plan changes can affect invoices, taxes, credits, or customer entitlements. Confirm the workspace or customer plan and the financial effect before changing them.",
    "settings": "API-key revocation, session sign-out, domain removal, retention changes, and ownership transfer can disrupt access or remove data. Confirm the exact account, workspace, and irreversible impact first.",
    "platform": "Reseller administration can affect customer accounts and credits. Verify the customer workspace, authority, and intended change before execution.",
    "migration": "Imports create or change workspace resources. Preview the exact source and destination, then confirm before starting an import.",
    "tasks": "History exports can contain sensitive conversation data. Confirm export authority and handle download links privately; check asynchronous task status before claiming completion.",
    "milian": "Milian questions and voice sessions consume additional workspace credits. Explain the cost and obtain approval for each request.",
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
        "Toolsets limit discovery context; they do not grant access. OAuth/API scopes and workspace roles are enforced separately. The Effect column reflects MCP risk annotations: `Delete/destructive` also covers overwrites or changes that can remove data or safeguards.",
        "",
        f"**Caution:** {SAFETY_NOTES[group]}",
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
