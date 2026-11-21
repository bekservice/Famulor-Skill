# Campaigns, sequences and templates

Use this guide to plan, build, launch, change and measure an outreach campaign through MCP, REST, CLI or SDK. Exact request contracts stay in the [Campaigns API](api/campaigns.md) and [campaigns toolset](toolsets/campaigns.md); look up a field with the bundled `find-operation.py` instead of guessing it.

Building a campaign does not authorize contacting anyone. Creating, filling or editing a draft is not a launch. Launch, start, resume and scheduling reach real people and need the human's explicit go-ahead.

## Classic or sequence

A **sequence** decides what happens to each contact of a phone campaign: how often to call, which outcome leads where, when to send an SMS & RCS message, a WhatsApp template or an email, and when to stop.

- Sequences exist only for `phone_call` campaigns that use their own contact list. WhatsApp, SMS and external-audience campaigns, and phone campaigns created without `sequence`, are classic: they keep the retry policy and the optional `follow_up_config`.
- A campaign created through API, MCP or CLI without `sequence` stays classic. A started campaign keeps its kind; you cannot add or remove its sequence later.
- `number_pool`, `contact_timezone_mode`, `holidays` and `double_dial` need a sequence. Without one they are rejected; removing the sequence of a draft resets them.
- A sequence replaces `follow_up_config`. Sending both is a 400 error; use a message step instead.
- Plan gates: sequences and number pools need **Campaign sequences**. A sequence whose first step is a message also needs **multi-channel campaigns**; WhatsApp steps need WhatsApp text and RCS senders need RCS in the plan. Report a plan denial; do not work around it.

## Start from a template

The template gallery holds ready-made sequences for calls, SMS & RCS, WhatsApp and email. Prefer a template over a hand-built sequence when one fits the user's goal.

1. **List.** Call `list_campaign_templates` (REST `GET /campaign-templates`, CLI `famulor list-campaign-templates`, SDK `client.campaigns.templates()` or `client.api.listCampaignTemplates`). Pass `language` as the user's language when it is `en`, `de`, `fr` or `es` (unknown values fall back to English) and optionally `category`: `basics`, `sales`, `appointments`, `service`, `billing` or `events` (an unknown category is a 400). Featured templates come first.
2. **Choose with the user.** Show the closest match by its returned `name`, `description`, `channels` and `step_count`. Use only ids and sequences the call returned; never invent a template, rename an id or claim a template exists in another language than the one returned.
3. **Fill the senders.** When `needs_sender` is `true`, the sequence still has empty senders:
   - each `sms` step needs exactly one of `from_number_id` (an SMS-capable workspace number from `list_phone_numbers`) or `rcs_sender_id` (an approved, ready company sender from `list_sms_rcs_senders`). Both or neither is a 400 error.
   - each `whatsapp_template` step needs `connector_id` and `template_id` from `list_messaging_connectors` and `list_whatsapp_templates`: an active sender and an approved text template whose placeholders map to contact fields.
   - `email` steps send from the verified address of the step's assistant (by default the campaign assistant); call steps use the campaign assistant.

   Use only ids returned for this workspace. When several senders fit, ask the user which one to use; when none exists, explain the missing channel setup instead of inventing an id. Until every sender is set, create and update reject the campaign.
4. **Adjust the copy.** Templates ship with message texts. Replace placeholders such as `[add your review link]` with real values from the user; never fabricate a link, price or offer.
5. **Save.** Pass the edited `sequence` to `create_campaign` (`channel: "phone_call"`, the assistant and the contact list setup) or to `update_campaign` for an existing draft. A template replaces the whole sequence, so use it only before the campaign was started; afterwards edit the steps.

## Sequence structure

`sequence` has `version: 1`, `start_node_id` and `nodes` (1 to 10 steps). Step and outcome ids match `^[a-z0-9][a-z0-9_-]{0,39}$`. A step without `channel` (or with `phone_call`) is a call step. Steps have no position: a `position` in a request is ignored.

**Call steps** have `attempts` (1 to 10; each `delay_minutes` counts from the start of the previous attempt, optional per-attempt `voicemail` with `hangup` or `drop_message`), an optional `assistant_id`, up to 10 `outcomes`, and the built-in routes `no_response` and `other`.

- An outcome's `condition` is either `{"type": "prompt", "description": "..."}`, where an AI matches the description against the call transcript, or `{"type": "rules", "match": "all" | "any", "rules": [...]}`, which checks call data without AI.
- Built-in outcomes: **No response** (every attempt unanswered or voicemail), **Other** (answered, nothing matched) and **Do not call** (the contact asked not to be called again or is suppressed). Do not call is detected automatically, wins over custom outcomes and ends the contact.
- A destination is another step (`{"type": "node", "node_id": ...}`, at least 5 minutes after an answered call), `retry` (next attempt of the same step; with none left, No response applies) or `{"type": "end", "successful": true | false}`. A successful end counts the contact as **Converted**.
- `global_outcomes` are sequence-wide outcomes that end the contact; `save_to_field` can write a value to a contact field when an outcome applies.

**Message steps** have `channel` `sms`, `whatsapp_template` or `email` and a `message` with `config`, `wait_minutes`, `next`, `failed` and optional `replied`. Only channels that can write first to a known phone number or email qualify; Telegram, Messenger, Instagram, web chat and WhatsApp Call are not steps.

| Route | Applies when |
| --- | --- |
| `next` (Sent / No reply) | The wait is over without a reply |
| `replied` | The contact answered on the same channel during the wait (needs a wait of at least 1 minute) |
| `failed` (Not sent) | No email address, channel opt-out, provider rejection, or RCS cannot reach the contact |

A reply on another channel does not count. An SMS `STOP` opts the contact out and never counts as Replied. A message the provider accepted, or whose result is unclear, is treated as sent and never sent twice. Messages follow the same calling hours, time zone and holidays as calls, plus the channel's workspace quiet hours.

## Schedule and caller numbers

- `contact_timezone_mode`: `campaign` uses the campaign time zone; `contact` derives each contact's zone from the phone number. A number with several possible zones is called only while every zone's hours are open. A contact whose hours never open in the next year gets `enroll_failure: no_calling_window`.
- `holidays`: `public: true` skips national public holidays of the contact's country where they are known (Austria, Belgium, Canada, Switzerland, Germany, Spain, France, the United Kingdom for England and Wales, Ireland, Italy, the Netherlands, United States; no regional holidays). `custom_dates` (up to 100 `YYYY-MM-DD`) count in the contact's local time.
- `double_dial` redials once immediately after no answer or busy. It is off by default. Repeated immediate calls can be an unreasonable nuisance under EU law; enable it only when the user confirms they checked this for the countries they call.
- `number_pool`: `mode` `local_presence` (area-code match in the US and Canada, Germany, Austria and Switzerland, otherwise the contact's country, otherwise the default) or `round_robin`, with `phone_number_ids` (active, outbound-capable workspace numbers) and an optional `default_phone_number_id`. A contact keeps its first caller ID for later attempts. Plan roughly one number per 50 contacts. The mode is fixed after the first start; numbers can still change.

## Launch with the compliance confirmation

A sequence campaign launches with `launch_campaign` (REST `POST /campaigns/{id}/launch`, CLI `famulor launch-campaign`). The request needs `compliance_attestation: true`; without it the call fails with `attestation_required`. `start_campaign` accepts the same field; a never-launched sequence campaign started without it fails with `launch_required`.

The attestation is the human's legal confirmation, not a technical flag. Set it only when the human user (or the API key holder in their own integration) explicitly confirms, for this campaign, that it complies with all laws and consent requirements for the contacts, including do-not-call lists and opt-in rules (for example TCPA in the US, UWG and GDPR in the EU). Never set it on your own initiative, carry it over from another campaign, or infer consent from a contact list, a CRM tag or an earlier conversation. Famulor stores who confirmed, when, from which surface and which wording version.

Before asking for the confirmation, show what will run: contacts (blocked ones are counted separately), assistant, steps, senders, pool numbers, calling hours and the start time.

1. Read the campaign with `get_campaign` and keep its `sequence_hash` unchanged. Pass it to `launch_campaign`; if the sequence changed since the user reviewed it, the launch fails with `sequence_changed` and nothing starts. Omit it for a campaign without a sequence.
2. Send `start_at: null` to start now, or an ISO 8601 time at least 5 minutes ahead to schedule.
3. With **Auto-complete when no leads remain** (`mark_complete_when_no_leads`) on, the default, a campaign without contacts is refused with "The campaign has no leads." With it off, the campaign waits for contacts added later.
4. Verify the returned status. `cancel_campaign_schedule` returns a scheduled campaign to draft and clears its schedule and confirmation.

Famulor checks the workspace suppression list before every call. It does not screen national or state do-not-call registries unless the workspace turned on the US Federal and State DNC checks; until those are verified, call steps do not dial US numbers (message steps still send). This guide is not legal advice.

## Pause, change and resume

| Status | Sequence edits |
| --- | --- |
| Draft | Allowed |
| Paused | Allowed; contacts keep their place |
| Running | 409 "Pause the campaign to edit the sequence." Use `pause_campaign` first |
| Scheduled | Locked; `cancel_campaign_schedule` first |
| Completed | 409 "Duplicate the campaign to change the sequence." Use `duplicate_campaign` (a draft with the same settings, no contacts, no schedule, no confirmation; counts against the plan's campaign limit) |

- Read `sequence_step_contacts` from `get_campaign_stats` first. Every step that still has unfinished contacts must stay, with the same step type; otherwise the update fails with 409 `Step "<name>" still has <n> contacts. ...`.
- A step added to a started campaign, a kept step id that changes type, and an outcome added to a step need an id that history never used there.
- A running wait or delay keeps its end time; the new value applies from the next send or attempt. Sent messages are not resent, and no contact restarts at the first step.
- "The campaign changed while it was saved." means the status changed between read and write: read again and retry once.
- A changed sequence clears the launch confirmation. Ask the user to confirm again, then resume with `resume_campaign` (or `start_campaign`) and `compliance_attestation: true`; without it the resume fails with `launch_required`. A paused campaign whose sequence did not change resumes without it.
- `pause_campaign` and `stop_campaign` stop new calls; calls in progress finish normally.

## Read contacts and analytics

Each sequence contact carries `stage` (`enrolled`, `in_progress`, `completed`, `enroll_failed`, `failed`), `sequence_node_id`, `sequence_attempt`, `campaign_outcome` (custom outcome id, or `no_response`, `other`, `do_not_call`, `sent`, `replied`, `not_sent`), `converted_at`, `enroll_failure` (`suppressed`, `invalid_number`, `no_calling_window`) and `caller_phone_number_id`.

`get_campaign_analytics` (REST `GET /campaigns/{id}/analytics`) returns the per-contact funnel; `get_campaign_stats` counts leads and calls instead.

| Figure | Definition |
| --- | --- |
| Dialed | Contacts with at least one call in the period |
| Connected | Contacts with at least one answered call with talk time (not voicemail or unavailable) |
| Converted | Contacts that reached a successful end; classic campaigns count calls marked successful or with a true goal field |
| Conversion rate | Converted divided by Dialed, capped at 100%; empty while nothing was dialed |
| Messages sent | Messages accepted for sending by message steps; failed sends are not counted |

The response also covers talk time and call cost in the workspace currency (not credits), the outcome flow as a Sankey (up to four steps, later steps combined), activity per day in the campaign time zone, and the caller numbers used. Filter with `from`/`to` (at most 366 days) and `phone_number_id`; Messages sent always counts the whole campaign because messages have no caller number. Report the numbers the tool returned; do not extrapolate conversions or attribute them to a single step without the outcome data.

## Write outcome descriptions the call can prove

Prompt outcomes are matched against the transcript, so describe observable results ("The contact booked a test drive", "The contact asked for a written quote by email") rather than intentions or sentiment guesses. For rules, prefer call data the assistant actually sets: the analysis goal field, a scheduled callback, a transfer or a call marked successful. Keep the assistant's prompt consistent with the outcomes: it must not promise a follow-up message that no step sends.
