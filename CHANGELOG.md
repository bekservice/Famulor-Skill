# Changelog

## 2.4.0 — 2026-10-28

- Refresh the bundled catalogs to 507 MCP tools and 501 public API operations.
- Automations: folders (list, create, rename, delete; `folder_id` on list, create and update), keyless export and import, share links (share, read, revoke, import from a link) and built-in templates (list, read, use). Imports, share links and templates always create drafts; connections, keys, workspace ids and captured test data are removed and listed as setup steps.
- Going live is refused while a draft still has required fields or placeholders (`YOUR_API_KEY`, `YOUR_ID`, `https://YOUR_WEBHOOK_URL`) open.

## 2.3.0 — 2026-10-27

- Refresh the bundled catalogs to 494 MCP tools and 488 public API operations, including duplicating an automation as an inactive draft and ten new messaging channels in the request contracts.
- Voice: announce a human transfer only in the turn that performs it. Offers and questions start nothing, an announced transfer, SMS, email or hang-up is carried out, and the assistant stays silent after a completed transfer.
- Booking: Cal.com meeting locations, the optional “Ask callers which location they prefer” setting, the caller's number for a phone-call location and confirmation emails in the conversation language.
- Messaging: LINE, Sendblue, Linq, Zernio, Mattermost, Webex, Lark/Feishu, Linear, Notion and Twitch, with reply formats, group-thread follow-ups without a new mention and Meta's 24-hour window for Messenger and Instagram.
- Testing: regression scenarios for an announced transfer, a declined transfer offer and a booking with a location choice; check remote MCP tools in a real conversation.
- Installation: Cursor signs in with OAuth natively.

## 2.2.2 — 2026-10-21

- Document customer assistant handoffs across messaging and native email, persistent target selection, channel restrictions and acceptance checks.
- Refresh the public API catalog with the optional target greeting setting; retain existing operation IDs and client mappings.
- Keep Milian identified as the platform copilot, separate from customer assistants.

## 2.2.1 — 2026-10-21

- Add four complete worked examples inspired by the public demo gallery: hotel front desk, drive-thru, order support across channels, and lead qualification.
- Show full prompts, setting placement, required runtime capabilities, illustrative conversations, failure paths and acceptance criteria.
- Add a model assistant deliverable and progressive example routing inside the installable skill.
- Clearly separate fictional demo role-play, illustrative test fixtures and verified actions in a customer integration.

## 2.2.0 — 2026-10-21

- Add practical channel-specific guidance for voice assistants, WhatsApp, website chat and email, with adaptable prompts and evaluation scenarios.
- Explain which instructions belong in shared prompts, channel prompts, tools, knowledge and settings.
- Refresh all 14 MCP toolset references to 493 tools and add a complete 487-operation REST/CLI/TypeScript API index with offline lookup.
- Add use-case navigation and verified installation guidance for Claude, ChatGPT, Codex, Cursor and Gemini CLI.
- Add a Claude Code marketplace manifest, portable skill metadata, contribution and security guides, and issue templates.
- Add deterministic ZIP/skill packaging, SHA-256 release checksums and automated validation.
- Preserve the separate 11-tool read-only Assistant & History profile; the public skill does not expand connection permissions.

## 2.1.6

Official Famulor mark and the 439-tool MCP catalog. Earlier release details are available in [GitHub Releases](https://github.com/bekservice/Famulor-Skill/releases).
