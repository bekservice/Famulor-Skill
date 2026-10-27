<p align="center"><img src="assets/logo.svg" alt="Famulor" width="88" /></p>

<h1 align="center">Famulor Skill</h1>
<p align="center">Build better voice, WhatsApp and webchat agents from your AI assistant.</p>

<p align="center">
<a href="https://github.com/bekservice/Famulor-Skill/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/bekservice/Famulor-Skill?color=087e98" /></a>
<a href="https://github.com/bekservice/Famulor-Skill/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/bekservice/Famulor-Skill/actions/workflows/validate.yml/badge.svg" /></a>
<a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-087e98" /></a>
<a href="https://skills.sh/bekservice/Famulor-Skill"><img alt="skills.sh" src="https://skills.sh/b/bekservice/Famulor-Skill" /></a>
</p>

[Famulor](https://www.famulor.io) builds AI assistants for phone calls, websites and messaging. This open-source skill teaches your AI client how to design their prompts, configure their tools, test their behavior and work with your Famulor workspace.

**Start with a business task.** The skill selects the relevant channel guide and current tools, instead of loading hundreds of endpoint descriptions into every conversation.

```bash
npx skills add bekservice/Famulor-Skill --skill famulor-skill
```

Then connect your client to `https://app.famulor.io/mcp` and sign in with OAuth. The skill supplies instructions; MCP supplies authorized workspace access. Prompt drafting works without a connection. Live data and changes require a Famulor account and the relevant plan and permissions.

[Installation guide](docs/installation.md) · [Worked examples](skills/famulor-skill/references/examples/README.md) · [Use cases](docs/use-cases.md) · [Prompt templates](skills/famulor-skill/assets/prompts) · [API index](skills/famulor-skill/references/api/index.md) · [Releases](https://github.com/bekservice/Famulor-Skill/releases)

## Choose what you want to build

| Use case | Try asking | Guide |
| --- | --- | --- |
| Phone receptionist | “Draft a bilingual receptionist that answers from our knowledge base and escalates urgent requests.” | [Voice prompting](skills/famulor-skill/references/voice-prompting.md) |
| Appointment booking | “Review my booking assistant. Make it check availability, confirm the time zone and verify the booking result.” | [Assistant design](skills/famulor-skill/references/assistant-design.md) |
| WhatsApp support | “Adapt our support assistant for WhatsApp, including human takeover and the messaging window.” | [Messaging](skills/famulor-skill/references/messaging-and-channels.md) |
| Website chat | “Create a webchat prompt with readable links and no spoken filler phrases.” | [Webchat](skills/famulor-skill/references/messaging-and-channels.md) |
| Email replies | “Draft email instructions with a clear answer and one next step.” | [Email](skills/famulor-skill/references/messaging-and-channels.md) |
| Quality review | “Review these conversations, identify recurring failures and propose regression tests.” | [Testing](skills/famulor-skill/references/testing-and-evaluation.md) |
| API integration | “Find the REST endpoint, CLI command and TypeScript method to list my assistants.” | [API and SDK](skills/famulor-skill/references/api-and-sdk.md) |

## See a complete assistant

The [worked examples](skills/famulor-skill/references/examples/README.md) turn familiar [Famulor demo scenarios](https://app.famulor.io/demo) into reviewable assistant designs:

| Example | What good looks like |
| --- | --- |
| [Hotel front desk](skills/famulor-skill/references/examples/hotel-front-desk.md) | Clear greeting, hotel knowledge, returned availability, confirmed reservation and recovery |
| [Drive-thru](skills/famulor-skill/references/examples/drive-thru.md) | Corrections update one basket; the current quote is confirmed and submitted once |
| [Order support](skills/famulor-skill/references/examples/order-support.md) | Verified order facts and controlled changes, with WhatsApp, webchat and email adaptations |
| [Lead qualification](skills/famulor-skill/references/examples/lead-qualification.md) | Useful discovery, an appropriate next step and respectful opt-out handling |

Each includes a filled business brief, complete prompt, setting placement, required runtime capabilities, an illustrative conversation and acceptance checks. The gallery's fictional business role-play is inspiration; the examples explicitly identify the real integrations needed before making customer-facing action claims. Use the [deliverable format](skills/famulor-skill/references/examples/assistant-deliverable.md) to see how an agent should present the finished proposal and its verification status.

## Install in your AI client

| Client | Setup |
| --- | --- |
| **Claude Code** | `/plugin marketplace add bekservice/Famulor-Skill`, then `/plugin install famulor@famulor`; authenticate in `/mcp` |
| **Claude web / desktop** | Upload the release's `famulor-skill.zip` in **Customize → Skills**, then connect Famulor separately |
| **ChatGPT** | Install the [Famulor plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a8a46791ed08191a79aa4c98f34d772) for assistant/history review; use a separate custom MCP connection for broader authorized actions |
| **Codex** | Install the skill, run `codex mcp add famulor --url https://app.famulor.io/mcp`, then `codex mcp login famulor` |
| **Cursor** | Install the skill and add the remote server in MCP settings |
| **Gemini CLI** | `gemini extensions install https://github.com/bekservice/Famulor-Skill` |
| **Other Agent Skills clients** | Use the universal installer above and configure Streamable HTTP MCP with OAuth |

See the [step-by-step guide](docs/installation.md) for prerequisites, exact commands, first-run verification, updates and troubleshooting. Client controls depend on the installed version and workspace policy.

**The public directory connection is read-only.** Its 11 tools review assistants and conversation history. Installing the full skill does not turn that profile into a write-enabled connection. A custom connection has its own approved permissions.

## What is included

- Channel-specific assistant design, voice prompting, messaging and evaluation guides grounded in Famulor's implementation.
- Adaptable prompts for reception, booking, qualification, WhatsApp, website chat and email.
- Four complete demo-inspired assistant designs, with expected conversations, failure paths and a model deliverable.
- **494 MCP tools in 14 groups** and **488 public API operations** with REST, CLI and TypeScript SDK navigation, reviewed on **27 October 2026**.
- An offline operation lookup, deterministic catalog generation and package validation.
- Portable Agent Skills plus Claude Code, Cursor and Gemini packaging; a separate restricted Claude Store package.
- Versioned ZIP and `.skill` downloads with SHA-256 checksums.

The catalogs are dated navigation snapshots. Live MCP schemas, the public OpenAPI contract and the installed CLI/SDK remain authoritative. Features can depend on your role, plan, channel and enabled integrations. This release does not deploy or change the Famulor service.

## A workflow you can review

1. **Discover:** identify the workspace, channel, current configuration and allowed tools.
2. **Design:** separate instructions from knowledge, tool configuration and routing.
3. **Validate:** test conversational behavior, tool outcomes and the actual target channel.
4. **Verify:** report what was drafted, saved, tested or delivered, with evidence.

The skill preserves the scope of your request. Reviewing a campaign does not start it; drafting a message does not send it. Authorized actions proceed without repeated confirmation, and uncertain writes are checked before retrying.

## Contribute

Found an outdated endpoint or a reproducible prompt failure? Open an [issue](https://github.com/bekservice/Famulor-Skill/issues/new/choose) with a redacted example. See [CONTRIBUTING.md](CONTRIBUTING.md) for validation and [SECURITY.md](SECURITY.md) for private reports.

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/package-release.py --check
```

If the skill helps, a star makes it easier for other Famulor builders to find. Share useful examples and improvements rather than private customer transcripts.

[Customer docs](https://docs.famulor.io/mcp/overview) · [Website](https://www.famulor.io) · [Support](https://www.famulor.io/support) · [MIT License](LICENSE)
