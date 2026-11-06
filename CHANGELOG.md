# Changelog

## 2.7.3 — 2026-11-06

- Document workspace Home pins on the dashboard create and update operations, including the CLI and MCP commands.

## 2.7.2 — 2026-11-05

- Add the booking deletion workflow and refresh the public REST, CLI, SDK and MCP catalogs.

## 2.7.1 — 2026-11-05

- Describe how to clear the default RCS fallback while retaining the existing SMS connection and other assigned numbers.

## 2.7.0 — 2026-11-04

- Document RCS as an optional part of the SMS channel: company sender drafts, branding, consent, review, explicit setup-credit acceptance, activation and delivery policy.
- Document explicit incoming RCS default routing, optional send transport metadata and identical plain-text SMS fallback.
- Explain separate company setup, sending, delivery and receipt usage rates, including one-time creation units and variable null credit amounts.
- Explain basic UTF-8 byte classes, Unicode SMS fallback segments, rich content and incoming RCS replies without inventing a separate channel.
- Refresh 518 MCP tools and 512 public API operations with matching CLI and SDK mappings. Distribution assets are prepared locally; publication remains separate.

## 2.6.4 — 2026-11-04

- Refresh the 510-tool MCP catalog, public request contracts and client mappings for 504 operations, including the optional published no-failures condition for manual/scheduled Milian Missions.
- Explain the explicit approval boundary, one-to-six owned automation references, shared call/runtime limits and zero-model empty checks. Incomplete reads never prove that no failures occurred.

## 2.6.3 — 2026-11-04

- Explain safe runtime variable substitution in messaging, email and SMS tools, external CRM identifiers, target-assistant attribute permissions and post-call follow-up regression checks.

## 2.6.2 — 2026-11-02

- Explain how to replace or deactivate an unused payment link in the operator’s billing scope and schedule a running subscription to end at period end.

## 2.6.1 — 2026-11-02

- Number buyers can review the quoted monthly rent and setup fee in the checkout currency. The skill explains how to refresh an offer for the same number and how to handle an address or voice-capability conflict.
- Refreshed the public catalog of 509 MCP tools and 503 API operations and aligned the README with the bundled references.

## 2.6.0 — 2026-11-01

- Refresh the bundled catalogs to the 2026-11-01 public contracts: 509 MCP tools and 503 public API operations, including cancelling a running CRM sync.
- Number verification: every verification needs an address, even where the country's rules list no address document. An older verification in review or approved without one (`has_address: false`) gets it with `add_number_verification_address` / `POST /phone-numbers/verifications/{id}/address` (`famulor add-phone-number-verification-address`); it is not resubmitted and stays approved.
- Buying a number: `verification_address_required` names the verification that still needs its address; `bundle_address_missing` is a support case.

## 2.5.0 — 2026-10-29

- Refresh the bundled catalogs to the 2026-10-29 public contracts. Still 507 MCP tools and 501 public API operations.
- Live chat: optional quick replies. Clickable answers in website chat and Test Chat, off until enabled. A click is the visitor's next message. Phone, WhatsApp, Messenger, Slack and email do not show them.
- Voice: a human-transfer tool can have its own hours. Outside those hours the transfer is refused and the call continues.
- History: transcripts are read in spoken order, including older calls. A greeting can appear after the caller's first words.
- Quality Assurance: a call with no caller speech is not scored and not charged. A scored call's judge can see the assistant's tool actions.

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
