# Choose a use case

Use these requests after [installation](installation.md). Replace the business details with your own. Requests that only draft or review do not change account data. State explicitly when you want a reviewed configuration saved or an external action performed.

## Launch a voice receptionist

> Use Famulor Skill to draft an English and German receptionist for our repair business. It should answer from our service knowledge base, collect the problem and preferred callback time, and escalate urgent issues. Explain which settings and tools need configuration. Do not place calls.

Start with [assistant design](../skills/famulor-skill/references/assistant-design.md), then the [receptionist template](../skills/famulor-skill/assets/prompts/voice-receptionist.md). Verify the opening, caller interruptions, language switching, knowledge retrieval and the handoff destination before routing customer traffic.

## Book appointments reliably

> Review our booking assistant's prompt and available calendar tools. Check that it resolves the time zone, offers actual availability, confirms the selected slot and reports a booking only after success. Propose a test for a slot that becomes unavailable.

Use [voice prompting](../skills/famulor-skill/references/voice-prompting.md) and the [booking template](../skills/famulor-skill/assets/prompts/voice-booking.md). A tool name in prompt text cannot connect a calendar. Test the configured integration with authorized test data.

## Adapt support to WhatsApp

> Draft a WhatsApp support prompt based on our shared assistant. Keep essential company policy in the shared system prompt, use short replies, support human takeover and explain when an approved template is required. Do not send or submit anything.

Follow [messaging and channels](../skills/famulor-skill/references/messaging-and-channels.md) and the [WhatsApp template](../skills/famulor-skill/assets/prompts/whatsapp-support.md). Verify the connected sender, customer messaging window, consent and actual delivery result separately.

## Add website chat

> Adapt our phone assistant for website text chat. It should answer with readable links, avoid spoken filler, request contact details only when needed and answer the pending question after a knowledge lookup.

Use the [webchat template](../skills/famulor-skill/assets/prompts/webchat-support.md). Test the actual widget: welcome behavior, early visitor input, tool results, history and the configured escalation path.

## Improve email replies

> Draft email instructions for clear answers with one next step. Explain how native assistant email differs from a connected Gmail or Outlook draft workflow. Do not send email.

Use the [email template](../skills/famulor-skill/assets/prompts/email-support.md). Confirm the channel, approved recipient, signature behavior and whether the result is a draft or a sent message.

## Diagnose conversation quality

> Review my last ten support conversations. Group observed failures, distinguish tool errors from prompt issues, and propose the smallest prompt changes plus regression scenarios. Do not save changes.

Use [testing and evaluation](../skills/famulor-skill/references/testing-and-evaluation.md). A history preview may be incomplete. Treat audio, transcript, tool completion and delivery as separate evidence.

## Build an integration

> Find the public API operation for listing assistants. Show its required inputs, matching CLI command and TypeScript SDK method. Use environment-based credentials and keep the example read-only.

Use [API and SDK](../skills/famulor-skill/references/api-and-sdk.md) and the [complete operation index](../skills/famulor-skill/references/api/index.md). Look up the live schema before using a dated example.

## Prepare an outbound campaign

> Review the audience, consent, suppression and assistant configuration for our renewal campaign. Show a readiness checklist and propose a small test batch. Do not start it yet.

Use [campaign tools](../skills/famulor-skill/references/toolsets/campaigns.md). Preparing recipients is distinct from authorizing a campaign start. State target campaign, recipients, timing and intended action when requesting launch.

## Automate a recurring workflow

> Design a weekly summary of failed support calls, including its schedule, destination, access scope and expected costs. Keep it as a proposal until we have reviewed those details.

Use [automation tools](../skills/famulor-skill/references/toolsets/automations.md). Review actions that can continue unattended and verify the saved schedule and run history after an authorized setup.
