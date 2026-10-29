# Calls API operations

Reviewed 2026-10-29. 13 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `createCall` | `POST /calls` | `famulor create-call` | [Start an outbound call](https://docs.famulor.io/api-reference/calls/start-an-outbound-call) |
| `getCall` | `GET /calls/{id}` | `famulor get-call` | [Get a call](https://docs.famulor.io/api-reference/calls/get-a-call) |
| `getCallBrowserRecording` | `GET /calls/{id}/browser-recordings/{recordingId}` | `famulor get-call-browser-recording` | [Download a browser video](https://docs.famulor.io/api-reference/calls/browser-recording) |
| `getCallBrowserSession` | `GET /calls/{id}/browser-session` | `famulor get-call-browser-session` | [Get the live browser view](https://docs.famulor.io/api-reference/calls/browser-session) |
| `getCallRecording` | `GET /calls/{id}/recording` | `famulor get-call-recording` | [Get a call recording URL](https://docs.famulor.io/api-reference/calls/get-a-call-recording-url) |
| `getMessagingBrowserRecording` | `GET /history/messaging/{id}/browser-recordings/{recordingId}` | `famulor get-messaging-browser-recording` | [Download a browser video](https://docs.famulor.io/api-reference/calls/messaging-browser-recording) |
| `listCallBrowserRecordings` | `GET /calls/{id}/browser-recordings` | `famulor list-call-browser-recordings` | [List browser videos](https://docs.famulor.io/api-reference/calls/browser-recordings) |
| `listCalls` | `GET /calls` | `famulor list-calls` | [List calls](https://docs.famulor.io/api-reference/calls/list-calls) |
| `listMessagingBrowserRecordings` | `GET /history/messaging/{id}/browser-recordings` | `famulor list-messaging-browser-recordings` | [List browser videos](https://docs.famulor.io/api-reference/calls/messaging-browser-recordings) |
| `liveCallControl` | `POST /calls/{id}/live-control` | `famulor live-call-control` | [Live call control](https://docs.famulor.io/api-reference/calls/live-call-control) |
| `runCallActions` | `POST /calls/actions` | `famulor run-call-actions` | [Run call history actions](https://docs.famulor.io/api-reference/calls/run-call-history-actions) |
| `startWhatsAppOutboundCall` | `POST /calls/whatsapp-outbound` | `famulor start-whatsapp-outbound-call` | [Start outbound WhatsApp voice call](https://docs.famulor.io/api-reference/calls/start-outbound-whatsapp-voice-call) |
| `verifyCallInputs` | `POST /calls/{id}/verify-inputs` | `famulor verify-call-inputs` | [Verify call inputs](https://docs.famulor.io/api-reference/calls/verify-call-inputs) |
