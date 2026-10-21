# A complete assistant deliverable

When a user asks for an assistant, return the pieces needed to review and implement it together. A system prompt alone leaves the greeting, knowledge, tools and channel behavior unresolved. Scale the format to the task: for a small prompt fix, show the changed sections and their effect instead of rewriting the entire design.

The filled response below uses the same fictional Hotel Seeblick design and fixed fixtures as the [hotel front-desk example](hotel-front-desk.md). The reviewed gallery assistant role-plays hotel outcomes without inventory or reservation tools. This production design adds the required integrations; it is not a clone, a saved assistant or a live test result.

## 1. State the outcome and status

> **Hotel Seeblick front desk — draft for review**
>
> Clara helps guests understand hotel policies, find a suitable room and complete a reservation only when the configured reservation tool confirms it. This proposal targets inbound phone or browser voice in English with configured German support. Unresolved requests can go to a front-desk follow-up integration. No assistant has been changed and no call or reservation has been made.

For actual work, replace that status with the evidence available. A saved prompt is not a tested call, and a completed intake is not a confirmed reservation.

## 2. Show where each piece belongs

| Piece | Example design | Implementation evidence to record |
| --- | --- | --- |
| Conversation structure | One Prompt, bounded front-desk role | Saved assistant structure |
| Channel | Inbound phone or browser voice | Correct assistant connected to the intended channel |
| Language and voice | Primary English, secondary German; a currently available compatible voice | Selected languages and voice from the workspace catalog |
| Greeting | “Hello, I'm Clara, Hotel Seeblick's AI assistant. How can I help?” | Greeting field; agent speaks first |
| Shared system prompt | The behavior block below | Saved shared prompt |
| Knowledge | Approved hotel policies and service descriptions | Assigned knowledge source and reviewed facts |
| Current data | Room availability and the returned rate conditions | Assigned availability capability and its input schema |
| Reservation action | Submit the guest's confirmed choice once | Assigned reservation capability and its success/failure behavior |
| Human fallback | Submit a front-desk follow-up request; otherwise provide a verified contact option from knowledge | Accepted request and returned reference, or an accurately reported failure |
| Closing | Briefly summarize the actual outcome, then finish when the guest is done | Configured end behavior without a duplicate farewell |

Do not fill evidence cells with invented resource IDs. During drafting, mark unresolved items as required setup. During implementation, resolve resources in the intended workspace and read the saved configuration back.

## 3. Provide the actual prompt separately

This short behavior block shows the finished writing style. Before saving, map its capability roles to the actual assigned callable names and resolve the follow-up integration. The [hotel example](hotel-front-desk.md#complete-system-prompt) contains the complete scenario prompt.

```text
You are Clara, the AI front-desk assistant for Hotel Seeblick.
Help guests understand hotel services, find a suitable stay and complete
only the actions supported by your configured tools.

Continue from the configured greeting. Give a concise spoken answer and
ask one useful question at a time. Use details already provided; acknowledge
corrections and update the current request without restarting the conversation.

Use the assigned hotel knowledge for policies and services. Use the assigned
availability capability for current rooms, rates and conditions. Collect the
arrival date, departure date and guest count only when missing. Offer only
options returned for the current request and clarify an ambiguous date.

Before a reservation, establish the selected room, dates, guest details and
any required acceptance of the returned terms. Once the guest has clearly
confirmed the concrete request and required inputs are known, submit it once
through the assigned reservation capability. Say it is confirmed only after
that capability returns a definite successful reservation result.

If a submission has an uncertain result, check its status when supported.
Otherwise explain that the reservation is not yet verified and use the
configured front-desk fallback. Do not repeat an uncertain write blindly.
Do not promise an email, payment, cancellation or completed human contact without the
corresponding successful result.

For an unsupported request, a missing answer or a request for a person,
offer the configured front-desk follow-up and collect only its required
contact details and reason. Say the request was saved only after acceptance.
Do not promise a callback time unless the result provides one. If submission
fails, explain that it was not saved and provide a verified contact option.
```

Keep substantial hotel facts outside this behavior block. The shared synthetic knowledge fixture has check-in at 15:00, check-out at 11:00, breakfast included in the quoted rate and spa hours of 07:00–21:00. Late checkout depends on availability. These are fictional teaching facts; current room offers and rates come from the reservation lookup.

## 4. Explain the tool contract without inventing an integration

| Capability role | When to use it | What the result must establish |
| --- | --- | --- |
| Availability lookup | Dates and guest count are known | Current options, rate basis and relevant conditions, or no matching option |
| Reservation submission | The specific choice and required guest details are confirmed | Confirmed reservation, explicit refusal/conflict, or an uncertain result |
| Reservation status lookup, if supported | A submission outcome is uncertain | Whether that same request completed; it must not create a second reservation |
| Front-desk follow-up | Guest requests human help or the reservation path cannot finish | Accepted request and reference, or failure; a saved request does not mean a person has called |

These are capability roles, not literal tool names or API request bodies. The configuring agent must inspect assigned runtime tools and replace these roles with the real callables. Management MCP access does not assign these capabilities by itself.

## 5. Show the expected experience

**Illustrative trace — no tools were executed.** Use the fixed hotel fixture below consistently. These are fictional offers, references and semantic outcomes, not actual bookings or public API response schemas. Resolve relative dates against the real current time and timezone when implementing another request.

| Turn | Expected behavior |
| --- | --- |
| Guest: “A lake-view room for two, from June 21 to June 23, 2030.” | Clara uses the supplied dates and guest count without asking for them again. |
| Availability fixture: `DEMO-LAKE-01`, two nights, lake-view double, EUR 378 stay total, breakfast included, free cancellation until 48 hours before arrival | Clara offers that room and the returned terms. She does not invent another option or say it is reserved. |
| Guest confirms that exact option and supplies required details | Clara submits the reservation once. She does not add a generic confirmation loop after an already complete authorization. |
| Reservation fixture: confirmed, `DEMO-HOTEL-104`, payment on arrival, email not sent | “Your reservation is confirmed. Your reference is Demo Hotel 104, and payment is on arrival. Check-in starts at three in the afternoon.” No claim of email delivery. |
| Alternative fixture: pending with `DEMO-REQUEST-7`; supported lookup returns not created | Clara says the reservation did not complete and offers a front-desk follow-up request. She does not claim success or immediately resubmit. |

Include at least one failure or correction path alongside the successful path. The example should teach the decision that changes the response, not merely prescribe a polished sentence.

## 6. Close with acceptance criteria and remaining work

For this proposal, the acceptance checks are:

- Answer a policy question from the assigned knowledge without an unnecessary availability lookup.
- Resolve ambiguous dates, then offer only returned rooms and rates.
- Apply a corrected guest count before submission.
- Handle no availability with a supported alternative.
- Confirm a reservation only from a successful result; handle a pending or uncertain write without duplication.
- Report a follow-up as requested only after acceptance; never imply a live transfer or completed callback. Avoid duplicate greeting or closing audio.

Finish the user-facing deliverable with a compact status such as:

> **Ready:** reviewed draft, greeting and acceptance cases.
> **Required setup:** select the real knowledge source; bind the availability, reservation and supported status callables; configure front-desk follow-up.
> **Not yet verified:** saved configuration, actual channel behavior and authorized reservation/recovery tests.

When implementation is authorized, replace those draft statements with the saved resource/version and observed results. Use [testing and evaluation](../testing-and-evaluation.md) to choose the right test. Illustrative dialogues, simulated results, real voice tests and external action outcomes must remain separately identified.
