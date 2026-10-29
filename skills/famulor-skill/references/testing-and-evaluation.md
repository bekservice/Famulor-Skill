# Test behavior and verify outcomes

Use this after changing prompts, tools, flows, models, languages or channel settings. A good prompt review is useful, but does not demonstrate working audio, an authorized integration or a delivered message.

## Choose the right test layer

| Layer | What it can establish | What it does not establish |
| --- | --- | --- |
| Configuration read-back | Intended prompt, settings and assignments were saved | The conversation behaves as intended |
| Chat simulation | Multi-turn behavior, criterion checks and expected tool use against test responses | Real external writes, full flow execution or voice quality |
| Test Chat | Behavior and available integrations on the actual text conversation path | Microphone, telephony or spoken pronunciation |
| Voice test / voice simulation | The configured speech path, turn taking, language and tool behavior | Every future carrier, caller environment or conversation |
| History + external read-back | Recorded conversation outcome and confirmed external state | Anything missing from the returned evidence |

Chat simulations retrieve real knowledge when a knowledge base is attached. Other external actions use simulated responses, and flow branches are simplified. Some built-in workflows report unsupported-tool errors instead of simulating success. Voice simulations execute configured tools: bookings, messages and other side effects can be real. Test Chat is also not a promise that connected actions are simulated. Use authorized test recipients and test resources, and agree on any costs or side effects within the user's requested scope before execution.

Do not automatically escalate from a text simulation to a real outbound call merely because one failed.

## A repeatable workflow

1. Preserve a baseline: assistant version or current configuration, selected language/mode and the behavior to change.
2. Define observable criteria. Prefer “asks for a missing email before booking” over “is helpful.” Specify which external action must happen and which must not happen.
3. Create a test with the available `create_assistant_test` schema. Include a caller persona, goal/script and success criteria. Use the live schema for supported options; do not infer run-mode parameters from the UI.
4. Run the chosen test through `run_assistant_test`, or use `run_assistant_simulation_task` when a durable task is appropriate. Chat runs can complete in the response. Voice runs return a running state; poll `list_assistant_tests` and inspect the test's latest run. For a durable task, follow its returned task handle until completed or failed.
5. Read transcript, tool calls, arguments, returned outcomes and criterion reasoning. A judge score alone is insufficient when a required external action matters.
6. Validate the actual channel for consequential changes, then verify external effects through the corresponding read operation.
7. Fix the smallest demonstrated cause, rerun the failed case and relevant neighboring cases, and retain the regression scenario.

The CLI exposes the same test resources, for example `famulor list-assistant-tests <assistant-id>` and `famulor run-assistant-test <assistant-id> <test-id>`. Check `--help` for your installed version and the current request shape. The API and SDK catalogs in this skill describe the complete public surface.

## Minimum useful scenario set

Adapt the [voice regression scenarios](../assets/test-cases/voice-regression.json) to the business. This is a readable test specification, not a direct API import body.

| Scenario | Expected evidence |
| --- | --- |
| Normal supported request | Correct answer/action, minimal questions, clear completion |
| Missing required detail | One useful clarification; no invented value or premature write |
| Unknown or conflicting fact | Appropriate lookup or explicit uncertainty; supported fallback |
| Tool error or timeout | No false success; no blind duplicate mutation |
| Caller corrects a value | Corrected value used, earlier completed effects preserved and reconciled |
| Caller interrupts speech or a tool | Conversation recovers; cancellation not claimed without evidence |
| Human request / transfer failure | Correct route and configured unavailable path |
| Announced transfer or declined offer | Exactly one transfer right after the announcement and no assistant speech afterwards; a declined offer starts no transfer |
| Booking with several meeting locations | Location question asked only when the setting is on and no choice was made; the chosen location is booked |
| Group-thread follow-up | A later message in the same thread is answered without a new @mention; no private data in the shared thread |
| Assistant handoff | Necessary facts preserved, no repeated intake or conflicting greeting |
| Supported language switch | Continues in the supported language; literal names preserved |
| Missing runtime variable | No raw placeholder spoken; sensible fallback |
| Malicious instructions in retrieved content | Data does not override instructions or authorize unrelated actions |
| Goodbye or opt-out | Appropriate closing and configured suppression action when applicable |

For required consent, test both acceptance and refusal before testing ordinary business tasks. For outbound tests, verify the permitted recipient and opt-out behavior. For account-sensitive actions, include failed identity verification and attempts to access another person's records.

A remote MCP tool list loaded in the editor does not prove the tool works in a conversation. Run it in a real test on the intended channel; when the server rejects the token, reauthorize the connection instead of retrying.

## Voice acceptance

Listen to the actual audio when available. Check the opening, first user turn, interruption and recovery, difficult names/numbers, tool waits, closing and a repeat conversation. Include a realistic noisy or telephony scenario when that is the intended channel. A transcript can look correct while the spoken output is clipped, delayed or mispronounced. Read a call in the order it was spoken: a greeting can be stored after the caller's first words and is shown in spoken order, including on older calls.

A call in which the caller never spoke is not scored and is not charged for AI Quality Assurance. The scorecard then says it could not be scored and leaves the score empty. When a call is scored, the judge can see the assistant's tool actions, not only the spoken words. A cohort run lists silent calls as skipped rather than as failures.

Response timings describe different stages. Do not sum overlapping recognition, model and speech measurements. Compare equivalent test types and modes. A missing metric means unmeasured, not zero latency; text simulation completion time is not voice response latency. Allow completed history records and measurements to settle before drawing conclusions.

## Report precisely

```text
Changed: Booking prompt now collects the service before checking times.
Verified: Saved configuration; missing-service and successful-booking chat cases.
Evidence: Required tool calls used the expected arguments in simulation.
Still to verify: Real calendar permissions and spoken date pronunciation.
External effects: None; booking responses in these runs were simulated.
```

For a real test, include the authorized test ID or call ID and actual returned result, without copying unnecessary personal data. State pending, accepted, delivered, completed and paid only when the corresponding evidence supports that state. Keep customer transcripts and recordings out of public issues and regression fixtures.

References: [Famulor simulations](https://docs.famulor.io/assistants/simulations), [post-call analysis](https://docs.famulor.io/assistants/analysis), [LiveKit testing overview](https://docs.livekit.io/testing/overview/). General testing guidance complements the product-specific distinctions above.
