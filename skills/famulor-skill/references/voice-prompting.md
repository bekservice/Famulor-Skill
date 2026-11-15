# Prompting for phone and web voice

Use this with [assistant design](assistant-design.md). These recommendations are derived from Famulor's assistant behavior and voice-runtime contracts. General runtime documentation helps explain the design, but does not make every upstream feature available in a Famulor workspace.

## Write for one spoken turn

State the role and outcome first. Then describe how to take the next useful step. Prefer a short response and one question at a time; expand only when the caller asks or the task requires it. Acknowledge meaningful corrections without repeating every fact. Give a few options that a listener can remember rather than reciting a catalog.

Use Markdown headings to structure the instructions, but ask for natural spoken responses. Do not ask the voice assistant to read tables, JSON, tool names or technical errors. Preserve exact data sent to tools: saying an email as “name at example dot com” does not mean changing its stored value. Check ambiguous dates, amounts, names and addresses before an important action.

Keep business logic shared across channels. Place voice-only rules in a voice channel instruction or a clearly scoped voice section so they do not force WhatsApp or webchat to spell out links and email addresses.

## Use the correct field for the opening

- **Agent speaks first:** configure a short greeting. Empty text can produce an improvised opening.
- **Caller speaks first:** let the caller begin; configure the optional silence opening and delay if needed.
- **Uploaded greeting audio:** the recording takes precedence over text. Keep the accompanying text consistent with the recording and test playback.
- **Conversational flow:** ensure the Start greeting and entry behavior agree with the intended opening.

Do not repeat a full greeting inside the system prompt and the greeting field. Tell the assistant to continue from what the caller says after the configured opening. A useful introduction gives the business identity, any requested AI disclosure and one invitation to speak. Required consent belongs in the dedicated consent configuration, with the appropriate accepted and declined paths.

Full Duplex can rephrase ordinary generated greetings and tool announcements. Use the product's supported exact-audio or consent mechanisms when exact wording matters; prompt wording alone is not a playback guarantee.

## Make actions operational

For each assigned tool, write a compact decision rule:

```text
Use [actual availability tool] when the customer requests an appointment.
Collect the service, date range and timezone only if missing.
Offer only returned slots. If none are available, ask for another range.
Use [actual booking tool] after the customer has confirmed the concrete slot
and all required details are known. Report a booking only after success.
If the result is uncertain, check status before attempting the write again.
```

Replace the bracketed labels with the assigned callable names before saving. Tool descriptions and parameter schemas should carry the exact formats, required values and limits. The prompt provides decision context; it should not duplicate an entire API schema.

Avoid a text-only promise followed by waiting for the caller to say “okay” when the requested action is already authorized and ready. Invoke the action and describe its actual outcome. If a tool supplies its own hold or transfer announcement, avoid prompting an additional announcement that will play twice.

A spoken interruption changes the conversation; it does not reliably undo an external write. If the caller corrects a booking while it is running, inspect the result before making a second booking or claiming cancellation. An unavailable tool should lead to a truthful fallback, not a guessed success.

## Route and hand off deliberately

Human call transfer and transfer to another assistant are different operations. Configure the real destination or target assistant, the trigger, the unavailable path and any announcement. For a warm transfer, define the concise information the receiving person needs and what to do if they cannot accept.

A transfer tool can have its own hours, separate from the assistant's personal working hours. Outside those hours the tool refuses and the call continues with the assistant, including any configured outside-hours message. Do not tell the caller they are being connected when the tool has refused.

Announce a human transfer only in the turn that performs it. In German and English calls, the voice runtime treats a definite announcement such as “I'm connecting you now” as a commitment: if the assistant says it without calling the transfer tool, it is made to call that tool right away. An offer or a question (“If you like, I can connect you with a colleague. Would you prefer that?”) leaves the choice to the caller and starts nothing. The same applies to an announced SMS, email or hang-up. A lookup before the transfer, such as checking the time against service hours, does not replace the transfer call. After a completed transfer the assistant says nothing more and never transfers a second time, so do not script anything for after the transfer; put the announcement before it or use the tool's own announcement. In other languages, instruct the assistant to call the tool in the same turn as the announcement.

For an assistant handoff, select a context plan deliberately: full history, conversation messages, recent messages, summary with recent messages, summary only or no messages, as available in the live schema. Choose whether the target greets. A second full introduction can be disruptive after the caller has already explained the issue.

Pass the customer objective, verified facts, completed actions and remaining work. A summary should distinguish a requested booking from a completed one. Variables can remain available even without transferred conversation messages; do not assume the next assistant will hear every earlier sentence. Avoid handoff loops and do not route back just because the caller asks a follow-up.

Use the configured End call tool or End node after the request is resolved, the caller declines further help or clearly says goodbye. Do not end while a required action is unresolved. If the end tool supplies a farewell, avoid a second goodbye in a preceding response.

## Language, pronunciation and timing

Configure the primary and supported secondary languages, not only a language sentence in the prompt. Author instructions and short examples in the intended conversation language when practical. A foreign name or a tool result in another language is not a request to switch. Preserve names and addresses without translating them.

Use the pronunciation dictionary for recurring brand or product names with supported TTS voices. With native Full Duplex, put pronunciation hints directly in the prompt. A short phonetic spelling in the caller's language is often enough. Keep the stored spelling for tools and records. Start with plain punctuation and check supported markup before using tags or stage directions.

Treat interruption sensitivity, response timing, silence timeouts and maximum duration as settings. The prompt can tell the assistant to acknowledge a correction; it cannot guarantee an exact pause length or override engine timing. Diagnose the actual symptom before tuning: premature response, missed interruption, long tool wait and difficult pronunciation have different causes.

## Prompt for GPT-Live Full Duplex

Discover workspace access and compatible conversation voices first. Use `get_voices` with `mode: "realtime"` and `realtime_variant: "full_duplex"`. The voice's listed language is a recommendation for its sound. Use the full compatible list when comparing voices in another language. Configure the assistant's primary and optional secondary languages separately and listen to the selected voice in each. Keep the current voice on an existing assistant until the user chooses a replacement.

Keep the spoken role and task goal short. Write the prompt and spoken examples in the intended conversation language. Specify the form of address, how to listen, how to yield, and when to check current information. Keep the workflow and required confirmations with the configured tools and flow. Model-specific instructions about speech still need a voice test.

- **Listening:** Allow the caller to finish names, contact details and corrections. Brief listening sounds are optional during a long explanation. Pause while the caller thinks or dictates.
- **Interruptions:** Yield when the caller asks to stop, wait, or correct a detail. Continue with their latest request. If an action is running, check its outcome before confirming, canceling or retrying it. A brief listening sound from the caller is not agreement to an action.
- **Tool waits:** Ask for a missing detail before requesting work. Summarize confirmed results in short spoken sentences. Give an update during a long wait only when it reflects actual progress. Leave the configured tool announcement to the tool.

Example excerpt for German phone reception:

```text
Sprich ruhig und freundlich und verwende Sie. Stelle eine Frage pro Gesprächsschritt.
Lass Anrufer Namen und Zahlen zu Ende sagen. Gib ihnen auch bei kurzen Denkpausen Zeit.
Bei „Moment“ oder einer Korrektur gib das Wort ab. Verwende die zuletzt bestätigte Angabe.
Prüfe aktuelle Termine über die verfügbare Kalenderfunktion. Bestätige eine Buchung erst nach Erfolg.
```

Use the [Full Duplex reception example](examples/full-duplex-reception.md) to test pronunciation, interruptions and tool waits together. A Voice Design Prompt and its sample script are inputs for creating a voice in systems that offer voice design. In Famulor, choose a supported voice from the catalog and put behavior such as pacing and listening in the assistant prompt.

## Three practical starting points

| Use case | Minimal behavior | Required setup | Template |
| --- | --- | --- | --- |
| Reception / support | Identify intent, answer from approved facts, route unresolved requests | Maintained knowledge and an explicit human or callback path | [Receptionist](../assets/prompts/voice-receptionist.md) |
| Appointment booking | Check availability, confirm the chosen details, book once, report result | Calendar connection, compatible assigned tools and timezone | [Booking](../assets/prompts/voice-booking.md) |
| Outbound qualification | Explain the authorized reason for contact, check willingness, qualify briefly, respect refusal | Eligible audience, permitted outreach, suppression handling and approved next step | [Qualification](../assets/prompts/outbound-qualification.md) |

These are templates to adapt, not ready-made permission to contact anyone. Replace all bracketed instructions, map actual tools, remove unsupported capabilities and test before live use.

For complete examples, read [hotel front desk](examples/hotel-front-desk.md), [drive-thru corrections](examples/drive-thru.md) or [lead qualification](examples/lead-qualification.md). Each combines a full prompt with settings, runtime capability requirements, illustrative conversations and failure checks. Sample successes are not evidence that the gallery or the customer's system performed an action.

## Review checklist

- One clear purpose; no contradictory business or language rules.
- Greeting, consent and end behavior configured separately and tested together.
- Only available actions named; input collection and failure behavior specified.
- Knowledge, current operational data and caller-supplied claims distinguished.
- No secrets, private infrastructure details or unnecessary personal information.
- Unsupported requests, missing variables, interruptions and failed transfers covered.

Customer references: [speech prompting](https://docs.famulor.io/assistants/prompting-for-speech), [conversation quality](https://docs.famulor.io/assistants/conversation-quality), [languages](https://docs.famulor.io/assistants/languages).

Design references reviewed: [LiveKit prompting](https://docs.livekit.io/agents/start/prompting/), [tool loop design](https://docs.livekit.io/agents/logic/tools/design/), [agents and handoffs](https://docs.livekit.io/agents/logic/agents-handoffs/), and the [open-source Agents implementation](https://github.com/livekit/agents). Apply these principles through Famulor's supported configuration; customers do not need to deploy or configure a separate voice runtime.
